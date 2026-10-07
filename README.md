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

## Latest list — 2026-10-07 17:18 UTC

New charts added between 2026-10-07 16:23 UTC and 2026-10-07 17:18 UTC.

[Full CSV](data/new-helm-charts-2026-10-07T17-18-45-763209Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-07 16:27:48 | [cerberus-robot-proxy](https://artifacthub.io/packages/helm/cerberus-robot-proxy/cerberus-robot-proxy) | cerberus-robot-proxy | 1.5.0-SNAPSHOT | A Helm chart for Kubernetes |
| 2026-10-07 16:43:05 | [multica-runtime-controller](https://artifacthub.io/packages/helm/korioinc/multica-runtime-controller) | korioinc | 2.0.0 | Run Multica agent tasks in dedicated Kubernetes Pods with shared workspace stor… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
