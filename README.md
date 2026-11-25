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

## Latest list — 2026-11-25 08:19 UTC

New charts added between 2026-11-25 07:20 UTC and 2026-11-25 08:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-25T08-19-04-314289Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-25 07:28:36 | [novacaap](https://artifacthub.io/packages/helm/acute/novacaap) | acute | 1.0.0 | Flexible chart for deploying apps as Deployment, StatefulSet, Job, or CronJob |
| 2026-11-25 07:29:26 | [data-diode-connector-egress](https://artifacthub.io/packages/helm/ffutop/data-diode-connector-egress) | ffutop | 1.0.0 | A Helm chart for Kubernetes to deploy the Data Diode Connector Egress. Securely… |
| 2026-11-25 07:29:26 | [data-diode-connector-ingress](https://artifacthub.io/packages/helm/ffutop/data-diode-connector-ingress) | ffutop | 1.0.0 | A Helm chart for Kubernetes to deploy the Data Diode Connector Ingress. Designe… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
