"""python render.py <book_dir>  -> <book_dir>/img/*.png  (reads <book_dir>/art.py: IM = {name: svg})"""
import sys, os, re, importlib.util
from playwright.sync_api import sync_playwright
d = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location('art', os.path.join(d, 'art.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
os.makedirs(os.path.join(d, 'img'), exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg = b.new_page(device_scale_factor=1)
    for name, svg in m.IM.items():
        h = int(re.search(r'height="(\d+)"', svg).group(1))
        pg.set_viewport_size({'width': 1200, 'height': h})
        pg.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
        pg.screenshot(path=os.path.join(d, 'img', name + '.png'), omit_background=True)
    b.close()
print(len(m.IM), 'images')
