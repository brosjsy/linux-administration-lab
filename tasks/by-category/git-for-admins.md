# Git for admins (12 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1481 | L1 | any | Clone the lab repository | `git clone https://github.com/brosjsy/linux-administration-lab.git` | Version control keeps a history of configs and scripts. |
| T1482 | L1 | any | Commit all changes with a message | `git add -A && git commit -m "Describe the change"` | Version control keeps a history of configs and scripts. |
| T1483 | L1 | any | Get the latest changes | `git pull` | Version control keeps a history of configs and scripts. |
| T1484 | L1 | any | Push commits to GitHub | `git push` | Version control keeps a history of configs and scripts. |
| T1485 | L1 | any | See what changed before committing | `git status && git diff` | Version control keeps a history of configs and scripts. |
| T1486 | L2 | any | Create and switch to a new branch | `git switch -c feature/hardening` | Version control keeps a history of configs and scripts. |
| T1487 | L2 | any | See who changed each line of a file | `git blame scripts/backup.sh` | Version control keeps a history of configs and scripts. |
| T1488 | L2 | any | Show the last 10 commits in one line each | `git log --oneline -10` | Version control keeps a history of configs and scripts. |
| T1489 | L2 | any | Store a config file in git with a backup copy | `cp /etc/nginx/nginx.conf configs/ && git add configs && git commit -m 'nginx config'` | Version control keeps a history of configs and scripts. |
| T1490 | L2 | any | Undo changes to one file | `git restore path/to/file` | Version control keeps a history of configs and scripts. |
| T1491 | L3 | any | Show what changed in /etc since the last commit | `sudo etckeeper vcs diff` | Version control keeps a history of configs and scripts. |
| T1492 | L3 | any | Track /etc changes with etckeeper | `sudo apt install etckeeper && sudo etckeeper init && sudo etckeeper commit 'baseline'` | Version control keeps a history of configs and scripts. |
