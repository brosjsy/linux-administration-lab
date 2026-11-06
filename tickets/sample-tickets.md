# Sample tickets (lab exercises)

| ID | Request | Classification | Resolution |
|----|---------|----------------|------------|
| LAB-101 | "I can't log in to srv1 since this morning" | Incident, P3, Access | Password expired (`chage -l`). Reset with forced change, user confirmed login. KB-001 linked. |
| LAB-102 | "Website shows 502 Bad Gateway" | Incident, P2, Service | Backend app stopped after update. Restarted, added to watchdog list. Root cause sent to app owner. |
| LAB-103 | "Please give new employee access to shared folder" | Request, P4, Access | Added to `support` group, verified access with `sudo -u newuser ls /srv/share`. |
| LAB-104 | "Server srv2 very slow" | Incident, P2, Performance | `vmstat` showed high `wa`; backup job running at 10:00. Moved backup to 02:00 via cron. |
| LAB-105 | "Cannot open intranet by name" | Incident, P3, Network | Wrong DNS server after netplan change. Fixed config, `netplan apply`, `dig` OK. KB-003 written. |
| LAB-106 | "Need a folder of logs from last night for an incident" | Request, P3, Logs | Exported with `journalctl --since/--until -o short-iso`, shared via restricted folder. |

### Escalation note template
```
Ticket: LAB-102 | Host: web1 | Since: 2026-11-05 09:40
Symptom: 502 from nginx for /api
Checked: nginx OK (nginx -t), upstream app.service inactive (exit code 1)
Log: journalctl -u app -> "port 8080 already in use"
Action: none yet on app config. Escalating to app team for port conflict.
```
