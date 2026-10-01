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

## Latest list — 2026-10-01 16:19 UTC

New charts added between 2026-10-01 15:21 UTC and 2026-10-01 16:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-01T16-19-16-782175Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-01 15:33:07 | [bind](https://artifacthub.io/packages/helm/quench-bind/bind) | quench-bind | 0.0.1 | ISC BIND 9 (named): an authoritative or caching recursive DNS server, configure… |
| 2026-10-01 15:33:24 | [kube-vip](https://artifacthub.io/packages/helm/quench-kube-vip/kube-vip) | quench-kube-vip | 0.0.1 | kube-vip: virtual IPs and load balancing for Services of type LoadBalancer and… |
| 2026-10-01 15:55:18 | [stunner-dev](https://artifacthub.io/packages/helm/stunner/stunner-dev) | stunner | 1.2.1 | STUNner Kubernetes Gateway Operator |
| 2026-10-01 16:02:34 | [kratix](https://artifacthub.io/packages/helm/syntasso/kratix) | syntasso | 0.0.1 | A Helm chart for installing Kratix (https://kratix.io) |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
