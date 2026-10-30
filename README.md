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

## Latest list — 2026-10-30 14:19 UTC

New charts added between 2026-10-30 13:20 UTC and 2026-10-30 14:19 UTC.

[Full CSV](data/new-helm-charts-2026-10-30T14-19-44-433159Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-30 13:30:42 | [cert-manager-webhook-domainchief](https://artifacthub.io/packages/helm/cert-manager-webhook-domainchief/cert-manager-webhook-domainchief) | cert-manager-webhook-do… | 0.1.2 | cert-manager ACME DNS01 webhook solver for Domain Chief |
| 2026-10-30 13:33:16 | [dsc-consent-manager](https://artifacthub.io/packages/helm/fiware/dsc-consent-manager) | fiware | 0.1.0 | A Helm chart for running the dsc-consent-manager, consent lifecycle management… |
| 2026-10-30 13:54:08 | [excalidraw](https://artifacthub.io/packages/helm/maarlo/excalidraw) | maarlo | 0.1.0 | Virtual collaborative whiteboard with a hand-drawn feel |
| 2026-10-30 14:02:47 | [excalidraw](https://artifacthub.io/packages/helm/maarlo-excalidraw/excalidraw) | maarlo-excalidraw | 0.1.0 | Virtual collaborative whiteboard with a hand-drawn feel |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
