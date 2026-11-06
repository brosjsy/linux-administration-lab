# 21. TLS certificates and OpenSSL

Level: intermediate

```bash
# check a remote certificate and its expiry
echo | openssl s_client -connect ya.ru:443 -servername ya.ru 2>/dev/null | openssl x509 -noout -subject -issuer -dates
# self-signed certificate for the lab
openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout /etc/ssl/private/lab.key -out /etc/ssl/certs/lab.crt -subj "/CN=lab.local"
# create a CSR for a real CA
openssl req -new -newkey rsa:2048 -nodes -keyout site.key -out site.csr -subj "/CN=site.example.ru"
# inspect files
openssl x509 -in lab.crt -noout -text | head -20
openssl rsa -in lab.key -check -noout
# Let's Encrypt with Nginx
sudo certbot --nginx -d site.example.ru && sudo certbot renew --dry-run
```
Scenario: users see "certificate expired". Check with `scripts/ssl_expiry_check.sh site.example.ru`, renew, reload Nginx, add the check to cron so it never happens again.
