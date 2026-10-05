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

## Latest list — 2026-10-05 13:22 UTC

New charts added between 2026-10-05 12:19 UTC and 2026-10-05 13:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-05T13-22-32-157951Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-05 13:17:02 | [agentgateway-crds](https://artifacthub.io/packages/helm/spnngl-agentgateway-crds/agentgateway-crds) | spnngl-agentgateway-crds | 1.5.0 | CustomResourceDefinitions for agentgateway (backends, models, parameters, polic… |
| 2026-10-05 13:17:02 | [cilium-crds](https://artifacthub.io/packages/helm/spnngl-cilium-crds/cilium-crds) | spnngl-cilium-crds | 1.20.2 | CustomResourceDefinitions for Cilium (cilium.io v2 and v2alpha1) |
| 2026-10-05 13:17:02 | [cluster-api-crds](https://artifacthub.io/packages/helm/spnngl-cluster-api-crds/cluster-api-crds) | spnngl-cluster-api-crds | 1.14.2 | CustomResourceDefinitions for Cluster API core (clusters, machines, ClusterClas… |
| 2026-10-05 13:17:02 | [external-dns-crds](https://artifacthub.io/packages/helm/spnngl-external-dns-crds/external-dns-crds) | spnngl-external-dns-crds | 0.23.0 | CustomResourceDefinitions for ExternalDNS (DNSEndpoint, DNSRecord) |
| 2026-10-05 13:17:02 | [external-secrets-crds](https://artifacthub.io/packages/helm/spnngl-external-secrets-crds/external-secrets-crds) | spnngl-external-secrets… | 2.11.0 | CustomResourceDefinitions for External Secrets Operator (stores, external/push… |
| 2026-10-05 13:17:02 | [gateway-api-crds](https://artifacthub.io/packages/helm/spnngl-gateway-api-crds/gateway-api-crds) | spnngl-gateway-api-crds | 1.6.2 | CustomResourceDefinitions for Kubernetes Gateway API, standard channel |
| 2026-10-05 13:17:02 | [gateway-api-exp-crds](https://artifacthub.io/packages/helm/spnngl-gateway-api-exp-crds/gateway-api-exp-crds) | spnngl-gateway-api-exp-… | 1.6.2 | CustomResourceDefinitions for Kubernetes Gateway API, experimental channel |
| 2026-10-05 13:17:02 | [orc-crds](https://artifacthub.io/packages/helm/spnngl-orc-crds/orc-crds) | spnngl-orc-crds | 2.6.0 | CustomResourceDefinitions for the OpenStack Resource Controller (ORC) |
| 2026-10-05 13:17:02 | [topolvm-crds](https://artifacthub.io/packages/helm/spnngl-topolvm-crds/topolvm-crds) | spnngl-topolvm-crds | 0.41.1 | CustomResourceDefinitions for TopoLVM (LogicalVolume, topolvm.io and legacy top… |
| 2026-10-05 13:17:02 | [velero-crds](https://artifacthub.io/packages/helm/spnngl-velero-crds/velero-crds) | spnngl-velero-crds | 1.18.4 | CustomResourceDefinitions for Velero (backups, restores, schedules, locations,… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
