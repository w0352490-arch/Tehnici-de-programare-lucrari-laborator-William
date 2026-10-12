# Laborator: funcții, metode și importuri pe web
# Student: <Chirița William>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import time

#Exercițiul 1
import requests 
print (requests.__version__)
import urllib.request
#Requests a avut nevoie de pip install din cauza că e o bibliotecă terță aparte care nu vine inclusă 
#implicit în Python, dar urllib.request face parte din bibloteca de bază a Python.

#Exercițiul 2
import requests
raspuns=requests.get(BASE_URL, timeout=TIMEOUT)
print (raspuns.status_code)
time.sleep(1)
from requests import get
raspuns2=get(BASE_URL, timeout=TIMEOUT)
print (raspuns2.status_code)
#Primul stil oferă claritate și evită suprapunerea cu alte funcții ce folosesc get. Al doilea stil ne 
# permite să apelăm funcția direct, fara a folosi ”requests” la fiecare apelare. 
time.sleep(1)

#Exercițiul 3   
import requests as rq 
descarcare=rq.get(BASE_URL, timeout=TIMEOUT)    
print (descarcare)
#Un alias face un cod mai usor de citit când e mai ușor de recunoscut pentru mai mulți oameni și 
#modulul la care este folosit aliasul e lung și mai greu de scris. Un alias face un cod mai greu de citit 
#cand se aseamana cu un alias folosit precedent la alt modul și când nu are semnificație contextuală.

time.sleep(1)

#Exercițiul 4
i = urllib.request.Request(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'})
x= urllib.request.urlopen(i, timeout=TIMEOUT)
y=x.status
print (y)
r=x.read() 
u=r.decode("utf-8")
print (u)  

time.sleep(1)

#Exercițiul 5
print(dir(requests))
#get-este o functie a modulului requests ce trimite cereri HTTP
#response-clasă ce reprezinta raspunsul primit în urma a unei cereri 
#exceptions-submodul intern ce contine toate tipurile de erori specifice

#Exercițiul 6
x=help(requests.get)
print (x)
raspuns=requests.get(BASE_URL, timeout=5)
print (raspuns)

#Exercițiul 7
import time
x=time.perf_counter()
raspuns=requests.get(BASE_URL, timeout=TIMEOUT)
y=time.perf_counter()
timpul=y-x
print (timpul)
durata=raspuns.elapsed.total_seconds()
print(durata)
#time.perf_counter() masoara durata totala la nivelul lui python, dar raspuns.elapsed.total_seconds() 
#masoara de la trimitere cererii  pana la primitere raspunsului.

time.sleep(1)

#Exercițiul 8
try:
    import bs4
except ImportError:
    print ("Instalați modulul cu: pip install beautifulsoup4")