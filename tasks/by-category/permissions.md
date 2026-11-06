# Permissions (94 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T2958 | L1 | any | Make alice the owner and developers the group of /srv/developers | `sudo chown -R alice:developers /srv/developers` | -R applies to everything inside. |
| T2959 | L1 | any | Make alice the owner and docker the group of /srv/docker | `sudo chown -R alice:docker /srv/docker` | -R applies to everything inside. |
| T2960 | L1 | any | Make alice the owner and sudo the group of /srv/sudo | `sudo chown -R alice:sudo /srv/sudo` | -R applies to everything inside. |
| T2961 | L1 | any | Make alice the owner and support the group of /srv/support | `sudo chown -R alice:support /srv/support` | -R applies to everything inside. |
| T2962 | L1 | any | Make alice the owner and wheel the group of /srv/wheel | `sudo chown -R alice:wheel /srv/wheel` | -R applies to everything inside. |
| T2963 | L1 | any | Make alice the owner and www-data the group of /srv/www-data | `sudo chown -R alice:www-data /srv/www-data` | -R applies to everything inside. |
| T2964 | L1 | any | Make backup the owner and developers the group of /srv/developers | `sudo chown -R backup:developers /srv/developers` | -R applies to everything inside. |
| T2965 | L1 | any | Make backup the owner and docker the group of /srv/docker | `sudo chown -R backup:docker /srv/docker` | -R applies to everything inside. |
| T2966 | L1 | any | Make backup the owner and sudo the group of /srv/sudo | `sudo chown -R backup:sudo /srv/sudo` | -R applies to everything inside. |
| T2967 | L1 | any | Make backup the owner and support the group of /srv/support | `sudo chown -R backup:support /srv/support` | -R applies to everything inside. |
| T2968 | L1 | any | Make backup the owner and wheel the group of /srv/wheel | `sudo chown -R backup:wheel /srv/wheel` | -R applies to everything inside. |
| T2969 | L1 | any | Make backup the owner and www-data the group of /srv/www-data | `sudo chown -R backup:www-data /srv/www-data` | -R applies to everything inside. |
| T2970 | L1 | any | Make bob the owner and developers the group of /srv/developers | `sudo chown -R bob:developers /srv/developers` | -R applies to everything inside. |
| T2971 | L1 | any | Make bob the owner and docker the group of /srv/docker | `sudo chown -R bob:docker /srv/docker` | -R applies to everything inside. |
| T2972 | L1 | any | Make bob the owner and sudo the group of /srv/sudo | `sudo chown -R bob:sudo /srv/sudo` | -R applies to everything inside. |
| T2973 | L1 | any | Make bob the owner and support the group of /srv/support | `sudo chown -R bob:support /srv/support` | -R applies to everything inside. |
| T2974 | L1 | any | Make bob the owner and wheel the group of /srv/wheel | `sudo chown -R bob:wheel /srv/wheel` | -R applies to everything inside. |
| T2975 | L1 | any | Make bob the owner and www-data the group of /srv/www-data | `sudo chown -R bob:www-data /srv/www-data` | -R applies to everything inside. |
| T2976 | L1 | any | Make deploy the owner and developers the group of /srv/developers | `sudo chown -R deploy:developers /srv/developers` | -R applies to everything inside. |
| T2977 | L1 | any | Make deploy the owner and docker the group of /srv/docker | `sudo chown -R deploy:docker /srv/docker` | -R applies to everything inside. |
| T2978 | L1 | any | Make deploy the owner and sudo the group of /srv/sudo | `sudo chown -R deploy:sudo /srv/sudo` | -R applies to everything inside. |
| T2979 | L1 | any | Make deploy the owner and support the group of /srv/support | `sudo chown -R deploy:support /srv/support` | -R applies to everything inside. |
| T2980 | L1 | any | Make deploy the owner and wheel the group of /srv/wheel | `sudo chown -R deploy:wheel /srv/wheel` | -R applies to everything inside. |
| T2981 | L1 | any | Make deploy the owner and www-data the group of /srv/www-data | `sudo chown -R deploy:www-data /srv/www-data` | -R applies to everything inside. |
| T2982 | L1 | any | Make ivan the owner and developers the group of /srv/developers | `sudo chown -R ivan:developers /srv/developers` | -R applies to everything inside. |
| T2983 | L1 | any | Make ivan the owner and docker the group of /srv/docker | `sudo chown -R ivan:docker /srv/docker` | -R applies to everything inside. |
| T2984 | L1 | any | Make ivan the owner and sudo the group of /srv/sudo | `sudo chown -R ivan:sudo /srv/sudo` | -R applies to everything inside. |
| T2985 | L1 | any | Make ivan the owner and support the group of /srv/support | `sudo chown -R ivan:support /srv/support` | -R applies to everything inside. |
| T2986 | L1 | any | Make ivan the owner and wheel the group of /srv/wheel | `sudo chown -R ivan:wheel /srv/wheel` | -R applies to everything inside. |
| T2987 | L1 | any | Make ivan the owner and www-data the group of /srv/www-data | `sudo chown -R ivan:www-data /srv/www-data` | -R applies to everything inside. |
| T2988 | L1 | any | Make olga the owner and developers the group of /srv/developers | `sudo chown -R olga:developers /srv/developers` | -R applies to everything inside. |
| T2989 | L1 | any | Make olga the owner and docker the group of /srv/docker | `sudo chown -R olga:docker /srv/docker` | -R applies to everything inside. |
| T2990 | L1 | any | Make olga the owner and sudo the group of /srv/sudo | `sudo chown -R olga:sudo /srv/sudo` | -R applies to everything inside. |
| T2991 | L1 | any | Make olga the owner and support the group of /srv/support | `sudo chown -R olga:support /srv/support` | -R applies to everything inside. |
| T2992 | L1 | any | Make olga the owner and wheel the group of /srv/wheel | `sudo chown -R olga:wheel /srv/wheel` | -R applies to everything inside. |
| T2993 | L1 | any | Make olga the owner and www-data the group of /srv/www-data | `sudo chown -R olga:www-data /srv/www-data` | -R applies to everything inside. |
| T2994 | L1 | any | Set mode 0400 (owner read only) on a script script.sh | `chmod 0400 script.sh` | Typical for certificates and keys that never change. |
| T2995 | L1 | any | Set mode 0400 (owner read only) on a shared directory /srv/share | `chmod 0400 /srv/share` | Typical for certificates and keys that never change. |
| T2996 | L1 | any | Set mode 0400 (owner read only) on an SSH private key ~/.ssh/id_ed25519 | `chmod 0400 ~/.ssh/id_ed25519` | Typical for certificates and keys that never change. |
| T2997 | L1 | any | Set mode 0400 (owner read only) on an application config /etc/app/app.conf | `chmod 0400 /etc/app/app.conf` | Typical for certificates and keys that never change. |
| T2998 | L1 | any | Set mode 0400 (owner read only) on the backup directory /srv/backups | `chmod 0400 /srv/backups` | Typical for certificates and keys that never change. |
| T2999 | L1 | any | Set mode 0440 (owner and group read only) on a script script.sh | `chmod 0440 script.sh` | Typical for sudoers drop-in files. |
| T3000 | L1 | any | Set mode 0440 (owner and group read only) on a shared directory /srv/share | `chmod 0440 /srv/share` | Typical for sudoers drop-in files. |
| T3001 | L1 | any | Set mode 0440 (owner and group read only) on an SSH private key ~/.ssh/id_ed25519 | `chmod 0440 ~/.ssh/id_ed25519` | Typical for sudoers drop-in files. |
| T3002 | L1 | any | Set mode 0440 (owner and group read only) on an application config /etc/app/app.conf | `chmod 0440 /etc/app/app.conf` | Typical for sudoers drop-in files. |
| T3003 | L1 | any | Set mode 0440 (owner and group read only) on the backup directory /srv/backups | `chmod 0440 /srv/backups` | Typical for sudoers drop-in files. |
| T3004 | L1 | any | Set mode 1777 (everyone full + sticky bit) on a script script.sh | `chmod 1777 script.sh` | Typical for shared temp directories. |
| T3005 | L1 | any | Set mode 1777 (everyone full + sticky bit) on a shared directory /srv/share | `chmod 1777 /srv/share` | Typical for shared temp directories. |
| T3006 | L1 | any | Set mode 1777 (everyone full + sticky bit) on an SSH private key ~/.ssh/id_ed25519 | `chmod 1777 ~/.ssh/id_ed25519` | Typical for shared temp directories. |
| T3007 | L1 | any | Set mode 1777 (everyone full + sticky bit) on an application config /etc/app/app.conf | `chmod 1777 /etc/app/app.conf` | Typical for shared temp directories. |
| T3008 | L1 | any | Set mode 1777 (everyone full + sticky bit) on the backup directory /srv/backups | `chmod 1777 /srv/backups` | Typical for shared temp directories. |
| T3009 | L1 | any | Set mode 2770 (group full + SGID) on a script script.sh | `chmod 2770 script.sh` | Typical for shared team folders. |
| T3010 | L1 | any | Set mode 2770 (group full + SGID) on a shared directory /srv/share | `chmod 2770 /srv/share` | Typical for shared team folders. |
| T3011 | L1 | any | Set mode 2770 (group full + SGID) on an SSH private key ~/.ssh/id_ed25519 | `chmod 2770 ~/.ssh/id_ed25519` | Typical for shared team folders. |
| T3012 | L1 | any | Set mode 2770 (group full + SGID) on an application config /etc/app/app.conf | `chmod 2770 /etc/app/app.conf` | Typical for shared team folders. |
| T3013 | L1 | any | Set mode 2770 (group full + SGID) on the backup directory /srv/backups | `chmod 2770 /srv/backups` | Typical for shared team folders. |
| T3014 | L1 | any | Set mode 600 (owner read/write only) on a script script.sh | `chmod 600 script.sh` | Typical for private keys, secrets. |
| T3015 | L1 | any | Set mode 600 (owner read/write only) on a shared directory /srv/share | `chmod 600 /srv/share` | Typical for private keys, secrets. |
| T3016 | L1 | any | Set mode 600 (owner read/write only) on an SSH private key ~/.ssh/id_ed25519 | `chmod 600 ~/.ssh/id_ed25519` | Typical for private keys, secrets. |
| T3017 | L1 | any | Set mode 600 (owner read/write only) on an application config /etc/app/app.conf | `chmod 600 /etc/app/app.conf` | Typical for private keys, secrets. |
| T3018 | L1 | any | Set mode 600 (owner read/write only) on the backup directory /srv/backups | `chmod 600 /srv/backups` | Typical for private keys, secrets. |
| T3019 | L1 | any | Set mode 640 (owner rw, group read) on a script script.sh | `chmod 640 script.sh` | Typical for config with secrets readable by a service group. |
| T3020 | L1 | any | Set mode 640 (owner rw, group read) on a shared directory /srv/share | `chmod 640 /srv/share` | Typical for config with secrets readable by a service group. |
| T3021 | L1 | any | Set mode 640 (owner rw, group read) on an SSH private key ~/.ssh/id_ed25519 | `chmod 640 ~/.ssh/id_ed25519` | Typical for config with secrets readable by a service group. |
| T3022 | L1 | any | Set mode 640 (owner rw, group read) on an application config /etc/app/app.conf | `chmod 640 /etc/app/app.conf` | Typical for config with secrets readable by a service group. |
| T3023 | L1 | any | Set mode 640 (owner rw, group read) on the backup directory /srv/backups | `chmod 640 /srv/backups` | Typical for config with secrets readable by a service group. |
| T3024 | L1 | any | Set mode 644 (owner rw, everyone read) on a script script.sh | `chmod 644 script.sh` | Typical for normal files. |
| T3025 | L1 | any | Set mode 644 (owner rw, everyone read) on a shared directory /srv/share | `chmod 644 /srv/share` | Typical for normal files. |
| T3026 | L1 | any | Set mode 644 (owner rw, everyone read) on an SSH private key ~/.ssh/id_ed25519 | `chmod 644 ~/.ssh/id_ed25519` | Typical for normal files. |
| T3027 | L1 | any | Set mode 644 (owner rw, everyone read) on an application config /etc/app/app.conf | `chmod 644 /etc/app/app.conf` | Typical for normal files. |
| T3028 | L1 | any | Set mode 644 (owner rw, everyone read) on the backup directory /srv/backups | `chmod 644 /srv/backups` | Typical for normal files. |
| T3029 | L1 | any | Set mode 700 (owner full, nobody else) on a script script.sh | `chmod 700 script.sh` | Typical for private directories, scripts. |
| T3030 | L1 | any | Set mode 700 (owner full, nobody else) on a shared directory /srv/share | `chmod 700 /srv/share` | Typical for private directories, scripts. |
| T3031 | L1 | any | Set mode 700 (owner full, nobody else) on an SSH private key ~/.ssh/id_ed25519 | `chmod 700 ~/.ssh/id_ed25519` | Typical for private directories, scripts. |
| T3032 | L1 | any | Set mode 700 (owner full, nobody else) on an application config /etc/app/app.conf | `chmod 700 /etc/app/app.conf` | Typical for private directories, scripts. |
| T3033 | L1 | any | Set mode 700 (owner full, nobody else) on the backup directory /srv/backups | `chmod 700 /srv/backups` | Typical for private directories, scripts. |
| T3034 | L1 | any | Set mode 750 (owner full, group read/execute) on a script script.sh | `chmod 750 script.sh` | Typical for team scripts and directories. |
| T3035 | L1 | any | Set mode 750 (owner full, group read/execute) on a shared directory /srv/share | `chmod 750 /srv/share` | Typical for team scripts and directories. |
| T3036 | L1 | any | Set mode 750 (owner full, group read/execute) on an SSH private key ~/.ssh/id_ed25519 | `chmod 750 ~/.ssh/id_ed25519` | Typical for team scripts and directories. |
| T3037 | L1 | any | Set mode 750 (owner full, group read/execute) on an application config /etc/app/app.conf | `chmod 750 /etc/app/app.conf` | Typical for team scripts and directories. |
| T3038 | L1 | any | Set mode 750 (owner full, group read/execute) on the backup directory /srv/backups | `chmod 750 /srv/backups` | Typical for team scripts and directories. |
| T3039 | L1 | any | Set mode 755 (owner full, everyone read/execute) on a script script.sh | `chmod 755 script.sh` | Typical for public programs and directories. |
| T3040 | L1 | any | Set mode 755 (owner full, everyone read/execute) on a shared directory /srv/share | `chmod 755 /srv/share` | Typical for public programs and directories. |
| T3041 | L1 | any | Set mode 755 (owner full, everyone read/execute) on an SSH private key ~/.ssh/id_ed25519 | `chmod 755 ~/.ssh/id_ed25519` | Typical for public programs and directories. |
| T3042 | L1 | any | Set mode 755 (owner full, everyone read/execute) on an application config /etc/app/app.conf | `chmod 755 /etc/app/app.conf` | Typical for public programs and directories. |
| T3043 | L1 | any | Set mode 755 (owner full, everyone read/execute) on the backup directory /srv/backups | `chmod 755 /srv/backups` | Typical for public programs and directories. |
| T3044 | L2 | any | Give user bob read access to /srv/share without changing its group | `sudo setfacl -m u:bob:rx /srv/share` | ACLs add exceptions on top of normal permissions. |
| T3045 | L2 | any | Make new files in /srv/share inherit an ACL for group developers | `sudo setfacl -d -m g:developers:rwx /srv/share` | -d sets the default ACL for new files. |
| T3046 | L2 | any | Remove all ACLs from /srv/share | `sudo setfacl -b /srv/share` | Back to normal permissions. |
| T3047 | L2 | any | Show ACLs of /srv/share | `getfacl /srv/share` | A + in ls -l output means ACLs exist. |
| T3048 | L2 | any | Show permissions as numbers | `stat -c '%a %U:%G %n' /etc/passwd /etc/shadow` | Easier to compare than rwx. |
| T3049 | L2 | any | Show the default permission mask | `umask` | 0022 means new files 644, directories 755. |
| T3050 | L3 | any | Find all SUID and SGID programs | `sudo find / -xdev -perm /6000 -type f 2>/dev/null` | Review regularly; unexpected entries may be backdoors. |
| T3051 | L3 | any | Make a file immutable even for root | `sudo chattr +i /etc/resolv.conf` | Remove with chattr -i; check with lsattr. |
