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

## Latest list — 2026-10-09 15:20 UTC

New charts added between 2026-10-09 14:20 UTC and 2026-10-09 15:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-09T15-20-13-374704Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-09 14:33:47 | [cs-firewall-bouncer](https://artifacthub.io/packages/helm/spnngl-cs-firewall-bouncer/cs-firewall-bouncer) | spnngl-cs-firewall-boun… | 0.1.0 | CrowdSec firewall bouncer (nftables mode) running as a hardened DaemonSet that… |
| 2026-10-09 14:45:44 | [domain-locker](https://artifacthub.io/packages/helm/domain-locker/domain-locker) | domain-locker | 0.3.3 | A Helm chart for deploying Domain Locker |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
