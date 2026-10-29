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

## Latest list — 2026-10-29 21:20 UTC

New charts added between 2026-10-29 20:21 UTC and 2026-10-29 21:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-29T21-20-26-897049Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-29 20:31:50 | [waf](https://artifacthub.io/packages/helm/light-waf/waf) | light-waf | 1.0.2 | Light WAF data plane (`waf-enterprise`) — a reverse-proxy Deployment that prote… |
| 2026-10-29 20:31:50 | [waf-controlplane](https://artifacthub.io/packages/helm/light-waf-controlplane/waf-controlplane) | light-waf-controlplane | 1.0.2 | Light WAF control plane — dashboard/API over the WAF telemetry (observability,… |
| 2026-10-29 21:01:53 | [elitea](https://artifacthub.io/packages/helm/elitea/elitea) | elitea | 7.1.0 | EliteA, as one chart. Installs the whole first-party platform — API, web, sched… |
| 2026-10-29 21:01:53 | [elitea-sandbox-runtime](https://artifacthub.io/packages/helm/elitea-sandbox-runtime/elitea-sandbox-runtime) | elitea-sandbox-runtime | 4.71.0 | Optional node-level installer for the sandbox runtime the EliteA cloud executor… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
