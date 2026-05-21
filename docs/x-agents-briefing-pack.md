# X Agents Briefing Pack

This is the starter briefing pack for Hermes Prime.

It is intentionally conservative. It captures what is known from inspected sources and flags anything that still needs Rob confirmation.

## Core Positioning

X Agents are lifelike voice and video agents that can be added to a website or app so customers can talk, get help, and move a workflow forward when configured.

The key benefit is engagement.

X Agents are not just chatbots. The intended product advantage is a more natural human experience through:

- voice interaction
- video avatar presence
- subject-matter environment
- approved knowledge
- workflow actions when configured

Rob has clarified that the MVP should not be framed as unlimited autonomous AI. At this stage, X Agents are grounded by:

- an internal dataset
- an LLM of choice
- configured tool access
- defined business workflows
- explicit limits on what the agent can claim or do

## Confirmed Product Constraints

From inspected X-LINK agent prompt rules:

- X Agents should answer from approved information.
- X Agents should not guess beyond what is confirmed.
- X Agents should explain integrations conditionally.
- X Agents can often connect to business tools when configured, but exact integrations depend on setup and permissions.
- X Agents should not promise specific systems, scale, compliance, support tiers, or implementation timelines unless confirmed.
- Good safe language includes `guided experience`, `interactive walkthrough`, `user-directed flow when configured`, and `business-tool connection when configured`.

## Product Thesis

The current way humans interact with many AI systems is cumbersome and impersonal.

X Agents aim to make AI interaction feel more natural, approachable, and business-specific by placing a lifelike agent inside an environment that matches the subject matter.

Examples:

- a service advisor inside a virtual shop or service desk
- a legal intake assistant inside a professional legal setting
- a home-service assistant inside a quote or booking flow
- a hospitality concierge inside a reservation environment
- a real estate guide inside a property or community experience

## Known X-LINK Agent Inventory

Source: `C:\AI Fusion Labs\X AGENTS\REPOS\X-LINK\config\agents.yaml`

Inspected agent names and domains:

| Agent | Domain |
| --- | --- |
| Morgan | Field Service Operations |
| Sarah Netic | Home Services |
| Dani | AI Agents and Platform |
| Amy | IT Solutions and Managed Services |
| James | Unknown from summary scan |
| Luke | Unknown from summary scan |
| Claire | Unknown from summary scan |
| Taylor | Unknown from summary scan |
| Michael | Unknown from summary scan |
| Evan Mullins Moving | Moving and Logistics |

These are not just GTM leads. They are evidence that X-LINK already contains domain-specific X Agent personas, prompts, evals, and demo concepts.

## Known Product/Platform Sources

### X-LINK repo / X-LINK Hub

Preferred product truth sources:

- `config/agents.yaml`
- `tools/xagent_eval/*`
- `tools/agent_validation.py`
- `tools/anam_sync.py`
- `tools/hermes_operator.py`
- `tools/hermes_memory.py`
- `hub/index.html`
- `hub/app.js`
- `docs/hermes_atlas_xlink_adoption_blueprint.md`
- `docs/hermes_mel_2_0_architecture.md`
- `docs/hermes_v2026_4_13_xlink_execution_plan.md`

Rob has clarified that X-LINK Hub is more reliable than existing Google Drive files for current product truth. Until direct Hub access is wired in, the X-LINK repo is the best available proxy source.

### ChatGPT Project folder: X Agents

Rob identified his ChatGPT Project folder named `X Agents` as a better or additional source.

Access status:

- Codex cannot directly access Rob's ChatGPT Projects folder from this workspace.
- Hermes should not claim it has inspected that folder unless Rob exports, attaches, pastes, or moves the relevant material into an accessible source.
- Once available, this source should be treated as a high-priority candidate source because it likely contains more current founder context than dated Drive exports.

### Google Drive

Inspected search results from the `aifusionlabs` Drive account included:

- `xagents_index`
- `xagents_index_v2.csv`
- `xagents_index.csv`
- `xagents_index_categorized.csv`
- `0325_x-agents-poc-summary.md`
- `0159_x-agents-mvp-reference-guide.md`
- `0393_x-agents-fake-ted-talk.md`

Downloaded and skimmed for this pass, but treated as dated/historical:

- `0325_x-agents-poc-summary.md`
- `0159_x-agents-mvp-reference-guide.md`
- `xagents_index_v2.csv`

## Source Confidence

| Source | Confidence | Notes |
| --- | --- | --- |
| Rob's direct clarification in this thread | High | Engagement factor and MVP limits are direct operator guidance. |
| ChatGPT Project folder `X Agents` | Not inspected | Likely important, but not directly accessible until Rob exports or shares it. |
| X-LINK `config/agents.yaml` | High | Current repo source for known agent personas and rules. |
| X-LINK eval/tool docs | Medium-high | Strong evidence for product direction and validation system. |
| Drive `0325_x-agents-poc-summary.md` | Low-medium | Historical context only. Existing Drive files are likely dated and require Rob promotion before use as product truth. |
| Drive `0159_x-agents-mvp-reference-guide.md` | Low-medium | Historical context only. Includes broad ideas that may no longer match current X Agents direction. |
| GTM lead scout outputs | Low for product truth | Useful for GTM tests, not product definition. |

## What Hermes Now Knows

Hermes should treat X Agents as a product concept centered on lifelike voice/video AI engagement, not merely generic chat automation.

Hermes should treat the GTM workflow as one operating lane, not the definition of X Agents.

Hermes should use X-LINK Hub as the preferred current product source once connected.

Until X-LINK Hub access is wired, Hermes should use the X-LINK repo as the best available technical/product source.

Hermes should use the aifusionlabs Drive folder as the curated business knowledge home, not as automatic product truth.

## What Hermes Still Does Not Know

Hermes still needs Rob to clarify:

- the official X Agents one-line pitch
- exact current MVP status
- which agent demos are active
- which industries are priority one
- what is customer-ready vs experimental
- what integrations are real today
- what pricing, packaging, and delivery model Rob wants
- whether X Agents is positioned as a platform, service, agency offer, or hybrid
- which Drive files, if any, should be promoted from dated/historical source material to canonical truth

## Rob Clarification Queue

Ask Rob these when ready:

1. What is the official one-sentence X Agents pitch?
2. Which current demo agent best represents the product?
3. What business vertical should be the first serious GTM lane?
4. What can X Agents do today without engineering work?
5. What should Hermes never promise about X Agents?
6. Should the first customer-facing offer be AI receptionist, website video concierge, AI sales assistant, or something else?
7. Which Drive files, if any, should be treated as current?
8. What is the best first X-LINK Hub export or source view for Hermes to learn from?
9. Can Rob export or share the ChatGPT Project folder `X Agents` into the curated Drive workspace?

## Operating Rule

When Hermes is asked about X Agents and does not have a source-backed answer, it should say:

```text
I do not have confirmed X Agents source knowledge for that yet. I can answer as a draft assumption or inspect the X-LINK/Drive source first.
```
