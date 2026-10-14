"""Empaqueta los MP3 (uno por elemento, nombrados <clave>.mp3) en un archivo por unidad: audio/u01.js … u50.js.

    python tools/empaquetar_audio.py carpeta_con_mp3

Cada archivo define window.LINGO_PACK["<unidad>"] = { "<módulo>.<tipo><n>": "<mp3 en base64>", … }.
La app los carga con <script>, así que funcionan también al abrir index.html desde el disco.
"""
import base64, json, os, sys
src = sys.argv[1] if len(sys.argv) > 1 else "mp3"
dst = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "audio")
os.makedirs(dst, exist_ok=True)
packs = {}
for f in sorted(os.listdir(src)):
    if not f.endswith(".mp3"):
        continue
    u, rest = f[:-4].split(".", 1)
    packs.setdefault(u, {})[rest] = base64.b64encode(open(os.path.join(src, f), "rb").read()).decode()
total = 0
for u, d in sorted(packs.items(), key=lambda x: int(x[0])):
    out = os.path.join(dst, "u%02d.js" % int(u))
    open(out, "w").write('(window.LINGO_PACK=window.LINGO_PACK||{})["%s"]=%s;\n' % (u, json.dumps(d, separators=(",", ":"))))
    total += os.path.getsize(out)
print("Total:", total // 1024 // 1024, "MB en", len(packs), "archivos")
