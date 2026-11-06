# Firewall: nftables (16 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1417 | L3 | any | Show nftables rules mentioning port 10050 | `sudo nft list ruleset \| grep -n 'dport 10050'` | Low-level view under ufw and firewalld. |
| T1418 | L3 | any | Show nftables rules mentioning port 123 | `sudo nft list ruleset \| grep -n 'dport 123'` | Low-level view under ufw and firewalld. |
| T1419 | L3 | any | Show nftables rules mentioning port 2049 | `sudo nft list ruleset \| grep -n 'dport 2049'` | Low-level view under ufw and firewalld. |
| T1420 | L3 | any | Show nftables rules mentioning port 22 | `sudo nft list ruleset \| grep -n 'dport 22'` | Low-level view under ufw and firewalld. |
| T1421 | L3 | any | Show nftables rules mentioning port 25 | `sudo nft list ruleset \| grep -n 'dport 25'` | Low-level view under ufw and firewalld. |
| T1422 | L3 | any | Show nftables rules mentioning port 3306 | `sudo nft list ruleset \| grep -n 'dport 3306'` | Low-level view under ufw and firewalld. |
| T1423 | L3 | any | Show nftables rules mentioning port 3389 | `sudo nft list ruleset \| grep -n 'dport 3389'` | Low-level view under ufw and firewalld. |
| T1424 | L3 | any | Show nftables rules mentioning port 443 | `sudo nft list ruleset \| grep -n 'dport 443'` | Low-level view under ufw and firewalld. |
| T1425 | L3 | any | Show nftables rules mentioning port 445 | `sudo nft list ruleset \| grep -n 'dport 445'` | Low-level view under ufw and firewalld. |
| T1426 | L3 | any | Show nftables rules mentioning port 53 | `sudo nft list ruleset \| grep -n 'dport 53'` | Low-level view under ufw and firewalld. |
| T1427 | L3 | any | Show nftables rules mentioning port 5432 | `sudo nft list ruleset \| grep -n 'dport 5432'` | Low-level view under ufw and firewalld. |
| T1428 | L3 | any | Show nftables rules mentioning port 6379 | `sudo nft list ruleset \| grep -n 'dport 6379'` | Low-level view under ufw and firewalld. |
| T1429 | L3 | any | Show nftables rules mentioning port 80 | `sudo nft list ruleset \| grep -n 'dport 80'` | Low-level view under ufw and firewalld. |
| T1430 | L3 | any | Show nftables rules mentioning port 8080 | `sudo nft list ruleset \| grep -n 'dport 8080'` | Low-level view under ufw and firewalld. |
| T1431 | L3 | any | Show nftables rules mentioning port 8443 | `sudo nft list ruleset \| grep -n 'dport 8443'` | Low-level view under ufw and firewalld. |
| T1432 | L3 | any | Show nftables rules mentioning port 9100 | `sudo nft list ruleset \| grep -n 'dport 9100'` | Low-level view under ufw and firewalld. |
