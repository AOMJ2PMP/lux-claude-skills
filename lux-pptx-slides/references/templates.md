# Lux. Slide Templates — pptxgenjs Code Reference

Complete, copy-paste-ready pptxgenjs code for each template in the Lux brand system.
All coordinates are in inches (pptxgenjs default). Slide size: 10" × 5.625" (16:9).

---

## Setup (always at top of your script)

```js
const pptxgen = require("pptxgenjs");
const prs = new pptxgen();

prs.layout = "LAYOUT_WIDE"; // 10" x 5.625"

// Brand colors
const C = {
  bg:       "1A1A1E",
  surface:  "2A2A2E",
  raised:   "323237",
  t1:       "F0EFE8",
  t2:       "9E9D99",
  t3:       "6A6966",
  teal:     "2ECFBE",
  lemon:    "E8D44D",
  violet:   "9B7FE8",
  rose:     "F06292",
  border:   "FFFFFF",  // use with transparency
};

// Fonts
const F = {
  display: "DM Serif Display",
  body:    "Noto Sans SC",
  mono:    "Fira Code",
};

// Slide dimensions
const W = 10;    // width inches
const H = 5.625; // height inches

// Helper: set slide background
function setBg(slide) {
  slide.background = { color: C.bg };
}

// Helper: add footer with Lux. logotype
function addFooter(slide, leftText = "") {
  // Left: section name or topic
  if (leftText) {
    slide.addText(leftText, {
      x: 0.4, y: H - 0.35, w: 5, h: 0.25,
      fontFace: F.mono, fontSize: 9,
      color: C.t3, align: "left",
    });
  }
  // Right: Lux. logotype (two-run text)
  slide.addText([
    { text: "Lux", options: { color: C.t1, fontFace: F.display, fontSize: 10 } },
    { text: ".", options: { color: C.teal, fontFace: F.display, fontSize: 10, italic: true } },
  ], {
    x: W - 1.0, y: H - 0.35, w: 0.6, h: 0.25,
    align: "right",
  });
}

// Helper: add teal eyebrow label
function addEyebrow(slide, text, x = 0.5, y = 0.38) {
  slide.addText(text.toUpperCase(), {
    x, y, w: 8, h: 0.2,
    fontFace: F.mono, fontSize: 11,
    color: C.teal, align: "left",
    charSpacing: 1.5,
  });
}

// Helper: add teal accent line
function addAccentLine(slide, x = 0.5, y = 1.0, w = 0.5) {
  slide.addShape(prs.ShapeType.rect, {
    x, y, w, h: 0.03,
    fill: { color: C.teal },
    line: { type: "none" },
  });
}
```

---

## Template A — Title / Cover

```js
function slideTitle(prs, { title, keyPhrase, subtitle = "", eyebrow = "", date = "" }) {
  // keyPhrase: the words in title that should be italic teal
  // title is split: before keyPhrase + keyPhrase + after keyPhrase

  const slide = prs.addSlide();
  setBg(slide);

  // Eyebrow
  if (eyebrow) addEyebrow(slide, eyebrow, 0.6, 1.2);

  // Hero title — split into runs so key phrase is italic teal
  const [before, after] = title.split(keyPhrase);
  slide.addText([
    { text: before || "", options: { color: C.t1, italic: false } },
    { text: keyPhrase, options: { color: C.teal, italic: true } },
    { text: after || "", options: { color: C.t1, italic: false } },
  ], {
    x: 0.6, y: eyebrow ? 1.55 : 1.4, w: 8.8, h: 2.2,
    fontFace: F.display, fontSize: 48,
    lineSpacingMultiple: 1.1,
  });

  // Subtitle
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.6, y: 3.5, w: 7, h: 0.5,
      fontFace: F.body, fontSize: 16,
      color: C.t2, bold: false,
    });
  }

  // Date bottom left
  if (date) {
    slide.addText(date, {
      x: 0.6, y: H - 0.38, w: 4, h: 0.25,
      fontFace: F.mono, fontSize: 9,
      color: C.t3, align: "left",
    });
  }

  // Lux. logotype bottom right
  slide.addText([
    { text: "Lux", options: { color: C.t1, fontFace: F.display, fontSize: 11 } },
    { text: ".", options: { color: C.teal, fontFace: F.display, fontSize: 11, italic: true } },
  ], {
    x: W - 1.1, y: H - 0.38, w: 0.7, h: 0.25,
    align: "right",
  });

  return slide;
}

// Usage:
// slideTitle(prs, {
//   title: "How I Use AI Tools in Analyst Relations",
//   keyPhrase: "AI Tools",
//   subtitle: "Sharing Session · Tencent Cloud AR Team · March 2026",
//   eyebrow: "Internal · March 2026",
//   date: "2026.03",
// });
```

---

## Template B — One Big Idea

```js
function slideBigIdea(prs, { quote, keyPhrase = "", support = "", eyebrow = "", footerText = "" }) {
  const slide = prs.addSlide();
  setBg(slide);

  if (eyebrow) addEyebrow(slide, eyebrow, 0.6, 0.5);

  // Teal accent line above quote
  addAccentLine(slide, 0.6, eyebrow ? 0.85 : 0.7, 0.55);

  // Quote text
  const y = eyebrow ? 1.0 : 0.85;
  // Split quote at keyPhrase boundary into two separate text boxes
  // to avoid mid-sentence orphan line breaks from mixed-style runs.
  if (keyPhrase && quote.includes(keyPhrase)) {
    const [before, after] = quote.split(keyPhrase);
    // Line 1: everything before the key phrase
    if (before.trim()) {
      slide.addText(before.trimEnd(), {
        x: 0.6, y, w: 8.8, h: 1.0,
        fontFace: F.display, fontSize: 36,
        color: C.t1, lineSpacingMultiple: 1.1,
      });
    }
    // Line 2: key phrase (teal italic) + remainder
    slide.addText([
      { text: keyPhrase, options: { color: C.teal, italic: true } },
      { text: after || "", options: { color: C.t1, italic: false } },
    ], {
      x: 0.6, y: y + 0.95, w: 8.8, h: 1.1,
      fontFace: F.display, fontSize: 36,
      lineSpacingMultiple: 1.1,
    });
  } else {
    slide.addText(quote, {
      x: 0.6, y, w: 8.8, h: 2.2,
      fontFace: F.display, fontSize: 36,
      color: C.t1, lineSpacingMultiple: 1.25,
    });
  }

  // Supporting sentence
  if (support) {
    slide.addText(support, {
      x: 0.6, y: 3.85, w: 8.0, h: 0.5,
      fontFace: F.body, fontSize: 15,
      color: C.t2,
    });
  }

  addFooter(slide, footerText);
  return slide;
}

// Usage:
// slideBigIdea(prs, {
//   quote: "Action doesn't just solve problems. It generates the information you need to solve them.",
//   keyPhrase: "generates the information",
//   support: "Most of what I know about AR came from doing it badly the first time.",
//   eyebrow: "Core Belief",
//   footerText: "AI in AR · Lux",
// });
```

---

## Template C — Bullet Points

```js
function slideBullets(prs, { title, keyPhrase = "", bullets, eyebrow = "", callout = null, footerText = "", accentColor = null }) {
  // bullets: array of strings, max 5
  // callout: string — shown in a highlighted box as the "most important" point
  // accentColor: override dot color (default: teal)

  const slide = prs.addSlide();
  setBg(slide);
  const dotColor = accentColor || C.teal;

  if (eyebrow) addEyebrow(slide, eyebrow, 0.5, 0.35);

  // Title
  const titleRuns = keyPhrase && title.includes(keyPhrase)
    ? [
        { text: title.split(keyPhrase)[0], options: { color: C.t1 } },
        { text: keyPhrase, options: { color: C.teal, italic: true } },
        { text: title.split(keyPhrase)[1] || "", options: { color: C.t1 } },
      ]
    : title;

  slide.addText(titleRuns, {
    x: 0.5, y: eyebrow ? 0.65 : 0.45, w: 9.0, h: 0.7,
    fontFace: F.display, fontSize: 36,
    color: C.t1,
  });

  // Bullets
  const bulletStartY = eyebrow ? 1.5 : 1.3;
  const bulletSpacing = callout ? 0.52 : 0.58;

  bullets.slice(0, 5).forEach((text, i) => {
    const y = bulletStartY + i * bulletSpacing;
    // Dot
    slide.addShape(prs.ShapeType.ellipse, {
      x: 0.5, y: y + 0.12, w: 0.1, h: 0.1,
      fill: { color: dotColor },
      line: { type: "none" },
    });
    // Text
    slide.addText(text, {
      x: 0.75, y, w: 8.8, h: 0.45,
      fontFace: F.body, fontSize: 16,
      color: C.t1, lineSpacingMultiple: 1.3,
    });
  });

  // Callout box
  if (callout) {
    const calloutY = bulletStartY + bullets.length * bulletSpacing + 0.1;
    slide.addShape(prs.ShapeType.rect, {
      x: 0.5, y: calloutY, w: 9.0, h: 0.7,
      fill: { color: C.raised },
      line: { pt: 0, type: "none" },
    });
    // Left teal border
    slide.addShape(prs.ShapeType.rect, {
      x: 0.5, y: calloutY, w: 0.05, h: 0.7,
      fill: { color: C.teal },
      line: { type: "none" },
    });
    slide.addText(callout, {
      x: 0.7, y: calloutY + 0.05, w: 8.6, h: 0.6,
      fontFace: F.body, fontSize: 14,
      color: C.t2,
    });
  }

  addFooter(slide, footerText);
  return slide;
}

// Usage:
// slideBullets(prs, {
//   title: "Three Things I Got Wrong",
//   keyPhrase: "Wrong",
//   bullets: [
//     "Assumed the analyst already understood our product positioning",
//     "Sent a 40-page doc when a 5-slide summary would have done it",
//     "Waited for the perfect answer instead of shipping a good one",
//   ],
//   callout: "The pattern: I optimized for thoroughness when I should have optimized for clarity.",
//   eyebrow: "Lessons Learned",
//   footerText: "AI in AR",
// });
```

---

## Template D — Two Column

```js
function slideTwoColumn(prs, { title, left, right, eyebrow = "", footerText = "" }) {
  // left / right: { label: string, items: string[] }

  const slide = prs.addSlide();
  setBg(slide);

  if (eyebrow) addEyebrow(slide, eyebrow, 0.5, 0.32);

  slide.addText(title, {
    x: 0.5, y: eyebrow ? 0.6 : 0.42, w: 9.0, h: 0.65,
    fontFace: F.display, fontSize: 34,
    color: C.t1,
  });

  const colY = eyebrow ? 1.38 : 1.2;
  const colH = H - colY - 0.5;

  [[left, 0.5], [right, 5.2]].forEach(([col, x]) => {
    // Column background
    slide.addShape(prs.ShapeType.rect, {
      x, y: colY, w: 4.5, h: colH,
      fill: { color: C.surface },
      line: { color: "FFFFFF", transparency: 92, pt: 1 },
      rectRadius: 0.12,
    });

    // Column label
    slide.addText(col.label.toUpperCase(), {
      x: x + 0.22, y: colY + 0.18, w: 4.1, h: 0.25,
      fontFace: F.mono, fontSize: 11,
      color: C.teal, charSpacing: 1.2,
    });

    // Items
    col.items.forEach((item, i) => {
      slide.addText(item, {
        x: x + 0.22, y: colY + 0.55 + i * 0.58, w: 4.0, h: 0.52,
        fontFace: F.body, fontSize: 15,
        color: C.t1, lineSpacingMultiple: 1.3,
      });
    });
  });

  addFooter(slide, footerText);
  return slide;
}

// Usage:
// slideTwoColumn(prs, {
//   title: "Before vs. After Using AI",
//   left: {
//     label: "Before",
//     items: ["3 hours per questionnaire", "Manual copy-paste from docs", "Generic answers, no customization"],
//   },
//   right: {
//     label: "After",
//     items: ["~20 minutes per questionnaire", "Structured prompt → review → send", "Tailored to each analyst's framework"],
//   },
//   eyebrow: "Impact",
//   footerText: "AI in AR",
// });
```

---

## Template E — Big Stat

```js
function slideBigStat(prs, { stat, statLabel, context = "", supporting = [], eyebrow = "", footerText = "", accentColor = null }) {
  // supporting: array of { num, label } for smaller secondary stats

  const slide = prs.addSlide();
  setBg(slide);
  const numColor = accentColor || C.teal;

  if (eyebrow) addEyebrow(slide, eyebrow, 0.6, 0.4);

  // Big number
  slide.addText(stat, {
    x: 0.6, y: eyebrow ? 0.75 : 0.6, w: 6, h: 2.2,
    fontFace: F.display, fontSize: 80,
    color: numColor,
    lineSpacingMultiple: 1.0,
  });

  // Stat label
  slide.addText(statLabel, {
    x: 0.6, y: eyebrow ? 2.85 : 2.7, w: 6, h: 0.45,
    fontFace: F.body, fontSize: 16,
    color: C.t1, bold: true,
  });

  // Context sentence
  if (context) {
    slide.addText(context, {
      x: 0.6, y: eyebrow ? 3.35 : 3.2, w: 8.0, h: 0.45,
      fontFace: F.body, fontSize: 14,
      color: C.t2,
    });
  }

  // Supporting mini-stats (right side)
  if (supporting.length > 0) {
    supporting.slice(0, 3).forEach(({ num, label }, i) => {
      const sy = 1.1 + i * 1.2;
      slide.addText(num, {
        x: 7.2, y: sy, w: 2.4, h: 0.9,
        fontFace: F.display, fontSize: 38,
        color: C.t1, align: "right",
      });
      slide.addText(label, {
        x: 7.2, y: sy + 0.85, w: 2.4, h: 0.28,
        fontFace: F.body, fontSize: 12,
        color: C.t2, align: "right",
      });
    });
  }

  addFooter(slide, footerText);
  return slide;
}

// Usage:
// slideBigStat(prs, {
//   stat: "3 min",
//   statLabel: "Average time to complete a Gartner questionnaire",
//   context: "Down from ~3 hours before we built the AI-assisted workflow.",
//   supporting: [
//     { num: "47", label: "questions answered" },
//     { num: "6×", label: "faster than before" },
//   ],
//   eyebrow: "Result",
//   footerText: "AI in AR",
// });
```

---

## Template F — Process / Timeline

```js
function slideProcess(prs, { title, steps, eyebrow = "", footerText = "", highlightIndex = -1, accentColor = null }) {
  // steps: array of { num, title, body } — max 5
  // highlightIndex: which step to highlight (-1 = none)

  const slide = prs.addSlide();
  setBg(slide);
  const accent = accentColor || C.teal;

  if (eyebrow) addEyebrow(slide, eyebrow, 0.5, 0.32);

  slide.addText(title, {
    x: 0.5, y: eyebrow ? 0.6 : 0.42, w: 9.0, h: 0.65,
    fontFace: F.display, fontSize: 34,
    color: C.t1,
  });

  const n = Math.min(steps.length, 5);
  const stepW = (W - 1.0) / n;
  const stepY = eyebrow ? 1.5 : 1.35;
  const stepH = H - stepY - 0.5;

  steps.slice(0, n).forEach((step, i) => {
    const x = 0.5 + i * stepW;
    const isHighlight = i === highlightIndex;

    // Step background
    slide.addShape(prs.ShapeType.rect, {
      x: x + 0.05, y: stepY, w: stepW - 0.12, h: stepH,
      fill: { color: isHighlight ? C.raised : C.surface },
      line: isHighlight
        ? { color: accent, pt: 1.5 }
        : { color: "FFFFFF", transparency: 93, pt: 1 },
      rectRadius: 0.1,
    });

    // Connector line between steps
    if (i < n - 1) {
      slide.addShape(prs.ShapeType.rect, {
        x: x + stepW - 0.07, y: stepY + stepH / 2 - 0.01,
        w: 0.12, h: 0.02,
        fill: { color: "3C3C42" },
        line: { type: "none" },
      });
    }

    // Step number
    slide.addText(String(step.num || i + 1).padStart(2, "0"), {
      x: x + 0.2, y: stepY + 0.2, w: stepW - 0.4, h: 0.3,
      fontFace: F.mono, fontSize: 11,
      color: isHighlight ? accent : C.teal,
    });

    // Step title
    slide.addText(step.title, {
      x: x + 0.2, y: stepY + 0.58, w: stepW - 0.4, h: 0.55,
      fontFace: F.body, fontSize: 14,
      color: C.t1, bold: true,
      lineSpacingMultiple: 1.2,
    });

    // Step body
    if (step.body) {
      slide.addText(step.body, {
        x: x + 0.2, y: stepY + 1.2, w: stepW - 0.4, h: stepH - 1.4,
        fontFace: F.body, fontSize: 13,
        color: C.t2, lineSpacingMultiple: 1.35,
      });
    }
  });

  addFooter(slide, footerText);
  return slide;
}

// Usage:
// slideProcess(prs, {
//   title: "How the Workflow Works",
//   eyebrow: "Process",
//   highlightIndex: 2,
//   steps: [
//     { title: "Receive Brief", body: "Analyst questionnaire arrives via email or portal" },
//     { title: "Extract Questions", body: "Parse into structured format with Claude" },
//     { title: "Generate Answers", body: "AI drafts answers using product context" },
//     { title: "Review & Edit", body: "Human review — 10-15 min spot-check" },
//     { title: "Submit", body: "Final answers sent to analyst on time" },
//   ],
//   footerText: "AI in AR",
// });
```

---

## Template G — Code / Technical

```js
function slideCode(prs, { title, codeLines, language = "", explanation = "", eyebrow = "", footerText = "" }) {
  // codeLines: array of strings (each is a line of code)

  const slide = prs.addSlide();
  setBg(slide);

  if (eyebrow) addEyebrow(slide, eyebrow, 0.5, 0.32);

  slide.addText(title, {
    x: 0.5, y: eyebrow ? 0.6 : 0.42, w: 9.0, h: 0.65,
    fontFace: F.display, fontSize: 32,
    color: C.t1,
  });

  // Code block background
  const codeY = eyebrow ? 1.4 : 1.25;
  const codeH = explanation ? 2.6 : 3.4;
  slide.addShape(prs.ShapeType.rect, {
    x: 0.5, y: codeY, w: 9.0, h: codeH,
    fill: { color: "111113" },
    line: { color: "FFFFFF", transparency: 94, pt: 1 },
    rectRadius: 0.1,
  });

  // Language label
  if (language) {
    slide.addText(language.toUpperCase(), {
      x: 0.7, y: codeY + 0.12, w: 3, h: 0.22,
      fontFace: F.mono, fontSize: 9,
      color: C.t3, charSpacing: 1.5,
    });
  }

  // Code text
  slide.addText(codeLines.join("\n"), {
    x: 0.7, y: codeY + (language ? 0.38 : 0.2), w: 8.6, h: codeH - 0.55,
    fontFace: F.mono, fontSize: 13,
    color: C.t1, lineSpacingMultiple: 1.5,
    valign: "top",
  });

  // Explanation
  if (explanation) {
    slide.addText(explanation, {
      x: 0.5, y: codeY + codeH + 0.18, w: 9.0, h: 0.55,
      fontFace: F.body, fontSize: 15,
      color: C.t2, lineSpacingMultiple: 1.3,
    });
  }

  addFooter(slide, footerText);
  return slide;
}
```

---

## Template H — Closing / Summary

```js
function slideClosing(prs, { takeaway, keyPhrase = "", actions = [], date = "", footerText = "" }) {
  const slide = prs.addSlide();
  setBg(slide);

  addEyebrow(slide, "Key Takeaway", 0.6, 0.55);
  addAccentLine(slide, 0.6, 0.92, 0.55);

  // Main takeaway
  // Use a single mixed-run text block; fontSize 30 gives enough room
  // to avoid the quote overflowing into the action items below.
  slide.addText([
    { text: takeaway.split(keyPhrase)[0] || "", options: { color: C.t1, italic: false } },
    { text: keyPhrase || "", options: { color: C.teal, italic: true } },
    { text: (keyPhrase ? takeaway.split(keyPhrase)[1] : "") || "", options: { color: C.t1, italic: false } },
  ], {
    x: 0.6, y: 0.78, w: 8.8, h: 2.35,
    fontFace: F.display, fontSize: 30,
    lineSpacingMultiple: 1.3, valign: "top",
  });

  // Action items — start at y=3.2 so they never overlap the quote
  if (actions.length > 0) {
    actions.slice(0, 3).forEach((action, i) => {
      const ay = 3.2 + i * 0.5;
      slide.addShape(prs.ShapeType.ellipse, {
        x: 0.6, y: ay + 0.1, w: 0.1, h: 0.1,
        fill: { color: C.teal }, line: { type: "none" },
      });
      slide.addText(action, {
        x: 0.85, y: ay, w: 8.5, h: 0.42,
        fontFace: F.body, fontSize: 14, color: C.t2,
        lineSpacingMultiple: 1.2,
      });
    });
  }

  // Large Lux. logotype centered
  slide.addText([
    { text: "Lux", options: { color: C.t1, fontFace: F.display, fontSize: 18 } },
    { text: ".", options: { color: C.teal, fontFace: F.display, fontSize: 18, italic: true } },
  ], {
    x: W / 2 - 0.4, y: H - 0.52, w: 0.85, h: 0.35,
    align: "center",
  });

  if (date) {
    slide.addText(date, {
      x: 0.6, y: H - 0.42, w: 3, h: 0.25,
      fontFace: F.mono, fontSize: 9,
      color: C.t3, align: "left",
    });
  }

  // luxlu.fun
  slide.addText("luxlu.fun", {
    x: W - 1.6, y: H - 0.42, w: 1.2, h: 0.25,
    fontFace: F.mono, fontSize: 9,
    color: C.t3, align: "right",
  });

  return slide;
}

// Usage:
// slideClosing(prs, {
//   takeaway: "The best way to learn how AI fits into your workflow is to start somewhere imperfect and see what breaks.",
//   keyPhrase: "start somewhere imperfect",
//   actions: [
//     "Try automating one repetitive task this week",
//     "Share what you built — even if it's rough",
//   ],
//   date: "March 2026",
// });
```

---

## Full Deck Example

```js
const pptxgen = require("pptxgenjs");
const prs = new pptxgen();
prs.layout = "LAYOUT_WIDE";
// ... (paste setup block here) ...

// Slide 1: Cover
slideTitle(prs, {
  title: "How I Use AI Tools in Analyst Relations",
  keyPhrase: "AI Tools",
  subtitle: "Sharing Session · Tencent Cloud AR Team · March 2026",
  eyebrow: "Internal · March 2026",
  date: "2026.03",
});

// Slide 2: Core belief
slideBigIdea(prs, {
  quote: "Action doesn't just solve problems. It generates the information you need.",
  keyPhrase: "generates the information",
  eyebrow: "Starting Point",
  footerText: "AI in AR",
});

// Slide 3: The problem
slideBullets(prs, {
  title: "Where Time Goes in AR",
  bullets: [
    "Reading 40-page analyst frameworks before every inquiry",
    "Formatting answers across different questionnaire styles",
    "Re-researching context you already had last quarter",
  ],
  callout: "Most of this is information retrieval — not actual thinking.",
  eyebrow: "The Problem",
  footerText: "AI in AR",
});

// Slide 4: Result stat
slideBigStat(prs, {
  stat: "3 min",
  statLabel: "Average time to complete a questionnaire",
  context: "Down from ~3 hours. The AI drafts; I review and edit.",
  eyebrow: "Result",
  footerText: "AI in AR",
});

// Slide 5: Process
slideProcess(prs, {
  title: "The Workflow",
  eyebrow: "How It Works",
  highlightIndex: 2,
  steps: [
    { title: "Receive Brief", body: "Questionnaire arrives" },
    { title: "Extract", body: "Parse into structured Q&A" },
    { title: "Draft", body: "AI generates first answers" },
    { title: "Review", body: "10-min human check" },
    { title: "Submit", body: "Done and on time" },
  ],
  footerText: "AI in AR",
});

// Slide 6: Closing
slideClosing(prs, {
  takeaway: "The best way to figure out where AI fits is to try it somewhere imperfect, see what breaks, and adjust.",
  keyPhrase: "try it somewhere imperfect",
  actions: [
    "Pick one repetitive AR task and test a simple prompt this week",
    "Share what you learn — rough is fine",
  ],
  date: "March 2026",
});

prs.writeFile({ fileName: "output.pptx" });
console.log("Done: output.pptx");
```
