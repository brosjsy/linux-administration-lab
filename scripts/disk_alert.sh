#!/usr/bin/env bash
# disk_alert.sh - warn when a filesystem passes a usage threshold
# Usage: disk_alert.sh [threshold_percent]   (default 85)
# Exit: 0 = all OK, 1 = at least one filesystem over threshold, 2 = bad usage
set -euo pipefail

threshold="${1:-85}"
if ! [[ "$threshold" =~ ^[0-9]+$ ]] || (( threshold < 1 || threshold > 100 )); then
  echo "Usage: $0 [threshold 1-100]" >&2
  exit 2
fi

alert=0
while read -r source pcent target; do
  used="${pcent%\%}"
  if (( used >= threshold )); then
    echo "$(date '+%F %T') ALERT ${target} (${source}) is ${used}% full (threshold ${threshold}%)"
    alert=1
  fi
done < <(df --output=source,pcent,target -x tmpfs -x devtmpfs -x overlay 2>/dev/null | tail -n +2)

if (( alert == 0 )); then
  echo "$(date '+%F %T') OK all filesystems below ${threshold}%"
fi
exit "$alert"
