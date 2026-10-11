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

## Latest list — 2026-10-11 22:20 UTC

New charts added between 2026-10-11 21:19 UTC and 2026-10-11 22:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-11T22-20-58-828239Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-11 21:27:51 | [kubevault-crd-manager](https://artifacthub.io/packages/helm/appscode/kubevault-crd-manager) | appscode | 2026.10.12 | KubeVault CRD Manager by AppsCode |
| 2026-10-11 22:01:51 | [decdn-node](https://artifacthub.io/packages/helm/decdn-node/decdn-node) | decdn-node | 0.1.0 | A deCDN node (decdn-node daemon) on Kubernetes: public QUIC over UDP, a persist… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
