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

## Latest list — 2026-11-26 14:21 UTC

New charts added between 2026-11-26 13:21 UTC and 2026-11-26 14:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-26T14-21-46-425979Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-26 13:37:13 | [mysql-innodbcluster](https://artifacthub.io/packages/helm/mysql-operator/mysql-innodbcluster) | mysql-operator | 2.3.2 | MySQL InnoDB Cluster Helm Chart for deploying MySQL InnoDB Cluster in Kubernetes |
| 2026-11-26 13:37:13 | [mysql-operator](https://artifacthub.io/packages/helm/mysql-operator/mysql-operator) | mysql-operator | 2.3.2 | MySQL Operator Helm Chart for deploying MySQL InnoDB Cluster in Kubernetes |
| 2026-11-26 13:53:11 | [castai-karpenter](https://artifacthub.io/packages/helm/castai/castai-karpenter) | castai | 0.1.0 | Karpenter for EKS, installed and upgraded by the CAST AI castware operator. Wra… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
