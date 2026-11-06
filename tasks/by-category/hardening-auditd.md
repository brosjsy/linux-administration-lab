# Hardening: auditd (16 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1519 | L4 | any | Audit every write to /etc/crontab | `sudo auditctl -w /etc/crontab -p wa -k crontab` | Persist the rule in /etc/audit/rules.d/. |
| T1520 | L4 | any | Audit every write to /etc/fstab | `sudo auditctl -w /etc/fstab -p wa -k fstab` | Persist the rule in /etc/audit/rules.d/. |
| T1521 | L4 | any | Audit every write to /etc/group | `sudo auditctl -w /etc/group -p wa -k group` | Persist the rule in /etc/audit/rules.d/. |
| T1522 | L4 | any | Audit every write to /etc/hosts | `sudo auditctl -w /etc/hosts -p wa -k hosts` | Persist the rule in /etc/audit/rules.d/. |
| T1523 | L4 | any | Audit every write to /etc/passwd | `sudo auditctl -w /etc/passwd -p wa -k passwd` | Persist the rule in /etc/audit/rules.d/. |
| T1524 | L4 | any | Audit every write to /etc/shadow | `sudo auditctl -w /etc/shadow -p wa -k shadow` | Persist the rule in /etc/audit/rules.d/. |
| T1525 | L4 | any | Audit every write to /etc/ssh/sshd_config | `sudo auditctl -w /etc/ssh/sshd_config -p wa -k sshd_config` | Persist the rule in /etc/audit/rules.d/. |
| T1526 | L4 | any | Audit every write to /etc/sudoers | `sudo auditctl -w /etc/sudoers -p wa -k sudoers` | Persist the rule in /etc/audit/rules.d/. |
| T1527 | L4 | any | Find who changed /etc/crontab | `sudo ausearch -k crontab -i` | Shows user, time, program and result. |
| T1528 | L4 | any | Find who changed /etc/fstab | `sudo ausearch -k fstab -i` | Shows user, time, program and result. |
| T1529 | L4 | any | Find who changed /etc/group | `sudo ausearch -k group -i` | Shows user, time, program and result. |
| T1530 | L4 | any | Find who changed /etc/hosts | `sudo ausearch -k hosts -i` | Shows user, time, program and result. |
| T1531 | L4 | any | Find who changed /etc/passwd | `sudo ausearch -k passwd -i` | Shows user, time, program and result. |
| T1532 | L4 | any | Find who changed /etc/shadow | `sudo ausearch -k shadow -i` | Shows user, time, program and result. |
| T1533 | L4 | any | Find who changed /etc/ssh/sshd_config | `sudo ausearch -k sshd_config -i` | Shows user, time, program and result. |
| T1534 | L4 | any | Find who changed /etc/sudoers | `sudo ausearch -k sudoers -i` | Shows user, time, program and result. |
