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

## Latest list — 2026-11-24 16:20 UTC

New charts added between 2026-11-24 15:22 UTC and 2026-11-24 16:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-24T16-20-20-579784Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-24 15:27:01 | [keda](https://artifacthub.io/packages/helm/wikimedia/keda) | wikimedia | 2.21.0 | Event-based autoscaler for workloads on Kubernetes |
| 2026-11-24 16:01:18 | [amadioha-agent](https://artifacthub.io/packages/helm/amadioha-agent/amadioha-agent) | amadioha-agent | 1.0.0-rc.2 | Amadioha's agent on every node of a Kubernetes cluster (a DaemonSet): each node… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
