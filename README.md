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

## Latest list — 2026-09-28 00:21 UTC

New charts added between 2026-09-27 23:21 UTC and 2026-09-28 00:21 UTC.

[Full CSV](data/new-helm-charts-2026-09-28T00-21-25-344518Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-09-27 23:38:41 | [quetzal](https://artifacthub.io/packages/helm/quetzal/quetzal) | quetzal | 0.5.0 | Game servers, run by Kubernetes. A self-hosted panel for Minecraft, Valheim and… |
| 2026-09-27 23:46:10 | [system-upgrade-controller](https://artifacthub.io/packages/helm/this-is-tobi-helm-charts/system-upgrade-controller) | this-is-tobi-helm-charts | 0.1.0 | Secure, plug-and-play Helm chart for the Rancher system-upgrade-controller, wit… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
