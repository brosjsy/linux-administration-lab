# 03. Permissions and ACLs

```bash
ls -l file                       # -rwxr-x--- owner/group/others
chmod 750 script.sh              # rwx r-x ---
chmod u+x,g-w file
chown alice:support /srv/share
umask                            # default 0022
chmod g+s /srv/share             # SGID: new files inherit group
chmod +t /srv/tmp                # sticky bit: only owners delete
find / -perm -4000 -type f 2>/dev/null   # audit SUID binaries
setfacl -m u:bob:rx /srv/share   # extra access without changing group
getfacl /srv/share
```

## Scenario: shared team folder
1. `mkdir /srv/share && chown root:support /srv/share`
2. `chmod 2770 /srv/share` (group rwx + SGID)
3. Verify a file created by `alice` is owned by group `support`.
