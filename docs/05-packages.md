# 05. Package management

| Task | Debian/Ubuntu | RHEL/Rocky |
|------|---------------|-----------|
| Refresh + upgrade | `apt update && apt upgrade` | `dnf upgrade` |
| Install | `apt install nginx` | `dnf install nginx` |
| Remove | `apt remove nginx` | `dnf remove nginx` |
| Search | `apt search htop` | `dnf search htop` |
| Which package owns a file | `dpkg -S /usr/bin/ls` | `rpm -qf /usr/bin/ls` |
| List installed | `apt list --installed` | `dnf list installed` |
| History / rollback | `/var/log/apt/history.log` | `dnf history`, `dnf history undo N` |
| Security updates only | `unattended-upgrades` | `dnf upgrade --security` |

Practice: install `htop`, find its files (`dpkg -L htop`), remove it, then roll back a change with `dnf history undo` on Rocky.
