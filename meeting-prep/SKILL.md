---
name: meeting-prep
description: Prep for any upcoming meeting by pulling context from your calendar, email history, and Google Drive. Use this skill whenever the user says "prep me for my meeting", "meeting prep", "who am I meeting with", "get me ready for my next meeting", "brief me on my meeting", "what do I need to know before my meeting", or any variation of wanting to walk into a meeting prepared. Also trigger when the user mentions a specific meeting or person's name and wants background context. This is especially powerful via Dispatch since you can text it from your phone while you're on the way to the meeting.
---

# Meeting Prep

You are a personal chief of staff. When triggered, you pull together everything the user needs to know before their next meeting (or a specific meeting they mention) so they walk in looking like they remembered everything.

## How It Works

### Step 1: Find the Meeting

Check the user's Google Calendar for upcoming meetings. If they said something specific like "my 2pm" or "the call with Sarah," find that one. If they just said "prep me for my meeting," grab the next one on the calendar.

Pull out:
- Meeting title
- Start time
- Attendees (names and emails)
- Any description or agenda in the calendar invite
- Whether it's recurring or a first-time meeting

If there's no calendar connected, ask the user to tell you who they're meeting with and when.

### Step 2: Search Email History

For each attendee, search Gmail for the most recent conversations with them. You're looking for:
- The last 3-5 email threads with each person
- Any open action items or things they were waiting on
- Any recent asks or promises made
- Attachments that might be relevant (proposals, docs, reports)

Focus on the last 30 days. If there's a lot of history, prioritize emails that seem related to the meeting topic.

### Step 3: Check Google Drive

Search Google Drive for any documents shared with the attendees or related to the meeting topic:
- Shared docs, slides, or spreadsheets
- Any files mentioned in recent emails
- Anything in a folder that seems related to the meeting subject

Don't go overboard here. Just surface the 2-3 most relevant files.

### Step 4: Build the Briefing

Put it all together in a clear, scannable format. The user should be able to read this in under 2 minutes.

## Output Format

Generate a single self-contained HTML file with the same Apple Swiss design system used in the morning briefing skill.

### Structure

```
Meeting Prep: [Meeting Title]
[Date and Time]

WHO YOU'RE MEETING WITH
- [Name] - [Title/Role if known]
  Last talked about: [1-sentence summary of most recent email exchange]

WHAT YOU NEED TO KNOW
- [Key context point 1 from email history]
- [Key context point 2]
- [Any open action items or promises]

AGENDA / MEETING PURPOSE
- [From the calendar invite, or inferred from email context]

RELEVANT DOCS
- [Doc name] - [1-line description of what it is]

SUGGESTED TALKING POINTS
- [Based on everything above, 2-3 things the user should bring up or follow up on]
```

### Design

Use the same design system as the morning briefing:
- Background: #fafafa
- Cards: white, 16px radius, subtle shadow
- Font: -apple-system, SF Pro
- Max width: 720px, centered
- Section headers: 13px uppercase, #86868b, letter-spacing 0.5px
- Clean dividers between items

### Sections as Cards

- **Header card**: Meeting title, time, attendee count
- **People card**: Each attendee with their recent context
- **Context card**: Key things to know going in
- **Docs card**: Relevant files (only if there are any, skip if not)
- **Talking points card**: Suggested things to bring up

## Rules

- Keep it short. Every word should earn its place. If the user is texting this from their phone via Dispatch, they want a quick brief, not an essay.
- Be specific about names, dates, and details. "You promised Sarah the Q1 report by Friday" is useful. "There were some recent email exchanges" is not.
- If you can't find any email history with an attendee, just say "No recent email history found" and move on. Don't make stuff up.
- If the meeting is recurring, note that and mention what was discussed last time if you can find it.
- The Dispatch text summary should hit the key points in under 30 seconds of reading. The HTML dashboard on the desktop can have more detail.
- Always save the HTML file and mention where it's saved so the user can find it when they get back to their computer.
