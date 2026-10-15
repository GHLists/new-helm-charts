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

## Latest list — 2026-10-15 14:21 UTC

New charts added between 2026-10-15 13:19 UTC and 2026-10-15 14:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-15T14-21-35-134639Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-15 13:21:37 | [cerberus-robot-proxy](https://artifacthub.io/packages/helm/cerberus-robot-proxy/cerberus-robot-proxy) | cerberus-robot-proxy | 1.5.0-SNAPSHOT | A Helm chart for Kubernetes |
| 2026-10-15 13:50:33 | [kron-aapm-agent](https://artifacthub.io/packages/helm/kron-pam-aapm-helmcharts/kron-aapm-agent) | kron-pam-aapm-helmcharts | 1.2.8 | Kron Aapm Agent for Kubernetes |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
