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

## Latest list — 2026-11-16 07:19 UTC

New charts added between 2026-11-16 06:21 UTC and 2026-11-16 07:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-16T07-19-50-118535Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-16 06:21:27 | [snipe-it](https://artifacthub.io/packages/helm/quench-snipe-it/snipe-it) | quench-snipe-it | 0.0.1 | Snipe-IT: IT asset management for hardware, licenses, accessories and consumabl… |
| 2026-11-16 06:50:47 | [koel](https://artifacthub.io/packages/helm/quench-koel/koel) | quench-koel | 0.0.1 | Koel: a personal music streaming server with a web player, playlists, podcasts… |
| 2026-11-16 07:15:39 | [lychee](https://artifacthub.io/packages/helm/quench-lychee/lychee) | quench-lychee | 0.0.1 | Lychee: photo management with albums, sharing, smart albums, EXIF and map views… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
