# 16. Cron in practice: real scenarios

Level: beginner to professional

## Syntax reminder
```
# ┌ minute (0-59)
# │ ┌ hour (0-23)
# │ │ ┌ day of month (1-31)
# │ │ │ ┌ month (1-12)
# │ │ │ │ ┌ day of week (0-7, 0 and 7 = Sunday)
# * * * * * command
```
| Shortcut | Same as |
|----------|---------|
| `@reboot` | once at boot |
| `@hourly` | `0 * * * *` |
| `@daily` | `0 0 * * *` |
| `@weekly` | `0 0 * * 0` |

## Where cron jobs live
| Location | Who | Notes |
|----------|-----|-------|
| `crontab -e` | per user | stored in `/var/spool/cron/` |
| `/etc/crontab` | system | has an extra **user** field |
| `/etc/cron.d/*` | packages and admins | extra user field, best for deployed jobs |
| `/etc/cron.daily/` etc. | run-parts | scripts without dots in the name |
| `anacron` | laptops and VMs that sleep | runs missed daily/weekly jobs later |

## Scenarios

### S1. Daily backup at 02:30 (beginner)
```
30 2 * * * /opt/lab/scripts/backup.sh /etc /srv/backups 14 >> /var/log/backup.log 2>&1
```

### S2. Disk check every 15 minutes, working hours only, Monday to Friday
```
*/15 8-20 * * 1-5 /opt/lab/scripts/disk_alert.sh 85 >> /var/log/disk_alert.log 2>&1
```

### S3. Last day of the month report
Cron has no "last day" field, so test the date inside the job:
```
55 23 28-31 * * [ "$(date -d tomorrow +\%d)" = "01" ] && /opt/lab/scripts/log_report.sh "1 month ago" > /srv/reports/monthly-$(date +\%Y\%m).txt
```
Note: `%` must be escaped as `\%` inside crontab.

### S4. Stop a job from running twice (flock)
If a backup takes longer than its interval, two copies overlap. Use a lock:
```
*/10 * * * * flock -n /run/lock/sync.lock /opt/lab/scripts/cron_wrapper.sh sync rsync -a /srv/share/ backup:/share/
```

### S5. Job works in the terminal but not in cron (classic ticket)
Causes: different `PATH`, no environment variables, relative paths, no permissions, `%` not escaped.
Fix: absolute paths, set `PATH` at the top of the crontab, log stdout and stderr:
```
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
MAILTO=""
```
Debug: `grep CRON /var/log/syslog` (Ubuntu) or `journalctl -u crond` (Rocky).

### S6. Clean old temporary files every night
```
0 3 * * * find /srv/uploads/tmp -type f -mtime +7 -delete
```

### S7. Rotate a custom app log weekly with a deployed job
`/etc/cron.d/app-maintenance`
```
0 4 * * 0 root /usr/sbin/logrotate /etc/logrotate.d/lab-app
```

### S8. Run at boot
```
@reboot sleep 60 && /opt/lab/scripts/service_watchdog.sh nginx ssh
```

### S9. Restrict who may use cron
`/etc/cron.allow` (only listed users) or `/etc/cron.deny`.

### S10. Professional: replace cron with a systemd timer
Timers give logging in the journal, randomised delay, catch-up after downtime and dependencies.
```ini
# /etc/systemd/system/backup.service
[Service]
Type=oneshot
ExecStart=/opt/lab/scripts/backup.sh /etc /srv/backups 14

# /etc/systemd/system/backup.timer
[Timer]
OnCalendar=*-*-* 02:30
RandomizedDelaySec=10m
Persistent=true
[Install]
WantedBy=timers.target
```
```bash
sudo systemctl enable --now backup.timer
systemctl list-timers
journalctl -u backup.service
```

### S11. Deploy cron jobs to 50 servers at once
Use Ansible: see [`ansible/playbooks/06-cron-jobs.yml`](../ansible/playbooks/06-cron-jobs.yml).

## Check yourself
- [x] Explain why a job works by hand but fails in cron
- [x] Prevent overlapping runs with `flock`
- [x] Convert one cron job to a systemd timer
