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

## Latest list — 2026-10-24 14:19 UTC

New charts added between 2026-10-24 13:19 UTC and 2026-10-24 14:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-24T14-19-12-990249Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-24 14:01:40 | [ci-accelerator](https://artifacthub.io/packages/helm/ci-accelerator/ci-accelerator) | ci-accelerator | 0.1.0-rc.2 | A self-hosted fast CI runner for GitLab: persistent BuildKit daemons with a sha… |
| 2026-10-24 14:01:40 | [buildkit](https://artifacthub.io/packages/helm/ci-accelerator-buildkit/buildkit) | ci-accelerator-buildkit | 0.1.0-rc.1 | Persistent BuildKit daemons as a shared build service for CI, with probe and ga… |
| 2026-10-24 14:01:40 | [console](https://artifacthub.io/packages/helm/ci-accelerator-console/console) | ci-accelerator-console | 0.2.0-rc.1 | Collects the build history of BuildKit daemons and the CI jobs around it, and e… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
