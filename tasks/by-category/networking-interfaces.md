# Networking: interfaces (24 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T2214 | L1 | any | Show IP addresses of enp0s8 | `ip addr show enp0s8` | Interface configuration and checks. |
| T2215 | L1 | any | Show IP addresses of ens33 | `ip addr show ens33` | Interface configuration and checks. |
| T2216 | L1 | any | Show IP addresses of eth0 | `ip addr show eth0` | Interface configuration and checks. |
| T2217 | L1 | any | Show IP addresses of eth1 | `ip addr show eth1` | Interface configuration and checks. |
| T2218 | L2 | any | Bring interface enp0s8 down and up | `sudo ip link set enp0s8 down && sudo ip link set enp0s8 up` | Interface configuration and checks. |
| T2219 | L2 | any | Bring interface ens33 down and up | `sudo ip link set ens33 down && sudo ip link set ens33 up` | Interface configuration and checks. |
| T2220 | L2 | any | Bring interface eth0 down and up | `sudo ip link set eth0 down && sudo ip link set eth0 up` | Interface configuration and checks. |
| T2221 | L2 | any | Bring interface eth1 down and up | `sudo ip link set eth1 down && sudo ip link set eth1 up` | Interface configuration and checks. |
| T2222 | L2 | any | Show NetworkManager settings of enp0s8 (Rocky) | `nmcli device show enp0s8` | Interface configuration and checks. |
| T2223 | L2 | any | Show NetworkManager settings of ens33 (Rocky) | `nmcli device show ens33` | Interface configuration and checks. |
| T2224 | L2 | any | Show NetworkManager settings of eth0 (Rocky) | `nmcli device show eth0` | Interface configuration and checks. |
| T2225 | L2 | any | Show NetworkManager settings of eth1 (Rocky) | `nmcli device show eth1` | Interface configuration and checks. |
| T2226 | L2 | any | Show errors and dropped packets on enp0s8 | `ip -s link show enp0s8` | Interface configuration and checks. |
| T2227 | L2 | any | Show errors and dropped packets on ens33 | `ip -s link show ens33` | Interface configuration and checks. |
| T2228 | L2 | any | Show errors and dropped packets on eth0 | `ip -s link show eth0` | Interface configuration and checks. |
| T2229 | L2 | any | Show errors and dropped packets on eth1 | `ip -s link show eth1` | Interface configuration and checks. |
| T2230 | L2 | any | Temporarily add IP 192.168.56.50/24 to enp0s8 | `sudo ip addr add 192.168.56.50/24 dev enp0s8` | Interface configuration and checks. |
| T2231 | L2 | any | Temporarily add IP 192.168.56.50/24 to ens33 | `sudo ip addr add 192.168.56.50/24 dev ens33` | Interface configuration and checks. |
| T2232 | L2 | any | Temporarily add IP 192.168.56.50/24 to eth0 | `sudo ip addr add 192.168.56.50/24 dev eth0` | Interface configuration and checks. |
| T2233 | L2 | any | Temporarily add IP 192.168.56.50/24 to eth1 | `sudo ip addr add 192.168.56.50/24 dev eth1` | Interface configuration and checks. |
| T2234 | L3 | any | Show link speed and duplex of enp0s8 | `sudo ethtool enp0s8 \| grep -E 'Speed\|Duplex\|Link detected'` | Interface configuration and checks. |
| T2235 | L3 | any | Show link speed and duplex of ens33 | `sudo ethtool ens33 \| grep -E 'Speed\|Duplex\|Link detected'` | Interface configuration and checks. |
| T2236 | L3 | any | Show link speed and duplex of eth0 | `sudo ethtool eth0 \| grep -E 'Speed\|Duplex\|Link detected'` | Interface configuration and checks. |
| T2237 | L3 | any | Show link speed and duplex of eth1 | `sudo ethtool eth1 \| grep -E 'Speed\|Duplex\|Link detected'` | Interface configuration and checks. |
