# Ansible (170 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T0001 | L3 | any | Ansible: Add a disk alert cron job on group 'all' | `ansible all -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0002 | L3 | any | Ansible: Add a disk alert cron job on group 'backup' | `ansible backup -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0003 | L3 | any | Ansible: Add a disk alert cron job on group 'db' | `ansible db -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0004 | L3 | any | Ansible: Add a disk alert cron job on group 'dev' | `ansible dev -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0005 | L3 | any | Ansible: Add a disk alert cron job on group 'infra' | `ansible infra -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0006 | L3 | any | Ansible: Add a disk alert cron job on group 'monitoring' | `ansible monitoring -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0007 | L3 | any | Ansible: Add a disk alert cron job on group 'prod' | `ansible prod -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0008 | L3 | any | Ansible: Add a disk alert cron job on group 'rocky' | `ansible rocky -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0009 | L3 | any | Ansible: Add a disk alert cron job on group 'ubuntu' | `ansible ubuntu -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0010 | L3 | any | Ansible: Add a disk alert cron job on group 'web' | `ansible web -m cron -a "name=disk minute=*/15 job='/opt/lab/scripts/disk_alert.sh 85'" -b` | Ad-hoc command from the ansible/ directory. |
| T0011 | L3 | any | Ansible: Check root disk usage on group 'all' | `ansible all -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0012 | L3 | any | Ansible: Check root disk usage on group 'backup' | `ansible backup -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0013 | L3 | any | Ansible: Check root disk usage on group 'db' | `ansible db -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0014 | L3 | any | Ansible: Check root disk usage on group 'dev' | `ansible dev -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0015 | L3 | any | Ansible: Check root disk usage on group 'infra' | `ansible infra -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0016 | L3 | any | Ansible: Check root disk usage on group 'monitoring' | `ansible monitoring -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0017 | L3 | any | Ansible: Check root disk usage on group 'prod' | `ansible prod -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0018 | L3 | any | Ansible: Check root disk usage on group 'rocky' | `ansible rocky -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0019 | L3 | any | Ansible: Check root disk usage on group 'ubuntu' | `ansible ubuntu -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0020 | L3 | any | Ansible: Check root disk usage on group 'web' | `ansible web -m shell -a "df -h / \| tail -1"` | Ad-hoc command from the ansible/ directory. |
| T0021 | L3 | any | Ansible: Collect syslog from every server in group 'all' | `ansible all -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0022 | L3 | any | Ansible: Collect syslog from every server in group 'backup' | `ansible backup -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0023 | L3 | any | Ansible: Collect syslog from every server in group 'db' | `ansible db -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0024 | L3 | any | Ansible: Collect syslog from every server in group 'dev' | `ansible dev -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0025 | L3 | any | Ansible: Collect syslog from every server in group 'infra' | `ansible infra -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0026 | L3 | any | Ansible: Collect syslog from every server in group 'monitoring' | `ansible monitoring -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0027 | L3 | any | Ansible: Collect syslog from every server in group 'prod' | `ansible prod -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0028 | L3 | any | Ansible: Collect syslog from every server in group 'rocky' | `ansible rocky -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0029 | L3 | any | Ansible: Collect syslog from every server in group 'ubuntu' | `ansible ubuntu -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0030 | L3 | any | Ansible: Collect syslog from every server in group 'web' | `ansible web -m fetch -a "src=/var/log/syslog dest=./logs/ flat=false" -b` | Ad-hoc command from the ansible/ directory. |
| T0031 | L3 | any | Ansible: Copy a login message to group 'all' | `ansible all -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0032 | L3 | any | Ansible: Copy a login message to group 'backup' | `ansible backup -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0033 | L3 | any | Ansible: Copy a login message to group 'db' | `ansible db -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0034 | L3 | any | Ansible: Copy a login message to group 'dev' | `ansible dev -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0035 | L3 | any | Ansible: Copy a login message to group 'infra' | `ansible infra -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0036 | L3 | any | Ansible: Copy a login message to group 'monitoring' | `ansible monitoring -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0037 | L3 | any | Ansible: Copy a login message to group 'prod' | `ansible prod -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0038 | L3 | any | Ansible: Copy a login message to group 'rocky' | `ansible rocky -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0039 | L3 | any | Ansible: Copy a login message to group 'ubuntu' | `ansible ubuntu -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0040 | L3 | any | Ansible: Copy a login message to group 'web' | `ansible web -m copy -a "src=./motd dest=/etc/motd mode=0644" -b` | Ad-hoc command from the ansible/ directory. |
| T0041 | L3 | any | Ansible: Create /opt/lab directory on group 'all' | `ansible all -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0042 | L3 | any | Ansible: Create /opt/lab directory on group 'backup' | `ansible backup -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0043 | L3 | any | Ansible: Create /opt/lab directory on group 'db' | `ansible db -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0044 | L3 | any | Ansible: Create /opt/lab directory on group 'dev' | `ansible dev -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0045 | L3 | any | Ansible: Create /opt/lab directory on group 'infra' | `ansible infra -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0046 | L3 | any | Ansible: Create /opt/lab directory on group 'monitoring' | `ansible monitoring -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0047 | L3 | any | Ansible: Create /opt/lab directory on group 'prod' | `ansible prod -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0048 | L3 | any | Ansible: Create /opt/lab directory on group 'rocky' | `ansible rocky -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0049 | L3 | any | Ansible: Create /opt/lab directory on group 'ubuntu' | `ansible ubuntu -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0050 | L3 | any | Ansible: Create /opt/lab directory on group 'web' | `ansible web -m file -a "path=/opt/lab state=directory mode=0755" -b` | Ad-hoc command from the ansible/ directory. |
| T0051 | L3 | any | Ansible: Create user ivan in group support on group 'all' | `ansible all -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0052 | L3 | any | Ansible: Create user ivan in group support on group 'backup' | `ansible backup -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0053 | L3 | any | Ansible: Create user ivan in group support on group 'db' | `ansible db -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0054 | L3 | any | Ansible: Create user ivan in group support on group 'dev' | `ansible dev -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0055 | L3 | any | Ansible: Create user ivan in group support on group 'infra' | `ansible infra -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0056 | L3 | any | Ansible: Create user ivan in group support on group 'monitoring' | `ansible monitoring -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0057 | L3 | any | Ansible: Create user ivan in group support on group 'prod' | `ansible prod -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0058 | L3 | any | Ansible: Create user ivan in group support on group 'rocky' | `ansible rocky -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0059 | L3 | any | Ansible: Create user ivan in group support on group 'ubuntu' | `ansible ubuntu -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0060 | L3 | any | Ansible: Create user ivan in group support on group 'web' | `ansible web -m user -a "name=ivan groups=support append=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0061 | L3 | any | Ansible: Install htop on Rocky servers in group 'all' | `ansible all -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0062 | L3 | any | Ansible: Install htop on Rocky servers in group 'backup' | `ansible backup -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0063 | L3 | any | Ansible: Install htop on Rocky servers in group 'db' | `ansible db -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0064 | L3 | any | Ansible: Install htop on Rocky servers in group 'dev' | `ansible dev -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0065 | L3 | any | Ansible: Install htop on Rocky servers in group 'infra' | `ansible infra -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0066 | L3 | any | Ansible: Install htop on Rocky servers in group 'monitoring' | `ansible monitoring -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0067 | L3 | any | Ansible: Install htop on Rocky servers in group 'prod' | `ansible prod -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0068 | L3 | any | Ansible: Install htop on Rocky servers in group 'rocky' | `ansible rocky -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0069 | L3 | any | Ansible: Install htop on Rocky servers in group 'ubuntu' | `ansible ubuntu -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0070 | L3 | any | Ansible: Install htop on Rocky servers in group 'web' | `ansible web -m dnf -a "name=htop state=present" -b` | Ad-hoc command from the ansible/ directory. |
| T0071 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'all' | `ansible all -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0072 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'backup' | `ansible backup -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0073 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'db' | `ansible db -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0074 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'dev' | `ansible dev -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0075 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'infra' | `ansible infra -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0076 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'monitoring' | `ansible monitoring -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0077 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'prod' | `ansible prod -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0078 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'rocky' | `ansible rocky -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0079 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'ubuntu' | `ansible ubuntu -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0080 | L3 | any | Ansible: Install htop on Ubuntu servers in group 'web' | `ansible web -m apt -a "name=htop state=present update_cache=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0081 | L3 | any | Ansible: Restart nginx on group 'all' | `ansible all -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0082 | L3 | any | Ansible: Restart nginx on group 'backup' | `ansible backup -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0083 | L3 | any | Ansible: Restart nginx on group 'db' | `ansible db -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0084 | L3 | any | Ansible: Restart nginx on group 'dev' | `ansible dev -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0085 | L3 | any | Ansible: Restart nginx on group 'infra' | `ansible infra -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0086 | L3 | any | Ansible: Restart nginx on group 'monitoring' | `ansible monitoring -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0087 | L3 | any | Ansible: Restart nginx on group 'prod' | `ansible prod -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0088 | L3 | any | Ansible: Restart nginx on group 'rocky' | `ansible rocky -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0089 | L3 | any | Ansible: Restart nginx on group 'ubuntu' | `ansible ubuntu -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0090 | L3 | any | Ansible: Restart nginx on group 'web' | `ansible web -m service -a "name=nginx state=restarted" -b` | Ad-hoc command from the ansible/ directory. |
| T0091 | L3 | any | Ansible: Show OS distribution facts for group 'all' | `ansible all -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0092 | L3 | any | Ansible: Show OS distribution facts for group 'backup' | `ansible backup -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0093 | L3 | any | Ansible: Show OS distribution facts for group 'db' | `ansible db -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0094 | L3 | any | Ansible: Show OS distribution facts for group 'dev' | `ansible dev -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0095 | L3 | any | Ansible: Show OS distribution facts for group 'infra' | `ansible infra -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0096 | L3 | any | Ansible: Show OS distribution facts for group 'monitoring' | `ansible monitoring -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0097 | L3 | any | Ansible: Show OS distribution facts for group 'prod' | `ansible prod -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0098 | L3 | any | Ansible: Show OS distribution facts for group 'rocky' | `ansible rocky -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0099 | L3 | any | Ansible: Show OS distribution facts for group 'ubuntu' | `ansible ubuntu -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0100 | L3 | any | Ansible: Show OS distribution facts for group 'web' | `ansible web -m setup -a "filter=ansible_distribution*"` | Ad-hoc command from the ansible/ directory. |
| T0101 | L3 | any | Ansible: Show uptime of every server in group 'all' | `ansible all -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0102 | L3 | any | Ansible: Show uptime of every server in group 'backup' | `ansible backup -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0103 | L3 | any | Ansible: Show uptime of every server in group 'db' | `ansible db -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0104 | L3 | any | Ansible: Show uptime of every server in group 'dev' | `ansible dev -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0105 | L3 | any | Ansible: Show uptime of every server in group 'infra' | `ansible infra -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0106 | L3 | any | Ansible: Show uptime of every server in group 'monitoring' | `ansible monitoring -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0107 | L3 | any | Ansible: Show uptime of every server in group 'prod' | `ansible prod -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0108 | L3 | any | Ansible: Show uptime of every server in group 'rocky' | `ansible rocky -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0109 | L3 | any | Ansible: Show uptime of every server in group 'ubuntu' | `ansible ubuntu -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0110 | L3 | any | Ansible: Show uptime of every server in group 'web' | `ansible web -m command -a "uptime"` | Ad-hoc command from the ansible/ directory. |
| T0111 | L3 | any | Ansible: Test connectivity and Python on group 'all' | `ansible all -m ping` | Ad-hoc command from the ansible/ directory. |
| T0112 | L3 | any | Ansible: Test connectivity and Python on group 'backup' | `ansible backup -m ping` | Ad-hoc command from the ansible/ directory. |
| T0113 | L3 | any | Ansible: Test connectivity and Python on group 'db' | `ansible db -m ping` | Ad-hoc command from the ansible/ directory. |
| T0114 | L3 | any | Ansible: Test connectivity and Python on group 'dev' | `ansible dev -m ping` | Ad-hoc command from the ansible/ directory. |
| T0115 | L3 | any | Ansible: Test connectivity and Python on group 'infra' | `ansible infra -m ping` | Ad-hoc command from the ansible/ directory. |
| T0116 | L3 | any | Ansible: Test connectivity and Python on group 'monitoring' | `ansible monitoring -m ping` | Ad-hoc command from the ansible/ directory. |
| T0117 | L3 | any | Ansible: Test connectivity and Python on group 'prod' | `ansible prod -m ping` | Ad-hoc command from the ansible/ directory. |
| T0118 | L3 | any | Ansible: Test connectivity and Python on group 'rocky' | `ansible rocky -m ping` | Ad-hoc command from the ansible/ directory. |
| T0119 | L3 | any | Ansible: Test connectivity and Python on group 'ubuntu' | `ansible ubuntu -m ping` | Ad-hoc command from the ansible/ directory. |
| T0120 | L3 | any | Ansible: Test connectivity and Python on group 'web' | `ansible web -m ping` | Ad-hoc command from the ansible/ directory. |
| T0121 | L3 | any | Apply playbook 01-baseline only to the web group | `ansible-playbook playbooks/01-baseline.yml --limit web` | --limit narrows the target hosts. |
| T0122 | L3 | any | Apply playbook 02-users only to the web group | `ansible-playbook playbooks/02-users.yml --limit web` | --limit narrows the target hosts. |
| T0123 | L3 | any | Apply playbook 03-ssh-hardening only to the web group | `ansible-playbook playbooks/03-ssh-hardening.yml --limit web` | --limit narrows the target hosts. |
| T0124 | L3 | any | Apply playbook 04-firewall only to the web group | `ansible-playbook playbooks/04-firewall.yml --limit web` | --limit narrows the target hosts. |
| T0125 | L3 | any | Apply playbook 05-patching only to the web group | `ansible-playbook playbooks/05-patching.yml --limit web` | --limit narrows the target hosts. |
| T0126 | L3 | any | Apply playbook 06-cron-jobs only to the web group | `ansible-playbook playbooks/06-cron-jobs.yml --limit web` | --limit narrows the target hosts. |
| T0127 | L3 | any | Apply playbook 07-nginx only to the web group | `ansible-playbook playbooks/07-nginx.yml --limit web` | --limit narrows the target hosts. |
| T0128 | L3 | any | Apply playbook 08-health-report only to the web group | `ansible-playbook playbooks/08-health-report.yml --limit web` | --limit narrows the target hosts. |
| T0129 | L3 | any | Check syntax of playbook 01-baseline | `ansible-playbook --syntax-check playbooks/01-baseline.yml` | Run in CI before merging. |
| T0130 | L3 | any | Check syntax of playbook 02-users | `ansible-playbook --syntax-check playbooks/02-users.yml` | Run in CI before merging. |
| T0131 | L3 | any | Check syntax of playbook 03-ssh-hardening | `ansible-playbook --syntax-check playbooks/03-ssh-hardening.yml` | Run in CI before merging. |
| T0132 | L3 | any | Check syntax of playbook 04-firewall | `ansible-playbook --syntax-check playbooks/04-firewall.yml` | Run in CI before merging. |
| T0133 | L3 | any | Check syntax of playbook 05-patching | `ansible-playbook --syntax-check playbooks/05-patching.yml` | Run in CI before merging. |
| T0134 | L3 | any | Check syntax of playbook 06-cron-jobs | `ansible-playbook --syntax-check playbooks/06-cron-jobs.yml` | Run in CI before merging. |
| T0135 | L3 | any | Check syntax of playbook 07-nginx | `ansible-playbook --syntax-check playbooks/07-nginx.yml` | Run in CI before merging. |
| T0136 | L3 | any | Check syntax of playbook 08-health-report | `ansible-playbook --syntax-check playbooks/08-health-report.yml` | Run in CI before merging. |
| T0137 | L3 | any | Dry-run playbook 01-baseline and show the diff | `ansible-playbook playbooks/01-baseline.yml --check --diff` | Nothing changes; review before applying. |
| T0138 | L3 | any | Dry-run playbook 02-users and show the diff | `ansible-playbook playbooks/02-users.yml --check --diff` | Nothing changes; review before applying. |
| T0139 | L3 | any | Dry-run playbook 03-ssh-hardening and show the diff | `ansible-playbook playbooks/03-ssh-hardening.yml --check --diff` | Nothing changes; review before applying. |
| T0140 | L3 | any | Dry-run playbook 04-firewall and show the diff | `ansible-playbook playbooks/04-firewall.yml --check --diff` | Nothing changes; review before applying. |
| T0141 | L3 | any | Dry-run playbook 05-patching and show the diff | `ansible-playbook playbooks/05-patching.yml --check --diff` | Nothing changes; review before applying. |
| T0142 | L3 | any | Dry-run playbook 06-cron-jobs and show the diff | `ansible-playbook playbooks/06-cron-jobs.yml --check --diff` | Nothing changes; review before applying. |
| T0143 | L3 | any | Dry-run playbook 07-nginx and show the diff | `ansible-playbook playbooks/07-nginx.yml --check --diff` | Nothing changes; review before applying. |
| T0144 | L3 | any | Dry-run playbook 08-health-report and show the diff | `ansible-playbook playbooks/08-health-report.yml --check --diff` | Nothing changes; review before applying. |
| T0145 | L3 | any | Encrypt a secrets file | `ansible-vault create group_vars/all/vault.yml` | Ansible operations. |
| T0146 | L3 | any | List hosts in the inventory | `ansible-inventory --graph` | Ansible operations. |
| T0147 | L3 | any | Run the full site playbook with vault password prompt | `ansible-playbook site.yml --ask-vault-pass` | Ansible operations. |
| T0148 | L3 | any | Show documentation of a module | `ansible-doc ansible.builtin.cron` | Ansible operations. |
| T0149 | L4 | any | Ansible: Disable root SSH login on group 'all' | `ansible all -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0150 | L4 | any | Ansible: Disable root SSH login on group 'backup' | `ansible backup -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0151 | L4 | any | Ansible: Disable root SSH login on group 'db' | `ansible db -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0152 | L4 | any | Ansible: Disable root SSH login on group 'dev' | `ansible dev -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0153 | L4 | any | Ansible: Disable root SSH login on group 'infra' | `ansible infra -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0154 | L4 | any | Ansible: Disable root SSH login on group 'monitoring' | `ansible monitoring -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0155 | L4 | any | Ansible: Disable root SSH login on group 'prod' | `ansible prod -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0156 | L4 | any | Ansible: Disable root SSH login on group 'rocky' | `ansible rocky -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0157 | L4 | any | Ansible: Disable root SSH login on group 'ubuntu' | `ansible ubuntu -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0158 | L4 | any | Ansible: Disable root SSH login on group 'web' | `ansible web -m lineinfile -a "path=/etc/ssh/sshd_config.d/10-hardening.conf line='PermitRootLogin no' create=true" -b` | Ad-hoc command from the ansible/ directory. |
| T0159 | L4 | any | Ansible: Reboot all servers in group 'all' and wait until back | `ansible all -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0160 | L4 | any | Ansible: Reboot all servers in group 'backup' and wait until back | `ansible backup -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0161 | L4 | any | Ansible: Reboot all servers in group 'db' and wait until back | `ansible db -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0162 | L4 | any | Ansible: Reboot all servers in group 'dev' and wait until back | `ansible dev -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0163 | L4 | any | Ansible: Reboot all servers in group 'infra' and wait until back | `ansible infra -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0164 | L4 | any | Ansible: Reboot all servers in group 'monitoring' and wait until back | `ansible monitoring -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0165 | L4 | any | Ansible: Reboot all servers in group 'prod' and wait until back | `ansible prod -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0166 | L4 | any | Ansible: Reboot all servers in group 'rocky' and wait until back | `ansible rocky -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0167 | L4 | any | Ansible: Reboot all servers in group 'ubuntu' and wait until back | `ansible ubuntu -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0168 | L4 | any | Ansible: Reboot all servers in group 'web' and wait until back | `ansible web -m reboot -b` | Ad-hoc command from the ansible/ directory. |
| T0169 | L4 | any | Run on 5 hosts at a time | `ansible-playbook site.yml --forks 5` | Ansible operations. |
| T0170 | L4 | any | Run only tasks tagged ssh | `ansible-playbook site.yml --tags ssh` | Ansible operations. |
