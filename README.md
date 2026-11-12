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

## Latest list — 2026-11-12 08:20 UTC

New charts added between 2026-11-12 07:22 UTC and 2026-11-12 08:20 UTC.

[Full CSV](data/new-helm-charts-2026-11-12T08-20-36-067848Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-12 07:44:33 | [nebula](https://artifacthub.io/packages/helm/quench-nebula/nebula) | quench-nebula | 0.0.1 | Nebula lighthouse: discovery and relay for a Nebula overlay network of mutually… |
| 2026-11-12 08:16:02 | [dnscrypt-proxy](https://artifacthub.io/packages/helm/quench-dnscrypt-proxy/dnscrypt-proxy) | quench-dnscrypt-proxy | 0.0.1 | dnscrypt-proxy: a DNS proxy that sends queries to upstream resolvers over DNSCr… |
| 2026-11-12 08:16:02 | [smokescreen](https://artifacthub.io/packages/helm/quench-smokescreen/smokescreen) | quench-smokescreen | 0.0.1 | Smokescreen: Stripe's egress HTTP and CONNECT proxy that refuses internal and p… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
