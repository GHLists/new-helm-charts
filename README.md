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

## Latest list — 2026-11-17 03:19 UTC

New charts added between 2026-11-17 02:19 UTC and 2026-11-17 03:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-17T03-19-05-435713Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-17 02:50:40 | [wikijs](https://artifacthub.io/packages/helm/quench-wikijs/wikijs) | quench-wikijs | 0.0.1 | Wiki.js: a wiki with Markdown and visual editors, Git sync and many auth provid… |
| 2026-11-17 03:03:37 | [calibre-web](https://artifacthub.io/packages/helm/quench-calibre-web/calibre-web) | quench-calibre-web | 0.0.1 | Calibre-Web: browse, read and download an ebook library kept in a Calibre datab… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
