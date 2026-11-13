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

## Latest list — 2026-11-13 05:18 UTC

New charts added between 2026-11-13 04:19 UTC and 2026-11-13 05:18 UTC.

[Full CSV](data/new-helm-charts-2026-11-13T05-18-59-057349Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-13 04:39:09 | [grafana-operator](https://artifacthub.io/packages/helm/quench-grafana-operator/grafana-operator) | quench-grafana-operator | 0.0.1 | Grafana Operator: run Grafana instances and manage their dashboards, datasource… |
| 2026-11-13 05:15:41 | [victoriametrics-operator](https://artifacthub.io/packages/helm/quench-victoriametrics-operator/victoriametrics-operator) | quench-victoriametrics-… | 0.0.1 | VictoriaMetrics Operator: run VMSingle, VMCluster, VMAgent, VMAlert, VMAuth, Al… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
