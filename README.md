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

## Latest list — 2026-11-15 16:21 UTC

New charts added between 2026-11-15 15:22 UTC and 2026-11-15 16:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T16-21-02-871503Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 15:30:38 | [cnpg-restore-check](https://artifacthub.io/packages/helm/cnpg-restore-check/cnpg-restore-check) | cnpg-restore-check | 0.1.0 | Scheduled restore checks for CloudNativePG backups made with plugin-barman-cloud |
| 2026-11-15 15:44:29 | [mercure](https://artifacthub.io/packages/helm/quench-mercure/mercure) | quench-mercure | 0.0.1 | Mercure: a real-time push hub (server-sent events) with JWT-authorised publishi… |
| 2026-11-15 15:52:26 | [openbao-config-operator](https://artifacthub.io/packages/helm/openbao-config-operator/openbao-config-operator) | openbao-config-operator | 0.1.1 | Manage the configuration of an existing OpenBao server through Kubernetes custo… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
