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

## Latest list — 2026-10-12 13:21 UTC

New charts added between 2026-10-12 12:20 UTC and 2026-10-12 13:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-12T13-21-36-505267Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-12 12:49:23 | [calendarops-api](https://artifacthub.io/packages/helm/calendarops/calendarops-api) | calendarops | 0.1.0 | REST API and browser preview for date-only calendars, business schedules, fisca… |
| 2026-10-12 12:49:23 | [calendarops-jobs](https://artifacthub.io/packages/helm/calendarops/calendarops-jobs) | calendarops | 0.1.0 | Kubernetes CronJobs that generate calendar, federal holiday, fiscal, CSV, JSON,… |
| 2026-10-12 12:49:23 | [calendarops-suite](https://artifacthub.io/packages/helm/calendarops/calendarops-suite) | calendarops | 0.1.0 | Umbrella chart composing the CalendarOps REST API and scheduled export CronJobs. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
