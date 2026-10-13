from checker import build_url, check_headers, is_https, retry_check, scan_sites, show_response, check_site, scan_sites, check_headers, retry_check
# Partea 1: apeluri pentru build_url și is_https
g=build_url("https://example.com", "/Login")
print (g)
u=is_https("https://example.com")
print (u)
# Partea 2: apeluri pentru show_response
f=show_response("https://httpbin.org/html")
print(f)
# Partea 3: apeluri pentru check_site
h=check_site("https://httpbin.org/html")
print(h)
# Partea 4: apelul scan_sites()
p= scan_sites("https://httpbin.org/html")
print(p)
# Partea 5: apeluri pentru check_headers
l=check_headers()
print(l)
# Partea 6: apeluri pentru retry_check
k=retry_check("https://httpbin.org/status/200", retries=5, delays=3)
print(k)


