# Backup and archives (72 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T0171 | L1 | any | Archive /etc with bzip2 (smaller, slower) | `sudo tar -cjpf /srv/backups/etc.tar.bz2 /etc` | -p keeps permissions. |
| T0172 | L1 | any | Archive /etc with gzip (fast, common) | `sudo tar -czpf /srv/backups/etc.tar.gz /etc` | -p keeps permissions. |
| T0173 | L1 | any | Archive /etc with xz (smallest, slowest) | `sudo tar -cJpf /srv/backups/etc.tar.xz /etc` | -p keeps permissions. |
| T0174 | L1 | any | Archive /etc with zstd (fast and small) | `sudo tar --zstd -cpf /srv/backups/etc.tar.zst /etc` | -p keeps permissions. |
| T0175 | L1 | any | Archive /home/ivan with bzip2 (smaller, slower) | `sudo tar -cjpf /srv/backups/home-ivan.tar.bz2 /home/ivan` | -p keeps permissions. |
| T0176 | L1 | any | Archive /home/ivan with gzip (fast, common) | `sudo tar -czpf /srv/backups/home-ivan.tar.gz /home/ivan` | -p keeps permissions. |
| T0177 | L1 | any | Archive /home/ivan with xz (smallest, slowest) | `sudo tar -cJpf /srv/backups/home-ivan.tar.xz /home/ivan` | -p keeps permissions. |
| T0178 | L1 | any | Archive /home/ivan with zstd (fast and small) | `sudo tar --zstd -cpf /srv/backups/home-ivan.tar.zst /home/ivan` | -p keeps permissions. |
| T0179 | L1 | any | Archive /opt/app with bzip2 (smaller, slower) | `sudo tar -cjpf /srv/backups/opt-app.tar.bz2 /opt/app` | -p keeps permissions. |
| T0180 | L1 | any | Archive /opt/app with gzip (fast, common) | `sudo tar -czpf /srv/backups/opt-app.tar.gz /opt/app` | -p keeps permissions. |
| T0181 | L1 | any | Archive /opt/app with xz (smallest, slowest) | `sudo tar -cJpf /srv/backups/opt-app.tar.xz /opt/app` | -p keeps permissions. |
| T0182 | L1 | any | Archive /opt/app with zstd (fast and small) | `sudo tar --zstd -cpf /srv/backups/opt-app.tar.zst /opt/app` | -p keeps permissions. |
| T0183 | L1 | any | Archive /srv/share with bzip2 (smaller, slower) | `sudo tar -cjpf /srv/backups/srv-share.tar.bz2 /srv/share` | -p keeps permissions. |
| T0184 | L1 | any | Archive /srv/share with gzip (fast, common) | `sudo tar -czpf /srv/backups/srv-share.tar.gz /srv/share` | -p keeps permissions. |
| T0185 | L1 | any | Archive /srv/share with xz (smallest, slowest) | `sudo tar -cJpf /srv/backups/srv-share.tar.xz /srv/share` | -p keeps permissions. |
| T0186 | L1 | any | Archive /srv/share with zstd (fast and small) | `sudo tar --zstd -cpf /srv/backups/srv-share.tar.zst /srv/share` | -p keeps permissions. |
| T0187 | L1 | any | Archive /var/www with bzip2 (smaller, slower) | `sudo tar -cjpf /srv/backups/var-www.tar.bz2 /var/www` | -p keeps permissions. |
| T0188 | L1 | any | Archive /var/www with gzip (fast, common) | `sudo tar -czpf /srv/backups/var-www.tar.gz /var/www` | -p keeps permissions. |
| T0189 | L1 | any | Archive /var/www with xz (smallest, slowest) | `sudo tar -cJpf /srv/backups/var-www.tar.xz /var/www` | -p keeps permissions. |
| T0190 | L1 | any | Archive /var/www with zstd (fast and small) | `sudo tar --zstd -cpf /srv/backups/var-www.tar.zst /var/www` | -p keeps permissions. |
| T0191 | L1 | any | List the contents of the bz2 archive of /etc | `tar -tjf /srv/backups/etc.tar.bz2 \| head` | Verify a backup without extracting. |
| T0192 | L1 | any | List the contents of the bz2 archive of /home/ivan | `tar -tjf /srv/backups/home-ivan.tar.bz2 \| head` | Verify a backup without extracting. |
| T0193 | L1 | any | List the contents of the bz2 archive of /opt/app | `tar -tjf /srv/backups/opt-app.tar.bz2 \| head` | Verify a backup without extracting. |
| T0194 | L1 | any | List the contents of the bz2 archive of /srv/share | `tar -tjf /srv/backups/srv-share.tar.bz2 \| head` | Verify a backup without extracting. |
| T0195 | L1 | any | List the contents of the bz2 archive of /var/www | `tar -tjf /srv/backups/var-www.tar.bz2 \| head` | Verify a backup without extracting. |
| T0196 | L1 | any | List the contents of the gz archive of /etc | `tar -tzf /srv/backups/etc.tar.gz \| head` | Verify a backup without extracting. |
| T0197 | L1 | any | List the contents of the gz archive of /home/ivan | `tar -tzf /srv/backups/home-ivan.tar.gz \| head` | Verify a backup without extracting. |
| T0198 | L1 | any | List the contents of the gz archive of /opt/app | `tar -tzf /srv/backups/opt-app.tar.gz \| head` | Verify a backup without extracting. |
| T0199 | L1 | any | List the contents of the gz archive of /srv/share | `tar -tzf /srv/backups/srv-share.tar.gz \| head` | Verify a backup without extracting. |
| T0200 | L1 | any | List the contents of the gz archive of /var/www | `tar -tzf /srv/backups/var-www.tar.gz \| head` | Verify a backup without extracting. |
| T0201 | L1 | any | List the contents of the xz archive of /etc | `tar -tJf /srv/backups/etc.tar.xz \| head` | Verify a backup without extracting. |
| T0202 | L1 | any | List the contents of the xz archive of /home/ivan | `tar -tJf /srv/backups/home-ivan.tar.xz \| head` | Verify a backup without extracting. |
| T0203 | L1 | any | List the contents of the xz archive of /opt/app | `tar -tJf /srv/backups/opt-app.tar.xz \| head` | Verify a backup without extracting. |
| T0204 | L1 | any | List the contents of the xz archive of /srv/share | `tar -tJf /srv/backups/srv-share.tar.xz \| head` | Verify a backup without extracting. |
| T0205 | L1 | any | List the contents of the xz archive of /var/www | `tar -tJf /srv/backups/var-www.tar.xz \| head` | Verify a backup without extracting. |
| T0206 | L1 | any | List the contents of the zst archive of /etc | `tar --zstd -tf /srv/backups/etc.tar.zst \| head` | Verify a backup without extracting. |
| T0207 | L1 | any | List the contents of the zst archive of /home/ivan | `tar --zstd -tf /srv/backups/home-ivan.tar.zst \| head` | Verify a backup without extracting. |
| T0208 | L1 | any | List the contents of the zst archive of /opt/app | `tar --zstd -tf /srv/backups/opt-app.tar.zst \| head` | Verify a backup without extracting. |
| T0209 | L1 | any | List the contents of the zst archive of /srv/share | `tar --zstd -tf /srv/backups/srv-share.tar.zst \| head` | Verify a backup without extracting. |
| T0210 | L1 | any | List the contents of the zst archive of /var/www | `tar --zstd -tf /srv/backups/var-www.tar.zst \| head` | Verify a backup without extracting. |
| T0211 | L2 | any | Dry-run a mirror of /etc/ to see what would change | `rsync -aAXvn --delete /etc/ backup-host:/backups/etc/` | -n shows actions without doing them. |
| T0212 | L2 | any | Dry-run a mirror of /home/ to see what would change | `rsync -aAXvn --delete /home/ backup-host:/backups/home/` | -n shows actions without doing them. |
| T0213 | L2 | any | Dry-run a mirror of /srv/share/ to see what would change | `rsync -aAXvn --delete /srv/share/ backup-host:/backups/srv/share/` | -n shows actions without doing them. |
| T0214 | L2 | any | Dry-run a mirror of /var/www/ to see what would change | `rsync -aAXvn --delete /var/www/ backup-host:/backups/var/www/` | -n shows actions without doing them. |
| T0215 | L2 | any | Mirror /etc/ to backup-host over SSH | `rsync -aAXv --delete /etc/ backup-host:/backups/etc/` | --delete makes an exact mirror; test with -n first. |
| T0216 | L2 | any | Mirror /home/ to backup-host over SSH | `rsync -aAXv --delete /home/ backup-host:/backups/home/` | --delete makes an exact mirror; test with -n first. |
| T0217 | L2 | any | Mirror /srv/share/ to backup-host over SSH | `rsync -aAXv --delete /srv/share/ backup-host:/backups/srv/share/` | --delete makes an exact mirror; test with -n first. |
| T0218 | L2 | any | Mirror /var/www/ to backup-host over SSH | `rsync -aAXv --delete /var/www/ backup-host:/backups/var/www/` | --delete makes an exact mirror; test with -n first. |
| T0219 | L2 | any | Restore the bz2 archive of /etc into /tmp/restore | `sudo tar -xjpf /srv/backups/etc.tar.bz2 -C /tmp/restore` | Restore to a test path first, then compare. |
| T0220 | L2 | any | Restore the bz2 archive of /home/ivan into /tmp/restore | `sudo tar -xjpf /srv/backups/home-ivan.tar.bz2 -C /tmp/restore` | Restore to a test path first, then compare. |
| T0221 | L2 | any | Restore the bz2 archive of /opt/app into /tmp/restore | `sudo tar -xjpf /srv/backups/opt-app.tar.bz2 -C /tmp/restore` | Restore to a test path first, then compare. |
| T0222 | L2 | any | Restore the bz2 archive of /srv/share into /tmp/restore | `sudo tar -xjpf /srv/backups/srv-share.tar.bz2 -C /tmp/restore` | Restore to a test path first, then compare. |
| T0223 | L2 | any | Restore the bz2 archive of /var/www into /tmp/restore | `sudo tar -xjpf /srv/backups/var-www.tar.bz2 -C /tmp/restore` | Restore to a test path first, then compare. |
| T0224 | L2 | any | Restore the gz archive of /etc into /tmp/restore | `sudo tar -xzpf /srv/backups/etc.tar.gz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0225 | L2 | any | Restore the gz archive of /home/ivan into /tmp/restore | `sudo tar -xzpf /srv/backups/home-ivan.tar.gz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0226 | L2 | any | Restore the gz archive of /opt/app into /tmp/restore | `sudo tar -xzpf /srv/backups/opt-app.tar.gz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0227 | L2 | any | Restore the gz archive of /srv/share into /tmp/restore | `sudo tar -xzpf /srv/backups/srv-share.tar.gz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0228 | L2 | any | Restore the gz archive of /var/www into /tmp/restore | `sudo tar -xzpf /srv/backups/var-www.tar.gz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0229 | L2 | any | Restore the xz archive of /etc into /tmp/restore | `sudo tar -xJpf /srv/backups/etc.tar.xz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0230 | L2 | any | Restore the xz archive of /home/ivan into /tmp/restore | `sudo tar -xJpf /srv/backups/home-ivan.tar.xz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0231 | L2 | any | Restore the xz archive of /opt/app into /tmp/restore | `sudo tar -xJpf /srv/backups/opt-app.tar.xz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0232 | L2 | any | Restore the xz archive of /srv/share into /tmp/restore | `sudo tar -xJpf /srv/backups/srv-share.tar.xz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0233 | L2 | any | Restore the xz archive of /var/www into /tmp/restore | `sudo tar -xJpf /srv/backups/var-www.tar.xz -C /tmp/restore` | Restore to a test path first, then compare. |
| T0234 | L2 | any | Restore the zst archive of /etc into /tmp/restore | `sudo tar --zstd -xpf /srv/backups/etc.tar.zst -C /tmp/restore` | Restore to a test path first, then compare. |
| T0235 | L2 | any | Restore the zst archive of /home/ivan into /tmp/restore | `sudo tar --zstd -xpf /srv/backups/home-ivan.tar.zst -C /tmp/restore` | Restore to a test path first, then compare. |
| T0236 | L2 | any | Restore the zst archive of /opt/app into /tmp/restore | `sudo tar --zstd -xpf /srv/backups/opt-app.tar.zst -C /tmp/restore` | Restore to a test path first, then compare. |
| T0237 | L2 | any | Restore the zst archive of /srv/share into /tmp/restore | `sudo tar --zstd -xpf /srv/backups/srv-share.tar.zst -C /tmp/restore` | Restore to a test path first, then compare. |
| T0238 | L2 | any | Restore the zst archive of /var/www into /tmp/restore | `sudo tar --zstd -xpf /srv/backups/var-www.tar.zst -C /tmp/restore` | Restore to a test path first, then compare. |
| T0239 | L3 | any | Compare /etc/ with its restored copy | `diff -r /etc/ /tmp/restore/etc/ && echo identical` | Proves the backup can be restored. |
| T0240 | L3 | any | Compare /home/ with its restored copy | `diff -r /home/ /tmp/restore/home/ && echo identical` | Proves the backup can be restored. |
| T0241 | L3 | any | Compare /srv/share/ with its restored copy | `diff -r /srv/share/ /tmp/restore/srv/share/ && echo identical` | Proves the backup can be restored. |
| T0242 | L3 | any | Compare /var/www/ with its restored copy | `diff -r /var/www/ /tmp/restore/var/www/ && echo identical` | Proves the backup can be restored. |
