# Superpowers Philosophy

## Why not just start coding?

When an agent jumps straight to code, it optimizes for the wrong thing: producing output quickly, not solving the right problem. The brainstorming phase forces the agent to understand what you're *actually* trying to do before any implementation decisions are locked in.

From the obra/superpowers README:
> "As soon as it sees that you're building something, it doesn't just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do."

## Why TDD specifically?

Tests-after verify what you built. Tests-first define what *should* be built.

When you write the test first:
- You discover edge cases before writing broken code
- You're forced to think about the interface before the implementation
- The failing test proves your test actually tests something
- You have a clear definition of "done"

"Simple code breaks. The test takes 30 seconds." There is no task too simple for a test.

## Why subagent-driven development?

A single agent working on a large plan accumulates context debt. After many tasks, it's carrying the full plan, all previous code, all previous results — and starts making mistakes from context saturation.

Subagents solve this: each task gets a fresh agent with a focused prompt (~1-2k tokens for that task only). The parent agent stays lean: just the task list and short summaries. This is why Superpowers can work autonomously for hours without derailing.

## Why mandatory design approval?

"Simple" projects are where unexamined assumptions cause the most wasted work. A design can be short (a few sentences for truly simple tasks), but presenting it forces both parties to agree on what "done" looks like before any code is written.

Skipping design → implementing the wrong thing → discovering it at the end → rewrite.

## Why the strict anti-rationalization stance?

Agents (and humans) are good at finding reasons to skip discipline under pressure. The Superpowers skills are deliberately written to preempt common rationalizations:

- "This is too simple" → still needs a design
- "I'll add tests later" → delete the code, start with the test
- "I just need to explore first" → fine, throw away the exploration, start with TDD

The methodology works precisely because it doesn't give the agent wiggle room.
