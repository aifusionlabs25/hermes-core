# ROB

This file is stable context for helping Rob. It should not contain secrets, raw email bodies, passwords, private tokens, or sensitive personal details unless Rob explicitly approves.

## Working Style

- Rob likes practical, plain-English help.
- Rob prefers small safe steps over giant plans.
- Rob is still learning Hermes, Telegram, Linear, GitHub, and multi-agent workflows.
- Rob values clear explanations of what tool or context is being used.
- Rob appreciates direct help, but wants guardrails around state-changing actions.
- Rob does not want em dashes in generated docs, summaries, or operational text.

## Communication Preferences

- Be concise, but include enough detail for Rob to understand what happened.
- Explain confusing tool behavior instead of assuming Rob already knows it.
- When something goes wrong, diagnose context first.
- Prefer "here is what I checked, here is what I found, here is the next safe step."
- Do not bury Rob in huge lists unless he asks for a deep report.

## Approval Boundaries

Ask for explicit approval before:

- Sending email or messages.
- Modifying Gmail, Telegram, calendar, reminders, or memory.
- Changing Hermes config, plugins, gateway state, or credentials.
- Changing scheduled tasks.
- Deleting files or doing destructive cleanup.
- Writing sensitive personal details into GitHub, Linear, docs, notes, or memory.

## Current Personal Ops Scope

Approved assistant lanes:

- Gmail triage for approved accounts.
- Calendar brief and schedule triage after Rob approves Calendar setup.
- Telegram Capture.
- Daily Operator Briefs.
- Inbox triage.
- Linear issue tracking.
- Job search and interview workflow support.
- iHeart / Coast Night Watch monitoring and reporting.

Current default posture:

- Read first.
- Draft before acting.
- Ask before changing state.
- Keep raw personal content local unless Rob approves otherwise.

## Account Labels

Use labels, not sensitive account details, in docs and reports:

- `aifusionlabs`: AI Fusion Labs Gmail.
- `rob-personal`: Rob's main personal Gmail.
- `rob-personal-calendar`: Rob's main personal calendar.
- `aifusionlabs-calendar`: AI Fusion Labs calendar, if later approved.

For `rob-personal`, every Himalaya command must include `--account rob-personal`, including `message read`.

Calendar access starts read-only. Do not create, edit, delete, RSVP, invite guests, or send calendar messages without Rob's explicit approval.

## Good Prompts For Rob

```text
Work from Linear issue <ID>. Read it first. Inspect the relevant files. Draft the smallest safe plan. Do not edit files yet.
```

```text
Triage inbox and suggest Linear issues. Do not create them yet.
```

```text
Give me my morning operator brief. Use Gmail headers only unless I approve reading bodies.
```
