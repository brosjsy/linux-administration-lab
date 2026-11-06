# 13. Infrastructure services

## DNS: BIND (Rocky, 192.168.56.20)
```bash
sudo dnf install bind bind-utils
# /etc/named.conf -> zone "lab.local" { type master; file "lab.local.zone"; };
sudo named-checkconf && sudo named-checkzone lab.local /var/named/lab.local.zone
sudo systemctl enable --now named
dig @192.168.56.20 srv1.lab.local
```
## DHCP: Kea
```bash
sudo dnf install kea
# /etc/kea/kea-dhcp4.conf: subnet 192.168.56.0/24, pool .100-.200, option routers, domain-name-servers
sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf && sudo systemctl enable --now kea-dhcp4
```
## File server: Samba (Windows clients) and NFS (Linux clients)
```bash
sudo apt install samba
# [share] path=/srv/share, valid users=@support, read only=no
testparm && sudo systemctl restart smbd
sudo smbpasswd -a alice
smbclient //localhost/share -U alice

echo "/srv/nfs 192.168.56.0/24(rw,sync,root_squash)" | sudo tee -a /etc/exports
sudo exportfs -ra && showmount -e localhost
```
## Web: Nginx
```bash
sudo apt install nginx && sudo nginx -t && sudo systemctl reload nginx
curl -I http://localhost
```
