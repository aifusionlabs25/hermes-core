#!/usr/bin/env bash
set -euo pipefail

ROOT="/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core"

echo "Hermes Core status"
echo "root: $ROOT"
echo

if [[ ! -d "$ROOT" ]]; then
  echo "missing repo root"
  exit 1
fi

echo "profiles:"
hermes profile list
echo

python3 - <<'PY'
import socket

for name, port in [("default", 8642), ("xlink-core", 8643)]:
    sock = socket.socket()
    sock.settimeout(1)
    try:
        sock.connect(("127.0.0.1", port))
        print(f"{name} api: open on {port}")
    except OSError:
        print(f"{name} api: closed on {port}")
    finally:
        sock.close()
PY

echo
echo "repo:"
git -C "$ROOT" status --short --branch
