# Networking: HTTP (28 tasks)

[Back to index](../README.md)

| ID | Level | Distro | Task | Command | Note |
|----|-------|--------|------|---------|------|
| T2117 | L2 | any | Show HTTP response headers of croc.ru | `curl -sI https://croc.ru` | Status code, server and redirects. |
| T2118 | L2 | any | Show HTTP response headers of example.com | `curl -sI https://example.com` | Status code, server and redirects. |
| T2119 | L2 | any | Show HTTP response headers of github.com | `curl -sI https://github.com` | Status code, server and redirects. |
| T2120 | L2 | any | Show HTTP response headers of gosuslugi.ru | `curl -sI https://gosuslugi.ru` | Status code, server and redirects. |
| T2121 | L2 | any | Show HTTP response headers of habr.com | `curl -sI https://habr.com` | Status code, server and redirects. |
| T2122 | L2 | any | Show HTTP response headers of itmo.ru | `curl -sI https://itmo.ru` | Status code, server and redirects. |
| T2123 | L2 | any | Show HTTP response headers of kernel.org | `curl -sI https://kernel.org` | Status code, server and redirects. |
| T2124 | L2 | any | Show HTTP response headers of mail.ru | `curl -sI https://mail.ru` | Status code, server and redirects. |
| T2125 | L2 | any | Show HTTP response headers of ozon.ru | `curl -sI https://ozon.ru` | Status code, server and redirects. |
| T2126 | L2 | any | Show HTTP response headers of rbc.ru | `curl -sI https://rbc.ru` | Status code, server and redirects. |
| T2127 | L2 | any | Show HTTP response headers of sber.ru | `curl -sI https://sber.ru` | Status code, server and redirects. |
| T2128 | L2 | any | Show HTTP response headers of spbu.ru | `curl -sI https://spbu.ru` | Status code, server and redirects. |
| T2129 | L2 | any | Show HTTP response headers of vk.com | `curl -sI https://vk.com` | Status code, server and redirects. |
| T2130 | L2 | any | Show HTTP response headers of ya.ru | `curl -sI https://ya.ru` | Status code, server and redirects. |
| T2131 | L3 | any | Measure HTTPS response time of croc.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://croc.ru` | Splits time into DNS, TCP, TLS and total. |
| T2132 | L3 | any | Measure HTTPS response time of example.com | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://example.com` | Splits time into DNS, TCP, TLS and total. |
| T2133 | L3 | any | Measure HTTPS response time of github.com | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://github.com` | Splits time into DNS, TCP, TLS and total. |
| T2134 | L3 | any | Measure HTTPS response time of gosuslugi.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://gosuslugi.ru` | Splits time into DNS, TCP, TLS and total. |
| T2135 | L3 | any | Measure HTTPS response time of habr.com | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://habr.com` | Splits time into DNS, TCP, TLS and total. |
| T2136 | L3 | any | Measure HTTPS response time of itmo.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://itmo.ru` | Splits time into DNS, TCP, TLS and total. |
| T2137 | L3 | any | Measure HTTPS response time of kernel.org | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://kernel.org` | Splits time into DNS, TCP, TLS and total. |
| T2138 | L3 | any | Measure HTTPS response time of mail.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://mail.ru` | Splits time into DNS, TCP, TLS and total. |
| T2139 | L3 | any | Measure HTTPS response time of ozon.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://ozon.ru` | Splits time into DNS, TCP, TLS and total. |
| T2140 | L3 | any | Measure HTTPS response time of rbc.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://rbc.ru` | Splits time into DNS, TCP, TLS and total. |
| T2141 | L3 | any | Measure HTTPS response time of sber.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://sber.ru` | Splits time into DNS, TCP, TLS and total. |
| T2142 | L3 | any | Measure HTTPS response time of spbu.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://spbu.ru` | Splits time into DNS, TCP, TLS and total. |
| T2143 | L3 | any | Measure HTTPS response time of vk.com | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://vk.com` | Splits time into DNS, TCP, TLS and total. |
| T2144 | L3 | any | Measure HTTPS response time of ya.ru | `curl -o /dev/null -s -w 'dns %{time_namelookup} connect %{time_connect} tls %{time_appconnect} total %{time_total}\n' https://ya.ru` | Splits time into DNS, TCP, TLS and total. |
