#!/usr/bin/env python3
"""Fetch Helm charts newly added to ArtifactHub.

New charts are read from the [ArtifactHub API](https://artifacthub.io/docs/api/)
search endpoint sorted by last update. Because the search results do not carry
a creation timestamp, every repository/chart pair seen in the window is
checked against its package detail endpoint, whose earliest chart version
timestamp decides whether the chart was newly tracked by ArtifactHub inside
the requested window (first release or first sync of the chart).

The search is capped by pagination, so the manifest records
``source_truncated`` whenever the page limit is reached before the requested
window is covered.

The end of the last list is stored in the manifest so the next run resumes
where the previous one stopped.
"""

import argparse
import csv
import datetime as dt
import http.client
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SEARCH_URL = (
    "https://artifacthub.io/api/v1/packages/search"
    "?kind=0&facets=false&sort=last_updated&limit=60"
)
PACKAGE_URL = "https://artifacthub.io/api/v1/packages/helm/{repo}/{name}"
DEFAULT_USER_AGENT = (
    "new-helm-charts/1.0 (https://github.com/GHLists/new-helm-charts)"
)

MAX_PAGES = 15
PAGE_SIZE = 60
WORKERS = 6
DESCRIPTION_LIMIT = 300
CSV_HEADER = (
    "created_at",
    "chart",
    "repository",
    "version",
    "description",
)

TRANSIENT_ERRORS = (
    urllib.error.URLError,
    TimeoutError,
    json.JSONDecodeError,
    http.client.HTTPException,
    OSError,
)


class NotFound(Exception):
    pass


def iso(moment):
    moment = moment.astimezone(dt.timezone.utc)
    if moment.microsecond:
        fraction = f"{moment.microsecond:06d}".rstrip("0")
        return moment.strftime("%Y-%m-%dT%H:%M:%S") + f".{fraction}Z"
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_timestamp_epoch(value):
    return dt.datetime.fromtimestamp(int(value), dt.timezone.utc)


def parse_timestamp(value):
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    moment = dt.datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=dt.timezone.utc)
    return moment.astimezone(dt.timezone.utc)


def timestamp_filename(moment):
    moment = moment.astimezone(dt.timezone.utc)
    stamp = moment.strftime("%Y-%m-%dT%H-%M-%S")
    if moment.microsecond:
        stamp += "-" + f"{moment.microsecond:06d}".rstrip("0")
    return stamp + "Z"


def fetch_json(url, user_agent, retries=3, backoff=5.0):
    last_error = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            url,
            headers={"User-Agent": user_agent, "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 404:
                raise NotFound(url) from error
            last_error = error
        except TRANSIENT_ERRORS as error:
            last_error = error
        if attempt < retries:
            print(f"attempt {attempt} failed ({last_error}), retrying", file=sys.stderr)
            time.sleep(backoff * attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def clean_text(value, limit=DESCRIPTION_LIMIT):
    text = " ".join(str(value or "").split())
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "\u2026"
    return text


def collect_search_hits(user_agent, retries, api_delay, since, until):
    """Return (repo, name) pairs whose last update falls in the window."""
    hits = []
    seen = set()
    offset = 0
    while offset < MAX_PAGES * PAGE_SIZE:
        data = fetch_json(f"{SEARCH_URL}&offset={offset}", user_agent, retries=retries)
        packages = data.get("packages")
        if not isinstance(packages, list):
            raise RuntimeError("search response does not contain packages")
        if not packages:
            break
        oldest = None
        for package in packages:
            if not isinstance(package, dict):
                continue
            repository = (package.get("repository") or {}).get("name") or ""
            name = package.get("name") or ""
            key = (repository, name)
            if not name or key in seen:
                continue
            seen.add(key)
            ts = package.get("ts")
            try:
                updated = parse_timestamp_epoch(ts)
            except (TypeError, ValueError, OSError):
                continue
            if updated > until:
                continue
            if updated <= since:
                oldest = updated
                continue
            hits.append(key)
        if oldest is not None:
            return hits, True
        if len(packages) < PAGE_SIZE:
            return hits, True
        offset += PAGE_SIZE
        time.sleep(api_delay)
    return hits, False


def chart_row(repo, name, user_agent, retries, since, until):
    """Check the package detail endpoint and build a row, or a status.

    Statuses: ``ok`` (chart newly tracked in the window), ``old`` (chart was
    tracked before the window), ``empty`` (no usable timestamps), ``missing``
    (no package detail).
    """
    url = PACKAGE_URL.format(
        repo=urllib.parse.quote(repo, safe=""),
        name=urllib.parse.quote(name, safe=""),
    )
    try:
        detail = fetch_json(url, user_agent, retries=retries)
    except NotFound:
        return "missing", None
    versions = detail.get("available_versions")
    if not isinstance(versions, list) or not versions:
        return "empty", None
    times = []
    for version in versions:
        if not isinstance(version, dict):
            continue
        ts = version.get("ts")
        if ts:
            try:
                times.append(parse_timestamp_epoch(ts))
            except (TypeError, ValueError, OSError):
                continue
    if not times:
        return "empty", None
    first = min(times)
    if not (since < first <= until):
        return "old", None
    latest = max(
        (version for version in versions if isinstance(version, dict)),
        key=lambda version: version.get("ts") or 0,
    )
    return "ok", {
        "created_at": iso(first),
        "chart": name,
        "repository": repo,
        "version": clean_text(latest.get("version") or detail.get("version"), 20),
        "description": clean_text(detail.get("description")),
    }


def write_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_HEADER)
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, path)


def read_manifest_text(path):
    """Read the manifest from disk, or fall back to the committed copy.

    The workflow checks out only ``scripts`` from the repository, so the
    manifest can be missing from the working tree even though it is committed.
    """
    manifest_path = Path(path)
    try:
        return manifest_path.read_text(encoding="utf-8")
    except OSError:
        pass
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{manifest_path.as_posix()}"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout


def load_manifest(path):
    text = read_manifest_text(path)
    if text is None:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"manifest {path} is not valid JSON") from error
    if not isinstance(data, dict):
        raise RuntimeError(f"manifest {path} must contain a JSON object")
    version = data.get("state_version", 1)
    if version != 1:
        raise RuntimeError(f"manifest {path} has an unsupported state version")
    return data


def save_manifest(path, manifest):
    manifest_path = Path(path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = manifest_path.with_name(f".{manifest_path.name}.tmp")
    text = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, manifest_path)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        help="UTC start timestamp as ISO 8601 (default: end of the last list)",
    )
    parser.add_argument(
        "--until",
        help="UTC end timestamp as ISO 8601 (default: now)",
    )
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--manifest", default="latest.json")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument(
        "--lookback-hours",
        type=float,
        default=1.0,
        help="window length when no previous list exists (default: 1)",
    )
    parser.add_argument(
        "--api-delay",
        type=float,
        default=0.3,
        help="seconds between ArtifactHub API requests (default: 0.3)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    now = dt.datetime.now(dt.timezone.utc)
    until = parse_timestamp(args.until) if args.until else now
    manifest = load_manifest(args.manifest)

    if args.since:
        since = parse_timestamp(args.since)
        if "window" in manifest:
            stored_window = parse_timestamp(manifest["window"])
            if since < stored_window:
                raise RuntimeError(
                    "backfill would move the window backwards; "
                    f"the manifest window is {iso(stored_window)}"
                )
    elif "window" in manifest:
        since = parse_timestamp(manifest["window"])
    else:
        since = until - dt.timedelta(hours=args.lookback_hours)

    hits, covered = collect_search_hits(
        args.user_agent, args.retries, args.api_delay, since, until
    )
    truncated = not covered
    if truncated:
        print(
            "search pagination cap reached before the window was covered; "
            "some charts in this window may be missing",
            file=sys.stderr,
        )

    rows = []
    skipped = 0
    statuses = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {
            key: pool.submit(
                chart_row, key[0], key[1], args.user_agent, args.retries, since, until
            )
            for key in sorted(hits)
        }
        for key, future in futures.items():
            try:
                status, row = future.result()
            except RuntimeError as error:
                print(f"failed to check {key}: {error}", file=sys.stderr)
                statuses[key] = "error"
                skipped += 1
                continue
            statuses[key] = status
            if status == "ok":
                rows.append(row)
            else:
                skipped += 1
    counts = {}
    for status in statuses.values():
        counts[status] = counts.get(status, 0) + 1
    print(f"checked {len(statuses)} charts: {counts}", file=sys.stderr)

    rows.sort(key=lambda row: row["created_at"])
    manifest["window"] = iso(until)
    manifest["source_truncated"] = bool(truncated)
    if rows:
        output = (
            Path(args.output_dir) / f"new-helm-charts-{timestamp_filename(until)}.csv"
        )
        write_csv(output, rows)
        manifest["list"] = {
            "path": output.as_posix(),
            "from": iso(since),
            "to": iso(until),
            "count": len(rows),
        }
        print(
            f"wrote {len(rows)} charts created between {iso(since)} "
            f"and {iso(until)} to {output}"
        )
    else:
        print(f"no new charts between {iso(since)} and {iso(until)}")
    save_manifest(args.manifest, manifest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
