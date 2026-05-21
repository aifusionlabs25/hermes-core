# Honcho Local Memory Evaluation

Status: planned local-only experiment.
Created: 2026-05-21.

## Decision

Evaluate Honcho as a self-hosted durable memory layer for Hermes Prime.

Do not use paid Honcho cloud credits for this phase.

## Why This Matters

Hermes is now useful for supervised read-only operator work, but still has these weaknesses:

- context loss across fresh sessions
- long-session compression degradation
- weak persistent user/project memory
- repeated need to reload source docs
- no durable memory layer for Rob clarifications and operating lessons

Honcho may help by giving Hermes a local memory service that can persist useful conclusions across sessions.

## Local-Only Rule

Use only a local/self-hosted Honcho instance unless Rob explicitly approves a hosted service.

Do not:

- buy Honcho credits
- use Honcho cloud by default
- send raw private archives to Honcho cloud
- store secrets, OAuth codes, API keys, app passwords, or client secrets
- dump raw ChatGPT, Antigravity, Gmail, Calendar, or Drive content into memory

## Intended Role

Honcho should be operational memory, not canonical truth.

Good Honcho candidates:

- Rob preferences
- Rob-confirmed X Agents clarifications
- repeated daily brief preferences
- lessons from failed Hermes runs
- approved GTM decisions
- stable source pointers
- recurring personal/business context Rob explicitly allows

Bad Honcho candidates:

- raw Antigravity brain
- raw ChatGPT archive
- raw Gmail bodies
- raw Calendar data
- secrets or credentials
- speculative model conclusions treated as fact

## System Role Map

- Hermes Core docs: operating rules and curated truth.
- X-LINK Hub: work orders, evals, archives, product operations.
- Google Drive: human-readable business docs and review artifacts.
- Honcho local: durable memory and representations.
- Future local database: audit logs, lead state, campaign history, CRM-like records.

## Current Machine Readiness

Checked from Codex on 2026-05-21:

- `docker --version`: not available.
- `docker compose version`: not available.

Result:

Local Honcho cannot be started from this environment until Docker is installed, exposed to this shell, or an alternate manual PostgreSQL/Redis/Python setup is chosen.

## Minimal Safe Proof

After Docker is available:

1. Clone Honcho locally outside Hermes Core.
2. Start Honcho on localhost only.
3. Use a local or approved OpenAI-compatible model endpoint.
4. Create workspace `hermes-prime`.
5. Create peers:
   - `rob`
   - `hermes`
   - `x-agents`
   - `x-link`
6. Store only 5 to 10 curated facts.
7. Start a fresh Hermes session and test recall.
8. Compare recall against Hermes Core docs.
9. If recall is useful and source discipline remains intact, expand slowly.

## First Test Facts

Use facts like these only after local Honcho is running:

- Rob prefers direct, practical operator briefs.
- X Agents should be described as specialized voice/video AI workers, not generic chatbots.
- X Agents pricing is not confirmed.
- Customer-ready demo list is not confirmed.
- X-LINK Hub should be treated as the future product/work-order coordination layer.
- Raw archives are evidence, not truth.

## Acceptance Criteria

Honcho is worth continuing only if:

- local service starts without cloud credits
- Hermes can write curated memory
- Hermes can recall that memory in a fresh session
- Hermes labels memory as memory, not source truth
- no secrets or raw private archives are stored
- memory improves brief quality without increasing overclaiming

## Recommended Next Step

Install or expose Docker, then run the minimal safe proof.

If Docker is not desired, evaluate a manual setup with PostgreSQL plus pgvector, Redis if needed, and the Honcho Python server.
