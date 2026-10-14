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

## Latest list — 2026-10-14 11:21 UTC

New charts added between 2026-10-14 10:21 UTC and 2026-10-14 11:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-14T11-21-55-936474Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-14 10:34:45 | [krevo-local-storage](https://artifacthub.io/packages/helm/krevopilot/krevo-local-storage) | krevopilot | 0.1.0 | Optional customer-hosted logs and Kubernetes events for KrevoPilot (pilot) |
| 2026-10-14 10:39:13 | [plone](https://artifacthub.io/packages/helm/quench-plone/plone) | quench-plone | 0.0.2 | The Plone 6 backend (Zope with the plone.restapi REST API that Volto talks to),… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
