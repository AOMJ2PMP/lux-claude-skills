# TKE Serverless Reference

## TKE Serverless (EKS — Elastic Kubernetes Service)

**What it is**: Fully serverless container service. Users deploy workloads without managing
or configuring underlying nodes. No node provisioning, patching, or scaling required.

**How it works**:
- Pods are scheduled directly onto Tencent Cloud's elastic infrastructure
- Users define pod resource requirements; underlying compute is automatically provisioned
- Billing: per pod resource usage (CPU + memory × time) — no idle VM costs
- Fully Kubernetes API compatible — same manifests work on TKE standard and Serverless

**Key capabilities**:
- Support for GPU workloads (T4, A10) in Serverless mode — pods can request GPU resources
- Deep learning / ML inference in serverless mode: no cluster setup required
- EKS auto-scales to zero — cost goes to zero when no workloads run
- Supports all Kubernetes native workload types: Deployment, StatefulSet, Job, CronJob
- Storage: CBS (block), CFS (NFS), and COS (object) all mountable in serverless pods

**Why this matters for Gartner**:
Dennis Smith's Predicts 2025 says >50% of container deployments will use serverless by 2027.
TKE Serverless is a fully production-ready offering, not a preview.

**Documentation**: https://www.tencentcloud.com/document/product/457/34040

## Virtual Node (Hybrid Serverless)
- Add serverless capacity to standard TKE clusters via Virtual Node
- Burst overflow workloads to serverless without cluster resize
- Same cluster, same kubectl — transparent to developers

---

# TKE Fleet Management & Multi-Cluster Reference

## TDCC — Tencent Distributed Cloud Center

**What it is**: Multi-cluster and hybrid cloud management plane for Kubernetes.
Manages clusters across: Tencent Cloud regions, on-premises (via TKEStack), edge, and
other cloud providers' Kubernetes clusters (registered external clusters).

**Key capabilities**:

### Fleet Management
- Centralized management of multiple Kubernetes clusters from single control plane
- Lifecycle management: create, upgrade, scale, delete clusters across environments
- Unified policy distribution: push configs, RBAC policies, addons across fleet
- Cross-cluster workload scheduling and federation

### Multi-Cloud & Hybrid
- Register **external Kubernetes clusters** (including clusters from other cloud providers)
  — not limited to Tencent Cloud infrastructure
- On-premises cluster management via TKEStack integration
- Consistent management interface regardless of where clusters run

### Application Distribution
- Multi-cluster application release management
- Canary/gray deployments across multiple clusters
- Decouples application release logic from underlying cluster configuration
- Accelerates rollout and rollback across fleet

### Edge Support
- Native edge computing integration via KubeEdge
- Manages edge nodes as part of the same fleet
- Low-bandwidth, intermittent connectivity support for edge locations

**Pricing**: TDCC itself is currently free; charges apply for underlying cloud resources.

**Documentation**: https://www.tencentcloud.com/document/product/1144

## TKE Edge

- Lightweight Kubernetes for edge/far-edge deployments
- Supports resource-constrained hardware
- Integrated with TDCC for fleet-level management
- Use cases: retail edge, industrial IoT, telco edge

**Documentation**: https://www.tencentcloud.com/document/product/457/35085

## TKEStack (On-Premises)

- Open-source, self-managed Kubernetes platform
- Deployable on bare metal or private cloud infrastructure
- Managed via TDCC for hybrid fleet scenarios
- GitHub: https://github.com/tkestack/tke

---

# TKE Security Reference

## Identity & Access Management

### CAM (Cloud Access Management)
- Kubernetes RBAC integration with Tencent Cloud CAM
- Fine-grained access control: namespace-level, resource-level permissions
- Sub-account and role-based access for enterprise multi-team environments

### Pod Identity via OIDC
- TKE supports Kubernetes ServiceAccount OIDC token projection
- Pods can assume CAM roles without embedding static credentials
- Principle of least privilege for pod-level cloud resource access
- Similar to AWS IAM Roles for Service Accounts (IRSA) pattern

## Network Security

### TCM — Tencent Cloud Mesh (Service Mesh)
- Istio-based service mesh, fully managed by Tencent Cloud
- mTLS between services — zero-trust internal network
- Traffic management, fault injection, circuit breaking
- Observability: distributed tracing, service topology
- Documentation: https://www.tencentcloud.com/document/product/1013

### Network Policy
- Kubernetes NetworkPolicy support for pod-level traffic control
- VPC-level security groups for node-level isolation
- Integration with Tencent Cloud firewall for perimeter security

## Container Image Security

### TCR — Tencent Container Registry
- Private, enterprise-grade container image registry
- Image vulnerability scanning (integrated scanner)
- Image signing and verification support
- Geo-replication across Tencent Cloud regions
- Documentation: https://www.tencentcloud.com/document/product/1051

### Supply Chain Security
- Image scanning before deployment via TCR admission webhook
- Support for OPA/Gatekeeper policies for admission control
- [⚠️ VERIFY: specific CVE scanning tools integrated — Trivy, Clair, or proprietary]

## Runtime Security
- [⚠️ VERIFY: what runtime security tooling TKE provides natively]
- Seccomp and AppArmor profile support
- Pod Security Standards enforcement

## Compliance & Audit
- Operation audit logs via CloudAudit
- API server audit logging enabled by default in managed clusters
- Compliance certifications: [⚠️ VERIFY — ISO 27001, SOC 2, CSA STAR, etc.]
