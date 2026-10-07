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

## Latest list — 2026-10-07 14:22 UTC

New charts added between 2026-10-07 13:22 UTC and 2026-10-07 14:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-07T14-22-04-827563Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-07 13:22:38 | [registry-stack](https://artifacthub.io/packages/helm/quench-registry-stack/registry-stack) | quench-registry-stack | 0.0.1 | One self-hosted artifact registry in one install: Harbor (container images and… |
| 2026-10-07 13:32:43 | [cnpg-stack](https://artifacthub.io/packages/helm/quench-cnpg-stack/cnpg-stack) | quench-cnpg-stack | 0.0.1 | Operator-managed HA PostgreSQL in one install: the CloudNativePG operator + a r… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
