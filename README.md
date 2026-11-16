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

## Latest list — 2026-11-16 16:20 UTC

New charts added between 2026-11-16 15:19 UTC and 2026-11-16 16:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-16T16-20-20-392566Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-16 15:21:43 | [zipline](https://artifacthub.io/packages/helm/quench-zipline/zipline) | quench-zipline | 0.0.1 | Zipline: file and image sharing with ShareX/Flameshot uploads, URL shortening,… |
| 2026-11-16 15:45:37 | [krci-security-operator](https://artifacthub.io/packages/helm/epmdedp-dev/krci-security-operator) | epmdedp-dev | 0.1.0-SNAPSHOT.2 | A Helm chart for the KubeRocketCI Security Operator |
| 2026-11-16 15:50:38 | [silverbullet](https://artifacthub.io/packages/helm/quench-silverbullet/silverbullet) | quench-silverbullet | 0.0.1 | SilverBullet: Markdown notes and personal knowledge platform with Lua scripting… |
| 2026-11-16 16:04:23 | [flatnotes](https://artifacthub.io/packages/helm/quench-flatnotes/flatnotes) | quench-flatnotes | 0.0.1 | flatnotes: database-less Markdown notes on a plain folder of files with full-te… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
