# Laborator: funcții, metode și importuri pe web
# Student: <Chirița William>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time
import requests

#Exercițiul 9
response=requests.get(BASE_URL, timeout=TIMEOUT)
print(response.status_code)#Atribut
print(response.ok)#Atribut
print(response.url)#Atribut
print(response.encoding)#Atribut

time.sleep(1)

#Exercițiul 10
response=requests.get(ECHO_URL, timeout=TIMEOUT)
response.raise_for_status()
try:
    requests.get(ECHO_URL + "/this-page-does-not-exist" , timeout=TIMEOUT).raise_for_status()
except requests.HTTPError:
    print ("eroare")

time.sleep(1)

#Exercițiul 11
response=requests.get(BASE_URL, timeout=TIMEOUT)
for nume, valoare in response.headers.items():
    print (f"{nume},{valoare}")

time.sleep(1)

#Exercițiul 12
response=requests.get(BASE_URL, timeout=TIMEOUT)
n=response.headers.get("Server","lipsește" )
u=response.headers.get("Content-Type","lipsește" )
print (n)
print(u)
g=response.headers.get("content-type", "lipsește")
print (g)
#Pot observa ca "Content-Type" și "content-type" afișează același lucru din cauza ca antetul http nu ține 
#cont de litere mici sau mari.

time.sleep(1)

#Exercițiul 13
response=requests.get(BASE_URL, timeout=TIMEOUT)
c=response.text.lower().count("cyber")
print (c)
#Putem înlanțui .lower() și .count() deoarece response.text este un șir de text string, iar metoda 
#.lower() tot returneaza un șir string așa ca putem folosi .count().

time.sleep(1)

#Exercițiul 14
response=requests.get(BASE_URL, timeout=TIMEOUT)
start = response.text.find("<title>") + len("<title>")
end = response.text.find("</title>")
d=response.text[start:end].strip()
print(d)

time.sleep(1)

#Exercițiul 15
response=requests.get(BASE_URL, timeout=TIMEOUT)
lines=response.text.splitlines()
print(len(lines))
cea_mai_mare=max(lines, key=len)
lungimea_cea_mai_mare=len(cea_mai_mare)
print (lungimea_cea_mai_mare)

time.sleep(1)

#Exercițiul 16
response=requests.get(BASE_URL, timeout=TIMEOUT)
if response.url.startswith("https://"):
    print ("Conexiune securizată ")
else:
    print ("Conexiune nesecurizată")

time.sleep(1)

#Exercițiul 17
response=requests.get("http://cybercor.org" , timeout=TIMEOUT)
for res in response.history:
    print (f"{res.status_code}-{res.url}")
print (f"{response.url}")

time.sleep(1)

#Exercițiul 18
response=requests.get(BASE_URL, timeout=TIMEOUT)
print (len(response.text)) 
time.sleep(1)
response1=requests.head(BASE_URL, timeout=TIMEOUT) 
print (len(response1.text))
#requests.get() returnează antetele și corpil, pe când requests.head() returnează doar antetele.

time.sleep(1)

#Exercițiul 19
response=requests.get(BASE_URL, timeout=TIMEOUT)
if len(response.cookies)>0:
    for cookie in response.cookies:
        print (f"{cookie.name}-{cookie.secure}")
else:
    print("Niciun cookie setat")

time.sleep(1)

#Exercițiul 20
session=requests.Session() 
session.headers.update({"User-Agent": "WebLab-Chirita William"})
response=session.get(ECHO_URL.rstrip('/') + "/headers", timeout=TIMEOUT)
print (response.json())

