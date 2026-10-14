"""Data-driven illustrations: one spec per unit -> SVG. Shared by every book.

spec = dict(title=..., sub=..., talk=(A, B) | None, cards=[...] | None, boxes=[...] | None, line=[...] | None, note=...)
  talk : two speakers, each dict(who='tom', say='text')        (people come from CAST)
  cards: list of (icon, label, sub)  icon = name of an i_* function, or '=TEXT' for a big text glyph
  boxes: list of (title, [lines], colour)   colour in 'p' primary, 'a' accent, 'o' ochre, 'b' blue, 'v' violet
  line : timeline marks (frac, label, sublabel, colour)
"""
import textwrap
import lib
from lib import *

VIOLET = '#5B4A6B'
COL = {'p': GREEN, 'a': RED, 'o': '#B9821F', 'b': BLUE, 'v': VIOLET, 'g': '#2E7D5B'}
CAST = {}


def cast(**people):
    """name=dict(shirt=, skin=, hair=, long=, old=, beard=)"""
    CAST.update(people)


def fit(text, width, size, k=0.54, lo=13):
    """Largest font size <= size at which text fits in width."""
    need = max(len(text), 1) * k
    return max(lo, min(size, width / need))


def wrap(text, width, size, k=0.52):
    n = max(8, int(width / (size * k)))
    out = []
    for part in str(text).split('\n'):
        out += textwrap.wrap(part, n) or ['']
    return out


def glyph(cx, cy, text, s, color):
    size = fit(text, s * 3.2, s * 1.25, 0.6)
    return T(cx, cy + size * .35, text, size, 700, color, 'middle')


def icon(name, cx, cy, s, color=None):
    if name is None:
        return ''
    if name.startswith('='):
        return glyph(cx, cy, name[1:], s, color or GREEN)
    f = getattr(lib, 'i_' + name)
    return f(cx, cy, s)


def talk(a, b, y0=104, ph=230, size=22):
    """Two people facing each other with speech bubbles. Returns (svg, bottom_y)."""
    out = ''
    la = wrap(a['say'], 400, size); lb = wrap(b['say'], 400, size)
    wa = min(440, max(len(l) for l in la) * size * .53 + 44); wb = min(440, max(len(l) for l in lb) * size * .53 + 44)
    ha = len(la) * size * 1.32 + 26; hb = len(lb) * size * 1.32 + 26
    by = y0 + max(ha + hb + 110, ph) + 46
    pa = CAST[a['who']]; pb = CAST[b['who']]
    kw = lambda d: {k: v for k, v in d.items() if k != 'label'}
    out += person(150, by, ph, **kw(pa)) + person(W - 150, by, ph, **kw(pb))
    out += T(150, by + 30, a['who'].capitalize() if not pa.get('label') else pa['label'], 19, 700, GREEN, 'middle')
    out += T(W - 150, by + 30, b['who'].capitalize() if not pb.get('label') else pb['label'], 19, 700, GREEN, 'middle')
    out += bubble(250, y0 + 14, wa, la, size, 'left')
    off = ha + 34 if 250 + wa > W - 250 - wb - 10 else min(ha * .55, 80) + 34
    out += bubble(W - 250 - wb, y0 + 14 + off, wb, lb, size, 'right')
    return out, by + 44


def cards(items, y, h=150):
    n = len(items)
    gap = 18
    w = (W - 80 - gap * (n - 1)) / n
    out = ''
    for i, it in enumerate(items):
        ic, lab, sub = (list(it) + [None, None])[:3]
        x = 40 + i * (w + gap)
        out += R(x, y, w, h, PAPER, stroke=GREEN)
        cy = y + h * .34
        out += icon(ic, x + w / 2, cy, min(34, h * .22), [GREEN, RED, BLUE, COL['o'], VIOLET][i % 5])
        s1 = fit(lab, w - 20, 21)
        out += T(x + w / 2, y + h * .72, lab, s1, 700, INK, 'middle')
        if sub:
            s2 = fit(sub, w - 16, 17)
            out += T(x + w / 2, y + h * .72 + 25, sub, s2, 400, GREY, 'middle')
    return out, y + h + 30


def boxes(items, y, size=20):
    n = len(items)
    gap = 20
    w = (W - 80 - gap * (n - 1)) / n
    laid = []
    for title, lines, col in items:
        ls = []
        for l in lines:
            ls += wrap(l, w - 40, size)
        laid.append((title, ls, COL.get(col, GREEN)))
    h = 62 + max(len(ls) for _, ls, _ in laid) * size * 1.42 + 14
    out = ''
    for i, (title, ls, col) in enumerate(laid):
        x = 40 + i * (w + gap)
        out += R(x, y, w, h, PAPER, stroke=col, sw=3)
        out += f'<path d="M{x},{y + 14} a14,14 0 0 1 14,-14 h{w - 28} a14,14 0 0 1 14,14 v32 h-{w} z" fill="{col}"/>'
        out += T(x + w / 2, y + 32, title, fit(title, w - 24, 22), 700, PAPER, 'middle')
        for j, l in enumerate(ls):
            out += T(x + 20, y + 80 + j * size * 1.42, l, size, 400, INK)
    return out, y + h + 30


def tline(marks, y):
    return timeline(90, W - 70, y + 20, [(f, a, b, COL.get(c, c)) for f, a, b, c in marks]), y + 120


def note(text, y):
    ls = wrap(text, W - 160, 21)
    h = len(ls) * 28 + 24
    out = R(60, y, W - 120, h, LEAF, rx=h / 2 if len(ls) == 1 else 22)
    for i, l in enumerate(ls):
        out += T(W / 2, y + 33 + i * 28, l, 21, 600, INK, 'middle')
    return out, y + h + 26


def scene(unit_label, spec):
    y = 104
    body = ''
    for key in spec.get('order', ('talk', 'line', 'boxes', 'cards', 'note')):
        v = spec.get(key)
        if not v:
            continue
        if key == 'talk':
            s, y = talk(*v, y0=y)
        elif key == 'line':
            s, y = tline(v, y)
        elif key == 'boxes':
            s, y = boxes(v, y)
        elif key == 'cards':
            s, y = cards(v, y)
        else:
            s, y = note(v, y)
        body += s
    return page(unit_label, spec['title'], body, int(y), spec.get('sub'))
