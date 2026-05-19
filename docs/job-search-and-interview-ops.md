# Job Search and Interview Ops

This guide defines safe workflows for job search, recruiter follow-up, interview prep, role tracking, and Gmail triage.

## Default Rules

- Draft first.
- Do not send email without Rob approval.
- Do not modify Gmail, calendar, reminders, Telegram, memory, or Linear without explicit approval.
- Keep personal details out of Linear unless Rob approves.
- Use `rob-personal` only with `--account rob-personal` on every Himalaya command.

## Recruiter Follow-Up Workflow

Use when Rob asks for help following up with a recruiter or hiring manager.

Collect:

- Company
- Role
- Contact name
- Contact email or source
- Last touch
- Desired next action
- Deadline or timing
- Relevant notes

Output:

```text
Recruiter follow-up draft

Company:
...

Role:
...

Contact:
...

Context:
...

Suggested next action:
...

Draft message:
...

Needs Rob approval before sending:
Yes
```

## Interview Prep Checklist

Use when Rob has an interview, screening call, or prep session.

Checklist:

- Company summary
- Role summary
- Why Rob fits
- Likely interview themes
- STAR examples to prepare
- Questions Rob should ask
- Risks or gaps to be ready for
- Follow-up draft rules

Output:

```text
Interview prep

Company:
...

Role:
...

Rob's fit narrative:
...

STAR examples to prepare:
- ...

Questions to ask:
- ...

Follow-up plan:
...
```

## Role Tracking Template

Use this format for a job-search Linear issue or local note.

```text
Company:

Role:

Source:

Status:

Contact:

Last touch:

Next action:

Deadline:

Notes:

Needs Rob approval before outreach:
Yes
```

## Gmail-to-Job-Search Triage

Use when Rob asks Hermes to review job-search email.

Rules:

- Headers first when possible.
- Bodies only when Rob asks or has already approved the account scope.
- Never send, archive, delete, label, or reply without explicit approval.
- Keep the output short and action-oriented.

Suggested prompt:

```text
Triage rob-personal Gmail for job search and interview items, page size 10. Read headers first. Read bodies only for likely relevant messages. Do not modify email or write memory.
```

Output:

```text
Job-search Gmail triage

Urgent:
- ...

Worth reading:
- ...

Follow-up candidates:
- ...

Can ignore:
- ...

Suggested next action:
- ...
```

