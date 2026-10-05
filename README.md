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

## Latest list — 2026-10-05 15:20 UTC

New charts added between 2026-10-05 14:21 UTC and 2026-10-05 15:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-05T15-20-07-877519Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-05 14:33:39 | [mongo-express](https://artifacthub.io/packages/helm/quench-mongo-express/mongo-express) | quench-mongo-express | 0.0.1 | Mongo Express, the web admin UI for MongoDB and FerretDB, behind generated basi… |
| 2026-10-05 14:33:40 | [profiling-stack](https://artifacthub.io/packages/helm/quench-profiling-stack/profiling-stack) | quench-profiling-stack | 0.0.2 | Hardened continuous profiling stack: Grafana Pyroscope (profile store and query… |
| 2026-10-05 15:10:53 | [trust-manager](https://artifacthub.io/packages/helm/quench-trust-manager/trust-manager) | quench-trust-manager | 0.0.2 | trust-manager, cert-manager's trust bundle distributor: a Bundle gathers CA cer… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
