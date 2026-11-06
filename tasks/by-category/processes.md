# Processes (92 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T3052 | L1 | any | Find PIDs of backup.sh | `pgrep -a backup.sh` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3053 | L1 | any | Find PIDs of dockerd | `pgrep -a dockerd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3054 | L1 | any | Find PIDs of java | `pgrep -a java` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3055 | L1 | any | Find PIDs of mysqld | `pgrep -a mysqld` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3056 | L1 | any | Find PIDs of nginx | `pgrep -a nginx` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3057 | L1 | any | Find PIDs of node | `pgrep -a node` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3058 | L1 | any | Find PIDs of php-fpm | `pgrep -a php-fpm` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3059 | L1 | any | Find PIDs of postgres | `pgrep -a postgres` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3060 | L1 | any | Find PIDs of python3 | `pgrep -a python3` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3061 | L1 | any | Find PIDs of rsync | `pgrep -a rsync` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3062 | L1 | any | Show the top 10 CPU consumers | `ps aux --sort=-%cpu \| head -11` | Performance and process basics. |
| T3063 | L1 | any | Show the top 10 memory consumers | `ps aux --sort=-%mem \| head -11` | Performance and process basics. |
| T3064 | L2 | any | Find zombie processes | `ps -eo stat,pid,ppid,cmd \| awk '$1 ~ /Z/'` | Performance and process basics. |
| T3065 | L2 | any | Gracefully stop all backup.sh processes | `sudo pkill -TERM backup.sh` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3066 | L2 | any | Gracefully stop all dockerd processes | `sudo pkill -TERM dockerd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3067 | L2 | any | Gracefully stop all java processes | `sudo pkill -TERM java` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3068 | L2 | any | Gracefully stop all mysqld processes | `sudo pkill -TERM mysqld` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3069 | L2 | any | Gracefully stop all nginx processes | `sudo pkill -TERM nginx` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3070 | L2 | any | Gracefully stop all node processes | `sudo pkill -TERM node` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3071 | L2 | any | Gracefully stop all php-fpm processes | `sudo pkill -TERM php-fpm` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3072 | L2 | any | Gracefully stop all postgres processes | `sudo pkill -TERM postgres` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3073 | L2 | any | Gracefully stop all python3 processes | `sudo pkill -TERM python3` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3074 | L2 | any | Gracefully stop all rsync processes | `sudo pkill -TERM rsync` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3075 | L2 | any | Run a long command that survives logout | `nohup ./long_job.sh > job.log 2>&1 &` | Performance and process basics. |
| T3076 | L2 | any | Show CPU and memory of backup.sh processes | `ps -C backup.sh -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3077 | L2 | any | Show CPU and memory of dockerd processes | `ps -C dockerd -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3078 | L2 | any | Show CPU and memory of java processes | `ps -C java -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3079 | L2 | any | Show CPU and memory of mysqld processes | `ps -C mysqld -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3080 | L2 | any | Show CPU and memory of nginx processes | `ps -C nginx -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3081 | L2 | any | Show CPU and memory of node processes | `ps -C node -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3082 | L2 | any | Show CPU and memory of php-fpm processes | `ps -C php-fpm -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3083 | L2 | any | Show CPU and memory of postgres processes | `ps -C postgres -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3084 | L2 | any | Show CPU and memory of python3 processes | `ps -C python3 -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3085 | L2 | any | Show CPU and memory of rsync processes | `ps -C rsync -o pid,user,%cpu,%mem,etime,cmd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3086 | L2 | any | Show load average and number of CPUs | `uptime; nproc` | Performance and process basics. |
| T3087 | L2 | any | Show the process tree | `pstree -p \| head -50` | Performance and process basics. |
| T3088 | L2 | any | Start a persistent terminal session | `tmux new -s work` | Performance and process basics. |
| T3089 | L3 | any | Count open file descriptors of backup.sh | `for p in $(pgrep backup.sh); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3090 | L3 | any | Count open file descriptors of dockerd | `for p in $(pgrep dockerd); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3091 | L3 | any | Count open file descriptors of java | `for p in $(pgrep java); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3092 | L3 | any | Count open file descriptors of mysqld | `for p in $(pgrep mysqld); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3093 | L3 | any | Count open file descriptors of nginx | `for p in $(pgrep nginx); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3094 | L3 | any | Count open file descriptors of node | `for p in $(pgrep node); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3095 | L3 | any | Count open file descriptors of php-fpm | `for p in $(pgrep php-fpm); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3096 | L3 | any | Count open file descriptors of postgres | `for p in $(pgrep postgres); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3097 | L3 | any | Count open file descriptors of python3 | `for p in $(pgrep python3); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3098 | L3 | any | Count open file descriptors of rsync | `for p in $(pgrep rsync); do echo "$p $(sudo ls /proc/$p/fd \| wc -l)"; done` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3099 | L3 | any | Find processes killed by the OOM killer | `journalctl -k \| grep -i -E 'out of memory\|killed process'` | Performance and process basics. |
| T3100 | L3 | any | Force kill hung backup.sh processes | `sudo pkill -KILL backup.sh` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3101 | L3 | any | Force kill hung dockerd processes | `sudo pkill -KILL dockerd` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3102 | L3 | any | Force kill hung java processes | `sudo pkill -KILL java` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3103 | L3 | any | Force kill hung mysqld processes | `sudo pkill -KILL mysqld` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3104 | L3 | any | Force kill hung nginx processes | `sudo pkill -KILL nginx` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3105 | L3 | any | Force kill hung node processes | `sudo pkill -KILL node` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3106 | L3 | any | Force kill hung php-fpm processes | `sudo pkill -KILL php-fpm` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3107 | L3 | any | Force kill hung postgres processes | `sudo pkill -KILL postgres` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3108 | L3 | any | Force kill hung python3 processes | `sudo pkill -KILL python3` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3109 | L3 | any | Force kill hung rsync processes | `sudo pkill -KILL rsync` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3110 | L3 | any | Lower the priority of running backup.sh | `sudo renice +10 -p $(pgrep backup.sh \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3111 | L3 | any | Lower the priority of running dockerd | `sudo renice +10 -p $(pgrep dockerd \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3112 | L3 | any | Lower the priority of running java | `sudo renice +10 -p $(pgrep java \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3113 | L3 | any | Lower the priority of running mysqld | `sudo renice +10 -p $(pgrep mysqld \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3114 | L3 | any | Lower the priority of running nginx | `sudo renice +10 -p $(pgrep nginx \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3115 | L3 | any | Lower the priority of running node | `sudo renice +10 -p $(pgrep node \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3116 | L3 | any | Lower the priority of running php-fpm | `sudo renice +10 -p $(pgrep php-fpm \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3117 | L3 | any | Lower the priority of running postgres | `sudo renice +10 -p $(pgrep postgres \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3118 | L3 | any | Lower the priority of running python3 | `sudo renice +10 -p $(pgrep python3 \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3119 | L3 | any | Lower the priority of running rsync | `sudo renice +10 -p $(pgrep rsync \| tr '\n' ' ')` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3120 | L3 | any | Show disk utilisation and latency | `iostat -xz 1 3` | Performance and process basics. |
| T3121 | L3 | any | Show files opened by backup.sh | `sudo lsof -c backup.sh \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3122 | L3 | any | Show files opened by dockerd | `sudo lsof -c dockerd \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3123 | L3 | any | Show files opened by java | `sudo lsof -c java \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3124 | L3 | any | Show files opened by mysqld | `sudo lsof -c mysqld \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3125 | L3 | any | Show files opened by nginx | `sudo lsof -c nginx \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3126 | L3 | any | Show files opened by node | `sudo lsof -c node \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3127 | L3 | any | Show files opened by php-fpm | `sudo lsof -c php-fpm \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3128 | L3 | any | Show files opened by postgres | `sudo lsof -c postgres \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3129 | L3 | any | Show files opened by python3 | `sudo lsof -c python3 \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3130 | L3 | any | Show files opened by rsync | `sudo lsof -c rsync \| head -30` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3131 | L3 | any | Show memory, swap and IO wait every second | `vmstat 1 5` | Performance and process basics. |
| T3132 | L3 | any | Show per-CPU usage every second, 3 times | `mpstat -P ALL 1 3` | Performance and process basics. |
| T3133 | L3 | any | Show per-process CPU, memory and disk every second | `pidstat -urd 1 5` | Performance and process basics. |
| T3134 | L4 | any | Trace system calls of backup.sh for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o backup.sh) -o /tmp/backup.sh.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3135 | L4 | any | Trace system calls of dockerd for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o dockerd) -o /tmp/dockerd.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3136 | L4 | any | Trace system calls of java for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o java) -o /tmp/java.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3137 | L4 | any | Trace system calls of mysqld for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o mysqld) -o /tmp/mysqld.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3138 | L4 | any | Trace system calls of nginx for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o nginx) -o /tmp/nginx.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3139 | L4 | any | Trace system calls of node for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o node) -o /tmp/node.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3140 | L4 | any | Trace system calls of php-fpm for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o php-fpm) -o /tmp/php-fpm.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3141 | L4 | any | Trace system calls of postgres for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o postgres) -o /tmp/postgres.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3142 | L4 | any | Trace system calls of python3 for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o python3) -o /tmp/python3.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
| T3143 | L4 | any | Trace system calls of rsync for 10 seconds | `sudo timeout 10 strace -f -p $(pgrep -o rsync) -o /tmp/rsync.strace` | Signals: TERM asks politely, KILL cannot be ignored. |
