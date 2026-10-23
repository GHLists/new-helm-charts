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

## Latest list — 2026-10-23 20:19 UTC

New charts added between 2026-10-23 19:19 UTC and 2026-10-23 20:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-23T20-19-45-50651Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-23 19:30:43 | [codesynapse](https://artifacthub.io/packages/helm/codesynapse/codesynapse) | codesynapse | 0.0.1 | CodeSynapse indexes code, docs, configuration and dependencies into a graph and… |
| 2026-10-23 19:31:30 | [gateway-auto-listener](https://artifacthub.io/packages/helm/itsh-gateway-auto-listener/gateway-auto-listener) | itsh-gateway-auto-liste… | 0.2.5 | Kubernetes controller that auto-creates Gateway HTTPS listeners from HTTPRoutes |
| 2026-10-23 19:31:30 | [karpenter-provider-hcloud](https://artifacthub.io/packages/helm/itsh-karpenter-provider-hcloud/karpenter-provider-hcloud) | itsh-karpenter-provider… | 0.1.0-alpha.1 | Karpenter cloud provider for Hetzner Cloud |
| 2026-10-23 19:31:30 | [stalwart](https://artifacthub.io/packages/helm/itsh-stalwart/stalwart) | itsh-stalwart | 0.4.0 | Helm chart for Stalwart Mail Server (0.16+ datastore config model) |
| 2026-10-23 19:41:25 | [rowflare](https://artifacthub.io/packages/helm/rowflare/rowflare) | rowflare | 0.1.0 | Rowflare, an open-source Airtable alternative. Runs the Rowflare Docker image w… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
