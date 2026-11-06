# Runbook: high load / server slow

```bash
uptime; nproc                         # load vs number of cores
top -o %CPU; top -o %MEM
vmstat 1 5                            # r = run queue, wa = waiting for disk, si/so = swapping
iostat -xz 1 3                        # disk %util and await
free -h; dmesg -T | grep -i -E "oom|killed"
```
| Pattern | Meaning | Action |
|---------|---------|--------|
| high `us`/`sy`, one process on top | CPU-bound process | identify, `renice` or restart, escalate to owner |
| high `wa` | disk bottleneck | find writer with `iotop`, check backups running |
| `si`/`so` > 0, OOM in dmesg | out of memory | find memory hog, add RAM/swap, fix leak |
