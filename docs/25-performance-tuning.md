# 25. Performance and resource limits

Level: professional

## Find the bottleneck (USE method: Utilisation, Saturation, Errors)
```bash
uptime; vmstat 1 5; mpstat -P ALL 1 3      # CPU
free -h; vmstat -s; slabtop                 # memory
iostat -xz 1 3; iotop                       # disk
sar -n DEV 1 3; ss -s                       # network
pidstat -urd 1 5                            # per process
```

## Limits
```bash
ulimit -n                                   # open files for this shell
# /etc/security/limits.d/app.conf
# appuser  soft  nofile  65535
# appuser  hard  nofile  65535
systemctl show nginx -p LimitNOFILE         # services use systemd limits
sudo systemctl edit nginx                   # [Service] LimitNOFILE=65535
```
Scenario: "Too many open files" in an application log. Check `ls /proc/<PID>/fd | wc -l` against the limit, raise it in the unit, restart.

## Control a greedy service with cgroups
```bash
sudo systemctl set-property backup.service CPUQuota=50% MemoryMax=1G
systemd-cgtop
```

## Kernel tuning examples
```
vm.swappiness = 10
net.core.somaxconn = 4096
fs.file-max = 2097152
```
Rocky: `sudo tuned-adm profile throughput-performance`.
Rule: change one thing, measure, keep notes.
