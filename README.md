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

## Latest list — 2026-10-26 10:20 UTC

New charts added between 2026-10-26 09:20 UTC and 2026-10-26 10:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-26T10-20-14-565562Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-26 09:24:50 | [nvd-mirror](https://artifacthub.io/packages/helm/ideaplexus/nvd-mirror) | ideaplexus | 0.1.0 | Mirrors the CVE data of the NIST National Vulnerability Database and serves it… |
| 2026-10-26 09:34:38 | [backup](https://artifacthub.io/packages/helm/k8ssandra/backup) | k8ssandra | 0.26.0 | Creates a CassandraBackup custom resource instance. This chart should be used i… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
