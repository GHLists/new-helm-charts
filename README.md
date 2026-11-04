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

## Latest list — 2026-11-04 13:19 UTC

New charts added between 2026-11-04 12:21 UTC and 2026-11-04 13:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-04T13-19-29-810334Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-04 12:41:40 | [inrun](https://artifacthub.io/packages/helm/inrun/inrun) | inrun | 0.1.0 | Inrun is the intent runner for Kubernetes. Callers send an intent through the g… |
| 2026-11-04 12:52:55 | [cwv](https://artifacthub.io/packages/helm/cwv/cwv) | cwv | 0.1.1 | CronJob that runs the cwv CLI and prints CoworkingView Price Index rates. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
