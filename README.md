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

## Latest list — 2026-09-29 07:19 UTC

New charts added between 2026-09-29 06:20 UTC and 2026-09-29 07:19 UTC.

[Full CSV](data/new-helm-charts-2026-09-29T07-19-34-507915Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-29 06:42:26 | [generic_service](https://artifacthub.io/packages/helm/loeken-at-home/generic_service) | loeken-at-home | 1.0.0 | a helm chart to install sinusbot |
| 2026-09-29 06:42:26 | [home-assistant](https://artifacthub.io/packages/helm/loeken-at-home/home-assistant) | loeken-at-home | 2026.5.1 | home-assistant - a free and open-source software for home automation designed t… |
| 2026-09-29 06:42:26 | [jellyfin](https://artifacthub.io/packages/helm/loeken-at-home/jellyfin) | loeken-at-home | 10.11.8 | a helm chart to install jellyfin |
| 2026-09-29 06:42:26 | [jellyseerr](https://artifacthub.io/packages/helm/loeken-at-home/jellyseerr) | loeken-at-home | 3.1.0 | a helm chart to install jellyseer |
| 2026-09-29 06:42:26 | [nzbget](https://artifacthub.io/packages/helm/loeken-at-home/nzbget) | loeken-at-home | 26.1.0-ls241 | nzbget - efficient usenet downloader. |
| 2026-09-29 06:42:26 | [prowlarr](https://artifacthub.io/packages/helm/loeken-at-home/prowlarr) | loeken-at-home | 1.37.0 | prowlarr - Prowlarr is an indexer manager/proxy built on the popular *arr softw… |
| 2026-09-29 06:42:26 | [radarr](https://artifacthub.io/packages/helm/loeken-at-home/radarr) | loeken-at-home | 5.27.0-nightly | a helm chart to install radarr |
| 2026-09-29 06:42:26 | [sinusbot](https://artifacthub.io/packages/helm/loeken-at-home/sinusbot) | loeken-at-home | 2.3.0 | a helm chart to install sinusbot |
| 2026-09-29 06:42:26 | [sonarr](https://artifacthub.io/packages/helm/loeken-at-home/sonarr) | loeken-at-home | 4.0.18 | sonarr - an internet PVR for Usenet and Torrents. |
| 2026-09-29 06:42:26 | [uptime-kuma](https://artifacthub.io/packages/helm/loeken-at-home/uptime-kuma) | loeken-at-home | 2.3.2 | a helm chart to install uptime-kuma |
| 2026-09-29 06:42:26 | [vaultwarden](https://artifacthub.io/packages/helm/loeken-at-home/vaultwarden) | loeken-at-home | 1.37.0-alpine | vaultwarden - unofficial bitwarden compatible server written in rust, formerly… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
