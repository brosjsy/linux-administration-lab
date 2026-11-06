# 10. Logs and monitoring

```bash
journalctl -p err -b                 # errors since boot
journalctl -u ssh --since today
journalctl -f                        # follow live
tail -f /var/log/auth.log            # Debian; /var/log/secure on RHEL
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head
uptime; free -h; df -h; vmstat 1 5; iostat -xz 1 3; sar -u 1 3
dmesg -T | tail
```
## logrotate
`/etc/logrotate.d/lab-app`
```
/var/log/lab-app/*.log {
    daily
    rotate 14
    compress
    missingok
    notifempty
}
```
`sudo logrotate -d /etc/logrotate.d/lab-app` (dry run).

## Monitoring basics
What to watch: CPU load vs cores, memory and swap, disk space and inodes (`df -i`), failed units, certificate expiry, backup success. In the lab: `node_exporter` + Prometheus + Grafana, and `scripts/disk_alert.sh` from cron.
