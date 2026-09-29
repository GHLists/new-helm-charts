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

## Latest list — 2026-09-29 10:19 UTC

New charts added between 2026-09-29 09:19 UTC and 2026-09-29 10:19 UTC.

[Full CSV](data/new-helm-charts-2026-09-29T10-19-29-381527Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-29 09:30:14 | [azimuth](https://artifacthub.io/packages/helm/azimuth/azimuth) | azimuth | 0.25.0 | Helm chart for deploying the Azimuth Portal. |
| 2026-09-29 10:05:11 | [redmine](https://artifacthub.io/packages/helm/quench-redmine/redmine) | quench-redmine | 0.0.1 | Redmine, the Ruby on Rails project management and issue tracker (issues, wikis,… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
