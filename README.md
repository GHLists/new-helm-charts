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

## Latest list — 2026-10-02 01:21 UTC

New charts added between 2026-10-02 00:19 UTC and 2026-10-02 01:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-02T01-21-23-16321Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-02 00:25:11 | [headplane](https://artifacthub.io/packages/helm/headplane-helm/headplane) | headplane-helm | 0.0.4 | Helm chart for Headplane, the web UI for Headscale |
| 2026-10-02 00:27:30 | [nostalgiatv](https://artifacthub.io/packages/helm/nostalgiatv-helm/nostalgiatv) | nostalgiatv-helm | 0.1.1 | Helm chart for the NostalgiaTV companion server (schedules, Jellyfin/Plex/Emby,… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
