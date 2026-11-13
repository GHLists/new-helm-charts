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

## Latest list — 2026-11-13 11:20 UTC

New charts added between 2026-11-13 10:20 UTC and 2026-11-13 11:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-13T11-20-08-969551Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-13 11:04:04 | [freshrss](https://artifacthub.io/packages/helm/quench-freshrss/freshrss) | quench-freshrss | 0.0.1 | FreshRSS: a self-hosted RSS and Atom aggregator with multi-user accounts and th… |
| 2026-11-13 11:04:12 | [nats-jetstream-controller](https://artifacthub.io/packages/helm/quench-nats-jetstream-controller/nats-jetstream-controller) | quench-nats-jetstream-c… | 0.0.1 | NATS JetStream Controller (NACK): manage JetStream streams, consumers, key-valu… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
