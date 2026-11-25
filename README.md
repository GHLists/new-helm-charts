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

## Latest list — 2026-11-25 06:21 UTC

New charts added between 2026-11-25 05:22 UTC and 2026-11-25 06:21 UTC.

[Full CSV](data/new-helm-charts-2026-11-25T06-21-31-125153Z.csv)

| Created (UTC) | Chart | Repository | Version | Description |
| :------------ | :---- | :--------- | :------ | :---------- |
| 2026-11-25 05:27:18 | [tinyproxy](https://artifacthub.io/packages/helm/quench-tinyproxy/tinyproxy) | quench-tinyproxy | 0.0.1 | Tinyproxy: a small HTTP and HTTPS (CONNECT) forward proxy with ACLs, filtering… |
| 2026-11-25 05:38:29 | [crowdsec](https://artifacthub.io/packages/helm/quench-crowdsec/crowdsec) | quench-crowdsec | 0.0.1 | CrowdSec: log-based attack detection with community scenarios; the Local API se… |
| 2026-11-25 05:56:24 | [haproxy-kubernetes-ingress](https://artifacthub.io/packages/helm/quench-haproxy-kubernetes-ingress/haproxy-kubernetes-ingress) | quench-haproxy-kubernet… | 0.0.1 | HAProxy Kubernetes Ingress Controller: Ingress through HAProxy with rate limiti… |
| 2026-11-25 06:21:24 | [coraza-spoa](https://artifacthub.io/packages/helm/quench-coraza-spoa/coraza-spoa) | quench-coraza-spoa | 0.0.1 | Coraza SPOA: the OWASP Coraza web application firewall as an HAProxy SPOE agent… |

## Data source

Data comes from the [ArtifactHub API](https://artifacthub.io/docs/api/).
ArtifactHub is a CNCF project; chart metadata is provided by the chart
repositories and their authors. This project is not affiliated with or
endorsed by the CNCF or ArtifactHub.
