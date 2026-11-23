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

## Latest list — 2026-11-23 09:19 UTC

New charts added between 2026-11-23 08:21 UTC and 2026-11-23 09:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-23T09-19-09-207587Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-23 08:22:03 | [soft-serve](https://artifacthub.io/packages/helm/quench-soft-serve/soft-serve) | quench-soft-serve | 0.0.1 | Soft Serve: a self-hostable Git server (Git over SSH, HTTP and the git daemon,… |
| 2026-11-23 08:50:58 | [homer](https://artifacthub.io/packages/helm/quench-homer/homer) | quench-homer | 0.0.1 | Homer: a static start page listing your services and links, configured from one… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
