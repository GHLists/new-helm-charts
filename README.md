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

## Latest list — 2026-11-16 14:20 UTC

New charts added between 2026-11-16 13:19 UTC and 2026-11-16 14:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-16T14-20-23-94253Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-16 13:38:42 | [donetick](https://artifacthub.io/packages/helm/quench-donetick/donetick) | quench-donetick | 0.0.1 | donetick: chore and task manager for households and teams with recurring schedu… |
| 2026-11-16 14:02:32 | [karpenter-crd](https://artifacthub.io/packages/helm/karpenter-provider-gcp-crd/karpenter-crd) | karpenter-provider-gcp-… | 0.6.0 | Karpenter GCP CRD chart - installs and upgrades Karpenter CustomResourceDefinit… |
| 2026-11-16 14:02:33 | [karpenter](https://artifacthub.io/packages/helm/karpenter-provider-gcp/karpenter) | karpenter-provider-gcp | 0.1.0-rc.0 | Karpenter GCP Cloud Provider — cost-efficient autoscaling for GKE clusters |
| 2026-11-16 14:03:40 | [apprise-api](https://artifacthub.io/packages/helm/quench-apprise-api/apprise-api) | quench-apprise-api | 0.0.1 | Apprise API: one REST call to notify 100+ services (email, Slack, Discord, Tele… |
| 2026-11-16 14:03:46 | [rampart](https://artifacthub.io/packages/helm/rampart/rampart) | rampart | 0.1.0 | Rampart Cloud-Native Application Security Posture Management (ASPM) Platform |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
