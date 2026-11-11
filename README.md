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

## Latest list — 2026-11-11 14:20 UTC

New charts added between 2026-11-11 13:19 UTC and 2026-11-11 14:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-11T14-20-26-762273Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-11 13:44:45 | [mitmproxy](https://artifacthub.io/packages/helm/quench-mitmproxy/mitmproxy) | quench-mitmproxy | 0.0.1 | mitmproxy, the interactive TLS-intercepting HTTP proxy for debugging and testin… |
| 2026-11-11 14:16:47 | [openziti](https://artifacthub.io/packages/helm/quench-openziti/openziti) | quench-openziti | 0.0.1 | OpenZiti, a zero-trust overlay network that replaces VPNs and open inbound port… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
