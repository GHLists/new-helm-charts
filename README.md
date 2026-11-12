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

## Latest list — 2026-11-12 17:19 UTC

New charts added between 2026-11-12 16:21 UTC and 2026-11-12 17:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-12T17-19-00-330159Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-12 16:37:34 | [jupyter-imagepuller](https://artifacthub.io/packages/helm/jupyter-jsc/jupyter-imagepuller) | jupyter-jsc | 1.0.0 | A Helm chart for Kubernetes |
| 2026-11-12 16:45:16 | [chaos-experiments](https://artifacthub.io/packages/helm/ktech-org/chaos-experiments) | ktech-org | 1.0.0 | Self-service Chaos Mesh scenarios (pod-kill, network-latency, memory-stress). R… |
| 2026-11-12 17:09:39 | [homebox](https://artifacthub.io/packages/helm/quench-homebox/homebox) | quench-homebox | 0.0.1 | Homebox: home inventory and asset tracking (items, tags, locations, attachments… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
