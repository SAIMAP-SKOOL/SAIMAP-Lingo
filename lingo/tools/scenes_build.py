"""Genera src/<curso>/scenes.js a partir de scenes_courses.PLANS (python3 tools/scenes_build.py en pt fr de)."""
import sys, os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import scenes_core
from scenes_courses import PLANS, LOCS

TEXT = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)


def translate_raw(svg, TR):
    return TEXT.sub(lambda m: f'<text{m.group(1)}>{TR.get(m.group(2), m.group(2))}</text>', svg)


def mirror(svg):
    def fix(m):
        attrs, body = m.group(1), m.group(2)
        x = re.search(r'\sx="([-\d.]+)"', attrs)
        ax = float(x.group(1)) if x else 0.0
        t = re.search(r'transform="translate\(([-\d.]+)', attrs)
        if t:
            ax += float(t.group(1))
        attrs = attrs.replace('text-anchor="start"', 'text-anchor="@@"').replace('text-anchor="end"', 'text-anchor="start"').replace('text-anchor="@@"', 'text-anchor="end"')
        return f'<g transform="matrix(-1 0 0 1 {2 * ax:.1f} 0)"><text{attrs}>{body}</text></g>'
    i = svg.index('>') + 1
    inner = TEXT.sub(fix, svg[i:-6])
    return svg[:i] + '<g transform="matrix(-1 0 0 1 400 0)">' + inner + '</g></svg>'


def build(course, report=True):
    ns = scenes_core.load(LOC=dict(LOCS[course]))
    out, missing = {}, {}
    for u in range(1, 51):
        spec = PLANS[course][u]
        tpl, TR = spec[0], spec[1]
        extra = spec[2] if len(spec) > 2 else {}
        ns['TR'].clear(); ns['TR'].update(TR)
        ns['POET'] = extra.get('poet')
        seen = set(); ns['SEEN'] = seen
        if isinstance(tpl, tuple):                  # mapa: se dibuja ya en el lado correcto
            d = ns['t_map'](tpl[1], 1 if u % 2 else -1)
            side_ok = True
        else:
            f = ns['s45b'] if tpl == 45 else ns[tpl if isinstance(tpl, str) else 's%d' % tpl]
            tside = 1 if isinstance(tpl, str) else tpl % 2
            side_ok = (tside == u % 2)
            ns['MIRROR'] = not side_ok
            d = f()
            ns['MIRROR'] = False
        svg = translate_raw(d['svg'], TR)
        if not side_ok:
            svg = mirror(svg)
        out[u] = dict(d, svg=svg)
        miss = sorted(t for t in seen if len(t) > 1 and t not in TR and not re.fullmatch(r'[\d:.,%€ -]+|BUS|HOTEL|SPORT|CINEMA', t))
        if miss and not isinstance(tpl, str):
            missing[u] = miss
    path = os.path.join(HERE, '..', 'src', course, 'scenes.js')
    open(path, 'w', encoding='utf8').write(
        f'// SAIMAP Lingo · {course} · fondos ilustrados y caminos por unidad (generado por tools/scenes_build.py)\n'
        'window.SCENES = ' + json.dumps(out, ensure_ascii=False) + ';\n')
    if report:
        print(course, 'ok', sum(len(v['svg']) for v in out.values()) // 1024, 'KB', 'sin traducir:', missing)


if __name__ == '__main__':
    for c in sys.argv[1:] or ['en', 'pt', 'fr', 'de']:
        build(c)
