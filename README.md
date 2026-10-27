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

## Latest list — 2026-10-27 09:21 UTC

New charts added between 2026-10-27 08:20 UTC and 2026-10-27 09:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-27T09-21-14-159268Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-27 08:25:25 | [alert-history-writer](https://artifacthub.io/packages/helm/svtech/alert-history-writer) | svtech | 0.2.0 | Alertmanager webhook receiver that stores alert history in MariaDB via a Redis… |
| 2026-10-27 08:25:27 | [network-exporter](https://artifacthub.io/packages/helm/svtech/network-exporter) | svtech | 0.2.0 | Prometheus network_exporter (ICMP/MTR/TCP/HTTP probes) |
| 2026-10-27 08:25:27 | [pnetlab-exporter](https://artifacthub.io/packages/helm/svtech/pnetlab-exporter) | svtech | 0.2.0 | query-exporter for PNETLab lab/node metrics |
| 2026-10-27 08:25:27 | [pve-exporter](https://artifacthub.io/packages/helm/svtech/pve-exporter) | svtech | 0.2.0 | Prometheus exporter for Proxmox VE |
| 2026-10-27 08:25:27 | [redfish-exporter](https://artifacthub.io/packages/helm/svtech/redfish-exporter) | svtech | 0.2.0 | Redfish hardware exporter |
| 2026-10-27 08:25:27 | [vmware-exporter](https://artifacthub.io/packages/helm/svtech/vmware-exporter) | svtech | 0.2.0 | Prometheus exporter for VMware vSphere |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
