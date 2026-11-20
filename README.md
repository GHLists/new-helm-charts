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

## Latest list — 2026-11-20 22:20 UTC

New charts added between 2026-11-20 21:22 UTC and 2026-11-20 22:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-20T22-20-21-82463Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-20 21:31:17 | [harbor](https://artifacthub.io/packages/helm/harbor-8gears/harbor) | harbor-8gears | 1.18.1 | A modern, production-ready Helm chart for [Harbor Next](https://github.com/cont… |
| 2026-11-20 21:32:01 | [aibom-webhook](https://artifacthub.io/packages/helm/openshift/aibom-webhook) | openshift | 1.0.4 | AIBOM mutating admission webhook and controller for OpenShift. PREREQUISITE: th… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
