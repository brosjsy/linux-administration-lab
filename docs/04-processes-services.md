# 04. Processes and services (systemd)

```bash
ps aux --sort=-%cpu | head
top / htop                         # live view, k to kill
pgrep -a nginx; kill -15 <PID>; kill -9 <PID>
nice -n 10 cmd; renice 5 -p <PID>
systemctl status nginx
sudo systemctl enable --now nginx
systemctl list-units --failed
systemctl list-unit-files --state=enabled
journalctl -u nginx --since "1 hour ago"
systemd-analyze blame | head      # slow boot services
```

## Custom service unit
`/etc/systemd/system/healthcheck.service`
```ini
[Unit]
Description=Lab health check
[Service]
Type=oneshot
ExecStart=/opt/lab/scripts/health_check.sh
```
```bash
sudo systemctl daemon-reload && sudo systemctl start healthcheck
```
