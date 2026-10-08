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

## Latest list — 2026-10-08 16:21 UTC

New charts added between 2026-10-08 15:19 UTC and 2026-10-08 16:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-08T16-21-57-798851Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-08 16:00:41 | [kratix](https://artifacthub.io/packages/helm/syntasso/kratix) | syntasso | 0.0.1 | A Helm chart for installing Kratix (https://kratix.io) |
| 2026-10-08 16:04:03 | [mongodb-exporter](https://artifacthub.io/packages/helm/quench-mongodb-exporter/mongodb-exporter) | quench-mongodb-exporter | 0.0.1 | Prometheus exporter for MongoDB (Percona's): server status, replica set, databa… |
| 2026-10-08 16:04:03 | [mysqld-exporter](https://artifacthub.io/packages/helm/quench-mysqld-exporter/mysqld-exporter) | quench-mysqld-exporter | 0.0.2 | Prometheus exporter for MySQL and MariaDB: server status, InnoDB, replication a… |
| 2026-10-08 16:04:03 | [node-exporter](https://artifacthub.io/packages/helm/quench-node-exporter/node-exporter) | quench-node-exporter | 0.0.2 | Prometheus node_exporter as a DaemonSet: CPU, memory, disk, filesystem, network… |
| 2026-10-08 16:04:05 | [postgres-exporter](https://artifacthub.io/packages/helm/quench-postgres-exporter/postgres-exporter) | quench-postgres-exporter | 0.0.1 | Prometheus exporter for PostgreSQL: server, database, replication, lock and sta… |
| 2026-10-08 16:04:05 | [redis-exporter](https://artifacthub.io/packages/helm/quench-redis-exporter/redis-exporter) | quench-redis-exporter | 0.0.2 | Prometheus exporter for Redis and Valkey: memory, clients, keyspace, replicatio… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
