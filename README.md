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

## Latest list — 2026-11-07 21:20 UTC

New charts added between 2026-11-07 20:19 UTC and 2026-11-07 21:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-07T21-20-30-61894Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-07 21:02:47 | [mmx](https://artifacthub.io/packages/helm/mmx/mmx) | mmx | 0.1.0-rc.1 | A self-hosted order book for game economies |
| 2026-11-07 21:03:22 | [pacboard](https://artifacthub.io/packages/helm/pacboard/pacboard) | pacboard | 0.2.0 | Dashboard for Tekton Pipelines-as-Code runs. Repositories, PR-linked runs, task… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
