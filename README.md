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

## Latest list — 2026-11-15 19:19 UTC

New charts added between 2026-11-15 18:19 UTC and 2026-11-15 19:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T19-19-18-018321Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 18:21:39 | [cyberchef](https://artifacthub.io/packages/helm/quench-cyberchef/cyberchef) | quench-cyberchef | 0.0.1 | CyberChef: GCHQ's web app for encoding, decoding, encryption, compression and d… |
| 2026-11-15 19:03:36 | [atuin-server](https://artifacthub.io/packages/helm/quench-atuin-server/atuin-server) | quench-atuin-server | 0.0.1 | Atuin server: the self-hosted sync server for Atuin shell history, end-to-end e… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
