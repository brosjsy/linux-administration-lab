# Web servers (78 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T4960 | L2 | rhel | Create the Nginx site api.lab.local on Rocky | `sudo nano /etc/nginx/conf.d/api.conf && sudo nginx -t && sudo systemctl reload nginx` | Rocky uses conf.d instead of sites-enabled. |
| T4961 | L2 | debian | Create the Nginx site file for api.lab.local | `sudo nano /etc/nginx/sites-available/api` | server_name, root and listen go here. |
| T4962 | L2 | debian | Create the Nginx site file for grafana.lab.local | `sudo nano /etc/nginx/sites-available/grafana` | server_name, root and listen go here. |
| T4963 | L2 | debian | Create the Nginx site file for intranet.lab.local | `sudo nano /etc/nginx/sites-available/intranet` | server_name, root and listen go here. |
| T4964 | L2 | debian | Create the Nginx site file for shop.lab.local | `sudo nano /etc/nginx/sites-available/shop` | server_name, root and listen go here. |
| T4965 | L2 | debian | Create the Nginx site file for status.lab.local | `sudo nano /etc/nginx/sites-available/status` | server_name, root and listen go here. |
| T4966 | L2 | debian | Create the Nginx site file for wiki.lab.local | `sudo nano /etc/nginx/sites-available/wiki` | server_name, root and listen go here. |
| T4967 | L2 | rhel | Create the Nginx site grafana.lab.local on Rocky | `sudo nano /etc/nginx/conf.d/grafana.conf && sudo nginx -t && sudo systemctl reload nginx` | Rocky uses conf.d instead of sites-enabled. |
| T4968 | L2 | rhel | Create the Nginx site intranet.lab.local on Rocky | `sudo nano /etc/nginx/conf.d/intranet.conf && sudo nginx -t && sudo systemctl reload nginx` | Rocky uses conf.d instead of sites-enabled. |
| T4969 | L2 | rhel | Create the Nginx site shop.lab.local on Rocky | `sudo nano /etc/nginx/conf.d/shop.conf && sudo nginx -t && sudo systemctl reload nginx` | Rocky uses conf.d instead of sites-enabled. |
| T4970 | L2 | rhel | Create the Nginx site status.lab.local on Rocky | `sudo nano /etc/nginx/conf.d/status.conf && sudo nginx -t && sudo systemctl reload nginx` | Rocky uses conf.d instead of sites-enabled. |
| T4971 | L2 | rhel | Create the Nginx site wiki.lab.local on Rocky | `sudo nano /etc/nginx/conf.d/wiki.conf && sudo nginx -t && sudo systemctl reload nginx` | Rocky uses conf.d instead of sites-enabled. |
| T4972 | L2 | debian | Disable the Nginx site api.lab.local | `sudo rm /etc/nginx/sites-enabled/api && sudo nginx -t && sudo systemctl reload nginx` | Config stays in sites-available. |
| T4973 | L2 | debian | Disable the Nginx site grafana.lab.local | `sudo rm /etc/nginx/sites-enabled/grafana && sudo nginx -t && sudo systemctl reload nginx` | Config stays in sites-available. |
| T4974 | L2 | debian | Disable the Nginx site intranet.lab.local | `sudo rm /etc/nginx/sites-enabled/intranet && sudo nginx -t && sudo systemctl reload nginx` | Config stays in sites-available. |
| T4975 | L2 | debian | Disable the Nginx site shop.lab.local | `sudo rm /etc/nginx/sites-enabled/shop && sudo nginx -t && sudo systemctl reload nginx` | Config stays in sites-available. |
| T4976 | L2 | debian | Disable the Nginx site status.lab.local | `sudo rm /etc/nginx/sites-enabled/status && sudo nginx -t && sudo systemctl reload nginx` | Config stays in sites-available. |
| T4977 | L2 | debian | Disable the Nginx site wiki.lab.local | `sudo rm /etc/nginx/sites-enabled/wiki && sudo nginx -t && sudo systemctl reload nginx` | Config stays in sites-available. |
| T4978 | L2 | debian | Enable the Nginx site api.lab.local | `sudo ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx` | Always nginx -t before reload. |
| T4979 | L2 | debian | Enable the Nginx site grafana.lab.local | `sudo ln -s /etc/nginx/sites-available/grafana /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx` | Always nginx -t before reload. |
| T4980 | L2 | debian | Enable the Nginx site intranet.lab.local | `sudo ln -s /etc/nginx/sites-available/intranet /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx` | Always nginx -t before reload. |
| T4981 | L2 | debian | Enable the Nginx site shop.lab.local | `sudo ln -s /etc/nginx/sites-available/shop /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx` | Always nginx -t before reload. |
| T4982 | L2 | debian | Enable the Nginx site status.lab.local | `sudo ln -s /etc/nginx/sites-available/status /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx` | Always nginx -t before reload. |
| T4983 | L2 | debian | Enable the Nginx site wiki.lab.local | `sudo ln -s /etc/nginx/sites-available/wiki /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx` | Always nginx -t before reload. |
| T4984 | L2 | any | List enabled Apache modules (Ubuntu) | `apache2ctl -M` | Validate before reloading. |
| T4985 | L2 | any | Show the full effective Nginx configuration | `sudo nginx -T \| less` | Validate before reloading. |
| T4986 | L2 | any | Test that api.lab.local answers locally | `curl -sI -H 'Host: api.lab.local' http://127.0.0.1/` | Tests the virtual host without DNS. |
| T4987 | L2 | any | Test that grafana.lab.local answers locally | `curl -sI -H 'Host: grafana.lab.local' http://127.0.0.1/` | Tests the virtual host without DNS. |
| T4988 | L2 | any | Test that intranet.lab.local answers locally | `curl -sI -H 'Host: intranet.lab.local' http://127.0.0.1/` | Tests the virtual host without DNS. |
| T4989 | L2 | any | Test that shop.lab.local answers locally | `curl -sI -H 'Host: shop.lab.local' http://127.0.0.1/` | Tests the virtual host without DNS. |
| T4990 | L2 | any | Test that status.lab.local answers locally | `curl -sI -H 'Host: status.lab.local' http://127.0.0.1/` | Tests the virtual host without DNS. |
| T4991 | L2 | any | Test that wiki.lab.local answers locally | `curl -sI -H 'Host: wiki.lab.local' http://127.0.0.1/` | Tests the virtual host without DNS. |
| T4992 | L2 | any | Test the Apache configuration (Rocky) | `sudo apachectl configtest` | Validate before reloading. |
| T4993 | L2 | any | Test the Apache configuration (Ubuntu) | `sudo apache2ctl configtest` | Validate before reloading. |
| T4994 | L2 | any | Test the Nginx configuration | `sudo nginx -t` | Validate before reloading. |
| T4995 | L3 | any | Check HAProxy config syntax | `sudo haproxy -c -f /etc/haproxy/haproxy.cfg` | Validate before reloading. |
| T4996 | L3 | any | Get a Let's Encrypt certificate for api.lab.local | `sudo certbot --nginx -d api.lab.local` | Certbot edits the server block and installs renewal. |
| T4997 | L3 | any | Get a Let's Encrypt certificate for grafana.lab.local | `sudo certbot --nginx -d grafana.lab.local` | Certbot edits the server block and installs renewal. |
| T4998 | L3 | any | Get a Let's Encrypt certificate for intranet.lab.local | `sudo certbot --nginx -d intranet.lab.local` | Certbot edits the server block and installs renewal. |
| T4999 | L3 | any | Get a Let's Encrypt certificate for shop.lab.local | `sudo certbot --nginx -d shop.lab.local` | Certbot edits the server block and installs renewal. |
| T5000 | L3 | any | Get a Let's Encrypt certificate for status.lab.local | `sudo certbot --nginx -d status.lab.local` | Certbot edits the server block and installs renewal. |
| T5001 | L3 | any | Get a Let's Encrypt certificate for wiki.lab.local | `sudo certbot --nginx -d wiki.lab.local` | Certbot edits the server block and installs renewal. |
| T5002 | L3 | any | Load-balance api.lab.local across two backends | `upstream api_back { server 192.168.56.11:8080; server 192.168.56.12:8080; }  # proxy_pass http://api_back;` | Round robin by default. |
| T5003 | L3 | any | Load-balance grafana.lab.local across two backends | `upstream grafana_back { server 192.168.56.11:8080; server 192.168.56.12:8080; }  # proxy_pass http://grafana_back;` | Round robin by default. |
| T5004 | L3 | any | Load-balance intranet.lab.local across two backends | `upstream intranet_back { server 192.168.56.11:8080; server 192.168.56.12:8080; }  # proxy_pass http://intranet_back;` | Round robin by default. |
| T5005 | L3 | any | Load-balance shop.lab.local across two backends | `upstream shop_back { server 192.168.56.11:8080; server 192.168.56.12:8080; }  # proxy_pass http://shop_back;` | Round robin by default. |
| T5006 | L3 | any | Load-balance status.lab.local across two backends | `upstream status_back { server 192.168.56.11:8080; server 192.168.56.12:8080; }  # proxy_pass http://status_back;` | Round robin by default. |
| T5007 | L3 | any | Load-balance wiki.lab.local across two backends | `upstream wiki_back { server 192.168.56.11:8080; server 192.168.56.12:8080; }  # proxy_pass http://wiki_back;` | Round robin by default. |
| T5008 | L3 | any | Protect api.lab.local with basic authentication | `sudo htpasswd -c /etc/nginx/.htpasswd-api admin  # then auth_basic and auth_basic_user_file in the location` | Package apache2-utils or httpd-tools. |
| T5009 | L3 | any | Protect grafana.lab.local with basic authentication | `sudo htpasswd -c /etc/nginx/.htpasswd-grafana admin  # then auth_basic and auth_basic_user_file in the location` | Package apache2-utils or httpd-tools. |
| T5010 | L3 | any | Protect intranet.lab.local with basic authentication | `sudo htpasswd -c /etc/nginx/.htpasswd-intranet admin  # then auth_basic and auth_basic_user_file in the location` | Package apache2-utils or httpd-tools. |
| T5011 | L3 | any | Protect shop.lab.local with basic authentication | `sudo htpasswd -c /etc/nginx/.htpasswd-shop admin  # then auth_basic and auth_basic_user_file in the location` | Package apache2-utils or httpd-tools. |
| T5012 | L3 | any | Protect status.lab.local with basic authentication | `sudo htpasswd -c /etc/nginx/.htpasswd-status admin  # then auth_basic and auth_basic_user_file in the location` | Package apache2-utils or httpd-tools. |
| T5013 | L3 | any | Protect wiki.lab.local with basic authentication | `sudo htpasswd -c /etc/nginx/.htpasswd-wiki admin  # then auth_basic and auth_basic_user_file in the location` | Package apache2-utils or httpd-tools. |
| T5014 | L3 | any | Redirect HTTP to HTTPS for api.lab.local | `server { listen 80; server_name api.lab.local; return 301 https://$host$request_uri; }` | Separate server block for port 80. |
| T5015 | L3 | any | Redirect HTTP to HTTPS for grafana.lab.local | `server { listen 80; server_name grafana.lab.local; return 301 https://$host$request_uri; }` | Separate server block for port 80. |
| T5016 | L3 | any | Redirect HTTP to HTTPS for intranet.lab.local | `server { listen 80; server_name intranet.lab.local; return 301 https://$host$request_uri; }` | Separate server block for port 80. |
| T5017 | L3 | any | Redirect HTTP to HTTPS for shop.lab.local | `server { listen 80; server_name shop.lab.local; return 301 https://$host$request_uri; }` | Separate server block for port 80. |
| T5018 | L3 | any | Redirect HTTP to HTTPS for status.lab.local | `server { listen 80; server_name status.lab.local; return 301 https://$host$request_uri; }` | Separate server block for port 80. |
| T5019 | L3 | any | Redirect HTTP to HTTPS for wiki.lab.local | `server { listen 80; server_name wiki.lab.local; return 301 https://$host$request_uri; }` | Separate server block for port 80. |
| T5020 | L3 | any | Reverse proxy api.lab.local to a backend on port 8080 | `location / { proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; }` | Inside the server block of the site. |
| T5021 | L3 | any | Reverse proxy grafana.lab.local to a backend on port 8080 | `location / { proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; }` | Inside the server block of the site. |
| T5022 | L3 | any | Reverse proxy intranet.lab.local to a backend on port 8080 | `location / { proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; }` | Inside the server block of the site. |
| T5023 | L3 | any | Reverse proxy shop.lab.local to a backend on port 8080 | `location / { proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; }` | Inside the server block of the site. |
| T5024 | L3 | any | Reverse proxy status.lab.local to a backend on port 8080 | `location / { proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; }` | Inside the server block of the site. |
| T5025 | L3 | any | Reverse proxy wiki.lab.local to a backend on port 8080 | `location / { proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; }` | Inside the server block of the site. |
| T5026 | L3 | any | Show only 5xx errors for api.lab.local in the access log | `awk '$9 ~ /^5/' /var/log/nginx/api.access.log \| tail -20` | Needs a per-site access_log line. |
| T5027 | L3 | any | Show only 5xx errors for grafana.lab.local in the access log | `awk '$9 ~ /^5/' /var/log/nginx/grafana.access.log \| tail -20` | Needs a per-site access_log line. |
| T5028 | L3 | any | Show only 5xx errors for intranet.lab.local in the access log | `awk '$9 ~ /^5/' /var/log/nginx/intranet.access.log \| tail -20` | Needs a per-site access_log line. |
| T5029 | L3 | any | Show only 5xx errors for shop.lab.local in the access log | `awk '$9 ~ /^5/' /var/log/nginx/shop.access.log \| tail -20` | Needs a per-site access_log line. |
| T5030 | L3 | any | Show only 5xx errors for status.lab.local in the access log | `awk '$9 ~ /^5/' /var/log/nginx/status.access.log \| tail -20` | Needs a per-site access_log line. |
| T5031 | L3 | any | Show only 5xx errors for wiki.lab.local in the access log | `awk '$9 ~ /^5/' /var/log/nginx/wiki.access.log \| tail -20` | Needs a per-site access_log line. |
| T5032 | L4 | any | Rate-limit requests to api.lab.local | `limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;  # http block; then limit_req zone=api burst=20; in location` | Stops brute force and simple floods. |
| T5033 | L4 | any | Rate-limit requests to grafana.lab.local | `limit_req_zone $binary_remote_addr zone=grafana:10m rate=10r/s;  # http block; then limit_req zone=grafana burst=20; in location` | Stops brute force and simple floods. |
| T5034 | L4 | any | Rate-limit requests to intranet.lab.local | `limit_req_zone $binary_remote_addr zone=intranet:10m rate=10r/s;  # http block; then limit_req zone=intranet burst=20; in location` | Stops brute force and simple floods. |
| T5035 | L4 | any | Rate-limit requests to shop.lab.local | `limit_req_zone $binary_remote_addr zone=shop:10m rate=10r/s;  # http block; then limit_req zone=shop burst=20; in location` | Stops brute force and simple floods. |
| T5036 | L4 | any | Rate-limit requests to status.lab.local | `limit_req_zone $binary_remote_addr zone=status:10m rate=10r/s;  # http block; then limit_req zone=status burst=20; in location` | Stops brute force and simple floods. |
| T5037 | L4 | any | Rate-limit requests to wiki.lab.local | `limit_req_zone $binary_remote_addr zone=wiki:10m rate=10r/s;  # http block; then limit_req zone=wiki burst=20; in location` | Stops brute force and simple floods. |
