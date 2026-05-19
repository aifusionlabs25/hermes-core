# Email Ops Workflow

This workflow defines how Hermes Core should handle email for Rob.

## Account

Approved account labels:

- `aifusionlabs@gmail.com`
- `aifusionlabs`: AI Fusion Labs Gmail.
- `rob-personal`: Rob's main personal Gmail.

Treat all Gmail accounts as read-only learning lanes until Rob explicitly approves more authority.

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

## Personal Gmail Rules

When using `rob-personal`, every Himalaya command must include `--account rob-personal`.

Examples:

```bash
himalaya envelope list --account rob-personal --page-size 5
himalaya message read --account rob-personal <ID>
```

If `himalaya envelope list --account rob-personal ...` works but `message read` fails, retry the message read with `--account rob-personal` before asking Rob for credentials.

If a Gmail command fails because of `HOME`, profile, account, or working directory confusion, diagnose that context first. Do not ask Rob to paste the password again unless the credential file is actually missing, empty, or rejected after the correct account and context are confirmed.

Personal Gmail summaries are temporary unless Rob explicitly asks to save them. Do not write personal email content into memory, repo files, Linear, or notes without explicit approval.

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
