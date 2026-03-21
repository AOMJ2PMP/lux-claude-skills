---
name: firehose-api
description: >
  Firehose is a real-time web monitoring API. You create rules (Lucene queries) and receive matching web pages via a Server-Sent Events stream. Use this skill whenever the user wants to: monitor the web for mentions of a brand, keyword, or topic in real time; create/manage/delete Firehose taps or rules; write code to connect to the Firehose stream; build a monitoring or alerting system using Firehose; craft or debug a Lucene query for web content matching; understand the Firehose data model (documents, diffs, page types, categories). Trigger on phrases like "monitor mentions of", "set up a web alert", "create a firehose rule", "stream web content", "watch for changes on the web", or any reference to the Firehose API.
---

# Firehose API

Firehose monitors the web in real-time. You create **rules** (Lucene queries), and every crawled page that matches gets delivered via a **Server-Sent Events (SSE) stream**.

**Base URL:** `https://api.firehose.com`

## Key Concepts

- **Tap**: A monitoring channel with its own token and set of rules. One tap = one SSE stream. Max 25 rules per organization.
- **Rule**: A Lucene query that describes what pages to match. When a crawled page matches, it's pushed to the stream.
- **Stream**: A long-lived SSE connection that delivers matching pages in real time, including the full page content as Markdown and a content diff.

## Authentication

Two key types — both use `Authorization: Bearer <token>`:

| Key | Prefix | Used for |
|-----|--------|----------|
| Management Key | `fhm_` | Create/list/update/revoke taps |
| Tap Token | `fh_` | Create/manage rules, connect to stream |

The management key is shown once on creation. Tap tokens are always retrievable via `GET /v1/taps`.

---

## API Reference

### Tap Management (requires `fhm_` key)

```
GET    /v1/taps          # List all taps (includes full tap tokens)
POST   /v1/taps          # Create tap: { "name": "My Tap" }
GET    /v1/taps/:id      # Get tap
PUT    /v1/taps/:id      # Rename tap: { "name": "New Name" }
DELETE /v1/taps/:id      # Revoke tap (204 no content)
```

### Rule Management (requires `fh_` tap token)

```
GET    /v1/rules         # List rules
POST   /v1/rules         # Create rule (see below)
GET    /v1/rules/:id     # Get rule
PUT    /v1/rules/:id     # Update rule (partial updates OK)
DELETE /v1/rules/:id     # Delete rule (204 no content)
```

**Create/update rule fields:**
```json
{
  "value": "ahrefs OR semrush",   // required: Lucene query
  "tag": "seo-tools",             // optional: label (max 255 chars)
  "nsfw": false,                  // optional: include adult content (default false)
  "quality": true                 // optional: filter out pagination/tag/category URLs (default true)
}
```

### Stream (requires `fh_` tap token)

```
GET /v1/stream?timeout=60&since=30m&limit=100
```

Opens an SSE connection. Only delivers events matching this tap's rules.

**Query params:**
- `timeout` (int, default 300): connection duration in seconds (max 300)
- `since` (string): replay buffered events, e.g. `5m`, `1h`, `24h` (max 24h buffer)
- `offset` (int): start from an exact Kafka offset
- `limit` (int, 1–10000): close stream after N matching events

**Reconnect:** Use `Last-Event-ID` header (format: `{partition}-{offset}`) to resume after disconnect. Browser `EventSource` sends this automatically.

**Parameter precedence:** `Last-Event-ID` > `offset` > `since` > live tail

#### Event types

```
event: connected   → connection opened, data: []
event: update      → a page matched a rule (see payload below)
event: error       → something went wrong, data: {"message": "..."}
event: end         → stream closed (timeout/limit), reconnect to continue
```

#### Update payload

```json
{
  "query_id": "1",
  "matched_at": "2026-02-13T08:06:32Z",
  "tap_id": "1",
  "document": {
    "url": "https://example.com/page",
    "title": "Example Page",
    "publish_time": "2026-02-13T08:06:32",
    "diff": {
      "chunks": [
        {"typ": "ins", "text": "New content added..."},
        {"typ": "del", "text": "Old content removed..."}
      ]
    },
    "page_category": ["/News"],
    "page_types": ["/Article"],
    "language": "en",
    "markdown": "Full page content in markdown..."
  }
}
```

Null fields and empty arrays are **omitted** from the response (not set to null).

---

## Lucene Query Syntax

Rules use **Lucene ClassicQueryParser** syntax. The default field is `added` (new content in a page's diff).

### Fields

| Field | Type | Case | Description |
|-------|------|------|-------------|
| `added` | text | insensitive | **Default.** Text from inserted diff chunks |
| `removed` | text | insensitive | Text from deleted diff chunks |
| `added_anchor` | text | insensitive | Anchor text from inserted links |
| `removed_anchor` | text | insensitive | Anchor text from deleted links |
| `title` | text | insensitive | Page title |
| `url` | keyword | **sensitive** | Full URL (exact token) |
| `domain` | keyword | **sensitive** | Domain (e.g. `example.com`) |
| `publish_time` | keyword | **sensitive** | ISO-8601 datetime (e.g. `2025-06-15T15:06:40`) |
| `page_category` | keyword | **sensitive** | ML category (e.g. `/News`) |
| `page_type` | keyword | **sensitive** | ML type (e.g. `/Article/How_to`) |
| `language` | keyword | **sensitive** | ISO 639-1 code (e.g. `en`, `zh-cn`) |
| `recent` | filter | — | Recency filter: `1h`, `7d`, `3mo` |

### Common query patterns

```
# Brand mentions (default = added field)
tencent cloud

# Exact phrase in title
title:"breaking news"

# Boolean combinations
title:tesla AND language:"en"
title:ahrefs AND added:seo AND page_type:"/Article"
domain:"techcrunch.com" AND title:IPO

# Recency filter (combine with anything)
title:tesla AND recent:24h
"kubernetes" AND page_category:"/Computers_and_Electronics" AND recent:7d

# Exclude junk URLs (pagination, tags, categories)
title:tesla AND NOT url:/.*\/page\/[0-9]+.*/ AND NOT url:*\/tag\/*

# Domain monitoring with quality filter off (see rule `quality: false`)
domain:"gartner.com"
```

### URL / domain query tips

**Text fields** (`added`, `title`, etc.): case-insensitive, tokenized on whitespace/punctuation.

**Keyword fields** (`url`, `domain`, `page_category`, `language`): exact match, case-sensitive.

For URL pattern matching, use wildcards or regex:
```
url:*\/category\/*             # wildcard: URLs containing /category/
url:/.*\/page\/[0-9]+.*/       # regex: pagination URLs
url:"https://example.com/page" # exact match
domain:"techcrunch.com"        # exact domain
```

**Escaping in wildcards:** Forward slashes need `\/`. In JSON: write `\\/` to produce `\/` in the query.

**Date ranges** (colons must be escaped with `\\`):
```
publish_time:[2025-01-01T00\\:00\\:00 TO 2025-12-31T23\\:59\\:59]
```

---

## Quick-start curl examples

```bash
# List your taps
curl -H "Authorization: Bearer $FIREHOSE_MANAGEMENT_KEY" \
  https://api.firehose.com/v1/taps

# Create a rule
curl -X POST https://api.firehose.com/v1/rules \
  -H "Authorization: Bearer $FIREHOSE_TAP_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"value": "\"tencent cloud\" AND recent:24h", "tag": "brand-mentions"}'

# Stream (live tail, 60s timeout)
curl -H "Authorization: Bearer $FIREHOSE_TAP_TOKEN" \
  "https://api.firehose.com/v1/stream?timeout=60"

# Replay last 30 minutes
curl -H "Authorization: Bearer $FIREHOSE_TAP_TOKEN" \
  "https://api.firehose.com/v1/stream?since=30m&limit=100"
```

## JavaScript / EventSource example

```javascript
const es = new EventSource(
  'https://api.firehose.com/v1/stream?timeout=300',
  { headers: { Authorization: `Bearer ${TAP_TOKEN}` } }
);

es.addEventListener('update', (e) => {
  const { document: doc, matched_at } = JSON.parse(e.data);
  console.log(`[${matched_at}] ${doc.title} — ${doc.url}`);
});

es.addEventListener('end', () => es.close());
es.onerror = (err) => console.error('Stream error', err);
```

---

## Reference

For the full list of `page_type` values (110+) and `page_category` values (700+ subcategories), read `references/taxonomy.md`.

For error codes and edge cases, read `references/errors.md`.
