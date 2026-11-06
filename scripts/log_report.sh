#!/usr/bin/env bash
# log_report.sh - security and error summary from the journal
# Usage: log_report.sh [since]   e.g. "24 hours ago" (default), "today"
set -euo pipefail

since="${1:-24 hours ago}"

if ! command -v journalctl >/dev/null 2>&1; then
  echo "journalctl not available" >&2
  exit 1
fi

echo "Log report since: $since"

echo
echo "== Failed SSH logins by source IP =="
journalctl --since "$since" -t sshd -t sshd-session 2>/dev/null \
  | grep -E "Failed password|Invalid user" \
  | grep -oE "from [0-9a-fA-F:.]+" | awk '{print $2}' \
  | sort | uniq -c | sort -rn | head -10 || echo "none"

echo
echo "== sudo commands =="
journalctl --since "$since" -t sudo 2>/dev/null | grep "COMMAND=" | tail -10 || echo "none"

echo
echo "== Error-level messages by unit =="
journalctl --since "$since" -p err -o json 2>/dev/null \
  | grep -oE '"_SYSTEMD_UNIT":"[^"]+"' | cut -d'"' -f4 \
  | sort | uniq -c | sort -rn | head -10 || echo "none"
