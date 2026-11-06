# Bash scripting (12 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T0243 | L2 | any | Add a timestamp to every output line | `./job.sh \| while read -r l; do echo "$(date '+%F %T') $l"; done` | Building blocks for admin scripts. |
| T0244 | L2 | any | Check that a command exists | `command -v jq >/dev/null \|\| { echo 'jq missing'; exit 1; }` | Building blocks for admin scripts. |
| T0245 | L2 | any | Check the exit code of the last command | `echo $?` | Building blocks for admin scripts. |
| T0246 | L2 | any | Loop over all .log files | `for f in /var/log/*.log; do echo "$f"; done` | Building blocks for admin scripts. |
| T0247 | L2 | any | Make a script stop on errors and unset variables | `set -euo pipefail` | Building blocks for admin scripts. |
| T0248 | L2 | any | Read a file line by line | `while IFS= read -r line; do echo "$line"; done < file.txt` | Building blocks for admin scripts. |
| T0249 | L2 | any | Run a command only if the previous succeeded | `mkdir /tmp/x && cd /tmp/x` | Building blocks for admin scripts. |
| T0250 | L2 | any | Use a default value for an argument | `threshold="${1:-85}"` | Building blocks for admin scripts. |
| T0251 | L3 | any | Create a safe temporary file | `tmp=$(mktemp)` | Building blocks for admin scripts. |
| T0252 | L3 | any | Lint a script for common mistakes | `shellcheck script.sh` | Building blocks for admin scripts. |
| T0253 | L3 | any | Run a function on several hosts in parallel | `for h in web1 web2 db1; do ssh "$h" uptime & done; wait` | Building blocks for admin scripts. |
| T0254 | L3 | any | Run cleanup when the script exits | `trap 'rm -f "$tmp"' EXIT` | Building blocks for admin scripts. |
