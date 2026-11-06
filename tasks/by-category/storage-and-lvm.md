# Storage and LVM (55 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T4102 | L1 | any | Show all disks and partitions with filesystems | `lsblk -f` | Core storage check. |
| T4103 | L1 | any | Show disk space of mounted filesystems | `df -hT` | Core storage check. |
| T4104 | L2 | any | Create a 10G swap file | `sudo fallocate -l 10G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile` | Add to /etc/fstab to keep after reboot. |
| T4105 | L2 | any | Create a 1G swap file | `sudo fallocate -l 1G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile` | Add to /etc/fstab to keep after reboot. |
| T4106 | L2 | any | Create a 20G swap file | `sudo fallocate -l 20G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile` | Add to /etc/fstab to keep after reboot. |
| T4107 | L2 | any | Create a 2G swap file | `sudo fallocate -l 2G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile` | Add to /etc/fstab to keep after reboot. |
| T4108 | L2 | any | Create a 5G swap file | `sudo fallocate -l 5G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile` | Add to /etc/fstab to keep after reboot. |
| T4109 | L2 | any | Create an ext4 filesystem on /dev/sdb1 | `sudo mkfs.ext4 /dev/sdb1` | Destroys existing data on the partition. |
| T4110 | L2 | any | Create an ext4 filesystem on /dev/sdc1 | `sudo mkfs.ext4 /dev/sdc1` | Destroys existing data on the partition. |
| T4111 | L2 | any | Create an ext4 filesystem on /dev/sdd1 | `sudo mkfs.ext4 /dev/sdd1` | Destroys existing data on the partition. |
| T4112 | L2 | any | Create an ext4 filesystem on /dev/vdb1 | `sudo mkfs.ext4 /dev/vdb1` | Destroys existing data on the partition. |
| T4113 | L2 | any | Create an ext4 filesystem on /dev/vdc1 | `sudo mkfs.ext4 /dev/vdc1` | Destroys existing data on the partition. |
| T4114 | L2 | any | Create an xfs filesystem on /dev/sdb1 | `sudo mkfs.xfs /dev/sdb1` | Destroys existing data on the partition. |
| T4115 | L2 | any | Create an xfs filesystem on /dev/sdc1 | `sudo mkfs.xfs /dev/sdc1` | Destroys existing data on the partition. |
| T4116 | L2 | any | Create an xfs filesystem on /dev/sdd1 | `sudo mkfs.xfs /dev/sdd1` | Destroys existing data on the partition. |
| T4117 | L2 | any | Create an xfs filesystem on /dev/vdb1 | `sudo mkfs.xfs /dev/vdb1` | Destroys existing data on the partition. |
| T4118 | L2 | any | Create an xfs filesystem on /dev/vdc1 | `sudo mkfs.xfs /dev/vdc1` | Destroys existing data on the partition. |
| T4119 | L2 | any | Find deleted files still holding disk space | `sudo lsof +L1` | Core storage check. |
| T4120 | L2 | any | Mount /dev/sdb1 (ext4) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/sdb1) /data ext4 defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4121 | L2 | any | Mount /dev/sdb1 (xfs) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/sdb1) /data xfs defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4122 | L2 | any | Mount /dev/sdc1 (ext4) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/sdc1) /data ext4 defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4123 | L2 | any | Mount /dev/sdc1 (xfs) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/sdc1) /data xfs defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4124 | L2 | any | Mount /dev/sdd1 (ext4) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/sdd1) /data ext4 defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4125 | L2 | any | Mount /dev/sdd1 (xfs) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/sdd1) /data xfs defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4126 | L2 | any | Mount /dev/vdb1 (ext4) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/vdb1) /data ext4 defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4127 | L2 | any | Mount /dev/vdb1 (xfs) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/vdb1) /data xfs defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4128 | L2 | any | Mount /dev/vdc1 (ext4) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/vdc1) /data ext4 defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4129 | L2 | any | Mount /dev/vdc1 (xfs) permanently on /data by UUID | `echo "UUID=$(sudo blkid -s UUID -o value /dev/vdc1) /data xfs defaults,nofail 0 2" \| sudo tee -a /etc/fstab && sudo mount -a` | nofail prevents emergency mode if the disk is missing. |
| T4130 | L2 | any | Show UUIDs of all block devices | `sudo blkid` | Core storage check. |
| T4131 | L2 | any | Show inode usage | `df -i` | Core storage check. |
| T4132 | L2 | any | Show physical volumes, volume groups and logical volumes | `sudo pvs; sudo vgs; sudo lvs` | Core storage check. |
| T4133 | L2 | any | Show swap usage | `swapon --show; free -h` | Core storage check. |
| T4134 | L2 | any | Test /etc/fstab without rebooting | `sudo mount -a` | Core storage check. |
| T4135 | L3 | any | Add /dev/sdb as an LVM physical volume to vg_data | `sudo pvcreate /dev/sdb && sudo vgextend vg_data /dev/sdb` | Grows the volume group capacity. |
| T4136 | L3 | any | Add /dev/sdc as an LVM physical volume to vg_data | `sudo pvcreate /dev/sdc && sudo vgextend vg_data /dev/sdc` | Grows the volume group capacity. |
| T4137 | L3 | any | Add /dev/sdd as an LVM physical volume to vg_data | `sudo pvcreate /dev/sdd && sudo vgextend vg_data /dev/sdd` | Grows the volume group capacity. |
| T4138 | L3 | any | Add /dev/vdb as an LVM physical volume to vg_data | `sudo pvcreate /dev/vdb && sudo vgextend vg_data /dev/vdb` | Grows the volume group capacity. |
| T4139 | L3 | any | Add /dev/vdc as an LVM physical volume to vg_data | `sudo pvcreate /dev/vdc && sudo vgextend vg_data /dev/vdc` | Grows the volume group capacity. |
| T4140 | L3 | any | Check SMART health of disk /dev/sda | `sudo smartctl -H /dev/sda` | Core storage check. |
| T4141 | L3 | any | Extend lv_app by 10G online, filesystem included | `sudo lvextend -r -L +10G /dev/vg_data/lv_app` | -r resizes ext4/xfs too. |
| T4142 | L3 | any | Extend lv_app by 1G online, filesystem included | `sudo lvextend -r -L +1G /dev/vg_data/lv_app` | -r resizes ext4/xfs too. |
| T4143 | L3 | any | Extend lv_app by 20G online, filesystem included | `sudo lvextend -r -L +20G /dev/vg_data/lv_app` | -r resizes ext4/xfs too. |
| T4144 | L3 | any | Extend lv_app by 2G online, filesystem included | `sudo lvextend -r -L +2G /dev/vg_data/lv_app` | -r resizes ext4/xfs too. |
| T4145 | L3 | any | Extend lv_app by 5G online, filesystem included | `sudo lvextend -r -L +5G /dev/vg_data/lv_app` | -r resizes ext4/xfs too. |
| T4146 | L3 | any | Extend lv_home by 10G online, filesystem included | `sudo lvextend -r -L +10G /dev/vg_data/lv_home` | -r resizes ext4/xfs too. |
| T4147 | L3 | any | Extend lv_home by 1G online, filesystem included | `sudo lvextend -r -L +1G /dev/vg_data/lv_home` | -r resizes ext4/xfs too. |
| T4148 | L3 | any | Extend lv_home by 20G online, filesystem included | `sudo lvextend -r -L +20G /dev/vg_data/lv_home` | -r resizes ext4/xfs too. |
| T4149 | L3 | any | Extend lv_home by 2G online, filesystem included | `sudo lvextend -r -L +2G /dev/vg_data/lv_home` | -r resizes ext4/xfs too. |
| T4150 | L3 | any | Extend lv_home by 5G online, filesystem included | `sudo lvextend -r -L +5G /dev/vg_data/lv_home` | -r resizes ext4/xfs too. |
| T4151 | L3 | any | Extend lv_var by 10G online, filesystem included | `sudo lvextend -r -L +10G /dev/vg_data/lv_var` | -r resizes ext4/xfs too. |
| T4152 | L3 | any | Extend lv_var by 1G online, filesystem included | `sudo lvextend -r -L +1G /dev/vg_data/lv_var` | -r resizes ext4/xfs too. |
| T4153 | L3 | any | Extend lv_var by 20G online, filesystem included | `sudo lvextend -r -L +20G /dev/vg_data/lv_var` | -r resizes ext4/xfs too. |
| T4154 | L3 | any | Extend lv_var by 2G online, filesystem included | `sudo lvextend -r -L +2G /dev/vg_data/lv_var` | -r resizes ext4/xfs too. |
| T4155 | L3 | any | Extend lv_var by 5G online, filesystem included | `sudo lvextend -r -L +5G /dev/vg_data/lv_var` | -r resizes ext4/xfs too. |
| T4156 | L3 | any | Show which processes use /data (before unmount) | `sudo fuser -vm /data` | Core storage check. |
