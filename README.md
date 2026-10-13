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

## Latest list — 2026-10-13 08:22 UTC

New charts added between 2026-10-13 07:19 UTC and 2026-10-13 08:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-13T08-22-40-922689Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-13 07:49:20 | [convertigo](https://artifacthub.io/packages/helm/convertigo/convertigo) | convertigo | 8.4.6 | The Convertigo Low Code / No Code Platform running on Kubernetes |
| 2026-10-13 08:11:37 | [grist](https://artifacthub.io/packages/helm/quench-grist/grist) | quench-grist | 0.0.2 | Grist, the self-hosted spreadsheet-database with Python formulas run in a pyodi… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
