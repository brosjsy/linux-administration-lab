# TLS certificates (64 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T4157 | L3 | any | Check that api.key matches api.crt | `diff <(openssl x509 -in api.crt -noout -modulus) <(openssl rsa -in api.key -noout -modulus) && echo match` | Mismatch is a common cause of web server start errors. |
| T4158 | L3 | any | Check that lab.key matches lab.crt | `diff <(openssl x509 -in lab.crt -noout -modulus) <(openssl rsa -in lab.key -noout -modulus) && echo match` | Mismatch is a common cause of web server start errors. |
| T4159 | L3 | any | Check that mail.key matches mail.crt | `diff <(openssl x509 -in mail.crt -noout -modulus) <(openssl rsa -in mail.key -noout -modulus) && echo match` | Mismatch is a common cause of web server start errors. |
| T4160 | L3 | any | Check that vpn.key matches vpn.crt | `diff <(openssl x509 -in vpn.crt -noout -modulus) <(openssl rsa -in vpn.key -noout -modulus) && echo match` | Mismatch is a common cause of web server start errors. |
| T4161 | L3 | any | Check that web1.key matches web1.crt | `diff <(openssl x509 -in web1.crt -noout -modulus) <(openssl rsa -in web1.key -noout -modulus) && echo match` | Mismatch is a common cause of web server start errors. |
| T4162 | L3 | any | Check that wiki.key matches wiki.crt | `diff <(openssl x509 -in wiki.crt -noout -modulus) <(openssl rsa -in wiki.key -noout -modulus) && echo match` | Mismatch is a common cause of web server start errors. |
| T4163 | L3 | any | Convert api.crt and api.key to a PFX bundle | `openssl pkcs12 -export -in api.crt -inkey api.key -out api.pfx` | For Windows and some appliances. |
| T4164 | L3 | any | Convert lab.crt and lab.key to a PFX bundle | `openssl pkcs12 -export -in lab.crt -inkey lab.key -out lab.pfx` | For Windows and some appliances. |
| T4165 | L3 | any | Convert mail.crt and mail.key to a PFX bundle | `openssl pkcs12 -export -in mail.crt -inkey mail.key -out mail.pfx` | For Windows and some appliances. |
| T4166 | L3 | any | Convert vpn.crt and vpn.key to a PFX bundle | `openssl pkcs12 -export -in vpn.crt -inkey vpn.key -out vpn.pfx` | For Windows and some appliances. |
| T4167 | L3 | any | Convert web1.crt and web1.key to a PFX bundle | `openssl pkcs12 -export -in web1.crt -inkey web1.key -out web1.pfx` | For Windows and some appliances. |
| T4168 | L3 | any | Convert wiki.crt and wiki.key to a PFX bundle | `openssl pkcs12 -export -in wiki.crt -inkey wiki.key -out wiki.pfx` | For Windows and some appliances. |
| T4169 | L3 | any | Create a 2048-bit private key and CSR for api.lab.local | `openssl req -new -newkey rsa:2048 -nodes -keyout api.key -out api.csr -subj "/CN=api.lab.local"` | Send the CSR to the CA, keep the key private. |
| T4170 | L3 | any | Create a 2048-bit private key and CSR for lab.lab.local | `openssl req -new -newkey rsa:2048 -nodes -keyout lab.key -out lab.csr -subj "/CN=lab.lab.local"` | Send the CSR to the CA, keep the key private. |
| T4171 | L3 | any | Create a 2048-bit private key and CSR for mail.lab.local | `openssl req -new -newkey rsa:2048 -nodes -keyout mail.key -out mail.csr -subj "/CN=mail.lab.local"` | Send the CSR to the CA, keep the key private. |
| T4172 | L3 | any | Create a 2048-bit private key and CSR for vpn.lab.local | `openssl req -new -newkey rsa:2048 -nodes -keyout vpn.key -out vpn.csr -subj "/CN=vpn.lab.local"` | Send the CSR to the CA, keep the key private. |
| T4173 | L3 | any | Create a 2048-bit private key and CSR for web1.lab.local | `openssl req -new -newkey rsa:2048 -nodes -keyout web1.key -out web1.csr -subj "/CN=web1.lab.local"` | Send the CSR to the CA, keep the key private. |
| T4174 | L3 | any | Create a 2048-bit private key and CSR for wiki.lab.local | `openssl req -new -newkey rsa:2048 -nodes -keyout wiki.key -out wiki.csr -subj "/CN=wiki.lab.local"` | Send the CSR to the CA, keep the key private. |
| T4175 | L3 | any | Create a self-signed certificate for api.lab.local valid 365 days | `openssl req -x509 -newkey rsa:2048 -nodes -days 365 -keyout api.key -out api.crt -subj "/CN=api.lab.local"` | Fine for labs, not for public sites. |
| T4176 | L3 | any | Create a self-signed certificate for lab.lab.local valid 365 days | `openssl req -x509 -newkey rsa:2048 -nodes -days 365 -keyout lab.key -out lab.crt -subj "/CN=lab.lab.local"` | Fine for labs, not for public sites. |
| T4177 | L3 | any | Create a self-signed certificate for mail.lab.local valid 365 days | `openssl req -x509 -newkey rsa:2048 -nodes -days 365 -keyout mail.key -out mail.crt -subj "/CN=mail.lab.local"` | Fine for labs, not for public sites. |
| T4178 | L3 | any | Create a self-signed certificate for vpn.lab.local valid 365 days | `openssl req -x509 -newkey rsa:2048 -nodes -days 365 -keyout vpn.key -out vpn.crt -subj "/CN=vpn.lab.local"` | Fine for labs, not for public sites. |
| T4179 | L3 | any | Create a self-signed certificate for web1.lab.local valid 365 days | `openssl req -x509 -newkey rsa:2048 -nodes -days 365 -keyout web1.key -out web1.crt -subj "/CN=web1.lab.local"` | Fine for labs, not for public sites. |
| T4180 | L3 | any | Create a self-signed certificate for wiki.lab.local valid 365 days | `openssl req -x509 -newkey rsa:2048 -nodes -days 365 -keyout wiki.key -out wiki.crt -subj "/CN=wiki.lab.local"` | Fine for labs, not for public sites. |
| T4181 | L3 | any | Show the SAN names in api.crt | `openssl x509 -in api.crt -noout -ext subjectAltName` | Browsers check SAN, not CN. |
| T4182 | L3 | any | Show the SAN names in lab.crt | `openssl x509 -in lab.crt -noout -ext subjectAltName` | Browsers check SAN, not CN. |
| T4183 | L3 | any | Show the SAN names in mail.crt | `openssl x509 -in mail.crt -noout -ext subjectAltName` | Browsers check SAN, not CN. |
| T4184 | L3 | any | Show the SAN names in vpn.crt | `openssl x509 -in vpn.crt -noout -ext subjectAltName` | Browsers check SAN, not CN. |
| T4185 | L3 | any | Show the SAN names in web1.crt | `openssl x509 -in web1.crt -noout -ext subjectAltName` | Browsers check SAN, not CN. |
| T4186 | L3 | any | Show the SAN names in wiki.crt | `openssl x509 -in wiki.crt -noout -ext subjectAltName` | Browsers check SAN, not CN. |
| T4187 | L3 | any | Show the certificate expiry date of croc.ru | `echo \| openssl s_client -connect croc.ru:443 -servername croc.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4188 | L3 | any | Show the certificate expiry date of example.com | `echo \| openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4189 | L3 | any | Show the certificate expiry date of github.com | `echo \| openssl s_client -connect github.com:443 -servername github.com 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4190 | L3 | any | Show the certificate expiry date of gosuslugi.ru | `echo \| openssl s_client -connect gosuslugi.ru:443 -servername gosuslugi.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4191 | L3 | any | Show the certificate expiry date of habr.com | `echo \| openssl s_client -connect habr.com:443 -servername habr.com 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4192 | L3 | any | Show the certificate expiry date of itmo.ru | `echo \| openssl s_client -connect itmo.ru:443 -servername itmo.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4193 | L3 | any | Show the certificate expiry date of kernel.org | `echo \| openssl s_client -connect kernel.org:443 -servername kernel.org 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4194 | L3 | any | Show the certificate expiry date of mail.ru | `echo \| openssl s_client -connect mail.ru:443 -servername mail.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4195 | L3 | any | Show the certificate expiry date of ozon.ru | `echo \| openssl s_client -connect ozon.ru:443 -servername ozon.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4196 | L3 | any | Show the certificate expiry date of rbc.ru | `echo \| openssl s_client -connect rbc.ru:443 -servername rbc.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4197 | L3 | any | Show the certificate expiry date of sber.ru | `echo \| openssl s_client -connect sber.ru:443 -servername sber.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4198 | L3 | any | Show the certificate expiry date of spbu.ru | `echo \| openssl s_client -connect spbu.ru:443 -servername spbu.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4199 | L3 | any | Show the certificate expiry date of vk.com | `echo \| openssl s_client -connect vk.com:443 -servername vk.com 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4200 | L3 | any | Show the certificate expiry date of ya.ru | `echo \| openssl s_client -connect ya.ru:443 -servername ya.ru 2>/dev/null \| openssl x509 -noout -dates` | notAfter is the expiry date. |
| T4201 | L3 | any | Show the expiry date of api.crt | `openssl x509 -in api.crt -noout -enddate` | notAfter is the expiry. |
| T4202 | L3 | any | Show the expiry date of lab.crt | `openssl x509 -in lab.crt -noout -enddate` | notAfter is the expiry. |
| T4203 | L3 | any | Show the expiry date of mail.crt | `openssl x509 -in mail.crt -noout -enddate` | notAfter is the expiry. |
| T4204 | L3 | any | Show the expiry date of vpn.crt | `openssl x509 -in vpn.crt -noout -enddate` | notAfter is the expiry. |
| T4205 | L3 | any | Show the expiry date of web1.crt | `openssl x509 -in web1.crt -noout -enddate` | notAfter is the expiry. |
| T4206 | L3 | any | Show the expiry date of wiki.crt | `openssl x509 -in wiki.crt -noout -enddate` | notAfter is the expiry. |
| T4207 | L3 | any | Show who issued the certificate of croc.ru | `echo \| openssl s_client -connect croc.ru:443 -servername croc.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4208 | L3 | any | Show who issued the certificate of example.com | `echo \| openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4209 | L3 | any | Show who issued the certificate of github.com | `echo \| openssl s_client -connect github.com:443 -servername github.com 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4210 | L3 | any | Show who issued the certificate of gosuslugi.ru | `echo \| openssl s_client -connect gosuslugi.ru:443 -servername gosuslugi.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4211 | L3 | any | Show who issued the certificate of habr.com | `echo \| openssl s_client -connect habr.com:443 -servername habr.com 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4212 | L3 | any | Show who issued the certificate of itmo.ru | `echo \| openssl s_client -connect itmo.ru:443 -servername itmo.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4213 | L3 | any | Show who issued the certificate of kernel.org | `echo \| openssl s_client -connect kernel.org:443 -servername kernel.org 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4214 | L3 | any | Show who issued the certificate of mail.ru | `echo \| openssl s_client -connect mail.ru:443 -servername mail.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4215 | L3 | any | Show who issued the certificate of ozon.ru | `echo \| openssl s_client -connect ozon.ru:443 -servername ozon.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4216 | L3 | any | Show who issued the certificate of rbc.ru | `echo \| openssl s_client -connect rbc.ru:443 -servername rbc.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4217 | L3 | any | Show who issued the certificate of sber.ru | `echo \| openssl s_client -connect sber.ru:443 -servername sber.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4218 | L3 | any | Show who issued the certificate of spbu.ru | `echo \| openssl s_client -connect spbu.ru:443 -servername spbu.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4219 | L3 | any | Show who issued the certificate of vk.com | `echo \| openssl s_client -connect vk.com:443 -servername vk.com 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
| T4220 | L3 | any | Show who issued the certificate of ya.ru | `echo \| openssl s_client -connect ya.ru:443 -servername ya.ru 2>/dev/null \| openssl x509 -noout -issuer -subject` | Issuer is the CA, subject is the site. |
