#!/usr/bin/env python3
"""Generate the Linux task library (tasks/): JSON, CSV, TSV, per-category Markdown and a searchable HTML page.

Each task: id, level (L1..L4), category, distro (any/debian/rhel), task, command, explanation, tags.
Run from the repo root:  python3 tools/generate_tasks.py
"""
import csv
import html
import json
import os
from collections import OrderedDict

OUT = "tasks"
tasks = []
seen = set()


def add(level, category, task, command, explanation, tags, distro="any"):
    key = task.strip().lower()
    if key in seen:
        return
    seen.add(key)
    tasks.append({
        "level": level, "category": category, "distro": distro,
        "task": task.strip(), "command": command.strip(),
        "explanation": explanation.strip(), "tags": tags,
    })


# ---------------------------------------------------------------- data pools
SERVICES = OrderedDict([
    ("nginx", "Nginx web server"), ("apache2", "Apache web server (Ubuntu)"), ("httpd", "Apache web server (Rocky)"),
    ("ssh", "OpenSSH server (Ubuntu)"), ("sshd", "OpenSSH server (Rocky)"), ("cron", "cron daemon (Ubuntu)"),
    ("crond", "cron daemon (Rocky)"), ("docker", "Docker engine"), ("postgresql", "PostgreSQL database"),
    ("mariadb", "MariaDB database"), ("redis-server", "Redis"), ("chrony", "time sync (Ubuntu)"),
    ("chronyd", "time sync (Rocky)"), ("firewalld", "firewalld"), ("named", "BIND DNS server"),
    ("smbd", "Samba file server"), ("nfs-server", "NFS server"), ("zabbix-agent2", "Zabbix agent"),
    ("fail2ban", "fail2ban"), ("auditd", "audit daemon"), ("rsyslog", "rsyslog"),
    ("systemd-resolved", "DNS resolver"), ("NetworkManager", "NetworkManager"), ("kea-dhcp4", "Kea DHCP server"),
    ("prometheus-node-exporter", "Prometheus node exporter"), ("sssd", "SSSD (directory login)"),
    ("php8.3-fpm", "PHP-FPM"), ("mysql", "MySQL database"), ("grafana-server", "Grafana"), ("prometheus", "Prometheus server"),
    ("haproxy", "HAProxy load balancer"), ("keepalived", "keepalived (virtual IP)"), ("postfix", "Postfix mail server"),
    ("squid", "Squid proxy"), ("openvpn-server@server", "OpenVPN server"), ("wg-quick@wg0", "WireGuard VPN"),
    ("libvirtd", "KVM virtualisation daemon"), ("containerd", "containerd runtime"), ("snmpd", "SNMP agent"),
    ("memcached", "Memcached"), ("rabbitmq-server", "RabbitMQ"),
])
SERVICE_ACTIONS = [
    ("L1", "Check the status of {d} ({s})", "systemctl status {s}", "Shows active state, PID, memory and the last log lines."),
    ("L1", "Start {d} ({s})", "sudo systemctl start {s}", "Starts the service now; it will not survive a reboot unless enabled."),
    ("L1", "Stop {d} ({s})", "sudo systemctl stop {s}", "Stops the service now."),
    ("L1", "Restart {d} ({s})", "sudo systemctl restart {s}", "Full stop and start; brief downtime."),
    ("L2", "Reload {d} ({s}) configuration without full restart", "sudo systemctl reload {s}", "Re-reads config without dropping connections, if the service supports reload."),
    ("L1", "Enable {d} ({s}) at boot and start it now", "sudo systemctl enable --now {s}", "Creates the boot symlink and starts the service in one command."),
    ("L1", "Disable {d} ({s}) at boot", "sudo systemctl disable {s}", "Service will not start automatically after reboot."),
    ("L3", "Prevent {d} ({s}) from being started at all", "sudo systemctl mask {s}", "Links the unit to /dev/null; unmask with systemctl unmask."),
    ("L2", "Check whether {d} ({s}) is running, script-friendly", "systemctl is-active --quiet {s} && echo running || echo down", "Exit code 0 means active; ideal for scripts and monitoring."),
    ("L2", "Show the last 50 log lines of {d} ({s})", "journalctl -u {s} -n 50 --no-pager", "Reads the systemd journal for one unit."),
    ("L2", "Follow the log of {d} ({s}) live", "journalctl -u {s} -f", "Like tail -f for the unit; Ctrl+C to stop."),
    ("L2", "Show only errors of {d} ({s}) since last boot", "journalctl -u {s} -b -p err", "Priority err and worse, current boot only."),
    ("L2", "Show the log of {d} ({s}) for the last hour", "journalctl -u {s} --since \"1 hour ago\"", "Time filters accept natural language."),
    ("L3", "Override settings of {d} ({s}) without editing the vendor unit", "sudo systemctl edit {s}", "Creates /etc/systemd/system/{s}.service.d/override.conf; survives package updates."),
    ("L3", "Show the open-files limit applied to {d} ({s})", "systemctl show {s} -p LimitNOFILE", "Services use systemd limits, not /etc/security/limits.conf."),
    ("L3", "List what {d} ({s}) depends on", "systemctl list-dependencies {s}", "Useful when a service fails because a dependency did not start."),
    ("L2", "See which unit file defines {d} ({s})", "systemctl cat {s}", "Prints the unit file and all drop-in overrides."),
    ("L4", "Limit CPU of {d} ({s}) to 50 percent", "sudo systemctl set-property {s} CPUQuota=50%", "cgroup limit, persists via a drop-in file."),
    ("L4", "Limit memory of {d} ({s}) to 1 GB", "sudo systemctl set-property {s} MemoryMax=1G", "The kernel OOM-kills the service if it exceeds the limit."),
    ("L2", "Find the main PID of {d} ({s})", "systemctl show -p MainPID --value {s}", "Use the PID with ps, lsof or /proc."),
]

PACKAGES = ["htop", "nginx", "curl", "wget", "git", "vim", "tmux", "rsync", "lsof", "tcpdump", "nmap", "net-tools",
            "bind-utils", "dnsutils", "sysstat", "iotop", "chrony", "fail2ban", "auditd", "aide", "lynis", "ansible",
            "docker.io", "podman", "python3-pip", "jq", "tree", "zip", "unzip", "mtr", "traceroute", "nfs-utils",
            "samba", "openssl", "certbot", "postgresql", "mariadb-server", "redis", "zabbix-agent2", "smartmontools",
            "haproxy", "keepalived", "postfix", "squid", "wireguard-tools", "openvpn", "bind9", "kea", "nfs-kernel-server",
            "cifs-utils", "acl", "attr", "lvm2", "mdadm", "parted", "xfsprogs", "e2fsprogs", "ncdu", "iperf3", "ethtool",
            "bash-completion", "shellcheck", "logrotate", "rsyslog", "auditd", "apparmor-utils", "policycoreutils-python-utils",
            "setroubleshoot-server", "unattended-upgrades", "dnf-automatic"]
PKG_ACTIONS = [
    ("L1", "debian", "Install {p} on Ubuntu/Debian", "sudo apt install -y {p}", "apt resolves and installs dependencies."),
    ("L1", "rhel", "Install {p} on Rocky/RHEL", "sudo dnf install -y {p}", "dnf resolves and installs dependencies."),
    ("L1", "debian", "Remove {p} on Ubuntu/Debian", "sudo apt remove {p}", "Keeps config files; use purge to remove them too."),
    ("L1", "rhel", "Remove {p} on Rocky/RHEL", "sudo dnf remove {p}", "Also removes packages that depend on it; read the list."),
    ("L2", "debian", "Show details and version of {p} (apt)", "apt show {p}", "Version, size, dependencies and description."),
    ("L2", "rhel", "Show details and version of {p} (dnf)", "dnf info {p}", "Version, repo, size and description."),
    ("L2", "debian", "List files installed by {p} (dpkg)", "dpkg -L {p}", "Find config files and binaries of a package."),
    ("L2", "rhel", "List files installed by {p} (rpm)", "rpm -ql {p}", "Find config files and binaries of a package."),
    ("L2", "debian", "Check if {p} is installed (dpkg)", "dpkg -l {p} 2>/dev/null | grep ^ii || echo not installed", "ii means installed."),
    ("L2", "rhel", "Check if {p} is installed (rpm)", "rpm -q {p}", "Prints the version or 'is not installed'."),
]

DOMAINS = ["ya.ru", "itmo.ru", "github.com", "gosuslugi.ru", "habr.com", "croc.ru", "vk.com", "example.com",
           "mail.ru", "sber.ru", "ozon.ru", "spbu.ru", "rbc.ru", "kernel.org"]
RECORDS = [("A", "IPv4 address"), ("AAAA", "IPv6 address"), ("MX", "mail servers"), ("NS", "name servers"),
           ("TXT", "TXT records (SPF, verification)"), ("SOA", "zone authority record"), ("CAA", "allowed certificate authorities")]

PORTS = OrderedDict([(22, "SSH"), (80, "HTTP"), (443, "HTTPS"), (53, "DNS"), (25, "SMTP"), (3306, "MySQL/MariaDB"),
                     (5432, "PostgreSQL"), (6379, "Redis"), (8080, "alternative HTTP"), (9100, "node_exporter"),
                     (10050, "Zabbix agent"), (445, "SMB"), (2049, "NFS"), (123, "NTP"), (3389, "RDP"), (8443, "alternative HTTPS")])
UDP_PORTS = {53, 123}

LOG_FILES = OrderedDict([
    ("/var/log/auth.log", "authentication log (Ubuntu)"), ("/var/log/secure", "authentication log (Rocky)"),
    ("/var/log/syslog", "system log (Ubuntu)"), ("/var/log/messages", "system log (Rocky)"),
    ("/var/log/nginx/access.log", "Nginx access log"), ("/var/log/nginx/error.log", "Nginx error log"),
    ("/var/log/kern.log", "kernel log (Ubuntu)"), ("/var/log/dpkg.log", "package install log (Ubuntu)"),
    ("/var/log/audit/audit.log", "audit log"), ("/var/log/fail2ban.log", "fail2ban log"),
])
PATTERNS = [("error", "the word error"), ("Failed password", "failed SSH passwords"), ("Accepted publickey", "successful key logins"),
            ("sudo", "sudo usage"), ("timeout", "timeouts"), ("denied", "permission denials"), ("OOM", "out-of-memory events"),
            ("segfault", "crashes (segfaults)"), (" 500 ", "HTTP 500 responses"), (" 404 ", "HTTP 404 responses")]

DIRS = ["/var/log", "/etc", "/home", "/srv", "/tmp", "/opt", "/var/www", "/var/lib/docker",
        "/var/lib/postgresql", "/var/backups", "/usr/local", "/root"]
EXTS = ["log", "conf", "sh", "txt", "tar.gz", "bak", "pdf", "py"]
SIZES = [("10M", "10 MB"), ("100M", "100 MB"), ("500M", "500 MB"), ("1G", "1 GB")]
AGES = [(1, "1 day"), (7, "7 days"), (30, "30 days"), (90, "90 days")]

MODES = [("600", "owner read/write only", "private keys, secrets"), ("640", "owner rw, group read", "config with secrets readable by a service group"),
         ("644", "owner rw, everyone read", "normal files"), ("700", "owner full, nobody else", "private directories, scripts"),
         ("750", "owner full, group read/execute", "team scripts and directories"), ("755", "owner full, everyone read/execute", "public programs and directories"),
         ("2770", "group full + SGID", "shared team folders"), ("1777", "everyone full + sticky bit", "shared temp directories"),
         ("0400", "owner read only", "certificates and keys that never change"), ("0440", "owner and group read only", "sudoers drop-in files")]
TARGETS = [("script.sh", "a script"), ("/srv/share", "a shared directory"), ("~/.ssh/id_ed25519", "an SSH private key"),
           ("/etc/app/app.conf", "an application config"), ("/srv/backups", "the backup directory")]

USERS = ["ivan", "olga", "alice", "bob", "deploy", "backup", "zabbix", "webadmin", "student", "auditor",
         "sergey", "anna", "dmitry", "maria", "jenkins", "gitlab-runner", "monitor", "intern", "contractor", "dbadmin"]
GROUPS = ["support", "developers", "docker", "wheel", "sudo", "www-data", "backup", "auditors"]

COMPRESS = [("z", "gz", "gzip (fast, common)"), ("j", "bz2", "bzip2 (smaller, slower)"), ("J", "xz", "xz (smallest, slowest)"), ("-zstd", "zst", "zstd (fast and small)")]

SYSCTLS = [("net.ipv4.ip_forward", "0", "disable routing between interfaces"), ("net.ipv4.tcp_syncookies", "1", "protect from SYN flood"),
           ("net.ipv4.conf.all.accept_redirects", "0", "ignore ICMP redirects"), ("net.ipv4.conf.all.send_redirects", "0", "do not send ICMP redirects"),
           ("net.ipv4.conf.all.rp_filter", "1", "reverse path filtering against spoofing"), ("net.ipv4.conf.all.log_martians", "1", "log impossible source addresses"),
           ("net.ipv4.icmp_echo_ignore_broadcasts", "1", "ignore broadcast pings"), ("kernel.randomize_va_space", "2", "full ASLR"),
           ("kernel.dmesg_restrict", "1", "only root reads kernel log"), ("kernel.kptr_restrict", "2", "hide kernel pointers"),
           ("fs.suid_dumpable", "0", "no core dumps from SUID programs"), ("vm.swappiness", "10", "prefer RAM over swap"),
           ("net.core.somaxconn", "4096", "bigger listen backlog for busy servers"), ("fs.file-max", "2097152", "system-wide open files limit"),
           ("net.ipv4.ip_local_port_range", "\"10240 65535\"", "more ephemeral ports for many outgoing connections"),
           ("vm.overcommit_memory", "1", "allow memory overcommit (Redis recommendation)")]

ANSIBLE_MODULES = [
    ("ping", "", "Test connectivity and Python on {g}", "L3"),
    ("command", "-a \"uptime\"", "Show uptime of every server in {g}", "L3"),
    ("shell", "-a \"df -h / | tail -1\"", "Check root disk usage on {g}", "L3"),
    ("setup", "-a \"filter=ansible_distribution*\"", "Show OS distribution facts for {g}", "L3"),
    ("apt", "-a \"name=htop state=present update_cache=true\" -b", "Install htop on Ubuntu servers in {g}", "L3"),
    ("dnf", "-a \"name=htop state=present\" -b", "Install htop on Rocky servers in {g}", "L3"),
    ("service", "-a \"name=nginx state=restarted\" -b", "Restart nginx on {g}", "L3"),
    ("user", "-a \"name=ivan groups=support append=true\" -b", "Create user ivan in group support on {g}", "L3"),
    ("copy", "-a \"src=./motd dest=/etc/motd mode=0644\" -b", "Copy a login message to {g}", "L3"),
    ("file", "-a \"path=/opt/lab state=directory mode=0755\" -b", "Create /opt/lab directory on {g}", "L3"),
    ("cron", "-a \"name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'\" -b", "Add a disk alert cron job on {g}", "L3"),
    ("reboot", "-b", "Reboot all servers in {g} and wait until back", "L4"),
    ("lineinfile", "-a \"path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true\" -b", "Disable root SSH login on {g}", "L4"),
    ("fetch", "-a \"src=/var/log/syslog dest=./logs/ flat=false\" -b", "Collect syslog from every server in {g}", "L3"),
]
ANSIBLE_GROUPS = ["all", "web", "infra", "ubuntu", "rocky", "db", "monitoring", "dev", "prod", "backup"]

DOCKER = [
    ("L2", "List running containers", "docker ps", "Add -a to include stopped ones."),
    ("L2", "List all images with size", "docker images", "docker image prune removes dangling images."),
    ("L2", "Show disk used by Docker", "docker system df", "Images, containers, volumes and build cache."),
    ("L3", "Free disk space used by unused Docker data", "docker system prune -f", "Add -a --volumes only if you are sure."),
]
IMAGES = ["nginx:stable", "postgres:16", "redis:7", "alpine:3.20", "ubuntu:24.04", "grafana/grafana:11.0.0", "prom/prometheus:v2.53.0"]


# ---------------------------------------------------------------- generators
def gen_services():
    for svc, desc in SERVICES.items():
        for lvl, t, c, e in SERVICE_ACTIONS:
            add(lvl, "Services (systemd)", t.format(d=desc, s=svc), c.format(s=svc), e.format(s=svc), ["systemd", svc])


def gen_packages():
    for p in PACKAGES:
        for lvl, distro, t, c, e in PKG_ACTIONS:
            add(lvl, "Packages", t.format(p=p), c.format(p=p), e, ["packages", p, "apt" if distro == "debian" else "dnf"], distro)


def gen_dns():
    for d in DOMAINS:
        for r, rd in RECORDS:
            add("L2", "Networking: DNS", f"Get the {rd} of {d}", f"dig {d} {r} +short", f"Queries {r} records with the system resolver.", ["dns", "dig", r])
            add("L2", "Networking: DNS", f"Get the {rd} of {d} from Google DNS 8.8.8.8", f"dig @8.8.8.8 {d} {r} +short",
                "Compare with the local resolver to find DNS problems.", ["dns", "dig", r, "troubleshooting"])
        add("L2", "Networking: DNS", f"Trace DNS resolution of {d} from the root servers", f"dig {d} +trace", "Shows each delegation step.", ["dns", "dig"])
        add("L1", "Networking: basics", f"Check if {d} is reachable", f"ping -c 4 {d}", "4 packets; look at loss and time.", ["ping", "network"])
        add("L2", "Networking: basics", f"Show the network path to {d}", f"traceroute {d}", "Each hop is a router; * means no reply.", ["traceroute", "network"])
        add("L2", "Networking: basics", f"Continuous path and loss report to {d}", f"mtr -rwc 20 {d}", "Better than traceroute for packet loss.", ["mtr", "network"])
        add("L2", "Networking: HTTP", f"Show HTTP response headers of {d}", f"curl -sI https://{d}", "Status code, server and redirects.", ["curl", "http"])
        add("L3", "Networking: HTTP", f"Measure HTTPS response time of {d}", f"curl -o /dev/null -s -w 'dns %{{time_namelookup}} connect %{{time_connect}} tls %{{time_appconnect}} total %{{time_total}}\\n' https://{d}",
            "Splits time into DNS, TCP, TLS and total.", ["curl", "performance"])
        add("L3", "TLS certificates", f"Show the certificate expiry date of {d}", f"echo | openssl s_client -connect {d}:443 -servername {d} 2>/dev/null | openssl x509 -noout -dates",
            "notAfter is the expiry date.", ["openssl", "tls"])
        add("L3", "TLS certificates", f"Show who issued the certificate of {d}", f"echo | openssl s_client -connect {d}:443 -servername {d} 2>/dev/null | openssl x509 -noout -issuer -subject",
            "Issuer is the CA, subject is the site.", ["openssl", "tls"])
    for ip in ["8.8.8.8", "77.88.8.8", "1.1.1.1", "192.168.56.10"]:
        add("L2", "Networking: DNS", f"Reverse lookup of IP {ip}", f"dig -x {ip} +short", "PTR record for the address.", ["dns", "ptr"])


def gen_ports():
    for port, name in PORTS.items():
        proto = "udp" if port in UDP_PORTS else "tcp"
        flag = "u" if proto == "udp" else "t"
        add("L2", "Networking: ports", f"Check which process listens on port {port} ({name})", f"sudo ss -{flag}lnp 'sport = :{port}'",
            "Shows the program and PID that owns the port.", ["ss", "ports", str(port)])
        if proto == "tcp":
            add("L2", "Networking: ports", f"Test if remote port {port} ({name}) is open on 192.168.56.20", f"nc -zv 192.168.56.20 {port}",
                "succeeded means a TCP connection was made.", ["nc", "ports", str(port)])
        add("L2", "Firewall: ufw", f"Allow {name} port {port}/{proto} in ufw", f"sudo ufw allow {port}/{proto}", "Rule applies to all sources.", ["ufw", "firewall", str(port)], "debian")
        add("L3", "Firewall: ufw", f"Allow {name} port {port}/{proto} only from 192.168.56.0/24 in ufw",
            f"sudo ufw allow from 192.168.56.0/24 to any port {port} proto {proto}", "Limits the service to the LAN.", ["ufw", "firewall", str(port)], "debian")
        add("L2", "Firewall: ufw", f"Block {name} port {port}/{proto} in ufw", f"sudo ufw deny {port}/{proto}", "Silently drops matching traffic.", ["ufw", "firewall", str(port)], "debian")
        add("L2", "Firewall: firewalld", f"Open {name} port {port}/{proto} permanently in firewalld",
            f"sudo firewall-cmd --permanent --add-port={port}/{proto} && sudo firewall-cmd --reload", "--permanent survives reboot; reload applies it.",
            ["firewalld", "firewall", str(port)], "rhel")
        add("L3", "Firewall: firewalld", f"Allow {name} port {port}/{proto} only from 192.168.56.0/24 in firewalld",
            f"sudo firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=192.168.56.0/24 port port={port} protocol={proto} accept' && sudo firewall-cmd --reload",
            "Rich rules filter by source address.", ["firewalld", "firewall", str(port)], "rhel")
        add("L2", "Firewall: firewalld", f"Close {name} port {port}/{proto} in firewalld",
            f"sudo firewall-cmd --permanent --remove-port={port}/{proto} && sudo firewall-cmd --reload", "Removes the permanent rule.", ["firewalld", "firewall", str(port)], "rhel")
        add("L3", "Networking: capture", f"Capture traffic on port {port} ({name}) for analysis", f"sudo tcpdump -i any -nn port {port} -w /tmp/port{port}.pcap",
            "Open the .pcap in Wireshark later.", ["tcpdump", "capture", str(port)])
        add("L3", "Firewall: nftables", f"Show nftables rules mentioning port {port}", f"sudo nft list ruleset | grep -n 'dport {port}'", "Low-level view under ufw and firewalld.", ["nftables", str(port)])


def gen_find():
    for d in DIRS:
        for ext in EXTS:
            add("L1", "Files: find", f"Find all .{ext} files under {d}", f"sudo find {d} -type f -name '*.{ext}'", "-name is case sensitive; -iname ignores case.", ["find", ext])
        for sz, szd in SIZES:
            add("L1", "Files: find", f"Find files larger than {szd} under {d}", f"sudo find {d} -type f -size +{sz} -exec ls -lh {{}} +", "Good first step for disk-full tickets.", ["find", "disk"])
        for days, dd in AGES:
            add("L2", "Files: find", f"Find files under {d} modified in the last {dd}", f"sudo find {d} -type f -mtime -{days}", "-mtime -N means newer than N days.", ["find", "audit"])
            add("L2", "Files: find", f"Find files under {d} not modified for more than {dd}", f"sudo find {d} -type f -mtime +{days}", "Candidates for cleanup or archive.", ["find", "cleanup"])
        add("L2", "Files: find", f"Find empty files and directories under {d}", f"sudo find {d} -empty", "Add -delete only after reviewing the list.", ["find"])
        add("L2", "Files: disk usage", f"Show the 10 biggest items in {d}", f"sudo du -xh {d} --max-depth=1 2>/dev/null | sort -h | tail -10", "-x stays on one filesystem.", ["du", "disk"])
        add("L3", "Files: find", f"Find world-writable files under {d}", f"sudo find {d} -xdev -type f -perm -0002", "Security audit: anyone can modify these.", ["find", "security"])
        add("L3", "Files: find", f"Find files under {d} with no valid owner", f"sudo find {d} -xdev \\( -nouser -o -nogroup \\)", "Left over after deleting users; reassign or remove.", ["find", "security"])
        add("L2", "Files: find", f"Count files under {d}", f"sudo find {d} -type f | wc -l", "Large counts can exhaust inodes.", ["find", "inodes"])


def gen_grep():
    for f, fd in LOG_FILES.items():
        for pat, pd in PATTERNS:
            add("L1", "Logs: grep", f"Search {pd} in the {fd}", f"sudo grep -i '{pat}' {f}", "-i ignores case; add -n for line numbers.", ["grep", "logs"])
            add("L2", "Logs: grep", f"Count {pd} in the {fd}", f"sudo grep -ci '{pat}' {f}", "-c prints only the number of matching lines.", ["grep", "logs", "count"])
        add("L1", "Logs: basics", f"Show the last 100 lines of the {fd}", f"sudo tail -n 100 {f}", "Most recent events are at the end.", ["tail", "logs"])
        add("L1", "Logs: basics", f"Follow the {fd} live", f"sudo tail -F {f}", "-F keeps following after log rotation.", ["tail", "logs"])
    nginx = "/var/log/nginx/access.log"
    extra = [
        ("Top 10 client IPs in the Nginx access log", f"awk '{{print $1}}' {nginx} | sort | uniq -c | sort -rn | head", "Find heavy users or attackers."),
        ("Top 10 requested URLs in the Nginx access log", f"awk '{{print $7}}' {nginx} | sort | uniq -c | sort -rn | head", "Most popular or most attacked paths."),
        ("Count HTTP status codes in the Nginx access log", f"awk '{{print $9}}' {nginx} | sort | uniq -c | sort -rn", "Spikes of 5xx mean backend problems."),
        ("Requests per minute in the Nginx access log", f"awk '{{print substr($4,2,17)}}' {nginx} | uniq -c | tail -20", "Shows traffic peaks."),
        ("Top user agents in the Nginx access log", f"awk -F'\"' '{{print $6}}' {nginx} | sort | uniq -c | sort -rn | head", "Spot bots and scanners."),
        ("Top IPs with failed SSH passwords (Ubuntu)", "sudo grep 'Failed password' /var/log/auth.log | grep -oE 'from [0-9.]+' | awk '{print $2}' | sort | uniq -c | sort -rn | head", "Candidates for fail2ban or firewall block."),
        ("Usernames attackers try over SSH (Ubuntu)", "sudo grep 'Invalid user' /var/log/auth.log | awk '{print $8}' | sort | uniq -c | sort -rn | head", "Shows brute-force dictionaries."),
    ]
    for t, c, e in extra:
        add("L2", "Logs: analysis", t, c, e, ["awk", "logs", "analysis"])


def gen_journal():
    windows = [("10 minutes ago", "last 10 minutes"), ("1 hour ago", "last hour"), ("today", "today"), ("yesterday", "since yesterday")]
    prios = [("err", "errors"), ("warning", "warnings"), ("crit", "critical messages")]
    for since, sd in windows:
        for p, pd in prios:
            add("L2", "Logs: journalctl", f"Show {pd} from the whole system {sd}", f"journalctl -p {p} --since \"{since}\" --no-pager", "Priority filter includes more severe levels.", ["journalctl", "logs"])
    base = [
        ("L1", "Show logs since the current boot", "journalctl -b", "Start of troubleshooting after a reboot."),
        ("L2", "Show errors from the previous boot", "journalctl -b -1 -p err", "Explains why a server crashed or rebooted."),
        ("L2", "List all recorded boots", "journalctl --list-boots", "Index 0 is current, -1 previous."),
        ("L2", "Show kernel messages from this boot", "journalctl -k", "Same as dmesg but with timestamps and history."),
        ("L2", "Show how much disk the journal uses", "journalctl --disk-usage", "Large journals cause disk-full alerts."),
        ("L2", "Shrink the journal to 200 MB", "sudo journalctl --vacuum-size=200M", "Deletes oldest archived journal files."),
        ("L2", "Delete journal entries older than 14 days", "sudo journalctl --vacuum-time=14d", "Time-based cleanup."),
        ("L3", "Export logs of a time window for an incident", "journalctl --since \"2026-11-06 22:00\" --until \"2026-11-06 23:00\" -o short-iso > incident.log", "ISO timestamps for reports."),
        ("L3", "Show logs as JSON for parsing", "journalctl -u nginx -o json-pretty -n 5", "Every field, including _PID and _SYSTEMD_UNIT."),
        ("L2", "Show logs of a specific program by name", "journalctl -t sudo --since today", "-t filters by syslog identifier."),
    ]
    for lvl, t, c, e in base:
        add(lvl, "Logs: journalctl", t, c, e, ["journalctl", "logs"])


def gen_permissions():
    for m, md, use in MODES:
        for tgt, tgd in TARGETS:
            add("L1", "Permissions", f"Set mode {m} ({md}) on {tgd} {tgt}", f"chmod {m} {tgt}", f"Typical for {use}.", ["chmod", "permissions", m])
    for u in USERS[:6]:
        for g in GROUPS[:6]:
            add("L1", "Permissions", f"Make {u} the owner and {g} the group of /srv/{g}", f"sudo chown -R {u}:{g} /srv/{g}", "-R applies to everything inside.", ["chown", "permissions"])
    extra = [
        ("L2", "Give user bob read access to /srv/share without changing its group", "sudo setfacl -m u:bob:rx /srv/share", "ACLs add exceptions on top of normal permissions."),
        ("L2", "Make new files in /srv/share inherit an ACL for group developers", "sudo setfacl -d -m g:developers:rwx /srv/share", "-d sets the default ACL for new files."),
        ("L2", "Show ACLs of /srv/share", "getfacl /srv/share", "A + in ls -l output means ACLs exist."),
        ("L2", "Remove all ACLs from /srv/share", "sudo setfacl -b /srv/share", "Back to normal permissions."),
        ("L3", "Find all SUID and SGID programs", "sudo find / -xdev -perm /6000 -type f 2>/dev/null", "Review regularly; unexpected entries may be backdoors."),
        ("L2", "Show the default permission mask", "umask", "0022 means new files 644, directories 755."),
        ("L3", "Make a file immutable even for root", "sudo chattr +i /etc/resolv.conf", "Remove with chattr -i; check with lsattr."),
        ("L2", "Show permissions as numbers", "stat -c '%a %U:%G %n' /etc/passwd /etc/shadow", "Easier to compare than rwx."),
    ]
    for lvl, t, c, e in extra:
        add(lvl, "Permissions", t, c, e, ["permissions", "acl"])


def gen_users():
    for u in USERS:
        rows = [
            ("L1", f"Create user {u} with a home directory and bash", f"sudo useradd -m -s /bin/bash {u}", "-m creates /home/USER."),
            ("L1", f"Set or reset the password of {u}", f"sudo passwd {u}", "Prompts for the new password."),
            ("L2", f"Force {u} to change password at next login", f"sudo chage -d 0 {u}", "Common after a reset ticket."),
            ("L2", f"Show password ageing of {u}", f"sudo chage -l {u}", "First check when a user cannot log in."),
            ("L2", f"Set password expiry of {u} to 90 days with 7 days warning", f"sudo chage -M 90 -W 7 {u}", "Matches typical security policy."),
            ("L2", f"Lock the account {u}", f"sudo usermod -L {u}", "Adds ! to the password hash; key logins may still work, also expire it."),
            ("L2", f"Unlock the account {u}", f"sudo usermod -U {u}", "Reverses -L."),
            ("L2", f"Expire the account {u} immediately", f"sudo chage -E 0 {u}", "Blocks all login methods, including SSH keys."),
            ("L2", f"Show groups of {u}", f"id {u}", "uid, gid and all groups."),
            ("L2", f"Show last logins of {u}", f"last -n 10 {u}", "From /var/log/wtmp."),
            ("L2", f"Reset failed login counter of {u} (pam_faillock)", f"sudo faillock --user {u} --reset", "Unblocks after too many wrong passwords."),
            ("L1", f"Delete user {u} and the home directory", f"sudo userdel -r {u}", "Back up the home first if needed."),
            ("L2", f"Switch to user {u} with their environment", f"sudo -iu {u}", "Test permissions as that user."),
            ("L3", f"List processes running as {u}", f"ps -u {u} -o pid,etime,cmd", "Before deleting a user, check running jobs."),
            ("L2", f"Show the crontab of {u}", f"sudo crontab -l -u {u}", "Find scheduled jobs of a user."),
        ]
        for lvl, t, c, e in rows:
            add(lvl, "Users and groups", t, c, e, ["users", u])
        for g in GROUPS:
            add("L1", "Users and groups", f"Add {u} to group {g} without removing other groups", f"sudo usermod -aG {g} {u}", "-a is essential; without it other groups are removed.", ["users", "groups", g])
            add("L2", "Users and groups", f"Remove {u} from group {g}", f"sudo gpasswd -d {u} {g}", "Takes effect at next login.", ["users", "groups", g])
    for g in GROUPS:
        add("L1", "Users and groups", f"Create group {g}", f"sudo groupadd {g}", "Fails if it already exists.", ["groups", g])
        add("L1", "Users and groups", f"List members of group {g}", f"getent group {g}", "Works for local and directory groups.", ["groups", g])


CRON_SPECS = []


def build_cron():
    for n in [1, 2, 3, 5, 10, 15, 20, 30]:
        CRON_SPECS.append((f"every {n} minute{'s' if n > 1 else ''}", f"*/{n} * * * *"))
    for n in [2, 3, 4, 6, 8, 12]:
        CRON_SPECS.append((f"every {n} hours", f"0 */{n} * * *"))
    for h in [0, 1, 2, 3, 4, 6, 7, 8, 9, 12, 18, 22, 23]:
        CRON_SPECS.append((f"every day at {h:02d}:00", f"0 {h} * * *"))
        CRON_SPECS.append((f"every day at {h:02d}:30", f"30 {h} * * *"))
    days = [("Monday", 1), ("Tuesday", 2), ("Wednesday", 3), ("Thursday", 4), ("Friday", 5), ("Saturday", 6), ("Sunday", 0)]
    for name, d in days:
        for h in [3, 9, 18]:
            CRON_SPECS.append((f"every {name} at {h:02d}:00", f"0 {h} * * {d}"))
    CRON_SPECS.extend([
        ("every weekday at 09:00", "0 9 * * 1-5"), ("every weekend day at 10:00", "0 10 * * 6,0"),
        ("every 15 minutes during working hours on weekdays", "*/15 9-18 * * 1-5"), ("on the 1st of every month at 00:05", "5 0 1 * *"),
        ("on the 15th of every month at 12:00", "0 12 15 * *"), ("every quarter (1 Jan, Apr, Jul, Oct) at 06:00", "0 6 1 1,4,7,10 *"),
        ("once a year on 1 January at 00:00", "0 0 1 1 *"), ("at every reboot", "@reboot"), ("every hour at minute 5", "5 * * * *"),
        ("twice a day at 06:00 and 18:00", "0 6,18 * * *"), ("every 10 minutes at night 00:00 to 05:59", "*/10 0-5 * * *"),
    ])


CRON_JOBS = [
    ("run the disk alert", "/opt/lab/scripts/disk_alert.sh 85 >> /var/log/disk_alert.log 2>&1"),
    ("back up /etc", "/opt/lab/scripts/backup.sh /etc /srv/backups 14 >> /var/log/backup.log 2>&1"),
    ("run the health check", "/opt/lab/scripts/health_check.sh > /var/log/health.txt 2>&1"),
    ("clean /tmp files older than 7 days", "find /tmp -type f -mtime +7 -delete"),
    ("sync the share to the backup server", "flock -n /run/lock/sync.lock rsync -a /srv/share/ backup:/share/"),
    ("check TLS certificates", "/opt/lab/scripts/ssl_expiry_check.sh -d 14 ya.ru itmo.ru >> /var/log/ssl.log 2>&1"),
    ("restart crashed services", "/opt/lab/scripts/service_watchdog.sh nginx ssh >> /var/log/watchdog.log 2>&1"),
    ("dump the PostgreSQL database", "pg_dump -U postgres appdb | gzip > /srv/backups/appdb-$(date +\\%F).sql.gz"),
]


def gen_cron():
    build_cron()
    for desc, spec in CRON_SPECS:
        for jd, job in CRON_JOBS:
            add("L1" if spec.startswith(("0 ", "30 ", "*/")) else "L2", "Cron", f"Cron: {jd} {desc}", f"{spec} {job}",
                f"Schedule '{spec}'. Add with crontab -e; % must be written as \\% inside crontab.", ["cron", "schedule"])
    for desc, spec in CRON_SPECS:
        if spec == "@reboot":
            continue
        oc = spec_to_oncalendar(spec)
        if oc:
            add("L3", "Cron: systemd timers", f"systemd timer equivalent of cron '{spec}' ({desc})", f"OnCalendar={oc}",
                "Put in [Timer] of a .timer unit; check with systemd-analyze calendar.", ["systemd", "timer"])


def spec_to_oncalendar(spec):
    parts = spec.split()
    if len(parts) != 5:
        return None
    m, h, dom, mon, dow = parts
    if any(x for x in (dom, mon) if x != "*") or dow != "*":
        return None
    if m.startswith("*/") and h == "*":
        return f"*:0/{m[2:]}"
    if m.isdigit() and h.startswith("*/"):
        return f"0/{h[2:]}:{int(m):02d}"
    if m.isdigit() and h.isdigit():
        return f"*-*-* {int(h):02d}:{int(m):02d}:00"
    return None


def gen_archives():
    for flag, ext, desc in COMPRESS:
        for src in ["/etc", "/var/www", "/home/ivan", "/srv/share", "/opt/app"]:
            name = src.strip("/").replace("/", "-")
            if flag == "-zstd":
                create = f"sudo tar --zstd -cpf /srv/backups/{name}.tar.{ext} {src}"
                extract = f"sudo tar --zstd -xpf /srv/backups/{name}.tar.{ext} -C /tmp/restore"
                listc = f"tar --zstd -tf /srv/backups/{name}.tar.{ext} | head"
            else:
                create = f"sudo tar -c{flag}pf /srv/backups/{name}.tar.{ext} {src}"
                extract = f"sudo tar -x{flag}pf /srv/backups/{name}.tar.{ext} -C /tmp/restore"
                listc = f"tar -t{flag}f /srv/backups/{name}.tar.{ext} | head"
            add("L1", "Backup and archives", f"Archive {src} with {desc}", create, "-p keeps permissions.", ["tar", "backup", ext])
            add("L2", "Backup and archives", f"Restore the {ext} archive of {src} into /tmp/restore", extract, "Restore to a test path first, then compare.", ["tar", "restore", ext])
            add("L1", "Backup and archives", f"List the contents of the {ext} archive of {src}", listc, "Verify a backup without extracting.", ["tar", "verify", ext])
    for src in ["/etc/", "/var/www/", "/srv/share/", "/home/"]:
        add("L2", "Backup and archives", f"Mirror {src} to backup-host over SSH", f"rsync -aAXv --delete {src} backup-host:/backups{src}", "--delete makes an exact mirror; test with -n first.", ["rsync", "backup"])
        add("L2", "Backup and archives", f"Dry-run a mirror of {src} to see what would change", f"rsync -aAXvn --delete {src} backup-host:/backups{src}", "-n shows actions without doing them.", ["rsync", "backup"])
        add("L3", "Backup and archives", f"Compare {src} with its restored copy", f"diff -r {src} /tmp/restore{src} && echo identical", "Proves the backup can be restored.", ["diff", "restore"])


def gen_storage():
    rows = [
        ("L1", "Show all disks and partitions with filesystems", "lsblk -f"),
        ("L1", "Show disk space of mounted filesystems", "df -hT"),
        ("L2", "Show inode usage", "df -i"),
        ("L2", "Show UUIDs of all block devices", "sudo blkid"),
        ("L2", "Test /etc/fstab without rebooting", "sudo mount -a"),
        ("L2", "Show physical volumes, volume groups and logical volumes", "sudo pvs; sudo vgs; sudo lvs"),
        ("L3", "Check SMART health of disk /dev/sda", "sudo smartctl -H /dev/sda"),
        ("L3", "Show which processes use /data (before unmount)", "sudo fuser -vm /data"),
        ("L2", "Find deleted files still holding disk space", "sudo lsof +L1"),
        ("L2", "Show swap usage", "swapon --show; free -h"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Storage and LVM", t, c, "Core storage check.", ["storage"])
    for disk in ["sdb", "sdc", "sdd", "vdb", "vdc"]:
        for fs in ["ext4", "xfs"]:
            add("L2", "Storage and LVM", f"Create an {fs} filesystem on /dev/{disk}1", f"sudo mkfs.{fs} /dev/{disk}1", "Destroys existing data on the partition.", ["mkfs", fs])
            add("L2", "Storage and LVM", f"Mount /dev/{disk}1 ({fs}) permanently on /data by UUID",
                f"echo \"UUID=$(sudo blkid -s UUID -o value /dev/{disk}1) /data {fs} defaults,nofail 0 2\" | sudo tee -a /etc/fstab && sudo mount -a",
                "nofail prevents emergency mode if the disk is missing.", ["fstab", fs])
        add("L3", "Storage and LVM", f"Add /dev/{disk} as an LVM physical volume to vg_data", f"sudo pvcreate /dev/{disk} && sudo vgextend vg_data /dev/{disk}", "Grows the volume group capacity.", ["lvm"])
    for size in ["1G", "2G", "5G", "10G", "20G"]:
        for lv in ["lv_app", "lv_var", "lv_home"]:
            add("L3", "Storage and LVM", f"Extend {lv} by {size} online, filesystem included", f"sudo lvextend -r -L +{size} /dev/vg_data/{lv}", "-r resizes ext4/xfs too.", ["lvm", "resize"])
        add("L2", "Storage and LVM", f"Create a {size} swap file", f"sudo fallocate -l {size} /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile",
            "Add to /etc/fstab to keep after reboot.", ["swap"])


def gen_processes():
    progs = ["nginx", "java", "python3", "postgres", "dockerd", "rsync", "backup.sh", "node", "php-fpm", "mysqld"]
    for p in progs:
        rows = [
            ("L1", f"Find PIDs of {p}", f"pgrep -a {p}"),
            ("L2", f"Gracefully stop all {p} processes", f"sudo pkill -TERM {p}"),
            ("L3", f"Force kill hung {p} processes", f"sudo pkill -KILL {p}"),
            ("L2", f"Show CPU and memory of {p} processes", f"ps -C {p} -o pid,user,%cpu,%mem,etime,cmd"),
            ("L3", f"Show files opened by {p}", f"sudo lsof -c {p} | head -30"),
            ("L3", f"Count open file descriptors of {p}", f"for p in $(pgrep {p}); do echo \"$p $(sudo ls /proc/$p/fd | wc -l)\"; done"),
            ("L3", f"Lower the priority of running {p}", f"sudo renice +10 -p $(pgrep {p} | tr '\\n' ' ')"),
            ("L4", f"Trace system calls of {p} for 10 seconds", f"sudo timeout 10 strace -f -p $(pgrep -o {p}) -o /tmp/{p}.strace"),
        ]
        for lvl, t, c in rows:
            add(lvl, "Processes", t, c, "Signals: TERM asks politely, KILL cannot be ignored.", ["process", p])
    rows = [
        ("L1", "Show the top 10 CPU consumers", "ps aux --sort=-%cpu | head -11"),
        ("L1", "Show the top 10 memory consumers", "ps aux --sort=-%mem | head -11"),
        ("L2", "Show the process tree", "pstree -p | head -50"),
        ("L2", "Find zombie processes", "ps -eo stat,pid,ppid,cmd | awk '$1 ~ /Z/'"),
        ("L2", "Show load average and number of CPUs", "uptime; nproc"),
        ("L3", "Show per-CPU usage every second, 3 times", "mpstat -P ALL 1 3"),
        ("L3", "Show per-process CPU, memory and disk every second", "pidstat -urd 1 5"),
        ("L3", "Show memory, swap and IO wait every second", "vmstat 1 5"),
        ("L3", "Show disk utilisation and latency", "iostat -xz 1 3"),
        ("L3", "Find processes killed by the OOM killer", "journalctl -k | grep -i -E 'out of memory|killed process'"),
        ("L2", "Run a long command that survives logout", "nohup ./long_job.sh > job.log 2>&1 &"),
        ("L2", "Start a persistent terminal session", "tmux new -s work"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Processes", t, c, "Performance and process basics.", ["process", "performance"])


def gen_ssh():
    hosts = ["192.168.56.10", "192.168.56.20", "web1.lab.local", "db1.lab.local", "backup-host"]
    for h in hosts:
        for u in ["ivan", "deploy", "admin"]:
            add("L1", "SSH and remote", f"Connect to {h} as {u} with SSH", f"ssh {u}@{h}", "Add -v to debug connection problems.", ["ssh", u])
            add("L2", "SSH and remote", f"Copy your SSH key to {u}@{h}", f"ssh-copy-id {u}@{h}", "Enables password-less login.", ["ssh", "keys"])
            add("L2", "SSH and remote", f"Run uptime on {h} as {u} without opening a shell", f"ssh {u}@{h} uptime", "Good for quick checks and scripts.", ["ssh"])
            add("L2", "SSH and remote", f"Copy app.tar.gz to /tmp on {h} as {u}", f"scp app.tar.gz {u}@{h}:/tmp/", "scp uses SSH; rsync is better for big folders.", ["scp"])
            add("L3", "SSH and remote", f"Open a tunnel to PostgreSQL on {h} via SSH as {u}", f"ssh -L 5432:localhost:5432 {u}@{h}", "Then connect to localhost:5432 locally.", ["ssh", "tunnel"])
            add("L3", "SSH and remote", f"Reach {h} through jump host bastion as {u}", f"ssh -J {u}@bastion {u}@{h}", "ProxyJump for servers without public access.", ["ssh", "jump"])
    rows = [
        ("L1", "Generate a modern SSH key", "ssh-keygen -t ed25519 -C \"name@company\""),
        ("L2", "Show the fingerprint of your SSH key", "ssh-keygen -lf ~/.ssh/id_ed25519.pub"),
        ("L2", "Remove an old host key after server reinstall", "ssh-keygen -R 192.168.56.10"),
        ("L3", "Test sshd config syntax before reload", "sudo sshd -t"),
        ("L3", "Show effective sshd settings", "sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication|maxauthtries'"),
        ("L2", "Show banned IPs in fail2ban for sshd", "sudo fail2ban-client status sshd"),
        ("L2", "Unban an IP in fail2ban", "sudo fail2ban-client set sshd unbanip 203.0.113.5"),
        ("L2", "Fix permissions of a user's .ssh directory", "chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"),
    ]
    for lvl, t, c in rows:
        add(lvl, "SSH and remote", t, c, "SSH administration.", ["ssh"])


def gen_sysctl():
    for key, val, why in SYSCTLS:
        add("L3", "Hardening: kernel", f"Check current value of {key}", f"sysctl {key}", f"Recommended {val}: {why}.", ["sysctl", "kernel"])
        add("L3", "Hardening: kernel", f"Set {key} = {val} now ({why})", f"sudo sysctl -w {key}={val}", "Lost after reboot; persist it in /etc/sysctl.d/.", ["sysctl", "kernel"])
        add("L4", "Hardening: kernel", f"Persist {key} = {val} across reboots", f"echo '{key} = {val.strip(chr(34))}' | sudo tee -a /etc/sysctl.d/99-lab.conf && sudo sysctl --system",
            why.capitalize() + ".", ["sysctl", "kernel", "persist"])


def gen_hardening():
    rows = [
        ("L3", "Disable root SSH login", "echo 'PermitRootLogin no' | sudo tee /etc/ssh/sshd_config.d/10-root.conf && sudo sshd -t && sudo systemctl reload ssh"),
        ("L3", "Disable SSH password authentication", "echo 'PasswordAuthentication no' | sudo tee /etc/ssh/sshd_config.d/11-pass.conf && sudo sshd -t && sudo systemctl reload ssh"),
        ("L3", "Limit SSH to members of group ssh-users", "echo 'AllowGroups ssh-users' | sudo tee /etc/ssh/sshd_config.d/12-groups.conf && sudo sshd -t && sudo systemctl reload ssh"),
        ("L3", "Find accounts with empty passwords", "sudo awk -F: '($2==\"\"){print $1}' /etc/shadow"),
        ("L3", "Find accounts with UID 0 besides root", "awk -F: '($3==0 && $1!=\"root\"){print $1}' /etc/passwd"),
        ("L3", "Require 12-character passwords", "sudo sed -i 's/^#\\? *minlen.*/minlen = 12/' /etc/security/pwquality.conf"),
        ("L3", "Set maximum password age to 90 days for new users", "sudo sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS 90/' /etc/login.defs"),
        ("L3", "Enable automatic security updates on Ubuntu", "sudo apt install -y unattended-upgrades && sudo dpkg-reconfigure -plow unattended-upgrades"),
        ("L3", "Enable automatic security updates on Rocky", "sudo dnf install -y dnf-automatic && sudo systemctl enable --now dnf-automatic-install.timer"),
        ("L3", "Mount /tmp with noexec,nosuid,nodev", "echo 'tmpfs /tmp tmpfs defaults,noexec,nosuid,nodev,size=1G 0 0' | sudo tee -a /etc/fstab && sudo mount -o remount /tmp"),
        ("L3", "Block USB storage kernel module", "echo 'install usb-storage /bin/true' | sudo tee /etc/modprobe.d/usb-storage.conf"),
        ("L3", "List enabled services to find unneeded ones", "systemctl list-unit-files --state=enabled --type=service"),
        ("L3", "Show all listening ports and programs", "sudo ss -tulpn"),
        ("L3", "Set a legal login banner", "echo 'Authorised access only. Activity is logged.' | sudo tee /etc/issue.net"),
        ("L3", "Allow cron only for root and admin", "printf 'root\\nadmin\\n' | sudo tee /etc/cron.allow"),
        ("L4", "Run a full Lynis security audit", "sudo lynis audit system --quick"),
        ("L4", "Show the Lynis hardening index", "sudo grep hardening_index /var/log/lynis-report.dat"),
        ("L4", "Initialise the AIDE integrity database", "sudo aideinit && sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db"),
        ("L4", "Check files against the AIDE database", "sudo aide --check"),
        ("L3", "Run the lab hardening audit", "sudo /opt/lab/scripts/harden_audit.sh"),
        ("L4", "Check SELinux mode", "getenforce && sestatus"),
        ("L4", "Show recent SELinux denials", "sudo ausearch -m avc -ts recent"),
        ("L4", "Restore SELinux contexts under /srv/web", "sudo restorecon -Rv /srv/web"),
        ("L4", "Allow Nginx to connect to backends under SELinux", "sudo setsebool -P httpd_can_network_connect on"),
        ("L4", "Show AppArmor profiles and their mode", "sudo aa-status"),
        ("L3", "Check fail2ban jail list", "sudo fail2ban-client status"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Hardening", t, c, "Part of a CIS-style baseline; re-run the audit after the change.", ["hardening", "security"],
            "rhel" if "Rocky" in t or "SELinux" in t else ("debian" if "Ubuntu" in t or "AppArmor" in t else "any"))
    watches = ["/etc/passwd", "/etc/shadow", "/etc/group", "/etc/sudoers", "/etc/ssh/sshd_config", "/etc/crontab", "/etc/hosts", "/etc/fstab"]
    for w in watches:
        k = os.path.basename(w).replace(".", "_")
        add("L4", "Hardening: auditd", f"Audit every write to {w}", f"sudo auditctl -w {w} -p wa -k {k}", "Persist the rule in /etc/audit/rules.d/.", ["auditd", "audit"])
        add("L4", "Hardening: auditd", f"Find who changed {w}", f"sudo ausearch -k {k} -i", "Shows user, time, program and result.", ["auditd", "investigation"])


def gen_ansible():
    for g in ANSIBLE_GROUPS:
        for mod, args, t, lvl in ANSIBLE_MODULES:
            add(lvl, "Ansible", "Ansible: " + t.format(g=f"group '{g}'"), f"ansible {g} -m {mod} {args}".strip(), "Ad-hoc command from the ansible/ directory.", ["ansible", mod, g])
    plays = ["01-baseline", "02-users", "03-ssh-hardening", "04-firewall", "05-patching", "06-cron-jobs", "07-nginx", "08-health-report"]
    for p in plays:
        add("L3", "Ansible", f"Dry-run playbook {p} and show the diff", f"ansible-playbook playbooks/{p}.yml --check --diff", "Nothing changes; review before applying.", ["ansible", "playbook"])
        add("L3", "Ansible", f"Apply playbook {p} only to the web group", f"ansible-playbook playbooks/{p}.yml --limit web", "--limit narrows the target hosts.", ["ansible", "playbook"])
        add("L3", "Ansible", f"Check syntax of playbook {p}", f"ansible-playbook --syntax-check playbooks/{p}.yml", "Run in CI before merging.", ["ansible", "ci"])
    rows = [
        ("L3", "List hosts in the inventory", "ansible-inventory --graph"),
        ("L3", "Encrypt a secrets file", "ansible-vault create group_vars/all/vault.yml"),
        ("L3", "Run the full site playbook with vault password prompt", "ansible-playbook site.yml --ask-vault-pass"),
        ("L4", "Run only tasks tagged ssh", "ansible-playbook site.yml --tags ssh"),
        ("L4", "Run on 5 hosts at a time", "ansible-playbook site.yml --forks 5"),
        ("L3", "Show documentation of a module", "ansible-doc ansible.builtin.cron"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Ansible", t, c, "Ansible operations.", ["ansible"])


def gen_docker():
    for lvl, t, c, e in DOCKER:
        add(lvl, "Containers", t, c, e, ["docker"])
    for img in IMAGES:
        name = img.split("/")[-1].split(":")[0]
        rows = [
            ("L2", f"Download image {img}", f"docker pull {img}"),
            ("L2", f"Run {img} in the background as {name}", f"docker run -d --name {name} --restart unless-stopped {img}"),
            ("L2", f"Show logs of container {name}", f"docker logs --tail 100 -f {name}"),
            ("L2", f"Open a shell in container {name}", f"docker exec -it {name} sh"),
            ("L2", f"Stop and remove container {name}", f"docker stop {name} && docker rm {name}"),
            ("L3", f"Show resource usage of container {name}", f"docker stats --no-stream {name}"),
            ("L3", f"Inspect IP address of container {name}", f"docker inspect -f '{{{{range .NetworkSettings.Networks}}}}{{{{.IPAddress}}}}{{{{end}}}}' {name}"),
            ("L3", f"Limit container {name} to 1 CPU and 512 MB", f"docker update --cpus 1 --memory 512m --memory-swap 512m {name}"),
        ]
        for lvl, t, c in rows:
            add(lvl, "Containers", t, c, "Podman accepts the same commands.", ["docker", name])


def gen_text():
    rows = [
        ("L1", "Show line count, word count and size of a file", "wc -lwc file.txt"),
        ("L1", "Show unique lines and how often they appear", "sort file.txt | uniq -c | sort -rn"),
        ("L1", "Show the 3rd column of a space-separated file", "awk '{print $3}' file.txt"),
        ("L1", "Show usernames from /etc/passwd", "cut -d: -f1 /etc/passwd"),
        ("L2", "Replace a word in a file in place with a backup", "sed -i.bak 's/old/new/g' file.conf"),
        ("L2", "Delete comment and empty lines from a config view", "grep -Ev '^\\s*(#|$)' /etc/ssh/sshd_config"),
        ("L2", "Print lines 10 to 20 of a file", "sed -n '10,20p' file.txt"),
        ("L2", "Compare two config files side by side", "diff -y --suppress-common-lines a.conf b.conf"),
        ("L2", "Sum a column of numbers", "awk '{s+=$1} END {print s}' numbers.txt"),
        ("L2", "Pretty-print JSON", "jq . data.json"),
        ("L3", "Extract a field from JSON", "jq -r '.items[].name' data.json"),
        ("L2", "Convert Windows line endings to Linux", "sed -i 's/\\r$//' script.sh"),
        ("L2", "Show non-printable characters in a file", "cat -A file.txt | head"),
        ("L2", "Search recursively for a string in configs", "grep -Rn 'listen' /etc/nginx/"),
        ("L3", "Show lines that appear in file1 but not file2", "comm -23 <(sort file1) <(sort file2)"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Text processing", t, c, "Classic text tools used every day in logs and configs.", ["text"])


def gen_bash():
    rows = [
        ("L2", "Make a script stop on errors and unset variables", "set -euo pipefail"),
        ("L2", "Check the exit code of the last command", "echo $?"),
        ("L2", "Loop over all .log files", "for f in /var/log/*.log; do echo \"$f\"; done"),
        ("L2", "Read a file line by line", "while IFS= read -r line; do echo \"$line\"; done < file.txt"),
        ("L2", "Run a command only if the previous succeeded", "mkdir /tmp/x && cd /tmp/x"),
        ("L2", "Use a default value for an argument", "threshold=\"${1:-85}\""),
        ("L2", "Check that a command exists", "command -v jq >/dev/null || { echo 'jq missing'; exit 1; }"),
        ("L3", "Run cleanup when the script exits", "trap 'rm -f \"$tmp\"' EXIT"),
        ("L3", "Create a safe temporary file", "tmp=$(mktemp)"),
        ("L3", "Lint a script for common mistakes", "shellcheck script.sh"),
        ("L2", "Add a timestamp to every output line", "./job.sh | while read -r l; do echo \"$(date '+%F %T') $l\"; done"),
        ("L3", "Run a function on several hosts in parallel", "for h in web1 web2 db1; do ssh \"$h\" uptime & done; wait"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Bash scripting", t, c, "Building blocks for admin scripts.", ["bash", "scripting"])


def gen_network_config():
    ifaces = ["eth0", "eth1", "ens33", "enp0s8"]
    for i in ifaces:
        rows = [
            ("L1", f"Show IP addresses of {i}", f"ip addr show {i}"),
            ("L2", f"Show errors and dropped packets on {i}", f"ip -s link show {i}"),
            ("L2", f"Temporarily add IP 192.168.56.50/24 to {i}", f"sudo ip addr add 192.168.56.50/24 dev {i}"),
            ("L2", f"Bring interface {i} down and up", f"sudo ip link set {i} down && sudo ip link set {i} up"),
            ("L3", f"Show link speed and duplex of {i}", f"sudo ethtool {i} | grep -E 'Speed|Duplex|Link detected'"),
            ("L2", f"Show NetworkManager settings of {i} (Rocky)", f"nmcli device show {i}"),
        ]
        for lvl, t, c in rows:
            add(lvl, "Networking: interfaces", t, c, "Interface configuration and checks.", ["ip", "interface", i])
    rows = [
        ("L1", "Show the routing table", "ip route"),
        ("L2", "Show which route is used to reach 8.8.8.8", "ip route get 8.8.8.8"),
        ("L2", "Add a temporary static route to 10.10.0.0/16 via 192.168.56.1", "sudo ip route add 10.10.0.0/16 via 192.168.56.1"),
        ("L2", "Show the ARP / neighbour table", "ip neigh"),
        ("L2", "Show DNS servers in use", "resolvectl status"),
        ("L2", "Apply netplan safely with automatic rollback", "sudo netplan try"),
        ("L2", "Show all TCP connections and their state counts", "ss -tan | awk 'NR>1{print $1}' | sort | uniq -c"),
        ("L2", "Show the hostname and set a new one", "hostnamectl; sudo hostnamectl set-hostname web1"),
        ("L2", "Check time sync status", "timedatectl; chronyc tracking"),
        ("L3", "Scan open ports on a lab host", "nmap -sV 192.168.56.20"),
        ("L3", "Measure bandwidth between two lab hosts", "iperf3 -s   # on server;  iperf3 -c 192.168.56.20   # on client"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Networking: basics", t, c, "Network administration basics.", ["network"])


def gen_troubleshooting():
    tickets = [
        ("Website returns 502 Bad Gateway", "systemctl status nginx; journalctl -u nginx -n 50; ss -tlnp | grep -E ':80|:8080'", "Backend is down or Nginx cannot reach it; see runbooks/service-down.md."),
        ("Server is slow", "uptime; top -o %CPU; vmstat 1 5; iostat -xz 1 3", "Check load vs cores, IO wait and swap; runbooks/high-load.md."),
        ("No space left on device", "df -h; df -i; sudo du -xh / --max-depth=2 | sort -h | tail; sudo lsof +L1", "runbooks/disk-full.md."),
        ("User cannot SSH in", "ssh -v user@host; sudo chage -l user; journalctl -u ssh -n 50", "runbooks/ssh-access.md."),
        ("Domain names do not resolve", "resolvectl status; dig ya.ru; dig @8.8.8.8 ya.ru", "runbooks/dns-failure.md."),
        ("Server went into emergency mode after reboot", "journalctl -xb | grep -i mount; cat /etc/fstab", "Usually a bad fstab line; docs/24-boot-recovery.md."),
        ("Cron job did not run", "grep CRON /var/log/syslog | tail; crontab -l; ls -l /path/to/script", "PATH, permissions or % escaping; docs/16-cron-scenarios.md."),
        ("Service fails to start after config change", "systemctl status SERVICE; journalctl -u SERVICE -n 50; nginx -t", "Validate config syntax and read the first error."),
        ("Permission denied on a shared folder", "id user; ls -ld /srv/share; getfacl /srv/share; ls -Z /srv/share", "Check groups, mode, ACL and SELinux context."),
        ("Too many open files", "systemctl show SERVICE -p LimitNOFILE; ls /proc/PID/fd | wc -l", "Raise LimitNOFILE in a drop-in; docs/25-performance-tuning.md."),
        ("Clock is wrong and Kerberos login fails", "timedatectl; chronyc sources", "Fix NTP; Kerberos allows only 5 minutes skew."),
        ("Package install fails with lock error (Ubuntu)", "ps aux | grep -E 'apt|dpkg'; sudo lsof /var/lib/dpkg/lock-frontend", "Wait for unattended-upgrades; never delete the lock blindly."),
        ("Certificate expired warning in browser", "/opt/lab/scripts/ssl_expiry_check.sh site.example.ru", "Renew, reload web server, monitor expiry."),
        ("Host unreachable alert from monitoring", "ping host; ip neigh; ssh host; check console", "Network, firewall or host down; escalate with facts."),
        ("High memory usage and OOM kills", "free -h; ps aux --sort=-%mem | head; journalctl -k | grep -i oom", "Find the leak, set MemoryMax, add swap if needed."),
        ("Docker host disk full", "docker system df; docker system prune", "Old images and logs; set log rotation in daemon.json."),
        ("Login to directory account fails", "realm list; systemctl status sssd; sudo sss_cache -E", "SSSD cache or domain trust problem."),
        ("Backup job reports success but files are missing", "tar -tzf /srv/backups/latest.tar.gz | head; check exclude rules", "Always test restores."),
    ]
    for t, c, e in tickets:
        add("L2", "Troubleshooting tickets", f"Ticket: {t}", c, e, ["troubleshooting", "ticket"])


def gen_web():
    sites = ["shop.lab.local", "api.lab.local", "wiki.lab.local", "grafana.lab.local", "intranet.lab.local", "status.lab.local"]
    for site in sites:
        n = site.split(".")[0]
        rows = [
            ("L2", f"Create the Nginx site file for {site}", f"sudo nano /etc/nginx/sites-available/{n}", "server_name, root and listen go here.", "debian"),
            ("L2", f"Enable the Nginx site {site}", f"sudo ln -s /etc/nginx/sites-available/{n} /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx", "Always nginx -t before reload.", "debian"),
            ("L2", f"Disable the Nginx site {site}", f"sudo rm /etc/nginx/sites-enabled/{n} && sudo nginx -t && sudo systemctl reload nginx", "Config stays in sites-available.", "debian"),
            ("L2", f"Create the Nginx site {site} on Rocky", f"sudo nano /etc/nginx/conf.d/{n}.conf && sudo nginx -t && sudo systemctl reload nginx", "Rocky uses conf.d instead of sites-enabled.", "rhel"),
            ("L3", f"Get a Let's Encrypt certificate for {site}", f"sudo certbot --nginx -d {site}", "Certbot edits the server block and installs renewal.", "any"),
            ("L3", f"Reverse proxy {site} to a backend on port 8080", f"location / {{ proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; }}", "Inside the server block of the site.", "any"),
            ("L3", f"Redirect HTTP to HTTPS for {site}", f"server {{ listen 80; server_name {site}; return 301 https://$host$request_uri; }}", "Separate server block for port 80.", "any"),
            ("L2", f"Test that {site} answers locally", f"curl -sI -H 'Host: {site}' http://127.0.0.1/", "Tests the virtual host without DNS.", "any"),
            ("L3", f"Show only 5xx errors for {site} in the access log", f"awk '$9 ~ /^5/' /var/log/nginx/{n}.access.log | tail -20", "Needs a per-site access_log line.", "any"),
            ("L3", f"Protect {site} with basic authentication", f"sudo htpasswd -c /etc/nginx/.htpasswd-{n} admin  # then auth_basic and auth_basic_user_file in the location", "Package apache2-utils or httpd-tools.", "any"),
            ("L4", f"Rate-limit requests to {site}", f"limit_req_zone $binary_remote_addr zone={n}:10m rate=10r/s;  # http block; then limit_req zone={n} burst=20; in location", "Stops brute force and simple floods.", "any"),
            ("L3", f"Load-balance {site} across two backends", f"upstream {n}_back {{ server 192.168.56.11:8080; server 192.168.56.12:8080; }}  # proxy_pass http://{n}_back;", "Round robin by default.", "any"),
        ]
        for lvl, t, c, e, d in rows:
            add(lvl, "Web servers", t, c, e, ["nginx", "web", n], d)
    rows = [
        ("L2", "Test the Nginx configuration", "sudo nginx -t"),
        ("L2", "Show the full effective Nginx configuration", "sudo nginx -T | less"),
        ("L2", "Test the Apache configuration (Ubuntu)", "sudo apache2ctl configtest"),
        ("L2", "Test the Apache configuration (Rocky)", "sudo apachectl configtest"),
        ("L2", "List enabled Apache modules (Ubuntu)", "apache2ctl -M"),
        ("L3", "Check HAProxy config syntax", "sudo haproxy -c -f /etc/haproxy/haproxy.cfg"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Web servers", t, c, "Validate before reloading.", ["web"])


def gen_db():
    dbs = ["appdb", "shop", "wiki", "crm", "analytics", "zabbix"]
    for db in dbs:
        u = db + "_user"
        rows = [
            ("L2", f"PostgreSQL: create database {db} owned by {u}", f"sudo -u postgres createuser -P {u} && sudo -u postgres createdb -O {u} {db}", "-P prompts for the password."),
            ("L2", f"PostgreSQL: back up database {db}", f"sudo -u postgres pg_dump -Fc {db} > /srv/backups/{db}-$(date +%F).dump", "-Fc custom format allows selective restore."),
            ("L3", f"PostgreSQL: restore database {db} from a dump", f"sudo -u postgres pg_restore -d {db} --clean /srv/backups/{db}.dump", "--clean drops objects first; test on a copy."),
            ("L2", f"PostgreSQL: show size of database {db}", f"sudo -u postgres psql -c \"SELECT pg_size_pretty(pg_database_size('{db}'));\"", "Find what fills the disk."),
            ("L3", f"PostgreSQL: show active connections to {db}", f"sudo -u postgres psql -c \"SELECT pid, usename, state, query_start FROM pg_stat_activity WHERE datname='{db}';\"", "Spot long-running queries."),
            ("L2", f"MariaDB: create database {db} and user {u}", f"sudo mysql -e \"CREATE DATABASE {db}; CREATE USER '{u}'@'localhost' IDENTIFIED BY 'ChangeMe!'; GRANT ALL ON {db}.* TO '{u}'@'localhost';\"", "Change the password immediately."),
            ("L2", f"MariaDB: back up database {db}", f"sudo mysqldump --single-transaction {db} | gzip > /srv/backups/{db}-$(date +%F).sql.gz", "--single-transaction avoids locking InnoDB tables."),
            ("L3", f"MariaDB: restore database {db}", f"gunzip -c /srv/backups/{db}.sql.gz | sudo mysql {db}", "Restore into an empty database."),
            ("L2", f"MariaDB: show table sizes in {db}", f"sudo mysql -e \"SELECT table_name, ROUND((data_length+index_length)/1024/1024,1) MB FROM information_schema.tables WHERE table_schema='{db}' ORDER BY MB DESC;\"", "Biggest tables first."),
            ("L3", f"Cron: nightly PostgreSQL dump of {db} at 01:00", f"0 1 * * * postgres pg_dump -Fc {db} > /srv/backups/{db}-$(date +\\%F).dump", "In /etc/cron.d/ with user field."),
        ]
        for lvl, t, c, e in rows:
            add(lvl, "Databases", t, c, e, ["database", db, "postgresql" if "PostgreSQL" in t else "mariadb"])
    rows = [
        ("L2", "PostgreSQL: list databases", "sudo -u postgres psql -l"),
        ("L2", "PostgreSQL: open the console", "sudo -u postgres psql"),
        ("L3", "PostgreSQL: reload config without restart", "sudo -u postgres psql -c 'SELECT pg_reload_conf();'"),
        ("L3", "PostgreSQL: find the config and data directory", "sudo -u postgres psql -c 'SHOW config_file;' -c 'SHOW data_directory;'"),
        ("L2", "MariaDB: secure a fresh installation", "sudo mysql_secure_installation"),
        ("L2", "MariaDB: list databases", "sudo mysql -e 'SHOW DATABASES;'"),
        ("L3", "MariaDB: show running queries", "sudo mysql -e 'SHOW FULL PROCESSLIST;'"),
        ("L2", "Redis: check it answers", "redis-cli ping"),
        ("L3", "Redis: show memory usage", "redis-cli info memory | grep used_memory_human"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Databases", t, c, "Database administration basics for Linux admins.", ["database"])


def gen_fileservers():
    shares = ["finance", "hr", "it", "projects", "public", "scans"]
    for sh in shares:
        rows = [
            ("L2", f"Create a Samba share '{sh}' for group {sh}", f"sudo mkdir -p /srv/samba/{sh} && sudo chgrp {sh} /srv/samba/{sh} && sudo chmod 2770 /srv/samba/{sh}  # [{sh}] path=/srv/samba/{sh} valid users=@{sh} read only=no", "Add the section to /etc/samba/smb.conf, then testparm."),
            ("L2", f"Test access to Samba share '{sh}'", f"smbclient //localhost/{sh} -U alice -c 'ls'", "Lists files if permissions are correct."),
            ("L2", f"Mount Samba share '{sh}' on a Linux client", f"sudo mount -t cifs //192.168.56.20/{sh} /mnt/{sh} -o username=alice,uid=$(id -u),gid=$(id -g)", "Needs cifs-utils; use a credentials file for fstab."),
            ("L2", f"Export /srv/nfs/{sh} over NFS to the lab network", f"echo '/srv/nfs/{sh} 192.168.56.0/24(rw,sync,root_squash)' | sudo tee -a /etc/exports && sudo exportfs -ra", "root_squash maps client root to nobody."),
            ("L2", f"Mount NFS export {sh} on a client", f"sudo mount -t nfs 192.168.56.20:/srv/nfs/{sh} /mnt/{sh}", "Add _netdev,nofail in fstab for boot safety."),
            ("L3", f"Mount NFS export {sh} on demand with autofs", f"echo '{sh} -rw,soft 192.168.56.20:/srv/nfs/{sh}' | sudo tee -a /etc/auto.nfs", "Mounted at first access, unmounted when idle."),
        ]
        for lvl, t, c, e in rows:
            add(lvl, "File servers", t, c, e, ["samba" if "Samba" in t else "nfs", sh])
    rows = [
        ("L2", "Check Samba configuration syntax", "testparm -s"),
        ("L2", "Add a Samba password for an existing user", "sudo smbpasswd -a alice"),
        ("L2", "Show connected Samba clients and open files", "sudo smbstatus"),
        ("L2", "Show NFS exports of a server", "showmount -e 192.168.56.20"),
        ("L3", "Show NFS client statistics", "nfsstat -c"),
    ]
    for lvl, t, c in rows:
        add(lvl, "File servers", t, c, "File server operations.", ["fileserver"])


def gen_selinux():
    booleans = [("httpd_can_network_connect", "let web servers connect to backends"), ("httpd_can_network_connect_db", "let web servers connect to databases"),
                ("httpd_enable_homedirs", "serve user home directories"), ("samba_enable_home_dirs", "share home directories over Samba"),
                ("samba_export_all_rw", "let Samba share any directory read-write"), ("nfs_export_all_rw", "let NFS export any directory read-write"),
                ("use_nfs_home_dirs", "allow NFS-mounted home directories"), ("httpd_use_nfs", "let web servers read NFS content"),
                ("ftpd_full_access", "give FTP full filesystem access"), ("container_manage_cgroup", "let containers manage cgroups")]
    for b, why in booleans:
        add("L4", "SELinux", f"Check the SELinux boolean {b}", f"getsebool {b}", f"Controls whether to {why}.", ["selinux", b], "rhel")
        add("L4", "SELinux", f"Permanently enable {b} ({why})", f"sudo setsebool -P {b} on", "-P survives reboot.", ["selinux", b], "rhel")
        add("L4", "SELinux", f"Permanently disable {b}", f"sudo setsebool -P {b} off", "Turn off what you do not need.", ["selinux", b], "rhel")
    ports = [(8081, "http_port_t"), (8443, "http_port_t"), (2222, "ssh_port_t"), (5433, "postgresql_port_t"), (3307, "mysqld_port_t"), (10051, "zabbix_port_t")]
    for port, typ in ports:
        add("L4", "SELinux", f"Allow a service on non-standard port {port} ({typ})", f"sudo semanage port -a -t {typ} -p tcp {port}", "Otherwise SELinux blocks the bind.", ["selinux", "port"], "rhel")
    paths = [("/srv/web", "httpd_sys_content_t"), ("/srv/web/uploads", "httpd_sys_rw_content_t"), ("/srv/samba", "samba_share_t"), ("/srv/pgdata", "postgresql_db_t")]
    for path, typ in paths:
        add("L4", "SELinux", f"Label {path} as {typ} permanently", f"sudo semanage fcontext -a -t {typ} \"{path}(/.*)?\" && sudo restorecon -Rv {path}", "restorecon applies the rule.", ["selinux", "context"], "rhel")


def gen_logrotate():
    apps = ["nginx", "myapp", "backup", "watchdog", "disk_alert", "api", "worker"]
    opts = [("daily", "rotate 14", "keep two weeks of daily logs"), ("weekly", "rotate 8", "keep two months of weekly logs"),
            ("size 100M", "rotate 5", "rotate when the log reaches 100 MB"), ("daily", "rotate 30\\n    dateext", "daily logs with the date in the name")]
    for a in apps:
        for when, keep, why in opts:
            body = f"/var/log/{a}/*.log {{\\n    {when}\\n    {keep}\\n    compress\\n    delaycompress\\n    missingok\\n    notifempty\\n}}"
            add("L2", "Logs: logrotate", f"logrotate config for {a} to {why}", f"printf '{body}\\n' | sudo tee /etc/logrotate.d/{a}", "Check with logrotate -d.", ["logrotate", a])
        add("L2", "Logs: logrotate", f"Dry-run logrotate for {a}", f"sudo logrotate -d /etc/logrotate.d/{a}", "Shows what would happen.", ["logrotate", a])
        add("L2", "Logs: logrotate", f"Force log rotation for {a} now", f"sudo logrotate -f /etc/logrotate.d/{a}", "Useful when a log grew too big.", ["logrotate", a])


def gen_git():
    rows = [
        ("L1", "Clone the lab repository", "git clone https://github.com/brosjsy/linux-administration-lab.git"),
        ("L1", "See what changed before committing", "git status && git diff"),
        ("L1", "Commit all changes with a message", "git add -A && git commit -m \"Describe the change\""),
        ("L1", "Push commits to GitHub", "git push"),
        ("L1", "Get the latest changes", "git pull"),
        ("L2", "Show the last 10 commits in one line each", "git log --oneline -10"),
        ("L2", "Create and switch to a new branch", "git switch -c feature/hardening"),
        ("L2", "Undo changes to one file", "git restore path/to/file"),
        ("L2", "See who changed each line of a file", "git blame scripts/backup.sh"),
        ("L3", "Track /etc changes with etckeeper", "sudo apt install etckeeper && sudo etckeeper init && sudo etckeeper commit 'baseline'"),
        ("L3", "Show what changed in /etc since the last commit", "sudo etckeeper vcs diff"),
        ("L2", "Store a config file in git with a backup copy", "cp /etc/nginx/nginx.conf configs/ && git add configs && git commit -m 'nginx config'"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Git for admins", t, c, "Version control keeps a history of configs and scripts.", ["git"])


def gen_tls_files():
    names = ["lab", "web1", "api", "wiki", "mail", "vpn"]
    for n in names:
        rows = [
            ("L3", f"Create a 2048-bit private key and CSR for {n}.lab.local", f"openssl req -new -newkey rsa:2048 -nodes -keyout {n}.key -out {n}.csr -subj \"/CN={n}.lab.local\"", "Send the CSR to the CA, keep the key private."),
            ("L3", f"Create a self-signed certificate for {n}.lab.local valid 365 days", f"openssl req -x509 -newkey rsa:2048 -nodes -days 365 -keyout {n}.key -out {n}.crt -subj \"/CN={n}.lab.local\"", "Fine for labs, not for public sites."),
            ("L3", f"Show the expiry date of {n}.crt", f"openssl x509 -in {n}.crt -noout -enddate", "notAfter is the expiry."),
            ("L3", f"Check that {n}.key matches {n}.crt", f"diff <(openssl x509 -in {n}.crt -noout -modulus) <(openssl rsa -in {n}.key -noout -modulus) && echo match", "Mismatch is a common cause of web server start errors."),
            ("L3", f"Convert {n}.crt and {n}.key to a PFX bundle", f"openssl pkcs12 -export -in {n}.crt -inkey {n}.key -out {n}.pfx", "For Windows and some appliances."),
            ("L3", f"Show the SAN names in {n}.crt", f"openssl x509 -in {n}.crt -noout -ext subjectAltName", "Browsers check SAN, not CN."),
        ]
        for lvl, t, c, e in rows:
            add(lvl, "TLS certificates", t, c, e, ["openssl", "tls", n])


def gen_monitoring():
    items = [("system.cpu.load[all,avg1]", "1-minute CPU load"), ("vm.memory.size[available]", "available memory"),
             ("vfs.fs.size[/,pused]", "root disk used percent"), ("net.if.in[eth0]", "incoming traffic on eth0"),
             ("proc.num[nginx]", "number of nginx processes"), ("net.tcp.listen[443]", "whether port 443 listens"),
             ("system.uptime", "uptime"), ("vfs.file.exists[/var/run/reboot-required]", "reboot required flag")]
    for host in ["192.168.56.10", "192.168.56.20"]:
        for key, d in items:
            add("L3", "Monitoring", f"Zabbix: read {d} from agent on {host}", f"zabbix_get -s {host} -k '{key}'", "Run on the Zabbix server to test an item.", ["zabbix", "monitoring"])
    promq = [("CPU busy percent per host", "100 - avg by (instance)(rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100"),
             ("Available memory percent", "node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100"),
             ("Root disk used percent", "100 - node_filesystem_avail_bytes{mountpoint=\"/\"} / node_filesystem_size_bytes{mountpoint=\"/\"} * 100"),
             ("Disk will be full within 24 hours", "predict_linear(node_filesystem_avail_bytes{fstype!=\"tmpfs\"}[6h], 86400) < 0"),
             ("Network receive rate", "rate(node_network_receive_bytes_total{device!=\"lo\"}[5m])"),
             ("Hosts that are down", "up == 0"), ("Systemd units in failed state", "node_systemd_unit_state{state=\"failed\"} == 1"),
             ("Load per CPU core", "node_load5 / count without (cpu, mode) (node_cpu_seconds_total{mode=\"idle\"})")]
    for d, q in promq:
        add("L4", "Monitoring", f"PromQL: {d}", q, "Paste in Prometheus or Grafana; use in alert rules with a for: duration.", ["prometheus", "promql"])
    rows = [("L2", "Check node_exporter answers", "curl -s localhost:9100/metrics | head"),
            ("L3", "Test a Zabbix agent item locally", "zabbix_agent2 -t system.cpu.load[all,avg1]"),
            ("L3", "Validate Prometheus configuration", "promtool check config /etc/prometheus/prometheus.yml"),
            ("L3", "Validate Prometheus alert rules", "promtool check rules /etc/prometheus/rules/*.yml"),
            ("L2", "Show system activity history for today (sysstat)", "sar -u -r -d")]
    for lvl, t, c in rows:
        add(lvl, "Monitoring", t, c, "Monitoring operations.", ["monitoring"])


def gen_kvm():
    vms = ["web1", "web2", "db1", "backup1", "test-ubuntu", "test-rocky"]
    for vm in vms:
        rows = [("L3", f"Start the KVM virtual machine {vm}", f"virsh start {vm}"), ("L3", f"Gracefully shut down VM {vm}", f"virsh shutdown {vm}"),
                ("L3", f"Force power off VM {vm}", f"virsh destroy {vm}"), ("L3", f"Start VM {vm} automatically at host boot", f"virsh autostart {vm}"),
                ("L3", f"Show CPU, memory and state of VM {vm}", f"virsh dominfo {vm}"), ("L3", f"Open the text console of VM {vm}", f"virsh console {vm}"),
                ("L4", f"Take a snapshot of VM {vm} before patching", f"virsh snapshot-create-as {vm} pre-patch-$(date +%F)"),
                ("L4", f"Revert VM {vm} to its last snapshot", f"virsh snapshot-revert {vm} --current"),
                ("L3", f"Show disks of VM {vm}", f"virsh domblklist {vm}"), ("L3", f"Show IP addresses of VM {vm}", f"virsh domifaddr {vm}")]
        for lvl, t, c in rows:
            add(lvl, "Virtualisation (KVM)", t, c, "libvirt management; virt-manager is the GUI.", ["kvm", "virsh", vm])
    for vm in ["ubuntu-srv", "rocky-srv"]:
        for a, d in [("up", "Start"), ("halt", "Stop"), ("ssh", "Connect to"), ("reload --provision", "Re-run provisioning on"), ("destroy -f", "Delete")]:
            add("L2", "Virtualisation (KVM)", f"Vagrant: {d} lab VM {vm}", f"vagrant {a} {vm}", "Run from the lab/ directory.", ["vagrant", vm])


def gen_boot_perf():
    rows = [
        ("L3", "Show the default boot target", "systemctl get-default"),
        ("L3", "Boot into text mode by default", "sudo systemctl set-default multi-user.target"),
        ("L3", "Show what slows down boot", "systemd-analyze blame | head -15"),
        ("L3", "Show the critical boot chain", "systemd-analyze critical-chain"),
        ("L3", "List installed kernels (Rocky)", "sudo grubby --info=ALL | grep -E '^kernel|^index'"),
        ("L3", "Set the current kernel as default (Rocky)", "sudo grubby --set-default /boot/vmlinuz-$(uname -r)"),
        ("L3", "Regenerate GRUB menu (Ubuntu)", "sudo update-grub"),
        ("L4", "Rescue: remount root read-write in emergency mode", "mount -o remount,rw /"),
        ("L4", "Rescue: reset root password on Rocky (after rd.break)", "mount -o remount,rw /sysroot && chroot /sysroot && passwd && touch /.autorelabel"),
        ("L4", "Check and repair an unmounted ext4 filesystem", "sudo fsck -f /dev/sdb1"),
        ("L4", "Repair an unmounted XFS filesystem", "sudo xfs_repair /dev/sdb1"),
        ("L3", "Show kernel version and build", "uname -a"),
        ("L3", "Show loaded kernel modules", "lsmod | head -20"),
        ("L3", "Load a kernel module now", "sudo modprobe br_netfilter"),
        ("L4", "Show the open-files limit of the current shell", "ulimit -n"),
        ("L4", "Raise the open-files limit for user appuser", "printf 'appuser soft nofile 65535\\nappuser hard nofile 65535\\n' | sudo tee /etc/security/limits.d/appuser.conf"),
        ("L4", "Show the active tuned profile (Rocky)", "tuned-adm active"),
        ("L4", "Switch to the throughput-performance tuned profile", "sudo tuned-adm profile throughput-performance"),
        ("L4", "Show live cgroup resource usage", "systemd-cgtop"),
        ("L4", "Show IO usage per process", "sudo iotop -oPa"),
        ("L4", "Show memory details including slab cache", "cat /proc/meminfo | head -25; sudo slabtop -o | head -15"),
        ("L4", "Drop page cache for a benchmark (test only)", "sync; echo 3 | sudo tee /proc/sys/vm/drop_caches"),
        ("L4", "Show NUMA layout of the server", "lscpu | grep -i numa; numactl --hardware"),
        ("L3", "Show hardware summary", "sudo lshw -short | head -40"),
        ("L3", "Show CPU model and cores", "lscpu | head -20"),
        ("L3", "Show memory modules", "sudo dmidecode -t memory | grep -E 'Size|Speed' | head"),
        ("L3", "Show PCI devices (network and disk controllers)", "lspci | grep -Ei 'net|sata|nvme|raid'"),
        ("L3", "Show software RAID status", "cat /proc/mdstat"),
    ]
    for lvl, t, c in rows:
        add(lvl, "Boot, kernel and performance", t, c, "Advanced system administration.", ["boot", "kernel", "performance"])


def main():
    gen_services(); gen_packages(); gen_dns(); gen_ports(); gen_find(); gen_grep(); gen_journal()
    gen_permissions(); gen_users(); gen_cron(); gen_archives(); gen_storage(); gen_processes(); gen_ssh()
    gen_sysctl(); gen_hardening(); gen_ansible(); gen_docker(); gen_text(); gen_bash(); gen_network_config()
    gen_troubleshooting(); gen_web(); gen_db(); gen_fileservers(); gen_selinux(); gen_logrotate(); gen_git(); gen_tls_files(); gen_monitoring(); gen_kvm(); gen_boot_perf()

    order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4}
    tasks.sort(key=lambda t: (t["category"], order[t["level"]], t["task"]))
    for i, t in enumerate(tasks, 1):
        t["id"] = f"T{i:04d}"

    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=1)
    fields = ["id", "level", "category", "distro", "task", "command", "explanation", "tags"]
    with open(f"{OUT}/tasks.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(fields)
        for t in tasks:
            w.writerow([t["id"], t["level"], t["category"], t["distro"], t["task"], t["command"], t["explanation"], " ".join(t["tags"])])
    with open(f"{OUT}/tasks.tsv", "w", encoding="utf-8") as f:
        for t in tasks:
            row = [t["id"], t["level"], t["category"], t["distro"], t["task"], t["command"], t["explanation"], " ".join(t["tags"])]
            f.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in row) + "\n")

    cats = OrderedDict()
    for t in tasks:
        cats.setdefault(t["category"], []).append(t)
    os.makedirs(f"{OUT}/by-category", exist_ok=True)
    index_rows = []
    for cat, items in cats.items():
        slug = "".join(c if c.isalnum() else "-" for c in cat.lower()).strip("-")
        while "--" in slug:
            slug = slug.replace("--", "-")
        with open(f"{OUT}/by-category/{slug}.md", "w", encoding="utf-8") as f:
            f.write(f"# {cat} ({len(items)} tasks)\n\n[Back to index](../README.md)\n\n")
            f.write("| ID | Level | Distro | Task | Command | Note |\n|----|-------|--------|------|---------|------|\n")
            for t in items:
                cmd = t["command"].replace("|", "\\|")
                f.write(f"| {t['id']} | {t['level']} | {t['distro']} | {t['task'].replace('|', '/')} | `{cmd}` | {t['explanation'].replace('|', '/')} |\n")
        index_rows.append((cat, slug, len(items)))

    levels = OrderedDict((lv, sum(1 for t in tasks if t["level"] == lv)) for lv in ["L1", "L2", "L3", "L4"])
    with open(f"{OUT}/README.md", "w", encoding="utf-8") as f:
        f.write(f"# Linux task library: {len(tasks)} tasks with example commands\n\n")
        f.write("Searchable in four ways:\n\n")
        f.write("1. **Web page:** open [`search.html`](search.html) in a browser (works offline) or via GitHub Pages. Type any word, filter by level, category and distro, copy commands with one click.\n")
        f.write("2. **Terminal:** `scripts/task_search.sh nginx`, `scripts/task_search.sh -l L3 -c cron backup`\n")
        f.write("3. **GitHub search / Ctrl+F** in the category pages below.\n")
        f.write("4. **Data files:** `tasks.json`, `tasks.csv` (Excel), `tasks.tsv` (grep/awk).\n\n")
        f.write("## By level\n\n| Level | Meaning | Tasks |\n|-------|---------|-------|\n")
        meaning = {"L1": "Beginner", "L2": "Junior admin / on-duty engineer", "L3": "Admin", "L4": "Professional"}
        for lv, n in levels.items():
            f.write(f"| {lv} | {meaning[lv]} | {n} |\n")
        f.write("\n## By category\n\n| Category | Tasks |\n|----------|-------|\n")
        for cat, slug, n in index_rows:
            f.write(f"| [{cat}](by-category/{slug}.md) | {n} |\n")
        f.write("\n> Commands use lab names (192.168.56.x, /srv/share, users ivan, olga...). Read the command before running it, and try risky ones on the lab VMs first.\n")
        f.write("\nRegenerate everything with `python3 tools/generate_tasks.py`.\n")
        f.write("\n## Publish the search page online\nGitHub repo Settings, Pages, Source: Deploy from branch `main`, folder `/ (root)`. "
                "The page is then at `https://brosjsy.github.io/linux-administration-lab/tasks/search.html`.\n")

    write_html(tasks, sorted(cats.keys()))
    print(f"{len(tasks)} tasks in {len(cats)} categories; levels {dict(levels)}")


def write_html(items, cats):
    data = json.dumps([[t["id"], t["level"], t["category"], t["distro"], t["task"], t["command"], t["explanation"], " ".join(t["tags"])] for t in items],
                      ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    opts = "".join(f'<option value="{html.escape(c)}">{html.escape(c)}</option>' for c in cats)
    page = HTML.replace("__COUNT__", str(len(items))).replace("__CATS__", opts).replace("__DATA__", data)
    with open(f"{OUT}/search.html", "w", encoding="utf-8") as f:
        f.write(page)


HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Linux Task Search</title>
<style>
:root{--bg:#f7f8fa;--card:#fff;--text:#1d2330;--muted:#5f6572;--line:#e3e6eb;--accent:#1f6feb;--code:#0f172a;--codetext:#e2e8f0;--chip:#eef2f7}
@media (prefers-color-scheme:dark){:root{--bg:#0f1218;--card:#171b23;--text:#e6e8ec;--muted:#9aa3b2;--line:#2a303b;--accent:#58a6ff;--code:#0b0e14;--codetext:#d6dde8;--chip:#222833}}
*{box-sizing:border-box}body{margin:0;font:15px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--text)}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:14px 16px;z-index:2}
h1{font-size:19px;margin:0 0 10px}.bar{display:flex;flex-wrap:wrap;gap:8px}
input,select{font:inherit;padding:9px 11px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--text)}
input{flex:1 1 260px}main{max-width:1000px;margin:0 auto;padding:12px 16px 40px}
.meta{color:var(--muted);font-size:13px;margin:6px 0 10px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:10px 0}
.top{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:12px;color:var(--muted)}
.chip{background:var(--chip);border-radius:20px;padding:2px 8px}.task{font-weight:600;margin:6px 0}
.cmd{display:flex;gap:8px;align-items:flex-start}pre{flex:1;margin:0;background:var(--code);color:var(--codetext);padding:9px 11px;border-radius:8px;overflow-x:auto;white-space:pre-wrap;word-break:break-word;font:13px/1.4 ui-monospace,Consolas,monospace}
button{font:inherit;font-size:12px;border:1px solid var(--line);background:var(--card);color:var(--text);border-radius:7px;padding:7px 10px;cursor:pointer}
.ex{color:var(--muted);font-size:13px;margin-top:6px}#more{display:block;margin:14px auto}
mark{background:#ffe58a;color:#000;border-radius:3px}
</style>
</head>
<body>
<header>
<h1>Linux Task Search: __COUNT__ tasks</h1>
<div class="bar">
<input id="q" type="search" placeholder="Search: nginx restart, cron backup, port 443, lvextend, ssh key..." autofocus>
<select id="lv"><option value="">All levels</option><option>L1</option><option>L2</option><option>L3</option><option>L4</option></select>
<select id="cat"><option value="">All categories</option>__CATS__</select>
<select id="ds"><option value="">Any distro</option><option value="debian">Ubuntu/Debian</option><option value="rhel">Rocky/RHEL</option></select>
</div>
</header>
<main>
<div class="meta" id="meta"></div>
<div id="list"></div>
<button id="more">Show more</button>
</main>
<script>
const D=__DATA__;
const q=document.getElementById('q'),lv=document.getElementById('lv'),cat=document.getElementById('cat'),ds=document.getElementById('ds');
const list=document.getElementById('list'),meta=document.getElementById('meta'),more=document.getElementById('more');
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let res=[],shown=0;const PAGE=60;
function hl(t,words){let s=esc(t);for(const w of words){if(w.length<2)continue;s=s.replace(new RegExp('('+w.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&')+')','ig'),'<mark>$1</mark>')}return s}
function run(){
  const words=q.value.toLowerCase().split(/\\s+/).filter(Boolean);
  res=D.filter(r=>{if(lv.value&&r[1]!==lv.value)return false;if(cat.value&&r[2]!==cat.value)return false;
    if(ds.value&&r[3]!==ds.value&&r[3]!=='any')return false;
    const hay=(r[0]+' '+r[2]+' '+r[4]+' '+r[5]+' '+r[6]+' '+r[7]).toLowerCase();return words.every(w=>hay.includes(w))});
  shown=0;list.innerHTML='';render(words);
  meta.textContent=res.length+' result'+(res.length===1?'':'s');
  try{localStorage.setItem('lts',JSON.stringify([q.value,lv.value,cat.value,ds.value]))}catch(e){}
}
function render(words){
  words=words||q.value.toLowerCase().split(/\\s+/).filter(Boolean);
  const frag=document.createDocumentFragment();
  for(const r of res.slice(shown,shown+PAGE)){
    const d=document.createElement('div');d.className='card';
    d.innerHTML='<div class="top"><span class="chip">'+r[0]+'</span><span class="chip">'+r[1]+'</span><span class="chip">'+esc(r[2])+'</span>'+(r[3]!=='any'?'<span class="chip">'+r[3]+'</span>':'')+'</div>'+
      '<div class="task">'+hl(r[4],words)+'</div><div class="cmd"><pre>'+hl(r[5],words)+'</pre><button>Copy</button></div><div class="ex">'+esc(r[6])+'</div>';
    d.querySelector('button').onclick=e=>{const b=e.target;const done=()=>{b.textContent='Copied';setTimeout(()=>b.textContent='Copy',1200)};
      if(navigator.clipboard){navigator.clipboard.writeText(r[5]).then(done,()=>{})}};
    frag.appendChild(d)}
  list.appendChild(frag);shown+=PAGE;more.style.display=shown<res.length?'block':'none';
}
let tm;[q,lv,cat,ds].forEach(el=>el.addEventListener('input',()=>{clearTimeout(tm);tm=setTimeout(run,120)}));
more.onclick=()=>render();
try{const s=JSON.parse(localStorage.getItem('lts')||'null');if(s){[q.value,lv.value,cat.value,ds.value]=s}}catch(e){}
run();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
