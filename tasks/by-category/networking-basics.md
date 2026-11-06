# Networking: basics (53 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T2145 | L1 | any | Check if croc.ru is reachable | `ping -c 4 croc.ru` | 4 packets; look at loss and time. |
| T2146 | L1 | any | Check if example.com is reachable | `ping -c 4 example.com` | 4 packets; look at loss and time. |
| T2147 | L1 | any | Check if github.com is reachable | `ping -c 4 github.com` | 4 packets; look at loss and time. |
| T2148 | L1 | any | Check if gosuslugi.ru is reachable | `ping -c 4 gosuslugi.ru` | 4 packets; look at loss and time. |
| T2149 | L1 | any | Check if habr.com is reachable | `ping -c 4 habr.com` | 4 packets; look at loss and time. |
| T2150 | L1 | any | Check if itmo.ru is reachable | `ping -c 4 itmo.ru` | 4 packets; look at loss and time. |
| T2151 | L1 | any | Check if kernel.org is reachable | `ping -c 4 kernel.org` | 4 packets; look at loss and time. |
| T2152 | L1 | any | Check if mail.ru is reachable | `ping -c 4 mail.ru` | 4 packets; look at loss and time. |
| T2153 | L1 | any | Check if ozon.ru is reachable | `ping -c 4 ozon.ru` | 4 packets; look at loss and time. |
| T2154 | L1 | any | Check if rbc.ru is reachable | `ping -c 4 rbc.ru` | 4 packets; look at loss and time. |
| T2155 | L1 | any | Check if sber.ru is reachable | `ping -c 4 sber.ru` | 4 packets; look at loss and time. |
| T2156 | L1 | any | Check if spbu.ru is reachable | `ping -c 4 spbu.ru` | 4 packets; look at loss and time. |
| T2157 | L1 | any | Check if vk.com is reachable | `ping -c 4 vk.com` | 4 packets; look at loss and time. |
| T2158 | L1 | any | Check if ya.ru is reachable | `ping -c 4 ya.ru` | 4 packets; look at loss and time. |
| T2159 | L1 | any | Show the routing table | `ip route` | Network administration basics. |
| T2160 | L2 | any | Add a temporary static route to 10.10.0.0/16 via 192.168.56.1 | `sudo ip route add 10.10.0.0/16 via 192.168.56.1` | Network administration basics. |
| T2161 | L2 | any | Apply netplan safely with automatic rollback | `sudo netplan try` | Network administration basics. |
| T2162 | L2 | any | Check time sync status | `timedatectl; chronyc tracking` | Network administration basics. |
| T2163 | L2 | any | Continuous path and loss report to croc.ru | `mtr -rwc 20 croc.ru` | Better than traceroute for packet loss. |
| T2164 | L2 | any | Continuous path and loss report to example.com | `mtr -rwc 20 example.com` | Better than traceroute for packet loss. |
| T2165 | L2 | any | Continuous path and loss report to github.com | `mtr -rwc 20 github.com` | Better than traceroute for packet loss. |
| T2166 | L2 | any | Continuous path and loss report to gosuslugi.ru | `mtr -rwc 20 gosuslugi.ru` | Better than traceroute for packet loss. |
| T2167 | L2 | any | Continuous path and loss report to habr.com | `mtr -rwc 20 habr.com` | Better than traceroute for packet loss. |
| T2168 | L2 | any | Continuous path and loss report to itmo.ru | `mtr -rwc 20 itmo.ru` | Better than traceroute for packet loss. |
| T2169 | L2 | any | Continuous path and loss report to kernel.org | `mtr -rwc 20 kernel.org` | Better than traceroute for packet loss. |
| T2170 | L2 | any | Continuous path and loss report to mail.ru | `mtr -rwc 20 mail.ru` | Better than traceroute for packet loss. |
| T2171 | L2 | any | Continuous path and loss report to ozon.ru | `mtr -rwc 20 ozon.ru` | Better than traceroute for packet loss. |
| T2172 | L2 | any | Continuous path and loss report to rbc.ru | `mtr -rwc 20 rbc.ru` | Better than traceroute for packet loss. |
| T2173 | L2 | any | Continuous path and loss report to sber.ru | `mtr -rwc 20 sber.ru` | Better than traceroute for packet loss. |
| T2174 | L2 | any | Continuous path and loss report to spbu.ru | `mtr -rwc 20 spbu.ru` | Better than traceroute for packet loss. |
| T2175 | L2 | any | Continuous path and loss report to vk.com | `mtr -rwc 20 vk.com` | Better than traceroute for packet loss. |
| T2176 | L2 | any | Continuous path and loss report to ya.ru | `mtr -rwc 20 ya.ru` | Better than traceroute for packet loss. |
| T2177 | L2 | any | Show DNS servers in use | `resolvectl status` | Network administration basics. |
| T2178 | L2 | any | Show all TCP connections and their state counts | `ss -tan \| awk 'NR>1{print $1}' \| sort \| uniq -c` | Network administration basics. |
| T2179 | L2 | any | Show the ARP / neighbour table | `ip neigh` | Network administration basics. |
| T2180 | L2 | any | Show the hostname and set a new one | `hostnamectl; sudo hostnamectl set-hostname web1` | Network administration basics. |
| T2181 | L2 | any | Show the network path to croc.ru | `traceroute croc.ru` | Each hop is a router; * means no reply. |
| T2182 | L2 | any | Show the network path to example.com | `traceroute example.com` | Each hop is a router; * means no reply. |
| T2183 | L2 | any | Show the network path to github.com | `traceroute github.com` | Each hop is a router; * means no reply. |
| T2184 | L2 | any | Show the network path to gosuslugi.ru | `traceroute gosuslugi.ru` | Each hop is a router; * means no reply. |
| T2185 | L2 | any | Show the network path to habr.com | `traceroute habr.com` | Each hop is a router; * means no reply. |
| T2186 | L2 | any | Show the network path to itmo.ru | `traceroute itmo.ru` | Each hop is a router; * means no reply. |
| T2187 | L2 | any | Show the network path to kernel.org | `traceroute kernel.org` | Each hop is a router; * means no reply. |
| T2188 | L2 | any | Show the network path to mail.ru | `traceroute mail.ru` | Each hop is a router; * means no reply. |
| T2189 | L2 | any | Show the network path to ozon.ru | `traceroute ozon.ru` | Each hop is a router; * means no reply. |
| T2190 | L2 | any | Show the network path to rbc.ru | `traceroute rbc.ru` | Each hop is a router; * means no reply. |
| T2191 | L2 | any | Show the network path to sber.ru | `traceroute sber.ru` | Each hop is a router; * means no reply. |
| T2192 | L2 | any | Show the network path to spbu.ru | `traceroute spbu.ru` | Each hop is a router; * means no reply. |
| T2193 | L2 | any | Show the network path to vk.com | `traceroute vk.com` | Each hop is a router; * means no reply. |
| T2194 | L2 | any | Show the network path to ya.ru | `traceroute ya.ru` | Each hop is a router; * means no reply. |
| T2195 | L2 | any | Show which route is used to reach 8.8.8.8 | `ip route get 8.8.8.8` | Network administration basics. |
| T2196 | L3 | any | Measure bandwidth between two lab hosts | `iperf3 -s   # on server;  iperf3 -c 192.168.56.20   # on client` | Network administration basics. |
| T2197 | L3 | any | Scan open ports on a lab host | `nmap -sV 192.168.56.20` | Network administration basics. |
