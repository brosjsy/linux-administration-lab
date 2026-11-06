# File servers (41 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1028 | L2 | any | Add a Samba password for an existing user | `sudo smbpasswd -a alice` | File server operations. |
| T1029 | L2 | any | Check Samba configuration syntax | `testparm -s` | File server operations. |
| T1030 | L2 | any | Create a Samba share 'finance' for group finance | `sudo mkdir -p /srv/samba/finance && sudo chgrp finance /srv/samba/finance && sudo chmod 2770 /srv/samba/finance  # [finance] path=/srv/samba/finance valid users=@finance read only=no` | Add the section to /etc/samba/smb.conf, then testparm. |
| T1031 | L2 | any | Create a Samba share 'hr' for group hr | `sudo mkdir -p /srv/samba/hr && sudo chgrp hr /srv/samba/hr && sudo chmod 2770 /srv/samba/hr  # [hr] path=/srv/samba/hr valid users=@hr read only=no` | Add the section to /etc/samba/smb.conf, then testparm. |
| T1032 | L2 | any | Create a Samba share 'it' for group it | `sudo mkdir -p /srv/samba/it && sudo chgrp it /srv/samba/it && sudo chmod 2770 /srv/samba/it  # [it] path=/srv/samba/it valid users=@it read only=no` | Add the section to /etc/samba/smb.conf, then testparm. |
| T1033 | L2 | any | Create a Samba share 'projects' for group projects | `sudo mkdir -p /srv/samba/projects && sudo chgrp projects /srv/samba/projects && sudo chmod 2770 /srv/samba/projects  # [projects] path=/srv/samba/projects valid users=@projects read only=no` | Add the section to /etc/samba/smb.conf, then testparm. |
| T1034 | L2 | any | Create a Samba share 'public' for group public | `sudo mkdir -p /srv/samba/public && sudo chgrp public /srv/samba/public && sudo chmod 2770 /srv/samba/public  # [public] path=/srv/samba/public valid users=@public read only=no` | Add the section to /etc/samba/smb.conf, then testparm. |
| T1035 | L2 | any | Create a Samba share 'scans' for group scans | `sudo mkdir -p /srv/samba/scans && sudo chgrp scans /srv/samba/scans && sudo chmod 2770 /srv/samba/scans  # [scans] path=/srv/samba/scans valid users=@scans read only=no` | Add the section to /etc/samba/smb.conf, then testparm. |
| T1036 | L2 | any | Export /srv/nfs/finance over NFS to the lab network | `echo '/srv/nfs/finance 192.168.56.0/24(rw,sync,root_squash)' \| sudo tee -a /etc/exports && sudo exportfs -ra` | root_squash maps client root to nobody. |
| T1037 | L2 | any | Export /srv/nfs/hr over NFS to the lab network | `echo '/srv/nfs/hr 192.168.56.0/24(rw,sync,root_squash)' \| sudo tee -a /etc/exports && sudo exportfs -ra` | root_squash maps client root to nobody. |
| T1038 | L2 | any | Export /srv/nfs/it over NFS to the lab network | `echo '/srv/nfs/it 192.168.56.0/24(rw,sync,root_squash)' \| sudo tee -a /etc/exports && sudo exportfs -ra` | root_squash maps client root to nobody. |
| T1039 | L2 | any | Export /srv/nfs/projects over NFS to the lab network | `echo '/srv/nfs/projects 192.168.56.0/24(rw,sync,root_squash)' \| sudo tee -a /etc/exports && sudo exportfs -ra` | root_squash maps client root to nobody. |
| T1040 | L2 | any | Export /srv/nfs/public over NFS to the lab network | `echo '/srv/nfs/public 192.168.56.0/24(rw,sync,root_squash)' \| sudo tee -a /etc/exports && sudo exportfs -ra` | root_squash maps client root to nobody. |
| T1041 | L2 | any | Export /srv/nfs/scans over NFS to the lab network | `echo '/srv/nfs/scans 192.168.56.0/24(rw,sync,root_squash)' \| sudo tee -a /etc/exports && sudo exportfs -ra` | root_squash maps client root to nobody. |
| T1042 | L2 | any | Mount NFS export finance on a client | `sudo mount -t nfs 192.168.56.20:/srv/nfs/finance /mnt/finance` | Add _netdev,nofail in fstab for boot safety. |
| T1043 | L2 | any | Mount NFS export hr on a client | `sudo mount -t nfs 192.168.56.20:/srv/nfs/hr /mnt/hr` | Add _netdev,nofail in fstab for boot safety. |
| T1044 | L2 | any | Mount NFS export it on a client | `sudo mount -t nfs 192.168.56.20:/srv/nfs/it /mnt/it` | Add _netdev,nofail in fstab for boot safety. |
| T1045 | L2 | any | Mount NFS export projects on a client | `sudo mount -t nfs 192.168.56.20:/srv/nfs/projects /mnt/projects` | Add _netdev,nofail in fstab for boot safety. |
| T1046 | L2 | any | Mount NFS export public on a client | `sudo mount -t nfs 192.168.56.20:/srv/nfs/public /mnt/public` | Add _netdev,nofail in fstab for boot safety. |
| T1047 | L2 | any | Mount NFS export scans on a client | `sudo mount -t nfs 192.168.56.20:/srv/nfs/scans /mnt/scans` | Add _netdev,nofail in fstab for boot safety. |
| T1048 | L2 | any | Mount Samba share 'finance' on a Linux client | `sudo mount -t cifs //192.168.56.20/finance /mnt/finance -o username=alice,uid=$(id -u),gid=$(id -g)` | Needs cifs-utils; use a credentials file for fstab. |
| T1049 | L2 | any | Mount Samba share 'hr' on a Linux client | `sudo mount -t cifs //192.168.56.20/hr /mnt/hr -o username=alice,uid=$(id -u),gid=$(id -g)` | Needs cifs-utils; use a credentials file for fstab. |
| T1050 | L2 | any | Mount Samba share 'it' on a Linux client | `sudo mount -t cifs //192.168.56.20/it /mnt/it -o username=alice,uid=$(id -u),gid=$(id -g)` | Needs cifs-utils; use a credentials file for fstab. |
| T1051 | L2 | any | Mount Samba share 'projects' on a Linux client | `sudo mount -t cifs //192.168.56.20/projects /mnt/projects -o username=alice,uid=$(id -u),gid=$(id -g)` | Needs cifs-utils; use a credentials file for fstab. |
| T1052 | L2 | any | Mount Samba share 'public' on a Linux client | `sudo mount -t cifs //192.168.56.20/public /mnt/public -o username=alice,uid=$(id -u),gid=$(id -g)` | Needs cifs-utils; use a credentials file for fstab. |
| T1053 | L2 | any | Mount Samba share 'scans' on a Linux client | `sudo mount -t cifs //192.168.56.20/scans /mnt/scans -o username=alice,uid=$(id -u),gid=$(id -g)` | Needs cifs-utils; use a credentials file for fstab. |
| T1054 | L2 | any | Show NFS exports of a server | `showmount -e 192.168.56.20` | File server operations. |
| T1055 | L2 | any | Show connected Samba clients and open files | `sudo smbstatus` | File server operations. |
| T1056 | L2 | any | Test access to Samba share 'finance' | `smbclient //localhost/finance -U alice -c 'ls'` | Lists files if permissions are correct. |
| T1057 | L2 | any | Test access to Samba share 'hr' | `smbclient //localhost/hr -U alice -c 'ls'` | Lists files if permissions are correct. |
| T1058 | L2 | any | Test access to Samba share 'it' | `smbclient //localhost/it -U alice -c 'ls'` | Lists files if permissions are correct. |
| T1059 | L2 | any | Test access to Samba share 'projects' | `smbclient //localhost/projects -U alice -c 'ls'` | Lists files if permissions are correct. |
| T1060 | L2 | any | Test access to Samba share 'public' | `smbclient //localhost/public -U alice -c 'ls'` | Lists files if permissions are correct. |
| T1061 | L2 | any | Test access to Samba share 'scans' | `smbclient //localhost/scans -U alice -c 'ls'` | Lists files if permissions are correct. |
| T1062 | L3 | any | Mount NFS export finance on demand with autofs | `echo 'finance -rw,soft 192.168.56.20:/srv/nfs/finance' \| sudo tee -a /etc/auto.nfs` | Mounted at first access, unmounted when idle. |
| T1063 | L3 | any | Mount NFS export hr on demand with autofs | `echo 'hr -rw,soft 192.168.56.20:/srv/nfs/hr' \| sudo tee -a /etc/auto.nfs` | Mounted at first access, unmounted when idle. |
| T1064 | L3 | any | Mount NFS export it on demand with autofs | `echo 'it -rw,soft 192.168.56.20:/srv/nfs/it' \| sudo tee -a /etc/auto.nfs` | Mounted at first access, unmounted when idle. |
| T1065 | L3 | any | Mount NFS export projects on demand with autofs | `echo 'projects -rw,soft 192.168.56.20:/srv/nfs/projects' \| sudo tee -a /etc/auto.nfs` | Mounted at first access, unmounted when idle. |
| T1066 | L3 | any | Mount NFS export public on demand with autofs | `echo 'public -rw,soft 192.168.56.20:/srv/nfs/public' \| sudo tee -a /etc/auto.nfs` | Mounted at first access, unmounted when idle. |
| T1067 | L3 | any | Mount NFS export scans on demand with autofs | `echo 'scans -rw,soft 192.168.56.20:/srv/nfs/scans' \| sudo tee -a /etc/auto.nfs` | Mounted at first access, unmounted when idle. |
| T1068 | L3 | any | Show NFS client statistics | `nfsstat -c` | File server operations. |
