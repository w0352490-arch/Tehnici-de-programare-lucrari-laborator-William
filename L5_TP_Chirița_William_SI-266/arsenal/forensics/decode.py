#A1
s = "Salut"
b = s.encode()          
k=b.hex()
print (k)
print (bytes.fromhex(k))

#A2
import re
import base64
def ghici_strat(s):
    if re.search(r'%[0-9a-fA-F]{2}', s):
        print("url")
        return "url"       
    if re.search(r'^([0-9a-fA-F]{2})+$', s):
        print("hex")
        return "hex"
    try:
        if isinstance(s, str):
            s_bytes = s.encode('utf-8')
        else:
            s_bytes = s
        base64.b64decode(s_bytes, validate=True)
        return "base64"
    except Exception:
        pass       
    if re.search(r'^[A-Za-z0-9+/=]+$', s):
        print("base64")
        return "base64"      
    return "necunoscut"
print(ghici_strat("%2Fetc"))
print(ghici_strat("48656c6c6f"))  

#A3
import base64
from urllib.parse import unquote
def desfa(s):
    strat = ghici_strat(s)
    if strat=='base64':
        b=base64.b64decode(s)
    elif strat=='hex':
        b=bytes.fromhex(s)
    elif strat=='url':
        b=unquote(s).encode()
    else:
        b = s.encode() if isinstance(s, str) else s
    return strat, b

#A4
def citibil(b):
    return all(32 <= c < 127 for c in b)
val = "NTM1OTU3NTk="
for _ in range(8):
    strat, b = desfa(val)
    if citibil (b):
        print(b.decode())
        break
    else:
        val = b.decode()

#A5
date =  open("probe/xor.bin", "rb").read()
for k in range(256):
    clar = bytes(b ^ k for b in date)
    if citibil(clar):
        print ("cheie:", k, clar.decode())


#A6
import hashlib
tinta = open("probe/hashuri.txt").readline().strip()
print(len(tinta))
for cuv in open("probe/wordlist.txt", encoding="latin1"):
    cuv = cuv.strip()
    if hashlib.md5(cuv.encode()).hexdigest()==tinta:
        print ("gasit:", cuv)
        break

#A7
if __name__ == "__main__":
    import argparse, json
    p = argparse.ArgumentParser()
    p.add_argument("intrare")          
    p.add_argument("--fisier", action="store_true")
    a = p.parse_args()
    rezultat = open(a.intrare, "r", encoding="utf-8").read() if a.fisier else a.intrare
    json.dump({"strat": "forensics", "rezultat": rezultat}, open("arsenal/forensics/fisa.json", "w"))
