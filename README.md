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

## Latest list — 2026-11-15 14:20 UTC

New charts added between 2026-11-15 13:20 UTC and 2026-11-15 14:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T14-20-21-836154Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 13:32:40 | [cloudreve](https://artifacthub.io/packages/helm/quench-cloudreve/cloudreve) | quench-cloudreve | 0.0.1 | Cloudreve: self-hosted file management and sharing with a web UI, storage polic… |
| 2026-11-15 14:09:30 | [ezbookkeeping](https://artifacthub.io/packages/helm/quench-ezbookkeeping/ezbookkeeping) | quench-ezbookkeeping | 0.0.1 | ezBookkeeping: self-hosted personal finance and bookkeeping with a web UI and P… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
