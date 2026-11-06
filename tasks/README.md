# Linux task library: 5037 tasks with example commands

Searchable in four ways:

1. **Web page:** open [`search.html`](search.html) in a browser (works offline) or via GitHub Pages. Type any word, filter by level, category and distro, copy commands with one click.
2. **Terminal:** `scripts/task_search.sh nginx`, `scripts/task_search.sh -l L3 -c cron backup`
3. **GitHub search / Ctrl+F** in the category pages below.
4. **Data files:** `tasks.json`, `tasks.csv` (Excel), `tasks.tsv` (grep/awk).

## By level

| Level | Meaning | Tasks |
|-------|---------|-------|
| L1 | Beginner | 1759 |
| L2 | Junior admin / on-duty engineer | 2160 |
| L3 | Admin | 884 |
| L4 | Professional | 234 |

## By category

| Category | Tasks |
|----------|-------|
| [Ansible](by-category/ansible.md) | 170 |
| [Backup and archives](by-category/backup-and-archives.md) | 72 |
| [Bash scripting](by-category/bash-scripting.md) | 12 |
| [Boot, kernel and performance](by-category/boot-kernel-and-performance.md) | 28 |
| [Containers](by-category/containers.md) | 60 |
| [Cron](by-category/cron.md) | 576 |
| [Cron: systemd timers](by-category/cron-systemd-timers.md) | 40 |
| [Databases](by-category/databases.md) | 69 |
| [File servers](by-category/file-servers.md) | 41 |
| [Files: disk usage](by-category/files-disk-usage.md) | 12 |
| [Files: find](by-category/files-find.md) | 288 |
| [Firewall: firewalld](by-category/firewall-firewalld.md) | 48 |
| [Firewall: nftables](by-category/firewall-nftables.md) | 16 |
| [Firewall: ufw](by-category/firewall-ufw.md) | 48 |
| [Git for admins](by-category/git-for-admins.md) | 12 |
| [Hardening](by-category/hardening.md) | 26 |
| [Hardening: auditd](by-category/hardening-auditd.md) | 16 |
| [Hardening: kernel](by-category/hardening-kernel.md) | 48 |
| [Logs: analysis](by-category/logs-analysis.md) | 7 |
| [Logs: basics](by-category/logs-basics.md) | 20 |
| [Logs: grep](by-category/logs-grep.md) | 200 |
| [Logs: journalctl](by-category/logs-journalctl.md) | 22 |
| [Logs: logrotate](by-category/logs-logrotate.md) | 42 |
| [Monitoring](by-category/monitoring.md) | 29 |
| [Networking: DNS](by-category/networking-dns.md) | 214 |
| [Networking: HTTP](by-category/networking-http.md) | 28 |
| [Networking: basics](by-category/networking-basics.md) | 53 |
| [Networking: capture](by-category/networking-capture.md) | 16 |
| [Networking: interfaces](by-category/networking-interfaces.md) | 24 |
| [Networking: ports](by-category/networking-ports.md) | 30 |
| [Packages](by-category/packages.md) | 690 |
| [Permissions](by-category/permissions.md) | 94 |
| [Processes](by-category/processes.md) | 92 |
| [SELinux](by-category/selinux.md) | 40 |
| [SSH and remote](by-category/ssh-and-remote.md) | 98 |
| [Services (systemd)](by-category/services-systemd.md) | 820 |
| [Storage and LVM](by-category/storage-and-lvm.md) | 55 |
| [TLS certificates](by-category/tls-certificates.md) | 64 |
| [Text processing](by-category/text-processing.md) | 15 |
| [Troubleshooting tickets](by-category/troubleshooting-tickets.md) | 18 |
| [Users and groups](by-category/users-and-groups.md) | 636 |
| [Virtualisation (KVM)](by-category/virtualisation-kvm.md) | 70 |
| [Web servers](by-category/web-servers.md) | 78 |

> Commands use lab names (192.168.56.x, /srv/share, users ivan, olga...). Read the command before running it, and try risky ones on the lab VMs first.

Regenerate everything with `python3 tools/generate_tasks.py`.

## Publish the search page online
GitHub repo Settings, Pages, Source: Deploy from branch `main`, folder `/ (root)`. The page is then at `https://brosjsy.github.io/linux-administration-lab/tasks/search.html`.
