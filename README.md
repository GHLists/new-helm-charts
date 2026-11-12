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

## Latest list — 2026-11-12 05:19 UTC

New charts added between 2026-11-12 04:19 UTC and 2026-11-12 05:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-12T05-19-18-009686Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-12 04:32:31 | [3proxy](https://artifacthub.io/packages/helm/quench-3proxy/3proxy) | quench-3proxy | 0.0.1 | 3proxy: a tiny multi-protocol proxy suite (HTTP and SOCKS4/5 proxies, port mapp… |
| 2026-11-12 05:03:32 | [chisel](https://artifacthub.io/packages/helm/quench-chisel/chisel) | quench-chisel | 0.0.1 | chisel: a fast TCP/UDP tunnel over HTTP, SSH-encrypted, for reaching services b… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
