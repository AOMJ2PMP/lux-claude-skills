---
name: superpowers-methodology
description: >
  Apply the Superpowers structured software development methodology when building any software feature, fixing bugs, or doing any non-trivial coding task. This skill encodes the complete obra/superpowers workflow: mandatory brainstorming before code, implementation planning with bite-sized tasks, TDD enforcement, and subagent-driven execution with two-stage code review.

  USE THIS SKILL whenever the user says any of: "let's build", "help me implement", "add a feature", "create a new", "fix this bug", "debug this", "write code for", "I want to build", "help me code", "plan this feature", "make a PR", or any other coding/building intent. Do NOT skip this process for "simple" tasks — unexamined assumptions waste the most time on supposedly simple projects.

  The philosophy: Don't jump into writing code. Step back, understand what's really needed, get design approval, make a plan, then execute systematically with tests.
---

# Superpowers Methodology

A structured agentic software development workflow based on obra/superpowers (github.com/obra/superpowers, 40k+ stars). Encodes proven patterns for getting coding agents to do high-quality, non-derailing work.

**Core principle:** The agent checks for relevant skills before ANY task. These are mandatory workflows, not suggestions.

---

## The 7-Stage Workflow

Always follow these stages in order. Do not skip stages, even for "simple" tasks.

### Stage 1: BRAINSTORMING (before any code)

**Trigger:** User wants to build/implement/add anything.

**Mandatory checklist — create a task for each item:**
1. Explore project context — check existing files, docs, recent commits
2. Offer visual companion if topic involves UI/layout questions (separate message)
3. Ask clarifying questions **one at a time** (multiple choice preferred)
4. Propose **2-3 alternative approaches** before settling on one
5. Present design in sections for incremental validation
6. Write design doc → save to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` and commit

**<HARD-GATE>:** No implementation skills, no code, no scaffolding until design is presented AND user approves.

**Principles:**
- One question at a time — don't overwhelm
- YAGNI ruthlessly — remove unnecessary features from ALL designs
- "This is too simple to need a design" is rationalization — resist it
- Incremental validation — present design sections, get approval before moving on

**After approval:** Invoke `writing-plans` stage. Do NOT jump to any other skill.

---

### Stage 2: GIT WORKTREE SETUP (after design approval)

**Trigger:** Design approved, about to start implementation.

**Steps:**
1. Create isolated workspace on a new branch
2. Run project setup (install deps, build, etc.)
3. Verify clean test baseline — all existing tests pass before touching code

**Why:** Keeps work isolated. If something goes wrong, you haven't polluted main.

---

### Stage 3: WRITING THE PLAN (with approved design)

**Trigger:** Design doc exists and is approved by user.

**Each task in the plan must have:**
- Exact file paths affected
- Complete code to write (no hand-waving)
- Verification step (how to confirm it's done)
- Estimated time: **2-5 minutes per task**

**Plan format:**
```markdown
# [Feature Name] Implementation Plan
> **For Claude:** Use executing-plans or subagent-driven-development to implement task-by-task.

## Task 1: [Name]
**File:** `src/path/to/file.ts`
**What:** [Exact description]
**Code:** [Complete snippet]
**Verify:** [Specific check]

## Task 2: ...
```

**Save to:** `docs/plans/YYYY-MM-DD-<feature-name>.md`

**Principles:**
- Write plans clear enough for "an enthusiastic junior engineer with poor taste, no judgment, no project context, and an aversion to testing"
- YAGNI — if it's not in the design, it's not in the plan
- DRY — no duplicate logic across tasks

---

### Stage 4: EXECUTION (subagent-driven or batch)

**Trigger:** Plan exists and user says "go."

**If subagents available (Claude Code, Codex):** Use `subagent-driven-development`
- Dispatch fresh subagent per task with focused prompt (just that task's content)
- Two-stage review per task: (1) spec compliance, (2) code quality
- Parent agent stays lean — only task list + summaries in context

**If no subagents:** Use `executing-plans`
- Work through tasks in batches
- Stop for human checkpoint after each batch
- Note: quality will be lower — recommend switching to a subagent-capable platform

**Never:** Execute all tasks in one shot without review checkpoints.

---

### Stage 5: TEST-DRIVEN DEVELOPMENT (during implementation)

**Trigger:** Implementing any task that involves new or changed behavior.

**The Iron Law — RED-GREEN-REFACTOR:**

```
RED:    Write a FAILING test first. Run it. Confirm it fails.
GREEN:  Write MINIMAL code to make it pass. Run tests. Confirm pass.
REFACTOR: Clean up. Run tests again. Confirm still passing. Commit.
```

**Hard rules:**
- Write code before the test? **Delete it. Start over.**
- "It's too simple to need a test" → write the test anyway (30 seconds)
- Tests-after ≠ TDD. Tests-after verify what you built. Tests-first define what should be built.
- Tests passing immediately after writing = tests don't work. Confirm RED first.

**Rationalization counter:**
- "I'll add tests later" → You won't. Delete the code, start with test.
- "It's just a utility function" → Write the test. It takes 30 seconds.
- "I need to explore first" → Fine. Throw away exploration code. Start fresh with TDD.

---

### Stage 6: CODE REVIEW (between tasks)

**Trigger:** Each task completes before moving to next.

**Two-stage review:**
1. **Spec compliance:** Does the code do what the task described?
2. **Code quality:** Is it clean, DRY, no obvious bugs?

**Severity levels:**
- 🔴 Critical — blocks progress, must fix before next task
- 🟡 Major — should fix before branch merge
- 🟢 Minor — note for later

**Critical issues block forward progress.** Do not proceed to next task.

---

### Stage 7: FINISHING THE BRANCH

**Trigger:** All tasks complete.

**Steps:**
1. Run full test suite — all tests must pass
2. Present options to user:
   - Merge to main
   - Open pull request
   - Keep branch, do more work
   - Discard branch
3. Clean up worktree

---

## Debugging Protocol

**Trigger:** Any bug, unexpected behavior, test failure.

**4-Phase systematic process:**

### Phase 1: Reproduce
- Get a reliable reproduction case before anything else
- "It sometimes fails" → find when it always fails

### Phase 2: Isolate
- Trace backward through call stack to find original trigger (see `root-cause-tracing`)
- Seeing symptoms ≠ understanding root cause
- 95% of "no root cause" cases = incomplete investigation

### Phase 3: Fix
- Fix the root cause, not the symptom
- Add validation at multiple layers after finding root cause (`defense-in-depth`)
- Write a failing test that reproduces the bug BEFORE fixing

### Phase 4: Verify
- Confirm the specific bug is fixed
- Confirm nothing else broke
- "I think it's fixed" is not verification

**Never:** Guess-and-check. Random changes without hypothesis.

---

## Key Principles Summary

| Principle | What it means |
|-----------|---------------|
| **TDD** | Test first, always. No exceptions. |
| **YAGNI** | Don't build what isn't in the design |
| **DRY** | No duplicate logic |
| **Systematic > Ad-hoc** | Process over guessing |
| **Evidence > Claims** | Verify before declaring success |
| **Complexity reduction** | Simplicity is the primary goal |

---

## Skill Invocation Map

| Situation | Invoke this stage |
|-----------|-------------------|
| "Let's build X" | Brainstorming → Writing Plans → Execution |
| "Fix this bug" | Debugging protocol → TDD fix |
| "Add a feature" | Brainstorming first, always |
| Implementing any task | TDD |
| Task complete | Code Review |
| All tasks done | Finish Branch |

**Rigid skills (follow exactly):** TDD, Debugging
**Flexible skills (adapt to context):** Brainstorming, Planning

---

## Reference Files

- `references/philosophy.md` — deeper rationale for why this methodology works
- `references/anti-patterns.md` — common rationalizations to resist
