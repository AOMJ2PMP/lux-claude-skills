---
name: lux-brand-guideline
description: Apply Lux's personal brand system to any creative or visual output. Use this skill whenever Lux asks to create, design, style, or write anything that should feel "on-brand" — including blog posts, slide decks, sharing session materials, social content, HTML artifacts, email templates, personal bios, or any other output that represents her publicly. Also trigger when she asks to "make it look like mine", "keep it consistent with my brand", or "use my brand colors/fonts". This skill defines Lux's complete visual identity, color palette, typography stack, voice guidelines, and usage examples — consult it before generating any artifact that Lux will publish or present under her own name.
---

# Lux. Brand Guideline — Execution Skill

> This skill gives you everything needed to produce on-brand output for Lux Lu.
> Read this **before** writing any HTML, slide, email, post, or visual artifact.
> The HTML reference file `lux_brand_guideline.html` (same folder) is a live visual example — open or read it when you need to see how components look in practice.

---

## Step 0 — How to Use This Skill

When Lux asks for any creative output:

1. **Read this file** (you're doing that now — good).
2. **Choose the right context** from Section 6 (blog, slide, LinkedIn, HTML artifact, etc.).
3. **Apply the CSS variables and font imports** from Section 3 to any HTML output.
4. **Follow the voice rules** from Section 5 when writing copy.
5. **Check yourself**: Is teal present? Is one accent color used consistently? Does the writing sound like Lux?

---

## Section 1 — Core Identity

**Logotype:** `Lux.`
- Font: DM Serif Display
- The period `.` is always italic, always Electric Teal `#2ECFBE`
- Never omit the period. It says: *I finished the thought.*

**Tagline:** `"Action Generates Information"`
— render in Fira Code, small, uppercase when used as a label or eyebrow

**Positioning:**
> "A young professional who takes AI seriously, thinks in systems, and writes like a real person."

**Four brand words** (each owns a color — use them for emphasis, tags, or section themes):

| Word | Color | Hex | Meaning |
|------|-------|-----|---------|
| Curious | Electric Teal | `#2ECFBE` | Signature — always present |
| Grounded | Violet | `#9B7FE8` | Depth, reflection, personal writing |
| Precise | Lemon | `#E8D44D` | Data, code, technical detail |
| In Motion | Rose | `#F06292` | Action, energy, urgency |

---

## Section 2 — Color System

**Base is deep gray, not white.** Built for screen-first.

```
--bg:          #2A2A2E   ← page background (always)
--bg-raised:   #323237   ← cards, panels
--bg-high:     #3C3C42   ← headers, nav bars
--border:      rgba(255,255,255,0.08)
--border-md:   rgba(255,255,255,0.14)

--teal:        #2ECFBE   ← SIGNATURE — use in every layout
--teal-pale:   rgba(46,207,190,0.12)
--yellow:      #E8D44D   ← Precise
--yellow-pale: rgba(232,212,77,0.12)
--violet:      #9B7FE8   ← Grounded
--violet-pale: rgba(155,127,232,0.12)
--rose:        #F06292   ← In Motion
--rose-pale:   rgba(240,98,146,0.12)

--t1:          #F0EFE8   ← primary text
--t2:          #9E9D99   ← secondary text / captions
--t3:          #6A6966   ← muted labels
```

**Rules:**
- Teal is the through-line — it **must** appear in every layout. Nav, links, brand mark, accents.
- Use **one** accent color at a time (violet, lemon, or rose). Never all four.
- ❌ Never use warm cream `#F5F0E8` or copper `#C4622A` — those are Anthropic's palette.
- Light mode (`#F2F1EE` bg) only for print or explicit light-mode variants; darken teal to `#1A9A8E` on light.

---

## Section 3 — Typography

### Font Import (always include in HTML `<head>`)

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Noto+Sans+SC:wght@300;400;500&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
```

### CSS Variables

```css
--fd: 'DM Serif Display', Georgia, serif;
--fs: 'Noto Sans SC', system-ui, sans-serif;
--fm: 'Fira Code', monospace;
```

### Font Roles

| Role | Font | Size | Weight | Use |
|------|------|------|--------|-----|
| Hero | DM Serif Display | `clamp(80px,14vw,130px)` | Regular | Page hero |
| H1 | DM Serif Display | `50px` | Regular | Post titles |
| H2 | DM Serif Display | `34–42px` | Regular | Section headings |
| H3 / Pull | DM Serif Display | `22–26px` | **Italic** | Pull quotes, emphasis |
| Body | Noto Sans SC | `15–16px` | 300 | Long-form reading |
| UI | Noto Sans SC | `13–14px` | 400 | Interface text |
| Label | Noto Sans SC | `13px` | 500 | Bold UI labels |
| Mono / Detail | Fira Code | `11–15px` | 400 | Dates, URLs, hex codes, taglines |

**Rules:**
- Italic in DM Serif Display **carries emotion** — use it for phrases that matter, not decoration.
- Noto Sans SC handles Chinese + English inline natively. **Never switch fonts or apologize for mixing languages.**
- Fira Code is for metadata — section numbers, dates, hex values, URLs, brand taglines.

---

## Section 4 — Animation Defaults

For HTML artifacts, use scroll-reveal on entering elements:

```css
.rv {
  opacity: 0;
  transform: translateY(14px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.rv.in {
  opacity: 1;
  transform: translateY(0);
}
```

```js
const obs = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
}), { threshold: 0.1 });
document.querySelectorAll('.rv').forEach(el => obs.observe(el));
```

Hero elements use `animation: up 0.6s ease forwards` with staggered delays (0.1s, 0.2s, 0.3s…).

```css
@keyframes up {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

---

## Section 5 — Voice & Tone

### ✅ Do this
- Start with a concrete observation or question
- Mix Chinese and English naturally — no apology needed
- Name the tension before you resolve it
- Use short sentences when making a point
- Reference specific tools, not vague categories
- Show you tried something before talking about it
- Let curiosity show — it's more interesting than authority

### ❌ Avoid this
- Corporate-speak ("leverage synergies", "holistic approach")
- Fake certainty ("Obviously, the best way is…")
- Over-hedging until you say nothing
- Lists of 7+ items that could be 3
- Generic AI content aesthetics — sounds like everyone else
- Putting conclusions first, action last
- Sounding like a press release about yourself

### Tone by context

| Context | Tone |
|---------|------|
| **Blog (luxlu.fun)** | Personal, thinking-out-loud, honest about uncertainty. Most "you" channel. |
| **Sharing Session** | More structured, still warm. You're the guide, not the expert. Teach by showing. |
| **LinkedIn** | Same person, slightly edited. Still specific. Never vague inspiration content. |

### Example — Blog intro

❌ *"In this article, I will discuss the importance of AI tools in analyst relations and how professionals can leverage them for maximum efficiency."*

✅ *"我最近在用 Claude Code 给团队搭了一个问卷回答工具。搭的过程中我意识到，原来我花最多时间的事情根本不是思考，而是格式化。"*

---

## Section 6 — Context-Specific Output Rules

### Blog post card (luxlu.fun)
- Tag eyebrow: Fira Code, teal, ALL CAPS, small
- Title: DM Serif Display, ~20px, mixed Chinese/English fine
- Meta line: Fira Code, muted gray (`--t3`)
- Excerpt: Noto Sans SC, weight 300
- CTA: `Read more →` in teal Fira Code

### Slide deck
- Background: `#1A1A1E` (darker than base)
- Eyebrow: Fira Code, small, teal, uppercase
- Title: DM Serif Display — italic teal for the key phrase
- Bullet dots: lemon yellow `#E8D44D` (4px circle), not standard bullets

### LinkedIn post
- Lead with a specific, concrete hook — no "excited to share"
- No preamble
- Tags in Fira Code style as plain text: `#AnalystRelations #AITools #BuildingInPublic`

### HTML artifact / interactive page
- Full CSS variable system from Section 2 + Section 3
- Dark base `#2A2A2E`, raised surfaces `#323237`
- Teal as primary interactive color (hover, focus, links)
- Use scroll-reveal animations from Section 4
- Sticky nav with `backdrop-filter: blur(16px)` on `rgba(42,42,46,0.92)`

### Email / written document
- Subject or title: short and specific, no preamble
- Opening line: observation or question, not "I hope this finds you well"
- Signature closes with `Lux.` (the period matters)

### Personal bio
- Third person is fine for "about" sections; first person for blog/LinkedIn
- Lead with role + what she's building, not just title
- Include: AR professional, AI builder, SCUPI '26, curious human

---

## Section 7 — Quick Reference Cheatsheet

```
COLORS
Background:   #2A2A2E  (base)   /  #323237  (raised)
Teal:         #2ECFBE  ← signature, always present
Lemon:        #E8D44D  ← precise / technical
Violet:       #9B7FE8  ← grounded / personal
Rose:         #F06292  ← action / energy
Text:         #F0EFE8  (primary)  /  #9E9D99  (secondary)

FONTS
Display:      DM Serif Display — headings, hero, italic emphasis
Body:         Noto Sans SC — all running text, Chinese + English
Mono:         Fira Code — labels, dates, URLs, metadata

BRAND
Logotype:     Lux[italic teal .]
Tagline:      "Action Generates Information"
Domain:       luxlu.fun
```

---

*Reference the HTML file `lux_brand_guideline.html` in this same folder to see all components rendered. When in doubt: dark background, teal present, one accent, DM Serif for headings, Noto for body, Fira Code for details.*
