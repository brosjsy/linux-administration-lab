# 14. Directory services

## Concepts
- **LDAP**: central directory of users and groups.
- **FreeIPA**: LDAP + Kerberos + DNS + sudo rules for Linux fleets.
- **Active Directory**: Microsoft directory; Linux joins via `realmd` + `sssd`.

## Join a Linux server to a domain
```bash
sudo dnf install realmd sssd adcli oddjob-mkhomedir
realm discover lab.local
sudo realm join -U Administrator lab.local
id alice@lab.local
sudo realm permit -g support@lab.local
```
## Typical tickets
- User cannot log in: check `realm list`, `systemctl status sssd`, `journalctl -u sssd`, time sync (`timedatectl`, Kerberos needs correct time).
- Group changes not visible: `sudo sss_cache -E`.
