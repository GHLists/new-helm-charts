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

## Latest list — 2026-11-18 12:21 UTC

New charts added between 2026-11-18 11:21 UTC and 2026-11-18 12:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-18T12-21-10-435416Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-18 12:03:41 | [prometheus-haproxy-exporter](https://artifacthub.io/packages/helm/prometheus-haproxy-exporter/prometheus-haproxy-exporter) | prometheus-haproxy-expo… | 0.1.8 | A Helm chart to export the metrics from haproxy in Prometheus format. |
| 2026-11-18 12:03:41 | [prometheus-pve-exporter](https://artifacthub.io/packages/helm/prometheus-pve-exporter/prometheus-pve-exporter) | prometheus-pve-exporter | 0.1.18 | A Helm chart to export the metrics from pve in Prometheus format. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
