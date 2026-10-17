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

## Latest list — 2026-10-17 12:19 UTC

New charts added between 2026-10-17 11:20 UTC and 2026-10-17 12:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-17T12-19-14-822227Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-17 11:22:40 | [xxl-job](https://artifacthub.io/packages/helm/upstreamyard/xxl-job) | upstreamyard | 0.1.1 | XXL-JOB admin (scheduling center), the distributed job scheduler for Java servi… |
| 2026-10-17 11:49:05 | [kube-arr](https://artifacthub.io/packages/helm/simplyzee/kube-arr) | simplyzee | 0.2.0 | Your *arr media stack on Kubernetes. Sonarr, Radarr, Prowlarr, Bazarr, Jackett,… |
| 2026-10-17 11:53:10 | [supertokens](https://artifacthub.io/packages/helm/upstreamyard/supertokens) | upstreamyard | 0.1.0 | SuperTokens core, the open-source authentication server (sessions, email/passwo… |
| 2026-10-17 11:53:10 | [tigerbeetle](https://artifacthub.io/packages/helm/upstreamyard/tigerbeetle) | upstreamyard | 0.1.0 | TigerBeetle Helm chart for Kubernetes. Fault-tolerant 3 or 6 replica TigerBeetl… |
| 2026-10-17 11:57:04 | [shardingsphere-proxy](https://artifacthub.io/packages/helm/upstreamyard/shardingsphere-proxy) | upstreamyard | 0.1.0 | Apache ShardingSphere-Proxy, the database proxy for sharding, read/write splitt… |
| 2026-10-17 11:57:48 | [postal](https://artifacthub.io/packages/helm/upstreamyard/postal) | upstreamyard | 0.1.0 | Postal, the open-source mail delivery platform for sending and receiving email… |
| 2026-10-17 11:58:26 | [plano](https://artifacthub.io/packages/helm/upstreamyard/plano) | upstreamyard | 0.1.0 | Plano Helm chart for Kubernetes. Plano (formerly archgw) is an AI gateway and L… |
| 2026-10-17 11:58:34 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
