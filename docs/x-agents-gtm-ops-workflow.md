# X Agents GTM Ops Workflow

This workflow defines how Hermes should help Rob research, plan, and operate go-to-market work for X Agents.

The goal is to let Hermes run a useful sales and marketing operating lane while Rob keeps approval over messaging, targets, outbound contact, CRM updates, and X-LINK work orders.

## North Star

Hermes should help Rob turn public market research into qualified opportunities, practical outreach, and product feedback loops.

Hermes should be able to:

- find local business prospects
- inspect public websites
- identify whether a business appears to use chat, live chat, or AI chat
- summarize the business and likely pain points
- score fit for X Agents
- draft a GTM plan
- draft outreach copy
- propose CRM follow-up steps
- propose X-LINK work orders based on real market signals

Hermes must not send messages, scrape private data, or modify CRM/Linear/X-LINK without Rob approval.

## Default Authority

Allowed without separate approval when Rob asks for GTM research:

- search public web sources
- inspect public business websites
- summarize public business information
- identify public contact channels
- classify lead fit
- draft outreach copy
- draft follow-up plans
- draft proposed Linear issues or X-LINK work orders
- produce CSV, Markdown, or table drafts

Blocked without explicit approval:

- send emails, texts, social messages, or form submissions
- call businesses
- create or update CRM records
- create or update Linear issues
- create or modify X-LINK work orders
- store sensitive personal details
- bypass website terms, paywalls, logins, CAPTCHAs, or rate limits
- collect non-public personal data

## Workflow 1: Local Lead Scout

Use this when Rob asks for prospects in a local market.

Example prompt:

```text
Find 10 blue-collar trade businesses within 10 miles of 85045 that have websites. Public web only. For each, summarize the business, website quality, whether they appear to have chat/live chat/AI chat, contact details, and one X Agents outreach angle. Save no files yet. Report sources.
```

Inputs:

- ZIP code or city
- radius
- target industries
- maximum number of leads
- output format
- whether to save results

Target industries:

- HVAC
- plumbing
- electrical
- roofing
- landscaping
- pest control
- pool service
- garage door
- locksmith
- auto repair
- home remodeling
- restoration and remediation
- other blue-collar trade businesses Rob specifies

Lead fields:

- business name
- website
- source URLs
- address or service area
- phone
- email or contact form URL, if public
- business description
- services offered
- website quality score
- chat/live chat/AI chat status
- apparent lead capture quality
- likely missed opportunities
- X Agents fit score
- recommended offer angle
- suggested first outreach
- confidence level
- notes and caveats

Fit score:

- 5: strong fit, clear lead intake problem or weak website conversion
- 4: good fit, likely benefits from AI receptionist/chat/follow-up
- 3: possible fit, needs more validation
- 2: weak fit, limited evidence
- 1: poor fit or not relevant

### Local Search Data Source Order

Do not start Local Lead Scout by driving a browser through Google, Bing, or DuckDuckGo search result pages. Those pages often block automated browsers and waste the run.

Use this source order instead:

1. Structured local data provider: use the Hermes `maps` skill / OpenStreetMap / Overpass path first for local business discovery when available.
2. Direct public business websites: inspect the business website for services, phone, contact form, chat status, and lead-capture quality.
3. Public directory pages: use public directory pages only when they are accessible without login, CAPTCHA, paywall, or terms bypass.
4. Browser search engine pages: use raw browser search only as a last resort.

If structured search and public directories are unavailable, stop and say exactly which source failed. Do not invent businesses or fill unknown fields from guesses.

For 85045 / Ahwatukee style searches, use structured queries like:

```text
python3 ~/.hermes/skills/maps/scripts/maps_client.py nearby --near "85045 Arizona" --category plumber --category electrician --category hvac --category roofer --category landscaper --radius 16093 --limit 20
```

Do not hand-roll raw Overpass `curl` queries for Local Lead Scout unless the maps helper script is missing or broken. Do not use hard-coded coordinates for ZIP searches. In particular, do not use `33.4484,-112.0740` for 85045; that is downtown Phoenix, not the 85045 / Ahwatukee search center.

Then inspect the returned websites and public source URLs before scoring a lead.

When a structured source provides only partial data, mark fields as `unknown` rather than guessing.

For website inspection, separate shallow checks from real review:

- If Hermes only fetched headers, first lines, or a partial HTML response, mark `website inspection` as `shallow`.
- Do not claim Cloudflare blocking unless the fetched content clearly shows a Cloudflare challenge or block page.
- Do not claim `no chat`, weak lead capture, or a website quality score unless Hermes inspected enough page content to support it.
- If page content cannot be inspected, use `unknown` for website quality, chat status, lead-capture quality, and missed opportunities.

## Workflow 2: Website AI Readiness Review

Use this when Rob wants to understand how a prospect website performs.

Hermes should inspect:

- homepage clarity
- services page
- contact page
- booking or quote flow
- mobile friendliness if browser tools are available
- visible phone number
- visible contact form
- chat/live chat/AI chat widget
- trust signals such as reviews, licenses, galleries, or badges
- missing conversion opportunities

Output:

```text
Website AI readiness review

Business:
- ...

Website:
- ...

What they do:
- ...

Lead capture:
- ...

Chat status:
- none found / live chat / AI chat / unclear

Conversion gaps:
- ...

X Agents opportunity:
- ...

Recommended offer:
- ...

Confidence:
- ...

Sources:
- ...
```

## Workflow 3: GTM Campaign Builder

Use this after a lead list or target niche exists.

Hermes should draft:

- target segment
- pain hypothesis
- X Agents offer
- positioning
- objections
- proof needed
- outreach sequence
- follow-up sequence
- A/B variants
- success metrics
- approval points

Campaign format:

```text
GTM campaign draft

Segment:
- ...

Pain hypothesis:
- ...

Offer:
- ...

Messaging angle:
- ...

Outreach sequence:
1. ...
2. ...
3. ...

A/B test:
- Variant A: ...
- Variant B: ...

Metrics:
- reply rate
- booked call rate
- demo interest
- objections
- qualified opportunities

Needs Rob approval:
- target list
- final copy
- send channel
- follow-up cadence
```

## Workflow 4: CRM Follow-Up Loop

Hermes can manage CRM-like activity as a draft-first workflow.

Stage 1 storage options:

- Markdown table
- CSV
- Google Sheet
- Linear project

Stage 2 possible CRM tools:

- HubSpot
- Pipedrive
- Airtable
- Notion
- Google Sheets

Recommended starting point:

- Use Google Sheets or CSV for lead data.
- Use Linear only for campaign tasks, product work, and follow-up commitments.
- Add a dedicated CRM later if outreach volume grows.

Lead status values:

- researched
- qualified
- needs Rob review
- approved for outreach
- outreach drafted
- sent
- replied
- meeting booked
- not a fit
- nurture
- closed

Hermes may draft CRM updates, but must not write them unless Rob approves the target system and update.

## Workflow 5: A/B Testing

Hermes may design A/B tests for copy, offers, landing pages, and follow-up sequences.

Hermes should define:

- test goal
- audience
- variants
- send volume
- success metric
- duration
- decision rule
- risk or caveat

Hermes must not launch a test or send outreach without approval.

## Workflow 6: GTM to X-LINK Work Orders

Use this when market research reveals product or agent opportunities.

Examples:

- prospects need missed-call follow-up
- websites lack quote intake
- trade businesses need after-hours response
- leads ask for SMS follow-up
- repeated objection suggests a demo asset is missing

Proposed work order format:

```text
Proposed X-LINK work order

Source:
- GTM research / prospect call / email reply / website review

Target repo:
- X-LINK

Target subsystem:
- agent workflow / tools / hub / evaluation / docs / unknown

Market signal:
- ...

Requested capability:
- ...

Why it matters:
- ...

Likely files or systems:
- ...

Acceptance criteria:
- ...

Needs Rob approval:
- Yes
```

Do not create or send the work order without Rob approval.

## Tooling Roadmap

Strong fits for this workflow:

- Web search
- Browser automation
- Screenshot capture
- Spreadsheet output
- Google Drive/Sheets
- Gmail drafts
- Google Calendar for booked calls
- Linear for campaign tasks and product work
- GitHub for implementation branches
- X-LINK bridge for work orders

Optional later:

- HubSpot or Pipedrive for CRM
- Apollo or Clay for enrichment
- Twilio or Google Voice for call/SMS workflows
- Analytics or UTM tracking for campaign measurement

## Recommended First Build

Build this in layers:

1. Local Lead Scout, public web only, no saved files.
2. Save lead lists to CSV or Google Sheet after Rob approval.
3. Draft GTM campaign and outreach sequences.
4. Track follow-up status in a simple CRM table.
5. Convert repeated market signals into proposed X-LINK work orders.
6. Add approved outbound sending only after the review loop is reliable.
