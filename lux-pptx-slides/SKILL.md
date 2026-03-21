---
name: lux-pptx-slides
description: >
  Create beautiful, on-brand PowerPoint (.pptx) slide decks using Lux's personal brand system.
  Use this skill whenever Lux asks to "make a deck", "build slides", "create a PPT", "presentation using my brand",
  "make it look like my brand", "sharing session slides", "把这个做成PPT", "做一个演示", or any request
  for a slide presentation that should match her visual identity. Also trigger when she asks for
  "a deck to explain X", "slides for my team", "slides for this topic", or uploads content and says "turn this into slides".
  This skill bakes in Lux's full brand system so every deck looks unmistakably hers — dark background,
  Electric Teal signature, DM Serif Display headings — without her having to specify it each time.
---

# Lux. PPT Slides Skill

You create polished `.pptx` slide decks that are unmistakably Lux's — dark, editorial, warm, precise. Not corporate. Not generic. Every deck uses her brand system automatically.

> **Dependency**: This skill uses `pptxgenjs`. Before writing any slide code, run:
> ```bash
> npm list -g pptxgenjs || npm install -g pptxgenjs
> ```
> Then read the full pptxgenjs guide before starting:
> ```
> /sessions/pensive-dazzling-gates/mnt/.skills/skills/pptx/pptxgenjs.md
> ```

---

## Step 0 — Before You Write a Single Slide

1. **Install pptxgenjs** (command above)
2. **Read** `pptx/pptxgenjs.md` for the full API reference
3. **Choose a template** from Section 3 below — match it to the topic
4. **Plan the narrative** in 1–2 sentences: what story are these slides telling?

---

## Step 1 — Clarify (if needed)

Ask only if the topic or audience is unclear. Default assumptions if not specified:
- **Audience**: internal team or professional peers
- **Length**: 8–12 slides
- **Language**: match whatever language Lux writes the request in (Chinese or English or mixed)
- **Tone**: Sharing Session (see brand voice below)

---

## Step 2 — Brand System

Apply these values in every single deck. They are non-negotiable defaults.

### Colors

```
Slide background:   #1A1A1E   (slightly darker than brand base)
Surface / cards:    #2A2A2E
Raised panel:       #323237

Text primary:       #F0EFE8
Text secondary:     #9E9D99
Text muted:         #6A6966

Teal (signature):   #2ECFBE   ← appears on EVERY slide
Lemon (precise):    #E8D44D   ← code, data, technical
Violet (grounded):  #9B7FE8   ← personal, reflective
Rose (in motion):   #F06292   ← action, urgency
```

**Color rules:**
- Teal must appear on every slide (at least as an eyebrow label, accent line, or icon color)
- Use ONE accent (lemon / violet / rose) per deck — pick based on topic mood
  - Technical / data-heavy → Lemon
  - Reflective / personal story → Violet
  - Action / call to action / energy → Rose
- Never put all four accent colors in one deck

### Typography (pptxgenjs font names)

```
Display:   "DM Serif Display"   → slide titles, hero text, pull quotes
Body:      "Noto Sans SC"       → body copy, bullets, captions
Mono:      "Fira Code"          → labels, eyebrows, dates, URLs, hex values
```

**Font size rules — read carefully:**

| Element | Font | Size (pt) | Weight |
|---------|------|-----------|--------|
| Hero title | DM Serif Display | 44–54 | Regular |
| Slide title | DM Serif Display | 36–40 | Regular |
| Section label / eyebrow | Fira Code | 11–13 | Regular |
| Body paragraph | Noto Sans SC | 16–18 | 300 |
| Bullet item | Noto Sans SC | 15–17 | 400 |
| Caption / metadata | Fira Code | 10–12 | Regular |
| Stat number | DM Serif Display | 60–80 | Regular |
| Stat label | Noto Sans SC | 13–14 | 500 |

**Why these sizes:** Presentations are read at a distance. 16pt is the *minimum* for body text. Never go below 14pt for anything the audience needs to read. Titles should feel commanding — 36pt+ always.

### Slide anatomy

Every slide has these layers:
1. **Background** — solid `#1A1A1E`, no gradients
2. **Eyebrow** (optional) — Fira Code, 11pt, Teal `#2ECFBE`, uppercase, top-left area
3. **Title** — DM Serif Display, 36–54pt, primary text `#F0EFE8`; the KEY phrase in italic Teal
4. **Content** — varies by template (see Section 3)
5. **Footer** — Fira Code, 10pt, muted `#6A6966`; left: topic/section name; right: `Lux.` logotype

### The logotype rule
The footer always ends with `Lux.` where the period is rendered in Teal. In pptxgenjs, use a text array with two runs:
```js
{ text: "Lux", options: { color: "F0EFE8", fontFace: "DM Serif Display", fontSize: 10 } },
{ text: ".", options: { color: "2ECFBE", fontFace: "DM Serif Display", fontSize: 10, italic: true } }
```

---

## Step 3 — Slide Templates

Pick the right template for each slide's content. Mix and match within a deck.

Read `references/templates.md` for complete pptxgenjs code examples for each template.

### Template A — Title / Cover
**Use for:** Opening slide, section divider
- Full-bleed dark background
- Large hero title (DM Serif Display, 48–54pt) with italic teal on key phrase
- Tagline or subtitle in Noto Sans SC, 16pt, secondary text
- Eyebrow: Fira Code, teal, uppercase — context like "INTERNAL · MARCH 2026"
- Bottom: `Lux.` logotype + date in Fira Code

### Template B — One Big Idea
**Use for:** Key message, thesis statement, memorable quote
- Single pull quote or statement — DM Serif Display, 32–40pt
- Italic teal on the most important 2–4 words
- Optional supporting sentence in Noto Sans SC, 16pt, secondary
- Teal accent line (2pt thick, 60px wide) above the quote
- Minimal — lots of breathing room

### Template C — Bullet Points (max 5 items)
**Use for:** Lists, key points, takeaways
- Title top-left, DM Serif Display 36pt
- Eyebrow label in teal Fira Code
- Each bullet: colored dot (4px circle, teal or accent) + Noto Sans SC 16pt text
- Max 5 bullets. If you have more, split into two slides.
- Generous line spacing (1.4× minimum)
- Optional: one callout box (bg: `#323237`, border-left: 3pt teal) for the most important point

### Template D — Two Column
**Use for:** Comparison, before/after, problem vs. solution, concept pairs
- Left column + right column, equal width, 0.2" gap
- Each column: small label (Fira Code, teal, 11pt) + content
- Column bg: `#2A2A2E` with 1pt border `rgba(255,255,255,0.08)`
- Title above both columns, DM Serif Display 36pt

### Template E — Big Stat / Number
**Use for:** A striking data point, metric, or number that anchors a slide
- Centered or left-aligned large number: DM Serif Display 72–80pt, Teal
- Label below: Noto Sans SC 14pt, secondary text
- Supporting context: Noto Sans SC 15pt, muted, beneath label
- Optional: 3 smaller supporting stats in a row (36pt / 13pt pattern)

### Template F — Process / Timeline (3–5 steps)
**Use for:** How something works, step-by-step flow, workflow
- Numbered steps in a horizontal row (or vertical if 4+)
- Step number: Fira Code 11pt, teal
- Step title: Noto Sans SC 14pt, 500 weight, primary
- Step body: Noto Sans SC 13pt, 300 weight, secondary
- Connector: thin line `#3C3C42`, 1pt between steps
- Active/highlight step: accent color bg `rgba(46,207,190,0.12)`, teal border

### Template G — Code / Technical
**Use for:** Showing code, commands, technical output, config
- Code block: bg `#111113`, font Fira Code 13pt, text `#F0EFE8`
- Syntax accent: keywords in Teal, strings in Lemon
- Label above code block: Fira Code 10pt, muted
- Context/explanation: Noto Sans SC 15pt beside or below the code block

### Template H — Closing / Summary
**Use for:** Final slide, key takeaway, what to do next
- Simple, spacious — like Template B but more explicit
- "Key takeaway" eyebrow in teal Fira Code
- 1–2 sentence summary in DM Serif Display 28–32pt
- Optional: 2–3 action items as small bullets
- `Lux.` logotype centered at bottom, larger (18pt)
- Date + `luxlu.fun` in Fira Code muted

---

## Step 4 — Build Process

```bash
# 1. Install if needed
npm list -g pptxgenjs || npm install -g pptxgenjs

# 2. Write your slide script to /sessions/pensive-dazzling-gates/slides.js

# 3. Run it
node /sessions/pensive-dazzling-gates/slides.js

# 4. Output goes to the workspace folder
# Copy final file:
cp /sessions/pensive-dazzling-gates/output.pptx \
   "/sessions/pensive-dazzling-gates/mnt/lux brand guideline skill/<filename>.pptx"
```

---

## Step 5 — QA (Required)

**Always do this before presenting the file to Lux.**

```bash
# Convert to images for visual inspection
python /sessions/pensive-dazzling-gates/mnt/.skills/skills/pptx/scripts/office/soffice.py \
  --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
ls slide-*.jpg
```

Then read each slide image and verify:
- Every slide has the teal color present somewhere
- Title font is DM Serif Display (not a fallback)
- No text is cut off or overflowing
- No slide is text-only with no visual element
- Eyebrow and footer are visible on every slide
- Font sizes feel readable at presentation distance (titles bold and large, body not tiny)
- Accent color is used consistently (same one throughout the deck)

Fix any issues before delivering.

---

## Step 6 — Voice Check

Before finalizing, read each slide's copy aloud and ask:

- Does this sound like Lux wrote it? (Curious, direct, specific)
- Is the title concrete? (Not "Key Insights" → "What I learned after 3 weeks of using this")
- Are there any bullets that could be cut? (5 bullets > 7 bullets, always)
- Is the key phrase in italic teal actually the most important thing on the slide?

---

## Quick Reference

```
EVERY SLIDE NEEDS:
  ✓ Teal somewhere (eyebrow, accent, logotype period)
  ✓ DM Serif Display title, 36pt+
  ✓ Footer with Lux. logotype
  ✓ At least one visual element (not just text)
  ✓ Max 5 bullets if using bullet template

FONT MINIMUMS:
  Body text:  16pt
  Captions:   12pt (Fira Code only)
  Titles:     36pt

NEVER:
  ✗ White or light background (dark only, #1A1A1E)
  ✗ All four accent colors in one deck
  ✗ More than 5 bullets on one slide
  ✗ Generic font fallbacks (Arial, Calibri)
  ✗ Missing footer / Lux. logotype
  ✗ Underline decorations under titles
```
