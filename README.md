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

## Latest list — 2026-10-19 11:21 UTC

New charts added between 2026-10-19 10:23 UTC and 2026-10-19 11:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-19T11-21-52-724839Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-19 11:03:37 | [cost-stack](https://artifacthub.io/packages/helm/quench-cost-stack/cost-stack) | quench-cost-stack | 0.0.2 | Hardened Kubernetes cost monitoring stack: OpenCost (the CNCF cost model) readi… |
| 2026-10-19 11:04:13 | [agent-substrate-crds](https://artifacthub.io/packages/helm/spnngl-agent-substrate-crds/agent-substrate-crds) | spnngl-agent-substrate-… | 0.5.0 | CustomResourceDefinitions for Agent Substrate (sandbox configs, worker pools, C… |
| 2026-10-19 11:04:13 | [kagent-crds](https://artifacthub.io/packages/helm/spnngl-kagent-crds/kagent-crds) | spnngl-kagent-crds | 0.10.3 | CustomResourceDefinitions for kagent (agents, model configs, memories, tool and… |
| 2026-10-19 11:04:13 | [kmcp-crds](https://artifacthub.io/packages/helm/spnngl-kmcp-crds/kmcp-crds) | spnngl-kmcp-crds | 0.3.0 | CustomResourceDefinitions for kmcp (MCPServer, used by kagent) |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
