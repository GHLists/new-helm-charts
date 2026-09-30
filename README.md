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

## Latest list — 2026-09-30 16:22 UTC

New charts added between 2026-09-30 15:21 UTC and 2026-09-30 16:22 UTC.

[Full CSV](data/new-helm-charts-2026-09-30T16-22-51-49869Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-30 15:36:23 | [seowebchecker](https://artifacthub.io/packages/helm/seowebchecker/seowebchecker) | seowebchecker | 1.0.0 | Enterprise Kubernetes Helm Chart for automated continuous technical SEO auditin… |
| 2026-09-30 15:37:02 | [victoria-traces-mcp](https://artifacthub.io/packages/helm/victoriametrics/victoria-traces-mcp) | victoriametrics | 0.1.0 | A Helm chart for VictoriaTraces MCP server |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
