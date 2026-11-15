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

## Latest list — 2026-11-15 21:20 UTC

New charts added between 2026-11-15 20:21 UTC and 2026-11-15 21:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T21-20-45-618622Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 20:30:57 | [generated-secrets-operator](https://artifacthub.io/packages/helm/generated-secrets-operator/generated-secrets-operator) | generated-secrets-opera… | 0.2.0 | Kubernetes operator that generates and rotates Secrets from GeneratedSecret res… |
| 2026-11-15 20:44:25 | [gotosocial](https://artifacthub.io/packages/helm/quench-gotosocial/gotosocial) | quench-gotosocial | 0.0.1 | GoToSocial: a lightweight ActivityPub server for the fediverse with a Mastodon-… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
