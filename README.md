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

## Latest list — 2026-11-21 14:21 UTC

New charts added between 2026-11-21 13:20 UTC and 2026-11-21 14:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-21T14-21-13-780385Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-21 13:51:02 | [tikete](https://artifacthub.io/packages/helm/tikete/tikete) | tikete | 0.1.0 | Tikete — self-hosted work tracking and service desk (API, worker, web app, Post… |
| 2026-11-21 14:15:33 | [questarr](https://artifacthub.io/packages/helm/questarr/questarr) | questarr | 0.1.4 | Questarr — an *Arr-inspired game manager that helps you discover, track, and au… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
