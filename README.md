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

## Latest list — 2026-10-11 18:20 UTC

New charts added between 2026-10-11 17:22 UTC and 2026-10-11 18:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-11T18-20-45-219046Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-11 17:24:59 | [paperless-gpt](https://artifacthub.io/packages/helm/taskmedia/paperless-gpt) | taskmedia | 0.3.0 | A Helm chart for paperless-gpt, an LLM-powered OCR and metadata assistant for p… |
| 2026-10-11 18:19:08 | [upgradescope](https://artifacthub.io/packages/helm/upgradescope/upgradescope) | upgradescope | 0.2.0 | Continuous Kubernetes upgrade-readiness scanner — read-only agent publishing a… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
