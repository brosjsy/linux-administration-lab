# Linux Administration Lab

Hands-on Linux system administration lab, from the first login to running and supporting production-style services.
Every module has the commands, the reasoning behind them and a verification step, and the `scripts/` folder holds tested automation I use in the lab.

**Author:** Joseph Olawoyin, MSc Information Security student, ITMO University, Saint Petersburg, Russia
**Lab environment:** Ubuntu Server 24.04 LTS and Rocky Linux 9 (VirtualBox / Vagrant, see `lab/Vagrantfile`)

## What this lab covers (A to Z)

| # | Module | Key tools | File |
|---|--------|-----------|------|
| 01 | Filesystem, navigation and help | `ls`, `find`, `grep`, `less`, `man`, FHS | [docs/01-basics.md](docs/01-basics.md) |
| 02 | Users, groups and sudo | `useradd`, `usermod`, `passwd`, `chage`, `visudo` | [docs/02-users-groups.md](docs/02-users-groups.md) |
| 03 | Permissions and ACLs | `chmod`, `chown`, `umask`, SUID/SGID/sticky, `setfacl` | [docs/03-permissions.md](docs/03-permissions.md) |
| 04 | Processes and services | `ps`, `top`, `kill`, `systemctl`, unit files | [docs/04-processes-services.md](docs/04-processes-services.md) |
| 05 | Package management | `apt`, `dnf`, `rpm`, `dpkg`, repositories | [docs/05-packages.md](docs/05-packages.md) |
| 06 | Storage and LVM | `lsblk`, `fdisk`, `mkfs`, `mount`, `/etc/fstab`, LVM | [docs/06-storage-lvm.md](docs/06-storage-lvm.md) |
| 07 | Networking | `ip`, `ss`, `nmcli`, `netplan`, `ping`, `traceroute`, `dig` | [docs/07-networking.md](docs/07-networking.md) |
| 08 | SSH and hardening | keys, `sshd_config`, `fail2ban` | [docs/08-ssh-hardening.md](docs/08-ssh-hardening.md) |
| 09 | Firewall | `ufw`, `firewalld`, `nftables` | [docs/09-firewall.md](docs/09-firewall.md) |
| 10 | Logs and monitoring | `journalctl`, `/var/log`, `logrotate`, `vmstat`, `iostat`, `df`, `free` | [docs/10-logs-monitoring.md](docs/10-logs-monitoring.md) |
| 11 | Scheduling | `cron`, `systemd` timers | [docs/11-scheduling.md](docs/11-scheduling.md) |
| 12 | Backup and restore | `tar`, `rsync`, restore testing | [docs/12-backup.md](docs/12-backup.md) |
| 13 | Infrastructure services | DNS (BIND), DHCP (Kea), file server (Samba, NFS), web (Nginx) | [docs/13-infra-services.md](docs/13-infra-services.md) |
| 14 | Directory services | LDAP / FreeIPA basics, joining Linux to AD (`realmd`, `sssd`) | [docs/14-directory-services.md](docs/14-directory-services.md) |
| 15 | Bash scripting | variables, loops, functions, exit codes, `set -euo pipefail` | [docs/15-bash-scripting.md](docs/15-bash-scripting.md) |
| 16 | Troubleshooting runbooks | disk full, service down, high load, no SSH, DNS failure | [runbooks/](runbooks/) |
| 17 | Service desk practice | ticket triage, knowledge base articles | [tickets/](tickets/), [kb/](kb/) |

## Scripts

| Script | What it does |
|--------|--------------|
| [`scripts/health_check.sh`](scripts/health_check.sh) | One-shot server health report: uptime, load, memory, disk, failed units, listening ports, last logins |
| [`scripts/disk_alert.sh`](scripts/disk_alert.sh) | Warns when any filesystem passes a usage threshold (cron-friendly, non-zero exit on alert) |
| [`scripts/user_onboard.sh`](scripts/user_onboard.sh) | Creates users from a CSV file with groups, forced password change and SSH key (dry-run by default) |
| [`scripts/backup.sh`](scripts/backup.sh) | Timestamped `tar` backups with retention and an integrity check |
| [`scripts/log_report.sh`](scripts/log_report.sh) | Summary of failed SSH logins, sudo use and service errors from the journal |
| [`scripts/service_watchdog.sh`](scripts/service_watchdog.sh) | Checks a list of systemd services and restarts any that are down, with logging |

All scripts pass [ShellCheck](https://www.shellcheck.net/) in CI (`.github/workflows/shellcheck.yml`).

## Quick start

```bash
git clone https://github.com/brosjsy/linux-administration-lab.git
cd linux-administration-lab/lab
vagrant up            # starts ubuntu-srv and rocky-srv
vagrant ssh ubuntu-srv
sudo /vagrant/scripts/health_check.sh
```

## Skills demonstrated

Linux administration (Debian and RHEL families), systemd, storage and LVM, TCP/IP networking and troubleshooting, DNS and DHCP, file servers, SSH hardening and firewalls, log analysis, backup and restore, Bash automation, ticket triage and writing knowledge base articles.
