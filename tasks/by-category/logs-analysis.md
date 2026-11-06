# Logs: analysis (7 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1583 | L2 | any | Count HTTP status codes in the Nginx access log | `awk '{print $9}' /var/log/nginx/access.log \| sort \| uniq -c \| sort -rn` | Spikes of 5xx mean backend problems. |
| T1584 | L2 | any | Requests per minute in the Nginx access log | `awk '{print substr($4,2,17)}' /var/log/nginx/access.log \| uniq -c \| tail -20` | Shows traffic peaks. |
| T1585 | L2 | any | Top 10 client IPs in the Nginx access log | `awk '{print $1}' /var/log/nginx/access.log \| sort \| uniq -c \| sort -rn \| head` | Find heavy users or attackers. |
| T1586 | L2 | any | Top 10 requested URLs in the Nginx access log | `awk '{print $7}' /var/log/nginx/access.log \| sort \| uniq -c \| sort -rn \| head` | Most popular or most attacked paths. |
| T1587 | L2 | any | Top IPs with failed SSH passwords (Ubuntu) | `sudo grep 'Failed password' /var/log/auth.log \| grep -oE 'from [0-9.]+' \| awk '{print $2}' \| sort \| uniq -c \| sort -rn \| head` | Candidates for fail2ban or firewall block. |
| T1588 | L2 | any | Top user agents in the Nginx access log | `awk -F'"' '{print $6}' /var/log/nginx/access.log \| sort \| uniq -c \| sort -rn \| head` | Spot bots and scanners. |
| T1589 | L2 | any | Usernames attackers try over SSH (Ubuntu) | `sudo grep 'Invalid user' /var/log/auth.log \| awk '{print $8}' \| sort \| uniq -c \| sort -rn \| head` | Shows brute-force dictionaries. |
