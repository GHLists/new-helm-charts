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

## Latest list — 2026-10-05 16:22 UTC

New charts added between 2026-10-05 15:20 UTC and 2026-10-05 16:22 UTC.

[Full CSV](data/new-helm-charts-2026-10-05T16-22-08-394531Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-05 15:33:30 | [step-issuer](https://artifacthub.io/packages/helm/quench-step-issuer/step-issuer) | quench-step-issuer | 0.0.2 | step-issuer, smallstep's cert-manager external issuer: StepIssuer and StepClust… |
| 2026-10-05 15:33:31 | [pki-stack](https://artifacthub.io/packages/helm/quench-pki-stack/pki-stack) | quench-pki-stack | 0.0.1 | Hardened internal PKI in one install: step-ca (your own certificate authority)… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
