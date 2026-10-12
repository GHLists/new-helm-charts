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

## Latest list — 2026-10-12 14:22 UTC

New charts added between 2026-10-12 13:21 UTC and 2026-10-12 14:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-12T14-22-36-13467Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-12 13:32:41 | [change-windows](https://artifacthub.io/packages/helm/projectcapsule/change-windows) | projectcapsule | 0.0.1 | Scheduled resource actions and admission maintenance windows for Kubernetes. |
| 2026-10-12 13:33:46 | [stunner-dev](https://artifacthub.io/packages/helm/stunner/stunner-dev) | stunner | 1.2.1 | STUNner Kubernetes Gateway Operator |
| 2026-10-12 13:34:38 | [apache-polaris](https://artifacthub.io/packages/helm/quench-apache-polaris/apache-polaris) | quench-apache-polaris | 0.0.1 | Apache Polaris, the open REST catalog for Apache Iceberg: Iceberg REST and mana… |
| 2026-10-12 13:47:02 | [nftables-exporter](https://artifacthub.io/packages/helm/spnngl-nftables-exporter/nftables-exporter) | spnngl-nftables-exporter | 0.1.0 | Prometheus exporter for the nftables ruleset of every node (counters, chains, r… |
| 2026-10-12 13:53:09 | [mo-platform-tests-dev](https://artifacthub.io/packages/helm/mogenius/mo-platform-tests-dev) | mogenius | 0.1.0-dev.1 | The mo-platform-tests operator with its UI. Needs nothing but its own namespace. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
