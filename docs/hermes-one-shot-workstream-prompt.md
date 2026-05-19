# Hermes One-Shot Workstream Prompt

Use this prompt at the start of a new Hermes xlink-core workstream when the task may touch files, Gmail, Telegram, memory, config, scheduled tasks, or repo docs.

```text
Use repo path /mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core.
Use absolute paths only.
Follow xlink-core Rules of Engagement.
Treat draft, inspect, verify, report only, and plan as read-only.
For rob-personal Gmail, every Himalaya command must include --account rob-personal, including message read.
Do not ask for passwords if envelope list already works.
Do not modify files, config, memory, email, Telegram, calendar, reminders, or scheduled tasks unless I explicitly approve that state change.
Before editing, state the exact file path.
After editing, show the final diff.
If a command fails because of HOME, profile, account, working directory, or path confusion, diagnose that context first before retrying setup or asking for credentials.
```

## When To Use It

- File edits in Hermes Core.
- Gmail work involving `rob-personal`.
- Telegram or Capture workflow changes.
- Gateway, plugin, profile, or config work.
- Any task where Rob says draft, inspect, verify, plan, or report only.

## Quick Pass Criteria

Hermes is behaving correctly when it:

- Uses `/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core` for Hermes Core work.
- Does not write files when asked for draft or inspection only.
- Includes `--account rob-personal` on every personal Gmail command.
- Does not ask for the Gmail password if the envelope list already works.
- Shows the exact path before edits and the diff after edits.
