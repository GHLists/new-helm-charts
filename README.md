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

## Latest list — 2026-11-16 03:19 UTC

New charts added between 2026-11-16 02:20 UTC and 2026-11-16 03:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-16T03-19-25-839114Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-16 02:44:27 | [microbin](https://artifacthub.io/packages/helm/quench-microbin/microbin) | quench-microbin | 0.0.1 | MicroBin: a small pastebin and file-sharing server with private, read-only and… |
| 2026-11-16 03:15:31 | [miniserve](https://artifacthub.io/packages/helm/quench-miniserve/miniserve) | quench-miniserve | 0.0.1 | miniserve: a small file server with directory listing, uploads, archive downloa… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
