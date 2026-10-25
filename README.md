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

## Latest list — 2026-10-25 12:22 UTC

New charts added between 2026-10-25 11:20 UTC and 2026-10-25 12:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-25T12-22-09-154896Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-25 11:31:37 | [kates](https://artifacthub.io/packages/helm/kates/kates) | kates | 0.13.5 | Kates — Kafka Advanced Testing & Engineering Suite |
| 2026-10-25 12:01:48 | [connect-cluster](https://artifacthub.io/packages/helm/connect-cluster/connect-cluster) | connect-cluster | 2.1.14 | A Helm chart for deploying Strimzi Kafka Connect clusters |
| 2026-10-25 12:02:35 | [kafka-cluster](https://artifacthub.io/packages/helm/kafka-cluster/kafka-cluster) | kafka-cluster | 1.0.18 | A Strimzi Kafka cluster in KRaft mode — node pools, topics, users, rebalancing,… |
| 2026-10-25 12:02:36 | [kates-chaos](https://artifacthub.io/packages/helm/kates-chaos/kates-chaos) | kates-chaos | 2.3.4 | Kates Chaos Engineering — wraps the LitmusChaos execution plane (operator, expo… |
| 2026-10-25 12:02:36 | [kates-monitoring](https://artifacthub.io/packages/helm/kates-monitoring/kates-monitoring) | kates-monitoring | 1.7.1 | Kates Monitoring — wraps kube-prometheus-stack with Kates-specific dashboards a… |
| 2026-10-25 12:02:36 | [kates-platform](https://artifacthub.io/packages/helm/kates-platform/kates-platform) | kates-platform | 0.8.4 | Umbrella chart for the full Kates platform — Kafka, Kates, and supporting infra… |
| 2026-10-25 12:02:57 | [mirror-maker2](https://artifacthub.io/packages/helm/mirror-maker2/mirror-maker2) | mirror-maker2 | 0.11.12 | Strimzi KafkaMirrorMaker2 — cross-cluster replication, DR, and cross-version mi… |
| 2026-10-25 12:16:18 | [strimzi-operator](https://artifacthub.io/packages/helm/strimzi-operator/strimzi-operator) | strimzi-operator | 0.4.4 | The Strimzi Kafka Operator — wraps the upstream chart with pinned kates default… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
