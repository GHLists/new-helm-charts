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

## Latest list — 2026-10-11 15:20 UTC

New charts added between 2026-10-11 14:19 UTC and 2026-10-11 15:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-11T15-20-29-58131Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-11 14:30:51 | [teslamate](https://artifacthub.io/packages/helm/dcardozoo/teslamate) | dcardozoo | 0.1.0 | TeslaMate data logger with Grafana dashboards, Mosquitto MQTT broker and a high… |
| 2026-10-11 14:56:46 | [openunison-k8s-cluster-management-by-group](https://artifacthub.io/packages/helm/tremolo/openunison-k8s-cluster-management-by-group) | tremolo | 0.1.0 | A Helm chart for Kubernetes |
| 2026-10-11 14:56:46 | [openunison-vcluster-admins](https://artifacthub.io/packages/helm/tremolo/openunison-vcluster-admins) | tremolo | 0.1.0 | Generates cluster-admins for vclusters |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
