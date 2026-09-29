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

## Latest list — 2026-09-29 03:22 UTC

New charts added between 2026-09-29 02:22 UTC and 2026-09-29 03:22 UTC.

[Full CSV](data/new-helm-charts-2026-09-29T03-22-39-843663Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-29 02:23:13 | [kodbox](https://artifacthub.io/packages/helm/kodbox/kodbox) | kodbox | 0.2.0 | Kodbox web file manager with MariaDB, Redis, KodOffice and Imaginary |
| 2026-09-29 02:31:15 | [helm-guestbook](https://artifacthub.io/packages/helm/helm-guestbook-demo/helm-guestbook) | helm-guestbook-demo | 0.1.0 | A Helm chart for Kubernetes |
| 2026-09-29 02:39:34 | [conversor-temperatura](https://artifacthub.io/packages/helm/conversor-temperatura/conversor-temperatura) | conversor-temperatura | 0.1.0 | A Helm chart for Kubernetes |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
