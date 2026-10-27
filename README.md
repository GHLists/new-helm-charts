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

## Latest list — 2026-10-27 00:21 UTC

New charts added between 2026-10-26 23:20 UTC and 2026-10-27 00:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-27T00-21-24-566565Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-27 00:01:13 | [solr](https://artifacthub.io/packages/helm/apache-solr-cloud/solr) | apache-solr-cloud | 0.8.1 | A SolrCloud cluster running on Kubernetes via the Solr Operator |
| 2026-10-27 00:01:13 | [solr-operator](https://artifacthub.io/packages/helm/apache-solr-operator/solr-operator) | apache-solr-operator | 0.9.1 | The Solr Operator enables easy management of Solr resources within Kubernetes. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
