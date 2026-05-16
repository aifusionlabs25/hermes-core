# Hermes Core Rules

Hermes Core is a standalone operator-core lab.

## Identity

- Profile name: `xlink-core`
- Repo root: `/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core`
- API server: `http://127.0.0.1:8643/v1`

## Rules

- Keep this repo separate from X Link Hub unless Rob explicitly approves a bridge task.
- Inspect before editing.
- Keep replies concise by default.
- Do not create cron jobs, background services, or external integrations without approval.
- Do not change model/provider settings without approval.
- Do not edit files outside this repo without approval.
- Prefer small, reversible changes with tests.

## Approval Required

Ask Rob before:

- touching `X-LINK`
- installing system-level packages
- changing credentials or `.env` files
- deleting files or state
- starting recurring automation
- creating external network integrations
