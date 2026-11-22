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

## Latest list — 2026-11-22 20:20 UTC

New charts added between 2026-11-22 19:19 UTC and 2026-11-22 20:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-22T20-20-48-889278Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-22 19:21:29 | [zap](https://artifacthub.io/packages/helm/quench-zap/zap) | quench-zap | 0.0.1 | OWASP ZAP: web application security scanner as an API daemon (spider, passive a… |
| 2026-11-22 19:32:29 | [etherpad](https://artifacthub.io/packages/helm/quench-etherpad/etherpad) | quench-etherpad | 0.0.2 | Etherpad: real-time collaborative document editing with plugins, an HTTP API an… |
| 2026-11-22 19:32:36 | [pentagi](https://artifacthub.io/packages/helm/quench-pentagi/pentagi) | quench-pentagi | 0.0.2 | PentAGI: autonomous AI agents for penetration testing, running their tools in c… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
