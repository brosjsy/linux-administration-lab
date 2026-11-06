# Networking: DNS (214 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T1903 | L2 | any | Get the IPv4 address of croc.ru | `dig croc.ru A +short` | Queries A records with the system resolver. |
| T1904 | L2 | any | Get the IPv4 address of croc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 croc.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1905 | L2 | any | Get the IPv4 address of example.com | `dig example.com A +short` | Queries A records with the system resolver. |
| T1906 | L2 | any | Get the IPv4 address of example.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 example.com A +short` | Compare with the local resolver to find DNS problems. |
| T1907 | L2 | any | Get the IPv4 address of github.com | `dig github.com A +short` | Queries A records with the system resolver. |
| T1908 | L2 | any | Get the IPv4 address of github.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 github.com A +short` | Compare with the local resolver to find DNS problems. |
| T1909 | L2 | any | Get the IPv4 address of gosuslugi.ru | `dig gosuslugi.ru A +short` | Queries A records with the system resolver. |
| T1910 | L2 | any | Get the IPv4 address of gosuslugi.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 gosuslugi.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1911 | L2 | any | Get the IPv4 address of habr.com | `dig habr.com A +short` | Queries A records with the system resolver. |
| T1912 | L2 | any | Get the IPv4 address of habr.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 habr.com A +short` | Compare with the local resolver to find DNS problems. |
| T1913 | L2 | any | Get the IPv4 address of itmo.ru | `dig itmo.ru A +short` | Queries A records with the system resolver. |
| T1914 | L2 | any | Get the IPv4 address of itmo.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 itmo.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1915 | L2 | any | Get the IPv4 address of kernel.org | `dig kernel.org A +short` | Queries A records with the system resolver. |
| T1916 | L2 | any | Get the IPv4 address of kernel.org from Google DNS 8.8.8.8 | `dig @8.8.8.8 kernel.org A +short` | Compare with the local resolver to find DNS problems. |
| T1917 | L2 | any | Get the IPv4 address of mail.ru | `dig mail.ru A +short` | Queries A records with the system resolver. |
| T1918 | L2 | any | Get the IPv4 address of mail.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 mail.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1919 | L2 | any | Get the IPv4 address of ozon.ru | `dig ozon.ru A +short` | Queries A records with the system resolver. |
| T1920 | L2 | any | Get the IPv4 address of ozon.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ozon.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1921 | L2 | any | Get the IPv4 address of rbc.ru | `dig rbc.ru A +short` | Queries A records with the system resolver. |
| T1922 | L2 | any | Get the IPv4 address of rbc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 rbc.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1923 | L2 | any | Get the IPv4 address of sber.ru | `dig sber.ru A +short` | Queries A records with the system resolver. |
| T1924 | L2 | any | Get the IPv4 address of sber.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 sber.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1925 | L2 | any | Get the IPv4 address of spbu.ru | `dig spbu.ru A +short` | Queries A records with the system resolver. |
| T1926 | L2 | any | Get the IPv4 address of spbu.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 spbu.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1927 | L2 | any | Get the IPv4 address of vk.com | `dig vk.com A +short` | Queries A records with the system resolver. |
| T1928 | L2 | any | Get the IPv4 address of vk.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 vk.com A +short` | Compare with the local resolver to find DNS problems. |
| T1929 | L2 | any | Get the IPv4 address of ya.ru | `dig ya.ru A +short` | Queries A records with the system resolver. |
| T1930 | L2 | any | Get the IPv4 address of ya.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ya.ru A +short` | Compare with the local resolver to find DNS problems. |
| T1931 | L2 | any | Get the IPv6 address of croc.ru | `dig croc.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1932 | L2 | any | Get the IPv6 address of croc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 croc.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1933 | L2 | any | Get the IPv6 address of example.com | `dig example.com AAAA +short` | Queries AAAA records with the system resolver. |
| T1934 | L2 | any | Get the IPv6 address of example.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 example.com AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1935 | L2 | any | Get the IPv6 address of github.com | `dig github.com AAAA +short` | Queries AAAA records with the system resolver. |
| T1936 | L2 | any | Get the IPv6 address of github.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 github.com AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1937 | L2 | any | Get the IPv6 address of gosuslugi.ru | `dig gosuslugi.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1938 | L2 | any | Get the IPv6 address of gosuslugi.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 gosuslugi.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1939 | L2 | any | Get the IPv6 address of habr.com | `dig habr.com AAAA +short` | Queries AAAA records with the system resolver. |
| T1940 | L2 | any | Get the IPv6 address of habr.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 habr.com AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1941 | L2 | any | Get the IPv6 address of itmo.ru | `dig itmo.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1942 | L2 | any | Get the IPv6 address of itmo.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 itmo.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1943 | L2 | any | Get the IPv6 address of kernel.org | `dig kernel.org AAAA +short` | Queries AAAA records with the system resolver. |
| T1944 | L2 | any | Get the IPv6 address of kernel.org from Google DNS 8.8.8.8 | `dig @8.8.8.8 kernel.org AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1945 | L2 | any | Get the IPv6 address of mail.ru | `dig mail.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1946 | L2 | any | Get the IPv6 address of mail.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 mail.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1947 | L2 | any | Get the IPv6 address of ozon.ru | `dig ozon.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1948 | L2 | any | Get the IPv6 address of ozon.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ozon.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1949 | L2 | any | Get the IPv6 address of rbc.ru | `dig rbc.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1950 | L2 | any | Get the IPv6 address of rbc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 rbc.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1951 | L2 | any | Get the IPv6 address of sber.ru | `dig sber.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1952 | L2 | any | Get the IPv6 address of sber.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 sber.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1953 | L2 | any | Get the IPv6 address of spbu.ru | `dig spbu.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1954 | L2 | any | Get the IPv6 address of spbu.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 spbu.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1955 | L2 | any | Get the IPv6 address of vk.com | `dig vk.com AAAA +short` | Queries AAAA records with the system resolver. |
| T1956 | L2 | any | Get the IPv6 address of vk.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 vk.com AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1957 | L2 | any | Get the IPv6 address of ya.ru | `dig ya.ru AAAA +short` | Queries AAAA records with the system resolver. |
| T1958 | L2 | any | Get the IPv6 address of ya.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ya.ru AAAA +short` | Compare with the local resolver to find DNS problems. |
| T1959 | L2 | any | Get the TXT records (SPF, verification) of croc.ru | `dig croc.ru TXT +short` | Queries TXT records with the system resolver. |
| T1960 | L2 | any | Get the TXT records (SPF, verification) of croc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 croc.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1961 | L2 | any | Get the TXT records (SPF, verification) of example.com | `dig example.com TXT +short` | Queries TXT records with the system resolver. |
| T1962 | L2 | any | Get the TXT records (SPF, verification) of example.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 example.com TXT +short` | Compare with the local resolver to find DNS problems. |
| T1963 | L2 | any | Get the TXT records (SPF, verification) of github.com | `dig github.com TXT +short` | Queries TXT records with the system resolver. |
| T1964 | L2 | any | Get the TXT records (SPF, verification) of github.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 github.com TXT +short` | Compare with the local resolver to find DNS problems. |
| T1965 | L2 | any | Get the TXT records (SPF, verification) of gosuslugi.ru | `dig gosuslugi.ru TXT +short` | Queries TXT records with the system resolver. |
| T1966 | L2 | any | Get the TXT records (SPF, verification) of gosuslugi.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 gosuslugi.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1967 | L2 | any | Get the TXT records (SPF, verification) of habr.com | `dig habr.com TXT +short` | Queries TXT records with the system resolver. |
| T1968 | L2 | any | Get the TXT records (SPF, verification) of habr.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 habr.com TXT +short` | Compare with the local resolver to find DNS problems. |
| T1969 | L2 | any | Get the TXT records (SPF, verification) of itmo.ru | `dig itmo.ru TXT +short` | Queries TXT records with the system resolver. |
| T1970 | L2 | any | Get the TXT records (SPF, verification) of itmo.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 itmo.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1971 | L2 | any | Get the TXT records (SPF, verification) of kernel.org | `dig kernel.org TXT +short` | Queries TXT records with the system resolver. |
| T1972 | L2 | any | Get the TXT records (SPF, verification) of kernel.org from Google DNS 8.8.8.8 | `dig @8.8.8.8 kernel.org TXT +short` | Compare with the local resolver to find DNS problems. |
| T1973 | L2 | any | Get the TXT records (SPF, verification) of mail.ru | `dig mail.ru TXT +short` | Queries TXT records with the system resolver. |
| T1974 | L2 | any | Get the TXT records (SPF, verification) of mail.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 mail.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1975 | L2 | any | Get the TXT records (SPF, verification) of ozon.ru | `dig ozon.ru TXT +short` | Queries TXT records with the system resolver. |
| T1976 | L2 | any | Get the TXT records (SPF, verification) of ozon.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ozon.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1977 | L2 | any | Get the TXT records (SPF, verification) of rbc.ru | `dig rbc.ru TXT +short` | Queries TXT records with the system resolver. |
| T1978 | L2 | any | Get the TXT records (SPF, verification) of rbc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 rbc.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1979 | L2 | any | Get the TXT records (SPF, verification) of sber.ru | `dig sber.ru TXT +short` | Queries TXT records with the system resolver. |
| T1980 | L2 | any | Get the TXT records (SPF, verification) of sber.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 sber.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1981 | L2 | any | Get the TXT records (SPF, verification) of spbu.ru | `dig spbu.ru TXT +short` | Queries TXT records with the system resolver. |
| T1982 | L2 | any | Get the TXT records (SPF, verification) of spbu.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 spbu.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1983 | L2 | any | Get the TXT records (SPF, verification) of vk.com | `dig vk.com TXT +short` | Queries TXT records with the system resolver. |
| T1984 | L2 | any | Get the TXT records (SPF, verification) of vk.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 vk.com TXT +short` | Compare with the local resolver to find DNS problems. |
| T1985 | L2 | any | Get the TXT records (SPF, verification) of ya.ru | `dig ya.ru TXT +short` | Queries TXT records with the system resolver. |
| T1986 | L2 | any | Get the TXT records (SPF, verification) of ya.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ya.ru TXT +short` | Compare with the local resolver to find DNS problems. |
| T1987 | L2 | any | Get the allowed certificate authorities of croc.ru | `dig croc.ru CAA +short` | Queries CAA records with the system resolver. |
| T1988 | L2 | any | Get the allowed certificate authorities of croc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 croc.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T1989 | L2 | any | Get the allowed certificate authorities of example.com | `dig example.com CAA +short` | Queries CAA records with the system resolver. |
| T1990 | L2 | any | Get the allowed certificate authorities of example.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 example.com CAA +short` | Compare with the local resolver to find DNS problems. |
| T1991 | L2 | any | Get the allowed certificate authorities of github.com | `dig github.com CAA +short` | Queries CAA records with the system resolver. |
| T1992 | L2 | any | Get the allowed certificate authorities of github.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 github.com CAA +short` | Compare with the local resolver to find DNS problems. |
| T1993 | L2 | any | Get the allowed certificate authorities of gosuslugi.ru | `dig gosuslugi.ru CAA +short` | Queries CAA records with the system resolver. |
| T1994 | L2 | any | Get the allowed certificate authorities of gosuslugi.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 gosuslugi.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T1995 | L2 | any | Get the allowed certificate authorities of habr.com | `dig habr.com CAA +short` | Queries CAA records with the system resolver. |
| T1996 | L2 | any | Get the allowed certificate authorities of habr.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 habr.com CAA +short` | Compare with the local resolver to find DNS problems. |
| T1997 | L2 | any | Get the allowed certificate authorities of itmo.ru | `dig itmo.ru CAA +short` | Queries CAA records with the system resolver. |
| T1998 | L2 | any | Get the allowed certificate authorities of itmo.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 itmo.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T1999 | L2 | any | Get the allowed certificate authorities of kernel.org | `dig kernel.org CAA +short` | Queries CAA records with the system resolver. |
| T2000 | L2 | any | Get the allowed certificate authorities of kernel.org from Google DNS 8.8.8.8 | `dig @8.8.8.8 kernel.org CAA +short` | Compare with the local resolver to find DNS problems. |
| T2001 | L2 | any | Get the allowed certificate authorities of mail.ru | `dig mail.ru CAA +short` | Queries CAA records with the system resolver. |
| T2002 | L2 | any | Get the allowed certificate authorities of mail.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 mail.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T2003 | L2 | any | Get the allowed certificate authorities of ozon.ru | `dig ozon.ru CAA +short` | Queries CAA records with the system resolver. |
| T2004 | L2 | any | Get the allowed certificate authorities of ozon.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ozon.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T2005 | L2 | any | Get the allowed certificate authorities of rbc.ru | `dig rbc.ru CAA +short` | Queries CAA records with the system resolver. |
| T2006 | L2 | any | Get the allowed certificate authorities of rbc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 rbc.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T2007 | L2 | any | Get the allowed certificate authorities of sber.ru | `dig sber.ru CAA +short` | Queries CAA records with the system resolver. |
| T2008 | L2 | any | Get the allowed certificate authorities of sber.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 sber.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T2009 | L2 | any | Get the allowed certificate authorities of spbu.ru | `dig spbu.ru CAA +short` | Queries CAA records with the system resolver. |
| T2010 | L2 | any | Get the allowed certificate authorities of spbu.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 spbu.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T2011 | L2 | any | Get the allowed certificate authorities of vk.com | `dig vk.com CAA +short` | Queries CAA records with the system resolver. |
| T2012 | L2 | any | Get the allowed certificate authorities of vk.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 vk.com CAA +short` | Compare with the local resolver to find DNS problems. |
| T2013 | L2 | any | Get the allowed certificate authorities of ya.ru | `dig ya.ru CAA +short` | Queries CAA records with the system resolver. |
| T2014 | L2 | any | Get the allowed certificate authorities of ya.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ya.ru CAA +short` | Compare with the local resolver to find DNS problems. |
| T2015 | L2 | any | Get the mail servers of croc.ru | `dig croc.ru MX +short` | Queries MX records with the system resolver. |
| T2016 | L2 | any | Get the mail servers of croc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 croc.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2017 | L2 | any | Get the mail servers of example.com | `dig example.com MX +short` | Queries MX records with the system resolver. |
| T2018 | L2 | any | Get the mail servers of example.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 example.com MX +short` | Compare with the local resolver to find DNS problems. |
| T2019 | L2 | any | Get the mail servers of github.com | `dig github.com MX +short` | Queries MX records with the system resolver. |
| T2020 | L2 | any | Get the mail servers of github.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 github.com MX +short` | Compare with the local resolver to find DNS problems. |
| T2021 | L2 | any | Get the mail servers of gosuslugi.ru | `dig gosuslugi.ru MX +short` | Queries MX records with the system resolver. |
| T2022 | L2 | any | Get the mail servers of gosuslugi.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 gosuslugi.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2023 | L2 | any | Get the mail servers of habr.com | `dig habr.com MX +short` | Queries MX records with the system resolver. |
| T2024 | L2 | any | Get the mail servers of habr.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 habr.com MX +short` | Compare with the local resolver to find DNS problems. |
| T2025 | L2 | any | Get the mail servers of itmo.ru | `dig itmo.ru MX +short` | Queries MX records with the system resolver. |
| T2026 | L2 | any | Get the mail servers of itmo.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 itmo.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2027 | L2 | any | Get the mail servers of kernel.org | `dig kernel.org MX +short` | Queries MX records with the system resolver. |
| T2028 | L2 | any | Get the mail servers of kernel.org from Google DNS 8.8.8.8 | `dig @8.8.8.8 kernel.org MX +short` | Compare with the local resolver to find DNS problems. |
| T2029 | L2 | any | Get the mail servers of mail.ru | `dig mail.ru MX +short` | Queries MX records with the system resolver. |
| T2030 | L2 | any | Get the mail servers of mail.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 mail.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2031 | L2 | any | Get the mail servers of ozon.ru | `dig ozon.ru MX +short` | Queries MX records with the system resolver. |
| T2032 | L2 | any | Get the mail servers of ozon.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ozon.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2033 | L2 | any | Get the mail servers of rbc.ru | `dig rbc.ru MX +short` | Queries MX records with the system resolver. |
| T2034 | L2 | any | Get the mail servers of rbc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 rbc.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2035 | L2 | any | Get the mail servers of sber.ru | `dig sber.ru MX +short` | Queries MX records with the system resolver. |
| T2036 | L2 | any | Get the mail servers of sber.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 sber.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2037 | L2 | any | Get the mail servers of spbu.ru | `dig spbu.ru MX +short` | Queries MX records with the system resolver. |
| T2038 | L2 | any | Get the mail servers of spbu.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 spbu.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2039 | L2 | any | Get the mail servers of vk.com | `dig vk.com MX +short` | Queries MX records with the system resolver. |
| T2040 | L2 | any | Get the mail servers of vk.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 vk.com MX +short` | Compare with the local resolver to find DNS problems. |
| T2041 | L2 | any | Get the mail servers of ya.ru | `dig ya.ru MX +short` | Queries MX records with the system resolver. |
| T2042 | L2 | any | Get the mail servers of ya.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ya.ru MX +short` | Compare with the local resolver to find DNS problems. |
| T2043 | L2 | any | Get the name servers of croc.ru | `dig croc.ru NS +short` | Queries NS records with the system resolver. |
| T2044 | L2 | any | Get the name servers of croc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 croc.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2045 | L2 | any | Get the name servers of example.com | `dig example.com NS +short` | Queries NS records with the system resolver. |
| T2046 | L2 | any | Get the name servers of example.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 example.com NS +short` | Compare with the local resolver to find DNS problems. |
| T2047 | L2 | any | Get the name servers of github.com | `dig github.com NS +short` | Queries NS records with the system resolver. |
| T2048 | L2 | any | Get the name servers of github.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 github.com NS +short` | Compare with the local resolver to find DNS problems. |
| T2049 | L2 | any | Get the name servers of gosuslugi.ru | `dig gosuslugi.ru NS +short` | Queries NS records with the system resolver. |
| T2050 | L2 | any | Get the name servers of gosuslugi.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 gosuslugi.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2051 | L2 | any | Get the name servers of habr.com | `dig habr.com NS +short` | Queries NS records with the system resolver. |
| T2052 | L2 | any | Get the name servers of habr.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 habr.com NS +short` | Compare with the local resolver to find DNS problems. |
| T2053 | L2 | any | Get the name servers of itmo.ru | `dig itmo.ru NS +short` | Queries NS records with the system resolver. |
| T2054 | L2 | any | Get the name servers of itmo.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 itmo.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2055 | L2 | any | Get the name servers of kernel.org | `dig kernel.org NS +short` | Queries NS records with the system resolver. |
| T2056 | L2 | any | Get the name servers of kernel.org from Google DNS 8.8.8.8 | `dig @8.8.8.8 kernel.org NS +short` | Compare with the local resolver to find DNS problems. |
| T2057 | L2 | any | Get the name servers of mail.ru | `dig mail.ru NS +short` | Queries NS records with the system resolver. |
| T2058 | L2 | any | Get the name servers of mail.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 mail.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2059 | L2 | any | Get the name servers of ozon.ru | `dig ozon.ru NS +short` | Queries NS records with the system resolver. |
| T2060 | L2 | any | Get the name servers of ozon.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ozon.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2061 | L2 | any | Get the name servers of rbc.ru | `dig rbc.ru NS +short` | Queries NS records with the system resolver. |
| T2062 | L2 | any | Get the name servers of rbc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 rbc.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2063 | L2 | any | Get the name servers of sber.ru | `dig sber.ru NS +short` | Queries NS records with the system resolver. |
| T2064 | L2 | any | Get the name servers of sber.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 sber.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2065 | L2 | any | Get the name servers of spbu.ru | `dig spbu.ru NS +short` | Queries NS records with the system resolver. |
| T2066 | L2 | any | Get the name servers of spbu.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 spbu.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2067 | L2 | any | Get the name servers of vk.com | `dig vk.com NS +short` | Queries NS records with the system resolver. |
| T2068 | L2 | any | Get the name servers of vk.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 vk.com NS +short` | Compare with the local resolver to find DNS problems. |
| T2069 | L2 | any | Get the name servers of ya.ru | `dig ya.ru NS +short` | Queries NS records with the system resolver. |
| T2070 | L2 | any | Get the name servers of ya.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ya.ru NS +short` | Compare with the local resolver to find DNS problems. |
| T2071 | L2 | any | Get the zone authority record of croc.ru | `dig croc.ru SOA +short` | Queries SOA records with the system resolver. |
| T2072 | L2 | any | Get the zone authority record of croc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 croc.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2073 | L2 | any | Get the zone authority record of example.com | `dig example.com SOA +short` | Queries SOA records with the system resolver. |
| T2074 | L2 | any | Get the zone authority record of example.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 example.com SOA +short` | Compare with the local resolver to find DNS problems. |
| T2075 | L2 | any | Get the zone authority record of github.com | `dig github.com SOA +short` | Queries SOA records with the system resolver. |
| T2076 | L2 | any | Get the zone authority record of github.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 github.com SOA +short` | Compare with the local resolver to find DNS problems. |
| T2077 | L2 | any | Get the zone authority record of gosuslugi.ru | `dig gosuslugi.ru SOA +short` | Queries SOA records with the system resolver. |
| T2078 | L2 | any | Get the zone authority record of gosuslugi.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 gosuslugi.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2079 | L2 | any | Get the zone authority record of habr.com | `dig habr.com SOA +short` | Queries SOA records with the system resolver. |
| T2080 | L2 | any | Get the zone authority record of habr.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 habr.com SOA +short` | Compare with the local resolver to find DNS problems. |
| T2081 | L2 | any | Get the zone authority record of itmo.ru | `dig itmo.ru SOA +short` | Queries SOA records with the system resolver. |
| T2082 | L2 | any | Get the zone authority record of itmo.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 itmo.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2083 | L2 | any | Get the zone authority record of kernel.org | `dig kernel.org SOA +short` | Queries SOA records with the system resolver. |
| T2084 | L2 | any | Get the zone authority record of kernel.org from Google DNS 8.8.8.8 | `dig @8.8.8.8 kernel.org SOA +short` | Compare with the local resolver to find DNS problems. |
| T2085 | L2 | any | Get the zone authority record of mail.ru | `dig mail.ru SOA +short` | Queries SOA records with the system resolver. |
| T2086 | L2 | any | Get the zone authority record of mail.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 mail.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2087 | L2 | any | Get the zone authority record of ozon.ru | `dig ozon.ru SOA +short` | Queries SOA records with the system resolver. |
| T2088 | L2 | any | Get the zone authority record of ozon.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ozon.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2089 | L2 | any | Get the zone authority record of rbc.ru | `dig rbc.ru SOA +short` | Queries SOA records with the system resolver. |
| T2090 | L2 | any | Get the zone authority record of rbc.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 rbc.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2091 | L2 | any | Get the zone authority record of sber.ru | `dig sber.ru SOA +short` | Queries SOA records with the system resolver. |
| T2092 | L2 | any | Get the zone authority record of sber.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 sber.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2093 | L2 | any | Get the zone authority record of spbu.ru | `dig spbu.ru SOA +short` | Queries SOA records with the system resolver. |
| T2094 | L2 | any | Get the zone authority record of spbu.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 spbu.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2095 | L2 | any | Get the zone authority record of vk.com | `dig vk.com SOA +short` | Queries SOA records with the system resolver. |
| T2096 | L2 | any | Get the zone authority record of vk.com from Google DNS 8.8.8.8 | `dig @8.8.8.8 vk.com SOA +short` | Compare with the local resolver to find DNS problems. |
| T2097 | L2 | any | Get the zone authority record of ya.ru | `dig ya.ru SOA +short` | Queries SOA records with the system resolver. |
| T2098 | L2 | any | Get the zone authority record of ya.ru from Google DNS 8.8.8.8 | `dig @8.8.8.8 ya.ru SOA +short` | Compare with the local resolver to find DNS problems. |
| T2099 | L2 | any | Reverse lookup of IP 1.1.1.1 | `dig -x 1.1.1.1 +short` | PTR record for the address. |
| T2100 | L2 | any | Reverse lookup of IP 192.168.56.10 | `dig -x 192.168.56.10 +short` | PTR record for the address. |
| T2101 | L2 | any | Reverse lookup of IP 77.88.8.8 | `dig -x 77.88.8.8 +short` | PTR record for the address. |
| T2102 | L2 | any | Reverse lookup of IP 8.8.8.8 | `dig -x 8.8.8.8 +short` | PTR record for the address. |
| T2103 | L2 | any | Trace DNS resolution of croc.ru from the root servers | `dig croc.ru +trace` | Shows each delegation step. |
| T2104 | L2 | any | Trace DNS resolution of example.com from the root servers | `dig example.com +trace` | Shows each delegation step. |
| T2105 | L2 | any | Trace DNS resolution of github.com from the root servers | `dig github.com +trace` | Shows each delegation step. |
| T2106 | L2 | any | Trace DNS resolution of gosuslugi.ru from the root servers | `dig gosuslugi.ru +trace` | Shows each delegation step. |
| T2107 | L2 | any | Trace DNS resolution of habr.com from the root servers | `dig habr.com +trace` | Shows each delegation step. |
| T2108 | L2 | any | Trace DNS resolution of itmo.ru from the root servers | `dig itmo.ru +trace` | Shows each delegation step. |
| T2109 | L2 | any | Trace DNS resolution of kernel.org from the root servers | `dig kernel.org +trace` | Shows each delegation step. |
| T2110 | L2 | any | Trace DNS resolution of mail.ru from the root servers | `dig mail.ru +trace` | Shows each delegation step. |
| T2111 | L2 | any | Trace DNS resolution of ozon.ru from the root servers | `dig ozon.ru +trace` | Shows each delegation step. |
| T2112 | L2 | any | Trace DNS resolution of rbc.ru from the root servers | `dig rbc.ru +trace` | Shows each delegation step. |
| T2113 | L2 | any | Trace DNS resolution of sber.ru from the root servers | `dig sber.ru +trace` | Shows each delegation step. |
| T2114 | L2 | any | Trace DNS resolution of spbu.ru from the root servers | `dig spbu.ru +trace` | Shows each delegation step. |
| T2115 | L2 | any | Trace DNS resolution of vk.com from the root servers | `dig vk.com +trace` | Shows each delegation step. |
| T2116 | L2 | any | Trace DNS resolution of ya.ru from the root servers | `dig ya.ru +trace` | Shows each delegation step. |
