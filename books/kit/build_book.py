"""python build_book.py <book_dir>

Builds <book_dir>/pdf/<pdf> from the Markdown files listed in <book_dir>/book.json.
One builder for every SAIMAP language book: only book.json, the Markdown and art.py change.
"""
import sys, os, re, json, html as H
import markdown
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

D = os.path.abspath(sys.argv[1])
CFG = json.load(open(os.path.join(D, 'book.json'), encoding='utf-8'))
os.environ['BOOK_THEME'] = CFG['theme']
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
P, A, TINT = lib.GREEN, lib.RED, lib.LEAF          # primary, accent, primary tint
STRIPE = lib.STRIPE

BOX = {}
for cls, names in CFG.get('boxes', {}).items():
    for n in names:
        BOX[n] = cls

def emphasis(src, fn):
    """Convert *em*, **strong** and any nesting of them to HTML ourselves: Markdown parsers
    disagree on nested and intra-word cases (*He **works***, w**or**k), which this book uses a lot."""
    TAG = {'*': 'em', '**': 'strong'}
    out = []
    for ln, line in enumerate(src.split('\n'), 1):
        cells = line.split('|') if line.lstrip().startswith('|') else [line]
        res = []
        for cell in cells:
            stack = []; buf = ''
            for tok in re.split(r'(\*+)', cell):
                if not tok.startswith('*'):
                    buf += tok; continue
                k = len(tok)
                while k:
                    top = stack[-1] if stack else None
                    if (top == '**' and k >= 2) or (top == '*' and k == 1) or (top == '*' and k >= 3 and '**' in stack):
                        t = stack.pop(); buf += f'</{TAG[t]}>'; k -= len(t)
                    elif k >= 3 and not stack:
                        stack += ['*', '**']; buf += '<em><strong>'; k -= 3
                    elif k >= 2 and '**' not in stack:
                        stack.append('**'); buf += '<strong>'; k -= 2
                    elif '*' not in stack:
                        stack.append('*'); buf += '<em>'; k -= 1
                    else:
                        print(f'EMPHASIS? {fn}:{ln}: {cell.strip()[:90]}'); k = 0
            if stack:
                print(f'UNCLOSED {fn}:{ln}: {cell.strip()[:90]}')
                buf += ''.join(f'</{TAG[t]}>' for t in reversed(stack))
            res.append(buf)
        out.append('|'.join(res))
    return '\n'.join(out)


toc = []
n = 0
body = ''
for fn in CFG['files']:
    src = open(os.path.join(D, fn), encoding='utf-8').read()
    src = re.sub(r'_{3,}', '<span class="gap"></span>', src)
    src = emphasis(src, fn)
    h = markdown.markdown(src, extensions=['tables', 'nl2br', 'sane_lists'])
    h = re.sub(r'<p><img alt="[^"]*" src="([^"]+)" ?/?></p>', r'<p class="fig"><img src="img/\1" alt=""></p>', h)
    h = re.sub(r'<thead>\s*<tr>\s*(?:<th></th>\s*)+</tr>\s*</thead>', '', h)
    units = fn in CFG['unit_files']

    # wrap each h3 block so that special sections can be styled as boxes
    parts = re.split(r'(?=<h[123][ >])', h)
    out = ''
    for part in parts:
        m = re.match(r'<h3>(.*?)</h3>', part, flags=re.S)
        if m:
            name = H.unescape(re.sub('<[^>]+>', '', m.group(1))).strip()
            cls = BOX.get(name)
            if cls:
                part = f'<div class="blk {cls}">{part}</div>'
        out += part
    h = out

    def hrep(m):
        global n
        lvl, txt = m.group(1), m.group(2)
        n += 1
        a = f'sec{n}'
        toc.append((int(lvl), H.unescape(re.sub('<[^>]+>', '', txt)), a))
        return f'<h{lvl} id="{a}">{txt}</h{lvl}>'
    h = re.sub(r'<h([12])>(.*?)</h\1>', hrep, h, flags=re.S)
    body += f'<section class="tab {"units" if units else "plain"}">{h}</section>'

stray = re.findall(r'[^<>\n]{0,30}\*[^<>\n]{0,30}', re.sub(r'<[^>]+>', '', body))
if stray:
    print('STRAY ASTERISKS:', len(stray)); [print('   ', s) for s in stray[:40]]

CSS = '''
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
* { box-sizing: border-box; }
body { font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif; font-size: 10.4pt; line-height: 1.45; color: #26323A; margin: 0; }
h1 { font-size: 25pt; color: P; margin: 0 0 6mm; padding-bottom: 3mm; border-bottom: 2.5pt solid P; break-before: page; }
h2 { font-size: 17pt; color: P; margin: 9mm 0 3mm; break-after: avoid; }
section.units h2 { break-before: page; margin-top: 0; padding: 3.5mm 5mm; background: P; color: #fff; border-radius: 3mm; }
section.units h1 + p { font-size: 12pt; color: #5b6770; }
h3 { font-size: 12.5pt; color: A; margin: 6mm 0 2mm; break-after: avoid; }
p { margin: 0 0 2.4mm; orphans: 2; widows: 2; }
p.fig { margin: 3mm 0 4mm; text-align: center; break-inside: avoid; }
p.fig img { width: 100%; border-radius: 3mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 4mm; font-size: 9.4pt; }
th { background: TINT; color: P; text-align: left; font-weight: 700; }
th, td { border: 0.6pt solid #C9D3CD; padding: 1.3mm 2mm; vertical-align: top; }
tr { break-inside: avoid; }
thead { display: table-header-group; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; }
li { margin-bottom: 1mm; } li p { margin: 0; }
hr { border: 0; border-top: 0.8pt solid #C9D3CD; margin: 6mm 0 4mm; }
strong { font-weight: 700; }
.gap { display: inline-block; width: 13mm; border-bottom: 0.8pt solid #26323A; transform: translateY(-0.4mm); }
.blk h3 { margin-top: 0; }
.blk.dialogue p, .blk.text p { margin: 0 0 2mm; }
.blk.dialogue, .blk.text { margin: 5mm 0 3mm; padding: 4mm 5mm 2.5mm; background: #FBF6EC; border-left: 2.5pt solid #E0A83A; border-radius: 0 3mm 3mm 0; }
.blk.dialogue strong { color: P; }
.blk.sound { margin: 5mm 0 3mm; padding: 4mm 5mm 2mm; background: TINT; border-radius: 3mm; break-inside: avoid; }
.blk.sound h3 { color: P; }
.blk.sound th { background: #fff; }
.blk.sound td { background: #fff; }
.blk.warn { margin: 5mm 0 3mm; padding: 4mm 5mm 1.5mm; border: 1pt solid A; border-radius: 3mm; break-inside: avoid; }
.blk.answers { margin-top: 5mm; padding: 3mm 5mm 1.5mm; background: #F3F4F5; border-radius: 3mm; font-size: 9.4pt; break-inside: avoid; }
.blk.answers h3 { font-size: 10.5pt; color: #5b6770; margin-bottom: 1.5mm; }
.cover { height: 255mm; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 0 8mm; break-after: page; }
.cover .flag { display: flex; width: 60mm; height: 5mm; margin-bottom: 14mm; }
.cover .flag i { flex: 1; }
.cover .t { font-size: 46pt; font-weight: 700; color: P; line-height: 1.05; }
.cover .s { font-size: 19pt; margin-top: 6mm; color: #26323A; }
.cover .d { font-size: 12pt; margin-top: 10mm; color: #5b6770; max-width: 130mm; }
.cover .b { margin-top: auto; font-size: 13pt; font-weight: 700; letter-spacing: 2pt; color: A; }
.cover .lv { display: flex; gap: 2.5mm; margin-top: 16mm; }
.cover .lv span { padding: 2mm 4.5mm; border-radius: 2.5mm; color: #fff; font-weight: 700; font-size: 13pt; }
.toc h1 { break-before: auto; }
.toc .l1 { font-weight: 700; color: P; margin-top: 3.2mm; font-size: 11.5pt; }
.toc .row { display: flex; align-items: baseline; gap: 2mm; font-size: 9.6pt; line-height: 1.32; }
.toc .row a { color: inherit; text-decoration: none; }
.toc .dots { flex: 1; border-bottom: 0.6pt dotted #9aa5ab; transform: translateY(-1mm); }
.toc .l2 { padding-left: 5mm; }
'''
CSS = re.sub(r'\bTINT\b', TINT, CSS)
CSS = re.sub(r'(?<![\w#-])P(?=[;\s])', P, CSS)
CSS = re.sub(r'(?<![\w#-])A(?=[;\s])', A, CSS)

LV = ['#8FBF9F', '#5FA47A', '#2E7D5B', '#3F6FA8', '#5B4A6B', '#C8443C']


def build(pages):
    t = f'<section class="toc"><h1>{CFG["toc_title"]}</h1>'
    for lvl, txt, a in toc:
        t += f'<div class="row l{lvl}"><a href="#{a}">{H.escape(txt)}</a><span class="dots"></span><span>{pages.get(a, "")}</span></div>'
    t += '</section>'
    stripe = ''.join(f'<i style="background:{c if c.upper() != "#FFFFFF" else "#f1efe8"}"></i>' for c in STRIPE)
    cover = (f'<div class="cover"><div class="flag">{stripe}</div><div class="t">{CFG["cover_title"]}</div>'
             f'<div class="s">{CFG["subtitle"]}</div><div class="d">{CFG["blurb"]}</div><div class="lv">'
             + ''.join(f'<span style="background:{c}">{l}</span>' for l, c in zip(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], LV)) +
             '</div><div class="b">SAIMAP</div></div>')
    return (f'<!doctype html><html lang="{CFG["lang"]}"><head><meta charset="utf-8"><title>{CFG["title"]}</title>'
            f'<style>{CSS}</style></head><body>{cover}{t}{body}</body></html>')


FOOT = ('<div style="width:100%;font-size:8pt;color:#8A949B;font-family:Liberation Sans,Arial;padding:0 16mm;display:flex;justify-content:space-between">'
        f'<span>{CFG["footer"]}</span><span class="pageNumber"></span></div>')
HTML = os.path.join(D, 'book.html')
os.makedirs(os.path.join(D, 'pdf'), exist_ok=True)
OUT = os.path.join(D, 'pdf', CFG['pdf'])


def render(pages):
    open(HTML, 'w', encoding='utf-8').write(build(pages))
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = b.new_page()
        pg.goto('file://' + HTML)
        pg.wait_for_load_state('networkidle')
        pg.pdf(path=OUT, format='A4', print_background=True, display_header_footer=True, header_template='<span></span>',
               footer_template=FOOT, margin={'top': '18mm', 'bottom': '20mm', 'left': '16mm', 'right': '16mm'})
        b.close()


render({})
r = PdfReader(OUT)
pages = {}
nd = r.named_destinations
for lvl, txt, a in toc:
    for k in (a, '/' + a):
        if k in nd:
            pages[a] = r.get_destination_page_number(nd[k]) + 1
print('toc', len(toc), 'resolved', len(pages), 'pages', len(r.pages))
render(pages)
r2 = PdfReader(OUT)
assert len(r2.pages) == len(r.pages), 'page count changed between passes'
print('final pages', len(r2.pages), os.path.getsize(OUT), OUT)
