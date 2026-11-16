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

## Latest list — 2026-11-16 12:21 UTC

New charts added between 2026-11-16 11:20 UTC and 2026-11-16 12:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-16T12-21-57-355859Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-16 11:23:56 | [rocketmq-dashboard](https://artifacthub.io/packages/helm/logic3579/rocketmq-dashboard) | logic3579 | 3.0.0 | A Helm chart for RocketMQ Studio 3.x, the Apache RocketMQ management console |
| 2026-11-16 11:51:04 | [komga](https://artifacthub.io/packages/helm/quench-komga/komga) | quench-komga | 0.0.1 | Komga: media server for comics, manga, BDs and ebooks with a web reader, OPDS a… |
| 2026-11-16 12:21:44 | [rss-bridge](https://artifacthub.io/packages/helm/quench-rss-bridge/rss-bridge) | quench-rss-bridge | 0.0.1 | RSS-Bridge: Atom, JSON and other feeds for sites that have none, with 400+ brid… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
