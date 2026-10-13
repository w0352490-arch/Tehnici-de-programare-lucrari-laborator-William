import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login."""
    if host.startswith("http://"):
        host = "https://" + host
    if path.startswith("/"):
        path = "/" + path
        print(host + path)
    pass


def is_https(url):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    if url.startswitch("https://"):
        return True
    else:
        return False
    pass


def show_response(url):
    """Trimite un GET la url și afișează statusul și Content-Type."""
    try:
        response=requests.get(url)
        print(f"Status:{response.status_code}, Content-Type: {response.get('Content-Type')}")
    except Exception as w:
        print(f"Eroare:{url}")
    pass


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    r=requests.get(url)
    return{ 
        "status" :r.status_code
        "content_type" : r.get("Content-Type"),
        "length" : len(r.content),
        "server" : r.headers.get("Server")
    }
    pass


def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
G=SITES
    for site in G:
        try:
            response=requests.get(site)
            print(f"Site: {site}, Status: {response.status_code}")
        except Exception as e:
            print(f"Site: {site}, Eroare: {e}")
pass
    pass


def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
H=SECURITY_HEADERS
    present=[]
    missing=[]
    E=requests.get(url)
    for header in H:
        if header in E.headers:
            present.append(header)
        else:
            missing.append(header)
    score=len(present)/len(H)*100
    return {"present": present, "missing": missing, "score": score}

    pass


def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
for g in range(attempts):
        try:
           res=requests.get(url)
           return {"status": res.status_code, "attempts": g+1}
        except Exception as e:
            if g == attempts - 1:
                return {"status": None, "attempts": attempts} 
    pass
