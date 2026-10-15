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

## Latest list — 2026-10-15 16:21 UTC

New charts added between 2026-10-15 15:20 UTC and 2026-10-15 16:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-15T16-21-31-392703Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-15 15:23:38 | [regioninfo](https://artifacthub.io/packages/helm/trisacrypto/regioninfo) | trisacrypto | 1.1.0 | Adds region information to the cluster for geographic debugging |
| 2026-10-15 15:37:26 | [krci-env-daemon](https://artifacthub.io/packages/helm/epmdedp-dev/krci-env-daemon) | epmdedp-dev | 0.1.0-SNAPSHOT.4 | A Helm chart for krci-env-daemon, which wakes KubeRocketCI environments that KE… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
