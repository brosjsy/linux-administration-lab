# 01. Filesystem, navigation and help

## Goal
Move around the system confidently, find files and read documentation without a browser.

## Filesystem hierarchy (FHS)
| Path | Purpose |
|------|---------|
| `/etc` | System configuration |
| `/var/log` | Logs |
| `/home` | User home directories |
| `/usr/bin`, `/usr/sbin` | Programs |
| `/tmp` | Temporary files (cleared on reboot) |
| `/proc`, `/sys` | Kernel and process information |

## Tasks
```bash
pwd; ls -lah /etc | head
cd /var/log && ls -lt | head          # newest logs first
find /etc -name "*.conf" -mtime -7     # configs changed in the last 7 days
grep -Rni "PermitRootLogin" /etc/ssh/  # search config files
du -sh /var/* 2>/dev/null | sort -h    # what takes space
less /var/log/syslog                   # /pattern to search, q to quit
man ls; ls --help; tldr tar            # documentation
history | tail -20
```

## Check
- [x] Found every `.conf` changed this week
- [x] Located the largest directory under `/var`
