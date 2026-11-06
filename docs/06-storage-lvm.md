# 06. Storage and LVM

```bash
lsblk -f; df -hT; blkid
sudo fdisk /dev/sdb               # n, p, w -> /dev/sdb1
sudo mkfs.ext4 /dev/sdb1
sudo mkdir /data && sudo mount /dev/sdb1 /data
# persistent mount by UUID
echo "UUID=$(blkid -s UUID -o value /dev/sdb1) /data ext4 defaults,nofail 0 2" | sudo tee -a /etc/fstab
sudo mount -a                     # test fstab before reboot!
```

## LVM: create and extend a volume online
```bash
sudo pvcreate /dev/sdc /dev/sdd
sudo vgcreate vg_data /dev/sdc /dev/sdd
sudo lvcreate -n lv_app -L 5G vg_data
sudo mkfs.xfs /dev/vg_data/lv_app
sudo lvextend -r -L +2G /dev/vg_data/lv_app   # -r grows the filesystem too
pvs; vgs; lvs
```

## Swap file
```bash
sudo fallocate -l 1G /swapfile && sudo chmod 600 /swapfile
sudo mkswap /swapfile && sudo swapon /swapfile && free -h
```
