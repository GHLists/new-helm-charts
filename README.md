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

## Latest list — 2026-09-27 12:20 UTC

New charts added between 2026-09-27 11:20 UTC and 2026-09-27 12:20 UTC.

[Full CSV](data/new-helm-charts-2026-09-27T12-20-16-566274Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-27 12:01:57 | [fauxgpu](https://artifacthub.io/packages/helm/fauxgpu/fauxgpu) | fauxgpu | 0.2.2 | Simulate a real GPU datacenter with zero GPUs — real Kubernetes GPU-resource sc… |
| 2026-09-27 12:09:51 | [proxysql](https://artifacthub.io/packages/helm/quench-proxysql/proxysql) | quench-proxysql | 0.0.2 | ProxySQL, the MySQL-protocol proxy: connection pooling, read/write splitting, q… |
| 2026-09-27 12:09:51 | [squid](https://artifacthub.io/packages/helm/quench-squid/squid) | quench-squid | 0.0.1 | Squid, the caching forward proxy for HTTP and HTTPS (CONNECT). Pods reach the o… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
