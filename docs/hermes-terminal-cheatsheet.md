# Hermes / WSL Terminal Cheat Sheet

Plain-English reference for knowing where you are and what kind of commands belong there.

## The Big Idea

You have two different places that can look similar:

1. A normal WSL terminal.
2. A Hermes chat session running inside WSL.

The biggest rule:

- In a normal WSL terminal, type real shell commands only.
- In Hermes chat, type natural-language requests.

If you paste natural language into a normal WSL terminal, it tries to run words like `Run`, `Create`, or `Stop` as Linux commands.

## How To Tell Where You Are

### Normal WSL Terminal

Looks like:

```bash
ai_fusion_labs@AIFusionLabs-Node1:~$
```

or:

```bash
ai_fusion_labs@AIFusionLabs-Node1:/mnt/c/AI Fusion Labs/...$
```

What it means:

You are talking to Linux/Bash directly.

Good examples:

```bash
pwd
ls
cd "/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core"
git status
hermes -p xlink-core chat
```

Bad examples in WSL:

```text
Run this terminal command:
Create a cron job...
Stop the currently running task...
Can you inspect this folder?
```

Those are requests for Hermes, not WSL commands.

## Hermes Chat

Looks like:

```text
xlink-core ❯
```

or:

```text
⚕ ❯
```

What it means:

You are talking to Hermes. Natural language is okay here.

Good examples:

```text
Who are you and what profile are you running under?
```

```text
Inspect this repo and summarize the current files.
```

```text
Run this terminal command:
git status
```

```text
Check my latest Gmail inbox subjects only. Do not read bodies unless I ask.
```

Bad examples in Hermes:

```bash
cd "/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core"
git status
```

Hermes may understand that, but it is clearer to say:

```text
Run these terminal commands:
cd "/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core"
git status
```

## If Hermes Is Suspended

You might see:

```text
Hermes Agent has been suspended. Run `fg` to bring Hermes Agent back.
[1]+  Stopped                 hermes chat
```

That means Hermes was paused, usually by `Ctrl+Z`.

To resume it, type this in the normal WSL terminal:

```bash
fg
```

If that feels messy, start a fresh Hermes chat:

```bash
hermes -p xlink-core chat
```

## Starting Hermes

From a normal WSL terminal:

```bash
hermes -p xlink-core chat
```

This opens the `xlink-core` Hermes chat profile.

To list profiles:

```bash
hermes profile list
```

## Gateway Basics

The gateway is what lets Hermes talk through messaging platforms like Telegram.

Check profiles/gateway status:

```bash
hermes profile list
```

Start the xlink-core gateway:

```bash
hermes -p xlink-core gateway run --accept-hooks
```

If it says the gateway is already running, do not panic. That usually means it is already alive.

Common safe choice:

```text
Do nothing / keep current instance running
```

Restart only when you intentionally changed config:

```bash
hermes -p xlink-core gateway restart
```

## Telegram Use

If Telegram is connected, you can message Hermes from your phone.

Good Telegram requests:

```text
Summarize my latest Gmail subjects only.
```

```text
Check the X Link Hub repo status.
```

```text
Remind me what Hermes profile you are running under.
```

Avoid giving Hermes destructive tasks casually from Telegram. If deleting files or changing credentials, slow down and confirm.

## Gmail / Himalaya

Himalaya is the command-line email tool Hermes can use.

Safe read-only style:

```text
List my latest 10 Gmail subjects only. Do not read bodies.
```

If you want bodies:

```text
Read the body of email ID 1234 and summarize it.
```

Useful WSL checks:

```bash
himalaya account list
himalaya folder list
himalaya envelope list --page-size 5
```

## Coast / iHeart Night Watch

This is now handled by Windows Task Scheduler, not Hermes cron.

Task name:

```text
\AI Fusion Labs\Coast Night Watch
```

Current production timing:

```text
11:05 PM Arizona time
4 hours
```

Do not ask Hermes to schedule or run this again unless you intentionally want a manual test.

Manual short test from normal WSL:

```bash
cd "/mnt/c/AI Fusion Labs/AI folder from OG Comp/iheart_dev"
./hermes_coast_night_watch.sh 30
```

Manual 15-minute test:

```bash
cd "/mnt/c/AI Fusion Labs/AI folder from OG Comp/iheart_dev"
./hermes_coast_night_watch.sh 900
```

Do not paste natural language above those commands into WSL.

## Windows Task Scheduler Checks

From PowerShell, not WSL:

```powershell
Get-ScheduledTask -TaskPath "\AI Fusion Labs\" -TaskName "Coast Night Watch"
```

```powershell
Get-ScheduledTaskInfo -TaskPath "\AI Fusion Labs\" -TaskName "Coast Night Watch"
```

From Codex, ask:

```text
Check the Coast Night Watch scheduled task status.
```

## Common Mistakes

### Mistake: Pasting a Hermes request into WSL

You typed:

```text
Run this terminal command:
```

WSL replied:

```text
Command 'Run' not found
```

Fix:

Either type only the real command in WSL, or enter Hermes chat first.

### Mistake: Hermes gets suspended

You see:

```text
Stopped hermes chat
```

Fix:

```bash
fg
```

### Mistake: Asking Hermes to schedule Coast

Hermes may run it immediately.

Fix:

Do not use Hermes for the Coast production schedule right now. Windows Task Scheduler owns it.

## Quick Reference

Normal WSL prompt:

```text
ai_fusion_labs@...$
```

Use:

```bash
cd
ls
git status
hermes -p xlink-core chat
```

Hermes prompt:

```text
xlink-core ❯
```

Use:

```text
Run this terminal command:
git status
```

Resume suspended Hermes:

```bash
fg
```

Start fresh Hermes:

```bash
hermes -p xlink-core chat
```

Check Hermes profiles:

```bash
hermes profile list
```

Check Gmail:

```bash
himalaya envelope list --page-size 5
```

Gmail account labels:

- `aifusionlabs`: AI Fusion Labs Gmail.
- `rob-personal`: Rob's main personal Gmail.

Hermes can summarize headers and bodies from approved Gmail accounts when you ask for Gmail summary, triage, or review.

Safe examples:

```text
Summarize Gmail for rob-personal.
Triage Gmail for aifusionlabs, page size 10.
Check both Gmail accounts for anything important today.
```

Rules:

- Hermes should always say which Gmail account it is checking.
- For `rob-personal`, every Himalaya command needs `--account rob-personal`, including `message read`.
- If `envelope list` works but `message read` fails, tell Hermes to retry with `himalaya message read --account rob-personal <ID>`. Do not paste the password again.
- Summaries are temporary unless you explicitly ask Hermes to save them.
- Sensitive categories need extra care: medical, legal, financial, tax, password/security, family conflict, and identity documents.
- Hermes must ask before sending, replying, forwarding, archiving, deleting, labeling, creating tasks, creating calendar events, creating reminders, sending Telegram messages, or writing memory.

Manual Coast test:

```bash
cd "/mnt/c/AI Fusion Labs/AI folder from OG Comp/iheart_dev"
./hermes_coast_night_watch.sh 30
```

---

**Telegram cheat-sheet (Rob-focused)**

---

**1. How Telegram talks to Hermes**
- Anything you type in Telegram is sent to Hermes for thinking.
- Hermes replies in the same Telegram chat unless the message is meant for a fast lane command.

**2. The "Capture:" fast lane**
- Prefix a note with `Capture:` and Hermes will skip the normal reasoning step.
- The note is saved directly to the inbox file.

**3. Example message**

```
Capture: remember to review this later
```

**4. What you will see back**

```
Captured to inbox.
```

If there is a problem you will see:

```
Capture failed. Check inbox script.
```

**5. Where the captured notes appear**

All notes are appended to

```
/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core/notes/inbox.md
```

You can view them from a terminal with:

```
cat "/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core/notes/inbox.md"
```

**6. Where to make configuration or plugin changes**
- Never edit plugins, gateway settings, or profile config from Telegram.
- Use the Hermes chat (run `hermes -p xlink-core chat` from a normal WSL terminal) for any of those tasks.

**7. If Telegram stops replying**
1. Check the gateway status from a regular WSL terminal:

```
hermes -p xlink-core gateway status
```

2. Or open a Hermes chat session (`hermes -p xlink-core chat`) and ask "What is the gateway status?".

---

Quick reminder: use Telegram for quick notes (`Capture:`) and for asking Hermes questions. Use the Hermes chat for any setup, plugin, or gateway work. This keeps the two interfaces clean and avoids accidental configuration changes from Telegram.

---

How to Talk to Hermes (for Rob)

- Use natural-language commands only when the prompt shows the Hermes chat indicator, e.g. "xlink-core >" or "* >".
- In a normal Bash prompt (e.g. "ai_fusion_labs@...$"), Hermes commands will not be understood; run shell commands there.
- To start Hermes chat from WSL, run: hermes -p xlink-core chat.
- Keep requests concise and action-oriented. Ask for one thing at a time.
- When you need Hermes to inspect something, phrase it as a read-only check first (e.g. "show gateway status", "list Gmail headers").
- Ask for confirmation before any state-changing action (file delete, config edit, sending messages, starting automations, etc.).
- Use the prescribed headings for daily briefs: Morning operator brief, Midday reset, Evening shutdown.
- For captures, start the line with "Capture:" and let Hermes append it to the inbox file.
- Never include em dashes; use commas, periods, colons, or semicolons.
- If you see an error like "command not found", you are probably in the wrong context; switch to the Hermes prompt.
- Remember the safety summary: read first, report findings, ask before changing.

---

Hermes Core reliability rules

- Hermes Core repo path:

```text
/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core
```

- Use absolute paths for Hermes Core docs, notes, scripts, and config.
- Do not let Hermes edit `docs/...` unless it has first confirmed the full repo path above.
- If you say draft, inspect, verify, plan, or report only, Hermes should not write files or change state.
- If Hermes asks for a password after a Gmail envelope list already worked, stop it and ask it to check account flags and HOME first.
- For file edits, ask Hermes to show the final diff.

One-shot starter prompt:

Saved reference:

```text
/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core/docs/hermes-one-shot-workstream-prompt.md
```

```text
Use repo path /mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core.
Use absolute paths only.
Follow xlink-core Rules of Engagement.
Treat draft, inspect, verify, report only, and plan as read-only.
For rob-personal Gmail, every Himalaya command must include --account rob-personal.
Do not ask for passwords if envelope list already works.
Do not modify files, config, memory, email, Telegram, calendar, reminders, or scheduled tasks unless I explicitly approve that state change.
Before editing, state the exact file path. After editing, show the final diff.
```
