# Runbook: user cannot connect via SSH

1. From the client: `ssh -v user@host` (read where it stops).
2. Network: `ping host`, `nc -zv host 22`.
3. On the server (console): `systemctl status ssh`, `ss -tlnp | grep :22`.
4. Firewall: `sudo ufw status` / `sudo firewall-cmd --list-all`.
5. Account: `sudo chage -l user`, `passwd -S user` (locked/expired?).
6. Keys: `~/.ssh` is 700, `authorized_keys` is 600, owned by the user.
7. Logs: `journalctl -u ssh -n 50`, `sudo fail2ban-client status sshd` (IP banned?).

**Verify:** user logs in. **Write up:** cause and fix in the ticket, add to KB if new.
