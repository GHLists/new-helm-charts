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

## Latest list — 2026-11-14 06:21 UTC

New charts added between 2026-11-14 05:19 UTC and 2026-11-14 06:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-14T06-21-11-238333Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-14 05:50:53 | [kubeflow-trainer](https://artifacthub.io/packages/helm/quench-kubeflow-trainer/kubeflow-trainer) | quench-kubeflow-trainer | 0.0.1 | Kubeflow Trainer: distributed training on Kubernetes (PyTorch, JAX, MPI) as Tra… |
| 2026-11-14 06:15:33 | [knative-operator](https://artifacthub.io/packages/helm/quench-knative-operator/knative-operator) | quench-knative-operator | 0.0.1 | Knative Operator: installs and upgrades Knative Serving (serverless containers… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
