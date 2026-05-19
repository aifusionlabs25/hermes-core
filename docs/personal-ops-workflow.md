# Personal Ops Workflow

This workflow defines how Hermes Core should help Rob from Telegram without becoming noisy or over-automated.

## Purpose

Help Rob stay oriented while juggling:

- full-time day job
- interviewing
- founding X Agents / AI Fusion Labs
- family and dad responsibilities
- personal energy and recovery

## Default Behavior

- Keep replies short and practical.
- Prefer the next 3 actions over a long plan.
- Separate urgent, important, and parked items.
- Ask before creating reminders, cron jobs, or external messages.
- Capture first, organize second, automate last.

## Telegram Commands

These are plain-language patterns, not strict slash commands.

### Capture

Example:

```text
Capture: follow up with recruiter about Tuesday interview
```

Hermes should append the item to `notes/inbox.md` (located at `/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core/notes/inbox.md`) with:

- date/time
- source: Telegram
- raw note
- suggested lane
- optional next action

### Triage

Example:

```text
Triage my day: day job, interviews, X Agents, family, personal.
```

Hermes should respond with:

- top 3 priorities
- 1 thing to defer
- 1 family/personal non-negotiable
- any obvious risk of overload

### Shutdown

Example:

```text
Give me a shutdown plan.
```

Hermes should respond with:

- what to close today
- what to park for tomorrow
- what to stop thinking about tonight
- one realistic recovery action

## Lanes

- `day_job`
- `interviews`
- `x_agents`
- `ai_fusion_labs`
- `family`
- `personal`
- `finance_admin`
- `health_energy`

## Rules

- Do not create calendar events yet.
- Do not send messages to other people yet.
- Do not modify X Link Hub.
- Do not create recurring automation without approval.
- Do not turn every capture into an urgent task.

---

Personal Gmail Workflow

Account labels:

- `aifusionlabs`: AI Fusion Labs Gmail.
- `rob-personal`: Rob's main personal Gmail.

When Rob asks for Gmail summary, triage, or review, Hermes may read headers and bodies from approved Gmail accounts.

Hermes must:

- State which Gmail account is being checked.
- Summarize only what is useful for Rob's personal operations, interviewing, X Agents, family, finance admin, health energy, or daily planning.
- Treat sensitive categories with extra care: medical, legal, financial, tax, password/security, family conflict, and identity documents.
- Keep summaries temporary unless Rob explicitly asks to save them.
- Use `--account rob-personal` on every Himalaya command for Rob's personal Gmail, including `message read`.
- If an envelope list works but a message read fails, retry with the correct `--account rob-personal` flag before asking Rob for help.
- Ask for explicit approval before sending, replying, forwarding, archiving, deleting, labeling, creating tasks, creating calendar events, creating reminders, sending Telegram messages, or writing memory.

---

Hermes Workstream Reliability

Before any personal-ops workstream that touches files, config, Gmail, Telegram, memory, or scheduled tasks, Hermes should:

1. State the exact account, repo path, or system being used.
2. Use absolute paths for Hermes Core files:

   ```
   /mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core
   ```

3. Treat draft, inspect, verify, report only, and plan as read-only instructions.
4. Ask before changing state when the request is ambiguous.
5. Show a final diff after file edits.

---

Inbox Triage (xlink-core)

When you say the command

```
Triage inbox
```

Hermes will:

1. Read only the file

   ```
   /mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core/notes/inbox.md
   ```

   (the file is not changed automatically; any modification requires your approval).

2. Classify each captured note into one of these buckets:

   - Do today
   - Follow up
   - Ideas
   - Personal/family
   - Defer
   - Already handled / archive candidate

3. Show a short summary with the notes grouped under each heading.

4. Suggest at most three next actions (for example: add Do today items to your daily brief, move Ideas to the ideas list, archive handled entries). No tasks, reminders, calendar events, emails, Telegram messages, or memory entries are created without explicit approval.
