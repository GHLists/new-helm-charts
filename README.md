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

## Latest list — 2026-10-28 16:19 UTC

New charts added between 2026-10-28 15:21 UTC and 2026-10-28 16:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-28T16-19-57-393026Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-28 15:24:27 | [cluster-percona](https://artifacthub.io/packages/helm/startx/cluster-percona) | startx | 21.3.309 | Helm chart used to configure highly available PostgreSQL clusters using the Per… |
| 2026-10-28 15:33:47 | [brickie](https://artifacthub.io/packages/helm/hatchet/brickie) | hatchet | 0.1.0 | Hatchet sandbox provider. Runs agent sandboxes as Hatchet tasks on Kubernetes,… |
| 2026-10-28 15:35:44 | [common](https://artifacthub.io/packages/helm/criblio/common) | criblio | 1.0.0 | Common templates for Cribl Helm Charts |
| 2026-10-28 15:35:44 | [pod-killer](https://artifacthub.io/packages/helm/criblio/pod-killer) | criblio | 1.0.0 | A Simple Cron Job that deletes pods based on pod name on a schedule defined in… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
