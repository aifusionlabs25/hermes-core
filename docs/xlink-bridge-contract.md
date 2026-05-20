# Future X Link Bridge Contract

This document is a placeholder for a future bridge between Hermes Core and X Link Hub. No bridge is implemented yet.

## Goal

Let Hermes Core inspect and operate against X Link Hub through a small, explicit surface instead of direct repo/process access.

## First Bridge Mode

The first bridge should be read-only.

Allowed:

- check Hub health
- list recent jobs
- read latest eval summaries
- inspect known artifact paths
- request status from approved endpoints

Blocked:

- patching agent configs
- editing prompts
- starting or stopping production jobs
- sending external messages
- deleting or overwriting artifacts

## Future Action Mode

Action mode should require explicit approval and durable logging.

Candidate actions:

- run a named evaluation
- draft a config patch
- produce a research brief
- summarize a job result
- propose an agent improvement
- draft an X-LINK work order from approved GTM research

## GTM Work Order Mode

GTM work order mode turns market signals into proposed X-LINK work.

Allowed:

- summarize the market signal
- identify the requested capability
- map the likely subsystem
- draft acceptance criteria
- link to approved prospect research
- ask Rob for approval

Blocked without approval:

- creating the work order in X-LINK
- changing X-LINK files
- starting implementation
- exposing sensitive prospect details
- using unreviewed personal notes as product requirements

Work order format:

```text
Proposed X-LINK work order

Source:
- ...

Market signal:
- ...

Requested capability:
- ...

Target subsystem:
- ...

Acceptance criteria:
- ...

Needs Rob approval:
- Yes
```

## Principle

Hermes Core should talk to X Link Hub through APIs or MCP tools with clear permissions. It should not treat the X Link repo as an unbounded filesystem workspace.
