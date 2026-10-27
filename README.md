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

## Latest list — 2026-10-27 15:21 UTC

New charts added between 2026-10-27 14:20 UTC and 2026-10-27 15:21 UTC.

[Full CSV](data/new-helm-charts-2026-10-27T15-21-58-785375Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-27 14:24:21 | [backend](https://artifacthub.io/packages/helm/cookielab/backend) | cookielab | 0.1.0 | A Helm chart for Kubernetes |
| 2026-10-27 14:24:21 | [complex](https://artifacthub.io/packages/helm/cookielab/complex) | cookielab | 0.10.0 | For deploying applications with consumers and cronjobs |
| 2026-10-27 14:24:21 | [frontend](https://artifacthub.io/packages/helm/cookielab/frontend) | cookielab | 0.1.0 | A Helm chart for Kubernetes |
| 2026-10-27 14:24:21 | [jiva-talos](https://artifacthub.io/packages/helm/cookielab/jiva-talos) | cookielab | 3.6.0 | Fixed Jiva for TALOS Linux. Helm chart for OpenEBS Jiva Operator. Jiva provides… |
| 2026-10-27 14:24:21 | [lib-datadog](https://artifacthub.io/packages/helm/cookielab/lib-datadog) | cookielab | 0.1.0 | Annotations, Labels and ENVs for DataDog |
| 2026-10-27 14:24:21 | [lib-gitlab](https://artifacthub.io/packages/helm/cookielab/lib-gitlab) | cookielab | 0.1.0 | Annotations for GitLab |
| 2026-10-27 14:24:21 | [lib-kubernetes](https://artifacthub.io/packages/helm/cookielab/lib-kubernetes) | cookielab | 0.1.0 | Annotations and Labels for Kubernetes |
| 2026-10-27 14:24:21 | [lib-prometheus](https://artifacthub.io/packages/helm/cookielab/lib-prometheus) | cookielab | 0.1.0 | Prometheus library object components |
| 2026-10-27 14:24:21 | [localpv-provisioner](https://artifacthub.io/packages/helm/cookielab/localpv-provisioner) | cookielab | 3.5.0 | Helm chart for OpenEBS Dynamic Local PV. For instructions to install OpenEBS Dy… |
| 2026-10-27 14:24:21 | [nfs-subdir-external-provisioner](https://artifacthub.io/packages/helm/cookielab/nfs-subdir-external-provisioner) | cookielab | 4.0.18 | nfs-subdir-external-provisioner is an automatic provisioner that used your *alr… |
| 2026-10-27 14:24:21 | [prometheus-rules](https://artifacthub.io/packages/helm/cookielab/prometheus-rules) | cookielab | 0.0.1 | For deploying separated Prometheus Rules for global definitions |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
