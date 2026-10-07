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

## Latest list — 2026-10-07 16:23 UTC

New charts added between 2026-10-07 15:19 UTC and 2026-10-07 16:23 UTC.

[Full CSV](data/new-helm-charts-2026-10-07T16-23-07-693049Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-07 15:32:44 | [mysql-ha-stack](https://artifacthub.io/packages/helm/quench-mysql-ha-stack/mysql-ha-stack) | quench-mysql-ha-stack | 0.0.2 | Operator-managed HA MySQL-compatible database in one install: MariaDB Operator… |
| 2026-10-07 15:56:10 | [smtp2x](https://artifacthub.io/packages/helm/jfwenisch/smtp2x) | jfwenisch | 0.5.3 | SMTP notifications to GitLab issues and webhooks |
| 2026-10-07 15:59:18 | [signal-cli-rest-api](https://artifacthub.io/packages/helm/leprechaun-charts/signal-cli-rest-api) | leprechaun-charts | 0.1.3 | A Helm chart for Kubernetes |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
