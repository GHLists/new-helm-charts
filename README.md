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

## Latest list — 2026-11-13 10:20 UTC

New charts added between 2026-11-13 09:19 UTC and 2026-11-13 10:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-13T10-20-24-290308Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-13 09:31:29 | [kadmo-agent-chart](https://artifacthub.io/packages/helm/kadmo/kadmo-agent-chart) | kadmo | 0.1.1 | One self-hosted Kadmo AI agent in a Kubernetes cluster you control - the kadmo-… |
| 2026-11-13 09:44:33 | [opensearch-operator](https://artifacthub.io/packages/helm/quench-opensearch-operator/opensearch-operator) | quench-opensearch-opera… | 0.0.1 | OpenSearch Operator: run OpenSearch clusters and OpenSearch Dashboards from Ope… |
| 2026-11-13 10:15:37 | [redis-operator](https://artifacthub.io/packages/helm/quench-redis-operator/redis-operator) | quench-redis-operator | 0.0.1 | Redis Operator (OT-CONTAINER-KIT): run Redis standalone, replication, Sentinel… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
