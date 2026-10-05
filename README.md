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

## Latest list — 2026-10-05 23:20 UTC

New charts added between 2026-10-05 22:21 UTC and 2026-10-05 23:20 UTC.

[Full CSV](data/new-helm-charts-2026-10-05T23-20-27-992564Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-05 23:16:00 | [cert-manager-crds](https://artifacthub.io/packages/helm/spnngl-cert-manager-crds/cert-manager-crds) | spnngl-cert-manager-crds | 1.21.2 | CustomResourceDefinitions for cert-manager (certificates, issuers, ACME orders… |
| 2026-10-05 23:16:00 | [traefik-crds](https://artifacthub.io/packages/helm/spnngl-traefik-crds/traefik-crds) | spnngl-traefik-crds | 3.7.13 | CustomResourceDefinitions for Traefik Proxy (IngressRoutes, Middlewares, TLS op… |
| 2026-10-05 23:16:00 | [vertical-pod-autoscaler-crds](https://artifacthub.io/packages/helm/spnngl-vertical-pod-autoscaler-crds/vertical-pod-autoscaler-crds) | spnngl-vertical-pod-aut… | 1.8.0 | CustomResourceDefinitions for the Kubernetes Vertical Pod Autoscaler (VerticalP… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
