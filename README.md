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

## Latest list — 2026-10-31 01:19 UTC

New charts added between 2026-10-31 00:20 UTC and 2026-10-31 01:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-31T01-19-59-392329Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-31 00:42:17 | [cloudflare-operator](https://artifacthub.io/packages/helm/ankra-charts/cloudflare-operator) | ankra-charts | 0.2.0 | Helm chart for the community Cloudflare Operator (adyanth/cloudflare-operator)… |
| 2026-10-31 00:42:17 | [isms-builder](https://artifacthub.io/packages/helm/ankra-charts/isms-builder) | ankra-charts | 0.1.0 | ISMS Builder on Kubernetes - the open-source ISO 27001 / NIS2 ISMS template bui… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
