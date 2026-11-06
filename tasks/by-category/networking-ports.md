# Networking: ports (30 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T2238 | L2 | any | Check which process listens on port 10050 (Zabbix agent) | `sudo ss -tlnp 'sport = :10050'` | Shows the program and PID that owns the port. |
| T2239 | L2 | any | Check which process listens on port 123 (NTP) | `sudo ss -ulnp 'sport = :123'` | Shows the program and PID that owns the port. |
| T2240 | L2 | any | Check which process listens on port 2049 (NFS) | `sudo ss -tlnp 'sport = :2049'` | Shows the program and PID that owns the port. |
| T2241 | L2 | any | Check which process listens on port 22 (SSH) | `sudo ss -tlnp 'sport = :22'` | Shows the program and PID that owns the port. |
| T2242 | L2 | any | Check which process listens on port 25 (SMTP) | `sudo ss -tlnp 'sport = :25'` | Shows the program and PID that owns the port. |
| T2243 | L2 | any | Check which process listens on port 3306 (MySQL/MariaDB) | `sudo ss -tlnp 'sport = :3306'` | Shows the program and PID that owns the port. |
| T2244 | L2 | any | Check which process listens on port 3389 (RDP) | `sudo ss -tlnp 'sport = :3389'` | Shows the program and PID that owns the port. |
| T2245 | L2 | any | Check which process listens on port 443 (HTTPS) | `sudo ss -tlnp 'sport = :443'` | Shows the program and PID that owns the port. |
| T2246 | L2 | any | Check which process listens on port 445 (SMB) | `sudo ss -tlnp 'sport = :445'` | Shows the program and PID that owns the port. |
| T2247 | L2 | any | Check which process listens on port 53 (DNS) | `sudo ss -ulnp 'sport = :53'` | Shows the program and PID that owns the port. |
| T2248 | L2 | any | Check which process listens on port 5432 (PostgreSQL) | `sudo ss -tlnp 'sport = :5432'` | Shows the program and PID that owns the port. |
| T2249 | L2 | any | Check which process listens on port 6379 (Redis) | `sudo ss -tlnp 'sport = :6379'` | Shows the program and PID that owns the port. |
| T2250 | L2 | any | Check which process listens on port 80 (HTTP) | `sudo ss -tlnp 'sport = :80'` | Shows the program and PID that owns the port. |
| T2251 | L2 | any | Check which process listens on port 8080 (alternative HTTP) | `sudo ss -tlnp 'sport = :8080'` | Shows the program and PID that owns the port. |
| T2252 | L2 | any | Check which process listens on port 8443 (alternative HTTPS) | `sudo ss -tlnp 'sport = :8443'` | Shows the program and PID that owns the port. |
| T2253 | L2 | any | Check which process listens on port 9100 (node_exporter) | `sudo ss -tlnp 'sport = :9100'` | Shows the program and PID that owns the port. |
| T2254 | L2 | any | Test if remote port 10050 (Zabbix agent) is open on 192.168.56.20 | `nc -zv 192.168.56.20 10050` | succeeded means a TCP connection was made. |
| T2255 | L2 | any | Test if remote port 2049 (NFS) is open on 192.168.56.20 | `nc -zv 192.168.56.20 2049` | succeeded means a TCP connection was made. |
| T2256 | L2 | any | Test if remote port 22 (SSH) is open on 192.168.56.20 | `nc -zv 192.168.56.20 22` | succeeded means a TCP connection was made. |
| T2257 | L2 | any | Test if remote port 25 (SMTP) is open on 192.168.56.20 | `nc -zv 192.168.56.20 25` | succeeded means a TCP connection was made. |
| T2258 | L2 | any | Test if remote port 3306 (MySQL/MariaDB) is open on 192.168.56.20 | `nc -zv 192.168.56.20 3306` | succeeded means a TCP connection was made. |
| T2259 | L2 | any | Test if remote port 3389 (RDP) is open on 192.168.56.20 | `nc -zv 192.168.56.20 3389` | succeeded means a TCP connection was made. |
| T2260 | L2 | any | Test if remote port 443 (HTTPS) is open on 192.168.56.20 | `nc -zv 192.168.56.20 443` | succeeded means a TCP connection was made. |
| T2261 | L2 | any | Test if remote port 445 (SMB) is open on 192.168.56.20 | `nc -zv 192.168.56.20 445` | succeeded means a TCP connection was made. |
| T2262 | L2 | any | Test if remote port 5432 (PostgreSQL) is open on 192.168.56.20 | `nc -zv 192.168.56.20 5432` | succeeded means a TCP connection was made. |
| T2263 | L2 | any | Test if remote port 6379 (Redis) is open on 192.168.56.20 | `nc -zv 192.168.56.20 6379` | succeeded means a TCP connection was made. |
| T2264 | L2 | any | Test if remote port 80 (HTTP) is open on 192.168.56.20 | `nc -zv 192.168.56.20 80` | succeeded means a TCP connection was made. |
| T2265 | L2 | any | Test if remote port 8080 (alternative HTTP) is open on 192.168.56.20 | `nc -zv 192.168.56.20 8080` | succeeded means a TCP connection was made. |
| T2266 | L2 | any | Test if remote port 8443 (alternative HTTPS) is open on 192.168.56.20 | `nc -zv 192.168.56.20 8443` | succeeded means a TCP connection was made. |
| T2267 | L2 | any | Test if remote port 9100 (node_exporter) is open on 192.168.56.20 | `nc -zv 192.168.56.20 9100` | succeeded means a TCP connection was made. |
