# 17. Ansible: managing many servers at once

Level: intermediate to professional

Ansible is the tool admins use to control tens or thousands of servers from one machine.
It connects over **SSH**, needs **no agent** on the servers, and describes the wanted state in **YAML playbooks**.
Similar tools: SaltStack, Puppet, Chef. In Russian companies Ansible is the most common.

## Key ideas
| Term | Meaning |
|------|---------|
| Control node | the machine where you run Ansible |
| Managed nodes | the servers you control |
| Inventory | list of servers and groups (`inventory.ini`) |
| Module | one action: `apt`, `user`, `copy`, `service`, `cron`, `lineinfile` |
| Playbook | ordered list of tasks for groups of hosts |
| Role | reusable bundle of tasks, templates and handlers |
| Idempotent | running twice changes nothing the second time |
| Handler | task that runs only when notified, e.g. restart sshd after config change |

## Setup
```bash
sudo apt install ansible        # or: pip install ansible
cd ansible
ansible all -m ping              # test connection to every server
ansible web -m shell -a "uptime" # ad-hoc command on the web group
ansible all -m setup -a "filter=ansible_distribution*"   # facts
```

## Playbooks in this lab
| Playbook | Scenario |
|----------|----------|
| `01-baseline.yml` | Same base packages, timezone and time sync on every server |
| `02-users.yml` | Create the support team accounts with SSH keys and limited sudo |
| `03-ssh-hardening.yml` | Push a hardened SSH config, validate it, reload only if changed |
| `04-firewall.yml` | ufw on Ubuntu, firewalld on Rocky, from one playbook |
| `05-patching.yml` | Rolling updates, one server at a time, reboot only if needed |
| `06-cron-jobs.yml` | Deploy scripts and cron jobs to all servers |
| `07-nginx.yml` | Install Nginx with a templated site and health check |
| `08-health-report.yml` | Collect disk, memory and uptime from every server into one report |
| `site.yml` | Runs everything in order |

## Run safely
```bash
ansible-playbook playbooks/03-ssh-hardening.yml --check --diff   # dry run, show changes
ansible-playbook playbooks/05-patching.yml --limit web           # only the web group
ansible-playbook site.yml --tags ssh                             # only tagged tasks
ansible-vault create group_vars/all/vault.yml                    # encrypt secrets
```

## Scenarios
1. **New engineer joins:** add them to `support_users` in `group_vars/all.yml`, run `02-users.yml`. Done on every server in one minute.
2. **Security asks to disable SSH passwords everywhere:** run `03-ssh-hardening.yml --check --diff`, review, then run for real.
3. **Monthly patching window:** `05-patching.yml` updates servers one by one (`serial: 1`) so the service stays up.
4. **"How much disk is left on all servers?"** run `08-health-report.yml`, read `reports/health.txt`.
