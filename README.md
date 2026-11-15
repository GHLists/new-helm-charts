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

## Latest list — 2026-11-15 01:21 UTC

New charts added between 2026-11-15 00:21 UTC and 2026-11-15 01:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T01-21-19-106014Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 00:50:31 | [pocket-id](https://artifacthub.io/packages/helm/quench-pocket-id/pocket-id) | quench-pocket-id | 0.0.1 | Pocket ID: a simple OIDC provider whose users sign in with passkeys only, with… |
| 2026-11-15 01:03:35 | [beszel](https://artifacthub.io/packages/helm/quench-beszel/beszel) | quench-beszel | 0.0.1 | Beszel: lightweight server monitoring, a hub (PocketBase plus a web UI) with th… |
| 2026-11-15 01:15:32 | [opengist](https://artifacthub.io/packages/helm/quench-opengist/opengist) | quench-opengist | 0.0.1 | Opengist: a self-hosted pastebin backed by Git, with a web UI, search and git o… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
