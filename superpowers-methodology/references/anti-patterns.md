# Anti-Patterns: Rationalizations to Resist

These are the exact rationalizations agents (and developers) use to skip the Superpowers workflow. Recognize them. Reject them.

## Skipping Brainstorming

❌ "This is too simple to need a design"
→ Simple projects are where unexamined assumptions cause the MOST wasted work. Write a short design anyway.

❌ "The user already knows what they want, I'll just build it"
→ What they said they want ≠ what they actually need. Clarifying questions exist for this reason.

❌ "I'll start coding while we brainstorm"
→ HARD-GATE: No code until design is approved.

## Skipping TDD

❌ "I'll add tests later"
→ You won't. Delete the code. Start with the test.

❌ "It's just a small utility function"
→ Write the test. It takes 30 seconds. Small functions break silently.

❌ "I need to explore the approach first"
→ Fine. Throw away the exploration. Start fresh with a test.

❌ "The tests pass" (written after the code)
→ Tests written after verify what you built, not what should be built. They're biased by your implementation.

❌ "Tests passing immediately is good"
→ Tests passing immediately = tests that don't actually test anything. Always confirm RED before GREEN.

## Skipping Code Review

❌ "I know this task is correct"
→ Overconfidence guarantees missed issues. Two-stage review takes minutes and catches real bugs.

❌ "I'll review after all tasks are done"
→ Critical issues compound. Review between every task.

## Skipping Root Cause in Debugging

❌ "I'll just try changing X and see if it helps"
→ Guess-and-check is slower than systematic debugging. Isolate root cause first.

❌ "I found the root cause" (after < 5 minutes)
→ 95% of "no root cause" cases are incomplete investigation. Keep digging.

❌ "The symptom is gone, must be fixed"
→ Symptom gone ≠ root cause fixed. Verify the specific bug and run the full suite.

## Meta Anti-Pattern: Violating the Spirit

"Technically I did brainstorm (one sentence) / write a test (after the code) / review (skimmed it quickly)"

**Violating the letter of the rules IS violating the spirit.** The rules exist to prevent exactly this category of corner-cutting.
