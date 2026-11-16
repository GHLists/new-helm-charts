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

## Latest list — 2026-11-16 20:21 UTC

New charts added between 2026-11-16 19:19 UTC and 2026-11-16 20:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-16T20-21-31-988397Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-16 19:21:34 | [apemind-web-access](https://artifacthub.io/packages/helm/kubeblocks/apemind-web-access) | kubeblocks | 0.1.1 | ApeMind web-access service for private deployment: SearxNG web search (port 808… |
| 2026-11-16 19:21:39 | [rallly](https://artifacthub.io/packages/helm/quench-rallly/rallly) | quench-rallly | 0.0.1 | Rallly: meeting scheduling polls (a self-hosted Doodle alternative) with sign-i… |
| 2026-11-16 19:27:11 | [apemind-computer](https://artifacthub.io/packages/helm/kubeblocks/apemind-computer) | kubeblocks | 0.2.14 | Multi-tenant hosted dsh (computer-host) gateway, control API, and supervisor. |
| 2026-11-16 19:32:35 | [convertx](https://artifacthub.io/packages/helm/quench-convertx/convertx) | quench-convertx | 0.0.1 | ConvertX: self-hosted file converter for images, video, audio and office docume… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
