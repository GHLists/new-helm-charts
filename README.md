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

## Latest list — 2026-10-19 14:22 UTC

New charts added between 2026-10-19 13:19 UTC and 2026-10-19 14:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-19T14-22-00-568936Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-19 13:21:03 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |
| 2026-10-19 13:46:16 | [ibm-opencontent-flink-migration](https://artifacthub.io/packages/helm/ibm-helm/ibm-opencontent-flink-migration) | ibm-helm | 0.0.2022 | A Helm chart for migrating the IBM OpenContent Flink Operator from OLM to Helm |
| 2026-10-19 14:03:41 | [camel-k](https://artifacthub.io/packages/helm/quench-camel-k/camel-k) | quench-camel-k | 0.0.1 | Apache Camel K operator: build and run Camel integrations on Kubernetes from CR… |
| 2026-10-19 14:09:42 | [selenium-grid](https://artifacthub.io/packages/helm/quench-selenium-grid/selenium-grid) | quench-selenium-grid | 0.0.2 | Selenium Grid 4, the WebDriver grid for browser automation: a hub (router, dist… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
