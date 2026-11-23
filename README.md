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

## Latest list — 2026-11-23 17:20 UTC

New charts added between 2026-11-23 16:18 UTC and 2026-11-23 17:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-23T17-20-52-95646Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-23 16:32:56 | [weaviate-otel-collector](https://artifacthub.io/packages/helm/weaviate/weaviate-otel-collector) | weaviate | 17.9.0 | Pushes aggregate Weaviate metrics to Weaviate Cloud (OSS "Cloud Connect"). |
| 2026-11-23 16:52:47 | [cvedetector](https://artifacthub.io/packages/helm/huseyinbabal/cvedetector) | huseyinbabal | 0.3.1 | Maps running container images to known CVEs using a published feed. No image sc… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
