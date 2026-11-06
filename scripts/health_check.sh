#!/usr/bin/env bash
# health_check.sh - one-shot server health report
set -euo pipefail

section() { printf '\n==== %s ====\n' "$1"; }

section "Host"
echo "Hostname : $(hostname)"
echo "OS       : $(grep -m1 PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '"')"
echo "Kernel   : $(uname -r)"
echo "Uptime   : $(uptime -p 2>/dev/null || uptime)"

section "Load (cores: $(nproc))"
cat /proc/loadavg

section "Memory"
free -h

section "Disk usage"
df -hT -x tmpfs -x devtmpfs 2>/dev/null || df -h

section "Inodes"
df -i -x tmpfs -x devtmpfs 2>/dev/null | awk 'NR==1 || $5+0 > 50' || true

section "Failed systemd units"
if command -v systemctl >/dev/null 2>&1 && [[ -d /run/systemd/system ]]; then
  systemctl --failed --no-legend || true
else
  echo "systemd not running here"
fi

section "Listening ports"
if command -v ss >/dev/null 2>&1; then
  ss -tulpn 2>/dev/null | head -20
else
  echo "ss not installed"
fi

section "Top 5 processes by CPU"
ps -eo pid,user,%cpu,%mem,comm --sort=-%cpu | head -6

section "Last logins"
last -n 5 2>/dev/null || echo "no login records"
