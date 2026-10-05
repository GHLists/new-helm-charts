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

## Latest list — 2026-10-05 19:22 UTC

New charts added between 2026-10-05 18:21 UTC and 2026-10-05 19:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-05T19-22-08-966101Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-05 18:31:35 | [krm-foyer](https://artifacthub.io/packages/helm/krm-foyer/krm-foyer) | krm-foyer | 0.2.0 | Browser login, Kubernetes API access and live resources on one origin, with eve… |
| 2026-10-05 19:16:28 | [subnet-operator](https://artifacthub.io/packages/helm/subnet-operator/subnet-operator) | subnet-operator | 2.0.0 | Kubernetes operator that discovers cloud networks and subnets (AWS and Google C… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
