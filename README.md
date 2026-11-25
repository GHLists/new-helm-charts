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

## Latest list — 2026-11-25 03:19 UTC

New charts added between 2026-11-25 02:20 UTC and 2026-11-25 03:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-25T03-19-37-673421Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-25 03:03:32 | [dashy](https://artifacthub.io/packages/helm/quench-dashy/dashy) | quench-dashy | 0.0.1 | Dashy: a self-hosted start page and dashboard with widgets, status checks, them… |
| 2026-11-25 03:03:41 | [pgadmin4](https://artifacthub.io/packages/helm/quench-pgadmin4/pgadmin4) | quench-pgadmin4 | 0.0.1 | pgAdmin 4: the web administration and development platform for PostgreSQL (quer… |
| 2026-11-25 03:03:41 | [postgres-operator](https://artifacthub.io/packages/helm/quench-postgres-operator/postgres-operator) | quench-postgres-operator | 0.0.1 | Zalando Postgres Operator: highly available PostgreSQL clusters on Patroni from… |
| 2026-11-25 03:03:42 | [radicale](https://artifacthub.io/packages/helm/quench-radicale/radicale) | quench-radicale | 0.0.1 | Radicale: a small CalDAV and CardDAV server for calendars, task lists and conta… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
