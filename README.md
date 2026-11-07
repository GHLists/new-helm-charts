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

## Latest list — 2026-11-07 09:19 UTC

New charts added between 2026-11-07 08:19 UTC and 2026-11-07 09:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-07T09-19-49-250216Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-07 08:22:02 | [matterjs-server](https://artifacthub.io/packages/helm/egeback/matterjs-server) | egeback | 1.0.0 | Open Home Foundation Matter Server (matter.js) for Home Assistant, the successo… |
| 2026-11-07 08:22:21 | [zwave-js-ui](https://artifacthub.io/packages/helm/egeback/zwave-js-ui) | egeback | 1.0.0 | Z-Wave control panel and Z-Wave JS server for Home Assistant |
| 2026-11-07 08:22:37 | [go2rtc](https://artifacthub.io/packages/helm/egeback/go2rtc) | egeback | 1.0.0 | Camera streaming application (RTSP, WebRTC, HomeKit, MSE) for Home Assistant an… |
| 2026-11-07 08:22:54 | [ha-tn-reporter](https://artifacthub.io/packages/helm/egeback/ha-tn-reporter) | egeback | 1.0.0 | Reports Home Assistant temperature sensors to temperatur.nu |
| 2026-11-07 08:23:16 | [teslamate-abrp](https://artifacthub.io/packages/helm/egeback/teslamate-abrp) | egeback | 1.0.0 | Sends TeslaMate data from MQTT to A Better Route Planner (ABRP) |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
