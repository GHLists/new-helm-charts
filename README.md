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

## Latest list — 2026-10-26 15:21 UTC

New charts added between 2026-10-26 14:20 UTC and 2026-10-26 15:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-26T15-21-34-424498Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-26 14:22:41 | [mo-platform-tests](https://artifacthub.io/packages/helm/mogenius/mo-platform-tests) | mogenius | 1.0.0 | The mo-platform-tests operator with its UI. Needs nothing but its own namespace. |
| 2026-10-26 14:44:57 | [cinny](https://artifacthub.io/packages/helm/spnngl-cinny/cinny) | spnngl-cinny | 0.1.0 | Cinny, a Matrix web client, as a hardened stateless Deployment serving its stat… |
| 2026-10-26 15:04:33 | [sable-next](https://artifacthub.io/packages/helm/spnngl-sable-next/sable-next) | spnngl-sable-next | 0.1.0 | Sable, a Matrix web client, as a hardened stateless Deployment serving its stat… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
