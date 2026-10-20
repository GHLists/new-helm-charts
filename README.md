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

## Latest list — 2026-10-20 17:19 UTC

New charts added between 2026-10-20 16:22 UTC and 2026-10-20 17:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-20T17-19-48-323164Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-20 16:28:48 | [transmute](https://artifacthub.io/packages/helm/helmforge/transmute) | helmforge | 1.0.0 | Production-ready Helm chart for Transmute, a self-hosted audio and video transc… |
| 2026-10-20 16:36:29 | [paperless-ngx](https://artifacthub.io/packages/helm/cfi2017/paperless-ngx) | cfi2017 | 0.1.0 | A document management system that transforms physical documents into a searchab… |
| 2026-10-20 16:53:48 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
