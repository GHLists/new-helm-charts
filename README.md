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

## Latest list — 2026-11-27 14:18 UTC

New charts added between 2026-11-27 13:19 UTC and 2026-11-27 14:18 UTC.

[Full CSV](data/new-helm-charts-2026-11-27T14-18-56-788485Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-27 13:40:02 | [lib-datadog](https://artifacthub.io/packages/helm/cookielab/lib-datadog) | cookielab | 0.1.0 | Annotations, Labels and ENVs for DataDog |
| 2026-11-27 13:40:02 | [lib-gitlab](https://artifacthub.io/packages/helm/cookielab/lib-gitlab) | cookielab | 0.1.0 | Annotations for GitLab |
| 2026-11-27 14:02:18 | [ha-enoceanmqtt](https://artifacthub.io/packages/helm/ha-enoceanmqtt/ha-enoceanmqtt) | ha-enoceanmqtt | 1.0.1-dev.459787644… | Helmchart for enoceanmqtt-addon |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
