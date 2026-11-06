# KB-002 How to connect to a Linux server with an SSH key

1. Create a key (once): `ssh-keygen -t ed25519`
2. Send **only** the public key (`~/.ssh/id_ed25519.pub`) to support. Never send the private key.
3. After support confirms, connect: `ssh username@server`
4. Windows: use the built-in OpenSSH client in PowerShell, same commands.

**Error `Permission denied (publickey)`:** check you use the right username and that the key file is the one you sent (`ssh -v` shows which key is offered).
