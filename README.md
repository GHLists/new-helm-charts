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

## Latest list — 2026-11-15 03:21 UTC

New charts added between 2026-11-15 02:21 UTC and 2026-11-15 03:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-15T03-21-51-737527Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-15 02:21:34 | [dozzle](https://artifacthub.io/packages/helm/quench-dozzle/dozzle) | quench-dozzle | 0.0.1 | Dozzle: a real-time log viewer for Kubernetes pods (reads logs through the API)… |
| 2026-11-15 02:21:35 | [tinyauth](https://artifacthub.io/packages/helm/quench-tinyauth/tinyauth) | quench-tinyauth | 0.0.1 | Tinyauth: a lightweight login portal and forward-auth server for nginx, Traefik… |
| 2026-11-15 02:44:27 | [healthchecks](https://artifacthub.io/packages/helm/quench-healthchecks/healthchecks) | quench-healthchecks | 0.0.2 | Healthchecks: cron job and heartbeat monitoring. Jobs ping a URL and missed pin… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
