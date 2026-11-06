# 24. Boot process and recovery

Level: advanced

## Boot order
BIOS/UEFI, GRUB2, kernel + initramfs, systemd (PID 1), targets (`multi-user.target`, `graphical.target`).
```bash
systemctl get-default
sudo systemctl set-default multi-user.target
journalctl -b -1 -p err        # errors from the previous boot
systemd-analyze critical-chain
```

## Scenario: forgotten root password (console access)
1. In GRUB press `e`, add `rd.break` (Rocky) or `init=/bin/bash` (Ubuntu) to the `linux` line, boot with Ctrl+X.
2. Rocky: `mount -o remount,rw /sysroot && chroot /sysroot && passwd && touch /.autorelabel && exit && reboot`
3. Ubuntu: `mount -o remount,rw / && passwd && exec /sbin/init`

## Scenario: server drops to emergency mode after editing /etc/fstab
```bash
journalctl -xb | grep -i mount
mount -o remount,rw /
vi /etc/fstab        # fix or comment the bad line, use nofail for non-critical disks
mount -a && reboot
```
Prevention: always run `sudo mount -a` after editing fstab.

## Scenario: filesystem errors
```bash
sudo umount /data && sudo fsck -f /dev/sdb1    # never fsck a mounted filesystem
```

## Kernel
```bash
uname -r; ls /boot
sudo grubby --default-kernel            # Rocky
sudo update-grub                        # Ubuntu
```
