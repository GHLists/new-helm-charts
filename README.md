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

## Latest list — 2026-11-09 13:20 UTC

New charts added between 2026-11-09 12:20 UTC and 2026-11-09 13:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-09T13-20-50-815365Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-09 12:31:39 | [lockstep](https://artifacthub.io/packages/helm/lockstep/lockstep) | lockstep | 0.1.0 | Compare, inspect and sync KV secrets across HashiCorp Vault clusters. |
| 2026-11-09 13:09:41 | [contour](https://artifacthub.io/packages/helm/quench-contour/contour) | quench-contour | 0.0.11 | Project Contour, the CNCF Kubernetes ingress controller that programs an Envoy… |
| 2026-11-09 13:15:45 | [renplay](https://artifacthub.io/packages/helm/renplay/renplay) | renplay | 4.6.2 | Play downloaded Ren'Py visual novels in your browser with server saves |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
