#!/usr/bin/env bash
# backup.sh - timestamped tar backup with retention and integrity check
# Usage: backup.sh <source_dir> <backup_dir> [keep_days]
set -euo pipefail

[[ $# -ge 2 ]] || { echo "Usage: $0 <source_dir> <backup_dir> [keep_days]" >&2; exit 2; }
src="$1"
dest="$2"
keep="${3:-7}"

[[ -d "$src" ]] || { echo "Source $src not found" >&2; exit 1; }
mkdir -p "$dest"

name="$(basename "$src")"
[[ "$name" == "/" ]] && name="root"
archive="${dest}/${name}-$(date +%Y%m%d-%H%M%S).tar.gz"

tar -czpf "$archive" -C "$(dirname "$src")" "$(basename "$src")"

if tar -tzf "$archive" >/dev/null; then
  echo "Backup OK: $archive ($(du -h "$archive" | cut -f1))"
else
  echo "Backup FAILED integrity check: $archive" >&2
  exit 1
fi

find "$dest" -maxdepth 1 -name "${name}-*.tar.gz" -mtime +"$keep" -print -delete
