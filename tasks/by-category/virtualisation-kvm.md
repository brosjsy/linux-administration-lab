# Virtualisation (KVM) (70 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T4890 | L2 | any | Vagrant: Connect to lab VM rocky-srv | `vagrant ssh rocky-srv` | Run from the lab/ directory. |
| T4891 | L2 | any | Vagrant: Connect to lab VM ubuntu-srv | `vagrant ssh ubuntu-srv` | Run from the lab/ directory. |
| T4892 | L2 | any | Vagrant: Delete lab VM rocky-srv | `vagrant destroy -f rocky-srv` | Run from the lab/ directory. |
| T4893 | L2 | any | Vagrant: Delete lab VM ubuntu-srv | `vagrant destroy -f ubuntu-srv` | Run from the lab/ directory. |
| T4894 | L2 | any | Vagrant: Re-run provisioning on lab VM rocky-srv | `vagrant reload --provision rocky-srv` | Run from the lab/ directory. |
| T4895 | L2 | any | Vagrant: Re-run provisioning on lab VM ubuntu-srv | `vagrant reload --provision ubuntu-srv` | Run from the lab/ directory. |
| T4896 | L2 | any | Vagrant: Start lab VM rocky-srv | `vagrant up rocky-srv` | Run from the lab/ directory. |
| T4897 | L2 | any | Vagrant: Start lab VM ubuntu-srv | `vagrant up ubuntu-srv` | Run from the lab/ directory. |
| T4898 | L2 | any | Vagrant: Stop lab VM rocky-srv | `vagrant halt rocky-srv` | Run from the lab/ directory. |
| T4899 | L2 | any | Vagrant: Stop lab VM ubuntu-srv | `vagrant halt ubuntu-srv` | Run from the lab/ directory. |
| T4900 | L3 | any | Force power off VM backup1 | `virsh destroy backup1` | libvirt management; virt-manager is the GUI. |
| T4901 | L3 | any | Force power off VM db1 | `virsh destroy db1` | libvirt management; virt-manager is the GUI. |
| T4902 | L3 | any | Force power off VM test-rocky | `virsh destroy test-rocky` | libvirt management; virt-manager is the GUI. |
| T4903 | L3 | any | Force power off VM test-ubuntu | `virsh destroy test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4904 | L3 | any | Force power off VM web1 | `virsh destroy web1` | libvirt management; virt-manager is the GUI. |
| T4905 | L3 | any | Force power off VM web2 | `virsh destroy web2` | libvirt management; virt-manager is the GUI. |
| T4906 | L3 | any | Gracefully shut down VM backup1 | `virsh shutdown backup1` | libvirt management; virt-manager is the GUI. |
| T4907 | L3 | any | Gracefully shut down VM db1 | `virsh shutdown db1` | libvirt management; virt-manager is the GUI. |
| T4908 | L3 | any | Gracefully shut down VM test-rocky | `virsh shutdown test-rocky` | libvirt management; virt-manager is the GUI. |
| T4909 | L3 | any | Gracefully shut down VM test-ubuntu | `virsh shutdown test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4910 | L3 | any | Gracefully shut down VM web1 | `virsh shutdown web1` | libvirt management; virt-manager is the GUI. |
| T4911 | L3 | any | Gracefully shut down VM web2 | `virsh shutdown web2` | libvirt management; virt-manager is the GUI. |
| T4912 | L3 | any | Open the text console of VM backup1 | `virsh console backup1` | libvirt management; virt-manager is the GUI. |
| T4913 | L3 | any | Open the text console of VM db1 | `virsh console db1` | libvirt management; virt-manager is the GUI. |
| T4914 | L3 | any | Open the text console of VM test-rocky | `virsh console test-rocky` | libvirt management; virt-manager is the GUI. |
| T4915 | L3 | any | Open the text console of VM test-ubuntu | `virsh console test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4916 | L3 | any | Open the text console of VM web1 | `virsh console web1` | libvirt management; virt-manager is the GUI. |
| T4917 | L3 | any | Open the text console of VM web2 | `virsh console web2` | libvirt management; virt-manager is the GUI. |
| T4918 | L3 | any | Show CPU, memory and state of VM backup1 | `virsh dominfo backup1` | libvirt management; virt-manager is the GUI. |
| T4919 | L3 | any | Show CPU, memory and state of VM db1 | `virsh dominfo db1` | libvirt management; virt-manager is the GUI. |
| T4920 | L3 | any | Show CPU, memory and state of VM test-rocky | `virsh dominfo test-rocky` | libvirt management; virt-manager is the GUI. |
| T4921 | L3 | any | Show CPU, memory and state of VM test-ubuntu | `virsh dominfo test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4922 | L3 | any | Show CPU, memory and state of VM web1 | `virsh dominfo web1` | libvirt management; virt-manager is the GUI. |
| T4923 | L3 | any | Show CPU, memory and state of VM web2 | `virsh dominfo web2` | libvirt management; virt-manager is the GUI. |
| T4924 | L3 | any | Show IP addresses of VM backup1 | `virsh domifaddr backup1` | libvirt management; virt-manager is the GUI. |
| T4925 | L3 | any | Show IP addresses of VM db1 | `virsh domifaddr db1` | libvirt management; virt-manager is the GUI. |
| T4926 | L3 | any | Show IP addresses of VM test-rocky | `virsh domifaddr test-rocky` | libvirt management; virt-manager is the GUI. |
| T4927 | L3 | any | Show IP addresses of VM test-ubuntu | `virsh domifaddr test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4928 | L3 | any | Show IP addresses of VM web1 | `virsh domifaddr web1` | libvirt management; virt-manager is the GUI. |
| T4929 | L3 | any | Show IP addresses of VM web2 | `virsh domifaddr web2` | libvirt management; virt-manager is the GUI. |
| T4930 | L3 | any | Show disks of VM backup1 | `virsh domblklist backup1` | libvirt management; virt-manager is the GUI. |
| T4931 | L3 | any | Show disks of VM db1 | `virsh domblklist db1` | libvirt management; virt-manager is the GUI. |
| T4932 | L3 | any | Show disks of VM test-rocky | `virsh domblklist test-rocky` | libvirt management; virt-manager is the GUI. |
| T4933 | L3 | any | Show disks of VM test-ubuntu | `virsh domblklist test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4934 | L3 | any | Show disks of VM web1 | `virsh domblklist web1` | libvirt management; virt-manager is the GUI. |
| T4935 | L3 | any | Show disks of VM web2 | `virsh domblklist web2` | libvirt management; virt-manager is the GUI. |
| T4936 | L3 | any | Start VM backup1 automatically at host boot | `virsh autostart backup1` | libvirt management; virt-manager is the GUI. |
| T4937 | L3 | any | Start VM db1 automatically at host boot | `virsh autostart db1` | libvirt management; virt-manager is the GUI. |
| T4938 | L3 | any | Start VM test-rocky automatically at host boot | `virsh autostart test-rocky` | libvirt management; virt-manager is the GUI. |
| T4939 | L3 | any | Start VM test-ubuntu automatically at host boot | `virsh autostart test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4940 | L3 | any | Start VM web1 automatically at host boot | `virsh autostart web1` | libvirt management; virt-manager is the GUI. |
| T4941 | L3 | any | Start VM web2 automatically at host boot | `virsh autostart web2` | libvirt management; virt-manager is the GUI. |
| T4942 | L3 | any | Start the KVM virtual machine backup1 | `virsh start backup1` | libvirt management; virt-manager is the GUI. |
| T4943 | L3 | any | Start the KVM virtual machine db1 | `virsh start db1` | libvirt management; virt-manager is the GUI. |
| T4944 | L3 | any | Start the KVM virtual machine test-rocky | `virsh start test-rocky` | libvirt management; virt-manager is the GUI. |
| T4945 | L3 | any | Start the KVM virtual machine test-ubuntu | `virsh start test-ubuntu` | libvirt management; virt-manager is the GUI. |
| T4946 | L3 | any | Start the KVM virtual machine web1 | `virsh start web1` | libvirt management; virt-manager is the GUI. |
| T4947 | L3 | any | Start the KVM virtual machine web2 | `virsh start web2` | libvirt management; virt-manager is the GUI. |
| T4948 | L4 | any | Revert VM backup1 to its last snapshot | `virsh snapshot-revert backup1 --current` | libvirt management; virt-manager is the GUI. |
| T4949 | L4 | any | Revert VM db1 to its last snapshot | `virsh snapshot-revert db1 --current` | libvirt management; virt-manager is the GUI. |
| T4950 | L4 | any | Revert VM test-rocky to its last snapshot | `virsh snapshot-revert test-rocky --current` | libvirt management; virt-manager is the GUI. |
| T4951 | L4 | any | Revert VM test-ubuntu to its last snapshot | `virsh snapshot-revert test-ubuntu --current` | libvirt management; virt-manager is the GUI. |
| T4952 | L4 | any | Revert VM web1 to its last snapshot | `virsh snapshot-revert web1 --current` | libvirt management; virt-manager is the GUI. |
| T4953 | L4 | any | Revert VM web2 to its last snapshot | `virsh snapshot-revert web2 --current` | libvirt management; virt-manager is the GUI. |
| T4954 | L4 | any | Take a snapshot of VM backup1 before patching | `virsh snapshot-create-as backup1 pre-patch-$(date +%F)` | libvirt management; virt-manager is the GUI. |
| T4955 | L4 | any | Take a snapshot of VM db1 before patching | `virsh snapshot-create-as db1 pre-patch-$(date +%F)` | libvirt management; virt-manager is the GUI. |
| T4956 | L4 | any | Take a snapshot of VM test-rocky before patching | `virsh snapshot-create-as test-rocky pre-patch-$(date +%F)` | libvirt management; virt-manager is the GUI. |
| T4957 | L4 | any | Take a snapshot of VM test-ubuntu before patching | `virsh snapshot-create-as test-ubuntu pre-patch-$(date +%F)` | libvirt management; virt-manager is the GUI. |
| T4958 | L4 | any | Take a snapshot of VM web1 before patching | `virsh snapshot-create-as web1 pre-patch-$(date +%F)` | libvirt management; virt-manager is the GUI. |
| T4959 | L4 | any | Take a snapshot of VM web2 before patching | `virsh snapshot-create-as web2 pre-patch-$(date +%F)` | libvirt management; virt-manager is the GUI. |
