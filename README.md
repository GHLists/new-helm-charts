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

## Latest list — 2026-10-22 09:20 UTC

New charts added between 2026-10-22 08:21 UTC and 2026-10-22 09:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-22T09-20-56-128586Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-22 08:54:38 | [cluster-cloudnativedb](https://artifacthub.io/packages/helm/startx/cluster-cloudnativedb) | startx | 21.3.300 | Helm chart used to configure highly available PostgreSQL clusters using the Clo… |
| 2026-10-22 08:54:39 | [cluster-etcdbackup](https://artifacthub.io/packages/helm/startx/cluster-etcdbackup) | startx | 21.3.300 | Helm chart used to deploy a CronJob that backs up OpenShift etcd to an S3-compa… |
| 2026-10-22 08:54:41 | [cluster-kasten](https://artifacthub.io/packages/helm/startx/cluster-kasten) | startx | 21.3.300 | Helm chart used to configure Kasten K10 data management platform (operator, K10… |
| 2026-10-22 08:54:42 | [cluster-qdrant](https://artifacthub.io/packages/helm/startx/cluster-qdrant) | startx | 21.3.300 | Helm chart used to deploy Qdrant vector database at the cluster level |
| 2026-10-22 08:54:42 | [cluster-trident](https://artifacthub.io/packages/helm/startx/cluster-trident) | startx | 21.3.300 | Helm chart used to configure NetApp Trident CSI (operator, orchestrator, backen… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
