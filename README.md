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

## Latest list — 2026-11-05 13:21 UTC

New charts added between 2026-11-05 12:20 UTC and 2026-11-05 13:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-05T13-21-11-763155Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-05 12:35:16 | [inrun](https://artifacthub.io/packages/helm/inrun/inrun) | inrun | 0.1.0 | Inrun is the intent runner for Kubernetes. Callers send an intent through the g… |
| 2026-11-05 13:02:27 | [kausa](https://artifacthub.io/packages/helm/kausa/kausa) | kausa | 0.6.0 | A tiny Kubernetes controller that explains failing workloads with an LLM |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
