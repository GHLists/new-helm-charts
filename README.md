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

## Latest list — 2026-10-08 17:21 UTC

New charts added between 2026-10-08 16:21 UTC and 2026-10-08 17:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-08T17-21-38-049993Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-08 16:32:49 | [linkerd-viz](https://artifacthub.io/packages/helm/quench-linkerd-viz/linkerd-viz) | quench-linkerd-viz | 0.0.1 | Linkerd Viz (edge release line) without the web dashboard: metrics-api (the Pro… |
| 2026-10-08 16:32:50 | [prometheus-nats-exporter](https://artifacthub.io/packages/helm/quench-prometheus-nats-exporter/prometheus-nats-exporter) | quench-prometheus-nats-… | 0.0.1 | Prometheus exporter for NATS: server (varz), connection, route, subscription an… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
