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

## Latest list — 2026-10-13 10:21 UTC

New charts added between 2026-10-13 09:20 UTC and 2026-10-13 10:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-13T10-21-25-557533Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-13 09:33:58 | [flux-crds](https://artifacthub.io/packages/helm/spnngl-flux-crds/flux-crds) | spnngl-flux-crds | 2.9.6 | CustomResourceDefinitions for Flux (sources, kustomizations, Helm releases, not… |
| 2026-10-13 09:43:39 | [cosmotech-kubernetes-workload-scaler](https://artifacthub.io/packages/helm/cosmotech-api/cosmotech-kubernetes-workload-scaler) | cosmotech-api | 0.0.0 | A Helm chart for Cosmo Tech Kubernetes workload scaler |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
