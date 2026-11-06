# Monitoring (29 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1874 | L2 | any | Check node_exporter answers | `curl -s localhost:9100/metrics \| head` | Monitoring operations. |
| T1875 | L2 | any | Show system activity history for today (sysstat) | `sar -u -r -d` | Monitoring operations. |
| T1876 | L3 | any | Test a Zabbix agent item locally | `zabbix_agent2 -t system.cpu.load[all,avg1]` | Monitoring operations. |
| T1877 | L3 | any | Validate Prometheus alert rules | `promtool check rules /etc/prometheus/rules/*.yml` | Monitoring operations. |
| T1878 | L3 | any | Validate Prometheus configuration | `promtool check config /etc/prometheus/prometheus.yml` | Monitoring operations. |
| T1879 | L3 | any | Zabbix: read 1-minute CPU load from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'system.cpu.load[all,avg1]'` | Run on the Zabbix server to test an item. |
| T1880 | L3 | any | Zabbix: read 1-minute CPU load from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'system.cpu.load[all,avg1]'` | Run on the Zabbix server to test an item. |
| T1881 | L3 | any | Zabbix: read available memory from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'vm.memory.size[available]'` | Run on the Zabbix server to test an item. |
| T1882 | L3 | any | Zabbix: read available memory from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'vm.memory.size[available]'` | Run on the Zabbix server to test an item. |
| T1883 | L3 | any | Zabbix: read incoming traffic on eth0 from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'net.if.in[eth0]'` | Run on the Zabbix server to test an item. |
| T1884 | L3 | any | Zabbix: read incoming traffic on eth0 from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'net.if.in[eth0]'` | Run on the Zabbix server to test an item. |
| T1885 | L3 | any | Zabbix: read number of nginx processes from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'proc.num[nginx]'` | Run on the Zabbix server to test an item. |
| T1886 | L3 | any | Zabbix: read number of nginx processes from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'proc.num[nginx]'` | Run on the Zabbix server to test an item. |
| T1887 | L3 | any | Zabbix: read reboot required flag from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'vfs.file.exists[/var/run/reboot-required]'` | Run on the Zabbix server to test an item. |
| T1888 | L3 | any | Zabbix: read reboot required flag from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'vfs.file.exists[/var/run/reboot-required]'` | Run on the Zabbix server to test an item. |
| T1889 | L3 | any | Zabbix: read root disk used percent from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'vfs.fs.size[/,pused]'` | Run on the Zabbix server to test an item. |
| T1890 | L3 | any | Zabbix: read root disk used percent from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'vfs.fs.size[/,pused]'` | Run on the Zabbix server to test an item. |
| T1891 | L3 | any | Zabbix: read uptime from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'system.uptime'` | Run on the Zabbix server to test an item. |
| T1892 | L3 | any | Zabbix: read uptime from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'system.uptime'` | Run on the Zabbix server to test an item. |
| T1893 | L3 | any | Zabbix: read whether port 443 listens from agent on 192.168.56.10 | `zabbix_get -s 192.168.56.10 -k 'net.tcp.listen[443]'` | Run on the Zabbix server to test an item. |
| T1894 | L3 | any | Zabbix: read whether port 443 listens from agent on 192.168.56.20 | `zabbix_get -s 192.168.56.20 -k 'net.tcp.listen[443]'` | Run on the Zabbix server to test an item. |
| T1895 | L4 | any | PromQL: Available memory percent | `node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
| T1896 | L4 | any | PromQL: CPU busy percent per host | `100 - avg by (instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
| T1897 | L4 | any | PromQL: Disk will be full within 24 hours | `predict_linear(node_filesystem_avail_bytes{fstype!="tmpfs"}[6h], 86400) < 0` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
| T1898 | L4 | any | PromQL: Hosts that are down | `up == 0` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
| T1899 | L4 | any | PromQL: Load per CPU core | `node_load5 / count without (cpu, mode) (node_cpu_seconds_total{mode="idle"})` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
| T1900 | L4 | any | PromQL: Network receive rate | `rate(node_network_receive_bytes_total{device!="lo"}[5m])` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
| T1901 | L4 | any | PromQL: Root disk used percent | `100 - node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"} * 100` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
| T1902 | L4 | any | PromQL: Systemd units in failed state | `node_systemd_unit_state{state="failed"} == 1` | Paste in Prometheus or Grafana; use in alert rules with a for: duration. |
