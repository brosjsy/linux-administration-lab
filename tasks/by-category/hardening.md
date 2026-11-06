# Hardening (26 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1493 | L3 | any | Allow cron only for root and admin | `printf 'root\nadmin\n' \| sudo tee /etc/cron.allow` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1494 | L3 | any | Block USB storage kernel module | `echo 'install usb-storage /bin/true' \| sudo tee /etc/modprobe.d/usb-storage.conf` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1495 | L3 | any | Check fail2ban jail list | `sudo fail2ban-client status` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1496 | L3 | any | Disable SSH password authentication | `echo 'PasswordAuthentication no' \| sudo tee /etc/ssh/sshd_config.d/11-pass.conf && sudo sshd -t && sudo systemctl reload ssh` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1497 | L3 | any | Disable root SSH login | `echo 'PermitRootLogin no' \| sudo tee /etc/ssh/sshd_config.d/10-root.conf && sudo sshd -t && sudo systemctl reload ssh` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1498 | L3 | rhel | Enable automatic security updates on Rocky | `sudo dnf install -y dnf-automatic && sudo systemctl enable --now dnf-automatic-install.timer` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1499 | L3 | debian | Enable automatic security updates on Ubuntu | `sudo apt install -y unattended-upgrades && sudo dpkg-reconfigure -plow unattended-upgrades` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1500 | L3 | any | Find accounts with UID 0 besides root | `awk -F: '($3==0 && $1!="root"){print $1}' /etc/passwd` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1501 | L3 | any | Find accounts with empty passwords | `sudo awk -F: '($2==""){print $1}' /etc/shadow` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1502 | L3 | any | Limit SSH to members of group ssh-users | `echo 'AllowGroups ssh-users' \| sudo tee /etc/ssh/sshd_config.d/12-groups.conf && sudo sshd -t && sudo systemctl reload ssh` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1503 | L3 | any | List enabled services to find unneeded ones | `systemctl list-unit-files --state=enabled --type=service` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1504 | L3 | any | Mount /tmp with noexec,nosuid,nodev | `echo 'tmpfs /tmp tmpfs defaults,noexec,nosuid,nodev,size=1G 0 0' \| sudo tee -a /etc/fstab && sudo mount -o remount /tmp` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1505 | L3 | any | Require 12-character passwords | `sudo sed -i 's/^#\? *minlen.*/minlen = 12/' /etc/security/pwquality.conf` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1506 | L3 | any | Run the lab hardening audit | `sudo /opt/lab/scripts/harden_audit.sh` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1507 | L3 | any | Set a legal login banner | `echo 'Authorised access only. Activity is logged.' \| sudo tee /etc/issue.net` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1508 | L3 | any | Set maximum password age to 90 days for new users | `sudo sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS 90/' /etc/login.defs` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1509 | L3 | any | Show all listening ports and programs | `sudo ss -tulpn` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1510 | L4 | rhel | Allow Nginx to connect to backends under SELinux | `sudo setsebool -P httpd_can_network_connect on` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1511 | L4 | rhel | Check SELinux mode | `getenforce && sestatus` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1512 | L4 | any | Check files against the AIDE database | `sudo aide --check` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1513 | L4 | any | Initialise the AIDE integrity database | `sudo aideinit && sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1514 | L4 | rhel | Restore SELinux contexts under /srv/web | `sudo restorecon -Rv /srv/web` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1515 | L4 | any | Run a full Lynis security audit | `sudo lynis audit system --quick` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1516 | L4 | debian | Show AppArmor profiles and their mode | `sudo aa-status` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1517 | L4 | rhel | Show recent SELinux denials | `sudo ausearch -m avc -ts recent` | Part of a CIS-style baseline; re-run the audit after the change. |
| T1518 | L4 | any | Show the Lynis hardening index | `sudo grep hardening_index /var/log/lynis-report.dat` | Part of a CIS-style baseline; re-run the audit after the change. |
