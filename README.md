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

## Latest list — 2026-11-15 05:18 UTC

New charts added between 2026-11-15 04:18 UTC and 2026-11-15 05:18 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T05-18-50-190168Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 04:50:24 | [croc](https://artifacthub.io/packages/helm/quench-croc/croc) | quench-croc | 0.0.1 | croc relay: a self-hosted relay for croc, which sends files between two compute… |
| 2026-11-15 04:50:24 | [privatebin](https://artifacthub.io/packages/helm/quench-privatebin/privatebin) | quench-privatebin | 0.0.1 | PrivateBin: a minimalist pastebin where the server has zero knowledge of the da… |
| 2026-11-15 05:15:29 | [inbucket](https://artifacthub.io/packages/helm/quench-inbucket/inbucket) | quench-inbucket | 0.0.1 | Inbucket: a disposable-email testing server that accepts mail for any address o… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
