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

## Latest list — 2026-11-14 14:21 UTC

New charts added between 2026-11-14 13:19 UTC and 2026-11-14 14:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-14T14-21-56-356592Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-14 13:22:08 | [t-rex](https://artifacthub.io/packages/helm/t-rex/t-rex) | t-rex | 1.0.1 | Helm chart for t-rex, a web app and API to track working time |
| 2026-11-14 13:50:23 | [dev-platform-stack](https://artifacthub.io/packages/helm/quench-dev-platform-stack/dev-platform-stack) | quench-dev-platform-sta… | 0.0.1 | Forgejo (Git hosting) with Woodpecker CI, PostgreSQL and Valkey: repositories,… |
| 2026-11-14 14:03:37 | [bi-stack](https://artifacthub.io/packages/helm/quench-bi-stack/bi-stack) | quench-bi-stack | 0.0.1 | Metabase (dashboards and questions) with ClickHouse (columnar analytics databas… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
