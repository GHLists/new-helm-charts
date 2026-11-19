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

## Latest list — 2026-11-19 13:20 UTC

New charts added between 2026-11-19 12:21 UTC and 2026-11-19 13:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-19T13-20-58-531739Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-19 12:51:01 | [jupyter-imagepuller](https://artifacthub.io/packages/helm/jupyter-jsc/jupyter-imagepuller) | jupyter-jsc | 1.0.0 | A Helm chart for Kubernetes |
| 2026-11-19 12:51:01 | [jupyter-tunnel-secrets](https://artifacthub.io/packages/helm/jupyter-jsc/jupyter-tunnel-secrets) | jupyter-jsc | 0.1.0 | ExternalSecrets for the Jupyter tunnel service |
| 2026-11-19 12:51:01 | [jupyterhub-outpost-secrets](https://artifacthub.io/packages/helm/jupyter-jsc/jupyterhub-outpost-secrets) | jupyter-jsc | 0.1.0 | ExternalSecrets for a JupyterHub outpost |
| 2026-11-19 12:51:01 | [jupyterhub-secrets](https://artifacthub.io/packages/helm/jupyter-jsc/jupyterhub-secrets) | jupyter-jsc | 0.1.0 | ExternalSecrets for a JupyterHub |
| 2026-11-19 13:01:15 | [bardiup](https://artifacthub.io/packages/helm/bardiup/bardiup) | bardiup | 0.1.0 | Lightweight, namespace-scoped PVC backups to S3 with Grandfather-Father-Son ret… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
