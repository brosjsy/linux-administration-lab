# SELinux (40 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T3144 | L4 | rhel | Allow a service on non-standard port 10051 (zabbix_port_t) | `sudo semanage port -a -t zabbix_port_t -p tcp 10051` | Otherwise SELinux blocks the bind. |
| T3145 | L4 | rhel | Allow a service on non-standard port 2222 (ssh_port_t) | `sudo semanage port -a -t ssh_port_t -p tcp 2222` | Otherwise SELinux blocks the bind. |
| T3146 | L4 | rhel | Allow a service on non-standard port 3307 (mysqld_port_t) | `sudo semanage port -a -t mysqld_port_t -p tcp 3307` | Otherwise SELinux blocks the bind. |
| T3147 | L4 | rhel | Allow a service on non-standard port 5433 (postgresql_port_t) | `sudo semanage port -a -t postgresql_port_t -p tcp 5433` | Otherwise SELinux blocks the bind. |
| T3148 | L4 | rhel | Allow a service on non-standard port 8081 (http_port_t) | `sudo semanage port -a -t http_port_t -p tcp 8081` | Otherwise SELinux blocks the bind. |
| T3149 | L4 | rhel | Allow a service on non-standard port 8443 (http_port_t) | `sudo semanage port -a -t http_port_t -p tcp 8443` | Otherwise SELinux blocks the bind. |
| T3150 | L4 | rhel | Check the SELinux boolean container_manage_cgroup | `getsebool container_manage_cgroup` | Controls whether to let containers manage cgroups. |
| T3151 | L4 | rhel | Check the SELinux boolean ftpd_full_access | `getsebool ftpd_full_access` | Controls whether to give FTP full filesystem access. |
| T3152 | L4 | rhel | Check the SELinux boolean httpd_can_network_connect | `getsebool httpd_can_network_connect` | Controls whether to let web servers connect to backends. |
| T3153 | L4 | rhel | Check the SELinux boolean httpd_can_network_connect_db | `getsebool httpd_can_network_connect_db` | Controls whether to let web servers connect to databases. |
| T3154 | L4 | rhel | Check the SELinux boolean httpd_enable_homedirs | `getsebool httpd_enable_homedirs` | Controls whether to serve user home directories. |
| T3155 | L4 | rhel | Check the SELinux boolean httpd_use_nfs | `getsebool httpd_use_nfs` | Controls whether to let web servers read NFS content. |
| T3156 | L4 | rhel | Check the SELinux boolean nfs_export_all_rw | `getsebool nfs_export_all_rw` | Controls whether to let NFS export any directory read-write. |
| T3157 | L4 | rhel | Check the SELinux boolean samba_enable_home_dirs | `getsebool samba_enable_home_dirs` | Controls whether to share home directories over Samba. |
| T3158 | L4 | rhel | Check the SELinux boolean samba_export_all_rw | `getsebool samba_export_all_rw` | Controls whether to let Samba share any directory read-write. |
| T3159 | L4 | rhel | Check the SELinux boolean use_nfs_home_dirs | `getsebool use_nfs_home_dirs` | Controls whether to allow NFS-mounted home directories. |
| T3160 | L4 | rhel | Label /srv/pgdata as postgresql_db_t permanently | `sudo semanage fcontext -a -t postgresql_db_t "/srv/pgdata(/.*)?" && sudo restorecon -Rv /srv/pgdata` | restorecon applies the rule. |
| T3161 | L4 | rhel | Label /srv/samba as samba_share_t permanently | `sudo semanage fcontext -a -t samba_share_t "/srv/samba(/.*)?" && sudo restorecon -Rv /srv/samba` | restorecon applies the rule. |
| T3162 | L4 | rhel | Label /srv/web as httpd_sys_content_t permanently | `sudo semanage fcontext -a -t httpd_sys_content_t "/srv/web(/.*)?" && sudo restorecon -Rv /srv/web` | restorecon applies the rule. |
| T3163 | L4 | rhel | Label /srv/web/uploads as httpd_sys_rw_content_t permanently | `sudo semanage fcontext -a -t httpd_sys_rw_content_t "/srv/web/uploads(/.*)?" && sudo restorecon -Rv /srv/web/uploads` | restorecon applies the rule. |
| T3164 | L4 | rhel | Permanently disable container_manage_cgroup | `sudo setsebool -P container_manage_cgroup off` | Turn off what you do not need. |
| T3165 | L4 | rhel | Permanently disable ftpd_full_access | `sudo setsebool -P ftpd_full_access off` | Turn off what you do not need. |
| T3166 | L4 | rhel | Permanently disable httpd_can_network_connect | `sudo setsebool -P httpd_can_network_connect off` | Turn off what you do not need. |
| T3167 | L4 | rhel | Permanently disable httpd_can_network_connect_db | `sudo setsebool -P httpd_can_network_connect_db off` | Turn off what you do not need. |
| T3168 | L4 | rhel | Permanently disable httpd_enable_homedirs | `sudo setsebool -P httpd_enable_homedirs off` | Turn off what you do not need. |
| T3169 | L4 | rhel | Permanently disable httpd_use_nfs | `sudo setsebool -P httpd_use_nfs off` | Turn off what you do not need. |
| T3170 | L4 | rhel | Permanently disable nfs_export_all_rw | `sudo setsebool -P nfs_export_all_rw off` | Turn off what you do not need. |
| T3171 | L4 | rhel | Permanently disable samba_enable_home_dirs | `sudo setsebool -P samba_enable_home_dirs off` | Turn off what you do not need. |
| T3172 | L4 | rhel | Permanently disable samba_export_all_rw | `sudo setsebool -P samba_export_all_rw off` | Turn off what you do not need. |
| T3173 | L4 | rhel | Permanently disable use_nfs_home_dirs | `sudo setsebool -P use_nfs_home_dirs off` | Turn off what you do not need. |
| T3174 | L4 | rhel | Permanently enable container_manage_cgroup (let containers manage cgroups) | `sudo setsebool -P container_manage_cgroup on` | -P survives reboot. |
| T3175 | L4 | rhel | Permanently enable ftpd_full_access (give FTP full filesystem access) | `sudo setsebool -P ftpd_full_access on` | -P survives reboot. |
| T3176 | L4 | rhel | Permanently enable httpd_can_network_connect (let web servers connect to backends) | `sudo setsebool -P httpd_can_network_connect on` | -P survives reboot. |
| T3177 | L4 | rhel | Permanently enable httpd_can_network_connect_db (let web servers connect to databases) | `sudo setsebool -P httpd_can_network_connect_db on` | -P survives reboot. |
| T3178 | L4 | rhel | Permanently enable httpd_enable_homedirs (serve user home directories) | `sudo setsebool -P httpd_enable_homedirs on` | -P survives reboot. |
| T3179 | L4 | rhel | Permanently enable httpd_use_nfs (let web servers read NFS content) | `sudo setsebool -P httpd_use_nfs on` | -P survives reboot. |
| T3180 | L4 | rhel | Permanently enable nfs_export_all_rw (let NFS export any directory read-write) | `sudo setsebool -P nfs_export_all_rw on` | -P survives reboot. |
| T3181 | L4 | rhel | Permanently enable samba_enable_home_dirs (share home directories over Samba) | `sudo setsebool -P samba_enable_home_dirs on` | -P survives reboot. |
| T3182 | L4 | rhel | Permanently enable samba_export_all_rw (let Samba share any directory read-write) | `sudo setsebool -P samba_export_all_rw on` | -P survives reboot. |
| T3183 | L4 | rhel | Permanently enable use_nfs_home_dirs (allow NFS-mounted home directories) | `sudo setsebool -P use_nfs_home_dirs on` | -P survives reboot. |
