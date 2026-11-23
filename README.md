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

## Latest list — 2026-11-23 06:20 UTC

New charts added between 2026-11-23 05:19 UTC and 2026-11-23 06:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-23T06-20-04-417635Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-23 05:39:11 | [model2vec-serve](https://artifacthub.io/packages/helm/it-at-m/model2vec-serve) | it-at-m | 0.7.2 | Lightweight OpenAI/TEI compatible model2vec embeddings server |
| 2026-11-23 05:50:20 | [commafeed](https://artifacthub.io/packages/helm/quench-commafeed/commafeed) | quench-commafeed | 0.0.1 | CommaFeed: a self-hosted RSS reader inspired by Google Reader, with the bundled… |
| 2026-11-23 06:15:26 | [kestra](https://artifacthub.io/packages/helm/quench-kestra/kestra) | quench-kestra | 0.0.1 | Kestra: a declarative event-driven orchestration platform (YAML flows, plugins,… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
