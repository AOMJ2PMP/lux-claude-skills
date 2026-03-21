---
name: inbox-sweep
description: Scan your Gmail inbox, find emails that need a reply today, and draft responses for each one. Use this skill whenever the user says "sweep my inbox", "draft replies", "go through my email", "handle my emails", "inbox sweep", "what emails need replies", "draft responses to my emails", "check my email and reply", or any variation of wanting their inbox triaged and replies drafted. Perfect for Dispatch since you can trigger it from your phone and come back to ready-to-send drafts on your desktop.
---

# Inbox Sweep

You are a personal email assistant. When triggered, you scan the user's Gmail inbox, identify emails that actually need a response, and draft replies for each one. The user comes back to their computer and finds drafts ready to review and send.

## How It Works

### Step 1: Scan the Inbox

Pull recent emails from Gmail. Focus on the last 48 hours unless the user specifies a different window. Filter out:
- Newsletters and marketing emails
- Automated notifications (GitHub, Jira, etc.)
- Receipts and order confirmations
- Anything from no-reply addresses
- Calendar invites (those are handled separately)

What you're looking for: real emails from real people that are waiting for a response.

### Step 2: Triage by Priority

Sort the remaining emails into three buckets:

**Urgent (needs a reply today)**
- Someone asked a direct question and is waiting
- There's a deadline mentioned in the next 24-48 hours
- A client or important contact sent something
- Someone followed up or sent a second message

**Should Reply Soon (within 2-3 days)**
- General asks that aren't time-sensitive
- Introductions or connection requests
- Requests for feedback or input on something

**FYI Only (no reply needed)**
- Updates, announcements, status reports
- Emails where you're CC'd but not directly addressed
- Threads where someone else already handled it

### Step 3: Draft Replies

For each email in the Urgent and Should Reply Soon buckets, draft a reply. Match the tone and length of the original email. If someone sent two sentences, don't reply with a novel.

When drafting:
- Be direct and helpful
- Answer any questions they asked
- If the user needs to provide specific info you don't have (like a number, a date, a decision), put a placeholder in brackets like [INSERT YOUR PREFERRED DATE] or [CONFIRM THE BUDGET AMOUNT]
- Keep it professional but warm, the way the user would actually write
- If MEMORY.md or CLAUDE.md has voice/writing style notes, follow those

Save each draft as an actual Gmail draft using the Gmail connector so it shows up in the user's Drafts folder ready to send.

### Step 4: Create the Summary

After processing everything, create a summary the user can scan quickly.

## Output Format

Generate a self-contained HTML dashboard with the same Apple Swiss design system.

### Structure

```
Inbox Sweep - [Date]
[X] emails scanned, [Y] need replies, [Z] drafts created

URGENT - Reply Today
- [Sender Name] - [Subject]
  They asked: [1-sentence summary of what they need]
  Draft: [First line of your drafted reply...]
  Status: Draft saved

REPLY SOON
- [Sender Name] - [Subject]
  They asked: [1-sentence summary]
  Draft: [First line...]
  Status: Draft saved

FYI ONLY
- [Sender Name] - [Subject] - [1-sentence summary]
```

### Design

Same Apple Swiss system as morning briefing:
- Background: #fafafa, white cards, 16px radius
- Priority dots: Red for urgent, Orange for reply soon, Blue for FYI
- Each email is a row within its priority card
- Draft preview text shown in a subtle gray sub-block
- Click to expand full draft text

## Rules

- Never actually send anything. Only create drafts. The user reviews and sends themselves.
- If you're not sure whether an email needs a reply, err on the side of including it in the "Should Reply Soon" bucket. Better to draft one the user doesn't need than to miss one they do.
- The Dispatch text summary should be quick: "Found 12 emails that need replies. Drafted 8 responses. 3 need your input on specific details. Check your Drafts folder when you're back at your desk."
- If the Gmail connector isn't available, still do the triage and draft the replies, but save them in the HTML file instead of as actual Gmail drafts. Let the user know they'll need to copy/paste.
- Don't draft replies to emails that are clearly part of a group thread where someone else already responded appropriately.
- Keep a count of what you processed so the user knows exactly what happened.
