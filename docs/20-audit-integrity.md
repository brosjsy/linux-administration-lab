# 20. Auditing and file integrity: auditd, AIDE, Lynis

Level: advanced

## auditd: who changed what
```bash
sudo apt install auditd    # Rocky: installed by default
```
`/etc/audit/rules.d/lab.rules`
```
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k sudoers
-w /etc/ssh/sshd_config -p wa -k sshd
-a always,exit -F arch=b64 -S execve -F euid=0 -k root_cmds
```
```bash
sudo augenrules --load
sudo ausearch -k identity -i         # who touched /etc/passwd
sudo aureport --summary
```
Scenario: "Someone added a user last night." Run `ausearch -k identity -ts yesterday -i` and see the user, time and command.

## AIDE: detect changed system files
```bash
sudo apt install aide
sudo aideinit                        # build baseline database
sudo aide --check                    # compare later (run daily from cron)
```

## Lynis: security audit
```bash
sudo lynis audit system
grep -E "warning|suggestion" /var/log/lynis-report.dat | head
```
Record the **Hardening index** before and after applying [18-hardening.md](18-hardening.md).
