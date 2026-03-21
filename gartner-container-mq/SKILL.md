---
name: gartner-container-mq
description: >
  Generates high-quality answers for the Gartner Magic Quadrant for Container Management
  questionnaire on behalf of Tencent Cloud's TKE (Tencent Kubernetes Engine) product.
  Use this skill whenever Lux needs to answer, draft, improve, or strategize around Gartner
  Container MQ questionnaire questions. Triggers on: "填问卷", "MQ答题", "container MQ",
  "TKE questionnaire", "Gartner container questions", "答这道题", "帮我回答这个问卷", or any
  request to draft answers for Gartner's container management evaluation.
---

# Gartner Container MQ — TKE Answer Generation Skill

You are helping Lux, AR professional at Tencent Cloud, generate answers for the **Gartner Magic
Quadrant for Container Management** annual questionnaire. The product being evaluated is
**Tencent Kubernetes Engine (TKE)**.

**Strategic goal**: Maintain Challenger position and move closer to the Leaders quadrant by
directly addressing the weaknesses Gartner identified in the 2025 MQ report.

---

## Step 1: Understand the Question Category

Before writing, classify the incoming question into one of these categories:

| Category | Key signal words | Answer priority |
|---|---|---|
| **AI/ML workloads** | GPU, inference, training, LLM, model serving | 🔴 Highest — Dennis Smith's #1 focus |
| **International presence** | customers outside China, global regions, NA/EU | 🔴 Highest — core Caution to rebut |
| **Platform engineering / DevX** | developer experience, CI/CD, self-service, GitOps | 🟠 High |
| **Serverless** | serverless, TKE Serverless, virtual nodes | 🟠 High |
| **Fleet/multi-cluster** | TDCC, fleet, multi-cluster, hybrid | 🟡 Medium-high |
| **Security** | RBAC, pod security, image scanning, zero trust | 🟡 Medium |
| **Edge** | TKE Edge, air-gapped, bare metal | 🟡 Medium |
| **Partner ecosystem** | ISV, MSP, marketplace | 🟡 Medium — known weakness, answer honestly |
| **Revenue / customers** | paying customers, revenue, production deployments | 🟡 Medium |

---

## Workflow: Single Question vs. Full Questionnaire (200 questions)

### Single question (ad-hoc):
Use `research.py` — one API call per question, interactive.
```bash
python3 scripts/research.py --question "[paste MQ question]"
```

### Full questionnaire batch (200 questions):
Use `batch_research.py` — **19 API calls total**, then zero for answer generation.

```
Step 1 — Build cache ONCE (~90 seconds, 19 API calls):
    python3 scripts/batch_research.py build-cache

Step 2 — Verify all topics covered:
    python3 scripts/batch_research.py status

Step 3 — Generate all answers (ZERO API calls, reads from cache):
    python3 scripts/batch_research.py answer questions.txt
```

`questions.txt` format: one question per line, blank lines and `#` comments ignored.

The cache persists in `cache/knowledge_base.json`. Re-fetch only when TKE releases
major new features or Gartner changes the question structure.

---

## Step 2: Run the Research Script (Always Do This First)

Before writing any answer, use the Perplexity research script to fetch the latest
official documentation. This ensures answers reference real, verifiable capabilities
rather than outdated information.

```bash
# Research by topic
python3 scripts/research.py --topic "TKE [capability]"

# Research by MQ question
python3 scripts/research.py --question "[paste the MQ question here]"
```

**Common research queries by category:**

| Category | Command |
|---|---|
| AI/GPU workloads | `python3 scripts/research.py --topic "TKE qGPU GPU sharing AI workloads"` |
| Serverless | `python3 scripts/research.py --topic "TKE Serverless EKS capabilities"` |
| Fleet management | `python3 scripts/research.py --topic "TDCC multi-cluster fleet management"` |
| Security | `python3 scripts/research.py --topic "TKE security OIDC CAM RBAC"` |
| Edge | `python3 scripts/research.py --topic "TKE Edge KubeEdge"` |
| CNCF/ecosystem | `python3 scripts/research.py --topic "Tencent Cloud CNCF contributions Volcano KubeEdge"` |

**The script returns:**
- Specific facts with official documentation URLs
- Version numbers, limits, and configuration options
- Flags `[UNVERIFIED]` on anything it's uncertain about

Use the script output to fill in the `[⚠️ VERIFY]` gaps in the reference files, and to
get exact URLs to cite in questionnaire answers.

The API key is already embedded in the script. No setup needed.

---

## Step 2b: Load the Right Reference

Before writing any answer, check which reference file is most relevant and read it:

- **`references/tke-core.md`** — TKE standard cluster, architecture, regions, SLA
- **`references/tke-ai.md`** — GPU support, LLM serving (TACO-LLM), AI scheduling, TI-One
- **`references/tke-serverless.md`** — TKE Serverless / EKS, virtual node, scaling
- **`references/tke-fleet.md`** — TDCC (distributed cloud), multi-cluster, hybrid/edge
- **`references/tke-security.md`** — CAM, OIDC, TCM (service mesh), image scanning
- **`references/positioning.md`** — 2025 Gartner feedback, competitive positioning, what to emphasize/avoid

Always read **`references/positioning.md`** regardless of category — it contains the strategic
constraints that apply to every answer.

---

## Step 3: Answer Construction Rules

### Structure every answer as:

```
[1-sentence capability claim]

[2-3 sentences of technical detail — HOW it works]

[Quantified evidence — numbers, scale, customer metrics where available]

[Documentation URL from tencentcloud.com (English) or cloud.tencent.com (Chinese)]
```

### Mandatory formatting rules:

- **Always include a documentation URL** at the end. Use `https://www.tencentcloud.com/document/product/457/...`
  for English answers. If no specific URL is known, use the product overview:
  `https://www.tencentcloud.com/document/product/457/6759`
- **Lead with a quantified claim if possible**: "TKE supports clusters of up to X nodes..."
  not "TKE provides scalable clusters..."
- **Avoid vague adjectives**: don't write "robust", "comprehensive", "industry-leading" without
  backing them up. Dennis Smith looks for specifics.
- **Write in English**. Questionnaire answers are submitted in English.
- **Length**: 100–250 words per answer unless the question explicitly asks for a short
  yes/no + explanation.

### For questions with multiple sub-parts:
Answer each sub-part separately with a bold label:

```
**[Sub-question label]**: [answer]
```

---

## Step 4: Apply Strategic Positioning

Every answer should subtly address one or more of the **2025 Cautions** Gartner raised:

### Caution 1: "Limited momentum outside China and Southeast Asia"
→ **Counter-strategy**: In every answer that involves customer evidence, deployment regions,
or partner ecosystem — proactively cite non-China use cases, international regions, or global
customer types. Even if the question doesn't ask about geography, add a sentence like:
"This capability is available across all TKE international regions, including North America,
Western Europe, Japan, and Southeast Asia."

### Caution 2: "Partner ecosystems for enterprise businesses in global market is limited"
→ **Counter-strategy**: When relevant, mention: Tencent Cloud Marketplace (腾讯云市场),
CNCF project contributions, ecosystem integrations (Prometheus, Istio/TCM, ArgoCD, Terraform).
Don't overclaim — acknowledge that this is a growth area while showing concrete steps.

### Caution 3: "Feature sets for containerizing existing applications not as comprehensive as Leaders"
→ **Counter-strategy**: Emphasize TKE's application migration capabilities, app catalog,
refactoring tooling, and integration with DevOps pipelines (CODING DevOps, cloud-native
CI/CD). Show concrete workflows, not just feature lists.

### Caution 4: "Unavailability of latest GPU models (Nvidia H100/B200/GB200)"
→ **Counter-strategy**: This is a geopolitical hardware constraint, not a software limitation.
Acknowledge it honestly (don't pretend it doesn't exist), then pivot to **software-layer
differentiation**: GPU sharing (qGPU), dynamic GPU memory scheduling, TACO-LLM inference
optimization, TI-One for training orchestration. The message: "We compensate at the software
layer for what geopolitics constrains at the hardware layer."

---

## Step 5: Dennis Smith's Evaluation Framework

Dennis Smith (Research VP, I&O) has specific scoring priorities based on the 2025 MQ
criteria weighting:

**High-weight criteria (answer these especially well):**
- Product/Service capabilities
- Market understanding
- Offering/Product strategy
- Innovation
- Market Responsiveness/Record

**Medium-weight (solid but not flashy):**
- Sales execution/pricing
- Marketing execution
- Customer experience
- Geographic strategy

**His known biases from report analysis:**
1. He counts **quantified customer evidence** heavily (node counts, scale metrics, named industries)
2. He cares about **AI workload support** more than any other use case in 2025–2026
3. He explicitly values **serverless maturity** — Gartner predicts >50% of container deployments
   will use serverless by 2027
4. He checks **CNCF participation** as a proxy for ecosystem credibility and innovation
5. He wants to see **platform engineering / self-service IDP** capability, not just raw K8s ops
6. **Fleet management** (multi-cluster at scale) is a key differentiator in his eyes
7. He is skeptical of Chinese vendors' **international enterprise** story — prove it with evidence,
   not claims

---

## Step 6: Quality Checklist Before Finalizing

Before returning any answer, verify:

- [ ] Does it include a specific number or metric? (cluster size, node count, uptime SLA, customer scale)
- [ ] Does it include a `tencentcloud.com` documentation URL?
- [ ] Does it avoid vague adjectives without backing?
- [ ] If the topic touches geography — does it mention international availability?
- [ ] Does it address the question asked, not just describe the product generically?
- [ ] Is it 100–250 words (or appropriately scoped to the question)?
- [ ] Does it avoid claiming unavailable Nvidia GPU models (H100/B200/GB200)?

---

## Handling Gaps & Uncertainty

If a question asks about a capability that TKE **may not have** or that you're **uncertain about**:

1. **Do not fabricate**. Write what TKE does support and flag the gap with: `[⚠️ VERIFY: need internal confirmation on X]`
2. For known gaps (e.g., no native container image build service in cluster), acknowledge the
   integration path: "TKE integrates with Tencent Container Registry (TCR) and supports
   third-party CI/CD tools including Jenkins, GitLab CI, and CODING DevOps for image build workflows."
3. Always give the product team a chance to fill in specifics by flagging them clearly.

---

## Example Answer (AI Workloads)

**Question**: "Describe your product's support for running AI/ML training workloads on Kubernetes."

**Good answer**:

TKE provides a comprehensive AI/ML workload stack built on Kubernetes-native scheduling
primitives. For training workloads, TKE integrates with TI-One (Tencent Cloud's AI training
platform), which orchestrates distributed training jobs using frameworks including PyTorch,
TensorFlow, and MXNet across multi-node GPU clusters.

Key capabilities include: (1) **GPU sharing via qGPU** — multiple pods can share a single
physical GPU with memory-level isolation, improving cluster utilization by up to 40% for
inference workloads; (2) **Volcano scheduler** for gang scheduling and fair-share queuing
across AI jobs; (3) **TACO-LLM inference acceleration** for optimized LLM serving, supporting
models including Llama, Qwen, and Baichuan with up to 3x throughput improvement vs. vanilla
vLLM; (4) dynamic heterogeneous node provisioning to balance CPU and GPU capacity
automatically as training demand fluctuates.

TKE AI clusters are deployed in production at hyperscale digital services across Tencent's
ecosystem, including platforms with tens of millions of concurrent users.

Available across all TKE international regions including Singapore, Japan, Frankfurt, and Virginia.

Documentation: https://www.tencentcloud.com/document/product/457/49636

---

## Reference Files

Read these files when you need product-specific details. They contain the raw material
for building answers — capabilities, URLs, customer evidence, and known gaps.

- `references/tke-core.md` — Core product: architecture, regions, SLA, upgrade mechanics
- `references/tke-ai.md` — AI/ML: GPU, scheduling, LLM serving, training integration
- `references/tke-serverless.md` — Serverless: TKE Serverless, virtual nodes, EKS
- `references/tke-fleet.md` — Multi-cluster: TDCC, hybrid, edge (TKE Edge)
- `references/tke-security.md` — Security: IAM, image scanning, network policy, TCM
- `references/positioning.md` — Strategic context: 2025 Gartner feedback, what to emphasize
