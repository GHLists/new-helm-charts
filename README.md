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

## Latest list — 2026-09-28 21:22 UTC

New charts added between 2026-09-28 20:19 UTC and 2026-09-28 21:22 UTC.

[Full CSV](data/new-helm-charts-2026-09-28T21-22-42-994409Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-28 20:31:03 | [github-oidc-exchange](https://artifacthub.io/packages/helm/github-oidc-exchange/github-oidc-exchange) | github-oidc-exchange | 0.3.4 | Platform OIDC exchange issuer for GitHub and Kubernetes workload identity |
| 2026-09-28 20:45:09 | [steward-run-arc](https://artifacthub.io/packages/helm/steward-run/steward-run-arc) | steward-run | 0.6.0 | Installable steward-run adapter for the upstream ARC runner scale set |
| 2026-09-28 20:45:11 | [steward](https://artifacthub.io/packages/helm/steward/steward) | steward | 0.1.7 | Governance control plane for policy-bound coding-agent workloads |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
