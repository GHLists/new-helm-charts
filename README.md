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

## Latest list — 2026-10-08 14:24 UTC

New charts added between 2026-10-08 13:19 UTC and 2026-10-08 14:24 UTC.

[Full CSV](data/new-helm-charts-2026-10-08T14-24-44-904434Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-08 13:32:46 | [istio-cni](https://artifacthub.io/packages/helm/quench-istio-cni/istio-cni) | quench-istio-cni | 0.0.1 | Istio CNI node agent for ambient mode: a DaemonSet that chains the istio-cni pl… |
| 2026-10-08 13:32:47 | [mesh-stack](https://artifacthub.io/packages/helm/quench-mesh-stack/mesh-stack) | quench-mesh-stack | 0.0.1 | Istio ambient mesh in one install: istiod (control plane and certificate author… |
| 2026-10-08 13:32:49 | [ztunnel](https://artifacthub.io/packages/helm/quench-ztunnel/ztunnel) | quench-ztunnel | 0.0.1 | Istio ztunnel, the per-node L4 proxy of ambient mode: it gives every ambient po… |
| 2026-10-08 13:53:11 | [governance-policy-addon-controller](https://artifacthub.io/packages/helm/ocm-helm-charts/governance-policy-addon-controller) | ocm-helm-charts | 0.20.1 | The Governance Policy Add-on Controller is a policy framework hub controller an… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
