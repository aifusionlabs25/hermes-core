# Model Benchmark Baseline Summary - 2026-05-19

Provider:
- nvidia

Model:
- openai/gpt-oss-120b

Status:
- Baseline completed before xAI/Grok OAuth was connected.

## Results

| Test | Latency | ASCII | Main result |
|---|---:|---|---|
| Daily Brief v2 | 31.90s | pass | Good structure, but included extra personal anchor content and mixed priorities. |
| Gmail Triage Rules | 12.05s | fail | Used non-ASCII, questionable Himalaya syntax, and wrong credential path style. |
| Capture to Linear Judgment | 22.42s | fail | Forced a stale capture into a Linear issue despite explicit instruction not to. |
| X Agents GTM Planning | 17.85s | fail | Useful plan, but too broad, non-ASCII, and invented unsupported example details. |
| X-LINK Work Order Draft | 18.72s | fail | Useful draft structure, but non-ASCII and invented likely files/systems. |

## Initial Scores

Scores are 1 to 5.

| Category | Score | Notes |
|---|---:|---|
| Instruction following | 2 | Missed key constraints in multiple tests. |
| Tool use | 3 | Oneshot mode worked, but no live tool test was part of this suite. |
| Evidence discipline | 2 | Invented details in GTM and X-LINK drafts. |
| Practical judgment | 3 | Several outputs were directionally useful. |
| Concision | 2 | GTM plan was too broad for the requested first batch plan. |
| Rob usefulness | 3 | Useful enough for drafts, not reliable enough for autonomy. |
| Workflow fit | 2 | Violated Capture-to-Linear and ASCII rules. |
| Speed | 3 | Fast enough for short tasks, slower on Daily Brief v2. |
| Reliability | 2 | Too many rule misses for default-agent trust. |

## Baseline Finding

The current NVIDIA/gpt-oss-120b setup is usable for drafting, but it is not reliable enough to be trusted as the long-term default without mechanical guardrails.

Primary weaknesses:

- Non-ASCII output despite explicit ASCII instruction.
- Weak adherence to stale-capture judgment rules.
- Occasional invented operational details.
- Over-expansion of scoped tasks.

## Grok Benchmark Requirement

After xAI/Grok OAuth is connected, run the same five tests and compare:

- rule following
- ASCII compliance
- evidence discipline
- practical usefulness
- latency
- failure modes

Do not switch the default provider until Grok has been tested against this baseline.
