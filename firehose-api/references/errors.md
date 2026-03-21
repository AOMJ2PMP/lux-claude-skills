# Firehose — Errors & Rate Limits

## Rate Limits

| Endpoint     | Limit                      |
|--------------|---------------------------|
| `/v1/rules`  | 60 req/min per tap         |
| `/v1/stream` | 30 connections/min per tap |

## HTTP Error Codes

| Status | Meaning |
|--------|---------|
| 401 | Missing or invalid token (management key or tap token) |
| 403 | Resource not owned by your organization |
| 404 | Not found |
| 422 | Validation error or rule limit reached (max 25 rules per org) |
| 429 | Rate limit exceeded |

## Stream Errors

The stream emits an `error` event when something goes wrong:

```
event: error
data: {"message": "No rules configured. Create rules first via POST /v1/rules."}
```

Common stream error messages:
- `No rules configured` — the tap has no rules; create at least one before streaming
- Rate limit exceeded — you've opened too many connections; close others and retry
