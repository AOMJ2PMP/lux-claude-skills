# TKE Serverless Deep Reference

(See also: tke-security.md has the combined serverless overview)

## Serverless Container — Key Differentiators for Gartner

### Why Serverless Matters to Dennis Smith
His Predicts 2025 report explicitly states: "By 2027, more than 50% of all container management
deployments will involve serverless container management services, up from <25% in 2024."

This is a high-weight criterion. If a vendor doesn't have a mature serverless story, they
lose points here.

### TKE Serverless Maturity Signals
- Generally available (not preview) — production workloads running on it
- GPU support in serverless mode (rare — most vendors don't support this yet)
- Scale-to-zero capability
- Tencent's own internal workloads use TKE Serverless for bursty jobs
- [⚠️ VERIFY: how long TKE Serverless has been GA — launch date matters]

### Use Cases to Highlight
1. **Bursty batch jobs** — ML training jobs, data processing, scales to zero between runs
2. **Dev/test environments** — no idle costs, spun up on demand
3. **Event-driven applications** — combined with Tencent Cloud SCF (serverless functions)
4. **GPU inference** — pay per inference request, not per idle GPU-hour

### Pricing Model (from documentation)
TKE Serverless charges based on:
- CPU cores × seconds used
- Memory GB × seconds used
- GPU card-seconds (for GPU workloads)
No node management fees. True pay-per-use.

### Virtual Node
- Standard TKE clusters can add a "virtual node" to burst overflow pods to serverless
- No manifest changes required — same pod spec works
- Enables gradual migration from node-based to serverless
- Documentation: https://www.tencentcloud.com/document/product/457

---

## Fleet Management Supplementary Notes

### How TDCC Compares to Market
| Feature | TDCC | AWS Fleet Manager (lacks native) | GKE Enterprise | AKS Fleet Manager |
|---|---|---|---|---|
| Register external clusters | ✅ | Limited | ✅ | ✅ |
| Cross-cloud management | ✅ | ❌ | ✅ | Limited |
| Edge integration | ✅ (KubeEdge) | Limited | ✅ (GDC) | Limited |
| Free pricing | ✅ | N/A | Paid | Paid |

Note: AWS was actually criticized in the 2025 MQ for lacking native fleet management.
This is an area where TKE/TDCC can genuinely differentiate.

### TDCC Application Distribution Use Case
A gaming company with clusters in Singapore, Tokyo, and Frankfurt:
- TDCC manages all three clusters from one control plane
- Deploy a game patch simultaneously to all regions with one ArgoCD-style release
- Roll back globally in minutes if issues detected
- Policy enforcement (RBAC, network policy) consistent across all clusters

This kind of narrative resonates with Dennis Smith's enterprise fleet management focus.
