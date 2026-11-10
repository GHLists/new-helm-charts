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

## Latest list — 2026-11-10 20:22 UTC

New charts added between 2026-11-10 19:21 UTC and 2026-11-10 20:22 UTC.

[Full CSV](data/new-helm-charts-2026-11-10T20-22-35-186071Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-10 19:30:13 | [argocd-generator](https://artifacthub.io/packages/helm/argocd-generator/argocd-generator) | argocd-generator | 1.0.0 | ApplicationSet plugin generator that turns what ArtefactFlow reports as deploye… |
| 2026-11-10 19:51:45 | [ankra-cloud-cosi](https://artifacthub.io/packages/helm/ankra-charts/ankra-cloud-cosi) | ankra-charts | 0.1.0 | COSI driver cosi.ankra.cloud for Ankra Cloud object storage (S3 buckets from Bu… |
| 2026-11-10 19:51:45 | [cloudflare-operator](https://artifacthub.io/packages/helm/ankra-charts/cloudflare-operator) | ankra-charts | 0.2.0 | Helm chart for the community Cloudflare Operator (adyanth/cloudflare-operator)… |
| 2026-11-10 19:51:45 | [gateway-api-crds](https://artifacthub.io/packages/helm/ankra-charts/gateway-api-crds) | ankra-charts | 1.5.1 | Kubernetes Gateway API CRDs (standard channel) as a small Helm chart, vendored… |
| 2026-11-10 19:51:45 | [isms-builder](https://artifacthub.io/packages/helm/ankra-charts/isms-builder) | ankra-charts | 0.1.0 | ISMS Builder on Kubernetes - the open-source ISO 27001 / NIS2 ISMS template bui… |
| 2026-11-10 20:03:35 | [onicost-agent](https://artifacthub.io/packages/helm/onicost/onicost-agent) | onicost | 0.6.0 | Onicost agent, which collects the inventory, the GPU capacity, the size of AWS… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
