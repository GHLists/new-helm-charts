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

## Latest list — 2026-10-24 04:21 UTC

New charts added between 2026-10-24 03:21 UTC and 2026-10-24 04:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-24T04-21-31-874097Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-24 03:59:06 | [libredb-platform](https://artifacthub.io/packages/helm/libredb-platform/libredb-platform) | libredb-platform | 1.1.1 | LibreDB Platform, database access governance, with LibreDB Studio, on Kubernete… |
| 2026-10-24 04:02:54 | [libredb-platform](https://artifacthub.io/packages/helm/libredb-platform-oci/libredb-platform) | libredb-platform-oci | 1.1.1 | LibreDB Platform, database access governance, with LibreDB Studio, on Kubernete… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
