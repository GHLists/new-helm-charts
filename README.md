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

## Latest list — 2026-10-28 21:21 UTC

New charts added between 2026-10-28 20:21 UTC and 2026-10-28 21:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-28T21-21-11-636553Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-28 20:30:04 | [agent-bom](https://artifacthub.io/packages/helm/agent-bom/agent-bom) | agent-bom | 0.109.0 | Open security scanner and graph for AI supply chain and infrastructure — discov… |
| 2026-10-28 21:04:21 | [spark-connect](https://artifacthub.io/packages/helm/spark-connect/spark-connect) | spark-connect | 1.0.0 | Apache Spark Connect server on Kubernetes, with executor pods started by the dr… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
