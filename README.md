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

## Latest list — 2026-10-17 13:20 UTC

New charts added between 2026-10-17 12:19 UTC and 2026-10-17 13:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-17T13-20-27-524491Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-17 12:24:47 | [saleor](https://artifacthub.io/packages/helm/upstreamyard/saleor) | upstreamyard | 0.1.0 | Saleor, the headless GraphQL commerce platform (API, Celery worker and beat, da… |
| 2026-10-17 12:34:03 | [parse-server](https://artifacthub.io/packages/helm/upstreamyard/parse-server) | upstreamyard | 0.1.0 | Parse Server, the open-source backend for mobile, web and IoT apps. Community c… |
| 2026-10-17 12:34:58 | [logto](https://artifacthub.io/packages/helm/upstreamyard/logto) | upstreamyard | 0.1.0 | Logto, the open-source identity and access management platform (OIDC, SSO, mult… |
| 2026-10-17 12:35:57 | [kvrocks](https://artifacthub.io/packages/helm/upstreamyard/kvrocks) | upstreamyard | 0.1.0 | Apache Kvrocks Helm chart for Kubernetes. Redis-compatible key-value database o… |
| 2026-10-17 12:36:58 | [falkordb](https://artifacthub.io/packages/helm/upstreamyard/falkordb) | upstreamyard | 0.1.0 | FalkorDB Helm chart for Kubernetes. Graph database (openCypher, GraphRAG, knowl… |
| 2026-10-17 12:38:09 | [electric](https://artifacthub.io/packages/helm/upstreamyard/electric) | upstreamyard | 0.1.0 | Electric sync engine, which syncs subsets of your PostgreSQL data to web and mo… |
| 2026-10-17 12:41:49 | [dolt](https://artifacthub.io/packages/helm/upstreamyard/dolt) | upstreamyard | 0.1.0 | Dolt Helm chart for Kubernetes. The version-controlled, MySQL-compatible SQL da… |
| 2026-10-17 12:45:35 | [discourse](https://artifacthub.io/packages/helm/upstreamyard/discourse) | upstreamyard | 0.1.0 | Discourse, the open-source community forum. Community chart by upstreamyard, no… |
| 2026-10-17 12:46:57 | [docling-serve](https://artifacthub.io/packages/helm/upstreamyard/docling-serve) | upstreamyard | 0.1.0 | Docling Serve Helm chart for Kubernetes. Document conversion API (PDF, DOCX, PP… |
| 2026-10-17 13:15:11 | [cube](https://artifacthub.io/packages/helm/upstreamyard/cube) | upstreamyard | 0.1.0 | Cube, the open-source semantic layer and data API for BI and AI, with Cube Stor… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
