# TKE Core Capabilities Reference

## Product Overview

**Tencent Kubernetes Engine (TKE)** is a fully managed Kubernetes service built on native
Kubernetes. It is fully compatible with Kubernetes APIs and extends them with Tencent Cloud
integrations (CBS storage, CLB load balancing, VPC networking).

**Product root URL**: https://www.tencentcloud.com/document/product/457
**Overview page**: https://www.tencentcloud.com/document/product/457/6759

---

## Global Infrastructure (as of early 2026)

Tencent Cloud operates **64 availability zones across 22 regions globally**:

**International regions where TKE is available:**
- Asia Pacific: Singapore, Tokyo, Seoul, Bangkok, Jakarta, Mumbai (closed 2025 — ⚠️ VERIFY)
- Americas: Silicon Valley (US West), Virginia (US East), São Paulo
- Europe: Frankfurt
- Middle East: Riyadh (Saudi Arabia — announced 2025, ⚠️ VERIFY launch status)
- Malaysia: Cyberjaya (Alto Cloud, launched 2024)

**China regions**: Guangzhou, Shenzhen, Shanghai, Nanjing, Beijing, Chengdu, Chongqing, Qingyuan, Hong Kong

Source: Wikipedia / Tencent Cloud global infrastructure page
https://www.tencentcloud.com/global-infrastructure

---

## Cluster Types

| Type | Description | Docs |
|---|---|---|
| **Standard cluster** | Managed K8s with user-managed nodes (CVM instances) | /457/6759 |
| **TKE Serverless (EKS)** | Fully serverless — no node management required | /457/34040 |
| **TKEStack** | Open-source, self-hosted K8s platform (on-premises) | GitHub: tkestack/tke |
| **TKE Edge** | K8s for edge locations | /457/35085 |

---

## Core Capabilities

### Orchestration & Scheduling
- Native Kubernetes API compatibility
- Support for Deployments, StatefulSets, DaemonSets, Jobs, CronJobs
- Horizontal Pod Autoscaler (HPA) and custom metrics autoscaling
- Cluster Autoscaler for node-level auto-scaling

### Networking
- VPC-native networking (high performance, no overlay overhead in most scenarios)
- Support for Cilium, flannel, and other CNI plugins
- GlobalRouter and VPC-CNI network modes
- Integration with CLB (Cloud Load Balancer) for L4/L7 ingress

### Storage
- Native integration with CBS (Cloud Block Storage) — dynamic provisioning via CSI
- CFS (Cloud File System / NFS) support
- COS (Object Storage) via FUSE/CSI for ML workload data access
- StatefulSet support for databases and stateful workloads

### Cluster Lifecycle Management
- One-click cluster creation via console or IaC
- Terraform provider for TKE: [⚠️ VERIFY URL - search tencentcloud.com terraform]
- In-place and rolling Kubernetes version upgrades
- Node pool management with auto-scaling policies
- [⚠️ VERIFY: SLA uptime for managed control plane — likely 99.95%]

### Observability
- Integration with Tencent Cloud Observability Platform (CLS + CM)
- Native Prometheus/Grafana support via managed addon
- Log collection to CLS via DaemonSet agent
- Alarm policies for cluster health, pod status, resource utilization

### Multi-Tenancy & Isolation
- Namespace-level resource quotas
- Network policies for pod-level traffic control
- Resource isolation between business units within same cluster

---

## Ecosystem Integrations

### CNCF & Open Source
- Kubernetes (core contributor)
- Istio (via TCM — Tencent Cloud Mesh)
- Helm 3.x support (native in TKE console)
- Prometheus operator
- ArgoCD / Flux for GitOps workflows
- Volcano scheduler (batch/AI job scheduling)
- KubeEdge (edge computing framework, Tencent contributed)
- [⚠️ VERIFY: full list of CNCF projects Tencent contributes to — needed for questionnaire]

### DevOps Integration
- CODING DevOps (Tencent's CI/CD platform)
- Jenkins integration
- GitLab CI/CD integration
- GitHub Actions support via self-hosted runners on TKE

### IaC / GitOps
- Terraform provider for Tencent Cloud (includes TKE resources)
- CRD-based cluster management
- Helm Chart repository via TCR (Tencent Container Registry)
- ArgoCD-compatible GitOps workflows

---

## Customer Scale Evidence

TKE powers Tencent's own hyperscale digital services:
- **WeChat** — ~1.3 billion monthly active users; backend microservices run on containers
- **Honor of Kings** — one of the world's highest-concurrency online games; container infrastructure
- **QQ, Tencent Video, Tencent Music** — large-scale streaming and social platforms

These are production deployments demonstrating:
- Clusters operating at extremely large scale (exact node counts: [⚠️ VERIFY internally])
- Auto-scaling under burst traffic (e.g., game launch events, livestreaming peaks)
- High availability across multi-AZ deployments

**External customers**: Gaming companies (Palworld multiplayer servers via Tencent Cloud Lighthouse, 2024), entertainment platforms across Southeast Asia.

---

## Known Gaps / Honest Limitations

- No native container image **build** service (use TCR + CODING CI or third-party)
- Fleet management via TDCC is a separate product (not native to core TKE console)
- MSP/ISV ecosystem in NA/EU is limited compared to AWS/Azure/GCP
- GPU hardware: H100, B200, GB200 not available due to US export controls
