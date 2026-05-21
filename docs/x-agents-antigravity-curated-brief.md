# X Agents Antigravity Curated Brief

Status: first-pass curated evidence.
Source: Antigravity brain index generated from `C:\Users\AI Fusion Labs\.gemini\antigravity\brain`.
Generated: 2026-05-21.

This brief promotes the highest-signal Antigravity evidence into a usable Hermes Prime reference. It is not final truth. Treat these notes as historical source material that must be checked against Rob's current direction and current repo state before implementation.

## Source Files Reviewed

Primary files sampled:

- `25716b26-b0e4-4095-8a95-9dada4eb9e34\repo_audit.md.resolved.0`
- `25716b26-b0e4-4095-8a95-9dada4eb9e34\implementation_plan.md.resolved.0`
- `68d014ba-3f72-4183-95eb-e59f8f45be21\01_PRD_xagents_memory_orchestrator.md.resolved.0`
- `68d014ba-3f72-4183-95eb-e59f8f45be21\02_ARCHITECTURE_xagents_memory_orchestrator.md.resolved.0`
- `91e45c3f-c7ef-43c7-863a-3b0286116683\X_AGENT_FACTORY_GENESIS_TRANSFER.md.resolved.3`
- `911b9bca-c7eb-4ecb-8827-426ca99012da\implementation_plan.md.resolved.7`
- `68d014ba-3f72-4183-95eb-e59f8f45be21\06_IMPLEMENTATION_PLAN_usage_auditor.md.resolved.17`
- `3d927456-5217-4748-a853-2955fd6fa720\deployment_notes_for_nova.md.resolved.5`

## Core Product Thesis

Antigravity evidence consistently frames X Agents as interactive, specialized AI workers, not simple chatbot widgets.

Historical product pattern:

- The agent is the interface.
- Video or voice presence is central to the experience.
- The surrounding UI supports the agent with context, controls, proof, and workflow surfaces.
- The product direction favors reusable agent shells that can be specialized by vertical, persona, knowledge base, handoff rules, and GTM context.

Important historical phrase:

- "Website with a chatbot" was rejected in favor of "Agent as the Interface."

Current confidence:

- High as historical design intent.
- Medium as current implementation truth until checked against active X-LINK Hub and current X Agents repos.

## X Agent Factory Concept

Antigravity contains an early "X Agent Factory" concept seeded from the Morgan/Tavus pilot.

Factory objective:

- Create a scalable way to generate specialized AI agents rapidly from reusable patterns.

Factory loop:

1. Build an agent.
2. Collect interaction data.
3. Refine the shared brain and templates.
4. Propose better agents and verticals.

Factory lessons:

- Each agent needs a clear persona, job, offer, and knowledge layer.
- Every agent needs a demo or narration guide that explains what the user is seeing.
- Access control, environment variables, and provider setup must be standardized.
- New agents should be generated from templates, not one-off rebuilds.

Current confidence:

- High as strategy.
- Medium as implementation status.

## Website / Demo Architecture Evidence

The Antigravity repo audit says `x-agent-website-a` was a Next.js App Router showcase platform hosting multiple X Agents through dynamic slug routing.

Important architecture patterns:

- One shared video/WebRTC engine.
- One agent registry.
- Agent routes generated from config.
- Demo pages mount the shared player.
- API route exchanges provider credentials for a session token.
- Transcript route saves sessions, runs lead analysis, and sends follow-up emails.
- Persona behavior was configured in the provider dashboard, not in the codebase.

Reusable components called out:

- `AnamPlayer.tsx` as the core reusable engine.
- `anam-token` API route as a generic token proxy.
- `save-transcript` as partially reusable, but brand/email coupled.
- Lead extraction service as useful but agent-name coupled.
- Sanitization utility as reusable.
- Maintenance middleware as reusable.

Current confidence:

- High for historical repo architecture.
- Must be checked against the current active repos before changing code.

## GTM Vertical Build Direction

The `x-agent-website-b` plan frames the next architecture as a config-driven vertical-build repo.

Key intended upgrades:

- Provider isolation.
- Shared agent shell logic.
- Vertical configs.
- Agent registry that loads verticals by slug.
- Handoff summary generation.
- Shared qualification logic.
- Shared fallback behavior.
- Health check route.
- KB layering.

Suggested vertical examples:

- Home services.
- Pest control.
- Law intake.
- Medspa.

Reusable knowledge-base layers:

- Tone and behavior.
- Qualification logic.
- Greeting logic.
- CTA and handoff.
- Fallback behavior.

Current confidence:

- High as a sensible product architecture direction.
- Medium as current roadmap unless Rob confirms.

## GTM Site / Offer Evidence

The beta launch plan aimed to turn the showcase site into a conversion-focused beta platform.

Planned sections:

- Hero.
- How it works.
- Pricing.
- Testimonials.
- FAQ.
- Beta signup.

Planned offer framing:

- "Deploy Lifelike AI Agents for Smarter Sales & Ops."
- Zero hallucinations.
- Easy integrations.
- Real-time voice and video.
- Sales and operations automation for SMBs.

Pricing was explicitly marked as requiring Rob confirmation. Do not treat old pricing as final.

Current confidence:

- Medium for offer direction.
- Low for pricing and package details until Rob confirms.

## Memory / Knowledge System Evidence

The X Agents Memory Orchestrator material is extremely relevant to Hermes Prime.

Problem identified:

- The main operational risk was loss of project knowledge between sessions, not only code quality.

Proposed memory layers:

1. Raw archive.
2. Structured summaries.
3. Current state.
4. Audit and reconciliation.

Design principles:

- Local-first.
- File-based.
- Git-trackable.
- Human-readable.
- Machine-readable.
- Idempotent workflows.
- Raw source separated from structured extraction and current state.

This maps strongly to the current Hermes Prime direction:

- ChatGPT Project archive equals raw source.
- Antigravity source index equals raw evidence index.
- Curated Hermes docs equal current operating knowledge.
- X-LINK Hub should become product/work-order source of truth.

Current confidence:

- High as architectural guidance for Hermes Prime.

## X-LINK / Sloane Operations Evidence

Usage auditor notes describe a broader X-LINK operating-assistant direction.

Capabilities mentioned:

- SaaS and API usage monitoring.
- Browser tab recovery.
- Morning notifications.
- Security-handshake alerts when login or MFA blocks automation.
- Discord command pivot.
- Resend email notifications.
- Inbox command handling.
- Tab hygiene.
- Audit dashboard.

This is useful as historical ambition for X-LINK, but it should not be treated as current implementation truth.

Current confidence:

- Medium as product direction.
- Low as current operational capability until checked in X-LINK.

## Deployment / Provider Lessons

Deployment notes for Dani and related agents captured several practical rules.

Provider and runtime rules:

- Copy `.env.example` to `.env.local`; Next.js does not load `.env.example`.
- Real provider IDs are required; placeholder persona or replica IDs break demos.
- Tavus conversational flow settings were dashboard-configured, not runtime payload fields.
- Browser autoplay can block first spoken audio unless the user interacts first.
- Testing WebRTC over LAN IP without HTTPS can block microphone access.
- Use `localhost` or HTTPS tunnel for microphone testing.
- Avoid passing `replica_id` when provider persona already has a default visual avatar.
- Use document tags and retrieval strategy to prevent KB cross-contamination.

These are high-value SOP lessons for future X Agent demos.

Current confidence:

- High as historical deployment lessons.
- Provider-specific details must be checked against current provider choice.

## What Hermes Prime Should Know Now

Hermes Prime can safely know:

- X Agents are intended to be specialized AI workers with agent-first interfaces.
- The product evolved through Tavus, Anam, Dani, Amy, Claire, Nova, Sloane, and X-LINK experiments.
- The strongest architecture direction is reusable shells plus vertical configs plus curated KB layers.
- GTM work should connect lead research, qualification, outreach drafts, and product feedback loops.
- Memory and source curation are core infrastructure, not side chores.
- X-LINK Hub is the best candidate for operational work orders and product-system coordination.

Hermes Prime should not assume:

- Old provider choices are current.
- Old pricing is final.
- Old agent counts are current.
- Old repo names are still active.
- Sloane/Nova/Alpha roles are current without Rob confirmation.
- Antigravity task snapshots represent completed work.

## Needs Rob Clarification

- Which X Agents are currently active, paused, or retired?
- Which provider is primary now: Anam, Tavus, another provider, or mixed?
- What are the current repos that define the product truth?
- Is `x-agent-website-b` still the desired vertical factory path?
- What is the current package/pricing model?
- Should X Agents target SMB home services first, or another vertical?
- Should Sloane remain a product/operator persona, or is Hermes Prime absorbing that role?
- Which historical agents matter most: Morgan, Dani, Amy, Claire, Sloane, Nova?

## Recommended Next Action

Create or update the main X Agents Briefing Pack using this brief plus:

- Current X-LINK Hub docs.
- Current active X Agents repos.
- Clean ChatGPT X Agents project archive.
- Rob's clarification on active agents and GTM vertical priority.

Do not ingest more Antigravity files until this first-pass brief is reviewed against current repo truth.
