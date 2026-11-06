#!/usr/bin/env bash
# user_onboard.sh - create users from a CSV file
# CSV format (no header): username,full name,group,ssh_public_key_file(optional)
# Usage: user_onboard.sh users.csv [--apply]   (dry-run unless --apply is given)
set -euo pipefail

[[ $# -ge 1 ]] || { echo "Usage: $0 users.csv [--apply]" >&2; exit 2; }
csv="$1"
apply="${2:-}"
[[ -r "$csv" ]] || { echo "Cannot read $csv" >&2; exit 2; }

run() {
  if [[ "$apply" == "--apply" ]]; then
    "$@"
  else
    echo "[dry-run] $*"
  fi
}

if [[ "$apply" == "--apply" && $EUID -ne 0 ]]; then
  echo "Run with sudo to apply changes" >&2
  exit 1
fi

while IFS=, read -r user fullname group keyfile; do
  [[ -z "$user" || "$user" == \#* ]] && continue
  if ! [[ "$user" =~ ^[a-z_][a-z0-9_-]{0,31}$ ]]; then
    echo "Skipping invalid username: $user" >&2
    continue
  fi
  if id "$user" >/dev/null 2>&1; then
    echo "User $user already exists, skipping"
    continue
  fi
  getent group "$group" >/dev/null 2>&1 || run groupadd "$group"
  run useradd -m -s /bin/bash -c "$fullname" -G "$group" "$user"
  run passwd -d "$user"
  run chage -d 0 "$user"
  if [[ -n "${keyfile:-}" && -r "$keyfile" ]]; then
    run install -d -m 700 -o "$user" -g "$user" "/home/$user/.ssh"
    run install -m 600 -o "$user" -g "$user" "$keyfile" "/home/$user/.ssh/authorized_keys"
  fi
  echo "Prepared user $user ($fullname) in group $group"
done < "$csv"
