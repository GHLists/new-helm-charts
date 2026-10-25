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

## Latest list — 2026-10-25 20:19 UTC

New charts added between 2026-10-25 19:21 UTC and 2026-10-25 20:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-25T20-19-20-195006Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-25 19:58:28 | [localai](https://artifacthub.io/packages/helm/upstreamyard/localai) | upstreamyard | 0.1.0 | LocalAI Helm chart for Kubernetes. Self-hosted OpenAI-compatible API for LLMs,… |
| 2026-10-25 20:03:10 | [napwake](https://artifacthub.io/packages/helm/napwake/napwake) | napwake | 0.2.0-rc.9 | Kubernetes operator that pauses idle workloads and wakes them when used — idle… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
