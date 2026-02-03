import os
import json
import unicodedata
from urllib.parse import quote

BASE = "imatges"
EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp")

def norm(s: str) -> str:
    return unicodedata.normalize("NFC", s)

data = {}

for baralla in sorted(os.listdir(BASE)):
    baralla_n = norm(baralla)
    ruta_baralla = os.path.join(BASE, baralla)

    if not os.path.isdir(ruta_baralla):
        continue

    files = []
    for f in sorted(os.listdir(ruta_baralla)):
        f_n = norm(f)

        if f_n.lower().endswith(EXTS):
            rel = f"{BASE}/{baralla_n}/{f_n}"
            rel_url = quote(rel, safe="/")
            files.append(rel_url)

    if files:
        data[baralla_n] = files

with open("manifest.json", "w", encoding="utf-8") as fp:
    json.dump(data, fp, ensure_ascii=False, indent=2)

print("Manifest creat correctament 👍")