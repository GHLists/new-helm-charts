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

## Latest list — 2026-10-07 10:20 UTC

New charts added between 2026-10-07 09:22 UTC and 2026-10-07 10:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-07T10-20-45-605207Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-07 09:32:40 | [policy-stack](https://artifacthub.io/packages/helm/quench-policy-stack/policy-stack) | quench-policy-stack | 0.0.4 | Hardened Kubernetes policy in one install: Kyverno (admission policies and back… |
| 2026-10-07 09:56:23 | [visa-k8s-controller](https://artifacthub.io/packages/helm/alba-visa-helm-charts/visa-k8s-controller) | alba-visa-helm-charts | 1.0.0 | A Helm chart for deploying VISA's kubernetes cloud provider controller |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
