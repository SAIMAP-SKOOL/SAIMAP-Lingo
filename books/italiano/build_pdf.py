import json, base64, re, glob, os, html as H
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

BASE = os.path.dirname(os.path.abspath(__file__))
RES = '/root/.claude/projects/-home-claude/cfd6ae6c-c1ad-59b2-85f6-b4a9eb174ac8'

BLOB = {
 'e31141ab-1ba6': 'u01', '4ae32db7-9c16': 'u02', 'dd6f9c0a-2145': 'u03', '8935357f-c2ea': 'u04', '9004b3a2-4066': 'u05',
 '846846b1-d705': 'u06', '0b3e37c9-f0c1': 'u07', 'b202f0e5-c6b0': 'u08', 'c228515d-58bc': 'u09', '0bb09767-3183': 'u10',
 'eec41bfa-7f91': 'u11', '0732ebe1-8b50': 'u12', '0e8273c8-0309': 'u13', '00b245b8-3882': 'u14', '112c6755-089e': 'u15',
 '0265d42e-c2e9': 'u16', '9d0db289-5059': 'u17', '0b9f6375-00d6': 'u18', '6581c1e6-8658': 'u19', '755c29ac-959d': 'u20',
 '2068a626-4f96': 'u21', '2e7775c9-165a': 'u22', '5a088740-2d56': 'u23', '85430923-70d1': 'u24', '521859d7-ca11': 'u25',
 '26df8f16-30d2': 'u26', '76098009-06a5': 'u27', '676a132c-2601': 'u28', 'dd6cf31f-1765': 'u29', '70ca28a1-4a5d': 'u30',
 'd6a6ca9f-3b37': 'u31', 'b1e0938f-4285': 'u32', 'a1327387-23ed': 'u33', '2439bd03-5980': 'u34', 'a0960a1f-eefc': 'u35',
 '87290d4f-e1a0': 'u36', 'a4cf8fc4-961d': 'u37', 'd0f8198e-cabb': 'u38', '4db11a55-8caf': 'u39', 'ffc5e5bf-389c': 'u40',
 '135cb80d-4724': 'u41', '571e9c74-98c4': 'u42', '4e400937-82a9': 'u43', 'f456b9ec-ffa0': 'u44', 'afa868e4-80b4': 'u45',
 '83a66bae-ddb6': 'u46', '8787565d-ea9d': 'u47', '07beb95a-abcc': 'u48', '756ba88e-fea1': 'u49', '4fcf94f2-b756': 'u50',
 '39be4ac4-9853': 'intro_livelli', 'f74303b7-4ef3': 'intro_suoni'}

tabs = {}
for p in glob.glob(RES + '/tool-results/mcp-Claude_Docs-export-*.txt'):
    try:
        d = json.loads(json.load(open(p))[1]['text'])['data']
    except Exception:
        continue
    if d['format'] == 'html':
        tabs[d['name']] = base64.b64decode(d['bytes_b64']).decode()
raw = open(RES + '.jsonl').read()
for name in ('Introduzione.html', 'Appendici.html'):
    m = None
    for m in re.finditer(re.escape(name) + r'.{0,300}?bytes_b64[\\"]*:[\\"]*([A-Za-z0-9+/=]{2000,})', raw):
        pass  # keep the last (most recent) export
    assert m, name
    tabs[name] = base64.b64decode(m.group(1)).decode()
print({k: len(v) for k, v in tabs.items()})

order = ['Introduzione.html', 'A1 · Primi passi.html', 'A2 · Sopravvivenza.html', 'B1 · Soglia.html', 'B2 · Progresso.html',
         'C1 · Efficacia.html', 'C2 · Padronanza.html', 'Appendici.html']
assert all(o in tabs for o in order), tabs.keys()

missing = set()
def fix_imgs(h):
    def rep(m):
        b = m.group(1)
        if b not in BLOB:
            missing.add(b); return m.group(0)
        return f'<p class="fig"><img src="out/{BLOB[b]}.png" alt="{m.group(2)}"></p>'
    return re.sub(r'<p><img src="blob/([0-9a-f-]+)" alt="([^"]*)"></p>', rep, h)

body = ''
toc = []  # (level, text, anchor)
n = 0
for o in order:
    h = tabs[o]
    if o == 'Introduzione.html':
        h = re.sub(r'<h1[^>]*>.*?</h1>\s*<p><time.*?</p>', '<h1 id="intro">Introduzione</h1>', h, flags=re.S)
        h = h.replace('Ogni livello è in una scheda separata, a sinistra. Le tabelle dei verbi e le liste di consultazione sono nella scheda <strong>Appendici</strong>.',
                      'Le tabelle dei verbi e le liste di consultazione sono nelle <strong>Appendici</strong>, alla fine del libro.')
    h = h.replace('nella scheda <strong>Appendici</strong>', 'nelle <strong>Appendici</strong>')
    h = fix_imgs(h)
    h = re.sub(r'<thead><tr>(?:<th></th>)+</tr></thead>', '', h)
    def hrep(m):
        global n
        lvl, txt = m.group(1), m.group(3)
        n += 1
        a = f'sec{n}'
        plain = H.unescape(re.sub('<[^>]+>', '', txt))
        if lvl == '1' or (lvl == '2' and o not in ('Introduzione.html',)) or (lvl == '2' and o == 'Introduzione.html'):
            toc.append((int(lvl), plain, a))
        return f'<h{lvl} id="{a}">{txt}</h{lvl}>'
    h = re.sub(r'<h([12])( [^>]*)?>(.*?)</h\1>', hrep, h, flags=re.S)
    cls = 'tab ' + ('units' if o[:2] in ('A1', 'A2', 'B1', 'B2', 'C1', 'C2') else 'plain')
    body += f'<section class="{cls}">{h}</section>'
assert not missing, missing

CSS = '''
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
body { font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif; font-size: 10.4pt; line-height: 1.45; color: #26323A; margin: 0; }
h1 { font-size: 25pt; color: #2E7D5B; margin: 0 0 6mm; padding-bottom: 3mm; border-bottom: 2.5pt solid #2E7D5B; break-before: page; }
h2 { font-size: 17pt; color: #2E7D5B; margin: 9mm 0 3mm; break-after: avoid; }
section.units h2 { break-before: page; margin-top: 0; padding: 3.5mm 5mm; background: #2E7D5B; color: #fff; border-radius: 3mm; }
section.units h1 + p { font-size: 12pt; color: #5b6770; }
h3 { font-size: 12.5pt; color: #C8443C; margin: 6mm 0 2mm; break-after: avoid; }
p { margin: 0 0 2.4mm; orphans: 2; widows: 2; }
p.fig { margin: 3mm 0 4mm; text-align: center; break-inside: avoid; }
p.fig img { width: 100%; border-radius: 3mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 4mm; font-size: 9.4pt; }
th { background: #E6F1EA; color: #1F5C42; text-align: left; font-weight: 700; }
th, td { border: 0.6pt solid #C9D3CD; padding: 1.3mm 2mm; vertical-align: top; }
tr { break-inside: avoid; }
thead { display: table-header-group; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; }
li { margin-bottom: 1mm; } li p { margin: 0; }
blockquote { margin: 3mm 0 3mm 4mm; padding: 2mm 5mm; border-left: 2.5pt solid #E0A83A; background: #FBF6EC; font-style: italic; white-space: pre-line; }
hr { border: 0; border-top: 0.8pt solid #C9D3CD; margin: 6mm 0 4mm; }
a { color: #3F6FA8; text-decoration: none; word-break: break-word; }
strong { font-weight: 700; }
.cover { height: 255mm; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 0 8mm; break-after: page; }
.cover .flag { display: flex; width: 60mm; height: 5mm; margin-bottom: 14mm; }
.cover .flag i { flex: 1; } .cover .g { background: #2E7D5B; } .cover .w { background: #f1efe8; } .cover .r { background: #C8443C; }
.cover .t { font-size: 46pt; font-weight: 700; color: #2E7D5B; line-height: 1.05; }
.cover .s { font-size: 19pt; margin-top: 6mm; color: #26323A; }
.cover .d { font-size: 12pt; margin-top: 10mm; color: #5b6770; max-width: 130mm; }
.cover .b { margin-top: auto; font-size: 13pt; font-weight: 700; letter-spacing: 2pt; color: #C8443C; }
.cover .lv { display: flex; gap: 2.5mm; margin-top: 16mm; }
.cover .lv span { padding: 2mm 4.5mm; border-radius: 2.5mm; color: #fff; font-weight: 700; font-size: 13pt; }
.toc h1 { break-before: auto; }
.toc .l1 { font-weight: 700; color: #2E7D5B; margin-top: 3.2mm; font-size: 11.5pt; }
.toc .row { display: flex; align-items: baseline; gap: 2mm; font-size: 9.6pt; line-height: 1.32; }
.toc .row a { color: inherit; }
.toc .dots { flex: 1; border-bottom: 0.6pt dotted #9aa5ab; transform: translateY(-1mm); }
.toc .l2 { padding-left: 5mm; }
'''

def build(pages):
    t = '<section class="toc"><h1>Indice</h1>'
    for lvl, txt, a in toc:
        pg = pages.get(a, '')
        t += f'<div class="row l{lvl}"><a href="#{a}">{H.escape(txt)}</a><span class="dots"></span><span>{pg}</span></div>'
    t += '</section>'
    cols = ['#8FBF9F', '#5FA47A', '#2E7D5B', '#3F6FA8', '#5B4A6B', '#C8443C']
    cover = ('<div class="cover"><div class="flag"><i class="g"></i><i class="w"></i><i class="r"></i></div>'
             '<div class="t">Italiano<br>dalla A alla Z</div><div class="s">Corso completo di lingua italiana · A1–C2</div>'
             '<div class="d">50 unità con dialoghi, parole, grammatica, esercizi e soluzioni. Per chi parla spagnolo.</div>'
             '<div class="lv">' + ''.join(f'<span style="background:{c}">{l}</span>' for l, c in zip(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], cols)) + '</div>'
             '<div class="b">SAIMAP</div></div>')
    return f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Italiano dalla A alla Z</title><style>{CSS}</style></head><body>{cover}{t}{body}</body></html>'

FOOT = ('<div style="width:100%;font-size:8pt;color:#8A949B;font-family:Liberation Sans,Arial;padding:0 16mm;display:flex;justify-content:space-between">'
        '<span>Italiano dalla A alla Z · SAIMAP</span><span class="pageNumber"></span></div>')

def render(pages, out):
    open(os.path.join(BASE, 'book.html'), 'w').write(build(pages))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + os.path.join(BASE, 'book.html'))
        pg.wait_for_load_state('networkidle')
        pg.pdf(path=out, format='A4', print_background=True, display_header_footer=True, header_template='<span></span>',
               footer_template=FOOT, margin={'top': '18mm', 'bottom': '20mm', 'left': '16mm', 'right': '16mm'}, prefer_css_page_size=False)
        b.close()

out = os.path.join(BASE, 'pdf', 'Italiano-dalla-A-alla-Z_SAIMAP.pdf')
render({}, out)
# second pass: find page of each toc entry via named destinations
r = PdfReader(out)
pages = {}
try:
    nd = r.named_destinations
    for lvl, txt, a in toc:
        if a in nd:
            pages[a] = r.get_destination_page_number(nd[a]) + 1
        elif '/' + a in nd:
            pages[a] = r.get_destination_page_number(nd['/' + a]) + 1
except Exception as e:
    print('dest err', e)
if len(pages) < len(toc) * 0.9:
    # fallback: text search
    texts = [(pp.extract_text() or '') for pp in r.pages]
    for lvl, txt, a in toc:
        key = re.sub(r'\s+', ' ', txt)[:28]
        for i, t in enumerate(texts[3:], start=4):
            if key in re.sub(r'\s+', ' ', t):
                pages.setdefault(a, i); break
print('toc', len(toc), 'resolved', len(pages), 'pages', len(r.pages))
render(pages, out)
r2 = PdfReader(out)
print('final pages', len(r2.pages), os.path.getsize(out))
