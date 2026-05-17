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

Manual Coast test:

```bash
cd "/mnt/c/AI Fusion Labs/AI folder from OG Comp/iheart_dev"
./hermes_coast_night_watch.sh 30
```
