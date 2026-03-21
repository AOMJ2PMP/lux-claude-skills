#!/usr/bin/env python3
"""
TKE MQ Batch Research Tool
============================
Pre-fetches ALL topic knowledge in one batch run (~15-20 API calls total),
caches results to JSON, then generates answers from cache without further API calls.

Workflow:
    Step 1 - Build the knowledge cache (run once):
        python3 batch_research.py --build-cache

    Step 2 - Generate answers from a question file:
        python3 batch_research.py --answer questions.txt

    Step 3 - (Optional) Regenerate a single answer:
        python3 batch_research.py --answer-one "Describe TKE's GPU support"

The cache is stored in: cache/knowledge_base.json
Once built, answer generation costs zero API calls.
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# ── Config ─────────────────────────────────────────────────────────────────────

API_KEY  = os.environ.get("PPLX_API_KEY", "")
API_URL  = "https://api.perplexity.ai/chat/completions"
MODEL    = "sonar-pro"
CACHE_DIR = Path(__file__).parent.parent / "cache"
CACHE_FILE = CACHE_DIR / "knowledge_base.json"

# Rate limiting: sonar-pro allows ~20 req/min on standard tier
# We use 4s between calls = safe at ~15 calls/min
CALL_DELAY_SECONDS = 4

TRUSTED_DOMAINS = [
    "tencentcloud.com",
    "cloud.tencent.com",
    "github.com/tkestack",
    "github.com/volcano-sh",
]

# ── Topic definitions ──────────────────────────────────────────────────────────
# Each topic maps to a group of related MQ questions.
# ~18 topics cover the full 200-question questionnaire.

RESEARCH_TOPICS = {
    # ── Core infrastructure ──────────────────────────────────────────────
    "cluster_lifecycle": {
        "query": "TKE cluster creation provisioning upgrades node management auto-repair SLA availability",
        "covers": ["cluster provisioning", "version upgrades", "node auto-repair", "SLA", "control plane management"],
    },
    "networking": {
        "query": "TKE networking VPC-CNI GlobalRouter CNI plugins service mesh TCM load balancing ingress",
        "covers": ["CNI", "VPC networking", "load balancer", "ingress", "network policy", "service mesh"],
    },
    "storage": {
        "query": "TKE storage CBS CFS COS CSI driver persistent volumes stateful workloads",
        "covers": ["persistent storage", "CBS CSI", "CFS NFS", "COS object storage", "stateful sets"],
    },
    "scaling_autoscaling": {
        "query": "TKE horizontal pod autoscaler cluster autoscaler node pools scaling limits metrics",
        "covers": ["HPA", "VPA", "cluster autoscaler", "node pool scaling", "KEDA"],
    },

    # ── AI / ML workloads ────────────────────────────────────────────────
    "gpu_sharing_qgpu": {
        "query": "TKE qGPU GPU sharing isolation memory compute fraction pods per GPU supported models",
        "covers": ["GPU sharing", "qGPU", "MIG", "GPU isolation", "multi-tenant GPU"],
    },
    "ai_scheduling": {
        "query": "TKE Volcano scheduler gang scheduling AI ML batch jobs priority queuing GPU scheduling",
        "covers": ["Volcano", "gang scheduling", "batch AI jobs", "fair-share queuing", "preemption"],
    },
    "llm_inference": {
        "query": "Tencent Cloud TACO-LLM LLM serving inference acceleration TKE model deployment",
        "covers": ["LLM serving", "TACO-LLM", "inference optimization", "model serving on K8s"],
    },
    "ai_training": {
        "query": "TKE TI-One AI training platform PyTorch TensorFlow distributed training Kubernetes",
        "covers": ["distributed training", "TI-One", "ML frameworks", "training jobs"],
    },

    # ── Serverless ───────────────────────────────────────────────────────
    "serverless": {
        "query": "TKE Serverless EKS elastic kubernetes service serverless containers pricing scale-to-zero GPU",
        "covers": ["TKE Serverless", "EKS", "virtual node", "serverless billing", "scale-to-zero"],
    },

    # ── Fleet & multi-cluster ────────────────────────────────────────────
    "fleet_management": {
        "query": "TDCC Tencent Distributed Cloud Center multi-cluster fleet management lifecycle policy distribution",
        "covers": ["TDCC", "multi-cluster", "fleet management", "cluster registration", "policy distribution"],
    },
    "hybrid_edge": {
        "query": "TKE Edge TKEStack KubeEdge edge computing bare metal on-premises hybrid cloud",
        "covers": ["TKE Edge", "edge deployment", "TKEStack", "on-premises", "bare metal", "air-gapped"],
    },

    # ── Security ─────────────────────────────────────────────────────────
    "security_iam": {
        "query": "TKE security CAM RBAC OIDC pod identity service account token namespace isolation",
        "covers": ["CAM RBAC", "OIDC", "pod identity", "namespace isolation", "least privilege"],
    },
    "security_images": {
        "query": "TCR Tencent Container Registry image scanning vulnerability CVE signing supply chain",
        "covers": ["TCR", "image scanning", "vulnerability", "image signing", "supply chain security"],
    },
    "security_runtime": {
        "query": "TKE runtime security network policy seccomp AppArmor OPA Gatekeeper admission control",
        "covers": ["runtime security", "network policy", "OPA Gatekeeper", "admission webhooks", "seccomp"],
    },

    # ── Developer experience & platform engineering ───────────────────────
    "devops_cicd": {
        "query": "TKE CODING DevOps CI/CD pipeline GitOps ArgoCD Flux Helm chart deployment blue-green canary",
        "covers": ["CI/CD", "CODING DevOps", "GitOps", "ArgoCD", "Helm", "blue-green deployment"],
    },
    "platform_engineering": {
        "query": "TKE platform engineering self-service IDP developer portal namespace management template catalog",
        "covers": ["platform engineering", "self-service", "developer portal", "namespace management"],
    },

    # ── Observability ────────────────────────────────────────────────────
    "observability": {
        "query": "TKE monitoring logging Prometheus Grafana CLS CloudMonitor distributed tracing alerting",
        "covers": ["monitoring", "logging CLS", "Prometheus", "Grafana", "distributed tracing", "alerting"],
    },

    # ── Global / ecosystem ───────────────────────────────────────────────
    "global_regions_customers": {
        "query": "Tencent Cloud TKE international regions availability zones global customers enterprise gaming",
        "covers": ["global regions", "international availability", "customer evidence", "enterprise"],
    },
    "cncf_ecosystem": {
        "query": "Tencent Cloud CNCF contributions Kubernetes Volcano KubeEdge open source projects count",
        "covers": ["CNCF", "open source", "ecosystem", "Kubernetes contributions", "community"],
    },
}

# ── Perplexity API call ────────────────────────────────────────────────────────

RESEARCH_SYSTEM = """You are a technical research assistant. Search official Tencent Cloud
documentation (tencentcloud.com) and return structured facts about TKE (Tencent Kubernetes Engine).

Rules:
- Only report what documentation confirms; flag uncertainty with [UNVERIFIED]
- Include specific metrics: node limits, API versions, pricing units, supported versions
- Always include exact documentation URLs for each fact
- Be concise: max 500 words per response
- Format: bullet points with inline URLs

Output format:
## Facts
- [fact with metric/detail] (URL: https://...)
- ...

## Key URLs
- [url]: [what it covers]
"""

def call_perplexity(query: str, retries: int = 3) -> dict | None:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": RESEARCH_SYSTEM},
            {"role": "user", "content": f"Research for TKE MQ questionnaire: {query}"},
        ],
        "max_tokens": 800,
        "search_domain_filter": TRUSTED_DOMAINS,
        "return_citations": True,
        "temperature": 0.1,
    }
    data = json.dumps(payload).encode()
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    for attempt in range(retries):
        req = urllib.request.Request(API_URL, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f"  ⚠️  Rate limited (429). Waiting {wait}s before retry {attempt+1}/{retries}...")
                time.sleep(wait)
            else:
                print(f"  ✗ HTTP {e.code}: {body[:100]}")
                return None
        except Exception as e:
            print(f"  ✗ Error: {e}")
            if attempt < retries - 1:
                time.sleep(5)
    return None


# ── Cache management ───────────────────────────────────────────────────────────

def load_cache() -> dict:
    if CACHE_FILE.exists():
        with open(CACHE_FILE) as f:
            return json.load(f)
    return {}

def save_cache(cache: dict):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def build_cache(force: bool = False):
    """Fetch all topics from Perplexity and cache results. Skips already-cached topics."""
    cache = load_cache()
    topics_to_fetch = [
        k for k in RESEARCH_TOPICS
        if force or k not in cache
    ]

    if not topics_to_fetch:
        print("✅ Cache is already complete. Use --force to rebuild.")
        return

    total = len(topics_to_fetch)
    print(f"📡 Fetching {total} topics (already cached: {len(RESEARCH_TOPICS) - total})")
    print(f"   Estimated time: ~{total * CALL_DELAY_SECONDS // 60}m {total * CALL_DELAY_SECONDS % 60}s\n")

    for i, topic_key in enumerate(topics_to_fetch, 1):
        topic = RESEARCH_TOPICS[topic_key]
        print(f"[{i:2d}/{total}] {topic_key}...", end=" ", flush=True)

        result = call_perplexity(topic["query"])

        if result:
            content = result["choices"][0]["message"]["content"]
            citations = result.get("citations", [])
            cache[topic_key] = {
                "query": topic["query"],
                "covers": topic["covers"],
                "content": content,
                "citations": citations,
                "fetched_at": time.strftime("%Y-%m-%d %H:%M"),
            }
            save_cache(cache)  # save after each call so progress isn't lost
            print(f"✓ ({len(content)} chars, {len(citations)} citations)")
        else:
            print("✗ FAILED — will retry on next run")

        # Rate limit protection between calls
        if i < total:
            time.sleep(CALL_DELAY_SECONDS)

    cached_count = sum(1 for k in RESEARCH_TOPICS if k in cache)
    print(f"\n✅ Cache complete: {cached_count}/{len(RESEARCH_TOPICS)} topics")
    print(f"   Saved to: {CACHE_FILE}")


# ── Topic classifier ──────────────────────────────────────────────────────────

# Keyword → topic_key mapping for question routing
QUESTION_ROUTER = {
    # AI / GPU
    "gpu": "gpu_sharing_qgpu",
    "qgpu": "gpu_sharing_qgpu",
    "cuda": "gpu_sharing_qgpu",
    "inference": "llm_inference",
    "llm": "llm_inference",
    "large language": "llm_inference",
    "training": "ai_training",
    "pytorch": "ai_training",
    "tensorflow": "ai_training",
    "volcano": "ai_scheduling",
    "gang sched": "ai_scheduling",
    "batch job": "ai_scheduling",
    "ai workload": "ai_scheduling",
    "ml workload": "ai_scheduling",
    # Serverless
    "serverless": "serverless",
    "scale to zero": "serverless",
    "elastic kubernetes": "serverless",
    "eks": "serverless",
    "virtual node": "serverless",
    # Fleet / multi-cluster
    "fleet": "fleet_management",
    "multi-cluster": "fleet_management",
    "multicluster": "fleet_management",
    "tdcc": "fleet_management",
    "distributed cloud": "fleet_management",
    "edge": "hybrid_edge",
    "on-premises": "hybrid_edge",
    "on premises": "hybrid_edge",
    "bare metal": "hybrid_edge",
    "air-gap": "hybrid_edge",
    "tkestack": "hybrid_edge",
    # Security
    "rbac": "security_iam",
    "iam": "security_iam",
    "oidc": "security_iam",
    "access control": "security_iam",
    "image scan": "security_images",
    "vulnerability": "security_images",
    "supply chain": "security_images",
    "tcr": "security_images",
    "network policy": "security_runtime",
    "admission": "security_runtime",
    "opa": "security_runtime",
    "runtime security": "security_runtime",
    # DevOps / Platform
    "ci/cd": "devops_cicd",
    "cicd": "devops_cicd",
    "gitops": "devops_cicd",
    "argocd": "devops_cicd",
    "helm": "devops_cicd",
    "pipeline": "devops_cicd",
    "platform engineer": "platform_engineering",
    "self-service": "platform_engineering",
    "developer portal": "platform_engineering",
    # Core infra
    "autoscal": "scaling_autoscaling",
    "hpa": "scaling_autoscaling",
    "cluster autoscal": "scaling_autoscaling",
    "storage": "storage",
    "persistent": "storage",
    "cbs": "storage",
    "cfs": "storage",
    "network": "networking",
    "cni": "networking",
    "vpc": "networking",
    "ingress": "networking",
    "upgrade": "cluster_lifecycle",
    "provision": "cluster_lifecycle",
    "sla": "cluster_lifecycle",
    "node repair": "cluster_lifecycle",
    # Observability
    "monitor": "observability",
    "logging": "observability",
    "prometheus": "observability",
    "tracing": "observability",
    "alert": "observability",
    # Global / ecosystem
    "region": "global_regions_customers",
    "customer": "global_regions_customers",
    "international": "global_regions_customers",
    "global": "global_regions_customers",
    "cncf": "cncf_ecosystem",
    "open source": "cncf_ecosystem",
    "ecosystem": "cncf_ecosystem",
    "contribution": "cncf_ecosystem",
}

def classify_question(question: str) -> list[str]:
    """Return a list of relevant topic keys for a question."""
    q_lower = question.lower()
    matched = set()
    for keyword, topic in QUESTION_ROUTER.items():
        if keyword in q_lower:
            matched.add(topic)
    return list(matched) if matched else ["cluster_lifecycle"]  # fallback


# ── Answer generation ──────────────────────────────────────────────────────────

ANSWER_SYSTEM = """You are writing answers for Tencent Cloud's TKE product in the
Gartner Magic Quadrant for Container Management questionnaire.

Use ONLY the research facts provided. Do not add information from general knowledge.

Answer format:
- 1 sentence: direct capability claim with a specific metric
- 2-3 sentences: technical detail of HOW it works
- 1 sentence: quantified evidence or customer scale
- 1 sentence: international availability (always include)
- Final line: Documentation URL: [url]

Rules:
- 100-200 words per answer
- No vague adjectives without numbers (no "robust", "comprehensive" alone)
- Never claim H100/B200/GB200 GPU availability
- Always mention at least one international region
- Flag uncertain facts with [VERIFY INTERNALLY]
"""

def generate_answer(question: str, cache: dict) -> str:
    """Generate a questionnaire answer using cached research only (no API calls)."""
    topic_keys = classify_question(question)

    # Gather relevant cached research
    context_parts = []
    for key in topic_keys:
        if key in cache:
            entry = cache[key]
            context_parts.append(f"### Research: {key}\n{entry['content']}")
            if entry.get("citations"):
                context_parts.append("Citations: " + ", ".join(entry["citations"][:5]))

    # Also always include positioning context (no API needed - it's static)
    positioning_path = Path(__file__).parent.parent / "references" / "positioning.md"
    if positioning_path.exists():
        positioning = positioning_path.read_text()[:1500]  # first 1500 chars
        context_parts.append(f"### Strategic Positioning\n{positioning}")

    if not context_parts:
        return f"[⚠️ No cached research for this question. Run: python3 batch_research.py --build-cache]\nQuestion was: {question}"

    context = "\n\n".join(context_parts)

    # Use Anthropic API via the artifact system — but since we're in Claude.ai,
    # we return a structured prompt for Claude to complete directly.
    # This function returns the assembled context + question for Claude to answer.
    return f"""RESEARCH CONTEXT:
{context}

QUESTION TO ANSWER:
{question}

[Claude: Using the research context above, write a Gartner MQ answer following the format in your SKILL.md instructions.]"""


def answer_questions_file(filepath: str, cache: dict):
    """Read a file of questions (one per line) and generate answers for all."""
    questions_path = Path(filepath)
    if not questions_path.exists():
        print(f"File not found: {filepath}")
        sys.exit(1)

    questions = [
        line.strip()
        for line in questions_path.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

    print(f"📝 Generating answers for {len(questions)} questions...")
    print(f"   Using cache: {CACHE_FILE}\n")

    output_lines = []
    for i, question in enumerate(questions, 1):
        topics = classify_question(question)
        print(f"[{i:3d}/{len(questions)}] → topics: {topics}")
        answer_context = generate_answer(question, cache)
        output_lines.append(f"## Q{i}: {question}\n\n{answer_context}\n\n---\n")

    output_file = questions_path.parent / (questions_path.stem + "_answers.md")
    output_file.write_text("\n".join(output_lines))
    print(f"\n✅ Answers saved to: {output_file}")


# ── Cache status ──────────────────────────────────────────────────────────────

def show_status():
    cache = load_cache()
    print(f"Cache file: {CACHE_FILE}")
    print(f"Topics cached: {len(cache)}/{len(RESEARCH_TOPICS)}\n")
    for key, topic in RESEARCH_TOPICS.items():
        status = "✅" if key in cache else "❌"
        fetched = cache[key].get("fetched_at", "?") if key in cache else "not fetched"
        print(f"  {status} {key:30s} ({fetched})")
        print(f"     Covers: {', '.join(topic['covers'][:3])}...")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Batch research and answer generation for Gartner Container MQ",
    )
    subparsers = parser.add_subparsers(dest="command")

    # build-cache
    p_cache = subparsers.add_parser("build-cache", help="Fetch all topics from Perplexity and cache")
    p_cache.add_argument("--force", action="store_true", help="Re-fetch even already-cached topics")

    # status
    subparsers.add_parser("status", help="Show cache status")

    # answer (from file)
    p_answer = subparsers.add_parser("answer", help="Generate answers for all questions in a file")
    p_answer.add_argument("questions_file", help="Path to .txt file with one question per line")

    # answer-one
    p_one = subparsers.add_parser("answer-one", help="Generate answer for a single question")
    p_one.add_argument("question", help="The question to answer")

    args = parser.parse_args()

    if args.command == "build-cache":
        build_cache(force=getattr(args, "force", False))

    elif args.command == "status":
        show_status()

    elif args.command == "answer":
        cache = load_cache()
        answer_questions_file(args.questions_file, cache)

    elif args.command == "answer-one":
        cache = load_cache()
        result = generate_answer(args.question, cache)
        print(result)

    else:
        parser.print_help()
        print("\nQuick start:")
        print("  1. python3 batch_research.py build-cache        # ~90 seconds, run once")
        print("  2. python3 batch_research.py status             # verify all topics cached")
        print("  3. python3 batch_research.py answer questions.txt  # generate all answers")


if __name__ == "__main__":
    main()
