# X Agents Knowledge Ops

This document defines how Hermes Prime should use Drive, Sheets, Linear, Hermes Core, and X-LINK for X Agents work.

## Principle

X Agents knowledge must be curated, not dumped.

Hermes should not absorb every old note as truth. Existing Google Drive files are likely dated. X-LINK Hub is more reliable for current product truth.

Hermes should build a source-backed briefing pack and mark uncertainty.

## Source Priority

For X Agents product knowledge, use this priority:

1. Rob's current direction.
2. ChatGPT Project folder `X Agents`, after Rob exports or shares it.
3. X-LINK Hub when available.
4. X-LINK repo docs, config, eval outputs, and current agent definitions.
5. Curated Hermes Core docs.
6. Google Drive files only after Rob promotes them or explicitly approves them for use.

Drive is still the primary workspace for curated business knowledge, but old Drive files must be treated as dated/historical until promoted.

Codex and Hermes cannot directly inspect the ChatGPT Projects folder from this environment. Rob must export, attach, paste, or move those materials into Drive or the repo before they can be curated.

## Drive Folder Use

Primary Drive path:

```text
AI FUSION LABS / Hermes Prime / X Agents Knowledge Base
```

Folder use:

| Folder | Use |
| --- | --- |
| `00_Inbox` | Raw source drops waiting for triage. |
| `01_X_Agents_Briefing_Pack` | Canonical or candidate product/business docs. |
| `02_GTM` | Campaign plans, outreach drafts, market notes. |
| `03_Lead_Lists` | CSVs, Sheets, and lead exports. |
| `04_Call_Notes_Transcripts` | Customer discovery, investor, partner, or founder calls. |
| `05_XLINK_Hub_Exports` | Exports from X-LINK Hub, evals, work orders, and product signals. |
| `06_Daily_Briefs` | Daily and weekly operator brief archives. |
| `07_Archive` | Superseded or old files retained for reference. |

## Source Promotion Workflow

1. Find a candidate source.
2. Record file name, location, date if available, and source type.
3. Summarize what it appears to contain.
4. Assign confidence:
   - high
   - medium
   - low
5. Mark whether it is:
   - canonical
   - candidate
   - historical
   - obsolete
   - unknown
6. Ask Rob for clarification if the source makes product claims that affect GTM, pricing, integrations, or customer promises.

If the candidate source is an old Google Drive file, default status should be `historical` unless Rob says otherwise.

## X Agents Briefing Pack Workflow

The briefing pack should answer:

- What are X Agents?
- Why do they matter?
- What problem do they solve?
- What is the engagement advantage?
- What can they do today?
- What are their limits?
- Which demos exist?
- Which verticals matter first?
- What should Hermes never promise?
- What sources support each claim?

## GTM Workflow

GTM research should use the X Agents briefing pack before scoring leads.

Hermes should not score a prospect only because the website lacks chat. It should score fit based on:

- vertical fit
- visible lead intake problem
- public website evidence
- likely value of voice/video engagement
- available contact channel
- source confidence
- alignment with current X Agents capability

## Lead Database Plan

Start with Google Sheets before adding a dedicated CRM.

Recommended columns:

```text
lead_id
business_name
website
source_url
category
address_or_service_area
phone
email_or_contact_form
website_inspection_level
chat_status
lead_capture_notes
x_agents_fit_score
fit_reason
recommended_offer
status
last_touch_date
next_step
approval_status
owner
notes
```

Recommended status values:

```text
researched
qualified
needs Rob review
approved for outreach
outreach drafted
sent
replied
meeting booked
not a fit
nurture
closed
```

Hermes may draft updates. Hermes must not send outreach or modify an external CRM without approval.

## X-LINK Hub Bridge Plan

The bridge should eventually let Hermes:

- read agent inventory
- read demo status
- read eval results
- read product signals
- draft work orders
- link GTM feedback to product improvements

Because X-LINK Hub is the more reliable source for the current X Agents state, connecting this bridge is a priority before making strong product, GTM, or roadmap claims.

Hermes must not create X-LINK work orders without Rob approval.

Proposed work order flow:

1. GTM or eval signal appears.
2. Hermes drafts a proposed work order.
3. Rob approves, rejects, or edits it.
4. Hermes creates or hands off the work order.
5. X-LINK tracks status and result.
6. Hermes summarizes completion back into Drive/Linear.

## Daily Brief Source Map

Daily Briefs should state sources explicitly:

| Source | Include when |
| --- | --- |
| Gmail rob-personal | Rob asks or Daily Brief includes Gmail. |
| Gmail aifusionlabs | Rob asks or Daily Brief includes business inbox. |
| Calendar rvicks | Rob asks or personal schedule is needed. |
| Calendar aifusionlabs | Rob asks or business schedule is needed. |
| Linear | Active work, blockers, and priorities are needed. |
| Hermes Core | Operating rules and current workflow status. |
| Drive knowledge base | X Agents context, GTM docs, and source-backed strategy. |
| X-LINK repo | Product demos, agent definitions, evals, and workbench state. |

Hermes must write `Not checked` for any source it did not inspect in the current request.

## Weekly Operating Review

Recommended weekly review sections:

- Top outcomes
- Open risks
- GTM progress
- X Agents product learnings
- X-LINK work orders proposed
- Lead list changes
- Calendar commitments
- Linear status
- Decisions needed from Rob

## Future Database Layer

Add a database when one of these becomes true:

- lead volume exceeds what Sheets can handle comfortably
- dedupe becomes unreliable
- outreach history needs auditability
- X-LINK work orders need durable cross-system state
- daily briefs need historical trend analysis

Candidate entities:

- sources
- claims
- leads
- campaigns
- contacts
- approvals
- messages
- work_orders
- daily_briefs
- tool_runs

Do not build the database before the knowledge model is stable.
