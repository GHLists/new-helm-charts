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

## Latest list — 2026-11-22 22:20 UTC

New charts added between 2026-11-22 21:18 UTC and 2026-11-22 22:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-22T22-20-28-551397Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-22 21:34:25 | [voimain-relay](https://artifacthub.io/packages/helm/biatec-repo/voimain-relay) | biatec-repo | 5.1.1 | VOI relay node for voimain-1.0 blockchain. |
| 2026-11-22 22:03:26 | [bloodhound](https://artifacthub.io/packages/helm/quench-bloodhound/bloodhound) | quench-bloodhound | 0.0.1 | BloodHound Community Edition: attack-path analysis for Active Directory and Ent… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
