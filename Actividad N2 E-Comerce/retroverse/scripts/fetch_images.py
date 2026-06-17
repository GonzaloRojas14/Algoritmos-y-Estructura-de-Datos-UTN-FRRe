#!/usr/bin/env python3
"""
RetroVerse — descarga fotos reales de cada producto desde Wikipedia/Wikimedia
Commons (imágenes libres / de uso educativo) y rellena imagen_url en db/seed.sql.

Uso: python3 scripts/fetch_images.py
"""
import json, os, re, sys, subprocess, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "public", "img")
SEED = os.path.join(ROOT, "db", "seed.sql")
UA = "RetroVerseDemo/1.0 (UTN-FRRe educational project; contact: gonzalo14rojas@gmail.com)"

# sku -> lista de títulos candidatos en Wikipedia (en inglés: mejores infobox)
CANDIDATES = {
    "RV-CBM64":    ["Commodore 64"],
    "RV-NESC":     ["Nintendo Entertainment System"],
    "RV-SNES":     ["Super Nintendo Entertainment System"],
    "RV-MEGADRV":  ["Sega Genesis", "Sega Mega Drive"],
    "RV-WALKMAN":  ["Walkman", "Sony Walkman"],
    "RV-DISCMAN":  ["Discman", "Portable CD player", "CD player"],
    "RV-VINILO1":  ["Phonograph record"],
    "RV-VINILO2":  ["LP record", "Phonograph record"],
    "RV-ATARI":    ["Atari 2600"],
    "RV-CARTZELDA":["The Legend of Zelda (video game)", "The Legend of Zelda"],
    "RV-CARTSONIC":["Sonic the Hedgehog (1991 video game)", "Sonic the Hedgehog"],
    "RV-JOYARCADE":["Joystick", "Arcade controller"],
    "RV-GAMEBOY":  ["Game Boy"],
    "RV-AMIGA":    ["Amiga 500", "Amiga"],
}

def http_get(url):
    # curl usa el almacen de certificados del sistema (urllib de Python.framework no lo tiene)
    p = subprocess.run(
        ["curl", "-sSL", "-f", "--max-time", "40", "-A", UA, url],
        capture_output=True,
    )
    if p.returncode != 0:
        raise RuntimeError(p.stderr.decode("utf-8", "ignore").strip() or f"curl exit {p.returncode}")
    return p.stdout

def summary_image(title):
    """Devuelve (url_descarga_800px, ext) para el título, usando el endpoint
    soportado Special:FilePath?width= (el bump directo del thumb da 400)."""
    t = urllib.parse.quote(title.replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{t}"
    try:
        d = json.loads(http_get(url).decode("utf-8"))
    except Exception as e:
        print(f"    [warn] summary fallo para '{title}': {e}")
        return None
    thumb = (d.get("thumbnail") or {}).get("source")
    if not thumb:
        return None
    # nombre de archivo + wiki desde la URL del thumb de Wikimedia
    if "/thumb/" in thumb:
        fname = thumb.split("/thumb/")[1].split("/")[2]   # a/ab/FILENAME/NNNpx-...
    else:
        fname = thumb.split("/")[-1]
    wiki = "commons.wikimedia.org" if "/wikipedia/commons/" in thumb else "en.wikipedia.org"
    big = f"https://{wiki}/wiki/Special:FilePath/{fname}?width=800"
    ext = os.path.splitext(fname)[1].lower() or ".jpg"
    if ext == ".svg":     # FilePath con width rasteriza SVG a PNG
        ext = ".png"
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
        ext = ".jpg"
    return big, ext

def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    mapping = {}  # sku -> /img/<sku><ext>
    for sku, titles in CANDIDATES.items():
        print(f"[{sku}]")
        got = None
        for title in titles:
            res = summary_image(title)
            if res:
                big, ext = res
                try:
                    data = http_get(big)
                    if len(data) < 1500:   # imagen rota / muy chica
                        raise ValueError("respuesta demasiado chica")
                    fname = f"{sku}{ext}"
                    with open(os.path.join(IMG_DIR, fname), "wb") as fh:
                        fh.write(data)
                    mapping[sku] = f"/img/{fname}"
                    got = title
                    print(f"    OK <- '{title}'  ({len(data)//1024} KB)  -> public/img/{fname}")
                    break
                except Exception as e:
                    print(f"    [warn] descarga fallo ('{title}'): {e}")
        if not got:
            print(f"    [ERROR] sin imagen para {sku}")

    # Rellenar imagen_url en seed.sql (cada línea de producto tiene exactamente un NULL = imagen_url)
    with open(SEED, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
    changed = 0
    for i, line in enumerate(lines):
        for sku, path in mapping.items():
            if f"'{sku}'" in line and " NULL," in line:
                lines[i] = line.replace(" NULL,", f" '{path}',", 1)
                changed += 1
                break
    with open(SEED, "w", encoding="utf-8") as fh:
        fh.writelines(lines)

    print(f"\nResumen: {len(mapping)}/{len(CANDIDATES)} imagenes descargadas; {changed} lineas de seed actualizadas.")
    if len(mapping) != len(CANDIDATES):
        sys.exit(1)

if __name__ == "__main__":
    main()
