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

## Latest list — 2026-11-12 22:21 UTC

New charts added between 2026-11-12 21:20 UTC and 2026-11-12 22:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-12T22-21-18-277476Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-12 21:30:31 | [bucket-backup-restore](https://artifacthub.io/packages/helm/bucket-backup-restore/bucket-backup-restore) | bucket-backup-restore | 2.0.0 | Scheduled backups of S3-compatible buckets (or any rclone remote) into encrypte… |
| 2026-11-12 21:32:25 | [postgresql-backup-restore](https://artifacthub.io/packages/helm/postgresql-backup-restore/postgresql-backup-restore) | postgresql-backup-resto… | 3.0.0 | Scheduled PostgreSQL backups (pg_dump) to S3-compatible storage with encryption… |
| 2026-11-12 21:32:32 | [bookstack](https://artifacthub.io/packages/helm/quench-bookstack/bookstack) | quench-bookstack | 0.0.1 | BookStack: a wiki and documentation platform (shelves, books, chapters, pages)… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
