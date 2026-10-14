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

## Latest list — 2026-10-14 16:22 UTC

New charts added between 2026-10-14 14:23 UTC and 2026-10-14 16:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-14T16-22-28-032118Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-14 14:50:19 | [mo-sandbox-agent-hub-dev](https://artifacthub.io/packages/helm/mogenius/mo-sandbox-agent-hub-dev) | mogenius | 0.1.0-dev.2 | The Sandbox Agent Hub: coding agents in mogenius sandboxes that turn a task int… |
| 2026-10-14 15:13:34 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |
| 2026-10-14 15:57:02 | [kratix](https://artifacthub.io/packages/helm/syntasso/kratix) | syntasso | 0.0.1 | A Helm chart for installing Kratix (https://kratix.io) |
| 2026-10-14 16:11:33 | [stunner-dev](https://artifacthub.io/packages/helm/stunner/stunner-dev) | stunner | 1.2.1 | STUNner Kubernetes Gateway Operator |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
