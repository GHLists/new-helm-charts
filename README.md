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

## Latest list — 2026-10-30 12:21 UTC

New charts added between 2026-10-30 11:21 UTC and 2026-10-30 12:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-30T12-21-09-516456Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-30 11:44:17 | [visa-k8s-provider](https://artifacthub.io/packages/helm/alba-visa-helm-charts/visa-k8s-provider) | alba-visa-helm-charts | 1.0.6 | A Helm chart for deploying VISA's kubernetes cloud provider controller |
| 2026-10-30 11:55:28 | [kratix](https://artifacthub.io/packages/helm/syntasso/kratix) | syntasso | 0.0.1 | A Helm chart for installing Kratix (https://kratix.io) |
| 2026-10-30 12:10:40 | [vault-secrets-reloader](https://artifacthub.io/packages/helm/vault-secrets-reloader-fork/vault-secrets-reloader) | vault-secrets-reloader-… | 0.5.0-operator-test… | A Kubernetes Controller that reloads workloads on a referenced secret change in… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
