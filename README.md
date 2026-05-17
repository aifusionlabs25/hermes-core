# Hermes Core

Standalone Hermes operator-core lab for Rob's local agent work.

This repo is separate from `X-LINK`. It can eventually connect to X Link Hub through an explicit bridge, but it should not depend on X Link Hub internals by default.

## Profile

- Hermes profile: `xlink-core`
- WSL profile path: `/home/ai_fusion_labs/.hermes/profiles/xlink-core`
- Workspace cwd: `/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core`
- API server: `http://127.0.0.1:8643/v1`
- Local API key: `xlink-core-local-dev`

The default Hermes profile can run at the same time. The default profile currently uses port `8642`; this profile uses port `8643`.

## Common Commands

```bash
hermes profile list
hermes -p xlink-core chat
hermes -p xlink-core chat -q "Give me a readiness check."
hermes -p xlink-core doctor
hermes -p xlink-core gateway run --accept-hooks
```

## Project Structure

```text
Hermes Core/
  configs/
    example.yaml
  docs/
    email-ops-workflow.md
    index.md
    operating-model.md
    personal-ops-workflow.md
    xlink-bridge-contract.md
  notes/
    inbox.md
  scripts/
    setup_env.sh
  src/
    __init__.py
    main.py
  tests/
    test_main.py
  .gitignore
  HERMES_CORE.md
  README.md
  requirements.txt
  run_hermes_core_gateway.sh
  run_xlink_core_gateway.sh
```

## Boundaries

- Keep this profile's `.env`, memory, sessions, cron jobs, and skills separate from the default Hermes profile.
- Do not reuse the same Telegram, Discord, Slack, WhatsApp, or Signal bot token in multiple running Hermes profiles.
- Do not modify X Link Hub from this repo until a bridge contract exists.
- Keep model settings in the Hermes profile unless there is a specific reason for repo-local overrides.

## Next Direction

The first useful milestone is not a big service. It is a safe operator lab:

1. Document how Hermes Core should behave.
2. Add small scripts for status checks and startup.
3. Add tests that verify the local scaffold works.
4. Define a future bridge contract to X Link Hub before implementing it.

Start with [docs/operating-model.md](docs/operating-model.md) and [docs/xlink-bridge-contract.md](docs/xlink-bridge-contract.md) before giving Hermes broader authority.

For phone-first personal operations, start with [docs/personal-ops-workflow.md](docs/personal-ops-workflow.md). Captured notes should land in [notes/inbox.md](notes/inbox.md).

For Gmail triage, use [docs/email-ops-workflow.md](docs/email-ops-workflow.md). Email starts read-only; sending requires explicit approval.

For a repeatable morning/midday/evening assistant flow, use [docs/daily-operator-routine.md](docs/daily-operator-routine.md).

For terminal basics and avoiding WSL/Hermes prompt confusion, use [docs/hermes-terminal-cheatsheet.md](docs/hermes-terminal-cheatsheet.md).

For the `xlink-core` operating guardrails, use [docs/rules-of-engagement-xlink-core.md](docs/rules-of-engagement-xlink-core.md).

## Health Check

From WSL:

```bash
cd "/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core"
./scripts/check_status.sh
```
