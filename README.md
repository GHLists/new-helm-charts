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

## Latest list — 2026-09-29 09:19 UTC

New charts added between 2026-09-29 08:28 UTC and 2026-09-29 09:19 UTC.

[Full CSV](data/new-helm-charts-2026-09-29T09-19-40-63408Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-29 08:32:27 | [observability-extras](https://artifacthub.io/packages/helm/observability-extras/observability-extras) | observability-extras | 0.1.1 | Content pack for the observability stack — dashboards, contracts and alert rule… |
| 2026-09-29 08:32:28 | [observability-core](https://artifacthub.io/packages/helm/observability-core/observability-core) | observability-core | 0.1.0 | Umbrella chart for the observability storage core (VictoriaMetrics / VictoriaLo… |
| 2026-09-29 08:32:29 | [observability-collect](https://artifacthub.io/packages/helm/observability-collect/observability-collect) | observability-collect | 0.1.0 | Umbrella chart for the observability collection core (vmagent / vlagent / vtage… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
