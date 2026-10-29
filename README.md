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

## Latest list — 2026-10-29 19:21 UTC

New charts added between 2026-10-29 18:21 UTC and 2026-10-29 19:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-29T19-21-37-311711Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-29 18:31:44 | [k-watch](https://artifacthub.io/packages/helm/k-watch/k-watch) | k-watch | 0.1.1 | Read-only Kubernetes dashboard that maps how resources in a namespace connect a… |
| 2026-10-29 19:01:47 | [cosmos-dashboard](https://artifacthub.io/packages/helm/cosmos-dashboard/cosmos-dashboard) | cosmos-dashboard | 1.0.2 | A Kubernetes cluster inventory and image security dashboard |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
