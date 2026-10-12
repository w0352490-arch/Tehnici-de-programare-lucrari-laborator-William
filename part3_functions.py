# Laborator: funcții, metode și importuri pe web
# Student: <Chirița William>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests

#Exercițiul 21
def fetch(url):
    """Returnează obiectul răspuns pentru adresa url"""
    response = requests.get(url, timeout=TIMEOUT)
    return response
respons=fetch(BASE_URL)
print(respons.status_code)

time.sleep(1)

#Exercițiul 22
def get_status(url):
    """Returnează codul de stare HTTP pentru adresa url."""
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
status=get_status(BASE_URL + "/")
print (status)
time.sleep(1)
status1=get_status(BASE_URL + "/robots.txt")
print(status1)
time.sleep(1)
status2=get_status(BASE_URL + "/sitemap.xml")
print (status2)

time.sleep(1)

#Exercițiul 23
def fetch(url, timeout=10):
     """Returnează obiectul răspuns pentru adresa url"""
     response = requests.get(url, timeout=timeout)
     return response
f=fetch (BASE_URL)
print (f)
time.sleep(1)
g=fetch (BASE_URL, timeout=3)
print (g)

time.sleep(1)

#Exercițiul 24
def get_title(html):
    """Extrage si returneaza titlul paginii dintr-un text HTML."""
    start = html.text.find("<title>") + len("<title>")
    end = html.text.find("</title>")
    d=html.text[start:end].strip()
    return d
response = requests.get(BASE_URL, timeout=TIMEOUT)
k=get_title(response)
print (k)

time.sleep(1)

#Exercițiul 25
def get_title(html):
    """Extrage si returneaza titlul paginii dintr-un text HTML."""
    start = html.text.find("<title>") + len("<title>")
    end = html.text.find("</title>")
    d=html.text[start:end].strip()
    return d
response = requests.get(BASE_URL, timeout=TIMEOUT)
k=get_title(response)
help(get_title)
print (k)

time.sleep(1)

#Exercițiul 26
def get_status(url: str) -> int: 
     """Returnează codul de stare HTTP pentru adresa url."""
     response = requests.get(url, timeout=TIMEOUT)
     return response.status_code
try:
    status= get_status(123)
    print(status)
except Exception:
    print ("eroare")
#Adnotările de tip nu opresc codul doar indică ce ar trebui să se întâmple.

time.sleep(1)

#Exercițiul 27
def page_exists(url):
    """returnează True sau False în dependență de existența a unei erori sau nu"""
    try:
        response = requests.get(url, timeout=TIMEOUT)
        return response
    except requests.RequestException:
        print ("eroare")
page_exists("https://this-domain-does-not-exist.invalid")

time.sleep(1)

#Exercițiul 28
def check_paths(base, paths):
    """returnează un dicționar cu codul de stare HTTP pentrtu fiecare cale din listă"""
    rezultat={}
    for path in paths:
        UY= base + path
        response = requests.get(UY, timeout=TIMEOUT)
        rezultat[path]=response.status_code  
    return rezultat
pathss=["/", "/robots.txt", "/sitemap.xml"]
n=check_paths(BASE_URL, pathss )
print(n)

time.sleep(1)

#Exercițiul 29
def get_header(url, name, default="lipsește"):

    try:
        response=requests.get(url, timeout=TIMEOUT)
        return response.header.get(name, default)
    except Exception:
        return default
head=get_header(BASE_URL,name="Server")
print (head)

time.sleep(1)

#Exercițiul 30
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

rezul =  security_headers(BASE_URL)
print(rezul)

time.sleep(1)

#Exercițiul  31
def score_headers(results):
    """Numără câte antete True are dicționarul""" 
    score= sum(1 for present in results.values() if present)
    total= len(results)
    return f"{score}/{total}"
p=score_headers(security_headers(BASE_URL))
print(p)

time.sleep(1)

#Execițiul 32
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

time.sleep(1)

#Exercițiul 33
def response_times(*urls):
    """returneaza un dicționar cu timpul de raspuns pentru fiecare url"""
    results={}
    for url in urls:
        try:
            start=time.perf_counter()
            requests.get(url, timeout=TIMEOUT)
            end=time.perf_counter()
            results[url]=end-start
        except Exception:
            results[url]=none
    return results
c=response_times(BASE_URL, ECHO_URL)
print (c)

#Exercițiul 34
def log(message, **details):
    """Afișează un mesaj urmat de perechile cheie=valoare din details, separate prin ' | '."""
    if details:
        formatted_details = " | ".join(f"{k}={v}" for k, v in details.items())
        print(f"{message} | {formatted_details}")
    else:
        print(message)
log("verificat", url=BASE_URL, status=200)
    
        







