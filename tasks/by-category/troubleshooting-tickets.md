# Troubleshooting tickets (18 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T4236 | L2 | any | Ticket: Backup job reports success but files are missing | `tar -tzf /srv/backups/latest.tar.gz \| head; check exclude rules` | Always test restores. |
| T4237 | L2 | any | Ticket: Certificate expired warning in browser | `/opt/lab/scripts/ssl_expiry_check.sh site.example.ru` | Renew, reload web server, monitor expiry. |
| T4238 | L2 | any | Ticket: Clock is wrong and Kerberos login fails | `timedatectl; chronyc sources` | Fix NTP; Kerberos allows only 5 minutes skew. |
| T4239 | L2 | any | Ticket: Cron job did not run | `grep CRON /var/log/syslog \| tail; crontab -l; ls -l /path/to/script` | PATH, permissions or % escaping; docs/16-cron-scenarios.md. |
| T4240 | L2 | any | Ticket: Docker host disk full | `docker system df; docker system prune` | Old images and logs; set log rotation in daemon.json. |
| T4241 | L2 | any | Ticket: Domain names do not resolve | `resolvectl status; dig ya.ru; dig @8.8.8.8 ya.ru` | runbooks/dns-failure.md. |
| T4242 | L2 | any | Ticket: High memory usage and OOM kills | `free -h; ps aux --sort=-%mem \| head; journalctl -k \| grep -i oom` | Find the leak, set MemoryMax, add swap if needed. |
| T4243 | L2 | any | Ticket: Host unreachable alert from monitoring | `ping host; ip neigh; ssh host; check console` | Network, firewall or host down; escalate with facts. |
| T4244 | L2 | any | Ticket: Login to directory account fails | `realm list; systemctl status sssd; sudo sss_cache -E` | SSSD cache or domain trust problem. |
| T4245 | L2 | any | Ticket: No space left on device | `df -h; df -i; sudo du -xh / --max-depth=2 \| sort -h \| tail; sudo lsof +L1` | runbooks/disk-full.md. |
| T4246 | L2 | any | Ticket: Package install fails with lock error (Ubuntu) | `ps aux \| grep -E 'apt\|dpkg'; sudo lsof /var/lib/dpkg/lock-frontend` | Wait for unattended-upgrades; never delete the lock blindly. |
| T4247 | L2 | any | Ticket: Permission denied on a shared folder | `id user; ls -ld /srv/share; getfacl /srv/share; ls -Z /srv/share` | Check groups, mode, ACL and SELinux context. |
| T4248 | L2 | any | Ticket: Server is slow | `uptime; top -o %CPU; vmstat 1 5; iostat -xz 1 3` | Check load vs cores, IO wait and swap; runbooks/high-load.md. |
| T4249 | L2 | any | Ticket: Server went into emergency mode after reboot | `journalctl -xb \| grep -i mount; cat /etc/fstab` | Usually a bad fstab line; docs/24-boot-recovery.md. |
| T4250 | L2 | any | Ticket: Service fails to start after config change | `systemctl status SERVICE; journalctl -u SERVICE -n 50; nginx -t` | Validate config syntax and read the first error. |
| T4251 | L2 | any | Ticket: Too many open files | `systemctl show SERVICE -p LimitNOFILE; ls /proc/PID/fd \| wc -l` | Raise LimitNOFILE in a drop-in; docs/25-performance-tuning.md. |
| T4252 | L2 | any | Ticket: User cannot SSH in | `ssh -v user@host; sudo chage -l user; journalctl -u ssh -n 50` | runbooks/ssh-access.md. |
| T4253 | L2 | any | Ticket: Website returns 502 Bad Gateway | `systemctl status nginx; journalctl -u nginx -n 50; ss -tlnp \| grep -E ':80\|:8080'` | Backend is down or Nginx cannot reach it; see runbooks/service-down.md. |
