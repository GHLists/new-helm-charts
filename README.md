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

## Latest list — 2026-10-18 03:21 UTC

New charts added between 2026-10-18 02:21 UTC and 2026-10-18 03:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-18T03-21-18-23057Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-18 02:39:48 | [sonarqube-exporter](https://artifacthub.io/packages/helm/ideaplexus/sonarqube-exporter) | ideaplexus | 0.1.0 | Exports the measures of every SonarQube project as Prometheus gauges, with the… |
| 2026-10-18 03:02:58 | [omniroute-operator](https://artifacthub.io/packages/helm/omniroute-operator/omniroute-operator) | omniroute-operator | 0.1.0 | Kubernetes operator for managing OmniRoute AI gateway instances |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
