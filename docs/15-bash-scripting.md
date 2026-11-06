# 15. Bash scripting

Rules I follow in `scripts/`:
- `#!/usr/bin/env bash` and `set -euo pipefail`
- quote variables, use functions, check required commands
- meaningful exit codes (0 OK, 1 alert/error, 2 usage)
- `--dry-run` for anything that changes the system
- pass ShellCheck

```bash
#!/usr/bin/env bash
set -euo pipefail
usage() { echo "Usage: $0 <threshold>"; exit 2; }
[[ $# -eq 1 ]] || usage
for fs in $(df --output=target -x tmpfs | tail -n +2); do
  echo "checking $fs"
done
```
