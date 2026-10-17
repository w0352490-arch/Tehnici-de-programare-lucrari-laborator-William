#B1
def tip_real(cale):
    cap = open(cale, "rb").read(8)
    if cap.startswith(b"%PDF"):
        return "pdf"
    if cap.startswith(b"\x89PNG"):
        return "png"
    if cap.startswith(b"\xff\xd8"):
        return "jpeg"
    if cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    return cap.hex()
print(tip_real("probe/foto.jpg"))

#B2
import re
date = open("probe/ascuns.png", "rb").read()
for m in re.findall(rb"[ -~]{4,}", date):
    print(m.decode(errors="ignore"))

#B3
from PIL import Image
from PIL.ExifTags import TAGS
exif = Image.open("probe/foto.jpg")._getexif() or {}
for id, val in exif.items():
    print(TAGS.get(id, id), "=", val)
gps = exif.get(34853, {})
if gps:
    print("Latitudine:", (gps[2][0] + gps[2][1]/60 + gps[2][2]/3600) * (1 if gps.get(1) == 'N' else -1))
    print("Longitudine:", (gps[4][0] + gps[4][1]/60 + gps[4][2]/3600) * (1 if gps.get(3) == 'E' else -1))

#B4
import zipfile
date = open("probe/ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")
if i != -1:
    open("gasit.zip", "wb").write(date[i:])
    print("arhiva extrasa de la octetul", i)
    zipfile.ZipFile("gasit.zip").extractall("extras")
    print("Fișiere extrase:", zipfile.ZipFile("gasit.zip").namelist())

#B5
from PIL import Image
img = Image.open("probe/foto.jpg").convert("RGB")
px = list(img.getdata())
mesaj = b"FLAG{ascuns_in_pixeli}\x00"
biti = "".join(f"{x:08b}" for x in mesaj)
canale = [c for p in px for c in p]
for i, b in enumerate(biti):
    canale[i] = (canale[i] & ~1) | int(b)
px2 = list(zip(*[iter(canale)] * 3))
img.putdata(px2)
img.save("stego.png")

#B6
px = list(Image.open("stego.png").convert("RGB").getdata())
biti = "".join(f"{r&1}{g&1}{b&1}" for r, g, b in px)
octeti = bytearray()
for i in range(0, len(biti), 8):
    b = int(biti[i:i+8], 2)
    if b == 0:
        break
    octeti.append(b)
mesaj = octeti.decode(errors="ignore")
print("Mesaj extras:", mesaj)

