# 07. Networking

```bash
ip -br a; ip r; ip -s link           # addresses, routes, errors
ss -tulpn                            # listening ports and owning process
ping -c 4 8.8.8.8; traceroute ya.ru; mtr ya.ru
dig ya.ru +short; dig @8.8.8.8 ya.ru; resolvectl status
curl -I https://example.com
nmcli con show; nmcli dev status     # NetworkManager (Rocky)
sudo tcpdump -i eth0 port 53 -nn     # watch DNS traffic
```

## Static IP with netplan (Ubuntu)
```yaml
network:
  version: 2
  ethernets:
    eth1:
      addresses: [192.168.56.10/24]
      routes: [{to: default, via: 192.168.56.1}]
      nameservers: {addresses: [192.168.56.20, 8.8.8.8]}
```
`sudo netplan try` (auto-rollback if connectivity breaks), then `sudo netplan apply`.

## Troubleshooting order (bottom-up)
1. Link up? `ip link`  2. IP + mask? `ip a`  3. Gateway reachable? `ping <gw>`
4. Internet by IP? `ping 8.8.8.8`  5. DNS works? `dig ya.ru`  6. Port open? `ss -tlnp`, `nc -zv host 443`
