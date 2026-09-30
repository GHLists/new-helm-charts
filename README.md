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

## Latest list — 2026-09-30 00:19 UTC

New charts added between 2026-09-29 23:20 UTC and 2026-09-30 00:19 UTC.

[Full CSV](data/new-helm-charts-2026-09-30T00-19-45-677118Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-29 23:23:26 | [qrcode-generator](https://artifacthub.io/packages/helm/qrcode-generator/qrcode-generator) | qrcode-generator | 0.1.0 | A Helm chart for Kubernetes |
| 2026-09-29 23:23:32 | [conversor-temperatura](https://artifacthub.io/packages/helm/conversor-temperatura/conversor-temperatura) | conversor-temperatura | 0.1.0 | A Helm chart for Kubernetes |
| 2026-09-29 23:23:37 | [db-connection-test](https://artifacthub.io/packages/helm/db-connection-test/db-connection-test) | db-connection-test | 0.1.0 | A Helm chart for Kubernetes |
| 2026-09-29 23:23:42 | [app-movies-series](https://artifacthub.io/packages/helm/app-movies-series/app-movies-series) | app-movies-series | 0.1.0 | A Helm chart for Kubernetes |
| 2026-09-29 23:23:49 | [landing-page](https://artifacthub.io/packages/helm/landing-page/landing-page) | landing-page | 0.1.0 | A Helm chart for Kubernetes |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
