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

## Latest list — 2026-10-22 14:19 UTC

New charts added between 2026-10-22 13:20 UTC and 2026-10-22 14:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-22T14-19-47-972955Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-22 13:33:05 | [gravitee-apim](https://artifacthub.io/packages/helm/quench-gravitee-apim/gravitee-apim) | quench-gravitee-apim | 0.0.4 | Hardened Gravitee API Management (APIM) community edition on 0-CVE nonroot imag… |
| 2026-10-22 13:33:20 | [runtime-security-stack](https://artifacthub.io/packages/helm/quench-runtime-security-stack/runtime-security-stack) | quench-runtime-security… | 0.0.4 | Hardened runtime security in one install: Falco (syscall rules with the modern… |
| 2026-10-22 13:51:00 | [kamaji-crds](https://artifacthub.io/packages/helm/clastix/kamaji-crds) | clastix | 0.0.0+latest | Kamaji is the Hosted Control Plane Manager for Kubernetes. |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
