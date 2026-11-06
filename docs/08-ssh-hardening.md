# 08. SSH and hardening

```bash
ssh-keygen -t ed25519 -C "joseph@lab"
ssh-copy-id alice@192.168.56.10
```
`/etc/ssh/sshd_config.d/10-hardening.conf`
```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
AllowGroups ssh-users
```
```bash
sudo sshd -t && sudo systemctl reload ssh   # test syntax before reload
sudo apt install fail2ban && sudo systemctl enable --now fail2ban
sudo fail2ban-client status sshd
```
Rule: keep a second session open while changing SSH settings, so a mistake does not lock you out.

Full hardening checklist: [18-hardening.md](18-hardening.md). Check a server with `scripts/harden_audit.sh`.
