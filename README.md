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

## Latest list — 2026-11-12 16:21 UTC

New charts added between 2026-11-12 15:21 UTC and 2026-11-12 16:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-12T16-21-57-366826Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-12 16:03:48 | [glance](https://artifacthub.io/packages/helm/quench-glance/glance) | quench-glance | 0.0.1 | Glance: a self-hosted dashboard that puts feeds, bookmarks, releases, weather a… |
| 2026-11-12 16:03:50 | [owncast](https://artifacthub.io/packages/helm/quench-owncast/owncast) | quench-owncast | 0.0.1 | Owncast: self-hosted live video streaming and chat (RTMP in, HLS out, web playe… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
