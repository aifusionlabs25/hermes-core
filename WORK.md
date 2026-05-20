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
- X Agents GTM Ops (planned)

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
2. Start testing the X Agents GTM workflow with small public-web-only Local Lead Scout runs using structured local data first, then public business websites.
3. Use current NVIDIA/gpt-oss-120b as the working Hermes model until Grok access is usable.
4. Keep the xAI/Grok OAuth side project parked. OAuth is connected, but inference is blocked by xAI entitlement. Revisit with an xAI API key or confirmed API-capable subscription.
5. Test Daily Brief v2 with source labels: Checked, Not checked, Snapshot used, and Unavailable.
6. Use Google Calendar as a read-only context source through Codex for now; decide later whether Hermes CLI/Telegram needs direct Calendar integration.
7. Start using Linear as the task board for new Hermes, X-LINK, iHeart, GTM, and job-search work.
8. Test the Capture to Linear workflow with inbox triage. Do not create issues without Rob approval, and recommend no issue when captures are stale, tests, duplicates, handled, or vague.
9. Keep `notes/inbox.md` local-only and out of GitHub.
10. Consider adding a short Hermes startup prompt that says: read `ROB.md`, `HERMES.md`, and `WORK.md`.
11. Design a Codex-as-Hermes-Prime operating lane: use Codex for high-judgment daily briefings, Calendar/Gmail/Linear synthesis, GTM research, repo work, and quality control while local Hermes handles Telegram capture, local quick checks, and proven lightweight routines.

## Parked Side Projects

Grok / xAI OAuth:

- Hermes was updated to v0.14.0.
- xAI OAuth is connected in the xlink-core profile.
- xAI proxy status reports ready.
- Actual inference is blocked by xAI subscription or permission entitlement.
- Baseline benchmark for current NVIDIA/gpt-oss-120b is recorded.
- Reopen when Rob has a working xAI API key or confirmed API-capable Grok subscription.

## Standard Startup Prompt

```text
Use repo path /mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core.
Read ROB.md, HERMES.md, and WORK.md first.
Then check Linear if the task mentions active work.
Follow xlink-core Rules of Engagement.
Do not change files, config, memory, email, Telegram, calendar, reminders, scheduled tasks, or Linear unless I explicitly approve.
```
