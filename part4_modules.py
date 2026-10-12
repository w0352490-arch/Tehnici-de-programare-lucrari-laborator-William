# Laborator: funcții, metode și importuri pe web
# Student: <Chirița William>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests
import re
import hashlib


#Exercițiul 35
def parse(url):
    """Analizeză adresa url și afișează scheme, netloc, path, query și fragment."""
    from urllib.parse import urlparse
    parse = urlparse(url)
    print(f"{parse.scheme}")
    print(f"{parse.netloc}")
    print(f"{parse.path}")
    print(f"{parse.query}")
    print(f"{parse.fragment}")

parse("https://cybercor.org/path?x=1#top")

time.sleep(1)

#Exercițiul 36
from urllib.parse import urljoin
def link(url, pathx):
    """transforma lista de legaturi relative in URl-uri complete pornind de la base_url"""
    f=[]
    for path in pathx:
        urlf = urljoin(url, path)
        f.append(urlf)
    return f

relativ=["/about", "contact.html", "../index.html"]
v=link(BASE_URL, relativ)
print (v)

time.sleep(1)

#Exercițiul 37
def extract_links(html):
    """Extrage și returnează o listă cu toate legăturile unice (fără duplicate) dintr-un text HTML."""
    h=re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(h))
p=requests.get (BASE_URL, timeout=TIMEOUT)
g=extract_links(p.text)
print (g)

time.sleep(1)

#Exercițiul 38
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

time.sleep(1)

#Exercițiul 39
from html.parser import HTMLParser
class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        # HTMLParser convertește automat 'tag' în litere mici (ex: 'IMG' devine 'img')
        if tag == "img":
            src = dict(attrs).get("src")
            if src:
                self.images.append(src)
response = requests.get(BASE_URL, timeout=TIMEOUT)
finder_real = ImageFinder()
finder_real.feed(response.text)

print(len(finder_real.images))
for src in finder_real.images:
    print(src)

time.sleep(1)

#Exercițiul 40
def page_fingerprint(url):
    """Calculează și returnează amprenta SHA-256 (hash) a conținutului unei pagini web."""
    res = requests.get(url, timeout=TIMEOUT)
    return hashlib.sha256(response.content).hexdigest()
hash1 = page_fingerprint(BASE_URL)
hash2 = page_fingerprint(BASE_URL)

print(hash1)
print(hash2)
print(hash1 == hash2)

time.sleep(1)


#Exercițiul 41
import json
import requests
def save_and_read_header(url, header_to_read, filename = "headers.json"):
    """Obține antetele de la URL, le salvează în JSON, apoi citește un antet specific din fișier."""
    response = requests.get(url, timeout=TIMEOUT)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(dict(response.headers), file, indent=2)
    with open(filename, "r", encoding="utf-8") as file:
        loaded_headers = json.load(file)        
    return loaded_headers.get(header_to_read, "Antet negăsit")
val = save_and_read_header(BASE_URL, "Content-Type")
print (f"{val}")

time.sleep(1)

#Exercițiul 42
import socket
def resolve(hostname):
    """Returnează adresa IP asociată unui nume de domeniu."""
    return socket.gethostbyname(hostname)
ip = resolve("")
print(ip)

time.sleep(1)

#Exercițiul 43
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











        
