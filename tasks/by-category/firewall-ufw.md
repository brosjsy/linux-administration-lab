# Firewall: ufw (48 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1433 | L2 | debian | Allow DNS port 53/udp in ufw | `sudo ufw allow 53/udp` | Rule applies to all sources. |
| T1434 | L2 | debian | Allow HTTP port 80/tcp in ufw | `sudo ufw allow 80/tcp` | Rule applies to all sources. |
| T1435 | L2 | debian | Allow HTTPS port 443/tcp in ufw | `sudo ufw allow 443/tcp` | Rule applies to all sources. |
| T1436 | L2 | debian | Allow MySQL/MariaDB port 3306/tcp in ufw | `sudo ufw allow 3306/tcp` | Rule applies to all sources. |
| T1437 | L2 | debian | Allow NFS port 2049/tcp in ufw | `sudo ufw allow 2049/tcp` | Rule applies to all sources. |
| T1438 | L2 | debian | Allow NTP port 123/udp in ufw | `sudo ufw allow 123/udp` | Rule applies to all sources. |
| T1439 | L2 | debian | Allow PostgreSQL port 5432/tcp in ufw | `sudo ufw allow 5432/tcp` | Rule applies to all sources. |
| T1440 | L2 | debian | Allow RDP port 3389/tcp in ufw | `sudo ufw allow 3389/tcp` | Rule applies to all sources. |
| T1441 | L2 | debian | Allow Redis port 6379/tcp in ufw | `sudo ufw allow 6379/tcp` | Rule applies to all sources. |
| T1442 | L2 | debian | Allow SMB port 445/tcp in ufw | `sudo ufw allow 445/tcp` | Rule applies to all sources. |
| T1443 | L2 | debian | Allow SMTP port 25/tcp in ufw | `sudo ufw allow 25/tcp` | Rule applies to all sources. |
| T1444 | L2 | debian | Allow SSH port 22/tcp in ufw | `sudo ufw allow 22/tcp` | Rule applies to all sources. |
| T1445 | L2 | debian | Allow Zabbix agent port 10050/tcp in ufw | `sudo ufw allow 10050/tcp` | Rule applies to all sources. |
| T1446 | L2 | debian | Allow alternative HTTP port 8080/tcp in ufw | `sudo ufw allow 8080/tcp` | Rule applies to all sources. |
| T1447 | L2 | debian | Allow alternative HTTPS port 8443/tcp in ufw | `sudo ufw allow 8443/tcp` | Rule applies to all sources. |
| T1448 | L2 | debian | Allow node_exporter port 9100/tcp in ufw | `sudo ufw allow 9100/tcp` | Rule applies to all sources. |
| T1449 | L2 | debian | Block DNS port 53/udp in ufw | `sudo ufw deny 53/udp` | Silently drops matching traffic. |
| T1450 | L2 | debian | Block HTTP port 80/tcp in ufw | `sudo ufw deny 80/tcp` | Silently drops matching traffic. |
| T1451 | L2 | debian | Block HTTPS port 443/tcp in ufw | `sudo ufw deny 443/tcp` | Silently drops matching traffic. |
| T1452 | L2 | debian | Block MySQL/MariaDB port 3306/tcp in ufw | `sudo ufw deny 3306/tcp` | Silently drops matching traffic. |
| T1453 | L2 | debian | Block NFS port 2049/tcp in ufw | `sudo ufw deny 2049/tcp` | Silently drops matching traffic. |
| T1454 | L2 | debian | Block NTP port 123/udp in ufw | `sudo ufw deny 123/udp` | Silently drops matching traffic. |
| T1455 | L2 | debian | Block PostgreSQL port 5432/tcp in ufw | `sudo ufw deny 5432/tcp` | Silently drops matching traffic. |
| T1456 | L2 | debian | Block RDP port 3389/tcp in ufw | `sudo ufw deny 3389/tcp` | Silently drops matching traffic. |
| T1457 | L2 | debian | Block Redis port 6379/tcp in ufw | `sudo ufw deny 6379/tcp` | Silently drops matching traffic. |
| T1458 | L2 | debian | Block SMB port 445/tcp in ufw | `sudo ufw deny 445/tcp` | Silently drops matching traffic. |
| T1459 | L2 | debian | Block SMTP port 25/tcp in ufw | `sudo ufw deny 25/tcp` | Silently drops matching traffic. |
| T1460 | L2 | debian | Block SSH port 22/tcp in ufw | `sudo ufw deny 22/tcp` | Silently drops matching traffic. |
| T1461 | L2 | debian | Block Zabbix agent port 10050/tcp in ufw | `sudo ufw deny 10050/tcp` | Silently drops matching traffic. |
| T1462 | L2 | debian | Block alternative HTTP port 8080/tcp in ufw | `sudo ufw deny 8080/tcp` | Silently drops matching traffic. |
| T1463 | L2 | debian | Block alternative HTTPS port 8443/tcp in ufw | `sudo ufw deny 8443/tcp` | Silently drops matching traffic. |
| T1464 | L2 | debian | Block node_exporter port 9100/tcp in ufw | `sudo ufw deny 9100/tcp` | Silently drops matching traffic. |
| T1465 | L3 | debian | Allow DNS port 53/udp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 53 proto udp` | Limits the service to the LAN. |
| T1466 | L3 | debian | Allow HTTP port 80/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 80 proto tcp` | Limits the service to the LAN. |
| T1467 | L3 | debian | Allow HTTPS port 443/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 443 proto tcp` | Limits the service to the LAN. |
| T1468 | L3 | debian | Allow MySQL/MariaDB port 3306/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 3306 proto tcp` | Limits the service to the LAN. |
| T1469 | L3 | debian | Allow NFS port 2049/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 2049 proto tcp` | Limits the service to the LAN. |
| T1470 | L3 | debian | Allow NTP port 123/udp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 123 proto udp` | Limits the service to the LAN. |
| T1471 | L3 | debian | Allow PostgreSQL port 5432/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 5432 proto tcp` | Limits the service to the LAN. |
| T1472 | L3 | debian | Allow RDP port 3389/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 3389 proto tcp` | Limits the service to the LAN. |
| T1473 | L3 | debian | Allow Redis port 6379/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 6379 proto tcp` | Limits the service to the LAN. |
| T1474 | L3 | debian | Allow SMB port 445/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 445 proto tcp` | Limits the service to the LAN. |
| T1475 | L3 | debian | Allow SMTP port 25/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 25 proto tcp` | Limits the service to the LAN. |
| T1476 | L3 | debian | Allow SSH port 22/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 22 proto tcp` | Limits the service to the LAN. |
| T1477 | L3 | debian | Allow Zabbix agent port 10050/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 10050 proto tcp` | Limits the service to the LAN. |
| T1478 | L3 | debian | Allow alternative HTTP port 8080/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 8080 proto tcp` | Limits the service to the LAN. |
| T1479 | L3 | debian | Allow alternative HTTPS port 8443/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 8443 proto tcp` | Limits the service to the LAN. |
| T1480 | L3 | debian | Allow node_exporter port 9100/tcp only from 192.168.56.0/24 in ufw | `sudo ufw allow from 192.168.56.0/24 to any port 9100 proto tcp` | Limits the service to the LAN. |
