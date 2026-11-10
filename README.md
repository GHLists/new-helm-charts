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

## Latest list — 2026-11-10 10:21 UTC

New charts added between 2026-11-10 09:21 UTC and 2026-11-10 10:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-10T10-21-38-723824Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-10 09:44:46 | [cluster-cudn](https://artifacthub.io/packages/helm/startx/cluster-cudn) | startx | 21.3.361 | Configure OVN-Kubernetes user-defined networks (ClusterUserDefinedNetwork and U… |
| 2026-11-10 09:44:46 | [cluster-dell-csm](https://artifacthub.io/packages/helm/startx/cluster-dell-csm) | startx | 21.3.361 | Configure the Dell Container Storage Modules (CSM) operator and a Dell CSI stor… |
| 2026-11-10 09:44:49 | [cluster-loki](https://artifacthub.io/packages/helm/startx/cluster-loki) | startx | 21.3.361 | Configure the Loki log store (LokiStack) of OpenShift Logging with the Red Hat… |
| 2026-11-10 09:44:50 | [cluster-network-observability](https://artifacthub.io/packages/helm/startx/cluster-network-observability) | startx | 21.3.361 | Configure the Network Observability operator and its FlowCollector to collect a… |
| 2026-11-10 09:44:52 | [cluster-unifai](https://artifacthub.io/packages/helm/startx/cluster-unifai) | startx | 21.3.361 | Helm chart used to configure UnifAI multi-agent AI platform at the cluster level |
| 2026-11-10 10:03:06 | [nginx-static](https://artifacthub.io/packages/helm/nginx-static/nginx-static) | nginx-static | 0.2.1 | Helm chart for deploying a static nginx-served website with optional HPA-driven… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
