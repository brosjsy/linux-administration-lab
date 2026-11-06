# KB-003 Website opens by IP but not by name

**Check:** `nslookup intranet.lab.local` (Windows) or `dig intranet.lab.local` (Linux).

- No answer: DNS server setting is wrong. On a managed PC, reconnect to the network or run `ipconfig /renew` (Windows).
- Wrong address: report it in a ticket with the output of the command above.

**For engineers:** see [runbooks/dns-failure.md](../runbooks/dns-failure.md).
