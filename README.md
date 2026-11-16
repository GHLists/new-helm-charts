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

## Latest list — 2026-11-16 02:20 UTC

New charts added between 2026-11-16 01:21 UTC and 2026-11-16 02:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-16T02-20-52-877236Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-16 01:37:28 | [unifi-os-server](https://artifacthub.io/packages/helm/schichtel/unifi-os-server) | schichtel | 0.1.0 | UniFi OS Server (UniFi OS core, UniFi Network and the UniFi identity services)… |
| 2026-11-16 01:50:26 | [derper](https://artifacthub.io/packages/helm/quench-derper/derper) | quench-derper | 0.0.1 | derper: Tailscale's DERP relay for tailnets (Tailscale or Headscale), relaying… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
