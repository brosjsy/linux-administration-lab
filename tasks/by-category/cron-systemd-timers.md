# Cron: systemd timers (40 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T0919 | L3 | any | systemd timer equivalent of cron '*/1 * * * *' (every 1 minute) | `OnCalendar=*:0/1` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0920 | L3 | any | systemd timer equivalent of cron '*/10 * * * *' (every 10 minutes) | `OnCalendar=*:0/10` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0921 | L3 | any | systemd timer equivalent of cron '*/15 * * * *' (every 15 minutes) | `OnCalendar=*:0/15` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0922 | L3 | any | systemd timer equivalent of cron '*/2 * * * *' (every 2 minutes) | `OnCalendar=*:0/2` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0923 | L3 | any | systemd timer equivalent of cron '*/20 * * * *' (every 20 minutes) | `OnCalendar=*:0/20` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0924 | L3 | any | systemd timer equivalent of cron '*/3 * * * *' (every 3 minutes) | `OnCalendar=*:0/3` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0925 | L3 | any | systemd timer equivalent of cron '*/30 * * * *' (every 30 minutes) | `OnCalendar=*:0/30` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0926 | L3 | any | systemd timer equivalent of cron '*/5 * * * *' (every 5 minutes) | `OnCalendar=*:0/5` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0927 | L3 | any | systemd timer equivalent of cron '0 */12 * * *' (every 12 hours) | `OnCalendar=0/12:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0928 | L3 | any | systemd timer equivalent of cron '0 */2 * * *' (every 2 hours) | `OnCalendar=0/2:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0929 | L3 | any | systemd timer equivalent of cron '0 */3 * * *' (every 3 hours) | `OnCalendar=0/3:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0930 | L3 | any | systemd timer equivalent of cron '0 */4 * * *' (every 4 hours) | `OnCalendar=0/4:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0931 | L3 | any | systemd timer equivalent of cron '0 */6 * * *' (every 6 hours) | `OnCalendar=0/6:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0932 | L3 | any | systemd timer equivalent of cron '0 */8 * * *' (every 8 hours) | `OnCalendar=0/8:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0933 | L3 | any | systemd timer equivalent of cron '0 0 * * *' (every day at 00:00) | `OnCalendar=*-*-* 00:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0934 | L3 | any | systemd timer equivalent of cron '0 1 * * *' (every day at 01:00) | `OnCalendar=*-*-* 01:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0935 | L3 | any | systemd timer equivalent of cron '0 12 * * *' (every day at 12:00) | `OnCalendar=*-*-* 12:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0936 | L3 | any | systemd timer equivalent of cron '0 18 * * *' (every day at 18:00) | `OnCalendar=*-*-* 18:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0937 | L3 | any | systemd timer equivalent of cron '0 2 * * *' (every day at 02:00) | `OnCalendar=*-*-* 02:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0938 | L3 | any | systemd timer equivalent of cron '0 22 * * *' (every day at 22:00) | `OnCalendar=*-*-* 22:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0939 | L3 | any | systemd timer equivalent of cron '0 23 * * *' (every day at 23:00) | `OnCalendar=*-*-* 23:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0940 | L3 | any | systemd timer equivalent of cron '0 3 * * *' (every day at 03:00) | `OnCalendar=*-*-* 03:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0941 | L3 | any | systemd timer equivalent of cron '0 4 * * *' (every day at 04:00) | `OnCalendar=*-*-* 04:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0942 | L3 | any | systemd timer equivalent of cron '0 6 * * *' (every day at 06:00) | `OnCalendar=*-*-* 06:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0943 | L3 | any | systemd timer equivalent of cron '0 7 * * *' (every day at 07:00) | `OnCalendar=*-*-* 07:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0944 | L3 | any | systemd timer equivalent of cron '0 8 * * *' (every day at 08:00) | `OnCalendar=*-*-* 08:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0945 | L3 | any | systemd timer equivalent of cron '0 9 * * *' (every day at 09:00) | `OnCalendar=*-*-* 09:00:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0946 | L3 | any | systemd timer equivalent of cron '30 0 * * *' (every day at 00:30) | `OnCalendar=*-*-* 00:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0947 | L3 | any | systemd timer equivalent of cron '30 1 * * *' (every day at 01:30) | `OnCalendar=*-*-* 01:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0948 | L3 | any | systemd timer equivalent of cron '30 12 * * *' (every day at 12:30) | `OnCalendar=*-*-* 12:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0949 | L3 | any | systemd timer equivalent of cron '30 18 * * *' (every day at 18:30) | `OnCalendar=*-*-* 18:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0950 | L3 | any | systemd timer equivalent of cron '30 2 * * *' (every day at 02:30) | `OnCalendar=*-*-* 02:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0951 | L3 | any | systemd timer equivalent of cron '30 22 * * *' (every day at 22:30) | `OnCalendar=*-*-* 22:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0952 | L3 | any | systemd timer equivalent of cron '30 23 * * *' (every day at 23:30) | `OnCalendar=*-*-* 23:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0953 | L3 | any | systemd timer equivalent of cron '30 3 * * *' (every day at 03:30) | `OnCalendar=*-*-* 03:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0954 | L3 | any | systemd timer equivalent of cron '30 4 * * *' (every day at 04:30) | `OnCalendar=*-*-* 04:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0955 | L3 | any | systemd timer equivalent of cron '30 6 * * *' (every day at 06:30) | `OnCalendar=*-*-* 06:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0956 | L3 | any | systemd timer equivalent of cron '30 7 * * *' (every day at 07:30) | `OnCalendar=*-*-* 07:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0957 | L3 | any | systemd timer equivalent of cron '30 8 * * *' (every day at 08:30) | `OnCalendar=*-*-* 08:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
| T0958 | L3 | any | systemd timer equivalent of cron '30 9 * * *' (every day at 09:30) | `OnCalendar=*-*-* 09:30:00` | Put in [Timer] of a .timer unit; check with systemd-analyze calendar. |
