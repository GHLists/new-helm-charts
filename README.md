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

## Latest list — 2026-10-09 16:20 UTC

New charts added between 2026-10-09 15:20 UTC and 2026-10-09 16:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-09T16-20-47-203441Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-09 15:34:38 | [kimistore](https://artifacthub.io/packages/helm/loafoe/kimistore) | loafoe | 0.1.0 | Kafka-compatible streaming agent that keeps its durable log in object storage |
| 2026-10-09 15:50:36 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |
| 2026-10-09 16:01:14 | [arith-ruby](https://artifacthub.io/packages/helm/arith-ruby/arith-ruby) | arith-ruby | 1.0.0 | Integer arithmetic over HTTP. Four endpoints, a page, metrics, traces and logs. |
| 2026-10-09 16:01:14 | [arith-rust](https://artifacthub.io/packages/helm/arith-rust/arith-rust) | arith-rust | 1.1.0 | Integer arithmetic over HTTP. Four endpoints, a page, metrics, traces and logs. |
| 2026-10-09 16:01:14 | [arith-ts](https://artifacthub.io/packages/helm/arith-ts/arith-ts) | arith-ts | 1.0.0 | Integer arithmetic over HTTP. Four endpoints, a page, metrics, traces and logs. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
