# Hermes Core Documentation

Hermes Core is a standalone operator-core lab. Its job is to help experiment with Hermes profiles, memory, skills, tool boundaries, and future bridge patterns without disturbing X Link Hub.

## Operating Model

- Codex acts as mission control and reviewer.
- Hermes Core acts as a fast local operator.
- X Link Hub remains separate until an explicit bridge is designed.

## Current Scope

- Keep the `xlink-core` profile running and understandable.
- Store project notes, scripts, and examples in this repo.
- Avoid repo-local model overrides until needed.
- Avoid cron jobs until the workflow is proven manually.

## Future Work

- Add a status script for the profile and API port.
- Add a bridge design document for future X Link Hub integration.
- Add a small MCP or HTTP client only after the bridge contract is clear.

## Reference Docs

- [Operating model](operating-model.md)
- [Future X Link bridge contract](xlink-bridge-contract.md)
