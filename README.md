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

## Latest list — 2026-10-31 19:20 UTC

New charts added between 2026-10-31 18:18 UTC and 2026-10-31 19:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-31T19-20-51-686149Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-31 18:54:34 | [bazarr](https://artifacthub.io/packages/helm/lbenicio-community/bazarr) | lbenicio-community | 0.1.0 | Bazarr (Sonarr, Radarr, Prowlarr, Bazarr, etc.) |
| 2026-10-31 18:54:34 | [glance](https://artifacthub.io/packages/helm/lbenicio-community/glance) | lbenicio-community | 0.1.3 | A Helm chart for glance |
| 2026-10-31 18:54:34 | [helm-pilot](https://artifacthub.io/packages/helm/lbenicio-community/helm-pilot) | lbenicio-community | 0.2.4 | AI-powered Helm management dashboard for Kubernetes clusters |
| 2026-10-31 18:54:34 | [homebridge](https://artifacthub.io/packages/helm/lbenicio-community/homebridge) | lbenicio-community | 0.1.15 | A Helm chart for homebridge |
| 2026-10-31 18:54:34 | [jellyfin](https://artifacthub.io/packages/helm/lbenicio-community/jellyfin) | lbenicio-community | 0.1.0 | Jellyfin (Sonarr, Radarr, Prowlarr, Bazarr, etc.) |
| 2026-10-31 18:54:34 | [jellyseerr](https://artifacthub.io/packages/helm/lbenicio-community/jellyseerr) | lbenicio-community | 0.1.0 | Jellyseerr (Sonarr, Radarr, Prowlarr, Bazarr, etc.) |
| 2026-10-31 18:54:34 | [kubernetes-dashboard](https://artifacthub.io/packages/helm/lbenicio-community/kubernetes-dashboard) | lbenicio-community | 7.14.10 | General-purpose web UI for Kubernetes clusters |
| 2026-10-31 18:54:34 | [listmonk](https://artifacthub.io/packages/helm/lbenicio-community/listmonk) | lbenicio-community | 0.1.0 | Self-hosted newsletter and mailing list manager |
| 2026-10-31 18:54:34 | [ping](https://artifacthub.io/packages/helm/lbenicio-community/ping) | lbenicio-community | 0.1.1 | Blackbox exporter for probing endpoints |
| 2026-10-31 18:54:34 | [pod-cleaner](https://artifacthub.io/packages/helm/lbenicio-community/pod-cleaner) | lbenicio-community | 0.1.1 | CronJob that periodically cleans up completed pods |
| 2026-10-31 18:54:34 | [prowlarr](https://artifacthub.io/packages/helm/lbenicio-community/prowlarr) | lbenicio-community | 0.1.0 | Prowlarr (Sonarr, Radarr, Prowlarr, Bazarr, etc.) |
| 2026-10-31 18:54:34 | [qbittorrent](https://artifacthub.io/packages/helm/lbenicio-community/qbittorrent) | lbenicio-community | 0.1.0 | Qbittorrent (Sonarr, Radarr, Prowlarr, Bazarr, etc.) |
| 2026-10-31 18:54:34 | [radarr](https://artifacthub.io/packages/helm/lbenicio-community/radarr) | lbenicio-community | 0.1.0 | Radarr (Sonarr, Radarr, Prowlarr, Bazarr, etc.) |
| 2026-10-31 18:54:34 | [searxng](https://artifacthub.io/packages/helm/lbenicio-community/searxng) | lbenicio-community | 0.1.1 | Privacy-respecting metasearch engine. StatefulSet with a single local-path volu… |
| 2026-10-31 18:54:34 | [smtp](https://artifacthub.io/packages/helm/lbenicio-community/smtp) | lbenicio-community | 0.1.4 | A Helm chart for smtp |
| 2026-10-31 18:54:34 | [sonarr](https://artifacthub.io/packages/helm/lbenicio-community/sonarr) | lbenicio-community | 0.1.0 | Sonarr (Sonarr, Radarr, Prowlarr, Bazarr, etc.) |
| 2026-10-31 18:54:34 | [speedtest](https://artifacthub.io/packages/helm/lbenicio-community/speedtest) | lbenicio-community | 0.1.0 | Internet performance exporter (speedtest, fast.com) |
| 2026-10-31 18:54:34 | [stremio](https://artifacthub.io/packages/helm/lbenicio-community/stremio) | lbenicio-community | 0.1.2 | Helm chart for Stremio server + web client |
| 2026-10-31 18:54:34 | [timemachine](https://artifacthub.io/packages/helm/lbenicio-community/timemachine) | lbenicio-community | 0.1.3 | Helm chart for Time Machine Samba backup server |
| 2026-10-31 18:54:34 | [uptime-kuma](https://artifacthub.io/packages/helm/lbenicio-community/uptime-kuma) | lbenicio-community | 0.1.1 | A self-hosted monitoring tool like Uptime Robot |
| 2026-10-31 18:54:34 | [whoami](https://artifacthub.io/packages/helm/lbenicio-community/whoami) | lbenicio-community | 0.1.2 | A Helm chart for whoami |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
