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

## Latest list — 2026-11-18 13:20 UTC

New charts added between 2026-11-18 12:21 UTC and 2026-11-18 13:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-18T13-20-03-484429Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-18 12:22:45 | [youtrack](https://artifacthub.io/packages/helm/youtrack/youtrack) | youtrack | 0.1.12 | A Helm chart to install YouTrack in your Kubernetes Cluster |
| 2026-11-18 12:49:46 | [cluster-eck](https://artifacthub.io/packages/helm/startx/cluster-eck) | startx | 21.3.362 | Configure the Elastic Cloud on Kubernetes (ECK) operator and the Elasticsearch… |
| 2026-11-18 12:49:49 | [cluster-metallb](https://artifacthub.io/packages/helm/startx/cluster-metallb) | startx | 21.3.362 | Configure the MetalLB operator and the load balancer address pools, layer 2 and… |
| 2026-11-18 12:49:50 | [cluster-prometheus](https://artifacthub.io/packages/helm/startx/cluster-prometheus) | startx | 21.3.362 | Configure the Cluster Observability Operator and the Prometheus monitoring stac… |
| 2026-11-18 12:49:53 | [unifai](https://artifacthub.io/packages/helm/startx/unifai) | startx | 21.3.363 | Deploy the UnifAI multi-agent AI platform on OpenShift or Kubernetes, by instal… |
| 2026-11-18 12:52:11 | [castai-config-sync](https://artifacthub.io/packages/helm/castai/castai-config-sync) | castai | 0.1.0-rc.1 | CAST AI Kubernetes operator for two-way sync of autoscaling policies, node conf… |
| 2026-11-18 12:59:19 | [openbao-config-operator](https://artifacthub.io/packages/helm/openbao-config-operator/openbao-config-operator) | openbao-config-operator | 1.0.0 | Manage existing OpenBao configuration declaratively with Kubernetes custom reso… |
| 2026-11-18 13:03:08 | [foundry-vtt](https://artifacthub.io/packages/helm/mahahe-foundry-vtt/foundry-vtt) | mahahe-foundry-vtt | 0.1.7 | Foundry Virtual Tabletop |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
