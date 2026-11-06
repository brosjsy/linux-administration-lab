# Runbook: disk full

**Symptoms:** `No space left on device`, application errors, logs stop.

**Quick checks**
```bash
df -h; df -i                                   # space AND inodes
sudo du -xh / --max-depth=2 2>/dev/null | sort -h | tail -15
sudo find /var/log -type f -size +100M -exec ls -lh {} +
sudo lsof +L1                                  # deleted files still held open
```
**Likely causes:** runaway logs, old backups, package cache, deleted file held by a process, too many small files (inodes).

**Fix**
```bash
sudo journalctl --vacuum-size=200M
sudo apt clean            # or: sudo dnf clean all
sudo truncate -s 0 /var/log/app/huge.log       # never rm a log a process is writing
sudo systemctl restart <service>               # frees space held by deleted files
```
**Verify:** `df -h` back under 80%. **Prevent:** logrotate, `scripts/disk_alert.sh` in cron, LVM extend if growth is real.
