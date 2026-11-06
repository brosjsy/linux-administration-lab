# 09. Firewall

## ufw (Ubuntu)
```bash
sudo ufw default deny incoming
sudo ufw allow OpenSSH
sudo ufw allow from 192.168.56.0/24 to any port 445 proto tcp   # Samba from LAN only
sudo ufw enable && sudo ufw status numbered
```
## firewalld (Rocky)
```bash
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --permanent --add-service={http,https}
sudo firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=192.168.56.0/24 service name=nfs accept'
sudo firewall-cmd --reload && sudo firewall-cmd --list-all
```
## nftables (view)
```bash
sudo nft list ruleset
```
