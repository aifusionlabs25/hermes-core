#!/usr/bin/env bash
set -euo pipefail

mkdir -p "$HOME/.hermes/profiles/xlink-core/logs"
exec hermes -p xlink-core gateway run --accept-hooks \
  >> "$HOME/.hermes/profiles/xlink-core/logs/gateway-manual.log" 2>&1
