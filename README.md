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

## Latest list — 2026-10-01 17:18 UTC

New charts added between 2026-10-01 16:19 UTC and 2026-10-01 17:18 UTC.

[Full CSV](data/new-helm-charts-2026-10-01T17-18-56-368503Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-10-01 16:32:06 | [n8n](https://artifacthub.io/packages/helm/n8n-io/n8n) | n8n-io | 1.3.1 | Production-grade Helm chart for n8n, the workflow automation platform. Supports… |
| 2026-10-01 16:47:27 | [stunner-dev](https://artifacthub.io/packages/helm/stunner/stunner-dev) | stunner | 1.2.1 | STUNner Kubernetes Gateway Operator |
| 2026-10-01 16:52:27 | [bulwark-mail](https://artifacthub.io/packages/helm/l4g/bulwark-mail) | l4g | 0.2.2 | Helm chart for Bulwark Mail — a self-hosted JMAP webmail with native Ingress an… |
| 2026-10-01 16:52:27 | [freescout](https://artifacthub.io/packages/helm/l4g/freescout) | l4g | 0.1.0 | A Helm chart for Kubernetes |
| 2026-10-01 16:52:27 | [inbox-zero](https://artifacthub.io/packages/helm/l4g/inbox-zero) | l4g | 0.1.0 | Helm chart for Inbox Zero — an open-source AI email assistant (web, BullMQ work… |
| 2026-10-01 16:52:27 | [stalwart-mail-ha](https://artifacthub.io/packages/helm/l4g/stalwart-mail-ha) | l4g | 0.1.2 | Helm chart for Stalwart Mail Server (SMTP, IMAP, JMAP, CalDAV/CardDAV) running… |
| 2026-10-01 17:01:18 | [azerothcore](https://artifacthub.io/packages/helm/azerothcore/azerothcore) | azerothcore | 0.1.0 | AzerothCore World of Warcraft server for Wrath of the Lich King (3.3.5a): auths… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
