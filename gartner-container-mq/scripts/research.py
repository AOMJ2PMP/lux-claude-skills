#!/usr/bin/env python3
"""
TKE Gartner MQ Research Tool
==============================
Uses Perplexity API (sonar-pro model) to fetch up-to-date information
from official Tencent Cloud documentation before answering MQ questions.

Usage:
    python research.py --topic "GPU sharing qGPU"
    python research.py --topic "TDCC fleet management" --verbose
    python research.py --question "Describe TKE's support for AI/ML workloads"

The script automatically:
1. Constructs a targeted search query focused on tencentcloud.com sources
2. Calls Perplexity sonar-pro for grounded, cited results
3. Prints a clean summary with source URLs for the answer-writer to use
"""

import argparse
import json
import os
import sys
import textwrap
import urllib.request
import urllib.error

# ── Config ────────────────────────────────────────────────────────────────────

API_KEY = os.environ.get("PPLX_API_KEY", "")
API_URL = "https://api.perplexity.ai/chat/completions"
MODEL   = "sonar-pro"   # grounded search model with citations

# Domains we trust for TKE product facts
TRUSTED_DOMAINS = [
    "tencentcloud.com",
    "cloud.tencent.com",
    "github.com/tkestack",
    "github.com/volcano-sh",
    "cncf.io",
]

# ── Query templates per topic category ────────────────────────────────────────

SYSTEM_PROMPT = """You are a technical research assistant helping an Analyst Relations
professional at Tencent Cloud prepare answers for the Gartner Magic Quadrant for Container
Management questionnaire.

Your job: given a topic or question, search for accurate, up-to-date facts about
Tencent Kubernetes Engine (TKE) and related products. 

Rules:
- Prioritize information from tencentcloud.com and cloud.tencent.com (official docs)
- Include specific version numbers, metrics, and quantities whenever available
- Always include the exact documentation URL for each fact
- Flag any information you are uncertain about with [UNVERIFIED]
- Do NOT invent capabilities — only report what documentation confirms
- Keep response focused and structured, under 600 words
- End with a "Key URLs" section listing all documentation links found

Format your response as:
## Summary
[2-3 sentence overview]

## Key Facts
[bullet list of specific, citable facts with URLs]

## Key URLs
[list of documentation links]
"""

def build_query(topic: str | None, question: str | None) -> str:
    """Build a targeted Perplexity search query."""
    base = (
        "Search official Tencent Cloud documentation (tencentcloud.com) for: "
    )
    if question:
        return (
            f"{base}information needed to answer this Gartner MQ question about TKE: "
            f'"{question}". '
            "Focus on: specific capabilities, metrics, version support, and documentation URLs."
        )
    return (
        f"{base}Tencent Kubernetes Engine (TKE) — {topic}. "
        "Include: specific features, configuration options, metrics, limits, and doc URLs."
    )


# ── API call ──────────────────────────────────────────────────────────────────

def call_perplexity(user_message: str, verbose: bool = False) -> dict:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message},
        ],
        "max_tokens": 1024,
        "search_domain_filter": TRUSTED_DOMAINS,
        "return_citations": True,
        "return_related_questions": False,
        "search_recency_filter": "month",   # prefer recent docs
        "temperature": 0.1,                  # low temp = more factual
    }

    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    req = urllib.request.Request(API_URL, data=data, headers=headers, method="POST")

    if verbose:
        print(f"[DEBUG] Calling {API_URL} with model={MODEL}", file=sys.stderr)
        print(f"[DEBUG] Query: {user_message[:120]}...", file=sys.stderr)

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[ERROR] HTTP {e.code}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    return result


# ── Output formatting ──────────────────────────────────────────────────────────

def format_output(result: dict, verbose: bool = False) -> str:
    lines = []

    # Main answer text
    content = result["choices"][0]["message"]["content"]
    lines.append(content)

    # Citations (if present in response)
    citations = result.get("citations", [])
    if citations:
        lines.append("\n" + "─" * 60)
        lines.append("📚 Sources cited by Perplexity:")
        for i, url in enumerate(citations, 1):
            lines.append(f"  [{i}] {url}")

    # Usage stats in verbose mode
    if verbose:
        usage = result.get("usage", {})
        lines.append(
            f"\n[DEBUG] Tokens — prompt: {usage.get('prompt_tokens', '?')}, "
            f"completion: {usage.get('completion_tokens', '?')}"
        )

    return "\n".join(lines)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Research TKE capabilities via Perplexity API for Gartner MQ answers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
        Examples:
          # Research a specific TKE topic
          python research.py --topic "qGPU GPU sharing"
          python research.py --topic "TDCC multi-cluster fleet management"
          python research.py --topic "TKE Serverless EKS pricing"
          python research.py --topic "TKEStack on-premises deployment"
          python research.py --topic "Volcano scheduler CNCF"

          # Research to answer a specific MQ question
          python research.py --question "What serverless container options does TKE offer?"
          python research.py --question "How does TKE support AI/ML GPU workloads?"
          python research.py --question "Describe TKE's multi-cluster fleet management"

          # Verbose mode shows debug info
          python research.py --topic "TKE security OIDC" --verbose
        """),
    )
    parser.add_argument(
        "--topic", "-t",
        help="A TKE capability topic to research (e.g. 'GPU sharing qGPU')",
    )
    parser.add_argument(
        "--question", "-q",
        help="A full Gartner MQ question to research for",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print debug information",
    )
    args = parser.parse_args()

    if not args.topic and not args.question:
        parser.error("Provide either --topic or --question")

    print(f"🔍 Researching via Perplexity ({MODEL})...\n", file=sys.stderr)

    query   = build_query(args.topic, args.question)
    result  = call_perplexity(query, verbose=args.verbose)
    output  = format_output(result, verbose=args.verbose)

    print(output)


if __name__ == "__main__":
    main()
