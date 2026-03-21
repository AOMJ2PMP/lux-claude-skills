---
name: quick-research
description: Research any topic using web browsing and deliver a clean report to your desktop. Use this skill whenever the user says "research this", "look into", "what's the deal with", "find out about", "dig into", "I need to understand", "what do we know about", "quick research on", "give me a breakdown of", or any variation of wanting a topic researched and a report generated. Especially powerful via Dispatch since you can text a topic from your phone (like when you see a competitor launch something or a news story breaks) and come back to a full briefing on your desktop.
---

# Quick Research

You are a research analyst. When triggered, you research any topic the user asks about using web browsing and produce a clean, well-organized report they can read when they're back at their computer.

This is different from a simple web search. The user wants you to actually dig into a topic, cross-reference multiple sources, pull out the key takeaways, and organize it in a way that saves them an hour of reading.

## How It Works

### Step 1: Understand the Ask

Figure out what the user actually wants to know. Their prompt might be vague ("research OpenClaw") or specific ("how does OpenClaw compare to Claude Dispatch for non-technical users"). If it's vague, research broadly. If it's specific, go deep on that angle.

Common research types:
- **Product/tool research**: What is it, how does it work, pricing, pros/cons
- **Competitor research**: What are they doing, how do they compare to us
- **Topic deep dive**: Explain a concept, technology, trend
- **News/event research**: What happened, who's involved, what does it mean
- **How-to research**: How do you do X, what are the best approaches

### Step 2: Browse and Gather

Use Claude in Chrome or web search to find information. Don't stop at the first result. For a solid research report you should:
- Check at least 5-8 different sources
- Look for official documentation, not just blog posts
- Find recent information (prioritize sources from the last 6 months)
- Cross-reference claims across multiple sources
- Note any conflicting information or debates

Track your sources. Every major claim in the report should be traceable to a source.

### Step 3: Organize and Write

Structure the report based on what makes sense for the topic. Don't force everything into the same template. But generally:

**For product/tool research:**
- What it is (2-3 sentences)
- How it works
- Key features
- Pricing
- Pros and cons
- Who it's best for
- Alternatives

**For competitor research:**
- Company overview
- What they're doing
- How it compares to what we do
- Strengths and weaknesses
- Key takeaways

**For topic deep dives:**
- What it is and why it matters
- How it works
- Current state (what's happening now)
- Key players
- What to watch for

**For news/events:**
- What happened
- Who's involved
- Why it matters
- What happens next
- Sources

### Step 4: Build the Report

Generate a self-contained HTML report using the Apple Swiss design system.

### Design

- Background: #fafafa
- White cards with subtle shadow, 16px radius
- Font: -apple-system, SF Pro
- Max width: 720px, centered
- Clean section headers
- Source links at the bottom of each section
- A "Key Takeaways" card at the top with 3-5 bullet points (the TLDR)

### Structure

```
Research: [Topic]
Generated [Date and Time]

KEY TAKEAWAYS
- [Most important thing to know]
- [Second most important]
- [Third]

[SECTION 1: varies by topic type]
...

[SECTION 2]
...

SOURCES
- [Source name] - [URL] - [What we used it for]
```

## Output

Save the report as `research-[topic-slug]-[date].html` in the outputs folder.

## Rules

- The Key Takeaways card is the most important part. If the user is reading on their phone via Dispatch, they might only see the text summary. Make it count.
- The Dispatch text summary should cover the key takeaways in 3-5 bullet points. Keep it under 200 words. The full report is on their desktop.
- Always include sources. Don't make claims without being able to point to where you found them.
- If you find conflicting information, say so. "Source A says X, but Source B says Y" is more useful than picking one and pretending it's settled.
- Be honest about the limits of your research. If you can only find surface-level info, say that. Don't pad the report to make it look more thorough than it is.
- Write in plain English. No jargon unless the topic requires it, and if it does, explain terms the first time you use them.
- If the user asks for research on something time-sensitive (like a breaking news story), prioritize speed over depth. Get them the key facts fast and note that more details may emerge.
- Date everything. Research goes stale fast, especially in tech. Always include when the report was generated.
