#!/usr/bin/env bash
# ssl_expiry_check.sh - warn when TLS certificates expire soon
# Usage: ssl_expiry_check.sh [-d days] host[:port] [host[:port]...]
# Exit: 0 = all OK, 1 = at least one expiring/expired/unreachable, 2 = bad usage
set -euo pipefail

days=14
if [[ "${1:-}" == "-d" ]]; then
  days="${2:-}"; shift 2 || true
fi
[[ "$days" =~ ^[0-9]+$ && $# -ge 1 ]] || { echo "Usage: $0 [-d days] host[:port]..." >&2; exit 2; }

status=0
now=$(date +%s)
for target in "$@"; do
  host="${target%%:*}"
  port="${target##*:}"
  [[ "$port" == "$target" ]] && port=443
  end=$(echo | timeout 10 openssl s_client -connect "${host}:${port}" -servername "$host" 2>/dev/null \
        | openssl x509 -noout -enddate 2>/dev/null | cut -d= -f2) || true
  if [[ -z "${end:-}" ]]; then
    echo "ERROR ${host}:${port} could not read certificate"
    status=1
    continue
  fi
  left=$(( ( $(date -d "$end" +%s) - now ) / 86400 ))
  if (( left < 0 )); then
    echo "EXPIRED ${host}:${port} on ${end}"
    status=1
  elif (( left <= days )); then
    echo "WARN ${host}:${port} expires in ${left} days (${end})"
    status=1
  else
    echo "OK ${host}:${port} ${left} days left"
  fi
done
exit "$status"
