import sys, os, importlib, re
from playwright.sync_api import sync_playwright

mods = sys.argv[1:]
os.makedirs('out', exist_ok=True)
ims = {}
for m in mods:
    ims.update(importlib.import_module(m).IM)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg = b.new_page(device_scale_factor=1)
    for name, svg in ims.items():
        h = int(re.search(r'height="(\d+)"', svg).group(1))
        pg.set_viewport_size({'width': 1200, 'height': h})
        pg.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
        pg.screenshot(path=f'out/{name}.png', omit_background=True)
        print(name, h)
    b.close()
