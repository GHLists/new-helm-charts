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

## Latest list — 2026-10-24 21:19 UTC

New charts added between 2026-10-24 20:19 UTC and 2026-10-24 21:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-24T21-19-56-79329Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-24 20:47:38 | [admiral-infra-agent](https://artifacthub.io/packages/helm/admiral/admiral-infra-agent) | admiral | 0.1.0 | Runs an Admiral agent in Kubernetes that plans and applies Terraform and OpenTo… |
| 2026-10-24 21:16:01 | [mailpit](https://artifacthub.io/packages/helm/spnngl-mailpit/mailpit) | spnngl-mailpit | 0.1.0 | Mailpit, an email and SMTP testing tool with a web UI and an API, as a hardened… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
