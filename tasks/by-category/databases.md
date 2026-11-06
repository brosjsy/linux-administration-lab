# Databases (69 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T0959 | L2 | any | MariaDB: back up database analytics | `sudo mysqldump --single-transaction analytics \| gzip > /srv/backups/analytics-$(date +%F).sql.gz` | --single-transaction avoids locking InnoDB tables. |
| T0960 | L2 | any | MariaDB: back up database appdb | `sudo mysqldump --single-transaction appdb \| gzip > /srv/backups/appdb-$(date +%F).sql.gz` | --single-transaction avoids locking InnoDB tables. |
| T0961 | L2 | any | MariaDB: back up database crm | `sudo mysqldump --single-transaction crm \| gzip > /srv/backups/crm-$(date +%F).sql.gz` | --single-transaction avoids locking InnoDB tables. |
| T0962 | L2 | any | MariaDB: back up database shop | `sudo mysqldump --single-transaction shop \| gzip > /srv/backups/shop-$(date +%F).sql.gz` | --single-transaction avoids locking InnoDB tables. |
| T0963 | L2 | any | MariaDB: back up database wiki | `sudo mysqldump --single-transaction wiki \| gzip > /srv/backups/wiki-$(date +%F).sql.gz` | --single-transaction avoids locking InnoDB tables. |
| T0964 | L2 | any | MariaDB: back up database zabbix | `sudo mysqldump --single-transaction zabbix \| gzip > /srv/backups/zabbix-$(date +%F).sql.gz` | --single-transaction avoids locking InnoDB tables. |
| T0965 | L2 | any | MariaDB: create database analytics and user analytics_user | `sudo mysql -e "CREATE DATABASE analytics; CREATE USER 'analytics_user'@'localhost' IDENTIFIED BY 'ChangeMe!'; GRANT ALL ON analytics.* TO 'analytics_user'@'localhost';"` | Change the password immediately. |
| T0966 | L2 | any | MariaDB: create database appdb and user appdb_user | `sudo mysql -e "CREATE DATABASE appdb; CREATE USER 'appdb_user'@'localhost' IDENTIFIED BY 'ChangeMe!'; GRANT ALL ON appdb.* TO 'appdb_user'@'localhost';"` | Change the password immediately. |
| T0967 | L2 | any | MariaDB: create database crm and user crm_user | `sudo mysql -e "CREATE DATABASE crm; CREATE USER 'crm_user'@'localhost' IDENTIFIED BY 'ChangeMe!'; GRANT ALL ON crm.* TO 'crm_user'@'localhost';"` | Change the password immediately. |
| T0968 | L2 | any | MariaDB: create database shop and user shop_user | `sudo mysql -e "CREATE DATABASE shop; CREATE USER 'shop_user'@'localhost' IDENTIFIED BY 'ChangeMe!'; GRANT ALL ON shop.* TO 'shop_user'@'localhost';"` | Change the password immediately. |
| T0969 | L2 | any | MariaDB: create database wiki and user wiki_user | `sudo mysql -e "CREATE DATABASE wiki; CREATE USER 'wiki_user'@'localhost' IDENTIFIED BY 'ChangeMe!'; GRANT ALL ON wiki.* TO 'wiki_user'@'localhost';"` | Change the password immediately. |
| T0970 | L2 | any | MariaDB: create database zabbix and user zabbix_user | `sudo mysql -e "CREATE DATABASE zabbix; CREATE USER 'zabbix_user'@'localhost' IDENTIFIED BY 'ChangeMe!'; GRANT ALL ON zabbix.* TO 'zabbix_user'@'localhost';"` | Change the password immediately. |
| T0971 | L2 | any | MariaDB: list databases | `sudo mysql -e 'SHOW DATABASES;'` | Database administration basics for Linux admins. |
| T0972 | L2 | any | MariaDB: secure a fresh installation | `sudo mysql_secure_installation` | Database administration basics for Linux admins. |
| T0973 | L2 | any | MariaDB: show table sizes in analytics | `sudo mysql -e "SELECT table_name, ROUND((data_length+index_length)/1024/1024,1) MB FROM information_schema.tables WHERE table_schema='analytics' ORDER BY MB DESC;"` | Biggest tables first. |
| T0974 | L2 | any | MariaDB: show table sizes in appdb | `sudo mysql -e "SELECT table_name, ROUND((data_length+index_length)/1024/1024,1) MB FROM information_schema.tables WHERE table_schema='appdb' ORDER BY MB DESC;"` | Biggest tables first. |
| T0975 | L2 | any | MariaDB: show table sizes in crm | `sudo mysql -e "SELECT table_name, ROUND((data_length+index_length)/1024/1024,1) MB FROM information_schema.tables WHERE table_schema='crm' ORDER BY MB DESC;"` | Biggest tables first. |
| T0976 | L2 | any | MariaDB: show table sizes in shop | `sudo mysql -e "SELECT table_name, ROUND((data_length+index_length)/1024/1024,1) MB FROM information_schema.tables WHERE table_schema='shop' ORDER BY MB DESC;"` | Biggest tables first. |
| T0977 | L2 | any | MariaDB: show table sizes in wiki | `sudo mysql -e "SELECT table_name, ROUND((data_length+index_length)/1024/1024,1) MB FROM information_schema.tables WHERE table_schema='wiki' ORDER BY MB DESC;"` | Biggest tables first. |
| T0978 | L2 | any | MariaDB: show table sizes in zabbix | `sudo mysql -e "SELECT table_name, ROUND((data_length+index_length)/1024/1024,1) MB FROM information_schema.tables WHERE table_schema='zabbix' ORDER BY MB DESC;"` | Biggest tables first. |
| T0979 | L2 | any | PostgreSQL: back up database analytics | `sudo -u postgres pg_dump -Fc analytics > /srv/backups/analytics-$(date +%F).dump` | -Fc custom format allows selective restore. |
| T0980 | L2 | any | PostgreSQL: back up database appdb | `sudo -u postgres pg_dump -Fc appdb > /srv/backups/appdb-$(date +%F).dump` | -Fc custom format allows selective restore. |
| T0981 | L2 | any | PostgreSQL: back up database crm | `sudo -u postgres pg_dump -Fc crm > /srv/backups/crm-$(date +%F).dump` | -Fc custom format allows selective restore. |
| T0982 | L2 | any | PostgreSQL: back up database shop | `sudo -u postgres pg_dump -Fc shop > /srv/backups/shop-$(date +%F).dump` | -Fc custom format allows selective restore. |
| T0983 | L2 | any | PostgreSQL: back up database wiki | `sudo -u postgres pg_dump -Fc wiki > /srv/backups/wiki-$(date +%F).dump` | -Fc custom format allows selective restore. |
| T0984 | L2 | any | PostgreSQL: back up database zabbix | `sudo -u postgres pg_dump -Fc zabbix > /srv/backups/zabbix-$(date +%F).dump` | -Fc custom format allows selective restore. |
| T0985 | L2 | any | PostgreSQL: create database analytics owned by analytics_user | `sudo -u postgres createuser -P analytics_user && sudo -u postgres createdb -O analytics_user analytics` | -P prompts for the password. |
| T0986 | L2 | any | PostgreSQL: create database appdb owned by appdb_user | `sudo -u postgres createuser -P appdb_user && sudo -u postgres createdb -O appdb_user appdb` | -P prompts for the password. |
| T0987 | L2 | any | PostgreSQL: create database crm owned by crm_user | `sudo -u postgres createuser -P crm_user && sudo -u postgres createdb -O crm_user crm` | -P prompts for the password. |
| T0988 | L2 | any | PostgreSQL: create database shop owned by shop_user | `sudo -u postgres createuser -P shop_user && sudo -u postgres createdb -O shop_user shop` | -P prompts for the password. |
| T0989 | L2 | any | PostgreSQL: create database wiki owned by wiki_user | `sudo -u postgres createuser -P wiki_user && sudo -u postgres createdb -O wiki_user wiki` | -P prompts for the password. |
| T0990 | L2 | any | PostgreSQL: create database zabbix owned by zabbix_user | `sudo -u postgres createuser -P zabbix_user && sudo -u postgres createdb -O zabbix_user zabbix` | -P prompts for the password. |
| T0991 | L2 | any | PostgreSQL: list databases | `sudo -u postgres psql -l` | Database administration basics for Linux admins. |
| T0992 | L2 | any | PostgreSQL: open the console | `sudo -u postgres psql` | Database administration basics for Linux admins. |
| T0993 | L2 | any | PostgreSQL: show size of database analytics | `sudo -u postgres psql -c "SELECT pg_size_pretty(pg_database_size('analytics'));"` | Find what fills the disk. |
| T0994 | L2 | any | PostgreSQL: show size of database appdb | `sudo -u postgres psql -c "SELECT pg_size_pretty(pg_database_size('appdb'));"` | Find what fills the disk. |
| T0995 | L2 | any | PostgreSQL: show size of database crm | `sudo -u postgres psql -c "SELECT pg_size_pretty(pg_database_size('crm'));"` | Find what fills the disk. |
| T0996 | L2 | any | PostgreSQL: show size of database shop | `sudo -u postgres psql -c "SELECT pg_size_pretty(pg_database_size('shop'));"` | Find what fills the disk. |
| T0997 | L2 | any | PostgreSQL: show size of database wiki | `sudo -u postgres psql -c "SELECT pg_size_pretty(pg_database_size('wiki'));"` | Find what fills the disk. |
| T0998 | L2 | any | PostgreSQL: show size of database zabbix | `sudo -u postgres psql -c "SELECT pg_size_pretty(pg_database_size('zabbix'));"` | Find what fills the disk. |
| T0999 | L2 | any | Redis: check it answers | `redis-cli ping` | Database administration basics for Linux admins. |
| T1000 | L3 | any | Cron: nightly PostgreSQL dump of analytics at 01:00 | `0 1 * * * postgres pg_dump -Fc analytics > /srv/backups/analytics-$(date +\%F).dump` | In /etc/cron.d/ with user field. |
| T1001 | L3 | any | Cron: nightly PostgreSQL dump of appdb at 01:00 | `0 1 * * * postgres pg_dump -Fc appdb > /srv/backups/appdb-$(date +\%F).dump` | In /etc/cron.d/ with user field. |
| T1002 | L3 | any | Cron: nightly PostgreSQL dump of crm at 01:00 | `0 1 * * * postgres pg_dump -Fc crm > /srv/backups/crm-$(date +\%F).dump` | In /etc/cron.d/ with user field. |
| T1003 | L3 | any | Cron: nightly PostgreSQL dump of shop at 01:00 | `0 1 * * * postgres pg_dump -Fc shop > /srv/backups/shop-$(date +\%F).dump` | In /etc/cron.d/ with user field. |
| T1004 | L3 | any | Cron: nightly PostgreSQL dump of wiki at 01:00 | `0 1 * * * postgres pg_dump -Fc wiki > /srv/backups/wiki-$(date +\%F).dump` | In /etc/cron.d/ with user field. |
| T1005 | L3 | any | Cron: nightly PostgreSQL dump of zabbix at 01:00 | `0 1 * * * postgres pg_dump -Fc zabbix > /srv/backups/zabbix-$(date +\%F).dump` | In /etc/cron.d/ with user field. |
| T1006 | L3 | any | MariaDB: restore database analytics | `gunzip -c /srv/backups/analytics.sql.gz \| sudo mysql analytics` | Restore into an empty database. |
| T1007 | L3 | any | MariaDB: restore database appdb | `gunzip -c /srv/backups/appdb.sql.gz \| sudo mysql appdb` | Restore into an empty database. |
| T1008 | L3 | any | MariaDB: restore database crm | `gunzip -c /srv/backups/crm.sql.gz \| sudo mysql crm` | Restore into an empty database. |
| T1009 | L3 | any | MariaDB: restore database shop | `gunzip -c /srv/backups/shop.sql.gz \| sudo mysql shop` | Restore into an empty database. |
| T1010 | L3 | any | MariaDB: restore database wiki | `gunzip -c /srv/backups/wiki.sql.gz \| sudo mysql wiki` | Restore into an empty database. |
| T1011 | L3 | any | MariaDB: restore database zabbix | `gunzip -c /srv/backups/zabbix.sql.gz \| sudo mysql zabbix` | Restore into an empty database. |
| T1012 | L3 | any | MariaDB: show running queries | `sudo mysql -e 'SHOW FULL PROCESSLIST;'` | Database administration basics for Linux admins. |
| T1013 | L3 | any | PostgreSQL: find the config and data directory | `sudo -u postgres psql -c 'SHOW config_file;' -c 'SHOW data_directory;'` | Database administration basics for Linux admins. |
| T1014 | L3 | any | PostgreSQL: reload config without restart | `sudo -u postgres psql -c 'SELECT pg_reload_conf();'` | Database administration basics for Linux admins. |
| T1015 | L3 | any | PostgreSQL: restore database analytics from a dump | `sudo -u postgres pg_restore -d analytics --clean /srv/backups/analytics.dump` | --clean drops objects first; test on a copy. |
| T1016 | L3 | any | PostgreSQL: restore database appdb from a dump | `sudo -u postgres pg_restore -d appdb --clean /srv/backups/appdb.dump` | --clean drops objects first; test on a copy. |
| T1017 | L3 | any | PostgreSQL: restore database crm from a dump | `sudo -u postgres pg_restore -d crm --clean /srv/backups/crm.dump` | --clean drops objects first; test on a copy. |
| T1018 | L3 | any | PostgreSQL: restore database shop from a dump | `sudo -u postgres pg_restore -d shop --clean /srv/backups/shop.dump` | --clean drops objects first; test on a copy. |
| T1019 | L3 | any | PostgreSQL: restore database wiki from a dump | `sudo -u postgres pg_restore -d wiki --clean /srv/backups/wiki.dump` | --clean drops objects first; test on a copy. |
| T1020 | L3 | any | PostgreSQL: restore database zabbix from a dump | `sudo -u postgres pg_restore -d zabbix --clean /srv/backups/zabbix.dump` | --clean drops objects first; test on a copy. |
| T1021 | L3 | any | PostgreSQL: show active connections to analytics | `sudo -u postgres psql -c "SELECT pid, usename, state, query_start FROM pg_stat_activity WHERE datname='analytics';"` | Spot long-running queries. |
| T1022 | L3 | any | PostgreSQL: show active connections to appdb | `sudo -u postgres psql -c "SELECT pid, usename, state, query_start FROM pg_stat_activity WHERE datname='appdb';"` | Spot long-running queries. |
| T1023 | L3 | any | PostgreSQL: show active connections to crm | `sudo -u postgres psql -c "SELECT pid, usename, state, query_start FROM pg_stat_activity WHERE datname='crm';"` | Spot long-running queries. |
| T1024 | L3 | any | PostgreSQL: show active connections to shop | `sudo -u postgres psql -c "SELECT pid, usename, state, query_start FROM pg_stat_activity WHERE datname='shop';"` | Spot long-running queries. |
| T1025 | L3 | any | PostgreSQL: show active connections to wiki | `sudo -u postgres psql -c "SELECT pid, usename, state, query_start FROM pg_stat_activity WHERE datname='wiki';"` | Spot long-running queries. |
| T1026 | L3 | any | PostgreSQL: show active connections to zabbix | `sudo -u postgres psql -c "SELECT pid, usename, state, query_start FROM pg_stat_activity WHERE datname='zabbix';"` | Spot long-running queries. |
| T1027 | L3 | any | Redis: show memory usage | `redis-cli info memory \| grep used_memory_human` | Database administration basics for Linux admins. |
