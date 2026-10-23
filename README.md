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

## Latest list — 2026-10-23 16:19 UTC

New charts added between 2026-10-23 15:19 UTC and 2026-10-23 16:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-23T16-19-30-381119Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-23 16:00:59 | [kratix](https://artifacthub.io/packages/helm/syntasso/kratix) | syntasso | 0.0.1 | A Helm chart for installing Kratix (https://kratix.io) |
| 2026-10-23 16:02:58 | [maintenant](https://artifacthub.io/packages/helm/maintenant/maintenant) | maintenant | 1.10.0 | Self-discovering infrastructure monitoring for Docker and Kubernetes |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
