# 18. Linux hardening

Level: intermediate to professional. Based on the ideas of CIS Benchmarks and the Russian FSTEC recommendations: reduce attack surface, least privilege, logging, updates.

## Hardening checklist
| Area | Action | Command / file |
|------|--------|----------------|
| Updates | Automatic security updates | `unattended-upgrades` (Ubuntu), `dnf-automatic` (Rocky) |
| Accounts | No empty passwords, lock unused accounts | `awk -F: '($2==""){print $1}' /etc/shadow`, `usermod -L` |
| Passwords | Length and complexity | `/etc/security/pwquality.conf`: `minlen = 12` |
| Passwords | Ageing | `/etc/login.defs`: `PASS_MAX_DAYS 90` |
| Login | Lock after failed attempts | `pam_faillock` (`authselect` on Rocky) |
| Root | No direct root SSH, use sudo | `PermitRootLogin no` |
| SSH | Keys only, limited users, modern ciphers | [08-ssh-hardening.md](08-ssh-hardening.md) |
| Network | Firewall default deny | [09-firewall.md](09-firewall.md) |
| Services | Disable what is not needed | `systemctl list-unit-files --state=enabled`, `systemctl disable --now cups avahi-daemon` |
| Ports | Know every listening port | `ss -tulpn` |
| Kernel | Safe network settings | `/etc/sysctl.d/99-hardening.conf` (below) |
| Filesystems | `noexec,nosuid,nodev` on `/tmp` and `/dev/shm` | `/etc/fstab` |
| Files | Correct permissions on sensitive files | `/etc/shadow 640 root:shadow`, `/etc/passwd 644` |
| SUID | Audit SUID/SGID binaries | `find / -perm /6000 -type f` |
| MAC | SELinux enforcing / AppArmor enabled | [19-selinux-apparmor.md](19-selinux-apparmor.md) |
| Audit | auditd rules, file integrity (AIDE) | [20-audit-integrity.md](20-audit-integrity.md) |
| Logging | Central logs, logrotate, time sync | `chrony`, `rsyslog` forwarding |
| Banner | Legal warning before login | `/etc/issue.net`, `Banner /etc/issue.net` |
| Cron | Only allowed users | `/etc/cron.allow` |
| USB / modules | Block unused kernel modules | `/etc/modprobe.d/blacklist.conf`: `install usb-storage /bin/true` |

## Kernel network hardening
`/etc/sysctl.d/99-hardening.conf`
```
net.ipv4.ip_forward = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.all.log_martians = 1
net.ipv4.tcp_syncookies = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
kernel.randomize_va_space = 2
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
fs.suid_dumpable = 0
```
```bash
sudo sysctl --system
```

## Secure /tmp
```
tmpfs  /tmp  tmpfs  defaults,noexec,nosuid,nodev,size=1G  0 0
```

## Measure, do not guess
```bash
sudo /opt/lab/scripts/harden_audit.sh      # this lab: quick PASS/WARN report
sudo apt install lynis && sudo lynis audit system   # full audit with hardening index
```
Workflow: audit, fix, re-audit, record the score before and after.
Automate the fixes with Ansible (`ansible/playbooks/03-ssh-hardening.yml`, `04-firewall.yml`).
