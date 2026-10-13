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

## Latest list — 2026-10-13 14:21 UTC

New charts added between 2026-10-13 13:19 UTC and 2026-10-13 14:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-13T14-21-56-156399Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-13 13:30:08 | [anychart](https://artifacthub.io/packages/helm/anychart/anychart) | anychart | 1.0.0 | A configurable Helm chart for application workloads and supporting Kubernetes r… |
| 2026-10-13 13:42:45 | [csi-driver-ipfs](https://artifacthub.io/packages/helm/csi-driver-ipfs/csi-driver-ipfs) | csi-driver-ipfs | 0.2.0 | CSI driver for IPFS volumes in Kubernetes |
| 2026-10-13 13:42:45 | [ipfs-cluster](https://artifacthub.io/packages/helm/csi-driver-ipfs/ipfs-cluster) | csi-driver-ipfs | 0.2.0 | IPFS Cluster - orchestrated pinning and replication for IPFS |
| 2026-10-13 14:00:03 | [domain-locker](https://artifacthub.io/packages/helm/domain-locker/domain-locker) | domain-locker | 0.3.4 | A Helm chart for deploying Domain Locker |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
