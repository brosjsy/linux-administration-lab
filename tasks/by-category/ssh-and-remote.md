# SSH and remote (98 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T3184 | L1 | any | Connect to 192.168.56.10 as admin with SSH | `ssh admin@192.168.56.10` | Add -v to debug connection problems. |
| T3185 | L1 | any | Connect to 192.168.56.10 as deploy with SSH | `ssh deploy@192.168.56.10` | Add -v to debug connection problems. |
| T3186 | L1 | any | Connect to 192.168.56.10 as ivan with SSH | `ssh ivan@192.168.56.10` | Add -v to debug connection problems. |
| T3187 | L1 | any | Connect to 192.168.56.20 as admin with SSH | `ssh admin@192.168.56.20` | Add -v to debug connection problems. |
| T3188 | L1 | any | Connect to 192.168.56.20 as deploy with SSH | `ssh deploy@192.168.56.20` | Add -v to debug connection problems. |
| T3189 | L1 | any | Connect to 192.168.56.20 as ivan with SSH | `ssh ivan@192.168.56.20` | Add -v to debug connection problems. |
| T3190 | L1 | any | Connect to backup-host as admin with SSH | `ssh admin@backup-host` | Add -v to debug connection problems. |
| T3191 | L1 | any | Connect to backup-host as deploy with SSH | `ssh deploy@backup-host` | Add -v to debug connection problems. |
| T3192 | L1 | any | Connect to backup-host as ivan with SSH | `ssh ivan@backup-host` | Add -v to debug connection problems. |
| T3193 | L1 | any | Connect to db1.lab.local as admin with SSH | `ssh admin@db1.lab.local` | Add -v to debug connection problems. |
| T3194 | L1 | any | Connect to db1.lab.local as deploy with SSH | `ssh deploy@db1.lab.local` | Add -v to debug connection problems. |
| T3195 | L1 | any | Connect to db1.lab.local as ivan with SSH | `ssh ivan@db1.lab.local` | Add -v to debug connection problems. |
| T3196 | L1 | any | Connect to web1.lab.local as admin with SSH | `ssh admin@web1.lab.local` | Add -v to debug connection problems. |
| T3197 | L1 | any | Connect to web1.lab.local as deploy with SSH | `ssh deploy@web1.lab.local` | Add -v to debug connection problems. |
| T3198 | L1 | any | Connect to web1.lab.local as ivan with SSH | `ssh ivan@web1.lab.local` | Add -v to debug connection problems. |
| T3199 | L1 | any | Generate a modern SSH key | `ssh-keygen -t ed25519 -C "name@company"` | SSH administration. |
| T3200 | L2 | any | Copy app.tar.gz to /tmp on 192.168.56.10 as admin | `scp app.tar.gz admin@192.168.56.10:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3201 | L2 | any | Copy app.tar.gz to /tmp on 192.168.56.10 as deploy | `scp app.tar.gz deploy@192.168.56.10:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3202 | L2 | any | Copy app.tar.gz to /tmp on 192.168.56.10 as ivan | `scp app.tar.gz ivan@192.168.56.10:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3203 | L2 | any | Copy app.tar.gz to /tmp on 192.168.56.20 as admin | `scp app.tar.gz admin@192.168.56.20:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3204 | L2 | any | Copy app.tar.gz to /tmp on 192.168.56.20 as deploy | `scp app.tar.gz deploy@192.168.56.20:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3205 | L2 | any | Copy app.tar.gz to /tmp on 192.168.56.20 as ivan | `scp app.tar.gz ivan@192.168.56.20:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3206 | L2 | any | Copy app.tar.gz to /tmp on backup-host as admin | `scp app.tar.gz admin@backup-host:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3207 | L2 | any | Copy app.tar.gz to /tmp on backup-host as deploy | `scp app.tar.gz deploy@backup-host:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3208 | L2 | any | Copy app.tar.gz to /tmp on backup-host as ivan | `scp app.tar.gz ivan@backup-host:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3209 | L2 | any | Copy app.tar.gz to /tmp on db1.lab.local as admin | `scp app.tar.gz admin@db1.lab.local:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3210 | L2 | any | Copy app.tar.gz to /tmp on db1.lab.local as deploy | `scp app.tar.gz deploy@db1.lab.local:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3211 | L2 | any | Copy app.tar.gz to /tmp on db1.lab.local as ivan | `scp app.tar.gz ivan@db1.lab.local:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3212 | L2 | any | Copy app.tar.gz to /tmp on web1.lab.local as admin | `scp app.tar.gz admin@web1.lab.local:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3213 | L2 | any | Copy app.tar.gz to /tmp on web1.lab.local as deploy | `scp app.tar.gz deploy@web1.lab.local:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3214 | L2 | any | Copy app.tar.gz to /tmp on web1.lab.local as ivan | `scp app.tar.gz ivan@web1.lab.local:/tmp/` | scp uses SSH; rsync is better for big folders. |
| T3215 | L2 | any | Copy your SSH key to admin@192.168.56.10 | `ssh-copy-id admin@192.168.56.10` | Enables password-less login. |
| T3216 | L2 | any | Copy your SSH key to admin@192.168.56.20 | `ssh-copy-id admin@192.168.56.20` | Enables password-less login. |
| T3217 | L2 | any | Copy your SSH key to admin@backup-host | `ssh-copy-id admin@backup-host` | Enables password-less login. |
| T3218 | L2 | any | Copy your SSH key to admin@db1.lab.local | `ssh-copy-id admin@db1.lab.local` | Enables password-less login. |
| T3219 | L2 | any | Copy your SSH key to admin@web1.lab.local | `ssh-copy-id admin@web1.lab.local` | Enables password-less login. |
| T3220 | L2 | any | Copy your SSH key to deploy@192.168.56.10 | `ssh-copy-id deploy@192.168.56.10` | Enables password-less login. |
| T3221 | L2 | any | Copy your SSH key to deploy@192.168.56.20 | `ssh-copy-id deploy@192.168.56.20` | Enables password-less login. |
| T3222 | L2 | any | Copy your SSH key to deploy@backup-host | `ssh-copy-id deploy@backup-host` | Enables password-less login. |
| T3223 | L2 | any | Copy your SSH key to deploy@db1.lab.local | `ssh-copy-id deploy@db1.lab.local` | Enables password-less login. |
| T3224 | L2 | any | Copy your SSH key to deploy@web1.lab.local | `ssh-copy-id deploy@web1.lab.local` | Enables password-less login. |
| T3225 | L2 | any | Copy your SSH key to ivan@192.168.56.10 | `ssh-copy-id ivan@192.168.56.10` | Enables password-less login. |
| T3226 | L2 | any | Copy your SSH key to ivan@192.168.56.20 | `ssh-copy-id ivan@192.168.56.20` | Enables password-less login. |
| T3227 | L2 | any | Copy your SSH key to ivan@backup-host | `ssh-copy-id ivan@backup-host` | Enables password-less login. |
| T3228 | L2 | any | Copy your SSH key to ivan@db1.lab.local | `ssh-copy-id ivan@db1.lab.local` | Enables password-less login. |
| T3229 | L2 | any | Copy your SSH key to ivan@web1.lab.local | `ssh-copy-id ivan@web1.lab.local` | Enables password-less login. |
| T3230 | L2 | any | Fix permissions of a user's .ssh directory | `chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys` | SSH administration. |
| T3231 | L2 | any | Remove an old host key after server reinstall | `ssh-keygen -R 192.168.56.10` | SSH administration. |
| T3232 | L2 | any | Run uptime on 192.168.56.10 as admin without opening a shell | `ssh admin@192.168.56.10 uptime` | Good for quick checks and scripts. |
| T3233 | L2 | any | Run uptime on 192.168.56.10 as deploy without opening a shell | `ssh deploy@192.168.56.10 uptime` | Good for quick checks and scripts. |
| T3234 | L2 | any | Run uptime on 192.168.56.10 as ivan without opening a shell | `ssh ivan@192.168.56.10 uptime` | Good for quick checks and scripts. |
| T3235 | L2 | any | Run uptime on 192.168.56.20 as admin without opening a shell | `ssh admin@192.168.56.20 uptime` | Good for quick checks and scripts. |
| T3236 | L2 | any | Run uptime on 192.168.56.20 as deploy without opening a shell | `ssh deploy@192.168.56.20 uptime` | Good for quick checks and scripts. |
| T3237 | L2 | any | Run uptime on 192.168.56.20 as ivan without opening a shell | `ssh ivan@192.168.56.20 uptime` | Good for quick checks and scripts. |
| T3238 | L2 | any | Run uptime on backup-host as admin without opening a shell | `ssh admin@backup-host uptime` | Good for quick checks and scripts. |
| T3239 | L2 | any | Run uptime on backup-host as deploy without opening a shell | `ssh deploy@backup-host uptime` | Good for quick checks and scripts. |
| T3240 | L2 | any | Run uptime on backup-host as ivan without opening a shell | `ssh ivan@backup-host uptime` | Good for quick checks and scripts. |
| T3241 | L2 | any | Run uptime on db1.lab.local as admin without opening a shell | `ssh admin@db1.lab.local uptime` | Good for quick checks and scripts. |
| T3242 | L2 | any | Run uptime on db1.lab.local as deploy without opening a shell | `ssh deploy@db1.lab.local uptime` | Good for quick checks and scripts. |
| T3243 | L2 | any | Run uptime on db1.lab.local as ivan without opening a shell | `ssh ivan@db1.lab.local uptime` | Good for quick checks and scripts. |
| T3244 | L2 | any | Run uptime on web1.lab.local as admin without opening a shell | `ssh admin@web1.lab.local uptime` | Good for quick checks and scripts. |
| T3245 | L2 | any | Run uptime on web1.lab.local as deploy without opening a shell | `ssh deploy@web1.lab.local uptime` | Good for quick checks and scripts. |
| T3246 | L2 | any | Run uptime on web1.lab.local as ivan without opening a shell | `ssh ivan@web1.lab.local uptime` | Good for quick checks and scripts. |
| T3247 | L2 | any | Show banned IPs in fail2ban for sshd | `sudo fail2ban-client status sshd` | SSH administration. |
| T3248 | L2 | any | Show the fingerprint of your SSH key | `ssh-keygen -lf ~/.ssh/id_ed25519.pub` | SSH administration. |
| T3249 | L2 | any | Unban an IP in fail2ban | `sudo fail2ban-client set sshd unbanip 203.0.113.5` | SSH administration. |
| T3250 | L3 | any | Open a tunnel to PostgreSQL on 192.168.56.10 via SSH as admin | `ssh -L 5432:localhost:5432 admin@192.168.56.10` | Then connect to localhost:5432 locally. |
| T3251 | L3 | any | Open a tunnel to PostgreSQL on 192.168.56.10 via SSH as deploy | `ssh -L 5432:localhost:5432 deploy@192.168.56.10` | Then connect to localhost:5432 locally. |
| T3252 | L3 | any | Open a tunnel to PostgreSQL on 192.168.56.10 via SSH as ivan | `ssh -L 5432:localhost:5432 ivan@192.168.56.10` | Then connect to localhost:5432 locally. |
| T3253 | L3 | any | Open a tunnel to PostgreSQL on 192.168.56.20 via SSH as admin | `ssh -L 5432:localhost:5432 admin@192.168.56.20` | Then connect to localhost:5432 locally. |
| T3254 | L3 | any | Open a tunnel to PostgreSQL on 192.168.56.20 via SSH as deploy | `ssh -L 5432:localhost:5432 deploy@192.168.56.20` | Then connect to localhost:5432 locally. |
| T3255 | L3 | any | Open a tunnel to PostgreSQL on 192.168.56.20 via SSH as ivan | `ssh -L 5432:localhost:5432 ivan@192.168.56.20` | Then connect to localhost:5432 locally. |
| T3256 | L3 | any | Open a tunnel to PostgreSQL on backup-host via SSH as admin | `ssh -L 5432:localhost:5432 admin@backup-host` | Then connect to localhost:5432 locally. |
| T3257 | L3 | any | Open a tunnel to PostgreSQL on backup-host via SSH as deploy | `ssh -L 5432:localhost:5432 deploy@backup-host` | Then connect to localhost:5432 locally. |
| T3258 | L3 | any | Open a tunnel to PostgreSQL on backup-host via SSH as ivan | `ssh -L 5432:localhost:5432 ivan@backup-host` | Then connect to localhost:5432 locally. |
| T3259 | L3 | any | Open a tunnel to PostgreSQL on db1.lab.local via SSH as admin | `ssh -L 5432:localhost:5432 admin@db1.lab.local` | Then connect to localhost:5432 locally. |
| T3260 | L3 | any | Open a tunnel to PostgreSQL on db1.lab.local via SSH as deploy | `ssh -L 5432:localhost:5432 deploy@db1.lab.local` | Then connect to localhost:5432 locally. |
| T3261 | L3 | any | Open a tunnel to PostgreSQL on db1.lab.local via SSH as ivan | `ssh -L 5432:localhost:5432 ivan@db1.lab.local` | Then connect to localhost:5432 locally. |
| T3262 | L3 | any | Open a tunnel to PostgreSQL on web1.lab.local via SSH as admin | `ssh -L 5432:localhost:5432 admin@web1.lab.local` | Then connect to localhost:5432 locally. |
| T3263 | L3 | any | Open a tunnel to PostgreSQL on web1.lab.local via SSH as deploy | `ssh -L 5432:localhost:5432 deploy@web1.lab.local` | Then connect to localhost:5432 locally. |
| T3264 | L3 | any | Open a tunnel to PostgreSQL on web1.lab.local via SSH as ivan | `ssh -L 5432:localhost:5432 ivan@web1.lab.local` | Then connect to localhost:5432 locally. |
| T3265 | L3 | any | Reach 192.168.56.10 through jump host bastion as admin | `ssh -J admin@bastion admin@192.168.56.10` | ProxyJump for servers without public access. |
| T3266 | L3 | any | Reach 192.168.56.10 through jump host bastion as deploy | `ssh -J deploy@bastion deploy@192.168.56.10` | ProxyJump for servers without public access. |
| T3267 | L3 | any | Reach 192.168.56.10 through jump host bastion as ivan | `ssh -J ivan@bastion ivan@192.168.56.10` | ProxyJump for servers without public access. |
| T3268 | L3 | any | Reach 192.168.56.20 through jump host bastion as admin | `ssh -J admin@bastion admin@192.168.56.20` | ProxyJump for servers without public access. |
| T3269 | L3 | any | Reach 192.168.56.20 through jump host bastion as deploy | `ssh -J deploy@bastion deploy@192.168.56.20` | ProxyJump for servers without public access. |
| T3270 | L3 | any | Reach 192.168.56.20 through jump host bastion as ivan | `ssh -J ivan@bastion ivan@192.168.56.20` | ProxyJump for servers without public access. |
| T3271 | L3 | any | Reach backup-host through jump host bastion as admin | `ssh -J admin@bastion admin@backup-host` | ProxyJump for servers without public access. |
| T3272 | L3 | any | Reach backup-host through jump host bastion as deploy | `ssh -J deploy@bastion deploy@backup-host` | ProxyJump for servers without public access. |
| T3273 | L3 | any | Reach backup-host through jump host bastion as ivan | `ssh -J ivan@bastion ivan@backup-host` | ProxyJump for servers without public access. |
| T3274 | L3 | any | Reach db1.lab.local through jump host bastion as admin | `ssh -J admin@bastion admin@db1.lab.local` | ProxyJump for servers without public access. |
| T3275 | L3 | any | Reach db1.lab.local through jump host bastion as deploy | `ssh -J deploy@bastion deploy@db1.lab.local` | ProxyJump for servers without public access. |
| T3276 | L3 | any | Reach db1.lab.local through jump host bastion as ivan | `ssh -J ivan@bastion ivan@db1.lab.local` | ProxyJump for servers without public access. |
| T3277 | L3 | any | Reach web1.lab.local through jump host bastion as admin | `ssh -J admin@bastion admin@web1.lab.local` | ProxyJump for servers without public access. |
| T3278 | L3 | any | Reach web1.lab.local through jump host bastion as deploy | `ssh -J deploy@bastion deploy@web1.lab.local` | ProxyJump for servers without public access. |
| T3279 | L3 | any | Reach web1.lab.local through jump host bastion as ivan | `ssh -J ivan@bastion ivan@web1.lab.local` | ProxyJump for servers without public access. |
| T3280 | L3 | any | Show effective sshd settings | `sudo sshd -T \| grep -E 'permitrootlogin\|passwordauthentication\|maxauthtries'` | SSH administration. |
| T3281 | L3 | any | Test sshd config syntax before reload | `sudo sshd -t` | SSH administration. |
