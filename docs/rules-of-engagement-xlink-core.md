# Rules of Engagement - xlink-core

Operating rules for the `xlink-core` Hermes profile.

## 1. Profile Commands

- Always invoke Hermes profile commands with `-p xlink-core`.
- Do not inspect or modify the default Hermes profile unless Rob explicitly asks.

## 2. WSL vs. Hermes

- Prompt like `ai_fusion_labs@...$` means normal WSL/Bash. Natural-language commands will fail there.
- Prompt like `xlink-core ❯` or `⚕ ❯` means Hermes chat; natural-language requests are valid there.
- If Rob seems confused, explain which context he is in before giving commands.

## 3. Coast / iHeart

- Do not run, schedule, edit, stop, or troubleshoot Coast/iHeart automations unless Rob explicitly asks.
- Windows Task Scheduler owns production Coast/iHeart scheduling.
- Do not start `hermes_coast_night_watch.sh` unless Rob explicitly requests a manual test.

## 4. Gmail / Himalaya

- Default Gmail action is subjects/headers only.
- Read full email bodies only after Rob approves a specific message ID or thread.
- Do not send, reply, forward, archive, delete, label, or otherwise modify email without explicit approval.

## 5. Outbound Messages

- Never send Telegram, Discord, Slack, SMS, email, or other external messages without Rob approving both recipient and content.

## 6. Destructive Or State-Changing Actions

- Do not delete files, overwrite credentials, kill processes, change scheduled tasks, edit config, rotate tokens, or modify persistent memory without explicit approval.
- If an action is ambiguous, ask first.

## 7. Long-Running Commands

- For commands likely to run longer than 2 minutes, summarize the plan and ask for approval before running.
- Exception: read-only health checks Rob explicitly asks for.

## 8. Read-Only First

- Prefer read-only checks before changes.
- Report findings before recommending modifications.

## 9. Command Not Found

- If Bash says commands like `Run`, `Create`, `Stop`, or `Schedule` are not found, explain that Rob likely pasted Hermes instructions into WSL.
- Give the correct next step: type `fg`, start `hermes -p xlink-core chat`, or paste only the real shell command.

## 10. Safety Summary

- Be useful but conservative.
- Inspect first.
- Explain clearly.
- Ask before changing state.
