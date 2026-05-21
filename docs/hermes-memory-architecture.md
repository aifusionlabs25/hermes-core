# Hermes Memory Architecture

Status: draft architecture plan.
Purpose: keep Hermes grounded without installing Honcho or Docker now.

## Product Form

Feature name: Hermes Memory Architecture.

Problem: Hermes needs durable business knowledge and task state, but a single chat transcript is not a reliable database.

User: Rob, Hermes, Codex as Hermes Prime.

Jobs to be done:
- Keep stable operating rules easy to load.
- Keep X Agents product truth source-backed.
- Keep GTM run state recoverable across sessions.
- Avoid dumping stale Drive or chat memory into truth.
- Leave a future path to Honcho or another local memory database.

Success criteria:
- Hermes can answer "what source supports this?".
- Hermes can continue GTM from a run packet.
- Rob can review knowledge in human-readable docs.
- Provider/model defaults stay explicit.
- Memory can grow without turning every chat into permanent truth.

Non-goals:
- Do not install Docker.
- Do not install Honcho now.
- Do not build a full CRM now.
- Do not make Hermes autonomous for outreach.
- Do not treat old Google Drive files as current truth without Rob approval.

Risks:
- Docs can become stale.
- Google Drive can become messy again.
- Sheets can drift from repo docs.
- Memory retrieval can surface old assumptions if not labeled.

Required docs:
- HERMES.md
- ROB.md
- WORK.md
- docs/x-agents-briefing-pack.md
- docs/x-agents-gtm-run-packet.md
- docs/hermes-session-health-and-handoff.md

Required commands or config:
- None now.
- Later: approved Google Drive folder and Sheets lead tracker.
- Later: Honcho/local database if Rob approves Docker or a non-Docker memory option.

Approval gates:
- Rob approves what becomes authoritative product truth.
- Rob approves creating or updating Drive/Sheets.
- Rob approves any memory/database installation.

Acceptance tests:
- A fresh Hermes session can load the docs index and know where GTM packets live.
- A GTM run can be resumed from a packet without prior chat.
- Hermes can distinguish confirmed facts from assumptions.

## Near-Term No-Docker Memory Layer

Use this stack now:

1. Hermes Core docs
   - Operating rules, SOPs, prompts, model/provider notes, session health, and GTM packet format.
   - Best for rules that should survive chat.

2. X-LINK repo and X-LINK Hub
   - Product truth and work-order truth.
   - X-LINK Hub becomes preferred once wired.

3. Google Drive knowledge folder
   - Human-readable business knowledge, briefing docs, strategy docs, call notes, transcripts, and curated exports.
   - Primary account: aifusionlabs.
   - Do not use cluttered Drive root as the knowledge base.

4. Google Sheets lead tracker
   - Structured GTM leads, scores, outreach approval status, campaign status, and follow-up dates.
   - Use only after Rob approves the tracker.

5. GTM run packets
   - Lightweight state object for each sourcing/scoring/inspection run.
   - Can start as chat output and later be saved to Markdown, JSON, or Sheets.

6. Linear
   - Approved implementation tasks, follow-up work, and GTM ops tasks.
   - Not for raw unreviewed leads.

## What Honcho Would Help With

Honcho or a similar memory database could help with:
- Durable user and project memory.
- Retrieval across sessions.
- Remembering decisions, preferences, lead history, and objections.
- Reducing dependence on long chat transcripts.
- Supporting agent-like continuity.

Honcho would not automatically fix:
- Context window limits.
- Long single-session compression.
- Bad tool loops.
- Unsupported claims.
- ASCII failures.
- xAI entitlement blockers.
- Poor workflow design.

## Future Upgrade Path

Phase 1: Docs and packets.
- Add session health rules.
- Add GTM run packet.
- Keep X Agents truth source-backed.

Phase 2: Sheets and Drive.
- Create a clean aifusionlabs Drive knowledge folder.
- Create or approve a Google Sheet lead tracker.
- Store only curated, reviewable records.

Phase 3: Local database.
- Add SQLite or similar local operational state.
- Track lead dedupe, scores, status, outreach approvals, and work-order candidates.

Phase 4: Honcho or memory service.
- Revisit Honcho when Docker or a non-Docker deployment is acceptable.
- Use it for retrieval and durable memory, not as a replacement for workflow packets.

Phase 5: X-LINK Hub integration.
- Promote repeated GTM market signals into proposed X-LINK work orders.
- Create official work orders only after Rob approval.

## Operating Principle

Do not ask Hermes to remember everything from chat. Give Hermes small, source-backed artifacts it can reload.

