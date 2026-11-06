# Boot, kernel and performance (28 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T0255 | L3 | any | Boot into text mode by default | `sudo systemctl set-default multi-user.target` | Advanced system administration. |
| T0256 | L3 | any | List installed kernels (Rocky) | `sudo grubby --info=ALL \| grep -E '^kernel\|^index'` | Advanced system administration. |
| T0257 | L3 | any | Load a kernel module now | `sudo modprobe br_netfilter` | Advanced system administration. |
| T0258 | L3 | any | Regenerate GRUB menu (Ubuntu) | `sudo update-grub` | Advanced system administration. |
| T0259 | L3 | any | Set the current kernel as default (Rocky) | `sudo grubby --set-default /boot/vmlinuz-$(uname -r)` | Advanced system administration. |
| T0260 | L3 | any | Show CPU model and cores | `lscpu \| head -20` | Advanced system administration. |
| T0261 | L3 | any | Show PCI devices (network and disk controllers) | `lspci \| grep -Ei 'net\|sata\|nvme\|raid'` | Advanced system administration. |
| T0262 | L3 | any | Show hardware summary | `sudo lshw -short \| head -40` | Advanced system administration. |
| T0263 | L3 | any | Show kernel version and build | `uname -a` | Advanced system administration. |
| T0264 | L3 | any | Show loaded kernel modules | `lsmod \| head -20` | Advanced system administration. |
| T0265 | L3 | any | Show memory modules | `sudo dmidecode -t memory \| grep -E 'Size\|Speed' \| head` | Advanced system administration. |
| T0266 | L3 | any | Show software RAID status | `cat /proc/mdstat` | Advanced system administration. |
| T0267 | L3 | any | Show the critical boot chain | `systemd-analyze critical-chain` | Advanced system administration. |
| T0268 | L3 | any | Show the default boot target | `systemctl get-default` | Advanced system administration. |
| T0269 | L3 | any | Show what slows down boot | `systemd-analyze blame \| head -15` | Advanced system administration. |
| T0270 | L4 | any | Check and repair an unmounted ext4 filesystem | `sudo fsck -f /dev/sdb1` | Advanced system administration. |
| T0271 | L4 | any | Drop page cache for a benchmark (test only) | `sync; echo 3 \| sudo tee /proc/sys/vm/drop_caches` | Advanced system administration. |
| T0272 | L4 | any | Raise the open-files limit for user appuser | `printf 'appuser soft nofile 65535\nappuser hard nofile 65535\n' \| sudo tee /etc/security/limits.d/appuser.conf` | Advanced system administration. |
| T0273 | L4 | any | Repair an unmounted XFS filesystem | `sudo xfs_repair /dev/sdb1` | Advanced system administration. |
| T0274 | L4 | any | Rescue: remount root read-write in emergency mode | `mount -o remount,rw /` | Advanced system administration. |
| T0275 | L4 | any | Rescue: reset root password on Rocky (after rd.break) | `mount -o remount,rw /sysroot && chroot /sysroot && passwd && touch /.autorelabel` | Advanced system administration. |
| T0276 | L4 | any | Show IO usage per process | `sudo iotop -oPa` | Advanced system administration. |
| T0277 | L4 | any | Show NUMA layout of the server | `lscpu \| grep -i numa; numactl --hardware` | Advanced system administration. |
| T0278 | L4 | any | Show live cgroup resource usage | `systemd-cgtop` | Advanced system administration. |
| T0279 | L4 | any | Show memory details including slab cache | `cat /proc/meminfo \| head -25; sudo slabtop -o \| head -15` | Advanced system administration. |
| T0280 | L4 | any | Show the active tuned profile (Rocky) | `tuned-adm active` | Advanced system administration. |
| T0281 | L4 | any | Show the open-files limit of the current shell | `ulimit -n` | Advanced system administration. |
| T0282 | L4 | any | Switch to the throughput-performance tuned profile | `sudo tuned-adm profile throughput-performance` | Advanced system administration. |
