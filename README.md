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

## Latest list — 2026-10-16 15:20 UTC

New charts added between 2026-10-16 14:20 UTC and 2026-10-16 15:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-16T15-20-54-534405Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-16 14:28:32 | [nemo-guardrails](https://artifacthub.io/packages/helm/upstreamyard/nemo-guardrails) | upstreamyard | 0.1.0 | NeMo Guardrails Helm chart for Kubernetes. NVIDIA NeMo Guardrails server, an Op… |
| 2026-10-16 14:31:20 | [hugegraph-helm](https://artifacthub.io/packages/helm/hugegraph-helm/hugegraph-helm) | hugegraph-helm | 0.2.0-dev.2 | Helm chart for Apache HugeGraph HStore cluster (PD + Store + Server) |
| 2026-10-16 15:01:43 | [automq](https://artifacthub.io/packages/helm/upstreamyard/automq) | upstreamyard | 0.1.0 | AutoMQ Helm chart for Kubernetes. Kafka-compatible streaming with messages stor… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
