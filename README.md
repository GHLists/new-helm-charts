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

## Latest list — 2026-11-04 10:18 UTC

New charts added between 2026-11-04 09:19 UTC and 2026-11-04 10:18 UTC.

[Full CSV](data/new-helm-charts-2026-11-04T10-18-58-802404Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-04 09:31:30 | [k8s-borg](https://artifacthub.io/packages/helm/k8s-borg/k8s-borg) | k8s-borg | 1.0.7-0 | Backup for Kubernetes clusters with BorgBackup. Deploys a node-backup DaemonSet… |
| 2026-11-04 10:01:39 | [cluster-api-janitor-openstack](https://artifacthub.io/packages/helm/cluster-api-janitor-openstack/cluster-api-janitor-openstack) | cluster-api-janitor-ope… | 0.1.0-rc.1 | Helm chart for deploying the Cluster API Janitor for OpenStack |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
