#!/usr/bin/env bash
# service_watchdog.sh - restart listed systemd services that are not active
# Usage: service_watchdog.sh nginx ssh cron ...
set -euo pipefail

[[ $# -ge 1 ]] || { echo "Usage: $0 <service> [service...]" >&2; exit 2; }
logfile="${WATCHDOG_LOG:-/var/log/service_watchdog.log}"
log() { echo "$(date '+%F %T') $*" | tee -a "$logfile" 2>/dev/null || echo "$(date '+%F %T') $*"; }

status=0
for svc in "$@"; do
  if systemctl is-active --quiet "$svc"; then
    log "OK $svc is active"
  else
    log "WARN $svc is not active, restarting"
    if systemctl restart "$svc" && systemctl is-active --quiet "$svc"; then
      log "FIXED $svc restarted"
    else
      log "FAIL $svc could not be restarted, escalate"
      status=1
    fi
  fi
done
exit "$status"
