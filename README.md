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

## Latest list — 2026-10-27 19:20 UTC

New charts added between 2026-10-27 18:19 UTC and 2026-10-27 19:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-27T19-20-28-012193Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-27 19:10:15 | [bazarr](https://artifacthub.io/packages/helm/spnngl-bazarr/bazarr) | spnngl-bazarr | 0.1.0 | Bazarr subtitle manager for Sonarr and Radarr as a hardened single-replica Stat… |
| 2026-10-27 19:10:15 | [configarr](https://artifacthub.io/packages/helm/spnngl-configarr/configarr) | spnngl-configarr | 0.1.0 | Configarr as a hardened CronJob that syncs TRaSH-Guides profiles and settings a… |
| 2026-10-27 19:10:16 | [prowlarr](https://artifacthub.io/packages/helm/spnngl-prowlarr/prowlarr) | spnngl-prowlarr | 0.1.0 | Prowlarr indexer manager for the Servarr apps as a hardened single-replica Stat… |
| 2026-10-27 19:10:16 | [radarr](https://artifacthub.io/packages/helm/spnngl-radarr/radarr) | spnngl-radarr | 0.1.0 | Radarr movie collection manager as a hardened single-replica StatefulSet, with… |
| 2026-10-27 19:10:16 | [sabnzbd](https://artifacthub.io/packages/helm/spnngl-sabnzbd/sabnzbd) | spnngl-sabnzbd | 0.1.0 | SABnzbd Usenet downloader as a hardened single-replica StatefulSet, with settin… |
| 2026-10-27 19:10:16 | [seerr](https://artifacthub.io/packages/helm/spnngl-seerr/seerr) | spnngl-seerr | 0.1.0 | Seerr media request manager for Jellyfin, Emby and Plex as a hardened single-re… |
| 2026-10-27 19:10:17 | [sonarr](https://artifacthub.io/packages/helm/spnngl-sonarr/sonarr) | spnngl-sonarr | 0.1.0 | Sonarr TV series collection manager as a hardened single-replica StatefulSet, w… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
