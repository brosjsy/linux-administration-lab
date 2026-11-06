# 12. Backup and restore

```bash
sudo tar -czpf /srv/backups/etc-$(date +%F).tar.gz /etc
tar -tzf /srv/backups/etc-2026-11-06.tar.gz | head     # verify contents
rsync -aAXv --delete /srv/share/ backup-host:/backups/share/
```
## Restore test (the backup only counts if restore works)
```bash
mkdir /tmp/restore && tar -xzf /srv/backups/etc-*.tar.gz -C /tmp/restore
diff -r /etc/ssh /tmp/restore/etc/ssh && echo "restore OK"
```
3-2-1 rule: 3 copies, 2 different media, 1 off-site. Automated with `scripts/backup.sh` + cron.
