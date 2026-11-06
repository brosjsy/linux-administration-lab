# Logs: journalctl (22 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1810 | L1 | any | Show logs since the current boot | `journalctl -b` | Start of troubleshooting after a reboot. |
| T1811 | L2 | any | Delete journal entries older than 14 days | `sudo journalctl --vacuum-time=14d` | Time-based cleanup. |
| T1812 | L2 | any | List all recorded boots | `journalctl --list-boots` | Index 0 is current, -1 previous. |
| T1813 | L2 | any | Show critical messages from the whole system last 10 minutes | `journalctl -p crit --since "10 minutes ago" --no-pager` | Priority filter includes more severe levels. |
| T1814 | L2 | any | Show critical messages from the whole system last hour | `journalctl -p crit --since "1 hour ago" --no-pager` | Priority filter includes more severe levels. |
| T1815 | L2 | any | Show critical messages from the whole system since yesterday | `journalctl -p crit --since "yesterday" --no-pager` | Priority filter includes more severe levels. |
| T1816 | L2 | any | Show critical messages from the whole system today | `journalctl -p crit --since "today" --no-pager` | Priority filter includes more severe levels. |
| T1817 | L2 | any | Show errors from the previous boot | `journalctl -b -1 -p err` | Explains why a server crashed or rebooted. |
| T1818 | L2 | any | Show errors from the whole system last 10 minutes | `journalctl -p err --since "10 minutes ago" --no-pager` | Priority filter includes more severe levels. |
| T1819 | L2 | any | Show errors from the whole system last hour | `journalctl -p err --since "1 hour ago" --no-pager` | Priority filter includes more severe levels. |
| T1820 | L2 | any | Show errors from the whole system since yesterday | `journalctl -p err --since "yesterday" --no-pager` | Priority filter includes more severe levels. |
| T1821 | L2 | any | Show errors from the whole system today | `journalctl -p err --since "today" --no-pager` | Priority filter includes more severe levels. |
| T1822 | L2 | any | Show how much disk the journal uses | `journalctl --disk-usage` | Large journals cause disk-full alerts. |
| T1823 | L2 | any | Show kernel messages from this boot | `journalctl -k` | Same as dmesg but with timestamps and history. |
| T1824 | L2 | any | Show logs of a specific program by name | `journalctl -t sudo --since today` | -t filters by syslog identifier. |
| T1825 | L2 | any | Show warnings from the whole system last 10 minutes | `journalctl -p warning --since "10 minutes ago" --no-pager` | Priority filter includes more severe levels. |
| T1826 | L2 | any | Show warnings from the whole system last hour | `journalctl -p warning --since "1 hour ago" --no-pager` | Priority filter includes more severe levels. |
| T1827 | L2 | any | Show warnings from the whole system since yesterday | `journalctl -p warning --since "yesterday" --no-pager` | Priority filter includes more severe levels. |
| T1828 | L2 | any | Show warnings from the whole system today | `journalctl -p warning --since "today" --no-pager` | Priority filter includes more severe levels. |
| T1829 | L2 | any | Shrink the journal to 200 MB | `sudo journalctl --vacuum-size=200M` | Deletes oldest archived journal files. |
| T1830 | L3 | any | Export logs of a time window for an incident | `journalctl --since "2026-11-06 22:00" --until "2026-11-06 23:00" -o short-iso > incident.log` | ISO timestamps for reports. |
| T1831 | L3 | any | Show logs as JSON for parsing | `journalctl -u nginx -o json-pretty -n 5` | Every field, including _PID and _SYSTEMD_UNIT. |
