# Networking: capture (16 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T2198 | L3 | any | Capture traffic on port 10050 (Zabbix agent) for analysis | `sudo tcpdump -i any -nn port 10050 -w /tmp/port10050.pcap` | Open the .pcap in Wireshark later. |
| T2199 | L3 | any | Capture traffic on port 123 (NTP) for analysis | `sudo tcpdump -i any -nn port 123 -w /tmp/port123.pcap` | Open the .pcap in Wireshark later. |
| T2200 | L3 | any | Capture traffic on port 2049 (NFS) for analysis | `sudo tcpdump -i any -nn port 2049 -w /tmp/port2049.pcap` | Open the .pcap in Wireshark later. |
| T2201 | L3 | any | Capture traffic on port 22 (SSH) for analysis | `sudo tcpdump -i any -nn port 22 -w /tmp/port22.pcap` | Open the .pcap in Wireshark later. |
| T2202 | L3 | any | Capture traffic on port 25 (SMTP) for analysis | `sudo tcpdump -i any -nn port 25 -w /tmp/port25.pcap` | Open the .pcap in Wireshark later. |
| T2203 | L3 | any | Capture traffic on port 3306 (MySQL/MariaDB) for analysis | `sudo tcpdump -i any -nn port 3306 -w /tmp/port3306.pcap` | Open the .pcap in Wireshark later. |
| T2204 | L3 | any | Capture traffic on port 3389 (RDP) for analysis | `sudo tcpdump -i any -nn port 3389 -w /tmp/port3389.pcap` | Open the .pcap in Wireshark later. |
| T2205 | L3 | any | Capture traffic on port 443 (HTTPS) for analysis | `sudo tcpdump -i any -nn port 443 -w /tmp/port443.pcap` | Open the .pcap in Wireshark later. |
| T2206 | L3 | any | Capture traffic on port 445 (SMB) for analysis | `sudo tcpdump -i any -nn port 445 -w /tmp/port445.pcap` | Open the .pcap in Wireshark later. |
| T2207 | L3 | any | Capture traffic on port 53 (DNS) for analysis | `sudo tcpdump -i any -nn port 53 -w /tmp/port53.pcap` | Open the .pcap in Wireshark later. |
| T2208 | L3 | any | Capture traffic on port 5432 (PostgreSQL) for analysis | `sudo tcpdump -i any -nn port 5432 -w /tmp/port5432.pcap` | Open the .pcap in Wireshark later. |
| T2209 | L3 | any | Capture traffic on port 6379 (Redis) for analysis | `sudo tcpdump -i any -nn port 6379 -w /tmp/port6379.pcap` | Open the .pcap in Wireshark later. |
| T2210 | L3 | any | Capture traffic on port 80 (HTTP) for analysis | `sudo tcpdump -i any -nn port 80 -w /tmp/port80.pcap` | Open the .pcap in Wireshark later. |
| T2211 | L3 | any | Capture traffic on port 8080 (alternative HTTP) for analysis | `sudo tcpdump -i any -nn port 8080 -w /tmp/port8080.pcap` | Open the .pcap in Wireshark later. |
| T2212 | L3 | any | Capture traffic on port 8443 (alternative HTTPS) for analysis | `sudo tcpdump -i any -nn port 8443 -w /tmp/port8443.pcap` | Open the .pcap in Wireshark later. |
| T2213 | L3 | any | Capture traffic on port 9100 (node_exporter) for analysis | `sudo tcpdump -i any -nn port 9100 -w /tmp/port9100.pcap` | Open the .pcap in Wireshark later. |
