# Logs: grep (200 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1610 | L1 | any | Search HTTP 404 responses in the Nginx access log | `sudo grep -i ' 404 ' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1611 | L1 | any | Search HTTP 404 responses in the Nginx error log | `sudo grep -i ' 404 ' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1612 | L1 | any | Search HTTP 404 responses in the audit log | `sudo grep -i ' 404 ' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1613 | L1 | any | Search HTTP 404 responses in the authentication log (Rocky) | `sudo grep -i ' 404 ' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1614 | L1 | any | Search HTTP 404 responses in the authentication log (Ubuntu) | `sudo grep -i ' 404 ' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1615 | L1 | any | Search HTTP 404 responses in the fail2ban log | `sudo grep -i ' 404 ' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1616 | L1 | any | Search HTTP 404 responses in the kernel log (Ubuntu) | `sudo grep -i ' 404 ' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1617 | L1 | any | Search HTTP 404 responses in the package install log (Ubuntu) | `sudo grep -i ' 404 ' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1618 | L1 | any | Search HTTP 404 responses in the system log (Rocky) | `sudo grep -i ' 404 ' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1619 | L1 | any | Search HTTP 404 responses in the system log (Ubuntu) | `sudo grep -i ' 404 ' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1620 | L1 | any | Search HTTP 500 responses in the Nginx access log | `sudo grep -i ' 500 ' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1621 | L1 | any | Search HTTP 500 responses in the Nginx error log | `sudo grep -i ' 500 ' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1622 | L1 | any | Search HTTP 500 responses in the audit log | `sudo grep -i ' 500 ' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1623 | L1 | any | Search HTTP 500 responses in the authentication log (Rocky) | `sudo grep -i ' 500 ' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1624 | L1 | any | Search HTTP 500 responses in the authentication log (Ubuntu) | `sudo grep -i ' 500 ' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1625 | L1 | any | Search HTTP 500 responses in the fail2ban log | `sudo grep -i ' 500 ' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1626 | L1 | any | Search HTTP 500 responses in the kernel log (Ubuntu) | `sudo grep -i ' 500 ' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1627 | L1 | any | Search HTTP 500 responses in the package install log (Ubuntu) | `sudo grep -i ' 500 ' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1628 | L1 | any | Search HTTP 500 responses in the system log (Rocky) | `sudo grep -i ' 500 ' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1629 | L1 | any | Search HTTP 500 responses in the system log (Ubuntu) | `sudo grep -i ' 500 ' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1630 | L1 | any | Search crashes (segfaults) in the Nginx access log | `sudo grep -i 'segfault' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1631 | L1 | any | Search crashes (segfaults) in the Nginx error log | `sudo grep -i 'segfault' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1632 | L1 | any | Search crashes (segfaults) in the audit log | `sudo grep -i 'segfault' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1633 | L1 | any | Search crashes (segfaults) in the authentication log (Rocky) | `sudo grep -i 'segfault' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1634 | L1 | any | Search crashes (segfaults) in the authentication log (Ubuntu) | `sudo grep -i 'segfault' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1635 | L1 | any | Search crashes (segfaults) in the fail2ban log | `sudo grep -i 'segfault' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1636 | L1 | any | Search crashes (segfaults) in the kernel log (Ubuntu) | `sudo grep -i 'segfault' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1637 | L1 | any | Search crashes (segfaults) in the package install log (Ubuntu) | `sudo grep -i 'segfault' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1638 | L1 | any | Search crashes (segfaults) in the system log (Rocky) | `sudo grep -i 'segfault' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1639 | L1 | any | Search crashes (segfaults) in the system log (Ubuntu) | `sudo grep -i 'segfault' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1640 | L1 | any | Search failed SSH passwords in the Nginx access log | `sudo grep -i 'Failed password' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1641 | L1 | any | Search failed SSH passwords in the Nginx error log | `sudo grep -i 'Failed password' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1642 | L1 | any | Search failed SSH passwords in the audit log | `sudo grep -i 'Failed password' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1643 | L1 | any | Search failed SSH passwords in the authentication log (Rocky) | `sudo grep -i 'Failed password' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1644 | L1 | any | Search failed SSH passwords in the authentication log (Ubuntu) | `sudo grep -i 'Failed password' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1645 | L1 | any | Search failed SSH passwords in the fail2ban log | `sudo grep -i 'Failed password' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1646 | L1 | any | Search failed SSH passwords in the kernel log (Ubuntu) | `sudo grep -i 'Failed password' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1647 | L1 | any | Search failed SSH passwords in the package install log (Ubuntu) | `sudo grep -i 'Failed password' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1648 | L1 | any | Search failed SSH passwords in the system log (Rocky) | `sudo grep -i 'Failed password' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1649 | L1 | any | Search failed SSH passwords in the system log (Ubuntu) | `sudo grep -i 'Failed password' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1650 | L1 | any | Search out-of-memory events in the Nginx access log | `sudo grep -i 'OOM' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1651 | L1 | any | Search out-of-memory events in the Nginx error log | `sudo grep -i 'OOM' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1652 | L1 | any | Search out-of-memory events in the audit log | `sudo grep -i 'OOM' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1653 | L1 | any | Search out-of-memory events in the authentication log (Rocky) | `sudo grep -i 'OOM' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1654 | L1 | any | Search out-of-memory events in the authentication log (Ubuntu) | `sudo grep -i 'OOM' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1655 | L1 | any | Search out-of-memory events in the fail2ban log | `sudo grep -i 'OOM' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1656 | L1 | any | Search out-of-memory events in the kernel log (Ubuntu) | `sudo grep -i 'OOM' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1657 | L1 | any | Search out-of-memory events in the package install log (Ubuntu) | `sudo grep -i 'OOM' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1658 | L1 | any | Search out-of-memory events in the system log (Rocky) | `sudo grep -i 'OOM' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1659 | L1 | any | Search out-of-memory events in the system log (Ubuntu) | `sudo grep -i 'OOM' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1660 | L1 | any | Search permission denials in the Nginx access log | `sudo grep -i 'denied' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1661 | L1 | any | Search permission denials in the Nginx error log | `sudo grep -i 'denied' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1662 | L1 | any | Search permission denials in the audit log | `sudo grep -i 'denied' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1663 | L1 | any | Search permission denials in the authentication log (Rocky) | `sudo grep -i 'denied' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1664 | L1 | any | Search permission denials in the authentication log (Ubuntu) | `sudo grep -i 'denied' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1665 | L1 | any | Search permission denials in the fail2ban log | `sudo grep -i 'denied' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1666 | L1 | any | Search permission denials in the kernel log (Ubuntu) | `sudo grep -i 'denied' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1667 | L1 | any | Search permission denials in the package install log (Ubuntu) | `sudo grep -i 'denied' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1668 | L1 | any | Search permission denials in the system log (Rocky) | `sudo grep -i 'denied' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1669 | L1 | any | Search permission denials in the system log (Ubuntu) | `sudo grep -i 'denied' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1670 | L1 | any | Search successful key logins in the Nginx access log | `sudo grep -i 'Accepted publickey' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1671 | L1 | any | Search successful key logins in the Nginx error log | `sudo grep -i 'Accepted publickey' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1672 | L1 | any | Search successful key logins in the audit log | `sudo grep -i 'Accepted publickey' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1673 | L1 | any | Search successful key logins in the authentication log (Rocky) | `sudo grep -i 'Accepted publickey' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1674 | L1 | any | Search successful key logins in the authentication log (Ubuntu) | `sudo grep -i 'Accepted publickey' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1675 | L1 | any | Search successful key logins in the fail2ban log | `sudo grep -i 'Accepted publickey' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1676 | L1 | any | Search successful key logins in the kernel log (Ubuntu) | `sudo grep -i 'Accepted publickey' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1677 | L1 | any | Search successful key logins in the package install log (Ubuntu) | `sudo grep -i 'Accepted publickey' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1678 | L1 | any | Search successful key logins in the system log (Rocky) | `sudo grep -i 'Accepted publickey' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1679 | L1 | any | Search successful key logins in the system log (Ubuntu) | `sudo grep -i 'Accepted publickey' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1680 | L1 | any | Search sudo usage in the Nginx access log | `sudo grep -i 'sudo' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1681 | L1 | any | Search sudo usage in the Nginx error log | `sudo grep -i 'sudo' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1682 | L1 | any | Search sudo usage in the audit log | `sudo grep -i 'sudo' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1683 | L1 | any | Search sudo usage in the authentication log (Rocky) | `sudo grep -i 'sudo' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1684 | L1 | any | Search sudo usage in the authentication log (Ubuntu) | `sudo grep -i 'sudo' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1685 | L1 | any | Search sudo usage in the fail2ban log | `sudo grep -i 'sudo' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1686 | L1 | any | Search sudo usage in the kernel log (Ubuntu) | `sudo grep -i 'sudo' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1687 | L1 | any | Search sudo usage in the package install log (Ubuntu) | `sudo grep -i 'sudo' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1688 | L1 | any | Search sudo usage in the system log (Rocky) | `sudo grep -i 'sudo' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1689 | L1 | any | Search sudo usage in the system log (Ubuntu) | `sudo grep -i 'sudo' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1690 | L1 | any | Search the word error in the Nginx access log | `sudo grep -i 'error' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1691 | L1 | any | Search the word error in the Nginx error log | `sudo grep -i 'error' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1692 | L1 | any | Search the word error in the audit log | `sudo grep -i 'error' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1693 | L1 | any | Search the word error in the authentication log (Rocky) | `sudo grep -i 'error' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1694 | L1 | any | Search the word error in the authentication log (Ubuntu) | `sudo grep -i 'error' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1695 | L1 | any | Search the word error in the fail2ban log | `sudo grep -i 'error' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1696 | L1 | any | Search the word error in the kernel log (Ubuntu) | `sudo grep -i 'error' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1697 | L1 | any | Search the word error in the package install log (Ubuntu) | `sudo grep -i 'error' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1698 | L1 | any | Search the word error in the system log (Rocky) | `sudo grep -i 'error' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1699 | L1 | any | Search the word error in the system log (Ubuntu) | `sudo grep -i 'error' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1700 | L1 | any | Search timeouts in the Nginx access log | `sudo grep -i 'timeout' /var/log/nginx/access.log` | -i ignores case; add -n for line numbers. |
| T1701 | L1 | any | Search timeouts in the Nginx error log | `sudo grep -i 'timeout' /var/log/nginx/error.log` | -i ignores case; add -n for line numbers. |
| T1702 | L1 | any | Search timeouts in the audit log | `sudo grep -i 'timeout' /var/log/audit/audit.log` | -i ignores case; add -n for line numbers. |
| T1703 | L1 | any | Search timeouts in the authentication log (Rocky) | `sudo grep -i 'timeout' /var/log/secure` | -i ignores case; add -n for line numbers. |
| T1704 | L1 | any | Search timeouts in the authentication log (Ubuntu) | `sudo grep -i 'timeout' /var/log/auth.log` | -i ignores case; add -n for line numbers. |
| T1705 | L1 | any | Search timeouts in the fail2ban log | `sudo grep -i 'timeout' /var/log/fail2ban.log` | -i ignores case; add -n for line numbers. |
| T1706 | L1 | any | Search timeouts in the kernel log (Ubuntu) | `sudo grep -i 'timeout' /var/log/kern.log` | -i ignores case; add -n for line numbers. |
| T1707 | L1 | any | Search timeouts in the package install log (Ubuntu) | `sudo grep -i 'timeout' /var/log/dpkg.log` | -i ignores case; add -n for line numbers. |
| T1708 | L1 | any | Search timeouts in the system log (Rocky) | `sudo grep -i 'timeout' /var/log/messages` | -i ignores case; add -n for line numbers. |
| T1709 | L1 | any | Search timeouts in the system log (Ubuntu) | `sudo grep -i 'timeout' /var/log/syslog` | -i ignores case; add -n for line numbers. |
| T1710 | L2 | any | Count HTTP 404 responses in the Nginx access log | `sudo grep -ci ' 404 ' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1711 | L2 | any | Count HTTP 404 responses in the Nginx error log | `sudo grep -ci ' 404 ' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1712 | L2 | any | Count HTTP 404 responses in the audit log | `sudo grep -ci ' 404 ' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1713 | L2 | any | Count HTTP 404 responses in the authentication log (Rocky) | `sudo grep -ci ' 404 ' /var/log/secure` | -c prints only the number of matching lines. |
| T1714 | L2 | any | Count HTTP 404 responses in the authentication log (Ubuntu) | `sudo grep -ci ' 404 ' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1715 | L2 | any | Count HTTP 404 responses in the fail2ban log | `sudo grep -ci ' 404 ' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1716 | L2 | any | Count HTTP 404 responses in the kernel log (Ubuntu) | `sudo grep -ci ' 404 ' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1717 | L2 | any | Count HTTP 404 responses in the package install log (Ubuntu) | `sudo grep -ci ' 404 ' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1718 | L2 | any | Count HTTP 404 responses in the system log (Rocky) | `sudo grep -ci ' 404 ' /var/log/messages` | -c prints only the number of matching lines. |
| T1719 | L2 | any | Count HTTP 404 responses in the system log (Ubuntu) | `sudo grep -ci ' 404 ' /var/log/syslog` | -c prints only the number of matching lines. |
| T1720 | L2 | any | Count HTTP 500 responses in the Nginx access log | `sudo grep -ci ' 500 ' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1721 | L2 | any | Count HTTP 500 responses in the Nginx error log | `sudo grep -ci ' 500 ' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1722 | L2 | any | Count HTTP 500 responses in the audit log | `sudo grep -ci ' 500 ' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1723 | L2 | any | Count HTTP 500 responses in the authentication log (Rocky) | `sudo grep -ci ' 500 ' /var/log/secure` | -c prints only the number of matching lines. |
| T1724 | L2 | any | Count HTTP 500 responses in the authentication log (Ubuntu) | `sudo grep -ci ' 500 ' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1725 | L2 | any | Count HTTP 500 responses in the fail2ban log | `sudo grep -ci ' 500 ' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1726 | L2 | any | Count HTTP 500 responses in the kernel log (Ubuntu) | `sudo grep -ci ' 500 ' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1727 | L2 | any | Count HTTP 500 responses in the package install log (Ubuntu) | `sudo grep -ci ' 500 ' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1728 | L2 | any | Count HTTP 500 responses in the system log (Rocky) | `sudo grep -ci ' 500 ' /var/log/messages` | -c prints only the number of matching lines. |
| T1729 | L2 | any | Count HTTP 500 responses in the system log (Ubuntu) | `sudo grep -ci ' 500 ' /var/log/syslog` | -c prints only the number of matching lines. |
| T1730 | L2 | any | Count crashes (segfaults) in the Nginx access log | `sudo grep -ci 'segfault' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1731 | L2 | any | Count crashes (segfaults) in the Nginx error log | `sudo grep -ci 'segfault' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1732 | L2 | any | Count crashes (segfaults) in the audit log | `sudo grep -ci 'segfault' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1733 | L2 | any | Count crashes (segfaults) in the authentication log (Rocky) | `sudo grep -ci 'segfault' /var/log/secure` | -c prints only the number of matching lines. |
| T1734 | L2 | any | Count crashes (segfaults) in the authentication log (Ubuntu) | `sudo grep -ci 'segfault' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1735 | L2 | any | Count crashes (segfaults) in the fail2ban log | `sudo grep -ci 'segfault' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1736 | L2 | any | Count crashes (segfaults) in the kernel log (Ubuntu) | `sudo grep -ci 'segfault' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1737 | L2 | any | Count crashes (segfaults) in the package install log (Ubuntu) | `sudo grep -ci 'segfault' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1738 | L2 | any | Count crashes (segfaults) in the system log (Rocky) | `sudo grep -ci 'segfault' /var/log/messages` | -c prints only the number of matching lines. |
| T1739 | L2 | any | Count crashes (segfaults) in the system log (Ubuntu) | `sudo grep -ci 'segfault' /var/log/syslog` | -c prints only the number of matching lines. |
| T1740 | L2 | any | Count failed SSH passwords in the Nginx access log | `sudo grep -ci 'Failed password' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1741 | L2 | any | Count failed SSH passwords in the Nginx error log | `sudo grep -ci 'Failed password' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1742 | L2 | any | Count failed SSH passwords in the audit log | `sudo grep -ci 'Failed password' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1743 | L2 | any | Count failed SSH passwords in the authentication log (Rocky) | `sudo grep -ci 'Failed password' /var/log/secure` | -c prints only the number of matching lines. |
| T1744 | L2 | any | Count failed SSH passwords in the authentication log (Ubuntu) | `sudo grep -ci 'Failed password' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1745 | L2 | any | Count failed SSH passwords in the fail2ban log | `sudo grep -ci 'Failed password' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1746 | L2 | any | Count failed SSH passwords in the kernel log (Ubuntu) | `sudo grep -ci 'Failed password' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1747 | L2 | any | Count failed SSH passwords in the package install log (Ubuntu) | `sudo grep -ci 'Failed password' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1748 | L2 | any | Count failed SSH passwords in the system log (Rocky) | `sudo grep -ci 'Failed password' /var/log/messages` | -c prints only the number of matching lines. |
| T1749 | L2 | any | Count failed SSH passwords in the system log (Ubuntu) | `sudo grep -ci 'Failed password' /var/log/syslog` | -c prints only the number of matching lines. |
| T1750 | L2 | any | Count out-of-memory events in the Nginx access log | `sudo grep -ci 'OOM' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1751 | L2 | any | Count out-of-memory events in the Nginx error log | `sudo grep -ci 'OOM' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1752 | L2 | any | Count out-of-memory events in the audit log | `sudo grep -ci 'OOM' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1753 | L2 | any | Count out-of-memory events in the authentication log (Rocky) | `sudo grep -ci 'OOM' /var/log/secure` | -c prints only the number of matching lines. |
| T1754 | L2 | any | Count out-of-memory events in the authentication log (Ubuntu) | `sudo grep -ci 'OOM' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1755 | L2 | any | Count out-of-memory events in the fail2ban log | `sudo grep -ci 'OOM' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1756 | L2 | any | Count out-of-memory events in the kernel log (Ubuntu) | `sudo grep -ci 'OOM' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1757 | L2 | any | Count out-of-memory events in the package install log (Ubuntu) | `sudo grep -ci 'OOM' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1758 | L2 | any | Count out-of-memory events in the system log (Rocky) | `sudo grep -ci 'OOM' /var/log/messages` | -c prints only the number of matching lines. |
| T1759 | L2 | any | Count out-of-memory events in the system log (Ubuntu) | `sudo grep -ci 'OOM' /var/log/syslog` | -c prints only the number of matching lines. |
| T1760 | L2 | any | Count permission denials in the Nginx access log | `sudo grep -ci 'denied' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1761 | L2 | any | Count permission denials in the Nginx error log | `sudo grep -ci 'denied' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1762 | L2 | any | Count permission denials in the audit log | `sudo grep -ci 'denied' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1763 | L2 | any | Count permission denials in the authentication log (Rocky) | `sudo grep -ci 'denied' /var/log/secure` | -c prints only the number of matching lines. |
| T1764 | L2 | any | Count permission denials in the authentication log (Ubuntu) | `sudo grep -ci 'denied' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1765 | L2 | any | Count permission denials in the fail2ban log | `sudo grep -ci 'denied' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1766 | L2 | any | Count permission denials in the kernel log (Ubuntu) | `sudo grep -ci 'denied' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1767 | L2 | any | Count permission denials in the package install log (Ubuntu) | `sudo grep -ci 'denied' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1768 | L2 | any | Count permission denials in the system log (Rocky) | `sudo grep -ci 'denied' /var/log/messages` | -c prints only the number of matching lines. |
| T1769 | L2 | any | Count permission denials in the system log (Ubuntu) | `sudo grep -ci 'denied' /var/log/syslog` | -c prints only the number of matching lines. |
| T1770 | L2 | any | Count successful key logins in the Nginx access log | `sudo grep -ci 'Accepted publickey' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1771 | L2 | any | Count successful key logins in the Nginx error log | `sudo grep -ci 'Accepted publickey' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1772 | L2 | any | Count successful key logins in the audit log | `sudo grep -ci 'Accepted publickey' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1773 | L2 | any | Count successful key logins in the authentication log (Rocky) | `sudo grep -ci 'Accepted publickey' /var/log/secure` | -c prints only the number of matching lines. |
| T1774 | L2 | any | Count successful key logins in the authentication log (Ubuntu) | `sudo grep -ci 'Accepted publickey' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1775 | L2 | any | Count successful key logins in the fail2ban log | `sudo grep -ci 'Accepted publickey' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1776 | L2 | any | Count successful key logins in the kernel log (Ubuntu) | `sudo grep -ci 'Accepted publickey' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1777 | L2 | any | Count successful key logins in the package install log (Ubuntu) | `sudo grep -ci 'Accepted publickey' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1778 | L2 | any | Count successful key logins in the system log (Rocky) | `sudo grep -ci 'Accepted publickey' /var/log/messages` | -c prints only the number of matching lines. |
| T1779 | L2 | any | Count successful key logins in the system log (Ubuntu) | `sudo grep -ci 'Accepted publickey' /var/log/syslog` | -c prints only the number of matching lines. |
| T1780 | L2 | any | Count sudo usage in the Nginx access log | `sudo grep -ci 'sudo' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1781 | L2 | any | Count sudo usage in the Nginx error log | `sudo grep -ci 'sudo' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1782 | L2 | any | Count sudo usage in the audit log | `sudo grep -ci 'sudo' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1783 | L2 | any | Count sudo usage in the authentication log (Rocky) | `sudo grep -ci 'sudo' /var/log/secure` | -c prints only the number of matching lines. |
| T1784 | L2 | any | Count sudo usage in the authentication log (Ubuntu) | `sudo grep -ci 'sudo' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1785 | L2 | any | Count sudo usage in the fail2ban log | `sudo grep -ci 'sudo' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1786 | L2 | any | Count sudo usage in the kernel log (Ubuntu) | `sudo grep -ci 'sudo' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1787 | L2 | any | Count sudo usage in the package install log (Ubuntu) | `sudo grep -ci 'sudo' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1788 | L2 | any | Count sudo usage in the system log (Rocky) | `sudo grep -ci 'sudo' /var/log/messages` | -c prints only the number of matching lines. |
| T1789 | L2 | any | Count sudo usage in the system log (Ubuntu) | `sudo grep -ci 'sudo' /var/log/syslog` | -c prints only the number of matching lines. |
| T1790 | L2 | any | Count the word error in the Nginx access log | `sudo grep -ci 'error' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1791 | L2 | any | Count the word error in the Nginx error log | `sudo grep -ci 'error' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1792 | L2 | any | Count the word error in the audit log | `sudo grep -ci 'error' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1793 | L2 | any | Count the word error in the authentication log (Rocky) | `sudo grep -ci 'error' /var/log/secure` | -c prints only the number of matching lines. |
| T1794 | L2 | any | Count the word error in the authentication log (Ubuntu) | `sudo grep -ci 'error' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1795 | L2 | any | Count the word error in the fail2ban log | `sudo grep -ci 'error' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1796 | L2 | any | Count the word error in the kernel log (Ubuntu) | `sudo grep -ci 'error' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1797 | L2 | any | Count the word error in the package install log (Ubuntu) | `sudo grep -ci 'error' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1798 | L2 | any | Count the word error in the system log (Rocky) | `sudo grep -ci 'error' /var/log/messages` | -c prints only the number of matching lines. |
| T1799 | L2 | any | Count the word error in the system log (Ubuntu) | `sudo grep -ci 'error' /var/log/syslog` | -c prints only the number of matching lines. |
| T1800 | L2 | any | Count timeouts in the Nginx access log | `sudo grep -ci 'timeout' /var/log/nginx/access.log` | -c prints only the number of matching lines. |
| T1801 | L2 | any | Count timeouts in the Nginx error log | `sudo grep -ci 'timeout' /var/log/nginx/error.log` | -c prints only the number of matching lines. |
| T1802 | L2 | any | Count timeouts in the audit log | `sudo grep -ci 'timeout' /var/log/audit/audit.log` | -c prints only the number of matching lines. |
| T1803 | L2 | any | Count timeouts in the authentication log (Rocky) | `sudo grep -ci 'timeout' /var/log/secure` | -c prints only the number of matching lines. |
| T1804 | L2 | any | Count timeouts in the authentication log (Ubuntu) | `sudo grep -ci 'timeout' /var/log/auth.log` | -c prints only the number of matching lines. |
| T1805 | L2 | any | Count timeouts in the fail2ban log | `sudo grep -ci 'timeout' /var/log/fail2ban.log` | -c prints only the number of matching lines. |
| T1806 | L2 | any | Count timeouts in the kernel log (Ubuntu) | `sudo grep -ci 'timeout' /var/log/kern.log` | -c prints only the number of matching lines. |
| T1807 | L2 | any | Count timeouts in the package install log (Ubuntu) | `sudo grep -ci 'timeout' /var/log/dpkg.log` | -c prints only the number of matching lines. |
| T1808 | L2 | any | Count timeouts in the system log (Rocky) | `sudo grep -ci 'timeout' /var/log/messages` | -c prints only the number of matching lines. |
| T1809 | L2 | any | Count timeouts in the system log (Ubuntu) | `sudo grep -ci 'timeout' /var/log/syslog` | -c prints only the number of matching lines. |
