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

## Latest list — 2026-11-23 10:20 UTC

New charts added between 2026-11-23 09:19 UTC and 2026-11-23 10:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-23T10-20-48-134724Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-23 09:22:53 | [treebind](https://artifacthub.io/packages/helm/treebind/treebind) | treebind | 0.0.1-alpha.3 | Kubernetes operator that keeps a Git repository and an application's files in s… |
| 2026-11-23 09:31:25 | [kubedelos](https://artifacthub.io/packages/helm/kubedelos/kubedelos) | kubedelos | 0.1.0 | Kubernetes image vulnerability scanner with a web UI and scheduled sweeps (kube… |
| 2026-11-23 10:03:57 | [caldera](https://artifacthub.io/packages/helm/quench-caldera/caldera) | quench-caldera | 0.0.1 | MITRE Caldera: adversary emulation for red and purple teams (ATT&CK-mapped abil… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
