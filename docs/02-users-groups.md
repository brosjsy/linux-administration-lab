# 02. Users, groups and sudo

## Tasks
```bash
sudo groupadd support
sudo useradd -m -s /bin/bash -G support alice
sudo passwd alice
sudo chage -d 0 alice                 # force password change at first login
sudo chage -M 90 -W 7 alice            # password expires every 90 days
id alice; groups alice
sudo usermod -aG sudo alice           # Debian/Ubuntu (wheel on RHEL)
sudo usermod -L bob                    # lock an account
sudo userdel -r olduser                # remove user and home
getent passwd alice
lastlog | head; last -n 10
```

## Restricted sudo for the support team
```bash
sudo visudo -f /etc/sudoers.d/support
# %support ALL=(root) /usr/bin/systemctl restart nginx, /usr/bin/journalctl
```

## Check
- [x] `alice` must change password at first login
- [x] `support` group can restart nginx and read logs, nothing else
