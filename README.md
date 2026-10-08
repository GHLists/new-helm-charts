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

## Latest list — 2026-10-08 15:19 UTC

New charts added between 2026-10-08 14:24 UTC and 2026-10-08 15:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-08T15-19-48-195236Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-08 14:32:39 | [linkerd-cni](https://artifacthub.io/packages/helm/quench-linkerd-cni/linkerd-cni) | quench-linkerd-cni | 0.0.1 | Linkerd CNI plugin: a DaemonSet that chains the linkerd-cni plugin into each no… |
| 2026-10-08 14:38:54 | [rainstone](https://artifacthub.io/packages/helm/cloudve/rainstone) | cloudve | 0.3.0 | Galaxy compute cost reporting, deployed alongside Galaxy |
| 2026-10-08 15:01:16 | [azimuth-schedule-operator](https://artifacthub.io/packages/helm/azimuth-schedule-operator-chart/azimuth-schedule-operator) | azimuth-schedule-operat… | 0.12.0 | Helm chart for deploying the Azimuth schedule operator. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
