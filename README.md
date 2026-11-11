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

## Latest list — 2026-11-11 10:20 UTC

New charts added between 2026-11-11 09:22 UTC and 2026-11-11 10:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-11T10-20-43-253627Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-11 09:32:41 | [opentodo](https://artifacthub.io/packages/helm/opentodo/opentodo) | opentodo | 0.18.0 | Open-source, local-first task manager. Works offline and syncs every device fro… |
| 2026-11-11 09:45:41 | [submilli](https://artifacthub.io/packages/helm/submilli/submilli) | submilli | 0.4.4 | Agent-native execution environment — runs a strict TypeScript subset in a WasmG… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
