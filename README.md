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

## Latest list — 2026-10-21 08:20 UTC

New charts added between 2026-10-21 07:22 UTC and 2026-10-21 08:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-21T08-20-05-388901Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-21 07:33:10 | [github-exporter](https://artifacthub.io/packages/helm/spnngl-github-exporter/github-exporter) | spnngl-github-exporter | 0.1.0 | Prometheus exporter for GitHub repository, organization and build status metric… |
| 2026-10-21 07:47:19 | [documenso](https://artifacthub.io/packages/helm/helmforge/documenso) | helmforge | 1.0.0 | Production-ready Documenso document signing with PostgreSQL, BullMQ, object sto… |
| 2026-10-21 07:47:19 | [docuseal](https://artifacthub.io/packages/helm/helmforge/docuseal) | helmforge | 1.0.0 | Production-ready DocuSeal electronic signatures with PostgreSQL, Redis, and dur… |
| 2026-10-21 08:00:03 | [ibm-odm-metering](https://artifacthub.io/packages/helm/ibm-odm-metering/ibm-odm-metering) | ibm-odm-metering | 1.0.0 | IBM Operational Decision Manager for Developers License By installing this prod… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
