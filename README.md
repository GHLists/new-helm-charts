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

## Latest list — 2026-10-21 13:19 UTC

New charts added between 2026-10-21 12:19 UTC and 2026-10-21 13:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-21T13-19-56-219816Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-21 12:21:02 | [kratix](https://artifacthub.io/packages/helm/syntasso/kratix) | syntasso | 0.0.1 | A Helm chart for installing Kratix (https://kratix.io) |
| 2026-10-21 12:45:34 | [feishin](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/feishin) | kubernetes-homelab-helm… | 0.1.0 | Deploys Feishin music streaming client on Kubernetes |
| 2026-10-21 12:45:34 | [homepage](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/homepage) | kubernetes-homelab-helm… | 0.1.0 | Deploys Homepage dashboard on Kubernetes. |
| 2026-10-21 12:45:34 | [k8s-debug-pod](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/k8s-debug-pod) | kubernetes-homelab-helm… | 0.1.0 | Deploys an Ubuntu-based Kubernetes troubleshooting pod |
| 2026-10-21 12:45:34 | [navidrome](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/navidrome) | kubernetes-homelab-helm… | 0.1.0 | Deploys Navidrome music streaming server on Kubernetes |
| 2026-10-21 12:45:34 | [pocket-id](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/pocket-id) | kubernetes-homelab-helm… | 0.1.0 | Deploys Pocket ID passkey-based OIDC provider on Kubernetes |
| 2026-10-21 12:45:34 | [portfolio-next](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/portfolio-next) | kubernetes-homelab-helm… | 0.1.0 | Static Astro portfolio served by unprivileged NGINX |
| 2026-10-21 12:45:34 | [portfolio-tracker](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/portfolio-tracker) | kubernetes-homelab-helm… | 0.1.0 | Deploys the self-hosted Portfolio Tracker with PostgreSQL |
| 2026-10-21 12:45:34 | [pve-exporter](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/pve-exporter) | kubernetes-homelab-helm… | 0.1.0 | Deploys the prometheus-pve-exporter for scraping Proxmox VE metrics |
| 2026-10-21 12:45:34 | [qbittorrent-exporter](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/qbittorrent-exporter) | kubernetes-homelab-helm… | 0.1.0 | Deploys the martabal qBittorrent Prometheus exporter on Kubernetes |
| 2026-10-21 12:45:34 | [syncthing](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/syncthing) | kubernetes-homelab-helm… | 0.1.0 | Deploys Syncthing continuous file synchronization on Kubernetes |
| 2026-10-21 12:45:34 | [umami](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/umami) | kubernetes-homelab-helm… | 0.1.0 | A Helm chart for Umami, a privacy-focused web analytics platform |
| 2026-10-21 13:01:53 | [dbmanager](https://artifacthub.io/packages/helm/dbmanager/dbmanager) | dbmanager | 0.15.1 | DBManager — unified administration, monitoring, performance, security and backu… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
