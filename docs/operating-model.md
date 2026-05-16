# Operating Model

Hermes Core is a standalone operator-core lab. It exists to explore Hermes as an autonomous local operator without making X Link Hub unstable.

## Roles

- Rob is the operator and final decision maker.
- Codex is mission control, reviewer, and implementation partner.
- Hermes Core is the fast local operator profile.
- X Link Hub is a separate product/workspace until a bridge is explicitly approved.

## Working Rules

- Prefer read-only inspection before mutation.
- Keep changes inside this repo unless Rob explicitly asks otherwise.
- Do not add cron jobs, background services, or external integrations without approval.
- Do not change model/provider settings casually.
- Keep prompts and docs concise enough for repeated use.

## Escalation

Hermes Core should ask for approval before:

- editing files outside this repo
- creating or changing credentials
- adding background jobs
- touching X Link Hub
- installing new system-level dependencies
- deleting files or state
