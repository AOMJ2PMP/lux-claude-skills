# TKE Fleet Management Reference

(Main content is in tke-security.md under TDCC section — this file has supplementary material)

## CNCF Contributions (Important for Innovation Score)

Tencent Cloud / TKE team's CNCF contributions:
- **Kubernetes** — core contributor
- **Volcano** — Tencent donated to CNCF; used for AI/ML batch scheduling
- **KubeEdge** — Tencent donated to CNCF; edge computing framework
- **Karmada** — multi-cluster resource management (check if Tencent contributed)
- **Nano GPU** — open-sourced by Tencent (basis for qGPU)
- [⚠️ VERIFY: total count of CNCF projects Tencent contributes to — Huawei claims 82;
  find the comparable number for Tencent]

Note from 2025 MQ: Huawei got credit for "contributing to 82 CNCF projects."
TKE needs to have a comparable or stronger CNCF narrative.

## Platform Engineering Support

Dennis Smith explicitly values Platform Engineering / IDP capability. Key TKE features:

### Self-Service Developer Platform
- TKE console provides self-service cluster creation and workload deployment
- Namespace-level isolation allows developer teams to manage their own environments
- Helm chart catalog in TCR for platform teams to publish vetted application templates
- RBAC configuration allows platform teams to grant scoped permissions to dev teams

### CI/CD Integration
- CODING DevOps: Tencent's native DevOps platform — pipeline from code to container
  - Connects to TKE for deployment stages
  - Supports blue/green, canary deployments
- External CI: Jenkins, GitLab CI, GitHub Actions all work with TKE via kubectl/helm
- Container Registry automation: push to TCR → trigger deployment to TKE

### GitOps
- ArgoCD: fully compatible; many customers use ArgoCD with TKE
- Flux: compatible with standard TKE clusters
- TDCC provides native GitOps-style application distribution across fleets

### Internal Developer Portal (IDP) Patterns
- [⚠️ VERIFY: does Tencent Cloud have any Backstage integration or native IDP offering?]
- Namespace-per-team model with quota management is the standard pattern

## Geographic Strategy for Fleet Management

TDCC's multi-cluster capability maps to real-world enterprise needs:
- **Chinese multinationals expanding globally**: manage CN + international clusters from one pane
- **Game companies**: separate clusters per region for latency, but unified operations
- **Financial services**: compliance isolation across regions, unified policy enforcement

This is the story to tell for Gartner's Geographic Strategy criterion.
