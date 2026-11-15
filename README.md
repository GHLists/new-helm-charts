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

## Latest list — 2026-11-15 12:20 UTC

New charts added between 2026-11-15 11:20 UTC and 2026-11-15 12:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T12-20-49-62607Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 11:34:01 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |
| 2026-11-15 11:34:48 | [kanidm](https://artifacthub.io/packages/helm/quench-kanidm/kanidm) | quench-kanidm | 0.0.1 | Kanidm: an identity management server with users, groups, OAuth2/OIDC, LDAPS, p… |
| 2026-11-15 12:15:44 | [semaphore](https://artifacthub.io/packages/helm/quench-semaphore/semaphore) | quench-semaphore | 0.0.1 | Semaphore UI: a web UI and API for running Ansible, Terraform/OpenTofu and shel… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
