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

## Latest list — 2026-11-15 18:19 UTC

New charts added between 2026-11-15 17:19 UTC and 2026-11-15 18:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T18-19-04-666275Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 17:21:30 | [soju](https://artifacthub.io/packages/helm/quench-soju/soju) | quench-soju | 0.0.1 | soju: an IRC bouncer that keeps users connected to their networks and plays bac… |
| 2026-11-15 17:38:30 | [go-httpbin](https://artifacthub.io/packages/helm/quench-go-httpbin/go-httpbin) | quench-go-httpbin | 0.0.1 | go-httpbin: httpbin in one Go binary, an HTTP request and response test service… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
