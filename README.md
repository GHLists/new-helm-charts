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

## Latest list — 2026-11-18 21:19 UTC

New charts added between 2026-11-18 20:21 UTC and 2026-11-18 21:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-18T21-19-58-622666Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-18 20:24:16 | [cluster-rhbk](https://artifacthub.io/packages/helm/startx/cluster-rhbk) | startx | 21.3.370 | Helm chart used to configure Red Hat build of Keycloak (RHBK) at the cluster le… |
| 2026-11-18 20:30:09 | [allure-docker-service](https://artifacthub.io/packages/helm/allure-docker-service-chart/allure-docker-service) | allure-docker-service-c… | 1.0.1 | Allure Docker Service on Kubernetes, with optional Allure UI, ingress and persi… |
| 2026-11-18 20:53:43 | [pangolin-cli](https://artifacthub.io/packages/helm/fosrl/pangolin-cli) | fosrl | 0.1.0 | Helm chart to run Pangolin sites with the Pangolin CLI (fosrl/cli) |
| 2026-11-18 21:04:17 | [rabbitmq-stomp](https://artifacthub.io/packages/helm/rabbitmq-stomp-chart/rabbitmq-stomp) | rabbitmq-stomp-chart | 1.0.0 | Single-node RabbitMQ with the management, STOMP and Web STOMP plugins, using th… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
