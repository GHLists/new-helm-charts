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

## Latest list — 2026-10-10 09:19 UTC

New charts added between 2026-10-10 08:22 UTC and 2026-10-10 09:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-10T09-19-33-658445Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-10 08:32:09 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |
| 2026-10-10 08:41:51 | [feishin](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/feishin) | kubernetes-homelab-helm… | 0.1.0 | Deploys Feishin music streaming client on Kubernetes |
| 2026-10-10 08:41:51 | [homepage](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/homepage) | kubernetes-homelab-helm… | 0.1.0 | Deploys Homepage dashboard on Kubernetes. |
| 2026-10-10 08:41:51 | [k8s-debug-pod](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/k8s-debug-pod) | kubernetes-homelab-helm… | 0.1.0 | Deploys an Ubuntu-based Kubernetes troubleshooting pod |
| 2026-10-10 08:41:51 | [navidrome](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/navidrome) | kubernetes-homelab-helm… | 0.1.0 | Deploys Navidrome music streaming server on Kubernetes |
| 2026-10-10 08:41:51 | [owncloud](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/owncloud) | kubernetes-homelab-helm… | 0.1.0 | Deploys ownCloud Server with MariaDB and Redis on Kubernetes |
| 2026-10-10 08:41:51 | [pocket-id](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/pocket-id) | kubernetes-homelab-helm… | 0.1.0 | Deploys Pocket ID passkey-based OIDC provider on Kubernetes |
| 2026-10-10 08:41:51 | [portfolio-next](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/portfolio-next) | kubernetes-homelab-helm… | 0.1.0 | Static Astro portfolio served by unprivileged NGINX |
| 2026-10-10 08:41:51 | [portfolio-tracker](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/portfolio-tracker) | kubernetes-homelab-helm… | 0.1.0 | Deploys the self-hosted Portfolio Tracker with PostgreSQL |
| 2026-10-10 08:41:51 | [pve-exporter](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/pve-exporter) | kubernetes-homelab-helm… | 0.1.0 | Deploys the prometheus-pve-exporter for scraping Proxmox VE metrics |
| 2026-10-10 08:41:51 | [qbittorrent-exporter](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/qbittorrent-exporter) | kubernetes-homelab-helm… | 0.1.0 | Deploys the martabal qBittorrent Prometheus exporter on Kubernetes |
| 2026-10-10 08:41:51 | [syncthing](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/syncthing) | kubernetes-homelab-helm… | 0.1.0 | Deploys Syncthing continuous file synchronization on Kubernetes |
| 2026-10-10 08:41:51 | [umami](https://artifacthub.io/packages/helm/kubernetes-homelab-helm-charts/umami) | kubernetes-homelab-helm… | 0.1.0 | A Helm chart for Umami, a privacy-focused web analytics platform |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
