# WORK

This file is the current operating map. Keep it concise and update it when projects, priorities, or active workflows change.

## Primary Repos

Hermes Core:

```text
C:\AI Fusion Labs\X AGENTS\REPOS\Hermes Core
```

X-LINK:

```text
C:\AI Fusion Labs\X AGENTS\REPOS\X-LINK
```

iHeart / Coast Night Watch:

```text
C:\AI Fusion Labs\AI folder from OG Comp\iheart_dev
```

## GitHub

Hermes Core:

```text
https://github.com/aifusionlabs25/hermes-core
```

X-LINK:

```text
https://github.com/aifusionlabs25/X-LINK
```

iHeart:

```text
https://github.com/aifusionlabs25/iheart
```

## Linear Projects

- Hermes Personal OS
- iHeart / Coast Night Watch
- X Agents Workbench
- Job Search and Interview Ops

## Current Linear Status

Done setup items:

- AI-5: Harden rob-personal Gmail triage workflow
- AI-6: Turn Telegram Capture into an approved Linear intake workflow
- AI-7: Regenerate Hermes cheat sheet after latest docs updates
- AI-8: Create a Linear usage guide for Hermes Core
- AI-10: Add compression verification to the nightly report
- AI-11: Review data discontinuity warnings and reduce noise safely
- AI-12: Design retention and cleanup policy for WAV and MP3 recordings
- AI-13: Define the X-LINK workbench intake workflow
- AI-14: Create issue templates for agent validation and evals
- AI-15: Map active repos and workstreams into Linear
- AI-16: Build recruiter follow-up workflow
- AI-17: Create interview prep checklist
- AI-18: Create role tracking issue template
- AI-19: Draft Gmail-to-job-search triage workflow

Open item:

- AI-9: Verify tonight's scheduled Coast/iHeart run with the new audio route fix.

## Recommended Next Moves

1. Monitor and verify the next Coast/iHeart scheduled recording, then close AI-9 if successful.
2. Test Daily Brief v2 with source labels: Checked, Not checked, Snapshot used, and Unavailable.
3. Use Google Calendar as a read-only context source through Codex for now; decide later whether Hermes CLI/Telegram needs direct Calendar integration.
4. Start using Linear as the task board for new Hermes, X-LINK, iHeart, and job-search work.
5. Test the Capture to Linear workflow with inbox triage. Do not create issues without Rob approval, and recommend no issue when captures are stale, tests, duplicates, handled, or vague.
6. Keep `notes/inbox.md` local-only and out of GitHub.
7. Consider adding a short Hermes startup prompt that says: read `ROB.md`, `HERMES.md`, and `WORK.md`.

## Standard Startup Prompt

```text
Use repo path /mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core.
Read ROB.md, HERMES.md, and WORK.md first.
Then check Linear if the task mentions active work.
Follow xlink-core Rules of Engagement.
Do not change files, config, memory, email, Telegram, calendar, reminders, scheduled tasks, or Linear unless I explicitly approve.
```
