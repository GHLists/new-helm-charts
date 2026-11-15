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

## Latest list — 2026-11-15 13:20 UTC

New charts added between 2026-11-15 12:20 UTC and 2026-11-15 13:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T13-20-55-513457Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 12:28:04 | [signoz-mcp-server](https://artifacthub.io/packages/helm/signoz/signoz-mcp-server) | signoz | 0.0.1-rc.1 | Helm chart for the SigNoz MCP server |
| 2026-11-15 12:32:30 | [adguardhome](https://artifacthub.io/packages/helm/quench-adguardhome/adguardhome) | quench-adguardhome | 0.0.1 | AdGuard Home: a network-wide ad and tracker blocking DNS server with a web UI,… |
| 2026-11-15 12:40:31 | [domain-locker](https://artifacthub.io/packages/helm/domain-locker/domain-locker) | domain-locker | 0.3.8 | A Helm chart for deploying Domain Locker |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
