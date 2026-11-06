# 19. SELinux and AppArmor (mandatory access control)

Level: advanced

Even if a service is hacked, MAC limits what the process can touch.

## SELinux (Rocky / RHEL)
```bash
getenforce                        # Enforcing / Permissive / Disabled
sestatus
ls -Z /var/www/html               # file contexts
ps -eZ | grep nginx               # process contexts
sudo ausearch -m avc -ts recent   # denials
sudo sealert -a /var/log/audit/audit.log
```
### Scenario: Nginx serves files from /srv/web and gets 403
Permissions are fine, so check SELinux:
```bash
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/web(/.*)?"
sudo restorecon -Rv /srv/web
```
### Scenario: service must listen on port 8081
```bash
sudo semanage port -a -t http_port_t -p tcp 8081
```
### Scenario: allow Nginx to proxy to a backend
```bash
sudo setsebool -P httpd_can_network_connect on
```
Rule: never "fix" by `setenforce 0` in production. Find the denial and allow exactly that.

## AppArmor (Ubuntu)
```bash
sudo aa-status
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx   # log only
sudo aa-enforce  /etc/apparmor.d/usr.sbin.nginx   # block
journalctl -k | grep apparmor
```
