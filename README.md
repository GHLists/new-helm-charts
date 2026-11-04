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

## Latest list — 2026-11-04 12:21 UTC

New charts added between 2026-11-04 10:18 UTC and 2026-11-04 12:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-04T12-21-34-713761Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-04 11:03:43 | [prometheus-mcp-server](https://artifacthub.io/packages/helm/prometheus-mcp-server/prometheus-mcp-server) | prometheus-mcp-server | 1.1.1 | A Helm chart for deploying the Prometheus MCP Server to Kubernetes |
| 2026-11-04 11:04:58 | [panopticum](https://artifacthub.io/packages/helm/panopticum/panopticum) | panopticum | 1.0.13 | A tool for developers and QA — web interface for viewing and managing database… |
| 2026-11-04 11:30:11 | [arkeep](https://artifacthub.io/packages/helm/arkeep/arkeep) | arkeep | 0.10.0 | Centralized backup management for self-hosted infrastructure |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
