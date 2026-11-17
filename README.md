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

## Latest list — 2026-11-17 19:20 UTC

New charts added between 2026-11-17 18:19 UTC and 2026-11-17 19:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-17T19-20-47-375439Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-17 18:50:32 | [netbird](https://artifacthub.io/packages/helm/quench-netbird/netbird) | quench-netbird | 0.0.1 | NetBird: a WireGuard mesh VPN with SSO, access control and routing peers. Manag… |
| 2026-11-17 19:15:45 | [vpn-stack](https://artifacthub.io/packages/helm/quench-vpn-stack/vpn-stack) | quench-vpn-stack | 0.0.1 | A self-hosted VPN: NetBird (WireGuard mesh with single sign-on, access policies… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
