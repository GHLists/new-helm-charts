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

## Latest list — 2026-10-26 14:20 UTC

New charts added between 2026-10-26 13:22 UTC and 2026-10-26 14:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-26T14-20-25-080545Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-26 13:38:55 | [eck-operator](https://artifacthub.io/packages/helm/adeptia-automate-eck-operator/eck-operator) | adeptia-automate-eck-op… | 3.5.0 | Elastic Cloud on Kubernetes (ECK) operator |
| 2026-10-26 13:38:59 | [opentelemetry-operator](https://artifacthub.io/packages/helm/adeptia-automate-opentelemetry-operator/opentelemetry-operator) | adeptia-automate-opente… | 0.122.0 | OpenTelemetry Operator Helm chart for Kubernetes |
| 2026-10-26 13:39:03 | [kube-prometheus-stack](https://artifacthub.io/packages/helm/adeptia-automate-prometheus-stack/kube-prometheus-stack) | adeptia-automate-promet… | 88.6.2 | kube-prometheus-stack collects Kubernetes manifests, Grafana dashboards, and Pr… |
| 2026-10-26 13:46:06 | [bayplan](https://artifacthub.io/packages/helm/bayplan/bayplan) | bayplan | 0.1.0 | Lightweight, self-hosted multi-cluster Kubernetes management. One binary (Go +… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
