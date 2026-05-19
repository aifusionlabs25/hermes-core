# Linear Usage Guide for Hermes Core

This guide explains how Rob, Hermes, and Codex should use Linear as a work tracker.

Linear is not the full memory system. Linear tracks active work, decisions, commitments, and follow-up items. Repo docs keep the operating rules. Chat sessions are working conversations.

## Core Rule

Use Linear for work that should survive the current chat.

Good Linear items:

- A bug that needs follow-up.
- A workflow that needs design or testing.
- A documentation update that should be done later.
- A project task with clear acceptance criteria.
- A decision or open loop that Rob wants tracked.

Do not create Linear issues for:

- Every chat message.
- Dead-end troubleshooting.
- One-off tests that are already complete.
- Sensitive personal details unless Rob explicitly approves.
- Raw Telegram Capture notes that have not been reviewed.

## Projects vs Issues

Projects are large workstreams.

Current projects:

- Hermes Personal OS
- iHeart / Coast Night Watch
- X Agents Workbench
- Job Search and Interview Ops

Issues are the actual units of work. Each issue should be small enough that Hermes or Codex can understand the scope, work it, verify it, and report back.

## What Every Issue Should Include

Each issue should have:

- A clear title.
- The project it belongs to.
- The reason it matters.
- Acceptance criteria.
- Guardrails or approval requirements.
- Links to repo files, docs, recordings, or related notes when useful.

## Approval Rules

Hermes and Codex may read Linear when Rob asks.

Hermes and Codex may create or update Linear issues when Rob explicitly approves or says to proceed with Linear setup.

Do not use Linear to bypass normal safety rules.

Approval is still required before:

- Editing files.
- Sending messages.
- Modifying email.
- Changing Hermes config.
- Changing scheduled tasks.
- Creating automations.
- Writing sensitive personal details into Linear.

## Telegram Capture and Linear

Telegram Capture is a fast inbox, not an automatic task creator.

Current flow:

1. Rob sends a Telegram message starting with `Capture:`.
2. Hermes stores the note in `notes/inbox.md`.
3. Hermes replies with `Captured to inbox.`
4. Later, Rob can ask Hermes to triage the inbox.
5. Hermes may suggest Linear issues, but must not create them without Rob approval.

Example:

```text
Triage inbox and suggest any Linear issues. Do not create them yet.
```

If Rob approves, Hermes or Codex can create the issue with a clear project, title, description, and acceptance criteria.

## Capture to Linear Intake

Use this workflow when Rob wants captured notes reviewed as possible Linear work.

Rob prompt:

```text
Triage inbox and suggest Linear issues. Do not create them yet.
```

Hermes should:

1. Read `notes/inbox.md` read-only.
2. Select only captures that look like real work, decisions, bugs, or follow-up items.
3. Ignore captures that are already handled, pure tests, or too vague to act on.
4. Draft proposed Linear issues, but do not create them yet.
5. Ask Rob for approval before creating any issue.

Proposal format:

```text
Proposed Linear issue

Project:
Hermes Personal OS

Title:
Build Gmail triage to Linear issue draft workflow

Description:
Short explanation of the captured idea and why it matters.

Suggested priority:
Medium

Acceptance criteria:
- ...
- ...

Needs Rob approval:
Yes
```

After Rob approves, Hermes or Codex may create the issue in Linear. The original capture stays in `notes/inbox.md` unless Rob separately approves editing or archiving the inbox.

## Daily and Weekly Reviews

Daily Operator Briefs may reference Linear, but should stay concise.

Useful daily checks:

- Highest priority issue in progress.
- Any urgent blocked item.
- One recommended next action.

Weekly reviews can be broader:

- What moved to Done.
- What is still In Progress.
- What should be closed, deferred, or split.
- What should be promoted from Capture or inbox notes into Linear.

## Agent Workflow

When working from Linear, Hermes or Codex should:

1. Confirm the issue ID and project.
2. Read the issue description and acceptance criteria.
3. Inspect the relevant repo files or systems.
4. State the intended change before editing when the task is sensitive or ambiguous.
5. Make only scoped changes.
6. Verify the result.
7. Report what changed.
8. Update Linear with a short status note when appropriate.

For code work tied to GitHub, prefer one Linear issue per branch or pull request.

## Recommended Prompt

Use this prompt when starting a Linear-driven Hermes or Codex task:

```text
Work from Linear issue <ID>.
Read the issue first.
Use the Hermes Core rules of engagement.
Keep changes scoped to the issue.
Do not modify files, config, email, Telegram, scheduled tasks, or memory unless the issue and Rob explicitly approve that action.
Report what you inspected, what you changed, how you verified it, and whether Linear should be updated.
```

## Current Best Next Issues

- AI-5: Harden rob-personal Gmail triage workflow
- AI-6: Turn Telegram Capture into an approved Linear intake workflow
- AI-8: Create a Linear usage guide for Hermes Core
- AI-9: Verify tonight's scheduled run with the new audio route fix
- AI-13: Define the X-LINK workbench intake workflow
- AI-16: Build recruiter follow-up workflow
