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

## Latest list — 2026-10-05 11:21 UTC

New charts added between 2026-10-05 10:19 UTC and 2026-10-05 11:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-05T11-21-01-621914Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-05 10:30:49 | [decision-model-operator](https://artifacthub.io/packages/helm/decision-model-operator/decision-model-operator) | decision-model-operator | 0.1.1 | Kubernetes Operator for Ollaya-served System-1 decision models (DecisionModel C… |
| 2026-10-05 10:38:56 | [betacalendars-calendar-boundary-lab](https://artifacthub.io/packages/helm/betacalendars-calendar-boundary-lab/betacalendars-calendar-boundary-lab) | betacalendars-calendar-… | 0.1.1 | Helm chart for a deterministic Gregorian calendar boundary and month-grid confo… |
| 2026-10-05 10:45:42 | [cluster-autoscaler](https://artifacthub.io/packages/helm/quench-cluster-autoscaler/cluster-autoscaler) | quench-cluster-autoscal… | 0.0.2 | Kubernetes Cluster Autoscaler, the SIG Autoscaling controller that adds nodes w… |
| 2026-10-05 11:03:43 | [connaisseur](https://artifacthub.io/packages/helm/quench-connaisseur/connaisseur) | quench-connaisseur | 0.0.1 | Connaisseur, the Kubernetes admission controller that verifies container image… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
