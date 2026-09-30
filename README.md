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

## Latest list — 2026-09-30 11:20 UTC

New charts added between 2026-09-30 10:21 UTC and 2026-09-30 11:20 UTC.

[Full CSV](data/new-helm-charts-2026-09-30T11-20-28-219424Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-30 10:30:39 | [certmate](https://artifacthub.io/packages/helm/certmate/certmate) | certmate | 2.25.4 | Self-hosted SSL/TLS certificate lifecycle management — issuance, renewal, disco… |
| 2026-09-30 10:52:56 | [manyfold](https://artifacthub.io/packages/helm/ideaplexus/manyfold) | ideaplexus | 0.1.0 | Manyfold is a self-hosted digital asset manager for 3D print files, organising… |
| 2026-09-30 11:02:47 | [loop-csi-provisioner](https://artifacthub.io/packages/helm/loop-csi-provisioner/loop-csi-provisioner) | loop-csi-provisioner | 0.1.1 | CSI driver providing ext4 volumes backed by image files in a local directory or… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
