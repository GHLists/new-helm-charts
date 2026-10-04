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

## Latest list — 2026-10-04 19:22 UTC

New charts added between 2026-10-04 18:20 UTC and 2026-10-04 19:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-04T19-22-22-694319Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-04 18:44:46 | [zabbix](https://artifacthub.io/packages/helm/quench-zabbix/zabbix) | quench-zabbix | 0.0.1 | Zabbix, the enterprise monitoring platform: the server, the web frontend and Po… |
| 2026-10-04 18:49:42 | [ms-filestorage-grpc](https://artifacthub.io/packages/helm/codedesignplus-charts/ms-filestorage-grpc) | codedesignplus-charts | 0.0.24 | This is a Helm chart for the ms-filestorage-gRPC service |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
