# Files: disk usage (12 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1069 | L2 | any | Show the 10 biggest items in /etc | `sudo du -xh /etc --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1070 | L2 | any | Show the 10 biggest items in /home | `sudo du -xh /home --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1071 | L2 | any | Show the 10 biggest items in /opt | `sudo du -xh /opt --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1072 | L2 | any | Show the 10 biggest items in /root | `sudo du -xh /root --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1073 | L2 | any | Show the 10 biggest items in /srv | `sudo du -xh /srv --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1074 | L2 | any | Show the 10 biggest items in /tmp | `sudo du -xh /tmp --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1075 | L2 | any | Show the 10 biggest items in /usr/local | `sudo du -xh /usr/local --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1076 | L2 | any | Show the 10 biggest items in /var/backups | `sudo du -xh /var/backups --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1077 | L2 | any | Show the 10 biggest items in /var/lib/docker | `sudo du -xh /var/lib/docker --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1078 | L2 | any | Show the 10 biggest items in /var/lib/postgresql | `sudo du -xh /var/lib/postgresql --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1079 | L2 | any | Show the 10 biggest items in /var/log | `sudo du -xh /var/log --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
| T1080 | L2 | any | Show the 10 biggest items in /var/www | `sudo du -xh /var/www --max-depth=1 2>/dev/null \| sort -h \| tail -10` | -x stays on one filesystem. |
