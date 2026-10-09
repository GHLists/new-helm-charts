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

## Latest list — 2026-10-09 12:19 UTC

New charts added between 2026-10-09 11:21 UTC and 2026-10-09 12:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-09T12-19-33-64972Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-09 11:28:16 | [mo-backup](https://artifacthub.io/packages/helm/mogenius/mo-backup) | mogenius | 1.0.29 | This is the mogenius backup script. |
| 2026-10-09 11:42:42 | [mo-backup-mysql](https://artifacthub.io/packages/helm/mogenius/mo-backup-mysql) | mogenius | 1.0.29 | This is the mogenius backup script. |
| 2026-10-09 11:59:24 | [domain-locker](https://artifacthub.io/packages/helm/domain-locker/domain-locker) | domain-locker | 0.3.2 | A Helm chart for deploying Domain Locker |
| 2026-10-09 12:01:12 | [arith](https://artifacthub.io/packages/helm/arith/arith) | arith | 1.0.0 | Integer arithmetic over HTTP. Four endpoints, a page, metrics, traces and logs. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
