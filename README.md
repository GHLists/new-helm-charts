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

## Latest list — 2026-09-28 10:25 UTC

New charts added between 2026-09-28 09:22 UTC and 2026-09-28 10:25 UTC.

[Full CSV](data/new-helm-charts-2026-09-28T10-25-50-328301Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-28 09:33:04 | [metabase](https://artifacthub.io/packages/helm/quench-metabase/metabase) | quench-metabase | 0.0.1 | Metabase open-source edition: self-service BI and dashboards, with its applicat… |
| 2026-09-28 10:04:00 | [activemq-artemis](https://artifacthub.io/packages/helm/quench-activemq-artemis/activemq-artemis) | quench-activemq-artemis | 0.0.1 | Apache Artemis (formerly ActiveMQ Artemis), the multi-protocol Java message bro… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
