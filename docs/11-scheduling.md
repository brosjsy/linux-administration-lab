# 11. Scheduling

## cron
```bash
crontab -e
# m h dom mon dow command
*/15 * * * * /opt/lab/scripts/disk_alert.sh 85 >> /var/log/disk_alert.log 2>&1
0 2 * * *    /opt/lab/scripts/backup.sh /etc /srv/backups 7
crontab -l; grep CRON /var/log/syslog
```
## systemd timer
`/etc/systemd/system/healthcheck.timer`
```ini
[Timer]
OnCalendar=hourly
Persistent=true
[Install]
WantedBy=timers.target
```
```bash
sudo systemctl enable --now healthcheck.timer && systemctl list-timers
```

More real-world cron scenarios: [16-cron-scenarios.md](16-cron-scenarios.md). Deploying jobs to many servers: [17-ansible.md](17-ansible.md).
