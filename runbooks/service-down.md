# Runbook: service down (example: nginx)

```bash
systemctl status nginx
journalctl -u nginx -n 50 --no-pager
sudo nginx -t                         # config syntax
ss -tlnp | grep -E ':80|:443'         # port taken by something else?
df -h /var                            # disk full?
```
**Fix:** correct the config error, free the port or disk, then `sudo systemctl restart nginx`.
**Verify:** `curl -I http://localhost` returns 200/301. **Prevent:** `nginx -t` before every reload, `scripts/service_watchdog.sh`.
