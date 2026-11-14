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

## Latest list — 2026-11-14 09:21 UTC

New charts added between 2026-11-14 08:18 UTC and 2026-11-14 09:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-14T09-21-18-670417Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-14 08:22:12 | [temporal-ui](https://artifacthub.io/packages/helm/quench-temporal-ui/temporal-ui) | quench-temporal-ui | 0.0.1 | Temporal UI: the web UI for a Temporal cluster (workflows and their event histo… |
| 2026-11-14 08:32:38 | [automation-stack](https://artifacthub.io/packages/helm/quench-automation-stack/automation-stack) | quench-automation-stack | 0.0.1 | n8n in queue mode with PostgreSQL and Valkey: workflow automation that scales o… |
| 2026-11-14 08:50:37 | [workflow-stack](https://artifacthub.io/packages/helm/quench-workflow-stack/workflow-stack) | quench-workflow-stack | 0.0.1 | Temporal with PostgreSQL and the Temporal UI: durable workflow orchestration wi… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
