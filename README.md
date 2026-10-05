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

## Latest list — 2026-10-05 10:19 UTC

New charts added between 2026-10-05 09:22 UTC and 2026-10-05 10:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-05T10-19-03-677083Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-05 09:34:09 | [convertigo](https://artifacthub.io/packages/helm/convertigo/convertigo) | convertigo | 8.4.5 | The Convertigo Low Code / No Code Platform running on Kubernetes |
| 2026-10-05 09:38:40 | [polaris](https://artifacthub.io/packages/helm/quench-polaris/polaris) | quench-polaris | 0.0.2 | Fairwinds Polaris, the Kubernetes configuration validator: a dashboard that aud… |
| 2026-10-05 09:38:41 | [versitygw](https://artifacthub.io/packages/helm/quench-versitygw/versitygw) | quench-versitygw | 0.0.1 | Versity S3 Gateway, an S3-compatible API server over a POSIX filesystem (or ano… |
| 2026-10-05 09:54:18 | [ansibleforms](https://artifacthub.io/packages/helm/ansibleforms/ansibleforms) | ansibleforms | 6.2.0 | A Helm chart for AnsibleForms, a web front end that turns Ansible playbooks int… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
