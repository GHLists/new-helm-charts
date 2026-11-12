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

## Latest list — 2026-11-12 18:20 UTC

New charts added between 2026-11-12 17:19 UTC and 2026-11-12 18:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-12T18-20-29-755761Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-12 17:44:39 | [vaultwarden](https://artifacthub.io/packages/helm/quench-vaultwarden/vaultwarden) | quench-vaultwarden | 0.0.1 | Vaultwarden: a Bitwarden-compatible password manager server for the official cl… |
| 2026-11-12 18:11:36 | [kanboard](https://artifacthub.io/packages/helm/quench-kanboard/kanboard) | quench-kanboard | 0.0.1 | Kanboard: Kanban project management with swimlanes, automatic actions, plugins… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
