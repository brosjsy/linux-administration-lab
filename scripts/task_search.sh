#!/usr/bin/env bash
# task_search.sh - search the Linux task library from the terminal
# Usage: task_search.sh [-l L1|L2|L3|L4] [-c category] [-d debian|rhel] [-n max] word [word...]
# All words must match (case-insensitive) in the task, command, explanation, category or tags.
# Examples:
#   task_search.sh nginx reload
#   task_search.sh -l L3 -c cron backup
#   task_search.sh -d rhel firewall 443
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
db="${TASKS_TSV:-$here/../tasks/tasks.tsv}"
[[ -r "$db" ]] || { echo "Task file not found: $db (run: python3 tools/generate_tasks.py)" >&2; exit 2; }

level="" category="" distro="" max=30
words=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    -l) level="${2:-}"; shift 2 ;;
    -c) category="${2:-}"; shift 2 ;;
    -d) distro="${2:-}"; shift 2 ;;
    -n) max="${2:-}"; shift 2 ;;
    -h|--help) sed -n '2,9p' "${BASH_SOURCE[0]}"; exit 0 ;;
    -*) echo "Unknown option $1. Use -h for help." >&2; exit 2 ;;
    *) words+=("$1"); shift ;;
  esac
done
[[ ${#words[@]} -ge 1 || -n "$level$category$distro" ]] || { sed -n '2,9p' "${BASH_SOURCE[0]}"; exit 2; }
[[ "$max" =~ ^[0-9]+$ ]] || { echo "-n needs a number" >&2; exit 2; }

query="${words[*]:-}"
use_color=0
[[ -t 1 ]] && use_color=1

awk -F'\t' -v words="$query" -v level="$level" -v cat="$category" -v distro="$distro" -v max="$max" -v color="$use_color" '
BEGIN {
  n = split(tolower(words), w, " ")
  b = color ? "\033[1m" : ""; g = color ? "\033[32m" : ""; d = color ? "\033[2m" : ""; r = color ? "\033[0m" : ""
  found = 0
}
{
  if (level != "" && $2 != level) next
  if (cat != "" && index(tolower($3), tolower(cat)) == 0) next
  if (distro != "" && $4 != distro && $4 != "any") next
  hay = tolower($3 " " $5 " " $6 " " $7 " " $8)
  for (i = 1; i <= n; i++) if (index(hay, w[i]) == 0) next
  found++
  if (found <= max) {
    printf "%s%s [%s] %s%s  %s(%s%s)%s\n", b, $1, $2, $5, r, d, $3, ($4 == "any" ? "" : ", " $4), r
    printf "    %s%s%s\n", g, $6, r
    printf "    %s%s%s\n\n", d, $7, r
  }
}
END {
  if (found == 0) { print "No matches." ; exit 1 }
  if (found > max) printf "%d matches, showing %d. Narrow the search or use -n.\n", found, max
  else printf "%d match%s.\n", found, (found == 1 ? "" : "es")
}' "$db"
