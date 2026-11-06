# Runbook: DNS failure

**Symptom:** `ping 8.8.8.8` works, `ping ya.ru` fails.
```bash
resolvectl status                    # which DNS servers are used
cat /etc/resolv.conf
dig ya.ru; dig @8.8.8.8 ya.ru        # local resolver vs public
sudo systemctl status systemd-resolved named
```
**Fix:** correct DNS server in netplan / NetworkManager, restart resolver, fix zone file (`named-checkzone`) on our DNS server.
**Verify:** `dig ya.ru +short` returns an address.
