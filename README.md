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

## Latest list — 2026-10-15 09:23 UTC

New charts added between 2026-10-15 08:22 UTC and 2026-10-15 09:23 UTC.

[Full CSV](data/new-helm-charts-2026-10-15T09-23-32-443821Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-15 08:31:49 | [resource-permits](https://artifacthub.io/packages/helm/projectcapsule/resource-permits) | projectcapsule | 0.0.1 | Kubernetes approval workflows and managed resource lifecycles |
| 2026-10-15 09:03:18 | [vistergy-agent-server](https://artifacthub.io/packages/helm/openshift/vistergy-agent-server) | openshift | 0.1.25 | Vistergy governed AI agent server for asset-intensive critical infrastructure.… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
