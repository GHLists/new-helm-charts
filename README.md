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

## Latest list — 2026-11-15 04:18 UTC

New charts added between 2026-11-15 03:21 UTC and 2026-11-15 04:18 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T04-18-50-798671Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 03:31:14 | [honeybeepf-llm](https://artifacthub.io/packages/helm/honeybeepf-llm/honeybeepf-llm) | honeybeepf-llm | 0.3.2 | Count LLM API tokens and USD cost per Kubernetes pod and workload with eBPF, wi… |
| 2026-11-15 03:50:31 | [yarr](https://artifacthub.io/packages/helm/quench-yarr/yarr) | quench-yarr | 0.0.1 | yarr: a self-hosted RSS and Atom reader with a web UI and a Fever API for mobil… |
| 2026-11-15 04:09:32 | [gokapi](https://artifacthub.io/packages/helm/quench-gokapi/gokapi) | quench-gokapi | 0.0.1 | Gokapi: lightweight self-hosted file sharing with expiring links, download limi… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
