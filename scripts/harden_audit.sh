#!/usr/bin/env bash
# harden_audit.sh - read-only hardening check with PASS / WARN / INFO lines
# Changes nothing. Run as root for complete results.
# Exit: 0 = no WARN, 1 = at least one WARN
# pass and warn always return 0, so "test && pass || warn" is safe here.
# shellcheck disable=SC2015
set -uo pipefail

warns=0
pass() { printf 'PASS  %s\n' "$1"; }
warn() { printf 'WARN  %s\n' "$1"; warns=$((warns + 1)); }
info() { printf 'INFO  %s\n' "$1"; }

sshd_value() {
  local key="$1"
  if command -v sshd >/dev/null 2>&1 && sshd -T >/dev/null 2>&1; then
    sshd -T 2>/dev/null | awk -v k="$key" 'tolower($1)==tolower(k){print $2; exit}'
  else
    cat /etc/ssh/sshd_config /etc/ssh/sshd_config.d/*.conf 2>/dev/null \
      | awk -v k="$key" 'tolower($1)==tolower(k){print $2; exit}'
  fi
}

echo "== SSH =="
if [[ -e /etc/ssh/sshd_config ]]; then
  [[ "$(sshd_value PermitRootLogin)" == "no" ]] && pass "PermitRootLogin no" || warn "PermitRootLogin is not 'no'"
  [[ "$(sshd_value PasswordAuthentication)" == "no" ]] && pass "PasswordAuthentication no" || warn "SSH password login allowed"
  mat="$(sshd_value MaxAuthTries)"
  [[ -n "$mat" && "$mat" -le 4 ]] && pass "MaxAuthTries ${mat}" || warn "MaxAuthTries not set to 4 or less"
else
  info "OpenSSH server not installed"
fi

echo "== Accounts =="
if [[ -r /etc/shadow ]]; then
  empty=$(awk -F: '($2==""){print $1}' /etc/shadow)
  [[ -z "$empty" ]] && pass "No accounts with empty password" || warn "Empty password: ${empty//$'\n'/ }"
else
  info "Run as root to check /etc/shadow"
fi
uid0=$(awk -F: '($3==0){print $1}' /etc/passwd | tr '\n' ' ')
[[ "$uid0" == "root " ]] && pass "Only root has UID 0" || warn "UID 0 accounts: ${uid0}"
maxdays=$(awk '/^PASS_MAX_DAYS/{print $2}' /etc/login.defs 2>/dev/null)
[[ -n "$maxdays" && "$maxdays" -le 90 ]] && pass "PASS_MAX_DAYS ${maxdays}" || warn "PASS_MAX_DAYS is ${maxdays:-unset} (want 90 or less)"

echo "== File permissions =="
check_mode() {
  local f="$1" max="$2" mode
  [[ -e "$f" ]] || { info "$f not present"; return; }
  mode=$(stat -c '%a' "$f")
  (( 8#$mode <= 8#$max )) && pass "$f mode $mode" || warn "$f mode $mode (want $max or stricter)"
}
check_mode /etc/passwd 644
check_mode /etc/shadow 640
check_mode /etc/group 644
check_mode /etc/ssh/sshd_config 644
ww=$(find /etc -xdev -type f -perm -0002 2>/dev/null | head -5)
[[ -z "$ww" ]] && pass "No world-writable files in /etc" || warn "World-writable in /etc: ${ww//$'\n'/ }"

echo "== Kernel =="
check_sysctl() {
  local key="$1" want="$2" val
  val=$(sysctl -n "$key" 2>/dev/null) || { info "$key not available"; return; }
  [[ "$val" == "$want" ]] && pass "$key = $val" || warn "$key = $val (want $want)"
}
check_sysctl kernel.randomize_va_space 2
check_sysctl net.ipv4.tcp_syncookies 1
check_sysctl net.ipv4.conf.all.accept_redirects 0
check_sysctl net.ipv4.conf.all.send_redirects 0
check_sysctl net.ipv4.ip_forward 0

echo "== Services and firewall =="
if command -v ufw >/dev/null 2>&1; then
  ufw status 2>/dev/null | grep -q "Status: active" && pass "ufw active" || warn "ufw not active"
elif command -v firewall-cmd >/dev/null 2>&1; then
  firewall-cmd --state >/dev/null 2>&1 && pass "firewalld running" || warn "firewalld not running"
else
  warn "No ufw or firewalld found"
fi
if command -v systemctl >/dev/null 2>&1 && [[ -d /run/systemd/system ]]; then
  for svc in telnet.socket rsh.socket vsftpd avahi-daemon cups; do
    systemctl is-enabled --quiet "$svc" 2>/dev/null && warn "Unneeded service enabled: $svc"
  done
  systemctl is-active --quiet auditd 2>/dev/null && pass "auditd running" || warn "auditd not running"
else
  info "systemd not running, service checks skipped"
fi

echo "== Mounts =="
if findmnt -no OPTIONS /tmp >/dev/null 2>&1; then
  opts=$(findmnt -no OPTIONS /tmp)
  [[ "$opts" == *noexec* ]] && pass "/tmp mounted noexec" || warn "/tmp not mounted noexec"
else
  warn "/tmp is not a separate mount"
fi

echo
echo "Result: ${warns} warning(s)"
(( warns == 0 ))
