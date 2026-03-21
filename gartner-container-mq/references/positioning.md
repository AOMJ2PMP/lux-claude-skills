# TKE MQ Positioning Reference

## 2025 Gartner MQ Result

- **Quadrant**: Challenger
- **Position**: Upper-left cluster (Challenger quadrant, mid-range on both axes)
- **Peer group in same cluster**: Nutanix, Mirantis, Broadcom (VMware), Oracle, Canonical, Spectro Cloud
- **Above us in Challenger**: Tencent Cloud is mid-pack; Huawei is closer to Leaders boundary
- **Target for 2026**: Maintain Challenger, increase both Ability to Execute score and Completeness of Vision

---

## 2025 Gartner Strengths (what's working — reinforce these)

1. **Entertainment and consumer industries** — Tencent's gaming/streaming/social ecosystem provides
   hyperscale use cases and credibility. Always reference scale metrics when available.

2. **Proven scalability for large-scale digital services** — Tencent's own products (WeChat, QQ,
   Honor of Kings, etc.) are the best reference customers. Use them as evidence of production
   scale even if named customers are limited.

3. **Integration with application platforms across digital ecosystems** — The tight integration
   between TKE and Tencent's game/social/e-commerce stacks is a genuine differentiator.
   Frame this as "platform engineering at hyperscale."

---

## 2025 Gartner Cautions (what to address head-on)

### Caution A: "Limited momentum outside China and Southeast Asia"
**Root cause**: Gartner clients are mostly NA/EU enterprises; Tencent Cloud has limited
reference customers in those regions.
**Answer strategy**:
- Cite specific international regions: US East/West, Frankfurt, Tokyo, Singapore, São Paulo,
  Mumbai, Bangkok
- Name any non-Chinese customer verticals (gaming companies with global operations,
  Chinese multinationals expanding overseas)
- Emphasize 24/7 international support and English-language documentation
- Don't overclaim — "growing international presence" is more credible than "global leader"

### Caution B: "Partner ecosystems for enterprise in global market is limited"
**Root cause**: TKE lacks the ISV/MSP ecosystem depth of AWS, Azure, Google in Western markets.
**Answer strategy**:
- Lead with CNCF: Tencent Cloud contributes to CNCF projects (list specific ones: Kubernetes,
  Istio, Helm, etc.)
- Mention Tencent Cloud Marketplace for packaged solutions
- Highlight technology integrations as ecosystem proxies: Terraform provider, ArgoCD support,
  Prometheus/Grafana native integration, Datadog agent support
- Acknowledge the gap honestly: "While our MSP ecosystem in Western markets is still developing,
  we have deep partnerships with [list any global SIs]"

### Caution C: "Feature sets for containerizing existing applications not as comprehensive"
**Root cause**: Application modernization tooling (migration assessment, refactoring, lift-and-shift
automation) is less developed than hyperscalers.
**Answer strategy**:
- Highlight TKE's application migration tooling and integration with Tencent Cloud Migration Hub
- Emphasize CODING DevOps as an end-to-end CI/CD platform for containerization workflows
- Show VM-to-container migration path support
- Reference any application catalog or service catalog capabilities

### Caution D: "Unavailability of latest GPU models (H100/B200/GB200)"
**Root cause**: US government export controls — this is geopolitical, not a product decision.
**Answer strategy** (NEVER claim these GPUs are available):
- Acknowledge: "Due to US export control regulations, certain Nvidia GPU models are not
  available in Tencent Cloud regions."
- Pivot immediately to software compensation:
  - qGPU (GPU sharing and memory isolation)
  - TACO-LLM (inference optimization framework)
  - Volcano scheduler (GPU-aware scheduling)
  - Available GPU models: T4, A10, V100 (verify current availability)
  - Support for domestic AI accelerators where applicable
- Frame as: "We are investing heavily in software-layer optimizations to maximize efficiency
  of available GPU hardware."

---

## Dennis Smith — Known Scoring Priorities

Based on 2025 MQ report analysis and his Predicts 2025 research:

| His priority | What to do |
|---|---|
| AI workload support | Lead every AI answer with specific capabilities + metrics |
| Serverless maturity | Proactively mention TKE Serverless in relevant answers |
| Platform engineering / developer UX | Show IDP, self-service, abstraction layers |
| Fleet management at scale | TDCC, multi-cluster policy, lifecycle management |
| CNCF community participation | Cite specific projects, contribution counts |
| Customer evidence at scale | Numbers > claims; Tencent's own ecosystem is valid evidence |
| International enterprise credibility | Geography + customer type evidence in every applicable answer |

---

## Key Product Names (use exact names)

| Product | Full name | Use for |
|---|---|---|
| TKE | Tencent Kubernetes Engine | Core managed K8s service |
| TKE Serverless | TKE Serverless (EKS) | Serverless containers |
| TDCC | Tencent Distributed Cloud Center | Fleet / multi-cluster / hybrid |
| TKE Edge | TKE Edge | Edge Kubernetes |
| TKEStack | TKEStack | Open-source on-premise version |
| TCR | Tencent Container Registry | Image registry |
| TCM | Tencent Cloud Mesh | Service mesh (Istio-based) |
| qGPU | qGPU | GPU sharing technology |
| TACO-LLM | TACO-LLM | LLM inference acceleration |
| TI-One | TI-One (Tencent Intelligent Titanium) | AI training platform |
| CODING DevOps | CODING DevOps | CI/CD, DevOps platform |
| CAM | Cloud Access Management | IAM / RBAC |
| CLS | Cloud Log Service | Logging |
| CM | Cloud Monitor | Monitoring/observability |

---

## Documentation URL Patterns

- **TKE product root (EN)**: https://www.tencentcloud.com/document/product/457
- **TKE overview (EN)**: https://www.tencentcloud.com/document/product/457/6759
- **TKE Serverless**: https://www.tencentcloud.com/document/product/457/34040
- **TDCC**: https://www.tencentcloud.com/document/product/1144
- **TKE Edge**: https://www.tencentcloud.com/document/product/457/35085
- **TCM (service mesh)**: https://www.tencentcloud.com/document/product/1013
- **TCR**: https://www.tencentcloud.com/document/product/1051
- **TI-One**: https://www.tencentcloud.com/document/product/851
- **qGPU**: https://www.tencentcloud.com/document/product/457/49636

⚠️ Always verify URLs before submitting the final questionnaire. These are reference patterns
and may have changed. When in doubt, navigate from the product root.

---

## What NOT to Say

- ❌ Do not claim H100, B200, or GB200 GPU availability
- ❌ Do not claim "global market leader" or "industry-leading" without quantification
- ❌ Do not use vague terms like "robust", "comprehensive" without supporting evidence
- ❌ Do not ignore the international question — always add international availability
- ❌ Do not fabricate customer names or metrics — flag as [⚠️ VERIFY] if uncertain
- ❌ Do not use Chinese-language product names in English answers
