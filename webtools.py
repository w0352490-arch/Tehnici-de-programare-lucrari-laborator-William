# Laborator: funcții, metode și importuri pe web
# Student: <Chirița William>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
DEFAULT_HEADERS = {"User-Agent": "WebLab-Student"}
import json
import re
import socket
import ssl
import requests


def fetch(url):
    """Returnează obiectul răspuns pentru adresa url"""
    response = requests.get(url, timeout=TIMEOUT)
    return response

def get_status(url):
    """Returnează codul de stare HTTP pentru adresa url."""
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

def get_title(html):
    """Extrage si returneaza titlul paginii dintr-un text HTML."""
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    d=html[start:end].strip()
    return d

def security_headers(url):
    """verifică prezența antetelor și returnează un dicționar cu True/False"""
    headers=["Strict-Transport-Security","Content-Security-Policy", "X-Frame-Options","X-Content-Type-Options","Referrer-Policy"]
    rezultat={}
    try:
        response=requests.get(url, timeout=TIMEOUT)
        for header in headers:
            rezultat[header]=header in response.headers
    except Exception:
        print ("eroare la conectare")
        for header in headers:
            rezultat[header]=False
    return rezultat

def fetch(url):
    return requests.get(url, headers=DEFAULT_HEADERS, timeout=TIMEOUT)

def resolve(hostname):
    import socket, ssl
    """Returnează adresa IP asociată unui nume de domeniu."""
    return socket.gethostbyname(hostname)
ip = resolve("")
print(ip)

def get_header(url, name, default="lipsește"):

    try:
        response=requests.get(url, timeout=TIMEOUT)
        return response.header.get(name, default)
    except Exception:
        return default
head=get_header(BASE_URL,name="Server")
print (head)

from urllib.parse import urljoin, urlparse
def split_links(links, domain):
    """Separă o listă de legături în interne și externe, raportate la un domeniu de bază."""
    internal=[]
    external=[]
    f = urlparse(domain).netloc or domain
    for link in links:
        g=urljoin(domain,link)
        if urlparse(g).netloc==f:
            internal.append(g)
        else:
            external.append(f)
    return internal, external
response = requests.get(BASE_URL, timeout=TIMEOUT)
toate_legaturile = re.findall(r'href="([^"]+)"', response.text)
interne, externe = split_links(toate_legaturile, BASE_URL)
print (interne)
print (externe)

def score_headers(results):
    """Numără câte antete True are dicționarul""" 
    score= sum(1 for present in results.values() if present)
    total= len(results)
    return f"{score}/{total}"
p=score_headers(security_headers(BASE_URL))
print(p)

import socket, ssl
from datetime import datetime, timezone
def cert_days_left(hostname):
    """Calculează numărul de zile rămase până la expirarea certificatului SSL/TLS al unui domeniu"""
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            expire_sec = ssl.cert_time_to_seconds(ssock.getpeercert()["notAfter"])
            expire_date = datetime.fromtimestamp(expire_sec, tz=timezone.utc)
            return (expire_date - datetime.now(timezone.utc)).days
print(cert_days_left("cybercor.org"))

from urllib.parse import urljoin, urlparse
def split_links(links, domain):
    """Separă o listă de legături în interne și externe, raportate la un domeniu de bază."""
    internal=[]
    external=[]
    f = urlparse(domain).netloc or domain
    for link in links:
        g=urljoin(domain,link)
        if urlparse(g).netloc==f:
            internal.append(g)
        else:
            external.append(f)
    return internal, external
response = requests.get(BASE_URL, timeout=TIMEOUT)
toate_legaturile = re.findall(r'href="([^"]+)"', response.text)
interne, externe = split_links(toate_legaturile, BASE_URL)
print (interne)
print (externe)

import socket
def resolve(hostname):
    """Returnează adresa IP asociată unui nume de domeniu."""
    return socket.gethostbyname(hostname)
ip = resolve("")
print(ip)

def fetch_robots(base):
    """returneaza textul fișierului /robots.txt sau none"""
    try:
        results=requests.get(f"{base}/robots.txt" , timeout=TIMEOUT)
        return results.text
    except Exception:
        return None
def disallowed_paths(robots_text):
    """returneaza lista tuturor Dissalow"""
    if not robots_text:
        return []
    paths=[]
    for line in robots_text.splitlines():
        if "Disallow" in line:
            path=line.split("Disallow:")[1].strip()
            if path:
                paths.append(path)
    return paths
robots=fetch_robots(BASE_URL)
paths=disallowed_paths(robots)
print (paths)

def check_paths(base, paths):
    """returnează un dicționar cu codul de stare HTTP pentrtu fiecare cale din listă"""
    rezultat={}
    for path in paths:
        UY= base + path
        response = requests.get(UY, timeout=TIMEOUT)
        rezultat[path]=response.status_code  
    return rezultat

import json, re
from urllib.parse import urlparse

def site_report(url):
    domain = urlparse(url).netloc or urlparse(url).path
    res = fetch(f"http://{domain}")

    links = re.findall(r'href=["\'](.*?)["\']', res.text)
    interne, externe = split_links(links, domain)

    report = {
        "status_code": res.status_code,
        "final_url": res.url,
        "title": get_title(res.text),
        "ip_address": resolve(domain),
        "redirect_chain": [r.url for r in res.history] + [res.url],
        "security_score": score_headers(security_headers(url)),
        "cert_days_left": cert_days_left(domain),
        "links": {"internal": len(interne), "external": len(externe)},
        "disallowed_paths": disallowed_paths(fetch_robots(url))
    }
    print(f"=== Raport site:\n{res.url} ===")
    print(json.dumps(report, indent=2, ensure_ascii=False))

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

def check_paths(base, path_list):
    return {p: get_status (f"{base}{p}") for p in path_list}

if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
