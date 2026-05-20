# Calendar Ops Workflow

This workflow defines how Hermes should use Google Calendar for Rob.

Google Calendar is a planned context source. It should start read-only.

## Purpose

Calendar access helps Hermes answer:

- What is on Rob's schedule today?
- What needs preparation?
- What conflicts or tight transitions exist?
- What should be protected for family, recovery, or focus?
- What should appear in the Daily Operator Brief?

## Default Mode

Calendar access is read-only by default.

Allowed:

- list events
- summarize the day
- identify conflicts
- identify prep items
- identify travel or transition risk
- suggest calendar-related next actions

Not allowed without explicit approval:

- create events
- edit events
- delete events
- invite people
- RSVP
- send calendar messages
- create reminders or recurring automations
- write private calendar details into GitHub, Linear, docs, notes, or memory

## Account Labels

Use labels instead of exposing account details in docs and summaries:

- `rob-personal-calendar`
- `aifusionlabs-calendar`

Start with Rob's personal calendar only if Rob approves.

## Hermes Google Workspace Account Slots

Hermes CLI uses account-specific Google Workspace token slots.

Use:

```text
python3 /home/ai_fusion_labs/.hermes/profiles/xlink-core/skills/productivity/google-workspace/scripts/google_api.py --account rvicks calendar list --max 5
```

for `rob-personal-calendar`.

Use:

```text
python3 /home/ai_fusion_labs/.hermes/profiles/xlink-core/skills/productivity/google-workspace/scripts/google_api.py --account aifusionlabs calendar list --max 5
```

for `aifusionlabs-calendar`.

Do not run Google Workspace setup or Calendar checks without an `--account` value, because the default token can be overwritten.

## Daily Brief Integration

When Rob asks for a Daily Operator Brief and Calendar is approved, Hermes should say what was checked.

Example:

```text
Calendar:
- Checked: rob-personal-calendar for today.
- Not checked: aifusionlabs-calendar.
```

If Calendar was not checked:

```text
Calendar:
- Not checked.
```

Do not imply Calendar was checked unless the calendar source was actually inspected.

## Calendar Triage Format

```text
Calendar brief

Checked:
- ...

Today:
- ...

Prep:
- ...

Conflicts or risks:
- ...

Protected time:
- ...

Suggested next action:
- ...
```

## Approval Rules

Hermes may suggest changes, but Rob must approve the exact action.

Examples:

```text
Draft calendar change:
- Move: ...
- From: ...
- To: ...
- Reason: ...

Approval needed before editing the calendar.
```

```text
Draft event:
- Title: ...
- Date/time: ...
- Guests: ...
- Notes: ...

Approval needed before creating the event.
```

## Failure Handling

If Calendar access fails:

- report the exact source that failed
- do not ask for credentials until account, profile, HOME, and connector context have been checked
- continue the brief using the sources that were checked
- do not claim no calendar conflicts were found

## Best Next Setup

Recommended setup path:

1. Connect Google Calendar in the assistant environment Rob wants to use.
2. Verify read-only listing of today's events.
3. Add Calendar to the Daily Operator Brief as a checked or not-checked source.
4. Keep create/edit/delete actions blocked until Rob explicitly approves a safe workflow.

## Current Setup Status

Codex has Google Calendar connector access.

Read-only verification completed:

- Calendar: primary
- Window: 2026-05-19 through 2026-05-20
- Result: read-only event search succeeded

Hermes CLI/Telegram may not have the same connector access. If Hermes cannot access Calendar directly, use Codex as the Calendar bridge or add a separate Hermes-safe Calendar integration later.
