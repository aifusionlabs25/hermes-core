#!/usr/bin/env bash
# capture_to_inbox.sh - Append a Telegram "Capture:" note to the repo inbox.
# Arguments:
#   $1 = raw note text (required)
#   $2 = optional lane tag (e.g., "Task", "Idea") - leave empty for none
#   $3 = optional source (default: Telegram)

set -euo pipefail

RAW="${1}"
LANE="${2:-}"
SRC="${3:-Telegram}"
TS=$(date '+%Y-%m-%d %H:%M')
INBOX="/mnt/c/AI Fusion Labs/X AGENTS/REPOS/Hermes Core/notes/inbox.md"

if [[ ! -f "$INBOX" ]]; then
  echo "ERROR: Inbox file not found: $INBOX" >&2
  exit 1
fi

# Append entry using the repo's template format.
{
  echo "### $TS - $SRC"
  echo ""
  echo "- Raw note: $RAW"
  echo "- Lane: $LANE"
  echo "- Suggested next action:"
  echo "- Status: captured"
  echo ""
} >> "$INBOX"

echo "Captured to inbox at $INBOX"
