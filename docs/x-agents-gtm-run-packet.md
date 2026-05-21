# X Agents GTM Run Packet

Status: draft operating format.
Purpose: store GTM work as structured state so Hermes does not depend on a long chat transcript.

## Product Form

Feature name: GTM Run Packet.

Problem: GTM work spans lead sourcing, filtering, inspection, scoring, angle drafting, approval, and follow-up. If all state lives in chat, compression causes drift.

User: Rob and Hermes.

Jobs to be done:
- Keep each GTM run bounded and reviewable.
- Preserve lead facts, source URLs, scores, and approvals.
- Separate raw data from assumptions.
- Make it easy to continue in a fresh Hermes session.

Success criteria:
- A fresh Hermes session can resume from a packet without reading the full prior chat.
- Each lead has source, status, score, and next action.
- Outreach and X-LINK actions stay blocked until Rob approval is recorded.

Non-goals:
- Do not replace a CRM yet.
- Do not send outreach automatically.
- Do not create X-LINK work orders automatically.
- Do not store private personal data.

Risks:
- Bad source data may look cleaner than it is.
- Over-detailed packets may become slow to maintain.
- Manual copy/paste errors can happen until a real database exists.

Required docs:
- docs/x-agents-pilot-offer-playbook.md
- docs/x-agents-pilot-economics-and-sop.md
- docs/x-agents-gtm-ops-workflow.md

Required commands or config:
- Maps skill for sourcing.
- Optional later: Google Sheet or local JSON store.

Approval gates:
- Rob approves outreach copy before sending.
- Rob approves pricing before it is shown to prospects.
- Rob approves Linear issues and X-LINK work orders.

Acceptance tests:
- Packet can represent a 10 to 15 lead scout.
- Packet can identify skipped leads without deleting them.
- Packet can feed the next fresh Hermes session.

## Packet Template

```text
GTM Run Packet

run_id:
date:
operator:
session_health:

target_geography:
radius:
categories:
source_method:
source_limits:

active_constraints:
- ascii_only:
- no_file_write:
- no_outreach:
- no_pricing:
- no_linear:
- no_xlink_work_orders:

raw_leads:
- id:
  business_name:
  category:
  address_or_service_area:
  phone:
  website:
  source_url:
  source_status:
  notes:

filtered_leads:
- id:
  business_name:
  bucket: strong | needs_enrichment | skip
  reason:
  next_validation_step:

website_inspection_results:
- id:
  website_loads: yes | no | blocked | unknown
  phone_visible: yes | no | unknown
  contact_form: yes | no | unknown
  quote_or_request_form: yes | no | unknown
  chat_widget: yes | no | unknown
  inspection_depth: shallow | browser | manual | unknown
  evidence_note:
  caveats:

scoring:
- id:
  x_agents_fit_score: 1-5
  lead_capture_quality: 1-5
  score_reason:
  confidence: high | medium | low

skipped_leads:
- id:
  business_name:
  reason:

outreach_status:
- not_started | internal_angles | draft_ready | approved | sent | paused

rob_approval_status:
- target_list:
- outreach_copy:
- pricing:
- linear:
- xlink_work_orders:

next_action:

xlink_work_order_candidates:
- signal:
  affected_agent_or_workflow:
  proposed_work_order:
  approval_required: yes
```

## GTM Workflow Stages

Stage 1: Source leads.
- Input: geography, radius, categories, source limits.
- Allowed: maps/OSM structured query.
- Blocked: outreach, scoring claims not supported by source.
- Output: raw leads.
- Stop if: maps query errors and no approved fallback exists.

Stage 2: Filter leads.
- Input: raw leads.
- Allowed: bucket leads by website, phone, category, obvious service fit.
- Blocked: website claims, pricing, outreach.
- Output: strong, needs enrichment, skip.
- Stop if: fewer than 3 inspectable leads and Rob wants volume.

Stage 3: Inspect websites.
- Input: strong website-ready leads.
- Allowed: public website fetch/browser inspection.
- Blocked: search engines unless approved, form submission, login/CAPTCHA bypass.
- Output: inspection fields and caveats.
- Stop if: site is blocked or unavailable.

Stage 4: Score fit.
- Input: filtered leads and inspection results.
- Allowed: score 1 to 5 with reasons and confidence.
- Blocked: unsupported assumptions.
- Output: ranked shortlist.
- Stop if: evidence is too weak.

Stage 5: Draft internal angles.
- Input: ranked shortlist.
- Allowed: internal value proposition notes and likely objections.
- Blocked: outreach copy, pricing, external action.
- Output: internal GTM angle notes.
- Stop if: Rob wants a different vertical.

Stage 6: Draft outreach.
- Input: Rob-approved target list and angle.
- Allowed: draft copy only.
- Blocked: sending.
- Output: copy for Rob approval.
- Stop if: pricing or claims are not approved.

Stage 7: Rob approval.
- Input: target list, copy, pricing if any.
- Allowed: Rob approves, rejects, or requests edits.
- Blocked: assuming approval.
- Output: approval status.

Stage 8: Follow-up tracking.
- Input: approved outreach results.
- Allowed: update approved tracker.
- Blocked: CRM/Linear updates unless approved.
- Output: status and next follow-up.

Stage 9: X-LINK feedback loop.
- Input: repeated market signals.
- Allowed: proposed X-LINK work order draft.
- Blocked: official work order creation without Rob approval.
- Output: work order candidates.

## Storage Options

Near term:
- Markdown packet in repo or Drive when Rob approves file creation.
- Google Sheet rows for lead tracking when Rob approves.
- Chat-only output for dry runs.

Later:
- Local SQLite or Honcho-backed memory.
- X-LINK Hub work order integration.
- CRM or campaign tracker.

