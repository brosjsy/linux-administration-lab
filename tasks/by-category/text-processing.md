# Text processing (15 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T4221 | L1 | any | Show line count, word count and size of a file | `wc -lwc file.txt` | Classic text tools used every day in logs and configs. |
| T4222 | L1 | any | Show the 3rd column of a space-separated file | `awk '{print $3}' file.txt` | Classic text tools used every day in logs and configs. |
| T4223 | L1 | any | Show unique lines and how often they appear | `sort file.txt \| uniq -c \| sort -rn` | Classic text tools used every day in logs and configs. |
| T4224 | L1 | any | Show usernames from /etc/passwd | `cut -d: -f1 /etc/passwd` | Classic text tools used every day in logs and configs. |
| T4225 | L2 | any | Compare two config files side by side | `diff -y --suppress-common-lines a.conf b.conf` | Classic text tools used every day in logs and configs. |
| T4226 | L2 | any | Convert Windows line endings to Linux | `sed -i 's/\r$//' script.sh` | Classic text tools used every day in logs and configs. |
| T4227 | L2 | any | Delete comment and empty lines from a config view | `grep -Ev '^\s*(#\|$)' /etc/ssh/sshd_config` | Classic text tools used every day in logs and configs. |
| T4228 | L2 | any | Pretty-print JSON | `jq . data.json` | Classic text tools used every day in logs and configs. |
| T4229 | L2 | any | Print lines 10 to 20 of a file | `sed -n '10,20p' file.txt` | Classic text tools used every day in logs and configs. |
| T4230 | L2 | any | Replace a word in a file in place with a backup | `sed -i.bak 's/old/new/g' file.conf` | Classic text tools used every day in logs and configs. |
| T4231 | L2 | any | Search recursively for a string in configs | `grep -Rn 'listen' /etc/nginx/` | Classic text tools used every day in logs and configs. |
| T4232 | L2 | any | Show non-printable characters in a file | `cat -A file.txt \| head` | Classic text tools used every day in logs and configs. |
| T4233 | L2 | any | Sum a column of numbers | `awk '{s+=$1} END {print s}' numbers.txt` | Classic text tools used every day in logs and configs. |
| T4234 | L3 | any | Extract a field from JSON | `jq -r '.items[].name' data.json` | Classic text tools used every day in logs and configs. |
| T4235 | L3 | any | Show lines that appear in file1 but not file2 | `comm -23 <(sort file1) <(sort file2)` | Classic text tools used every day in logs and configs. |
