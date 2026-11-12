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

## Latest list — 2026-11-12 10:21 UTC

New charts added between 2026-11-12 09:19 UTC and 2026-11-12 10:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-12T10-21-47-646858Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-12 09:30:48 | [bento](https://artifacthub.io/packages/helm/wikimedia/bento) | wikimedia | 0.1.0 | Bento stream processor |
| 2026-11-12 09:33:14 | [tusd](https://artifacthub.io/packages/helm/quench-tusd/tusd) | quench-tusd | 0.0.1 | tusd: the reference server for the tus resumable-upload protocol, storing uploa… |
| 2026-11-12 10:10:15 | [promxy](https://artifacthub.io/packages/helm/quench-promxy/promxy) | quench-promxy | 0.0.1 | Promxy: a Prometheus aggregating proxy, one PromQL endpoint over several Promet… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
