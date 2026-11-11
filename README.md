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

## Latest list — 2026-11-11 12:19 UTC

New charts added between 2026-11-11 11:21 UTC and 2026-11-11 12:19 UTC.

[Full CSV](data/new-helm-charts-2026-11-11T12-19-01-02594Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-11 11:44:32 | [trafficserver](https://artifacthub.io/packages/helm/quench-trafficserver/trafficserver) | quench-trafficserver | 0.0.2 | Apache Traffic Server, a caching HTTP/1.1, HTTP/2 and TLS reverse proxy. Remap… |
| 2026-11-11 12:03:00 | [myriarch](https://artifacthub.io/packages/helm/myriarch/myriarch) | myriarch | 0.2.0 | Myriarch server (myriarchd): OpAMP fleet manager for OpenTelemetry Collectors (… |
| 2026-11-11 12:03:00 | [myriarch-collector](https://artifacthub.io/packages/helm/myriarch-collector/myriarch-collector) | myriarch-collector | 0.2.0 | OpenTelemetry Collector with the OpAMP Supervisor from the unchanged upstream i… |
| 2026-11-11 12:03:47 | [kroxylicious](https://artifacthub.io/packages/helm/quench-kroxylicious/kroxylicious) | quench-kroxylicious | 0.0.1 | Kroxylicious, a Kafka protocol proxy that sits between Kafka clients and broker… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
