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

## Latest list — 2026-11-17 09:21 UTC

New charts added between 2026-11-17 08:21 UTC and 2026-11-17 09:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-17T09-21-27-770498Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-17 08:30:11 | [krci-cache](https://artifacthub.io/packages/helm/epmdedp/krci-cache) | epmdedp | 0.5.0 | A Helm chart for KubeRocketCI Cache, an HTTP cache for Tekton pipeline artifacts |
| 2026-11-17 08:44:44 | [backup-operator](https://artifacthub.io/packages/helm/janip81-helm-charts/backup-operator) | janip81-helm-charts | 0.4.0 | Kubernetes operator that backs up PersistentVolume data as versioned, encrypted… |
| 2026-11-17 09:04:07 | [paperless-ngx](https://artifacthub.io/packages/helm/quench-paperless-ngx/paperless-ngx) | quench-paperless-ngx | 0.0.1 | Paperless-ngx: scan, OCR, index and archive your documents, on the bundled Post… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
