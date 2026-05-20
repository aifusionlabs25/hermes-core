# Model Benchmark Workflow

This workflow defines how Rob, Codex, and Hermes should compare model providers before changing the default Hermes model.

The immediate comparison is:

- Current xlink-core setup: NVIDIA provider using `openai/gpt-oss-120b`
- Candidate setup: xAI Grok through Hermes `xai-oauth` or xAI API key

## Goal

Choose models by evidence, not vibes.

Hermes should use the model that best handles Rob's real workflows:

- Daily Brief v2
- Gmail triage
- Calendar-aware planning
- Linear next-action planning
- Capture to Linear judgment
- X Agents GTM research and campaign planning
- X-LINK work-order drafting
- tool and rule following

## Current Baseline

As of this workflow:

- xlink-core default provider: `nvidia`
- xlink-core default model: `openai/gpt-oss-120b`
- xAI/Grok provider: supported after Hermes update to v0.14.0
- xAI OAuth/API status: pending Rob browser login callback
- Baseline summary: [model-benchmark-baseline-summary-2026-05-19.md](model-benchmark-baseline-summary-2026-05-19.md)

## Evaluation Principles

Do not switch the default model until the candidate is tested.

Use the same prompts for each model.

Record:

- model/provider
- prompt
- start time
- end time
- latency
- whether tools were used correctly
- whether instructions were followed
- whether output was ASCII-clean when required
- factuality and evidence quality
- usefulness to Rob
- cost or quota concern
- failure mode

## Scorecard

Use a 1 to 5 score for each category:

- Instruction following
- Tool use
- Evidence discipline
- Practical judgment
- Concision
- Rob usefulness
- Workflow fit
- Speed
- Reliability

Recommended decision:

- Keep current model if Grok is not clearly better.
- Use Grok selectively if it wins specific lanes.
- Switch default only if Grok is clearly better across daily operations and tool use.

## Test Set

### Test 1: Daily Brief v2

```text
Give me a Daily Brief v2 using loaded context only. Do not check Gmail or Calendar. Use ASCII only. Include Sources and Needs Rob approval.
```

Expected:

- Source ledger included.
- Gmail and Calendar are `Not checked`.
- Linear is `Snapshot used` if using WORK.md.
- No unsupported source such as Contacts is invented.
- No fake claim such as `No security alerts detected`.

### Test 2: Gmail Triage Rules

```text
Tell me how you would safely triage rob-personal Gmail. Do not run commands. Use ASCII only.
```

Expected:

- Uses `--account rob-personal`.
- Mentions read-only default.
- Does not ask for password before diagnosing context.
- Does not include unrelated Daily Brief sections.

### Test 3: Capture to Linear Judgment

```text
Triage inbox and suggest Linear issues. Do not create them yet. Do not force stale captures, tests, duplicates, handled notes, or vague ideas into issues.
```

Expected:

- Recommends no issue for weak captures.
- Drafts issue only for concrete work.
- Asks approval before creation.

### Test 4: X Agents GTM Planning

```text
Draft a Local Lead Scout plan for 10 blue-collar trade businesses within 10 miles of 85045. Public web only. Do not save files, send outreach, create Linear issues, or create X-LINK work orders. Show lead fields, scoring method, and first batch plan.
```

Expected:

- Uses GTM workflow.
- Does not send or save.
- Defines fields, scoring, and source requirements.
- Keeps public-data boundaries.

### Test 5: X-LINK Work Order Draft

```text
Using a hypothetical market signal that HVAC companies miss after-hours leads, draft a proposed X-LINK work order. Do not create it.
```

Expected:

- Uses proposed work-order format.
- Includes source, market signal, requested capability, subsystem, acceptance criteria, and approval needed.
- Does not start implementation.

## Candidate Model Roles

Possible roles after testing:

- default Hermes operator model
- GTM research model
- writing and messaging model
- coding/work-order model
- second-opinion reviewer
- long-context research model

## Setup Notes

xAI/Grok can be tested two ways:

1. `xai-oauth`, using Rob's eligible Grok subscription through Hermes auth.
2. xAI API key, if OAuth is unavailable or returns authorization errors.

Do not store secrets in this repo.

Do not commit auth files.

## Decision Record Format

```text
Model benchmark decision

Date:
- ...

Models tested:
- ...

Winner by workflow:
- Daily Brief:
- Gmail triage:
- GTM planning:
- X-LINK work order:
- Overall:

Recommendation:
- ...

Risks:
- ...

Next step:
- ...
```
