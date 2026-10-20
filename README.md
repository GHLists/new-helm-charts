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

## Latest list — 2026-10-20 20:21 UTC

New charts added between 2026-10-20 19:19 UTC and 2026-10-20 20:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-20T20-21-07-596693Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-20 19:50:01 | [galaxy-k8s-monitor](https://artifacthub.io/packages/helm/cloudve/galaxy-k8s-monitor) | cloudve | 0.1.1 | Real-time Kubernetes pod resource monitor for Galaxy namespaces |
| 2026-10-20 20:02:26 | [powerdns](https://artifacthub.io/packages/helm/unxwares/powerdns) | unxwares | 2026.10.1 | PowerDNS Authoritative Server with its REST API, SQLite/PostgreSQL/MySQL backen… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
