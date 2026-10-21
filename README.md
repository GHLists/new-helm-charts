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

## Latest list — 2026-10-21 07:22 UTC

New charts added between 2026-10-21 06:19 UTC and 2026-10-21 07:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-21T07-22-07-529159Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-21 06:45:01 | [ghcr-exporter](https://artifacthub.io/packages/helm/spnngl-ghcr-exporter/ghcr-exporter) | spnngl-ghcr-exporter | 0.1.0 | Prometheus exporter for GitHub Container Registry package metrics (ghcr-exporte… |
| 2026-10-21 06:45:01 | [transmission](https://artifacthub.io/packages/helm/spnngl-transmission/transmission) | spnngl-transmission | 0.1.0 | Transmission BitTorrent daemon and web UI as a hardened single-replica Stateful… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
