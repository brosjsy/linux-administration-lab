# Scenario bank: 40 real use cases from beginner to professional

Each scenario is a realistic task or ticket. Try it on the lab VMs first, then open the hint.
Levels: **L1 Beginner**, **L2 Junior admin / on-duty engineer**, **L3 Admin**, **L4 Professional / senior**.

## L1 Beginner

| # | Scenario | Hint |
|---|----------|------|
| 1 | Find every log file bigger than 50 MB | `find /var/log -type f -size +50M -exec ls -lh {} +` |
| 2 | Show the 10 most recent lines of the system log and follow new ones | `tail -n 10 -f /var/log/syslog` or `journalctl -f` |
| 3 | Create user `ivan`, make him change password at first login | `useradd -m ivan && passwd ivan && chage -d 0 ivan` |
| 4 | Give a script execute permission only for its owner | `chmod 700 script.sh` |
| 5 | Find which process uses port 80 | `sudo ss -tlnp 'sport = :80'` |
| 6 | Count failed SSH logins today | `journalctl -u ssh --since today \| grep -c "Failed password"` |
| 7 | Check free disk and memory in human units | `df -h; free -h` |
| 8 | Archive a folder and list the archive without extracting | `tar -czf docs.tgz docs/ && tar -tzf docs.tgz` |
| 9 | Install, start and enable `htop` and `nginx` | `apt install htop nginx && systemctl enable --now nginx` |
| 10 | Schedule a script every day at 06:00 | `crontab -e` -> `0 6 * * * /path/script.sh` ([module 16](../docs/16-cron-scenarios.md)) |

## L2 Junior admin / on-duty engineer

| # | Scenario | Hint |
|---|----------|------|
| 11 | Ticket: "Site is down." Find the cause in 5 minutes | [runbooks/service-down.md](../runbooks/service-down.md) |
| 12 | Alert: disk 95% on `/var`. Free space without breaking logs | [runbooks/disk-full.md](../runbooks/disk-full.md), `journalctl --vacuum-size`, `lsof +L1` |
| 13 | User cannot SSH in after a password reset | [runbooks/ssh-access.md](../runbooks/ssh-access.md), `chage -l`, `faillock --user` |
| 14 | Give the support group rights to restart only nginx | `visudo -f /etc/sudoers.d/support` ([module 02](../docs/02-users-groups.md)) |
| 15 | Cron job works by hand but not from cron | PATH, `%` escaping, logging ([module 16, S5](../docs/16-cron-scenarios.md)) |
| 16 | Stop a long backup from starting twice | `flock` or `scripts/cron_wrapper.sh` |
| 17 | Mount a new disk permanently by UUID and survive reboot | [module 06](../docs/06-storage-lvm.md), test with `mount -a` |
| 18 | Name resolution fails but ping by IP works | [runbooks/dns-failure.md](../runbooks/dns-failure.md) |
| 19 | Make a shared folder where new files keep the team group | `chmod 2770` + SGID ([module 03](../docs/03-permissions.md)) |
| 20 | Write a KB article for a repeated user question | [kb/](../kb/) template |

## L3 Admin

| # | Scenario | Hint |
|---|----------|------|
| 21 | Extend `/var` by 5 GB without downtime | `lvextend -r -L +5G` ([module 06](../docs/06-storage-lvm.md)) |
| 22 | Disable SSH passwords and root login on all servers at once | `ansible/playbooks/03-ssh-hardening.yml --check --diff`, then apply |
| 23 | Onboard 20 new users from HR's CSV | `scripts/user_onboard.sh users.csv --apply` or `ansible/playbooks/02-users.yml` |
| 24 | Monthly patching with no service outage | `ansible/playbooks/05-patching.yml` (`serial: 1`) |
| 25 | Nginx returns 403 on Rocky although permissions are right | SELinux context ([module 19](../docs/19-selinux-apparmor.md)) |
| 26 | Find who modified `/etc/passwd` last night | auditd `ausearch -k identity` ([module 20](../docs/20-audit-integrity.md)) |
| 27 | Certificate expires next week on 10 sites | `scripts/ssl_expiry_check.sh -d 14 site1 site2 ...`, renew, add to cron |
| 28 | Set up DNS and DHCP for the lab network | [module 13](../docs/13-infra-services.md) |
| 29 | Replace a cron job by a systemd timer with logging | [module 16, S10](../docs/16-cron-scenarios.md) |
| 30 | Run a web app in a container that restarts automatically | `compose.yaml` with `restart: unless-stopped` ([module 22](../docs/22-containers.md)) |

## L4 Professional / senior

| # | Scenario | Hint |
|---|----------|------|
| 31 | Harden a fresh server and prove it with numbers | `scripts/harden_audit.sh` + `lynis` before/after ([module 18](../docs/18-hardening.md)) |
| 32 | Build a baseline for 100 servers that runs the same everywhere | `ansible/site.yml`, idempotent, `--check` in CI |
| 33 | Server is slow at 10:00 every day | `sar` history, `iotop`, find the cron/backup job, move or limit it with `CPUQuota` ([module 25](../docs/25-performance-tuning.md)) |
| 34 | App fails with "Too many open files" | raise `LimitNOFILE` in the unit ([module 25](../docs/25-performance-tuning.md)) |
| 35 | Server stuck in emergency mode after a change | bad `/etc/fstab` ([module 24](../docs/24-boot-recovery.md)) |
| 36 | Recover access when the root password is lost | `rd.break` / `init=/bin/bash` ([module 24](../docs/24-boot-recovery.md)) |
| 37 | Design alerts so the on-duty team is not flooded | thresholds + `for:` duration, warning vs critical ([module 23](../docs/23-monitoring.md)) |
| 38 | Detect changed system binaries | AIDE baseline and daily check ([module 20](../docs/20-audit-integrity.md)) |
| 39 | Prove backups work | monthly restore test with `diff` ([module 12](../docs/12-backup.md)) |
| 40 | Write the post-incident report | timeline, root cause, fix, prevention, in the ticket and KB |

## How I record a scenario
```
Scenario #12  Date: 2026-11-07  VM: ubuntu-srv
Commands used: ...
Result / screenshot: ...
What I learned: ...
```
