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

## Latest list — 2026-11-11 08:20 UTC

New charts added between 2026-11-11 07:19 UTC and 2026-11-11 08:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-11T08-20-32-04895Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-11 07:38:36 | [gost](https://artifacthub.io/packages/helm/quench-gost/gost) | quench-gost | 0.0.1 | GOST (GO Simple Tunnel): a multi-protocol forward proxy and tunnel (HTTP, SOCKS… |
| 2026-11-11 08:03:35 | [cloudflared](https://artifacthub.io/packages/helm/quench-cloudflared/cloudflared) | quench-cloudflared | 0.0.1 | cloudflared, the Cloudflare Tunnel client: publishes in-cluster services throug… |
| 2026-11-11 08:03:35 | [frp](https://artifacthub.io/packages/helm/quench-frp/frp) | quench-frp | 0.0.1 | frp server (frps): a fast reverse proxy that exposes services behind NAT or a f… |
| 2026-11-11 08:15:33 | [vouch-proxy](https://artifacthub.io/packages/helm/quench-vouch-proxy/vouch-proxy) | quench-vouch-proxy | 0.0.1 | Vouch Proxy: SSO for nginx auth_request. Logs users in through OIDC or OAuth (G… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
