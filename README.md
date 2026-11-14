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

## Latest list — 2026-11-14 17:20 UTC

New charts added between 2026-11-14 16:19 UTC and 2026-11-14 17:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-14T17-20-07-736884Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-14 16:32:32 | [cdi-operator](https://artifacthub.io/packages/helm/quench-cdi-operator/cdi-operator) | quench-cdi-operator | 0.0.1 | KubeVirt Containerized Data Importer (CDI) through its operator: DataVolumes im… |
| 2026-11-14 16:32:36 | [goalert](https://artifacthub.io/packages/helm/quench-goalert/goalert) | quench-goalert | 0.0.1 | GoAlert: on-call scheduling, automated escalations and notifications (SMS, voic… |
| 2026-11-14 16:32:41 | [node-feature-discovery](https://artifacthub.io/packages/helm/quench-node-feature-discovery/node-feature-discovery) | quench-node-feature-dis… | 0.0.1 | Node Feature Discovery: label Kubernetes nodes with their CPU, kernel, PCI, USB… |
| 2026-11-14 16:32:46 | [tidb-operator](https://artifacthub.io/packages/helm/quench-tidb-operator/tidb-operator) | quench-tidb-operator | 0.0.1 | TiDB Operator: runs TiDB clusters (PD, TiKV and the MySQL-compatible TiDB serve… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
