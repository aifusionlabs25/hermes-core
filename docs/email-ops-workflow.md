# Email Ops Workflow

This workflow defines how Hermes Core should handle email for Rob.

## Account

Initial account:

- `aifusionlabs@gmail.com`

This account is a low-risk starting point. Treat it as a read-only learning lane until Rob explicitly approves more authority.

## Default Mode

Email access starts as read-only.

Allowed:

- list recent emails
- search by sender, subject, date, or keyword
- summarize emails
- classify urgency
- identify likely next actions
- send summaries back to Telegram

Not allowed without explicit approval:

- send email
- reply to email
- forward email
- delete email
- archive or move email
- mark email read/unread
- create recurring email scans
- store email passwords in repo files

## Triage Lanes

- `urgent_response`
- `interview_recruiting`
- `day_job`
- `x_agents`
- `ai_fusion_labs`
- `finance_admin`
- `family_personal`
- `ai_news_learning`
- `newsletter_low_priority`
- `ignore_archive_candidate`

## Telegram Prompts

Examples:

```text
Check Gmail for anything urgent from today.
```

```text
Find AI-related emails from the last 3 days and summarize the useful ones.
```

```text
Look for recruiter or interview emails that need a response.
```

```text
Draft a reply, but do not send it.
```

## Summary Format

Keep summaries short:

```text
Gmail triage

Urgent:
- ...

Worth reading:
- ...

Can ignore:
- ...

Suggested next action:
- ...
```

## Sending Rules

Hermes Core may draft emails, but must not send until Rob explicitly approves the final text.

Approval must include:

- recipient
- subject
- exact body
- explicit send instruction

Example:

```text
Approved: send this exact email to jane@example.com.
```

## Credential Rules

- Use Google App Passwords for IMAP/SMTP.
- Do not commit credentials.
- Do not write credentials into this repo.
- Prefer OS keyring or a local config outside the repo, such as `~/.config/himalaya/config.toml`.
