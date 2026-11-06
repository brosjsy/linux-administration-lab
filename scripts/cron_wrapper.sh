#!/usr/bin/env bash
# cron_wrapper.sh - run a cron job safely: lock, timeout, timestamped log, exit code
# Usage: cron_wrapper.sh <job_name> <command> [args...]
# Example: cron_wrapper.sh backup /opt/lab/scripts/backup.sh /etc /srv/backups 14
set -euo pipefail

[[ $# -ge 2 ]] || { echo "Usage: $0 <job_name> <command> [args...]" >&2; exit 2; }
job="$1"; shift
[[ "$job" =~ ^[A-Za-z0-9_-]+$ ]] || { echo "job_name: letters, digits, _ and - only" >&2; exit 2; }

log_dir="${CRON_LOG_DIR:-/var/log/lab-cron}"
lock_dir="${CRON_LOCK_DIR:-/run/lock}"
max_runtime="${CRON_TIMEOUT:-3600}"
mkdir -p "$log_dir" 2>/dev/null || log_dir="/tmp"
[[ -w "$lock_dir" ]] || lock_dir="/tmp"
log="${log_dir}/${job}.log"
lock="${lock_dir}/lab-${job}.lock"

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

exec 9>"$lock"
if ! flock -n 9; then
  echo "$(date '+%F %T') SKIP ${job}: previous run still active" >> "$log"
  exit 0
fi

start=$(date +%s)
echo "$(date '+%F %T') START ${job}: $*" >> "$log"
set +e
timeout "$max_runtime" "$@" >> "$log" 2>&1
rc=$?
set -e
dur=$(( $(date +%s) - start ))
if (( rc == 0 )); then
  echo "$(date '+%F %T') OK ${job} (${dur}s)" >> "$log"
elif (( rc == 124 )); then
  echo "$(date '+%F %T') TIMEOUT ${job} after ${max_runtime}s" >> "$log"
  logger -t lab-cron "TIMEOUT ${job}" 2>/dev/null || true
else
  echo "$(date '+%F %T') FAIL ${job} rc=${rc} (${dur}s)" >> "$log"
  logger -t lab-cron "FAIL ${job} rc=${rc}" 2>/dev/null || true
fi
exit "$rc"
