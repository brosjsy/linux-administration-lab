# Logs: basics (20 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1590 | L1 | any | Follow the Nginx access log live | `sudo tail -F /var/log/nginx/access.log` | -F keeps following after log rotation. |
| T1591 | L1 | any | Follow the Nginx error log live | `sudo tail -F /var/log/nginx/error.log` | -F keeps following after log rotation. |
| T1592 | L1 | any | Follow the audit log live | `sudo tail -F /var/log/audit/audit.log` | -F keeps following after log rotation. |
| T1593 | L1 | any | Follow the authentication log (Rocky) live | `sudo tail -F /var/log/secure` | -F keeps following after log rotation. |
| T1594 | L1 | any | Follow the authentication log (Ubuntu) live | `sudo tail -F /var/log/auth.log` | -F keeps following after log rotation. |
| T1595 | L1 | any | Follow the fail2ban log live | `sudo tail -F /var/log/fail2ban.log` | -F keeps following after log rotation. |
| T1596 | L1 | any | Follow the kernel log (Ubuntu) live | `sudo tail -F /var/log/kern.log` | -F keeps following after log rotation. |
| T1597 | L1 | any | Follow the package install log (Ubuntu) live | `sudo tail -F /var/log/dpkg.log` | -F keeps following after log rotation. |
| T1598 | L1 | any | Follow the system log (Rocky) live | `sudo tail -F /var/log/messages` | -F keeps following after log rotation. |
| T1599 | L1 | any | Follow the system log (Ubuntu) live | `sudo tail -F /var/log/syslog` | -F keeps following after log rotation. |
| T1600 | L1 | any | Show the last 100 lines of the Nginx access log | `sudo tail -n 100 /var/log/nginx/access.log` | Most recent events are at the end. |
| T1601 | L1 | any | Show the last 100 lines of the Nginx error log | `sudo tail -n 100 /var/log/nginx/error.log` | Most recent events are at the end. |
| T1602 | L1 | any | Show the last 100 lines of the audit log | `sudo tail -n 100 /var/log/audit/audit.log` | Most recent events are at the end. |
| T1603 | L1 | any | Show the last 100 lines of the authentication log (Rocky) | `sudo tail -n 100 /var/log/secure` | Most recent events are at the end. |
| T1604 | L1 | any | Show the last 100 lines of the authentication log (Ubuntu) | `sudo tail -n 100 /var/log/auth.log` | Most recent events are at the end. |
| T1605 | L1 | any | Show the last 100 lines of the fail2ban log | `sudo tail -n 100 /var/log/fail2ban.log` | Most recent events are at the end. |
| T1606 | L1 | any | Show the last 100 lines of the kernel log (Ubuntu) | `sudo tail -n 100 /var/log/kern.log` | Most recent events are at the end. |
| T1607 | L1 | any | Show the last 100 lines of the package install log (Ubuntu) | `sudo tail -n 100 /var/log/dpkg.log` | Most recent events are at the end. |
| T1608 | L1 | any | Show the last 100 lines of the system log (Rocky) | `sudo tail -n 100 /var/log/messages` | Most recent events are at the end. |
| T1609 | L1 | any | Show the last 100 lines of the system log (Ubuntu) | `sudo tail -n 100 /var/log/syslog` | Most recent events are at the end. |
