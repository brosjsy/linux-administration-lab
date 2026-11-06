# Ansible part of the lab

Manage both lab servers (and any number of real ones) from one machine. Full explanation: [docs/17-ansible.md](../docs/17-ansible.md).

```bash
cd ansible
ansible all -m ping
ansible-playbook site.yml --check --diff     # dry run
ansible-playbook site.yml                    # apply
ansible-playbook playbooks/05-patching.yml   # monthly rolling updates
ansible-playbook playbooks/08-health-report.yml && cat reports/health.txt
```
Before real use: replace the example SSH keys in `group_vars/all.yml` and keep secrets in `ansible-vault`.
