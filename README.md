# New Helm charts

Hourly lists of charts newly added to
[ArtifactHub](https://artifacthub.io/), the discovery hub for cloud-native
packages. Charts are read from the [ArtifactHub search API](
https://artifacthub.io/docs/api/) sorted by last update; because the results
carry no creation timestamp, each candidate is checked against its package
detail endpoint, whose earliest chart version timestamp decides whether the
chart was newly tracked by ArtifactHub inside the window (a first release or
a first sync of the chart).
A GitHub Actions workflow runs every hour, fetches the charts added since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-helm-charts-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 12:23 UTC

New charts added between 2026-10-07 11:20 UTC and 2026-10-07 12:23 UTC.

[Full CSV](data/new-helm-charts-2026-10-07T12-23-02-961Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-07 11:43:25 | [panopticum](https://artifacthub.io/packages/helm/panopticum/panopticum) | panopticum | 1.0.11 | A tool for developers and QA — web interface for viewing and managing database… |
| 2026-10-07 11:44:41 | [opensearch-dashboards](https://artifacthub.io/packages/helm/quench-opensearch-dashboards/opensearch-dashboards) | quench-opensearch-dashb… | 0.0.1 | OpenSearch Dashboards, the web UI for OpenSearch search, dashboards and visuali… |
| 2026-10-07 12:03:43 | [search-stack](https://artifacthub.io/packages/helm/quench-search-stack/search-stack) | quench-search-stack | 0.0.2 | Hardened search with a UI in one install: OpenSearch (search and analytics engi… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
