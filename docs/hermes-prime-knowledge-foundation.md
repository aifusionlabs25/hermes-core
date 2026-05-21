# Hermes Prime Knowledge Foundation

This document defines the first durable knowledge foundation for Hermes Prime and X Agents.

Hermes Prime is the high-judgment operating lane for Rob. Local Hermes remains the lightweight local and Telegram assistant.

## Current Decision

Use the `aifusionlabs` Google Workspace account as the primary business workspace.

Do not use `rvicks` as the primary knowledge base. The `rvicks` account may be used later for backup or redundancy only after Rob explicitly approves that use.

## Primary Drive Workspace

The primary Drive workspace is:

```text
AI FUSION LABS / Hermes Prime / X Agents Knowledge Base
```

Created under the `aifusionlabs` Google Drive account.

Knowledge base folder:

```text
https://drive.google.com/drive/folders/1tL-Vnxko33WEqcQAe9tfwuA_K21w97sS
```

Subfolders:

```text
00_Inbox
01_X_Agents_Briefing_Pack
02_GTM
03_Lead_Lists
04_Call_Notes_Transcripts
05_XLINK_Hub_Exports
06_Daily_Briefs
07_Archive
```

## System Roles

### Google Drive

Drive is the human-readable business knowledge base.

Use Drive for:

- X Agents briefing docs
- founder notes
- strategy docs
- call notes and transcripts
- GTM plans
- lead-list exports
- X-LINK Hub exports
- daily and weekly brief archives

Do not use Drive as raw memory dumping ground. Every document should have a clear purpose and source label.

### Google Sheets

Sheets is the first practical CRM-like layer.

Use Sheets for:

- lead lists
- fit scoring
- campaign status
- outreach approval status
- follow-up stage
- market signal counts
- product feedback loops

Recommended first lead status values:

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

### Hermes Core Repo

Hermes Core stores operating rules and repeatable workflows.

Use Hermes Core for:

- SOPs
- source discipline rules
- prompt templates
- Daily Brief rules
- Linear usage rules
- GTM workflow rules
- model benchmark workflow
- account-slot rules
- X Agents knowledge rules

Do not store secrets, raw inbox contents, raw email bodies, OAuth files, app passwords, or private token files in Hermes Core.

### Linear

Linear is the approved task and execution board.

Use Linear for:

- implementation tasks
- approved GTM tasks
- product follow-up
- bug fixes
- documentation work
- X-LINK work that needs tracking

Do not create Linear issues from vague notes, stale captures, duplicate tests, or raw unreviewed thoughts.

### X-LINK Hub

X-LINK Hub is the future product and work-order source of truth.

Use X-LINK Hub for:

- agent inventory
- live demo status
- eval and validation outputs
- work-order intake
- market-signal-to-product loops
- product readiness views

Until the Hub bridge is connected, Hermes should treat X-LINK repo docs and config as source material, not as a writable operating system.

### Local Database

A local database is not required for this first layer, but it is likely needed later.

Use a local database later for:

- durable state
- dedupe
- audit logs
- lead history
- campaign history
- daily brief history
- tool-run records
- work-order state

Do not build this until the Drive, Sheets, Linear, and X-LINK boundaries are stable.

## Knowledge Rules

Hermes must separate:

- confirmed facts
- source-backed notes
- assumptions
- Rob preferences
- draft strategy
- unknowns

Hermes should cite or name the source type when using knowledge:

```text
Source: Hermes Core doc
Source: X-LINK repo
Source: Google Drive file
Source: Linear snapshot
Source: Rob clarification needed
```

Hermes must say `unknown` when it lacks source-backed knowledge.

Hermes must not treat old ChatGPT memory exports or old Google Drive files as final truth. Rob has warned that existing Drive files are likely dated.

Source priority for X Agents product truth:

1. Rob's current direction.
2. ChatGPT Project folder `X Agents`, after Rob exports or shares the relevant files.
3. X-LINK Hub when available.
4. X-LINK repo docs, config, eval outputs, and current agent definitions.
5. Curated Hermes Core docs.
6. Google Drive files only after they are promoted or explicitly approved.

Drive is useful as a storage and review workspace, but dated Drive files should be treated as historical candidate material until Rob confirms them.

Codex and Hermes cannot directly inspect Rob's ChatGPT Projects folder unless Rob exports, attaches, pastes, or places the source material in an accessible location such as the curated Drive workspace or repo.

## Growth Model

This foundation should support a future company workflow with:

- GTM operations
- lead research
- outreach approval
- customer discovery
- CRM-like tracking
- product feedback loops
- X-LINK work orders
- partner and vendor tracking
- daily executive briefings
- weekly operating reviews
- audit logs

The immediate goal is not a perfect database. The immediate goal is a clean source map, a stable Drive home, and enough operating discipline that Hermes stops searching blind.
