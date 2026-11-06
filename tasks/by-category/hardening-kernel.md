# Hardening: kernel (48 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1535 | L3 | any | Check current value of fs.file-max | `sysctl fs.file-max` | Recommended 2097152: system-wide open files limit. |
| T1536 | L3 | any | Check current value of fs.suid_dumpable | `sysctl fs.suid_dumpable` | Recommended 0: no core dumps from SUID programs. |
| T1537 | L3 | any | Check current value of kernel.dmesg_restrict | `sysctl kernel.dmesg_restrict` | Recommended 1: only root reads kernel log. |
| T1538 | L3 | any | Check current value of kernel.kptr_restrict | `sysctl kernel.kptr_restrict` | Recommended 2: hide kernel pointers. |
| T1539 | L3 | any | Check current value of kernel.randomize_va_space | `sysctl kernel.randomize_va_space` | Recommended 2: full ASLR. |
| T1540 | L3 | any | Check current value of net.core.somaxconn | `sysctl net.core.somaxconn` | Recommended 4096: bigger listen backlog for busy servers. |
| T1541 | L3 | any | Check current value of net.ipv4.conf.all.accept_redirects | `sysctl net.ipv4.conf.all.accept_redirects` | Recommended 0: ignore ICMP redirects. |
| T1542 | L3 | any | Check current value of net.ipv4.conf.all.log_martians | `sysctl net.ipv4.conf.all.log_martians` | Recommended 1: log impossible source addresses. |
| T1543 | L3 | any | Check current value of net.ipv4.conf.all.rp_filter | `sysctl net.ipv4.conf.all.rp_filter` | Recommended 1: reverse path filtering against spoofing. |
| T1544 | L3 | any | Check current value of net.ipv4.conf.all.send_redirects | `sysctl net.ipv4.conf.all.send_redirects` | Recommended 0: do not send ICMP redirects. |
| T1545 | L3 | any | Check current value of net.ipv4.icmp_echo_ignore_broadcasts | `sysctl net.ipv4.icmp_echo_ignore_broadcasts` | Recommended 1: ignore broadcast pings. |
| T1546 | L3 | any | Check current value of net.ipv4.ip_forward | `sysctl net.ipv4.ip_forward` | Recommended 0: disable routing between interfaces. |
| T1547 | L3 | any | Check current value of net.ipv4.ip_local_port_range | `sysctl net.ipv4.ip_local_port_range` | Recommended "10240 65535": more ephemeral ports for many outgoing connections. |
| T1548 | L3 | any | Check current value of net.ipv4.tcp_syncookies | `sysctl net.ipv4.tcp_syncookies` | Recommended 1: protect from SYN flood. |
| T1549 | L3 | any | Check current value of vm.overcommit_memory | `sysctl vm.overcommit_memory` | Recommended 1: allow memory overcommit (Redis recommendation). |
| T1550 | L3 | any | Check current value of vm.swappiness | `sysctl vm.swappiness` | Recommended 10: prefer RAM over swap. |
| T1551 | L3 | any | Set fs.file-max = 2097152 now (system-wide open files limit) | `sudo sysctl -w fs.file-max=2097152` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1552 | L3 | any | Set fs.suid_dumpable = 0 now (no core dumps from SUID programs) | `sudo sysctl -w fs.suid_dumpable=0` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1553 | L3 | any | Set kernel.dmesg_restrict = 1 now (only root reads kernel log) | `sudo sysctl -w kernel.dmesg_restrict=1` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1554 | L3 | any | Set kernel.kptr_restrict = 2 now (hide kernel pointers) | `sudo sysctl -w kernel.kptr_restrict=2` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1555 | L3 | any | Set kernel.randomize_va_space = 2 now (full ASLR) | `sudo sysctl -w kernel.randomize_va_space=2` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1556 | L3 | any | Set net.core.somaxconn = 4096 now (bigger listen backlog for busy servers) | `sudo sysctl -w net.core.somaxconn=4096` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1557 | L3 | any | Set net.ipv4.conf.all.accept_redirects = 0 now (ignore ICMP redirects) | `sudo sysctl -w net.ipv4.conf.all.accept_redirects=0` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1558 | L3 | any | Set net.ipv4.conf.all.log_martians = 1 now (log impossible source addresses) | `sudo sysctl -w net.ipv4.conf.all.log_martians=1` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1559 | L3 | any | Set net.ipv4.conf.all.rp_filter = 1 now (reverse path filtering against spoofing) | `sudo sysctl -w net.ipv4.conf.all.rp_filter=1` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1560 | L3 | any | Set net.ipv4.conf.all.send_redirects = 0 now (do not send ICMP redirects) | `sudo sysctl -w net.ipv4.conf.all.send_redirects=0` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1561 | L3 | any | Set net.ipv4.icmp_echo_ignore_broadcasts = 1 now (ignore broadcast pings) | `sudo sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1562 | L3 | any | Set net.ipv4.ip_forward = 0 now (disable routing between interfaces) | `sudo sysctl -w net.ipv4.ip_forward=0` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1563 | L3 | any | Set net.ipv4.ip_local_port_range = "10240 65535" now (more ephemeral ports for many outgoing connections) | `sudo sysctl -w net.ipv4.ip_local_port_range="10240 65535"` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1564 | L3 | any | Set net.ipv4.tcp_syncookies = 1 now (protect from SYN flood) | `sudo sysctl -w net.ipv4.tcp_syncookies=1` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1565 | L3 | any | Set vm.overcommit_memory = 1 now (allow memory overcommit (Redis recommendation)) | `sudo sysctl -w vm.overcommit_memory=1` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1566 | L3 | any | Set vm.swappiness = 10 now (prefer RAM over swap) | `sudo sysctl -w vm.swappiness=10` | Lost after reboot; persist it in /etc/sysctl.d/. |
| T1567 | L4 | any | Persist fs.file-max = 2097152 across reboots | `echo 'fs.file-max = 2097152' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | System-wide open files limit. |
| T1568 | L4 | any | Persist fs.suid_dumpable = 0 across reboots | `echo 'fs.suid_dumpable = 0' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | No core dumps from suid programs. |
| T1569 | L4 | any | Persist kernel.dmesg_restrict = 1 across reboots | `echo 'kernel.dmesg_restrict = 1' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Only root reads kernel log. |
| T1570 | L4 | any | Persist kernel.kptr_restrict = 2 across reboots | `echo 'kernel.kptr_restrict = 2' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Hide kernel pointers. |
| T1571 | L4 | any | Persist kernel.randomize_va_space = 2 across reboots | `echo 'kernel.randomize_va_space = 2' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Full aslr. |
| T1572 | L4 | any | Persist net.core.somaxconn = 4096 across reboots | `echo 'net.core.somaxconn = 4096' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Bigger listen backlog for busy servers. |
| T1573 | L4 | any | Persist net.ipv4.conf.all.accept_redirects = 0 across reboots | `echo 'net.ipv4.conf.all.accept_redirects = 0' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Ignore icmp redirects. |
| T1574 | L4 | any | Persist net.ipv4.conf.all.log_martians = 1 across reboots | `echo 'net.ipv4.conf.all.log_martians = 1' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Log impossible source addresses. |
| T1575 | L4 | any | Persist net.ipv4.conf.all.rp_filter = 1 across reboots | `echo 'net.ipv4.conf.all.rp_filter = 1' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Reverse path filtering against spoofing. |
| T1576 | L4 | any | Persist net.ipv4.conf.all.send_redirects = 0 across reboots | `echo 'net.ipv4.conf.all.send_redirects = 0' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Do not send icmp redirects. |
| T1577 | L4 | any | Persist net.ipv4.icmp_echo_ignore_broadcasts = 1 across reboots | `echo 'net.ipv4.icmp_echo_ignore_broadcasts = 1' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Ignore broadcast pings. |
| T1578 | L4 | any | Persist net.ipv4.ip_forward = 0 across reboots | `echo 'net.ipv4.ip_forward = 0' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Disable routing between interfaces. |
| T1579 | L4 | any | Persist net.ipv4.ip_local_port_range = "10240 65535" across reboots | `echo 'net.ipv4.ip_local_port_range = 10240 65535' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | More ephemeral ports for many outgoing connections. |
| T1580 | L4 | any | Persist net.ipv4.tcp_syncookies = 1 across reboots | `echo 'net.ipv4.tcp_syncookies = 1' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Protect from syn flood. |
| T1581 | L4 | any | Persist vm.overcommit_memory = 1 across reboots | `echo 'vm.overcommit_memory = 1' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Allow memory overcommit (redis recommendation). |
| T1582 | L4 | any | Persist vm.swappiness = 10 across reboots | `echo 'vm.swappiness = 10' \| sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system` | Prefer ram over swap. |
