# Daily Brief v2

Daily Brief v2 is the source-aware morning operator brief for Rob.

It should answer three questions:

1. What was checked?
2. What matters today?
3. What should Rob do next?

## Source Ledger

Start every brief with a compact source ledger.

Use these statuses:

- Checked
- Not checked
- Snapshot used
- Unavailable

Example:

```text
Sources:
- Gmail rob-personal: Checked, headers only.
- Gmail aifusionlabs: Unavailable, missing profile secret.
- Calendar rob-personal-calendar: Checked.
- Linear: Snapshot used from WORK.md.
- Inbox Captures: Checked.
```

Do not imply a source was checked unless Hermes actually inspected it during the current request.

## Format

```text
Morning operator brief

Date:
- YYYY-MM-DD

Sources:
- ...

Verify:
- ...

Urgent:
- ...

Worth attention:
- ...

Calendar:
- ...

Today's Top 3:
1. ...
2. ...
3. ...

Defer:
- ...

Personal/Family Anchor:
- One family/personal thing to protect today:

Risk:
- ...

Inbox Captures:
- ...

Needs Rob approval:
- ...
```

## Source Rules

Gmail:

- Headers only unless Rob approves reading bodies.
- Separate `rob-personal` from `aifusionlabs`.
- Do not mark financial items urgent unless the header shows immediate risk, deadline today, fraud, failed payment, overdraft, lockout, or security issue.

Calendar:

- Read-only by default.
- Include only schedule items, prep needs, conflicts, and protected-time risks.
- If Calendar was not inspected, write: `Calendar: Not checked.`
- Do not create, edit, delete, RSVP, invite, or send calendar messages without approval.

Linear:

- Use live Linear if available.
- If live Linear is unavailable, use WORK.md and label it as `Snapshot used`.
- Do not create or update Linear issues unless Rob approves.

Inbox Captures:

- Include only actionable current captures.
- Do not force stale captures, tests, duplicates, handled notes, or vague ideas into tasks.
- If none are actionable, write: `No actionable inbox captures.`

## Evidence Rules

Use careful evidence language:

- `Checked` means Hermes inspected the source.
- `Verified` means Hermes performed an explicit verification step.
- `Detected` means Hermes actively scanned the source.
- `None found` means the source was inspected and nothing matched.
- `None known from loaded context` means Hermes did not inspect a live source.
- `Not checked` means the source was skipped.

## Approval Queue

Use `Needs Rob approval` for any proposed state change.

Examples:

- Send or reply to email.
- Modify Calendar.
- Create or update Linear.
- Edit repo files.
- Change config, credentials, plugins, gateway state, or scheduled tasks.
- Save sensitive personal details.

If no approvals are needed:

```text
Needs Rob approval:
- None.
```
