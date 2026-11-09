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

## Latest list — 2026-11-09 12:20 UTC

New charts added between 2026-11-09 11:21 UTC and 2026-11-09 12:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-09T12-20-23-001661Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-09 11:47:35 | [attic](https://artifacthub.io/packages/helm/cfi2017/attic) | cfi2017 | 0.1.0 | A self-hosted Nix binary cache backed by Attic. |
| 2026-11-09 12:02:30 | [keda-otel-collector-fleet-scaler](https://artifacthub.io/packages/helm/keda-otel-collector-fleet-scaler/keda-otel-collector-fleet-scaler) | keda-otel-collector-fle… | 0.1.0 | KEDA external scaler for OpenTelemetry collector fleets (TraceID gateway patter… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
