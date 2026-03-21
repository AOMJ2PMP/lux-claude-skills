---
name: lux-blog-post
description: Convert a piece of writing into a Markdown file ready to publish on Lux's personal blog. Use when the user wants to publish a new blog post, convert writing to blog format, or add a post to the lux-blog Next.js project.
---

You are converting the user's writing into a `.md` file that can be dropped into `/content/posts/` of the `blog/` Next.js project at `/Users/luxlu/Desktop/coding projects/blog/`.

The blog uses a **custom Markdown format** with specific syntax rules. Follow this guide exactly.

---

## Step 1 — Gather what you need

Ask the user for anything missing:

| Field | Required? | Notes |
|---|---|---|
| `slug` | Yes | URL-safe, hyphenated, e.g. `my-post-title` |
| `title` | Yes | Display title |
| `updatedDate` | Yes | `YYYY-MM-DD` format |
| `readingTime` | Yes | e.g. `4 min read` |
| `relatedPosts` | Optional | Up to 2 entries (href, title, description, readingTime) |
| `upNext` | Optional | 1 entry (href, title, description, readingTime) |
| Chinese translation | Optional | Separate `title`, `readingTime`, and body |

If the user gives you a plain piece of writing without metadata, make reasonable guesses for slug (from title), estimate reading time (~200 words/min), use today's date, and ask only for things you truly cannot infer.

---

## Step 2 — File structure

```
/content/posts/<slug>.md
```

### Frontmatter (top of file)

```markdown
---
slug: example-post
title: Example Post Title
updatedDate: 2026-03-11
readingTime: 4 min read
relatedPosts:
  - href: /other-post
    title: Other Post Title
    description: One sentence description.
    readingTime: 3 min read
upNext:
  href: /another-post
  title: Another Post Title
  description: One sentence description.
  readingTime: 5 min read
---
```

If `relatedPosts` or `upNext` are not provided, omit those keys entirely.

---

## Step 3 — Body syntax reference

### Paragraphs
Plain paragraphs — no special syntax needed.

### Horizontal rule / section break
```markdown
---
```
Renders as a decorative `...` separator (styled in CSS, not a plain line).

### Headings
```markdown
## Section Title       ← h2, large serif font
### Subsection Title   ← h3
```
**Do not use `#` (h1)** — the post title is already an h1 in the layout.

### Bold and italic
```markdown
**bold text**
*italic text*
```

### Blockquote (styled pull-quote)
```markdown
> First line of quote
> Second line of quote
```
Renders as a centred pull-quote with horizontal lines above and below, in a sans-serif muted style. This is the `kg-blockquote-alt` class.

### Sidenote (margin annotation)
```markdown
:::sidenote
The note text goes here. Keep it short — one or two sentences.
:::
```
Renders as a floating note in the left margin with a `*` prefix. On mobile it collapses inline.

### Links
```markdown
[link text](https://external.com)      ← external: auto-gets ↗ arrow + opens new tab
[link text](/internal-path)            ← internal: no arrow
```

### Images
```markdown
![Alt description](/images/filename.jpg)
```
Place image files in `/public/images/`. The path in the Markdown is relative to `public/`.

---

## Step 4 — Chinese translation (optional)

If the post has a Chinese version, append it after the English body using `---zh---` as the separator:

```markdown
[English body ends here]

---zh---
title: 中文标题
readingTime: 4 分钟

中文正文从这里开始。

---

## 中文二级标题

更多内容...

:::sidenote
中文侧边注释
:::
```

Rules:
- The `title:` and `readingTime:` lines must come **immediately** after `---zh---`, one per line, no blank line between them
- The first blank line after those key-value lines marks the start of the body
- All the same Markdown syntax applies (blockquotes, sidenotes, headings, etc.)
- Do NOT use `---` YAML fence markers around the Chinese metadata — they will break parsing

---

## Step 5 — Write the file

Once you have all the information, write the file directly to:
```
/Users/luxlu/Desktop/coding projects/blog/content/posts/<slug>.md
```

After writing, confirm the file path and tell the user:
- The URL where the post will be live: `/<slug>`
- Whether a Chinese translation was included
- Any fields you guessed or left out
