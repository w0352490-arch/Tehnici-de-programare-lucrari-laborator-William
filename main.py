# Laborator: funcții, metode și importuri pe web
# Student: <Chirița William>
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde
import webtools 
import time
#Exercițiul 44
f=webtools.get_title(webtools.fetch(BASE_URL).text)
print(f)

time.sleep(1)

#Exercițiul 45
from webtools import get_title, security_headers
# Dacă main.py ar avea o funcție get_title proprie, ultima definită sau importată 
# o va suprascrie pe cealaltă.

#Exercițiul 46
#Când rulezi python webtools.py direct, Python setează automat variabila specială
# __name__ la valoarea "__main__", ceea ce face ca condiția if să fie adevărată și 
# autotestul să se execute.

#Exercițiul 47
from webtools import DEFAULT_HEADERS, fetch, get_title
print("Antetele implicite sunt:", DEFAULT_HEADERS)
BASE_URL = "https://cybercor.org"
html_content = fetch(BASE_URL).text
print (get_title(html_content))

#Exercițiul 48
import argparse
from webtools import DEFAULT_HEADERS, fetch, get_title
parser = argparse.ArgumentParser(description="Instrument pentru analiză web")
parser.add_argument("url", help="URL-ul țintă pentru analiză")
args=parser.parse_args()
print("Antetele implicite:", DEFAULT_HEADERS)
response = fetch(args.url)
titlu = get_title(response.text)
print(f"{args.url} {titlu}")


    # --- Exercițiul 49: Raport CSV ---
import csv
from datetime import datetime
from webtools import check_paths
paths = ["/", "/admin", "/robots.txt", "/login"]
results = check_paths(BASE_URL, paths)
now = datetime.now().isoformat()
with open("report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["path", "status", "checked_at"])
    writer.writerows([[path, status, now] for path, status in results.items()])

#Exercițiul 50
import sys
from webtools import site_report
if __name__ == "__main__":
  url = sys.argv[1] if len(sys.argv) > 1 else BASE_URL
  site_report(url)
