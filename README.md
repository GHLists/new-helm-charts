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

## Latest list — 2026-11-01 22:19 UTC

New charts added between 2026-11-01 21:20 UTC and 2026-11-01 22:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-01T22-19-48-977222Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-01 21:58:38 | [freescout](https://artifacthub.io/packages/helm/l4g/freescout) | l4g | 0.1.0 | A Helm chart for Kubernetes |
| 2026-11-01 21:58:38 | [inbox-zero](https://artifacthub.io/packages/helm/l4g/inbox-zero) | l4g | 0.1.0 | Helm chart for Inbox Zero — an open-source AI email assistant (web, BullMQ work… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
