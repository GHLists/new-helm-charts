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

## Latest list — 2026-10-12 16:18 UTC

New charts added between 2026-10-12 15:19 UTC and 2026-10-12 16:18 UTC.

[Full CSV](data/new-helm-charts-2026-10-12T16-18-54-254963Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-12 16:18:20 | [external-snapshotter-crds](https://artifacthub.io/packages/helm/spnngl-external-snapshotter-crds/external-snapshotter-crds) | spnngl-external-snapsho… | 8.6.0 | CustomResourceDefinitions for the Kubernetes CSI external-snapshotter (VolumeSn… |
| 2026-10-12 16:18:20 | [kubemod-crds](https://artifacthub.io/packages/helm/spnngl-kubemod-crds/kubemod-crds) | spnngl-kubemod-crds | 0.21.0 | CustomResourceDefinitions for KubeMod (ModRule) |
| 2026-10-12 16:18:20 | [trivy-operator-crds](https://artifacthub.io/packages/helm/spnngl-trivy-operator-crds/trivy-operator-crds) | spnngl-trivy-operator-c… | 0.35.0 | CustomResourceDefinitions for Trivy Operator (VulnerabilityReport, ConfigAuditR… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
