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

## Latest list — 2026-11-23 14:22 UTC

New charts added between 2026-11-23 13:21 UTC and 2026-11-23 14:22 UTC.

[Full CSV](data/new-helm-charts-2026-11-23T14-22-33-001502Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-23 13:26:06 | [upgradoor](https://artifacthub.io/packages/helm/ethereum-helm-charts/upgradoor) | ethereum-helm-charts | 0.1.0 | Per-devnet controller that staggers docker image rolls, package upgrades and re… |
| 2026-11-23 13:44:38 | [langflow](https://artifacthub.io/packages/helm/quench-langflow/langflow) | quench-langflow | 0.0.1 | Langflow: a visual builder for LLM applications and agent workflows (React UI a… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
