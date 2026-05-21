# Hermes Session Health and Handoff

Status: draft operating rule.
Owner: Rob.
Purpose: keep Hermes useful during long operating work without trusting a degraded chat transcript.

## Product Form

Feature name: Session Health and Handoff.

Problem: long Hermes sessions can drift after repeated compression. Drift shows up as forgotten constraints, forced answers, weak source labels, ASCII failures, and mixing old context with new instructions.

User: Rob as approving operator. Hermes as local operator assistant.

Jobs to be done:
- Warn Rob before accuracy degrades.
- Preserve the active task state in a clean handoff.
- Recommend a fresh session before high-risk operational work continues.
- Keep Hermes useful without making it timid.

Success criteria:
- Hermes reports session health when compression appears.
- Hermes does not start new multi-step research from a heavily compressed session unless Rob explicitly approves.
- Hermes can produce a copy-paste handoff that restarts the task cleanly.
- Handoff includes objective, constraints, current results, failures, next action, and what not to do.

Non-goals:
- Do not replace model context limits.
- Do not install Honcho or Docker.
- Do not change provider defaults.
- Do not store secrets or private raw data.

Risks:
- Hermes may over-warn and slow Rob down.
- Handoff summaries may omit details if created too late.
- A fresh session may lose unstored results unless a run packet exists.

Required docs:
- HERMES.md
- docs/x-agents-gtm-run-packet.md
- docs/hermes-memory-architecture.md

Required commands or config:
- None required now.
- Future: optional session-health helper command.

Approval gates:
- Rob approves any new persistent storage, automation, or provider default change.
- Rob approves any outbound outreach, Linear issue creation, or X-LINK work order creation.

Acceptance tests:
- At compression count 5, Hermes warns and offers a handoff.
- At compression count 8, Hermes avoids starting a new multi-step research task unless Rob approves.
- At compression count 10, Hermes produces a handoff and recommends a fresh session.
- Handoff is ASCII-only and copy-paste ready.

## Session Health Levels

Fresh:
- Compression count: 0 to 2.
- Action: normal work is allowed.
- Required language: `Session health: Fresh.`

Caution:
- Compression count: 3 to 5.
- Action: continue, but restate active constraints before multi-step work.
- Required language: `Session health: Caution. I can continue, but I should restate constraints before multi-step work.`

Degraded:
- Compression count: 6 to 9.
- Action: finish the current small step only. Do not begin new multi-step research unless Rob explicitly approves.
- Required language: `Session health: Degraded. I recommend a fresh session before starting a new multi-step task.`

Handoff required:
- Compression count: 10 or more.
- Action: stop new operational work. Produce a handoff. Recommend a fresh session.
- Required language: `Session health: Handoff required. I should not start new operational work from this session.`

If compression count is unknown, Hermes should say:

```text
Session health: Unknown. Compression count was not checked.
```

## Rules

- Do not hide compression risk.
- Do not claim the session is healthy without checking the visible session state or current context.
- Do not use a degraded session to make final GTM, financial, provider, or product-truth decisions.
- Do not rely on chat memory for GTM lead state. Use a GTM run packet.
- If Rob asks to continue anyway, do the smallest next step and label residual risk.
- If a session has repeated failed tool calls, treat it as one level worse.
- If the work involves outreach, CRM, Linear, X-LINK, Drive, Gmail, Calendar, or provider config, prefer a fresh session when degraded.

## Handoff Template

Copy this into a fresh Hermes chat:

```text
Fresh session handoff.

Task objective:
- <what we are trying to finish>

Active constraints:
- <no files / no outreach / no search / ASCII only / source limits / approval gates>

Source facts:
- <facts from checked sources only>

Current results:
- <lead list, scores, inspection results, doc changes, or command results>

Skipped or failed items:
- <timeouts, blocked sites, invalid sources, bad data, failed commands>

Next recommended action:
- <one next step only>

Do not do:
- <things to avoid in the fresh session>

Output requested:
- <exact format Rob wants>
```

## Example GTM Handoff

```text
Fresh session handoff.

Task objective:
- Continue X Agents Pilot GTM lead validation.

Active constraints:
- Use ASCII only.
- Do not save files.
- Do not draft outreach.
- Do not include pricing.
- Do not use Google/Bing/DuckDuckGo.
- Do not create Linear issues or X-LINK work orders.

Source facts:
- Leads came from maps/OSM-derived local scout near ZIP 85045.
- Website inspection was shallow HTML/curl only.

Current results:
- Strong candidates: Penguin Air, Zippity Split Plumbing, All Vee's Plumbing Services, Canyon State Roofing.
- Skipped: Goettl, Faith Technologies.

Skipped or failed items:
- Goettl returned Cloudflare challenge.
- Faith Technologies website looked mismatched/unreachable.

Next recommended action:
- Produce internal-only GTM angle notes for the four strong candidates.

Do not do:
- Do not send outreach.
- Do not create files.
- Do not force a fixed number of leads.

Output requested:
- Table with business, likely pain, X Agents Pilot angle, objection risk, and Rob manual verification item.
```

