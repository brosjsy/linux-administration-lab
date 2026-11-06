# 23. Monitoring: Zabbix and Prometheus

Level: intermediate to professional

On-duty engineers mostly **react to monitoring alerts**, so knowing how alerts are built matters.

## What to monitor
| Metric | Typical alert |
|--------|---------------|
| Host up / ping | host unreachable for 3 minutes |
| CPU load | load average above cores x 2 for 10 minutes |
| Memory | available below 10% |
| Disk | used above 85% (warning), 95% (critical); inodes too |
| Services | nginx / sshd / database not running |
| Certificates | expires in less than 14 days |
| Backups | last success older than 26 hours |

## Zabbix (very common in Russian companies)
```bash
sudo apt install zabbix-agent2
# /etc/zabbix/zabbix_agent2.conf: Server=<zabbix-server-ip>, Hostname=web1
sudo systemctl enable --now zabbix-agent2
zabbix_agent2 -t system.cpu.load[all,avg1]     # test an item locally
```
Then on the server: add host, link template "Linux by Zabbix agent", check Latest data.

## Prometheus + node_exporter + Grafana
```bash
sudo apt install prometheus-node-exporter
curl -s localhost:9100/metrics | grep node_load1
```
Example alert rule:
```yaml
- alert: DiskAlmostFull
  expr: (1 - node_filesystem_avail_bytes{fstype!="tmpfs"} / node_filesystem_size_bytes) * 100 > 85
  for: 10m
  labels: {severity: warning}
```

## On-duty workflow for an alert
1. Acknowledge the alert, open a ticket.
2. Check the host (runbooks in [`runbooks/`](../runbooks/)).
3. Fix or escalate with facts.
4. Close the alert and the ticket with a short summary.
