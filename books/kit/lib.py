"""Small SVG drawing kit for the book illustrations."""
import math, html

import os
# Themes: one per book. GREEN = primary, RED = accent, LEAF = primary tint, HEADTINT = light text on the header band,
# STRIPE = the three small colour blocks under the header (the flag).
THEMES = {
    'it': dict(GREEN='#2E7D5B', RED='#C8443C', LEAF='#DCEEE3', HEADTINT='#CFE8DA', STRIPE=('#2E7D5B', '#FFFFFF', '#C8443C')),
    'en': dict(GREEN='#1F3A6E', RED='#C8102E', LEAF='#E1E8F4', HEADTINT='#C9D6EE', STRIPE=('#1F3A6E', '#FFFFFF', '#C8102E')),
    'fr': dict(GREEN='#24408E', RED='#D8323A', LEAF='#E1E6F4', HEADTINT='#CCD5EE', STRIPE=('#24408E', '#FFFFFF', '#D8323A')),
    'de': dict(GREEN='#2B2B2B', RED='#C8102E', LEAF='#F3ECD6', HEADTINT='#E8D9A8', STRIPE=('#2B2B2B', '#C8102E', '#E0A83A')),
    'el': dict(GREEN='#0D5EAF', RED='#C0522F', LEAF='#DFEAF7', HEADTINT='#C9DBF1', STRIPE=('#0D5EAF', '#FFFFFF', '#0D5EAF')),
    'ca': dict(GREEN='#A3262A', RED='#C98A0B', LEAF='#FBEFD2', HEADTINT='#F6D9A0', STRIPE=('#F2C230', '#A3262A', '#F2C230')),
    'pt': dict(GREEN='#1E6B45', RED='#C8102E', LEAF='#DCEEE3', HEADTINT='#CFE8DA', STRIPE=('#1E6B45', '#C8102E', '#E0A83A')),
}
_T = THEMES[os.environ.get('BOOK_THEME', 'it')]
GREEN = _T['GREEN']; RED = _T['RED']; LEAF = _T['LEAF']; HEADTINT = _T['HEADTINT']; STRIPE = _T['STRIPE']
CREAM = '#FBF6EC'; INK = '#26323A'
OCHRE = '#E0A83A'; BLUE = '#3F6FA8'; SKY = '#DCEBF5'; GREY = '#8A949B'
PAPER = '#FFFFFF'; SAND = '#F1E6CF'; ROSE = '#F7DEDA'
SKIN = ['#F2C9A5', '#D9A47A', '#F6D7BC', '#B9825A']
FONT = "Liberation Sans, Arial, sans-serif"
W = 1200


def esc(s):
    return html.escape(str(s), quote=False)


def T(x, y, s, size=26, weight=400, fill=INK, anchor='start', italic=False):
    st = ' font-style="italic"' if italic else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{st}>{esc(s)}</text>')


def TL(x, y, lines, size=24, lh=None, **kw):
    lh = lh or size * 1.3
    return ''.join(T(x, y + i * lh, l, size, **kw) for i, l in enumerate(lines))


def R(x, y, w, h, fill=PAPER, rx=14, stroke=None, sw=2, dash=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}{d}/>'


def C(cx, cy, r, fill=PAPER, stroke=None, sw=2):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}/>'


def L(x1, y1, x2, y2, stroke=INK, sw=3, dash=None, cap='round'):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'


def P(d, fill='none', stroke=INK, sw=3):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'


def arrow(x1, y1, x2, y2, color=INK, sw=4, head=14):
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - head * math.cos(a), y2 - head * math.sin(a)
    p1 = (hx + head * .55 * math.cos(a + math.pi / 2), hy + head * .55 * math.sin(a + math.pi / 2))
    p2 = (hx - head * .55 * math.cos(a + math.pi / 2), hy - head * .55 * math.sin(a + math.pi / 2))
    return (L(x1, y1, hx, hy, color, sw) +
            f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')


def chip(x, y, text, fill=LEAF, color=INK, size=22, weight=600, pad=16, h=None):
    w = len(text) * size * 0.56 + pad * 2
    h = h or size + 18
    return R(x, y, w, h, fill, rx=h / 2) + T(x + w / 2, y + h / 2 + size * .35, text, size, weight, color, 'middle'), w


def box(x, y, w, h, title=None, lines=(), fill=PAPER, stroke=GREEN, tsize=24, size=21, tcolor=None, center=False):
    out = R(x, y, w, h, fill, stroke=stroke)
    yy = y + 36
    ax, an = (x + w / 2, 'middle') if center else (x + 20, 'start')
    if title:
        out += T(ax, yy, title, tsize, 700, tcolor or stroke if stroke else INK, an)
        yy += tsize * 1.35
    for l in lines:
        out += T(ax, yy, l, size, 400, INK, an)
        yy += size * 1.38
    return out


def person(cx, by, h=220, shirt=BLUE, skin=0, hair='#4A3426', long=False, smile=True, beard=False, old=False):
    """Simple friendly figure. (cx, by) = feet centre."""
    sk = SKIN[skin % len(SKIN)]
    r = h * 0.15
    hy = by - h + r
    tw = h * 0.36; th = h * 0.36; ty = hy + r + h * 0.03
    out = ''
    lw = h * 0.085
    # legs
    out += L(cx - tw * .22, ty + th - 4, cx - tw * .22, by - lw / 2, INK if not long else '#5B4A6B', lw)
    out += L(cx + tw * .22, ty + th - 4, cx + tw * .22, by - lw / 2, INK if not long else '#5B4A6B', lw)
    # arms
    out += L(cx - tw * .5, ty + 14, cx - tw * .72, ty + th * .8, shirt, lw * .9)
    out += L(cx + tw * .5, ty + 14, cx + tw * .72, ty + th * .8, shirt, lw * .9)
    out += C(cx - tw * .72, ty + th * .84, lw * .5, sk) + C(cx + tw * .72, ty + th * .84, lw * .5, sk)
    # torso
    out += R(cx - tw / 2, ty, tw, th, shirt, rx=tw * .28)
    hc = '#C9CDD1' if old else hair
    if long:
        out += f'<path d="M{cx - r * 1.12},{hy - r * .1} Q{cx - r * 1.3},{hy + r * 1.6} {cx - r * .7},{hy + r * 1.7} L{cx + r * .7},{hy + r * 1.7} Q{cx + r * 1.3},{hy + r * 1.6} {cx + r * 1.12},{hy - r * .1} Z" fill="{hc}"/>'
    out += C(cx, hy, r, sk)
    # hair cap
    out += f'<path d="M{cx - r * 1.04},{hy - r * .05} A{r * 1.04},{r * 1.04} 0 0 1 {cx + r * 1.04},{hy - r * .05} Q{cx + r * .3},{hy - r * .62} {cx - r * 1.04},{hy - r * .05} Z" fill="{hc}"/>'
    out += C(cx - r * .36, hy + r * .1, r * .09, INK) + C(cx + r * .36, hy + r * .1, r * .09, INK)
    if smile:
        out += P(f'M{cx - r * .32},{hy + r * .45} Q{cx},{hy + r * .75} {cx + r * .32},{hy + r * .45}', sw=max(2, r * .09))
    if beard:
        out += f'<path d="M{cx - r * .8},{hy + r * .45} Q{cx},{hy + r * 1.5} {cx + r * .8},{hy + r * .45} Q{cx},{hy + r * .95} {cx - r * .8},{hy + r * .45} Z" fill="{hc}"/>'
    return out


def bubble(x, y, w, lines, size=24, tail='left', fill=PAPER, stroke=INK, bold_first=False):
    lh = size * 1.32
    h = len(lines) * lh + 26
    out = R(x, y, w, h, fill, rx=20, stroke=stroke)
    tx = x + 46 if tail == 'left' else x + w - 46
    out += f'<path d="M{tx - 14},{y + h - 1} L{tx},{y + h + 24} L{tx + 16},{y + h - 1}" fill="{fill}" stroke="{stroke}" stroke-width="2" stroke-linejoin="round"/>'
    out += L(tx - 12, y + h - 1, tx + 14, y + h - 1, fill, 4, cap='butt')
    for i, l in enumerate(lines):
        out += T(x + 20, y + 18 + size * .8 + i * lh, l, size, 700 if (bold_first and i == 0) else 400)
    return out


def clock(cx, cy, r, hh, mm, face=PAPER, ring=GREEN):
    out = C(cx, cy, r, face, ring, max(4, r * .09))
    for i in range(12):
        a = math.radians(i * 30)
        out += L(cx + math.sin(a) * r * .8, cy - math.cos(a) * r * .8, cx + math.sin(a) * r * .9, cy - math.cos(a) * r * .9, GREY, 2)
    ah = math.radians((hh % 12 + mm / 60) * 30); am = math.radians(mm * 6)
    out += L(cx, cy, cx + math.sin(ah) * r * .5, cy - math.cos(ah) * r * .5, INK, max(4, r * .1))
    out += L(cx, cy, cx + math.sin(am) * r * .74, cy - math.cos(am) * r * .74, RED, max(3, r * .06))
    out += C(cx, cy, r * .07, INK)
    return out


def flag(x, y, w, h, colors, horizontal=False):
    out = ''
    n = len(colors)
    for i, c in enumerate(colors):
        if horizontal:
            out += f'<rect x="{x}" y="{y + i * h / n}" width="{w}" height="{h / n}" fill="{c}"/>'
        else:
            out += f'<rect x="{x + i * w / n}" y="{y}" width="{w / n}" height="{h}" fill="{c}"/>'
    return out + R(x, y, w, h, 'none', rx=3, stroke=GREY, sw=1.5)


# ---------- icons (centre cx, cy; size s ~ half-width) ----------
def i_sun(cx, cy, s=40):
    out = ''
    for i in range(8):
        a = math.radians(i * 45)
        out += L(cx + math.cos(a) * s * .75, cy + math.sin(a) * s * .75, cx + math.cos(a) * s, cy + math.sin(a) * s, OCHRE, 5)
    return out + C(cx, cy, s * .55, OCHRE)


def i_cloud(cx, cy, s=40, fill='#C9D3DA'):
    return (C(cx - s * .45, cy + s * .1, s * .38, fill) + C(cx, cy - s * .15, s * .5, fill) +
            C(cx + s * .5, cy + s * .1, s * .36, fill) + R(cx - s * .78, cy + s * .08, s * 1.6, s * .42, fill, rx=s * .2))


def i_rain(cx, cy, s=40):
    out = i_cloud(cx, cy - s * .25, s, '#9FAEB8')
    for dx in (-.45, 0, .45):
        out += L(cx + dx * s, cy + s * .45, cx + dx * s - s * .12, cy + s * .85, BLUE, 5)
    return out


def i_snow(cx, cy, s=40):
    out = i_cloud(cx, cy - s * .25, s)
    for dx in (-.45, 0, .45):
        out += C(cx + dx * s, cy + s * .65, s * .09, BLUE)
        out += C(cx + dx * s + s * .2, cy + s * .9, s * .07, BLUE)
    return out


def i_wind(cx, cy, s=40):
    out = ''
    for k, (dy, ln) in enumerate(((-.4, 1.5), (0, 1.9), (.4, 1.3))):
        x0 = cx - s * .9; x1 = x0 + s * ln
        out += P(f'M{x0},{cy + dy * s} H{x1} q{s * .28},0 {s * .28},-{s * .22} q0,-{s * .2} -{s * .22},-{s * .2}', stroke=GREY, sw=5)
    return out


def i_moon(cx, cy, s=40):
    return C(cx, cy, s * .6, '#E9E2B8') + C(cx + s * .28, cy - s * .15, s * .52, '#27364A')


def i_cup(cx, cy, s=40):
    return (R(cx - s * .55, cy - s * .3, s * 1.1, s * .75, PAPER, rx=s * .22, stroke=INK, sw=3) +
            P(f'M{cx + s * .55},{cy - s * .1} q{s * .4},{s * .15} 0,{s * .35}') +
            R(cx - s * .45, cy - s * .2, s * .9, s * .2, '#6B4226', rx=4) +
            L(cx - s * .8, cy + s * .58, cx + s * .8, cy + s * .58, INK, 3) +
            P(f'M{cx - s * .15},{cy - s * .5} q{s * .12},-{s * .2} 0,-{s * .4}', stroke=GREY, sw=3) +
            P(f'M{cx + s * .15},{cy - s * .5} q{s * .12},-{s * .2} 0,-{s * .4}', stroke=GREY, sw=3))


def i_cornetto(cx, cy, s=40):
    return (f'<path d="M{cx - s},{cy + s * .3} Q{cx},{cy - s * 1.1} {cx + s},{cy + s * .3} Q{cx},{cy - s * .25} {cx - s},{cy + s * .3} Z" fill="#D9984A" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            L(cx - s * .35, cy - s * .3, cx - s * .2, cy - s * .02, '#A66A2B', 3) + L(cx, cy - s * .4, cx, cy - s * .1, '#A66A2B', 3) +
            L(cx + s * .35, cy - s * .3, cx + s * .2, cy - s * .02, '#A66A2B', 3))


def i_panino(cx, cy, s=40):
    return (f'<path d="M{cx - s},{cy - s * .1} Q{cx},{cy - s * .95} {cx + s},{cy - s * .1} Z" fill="#E3B26B" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            R(cx - s * 1.02, cy - s * .1, s * 2.04, s * .16, '#6FAE5A', rx=4) + R(cx - s * .95, cy + s * .06, s * 1.9, s * .14, RED, rx=4) +
            R(cx - s * .95, cy + s * .2, s * 1.9, s * .3, '#E3B26B', rx=s * .12, stroke=INK, sw=3))


def i_glass(cx, cy, s=40, liquid='#BFE0F2'):
    return (f'<path d="M{cx - s * .45},{cy - s * .7} L{cx - s * .32},{cy + s * .7} L{cx + s * .32},{cy + s * .7} L{cx + s * .45},{cy - s * .7} Z" fill="{PAPER}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            f'<path d="M{cx - s * .4},{cy - s * .2} L{cx - s * .32},{cy + s * .66} L{cx + s * .32},{cy + s * .66} L{cx + s * .4},{cy - s * .2} Z" fill="{liquid}"/>')


def i_bottle(cx, cy, s=40, liquid='#BFE0F2'):
    return (R(cx - s * .14, cy - s * .95, s * .28, s * .3, BLUE, rx=3) +
            f'<path d="M{cx - s * .14},{cy - s * .65} Q{cx - s * .4},{cy - s * .45} {cx - s * .4},{cy - s * .2} V{cy + s * .9} H{cx + s * .4} V{cy - s * .2} Q{cx + s * .4},{cy - s * .45} {cx + s * .14},{cy - s * .65} Z" fill="{liquid}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            R(cx - s * .4, cy + s * .05, s * .8, s * .35, PAPER, rx=0))


def i_apple(cx, cy, s=40, color=RED):
    return (C(cx - s * .25, cy + s * .1, s * .55, color) + C(cx + s * .25, cy + s * .1, s * .55, color) +
            L(cx, cy - s * .35, cx + s * .08, cy - s * .8, '#5B3A1E', 4) +
            f'<ellipse cx="{cx + s * .32}" cy="{cy - s * .68}" rx="{s * .26}" ry="{s * .13}" fill="{GREEN}" transform="rotate(-25 {cx + s * .32} {cy - s * .68})"/>')


def i_bread(cx, cy, s=40):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{s}" ry="{s * .5}" fill="#D9984A" stroke="{INK}" stroke-width="3"/>' +
            ''.join(L(cx + dx * s, cy - s * .28, cx + dx * s + s * .18, cy + s * .1, '#A66A2B', 4) for dx in (-.5, -.1, .3)))


def i_cheese(cx, cy, s=40):
    return (f'<path d="M{cx - s},{cy + s * .5} L{cx + s},{cy + s * .5} L{cx + s},{cy - s * .1} L{cx - s * .2},{cy - s * .6} Z" fill="{OCHRE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            C(cx + s * .4, cy + s * .15, s * .13, '#C28A22') + C(cx - s * .15, cy + s * .25, s * .1, '#C28A22') + C(cx + s * .1, cy - s * .15, s * .08, '#C28A22'))


def i_milk(cx, cy, s=40):
    return (f'<path d="M{cx - s * .4},{cy - s * .45} L{cx},{cy - s * .95} L{cx + s * .4},{cy - s * .45} V{cy + s * .9} H{cx - s * .4} Z" fill="{PAPER}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            R(cx - s * .4, cy - s * .1, s * .8, s * .5, BLUE, rx=0) + T(cx, cy + s * .28, 'LATTE', s * .26, 700, PAPER, 'middle'))


def i_eggs(cx, cy, s=40):
    out = R(cx - s, cy, s * 2, s * .55, '#C9B79A', rx=8, stroke=INK, sw=3)
    for dx in (-.62, 0, .62):
        out += f'<ellipse cx="{cx + dx * s}" cy="{cy - s * .05}" rx="{s * .26}" ry="{s * .36}" fill="#FFF4E2" stroke="{INK}" stroke-width="3"/>'
    return out + R(cx - s, cy + s * .08, s * 2, s * .47, '#C9B79A', rx=8, stroke=INK, sw=3)


def i_pasta(cx, cy, s=40):
    return (R(cx - s * .55, cy - s * .9, s * 1.1, s * 1.8, BLUE, rx=8, stroke=INK, sw=3) +
            R(cx - s * .38, cy - s * .35, s * .76, s * .8, '#F3DC9A', rx=6) + T(cx, cy - s * .5, 'PASTA', s * .26, 700, PAPER, 'middle'))


def i_tomato(cx, cy, s=40):
    return C(cx, cy + s * .1, s * .7, RED) + f'<path d="M{cx - s * .35},{cy - s * .5} L{cx},{cy - s * .3} L{cx + s * .35},{cy - s * .5} L{cx + s * .1},{cy - s * .2} L{cx},{cy - s * .75} L{cx - s * .1},{cy - s * .2} Z" fill="{GREEN}"/>'


def i_ham(cx, cy, s=40):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{s}" ry="{s * .6}" fill="#E79A9A" stroke="{INK}" stroke-width="3"/>' +
            f'<ellipse cx="{cx - s * .2}" cy="{cy}" rx="{s * .45}" ry="{s * .28}" fill="#F7D6D0"/>')


def i_pizza(cx, cy, s=40):
    return (C(cx, cy, s, '#E3B26B', INK, 3) + C(cx, cy, s * .82, '#E0574A') +
            ''.join(C(cx + dx * s, cy + dy * s, s * .14, '#FFF4E2') for dx, dy in ((-.35, -.3), (.3, -.35), (.4, .25), (-.25, .4), (0, 0))) +
            ''.join(C(cx + dx * s, cy + dy * s, s * .07, GREEN) for dx, dy in ((0, -.5), (-.5, .05), (.1, .5))))


def i_book(cx, cy, s=40, color=RED):
    return (f'<path d="M{cx},{cy - s * .5} Q{cx - s * .5},{cy - s * .8} {cx - s},{cy - s * .5} V{cy + s * .6} Q{cx - s * .5},{cy + s * .3} {cx},{cy + s * .6} Q{cx + s * .5},{cy + s * .3} {cx + s},{cy + s * .6} V{cy - s * .5} Q{cx + s * .5},{cy - s * .8} {cx},{cy - s * .5} Z" fill="{PAPER}" stroke="{color}" stroke-width="4" stroke-linejoin="round"/>' +
            L(cx, cy - s * .5, cx, cy + s * .6, color, 3) +
            ''.join(L(cx + sg * s * .2, cy - s * .3 + k * s * .22, cx + sg * s * .8, cy - s * .32 + k * s * .22, GREY, 2) for sg in (-1, 1) for k in range(3)))


def i_note(cx, cy, s=40):
    return (f'<ellipse cx="{cx - s * .45}" cy="{cy + s * .55}" rx="{s * .28}" ry="{s * .2}" fill="{INK}"/><ellipse cx="{cx + s * .45}" cy="{cy + s * .35}" rx="{s * .28}" ry="{s * .2}" fill="{INK}"/>' +
            L(cx - s * .2, cy + s * .55, cx - s * .2, cy - s * .6, INK, 5) + L(cx + s * .7, cy + s * .35, cx + s * .7, cy - s * .8, INK, 5) +
            L(cx - s * .2, cy - s * .6, cx + s * .7, cy - s * .8, INK, 9, cap='butt'))


def i_ball(cx, cy, s=40):
    return (C(cx, cy, s * .8, PAPER, INK, 3) +
            f'<polygon points="{cx},{cy - s * .3} {cx + s * .28},{cy - s * .08} {cx + s * .18},{cy + s * .25} {cx - s * .18},{cy + s * .25} {cx - s * .28},{cy - s * .08}" fill="{INK}"/>' +
            L(cx, cy - s * .3, cx, cy - s * .78, INK, 3) + L(cx + s * .28, cy - s * .08, cx + s * .74, cy - s * .25, INK, 3) +
            L(cx - s * .28, cy - s * .08, cx - s * .74, cy - s * .25, INK, 3) + L(cx + s * .18, cy + s * .25, cx + s * .46, cy + s * .64, INK, 3) +
            L(cx - s * .18, cy + s * .25, cx - s * .46, cy + s * .64, INK, 3))


def i_bike(cx, cy, s=40):
    return (C(cx - s * .65, cy + s * .3, s * .42, 'none', INK, 4) + C(cx + s * .65, cy + s * .3, s * .42, 'none', INK, 4) +
            P(f'M{cx - s * .65},{cy + s * .3} L{cx - s * .2},{cy - s * .35} L{cx + s * .4},{cy - s * .35} L{cx + s * .65},{cy + s * .3} M{cx - s * .2},{cy - s * .35} L{cx + s * .05},{cy + s * .3} L{cx - s * .65},{cy + s * .3} M{cx + s * .05},{cy + s * .3} L{cx + s * .4},{cy - s * .35} L{cx + s * .32},{cy - s * .6} H{cx + s * .6} M{cx - s * .32},{cy - s * .5} H{cx - s * .02}', stroke=RED, sw=4))


def i_screen(cx, cy, s=40):
    return (R(cx - s, cy - s * .65, s * 2, s * 1.2, INK, rx=8) + R(cx - s * .88, cy - s * .53, s * 1.76, s * .96, SKY, rx=4) +
            f'<polygon points="{cx - s * .18},{cy - s * .35} {cx + s * .3},{cy - s * .05} {cx - s * .18},{cy + s * .25}" fill="{RED}"/>' +
            L(cx, cy + s * .55, cx, cy + s * .8, INK, 5) + L(cx - s * .4, cy + s * .8, cx + s * .4, cy + s * .8, INK, 5))


def i_pot(cx, cy, s=40):
    return (R(cx - s * .75, cy - s * .2, s * 1.5, s * .85, GREY, rx=10, stroke=INK, sw=3) + L(cx - s * .85, cy - s * .2, cx + s * .85, cy - s * .2, INK, 5) +
            L(cx - s * .75, cy, cx - s * 1.05, cy, INK, 5) + L(cx + s * .75, cy, cx + s * 1.05, cy, INK, 5) +
            P(f'M{cx - s * .25},{cy - s * .4} q{s * .14},-{s * .2} 0,-{s * .4}', stroke=GREY, sw=3) + P(f'M{cx + s * .2},{cy - s * .4} q{s * .14},-{s * .2} 0,-{s * .4}', stroke=GREY, sw=3))


def i_train(cx, cy, s=40):
    return (R(cx - s, cy - s * .55, s * 2, s * .95, RED, rx=14, stroke=INK, sw=3) +
            ''.join(R(cx - s * .82 + k * s * .58, cy - s * .38, s * .44, s * .36, SKY, rx=4) for k in range(3)) +
            C(cx - s * .55, cy + s * .5, s * .16, INK) + C(cx + s * .55, cy + s * .5, s * .16, INK) + L(cx - s * 1.1, cy + s * .7, cx + s * 1.1, cy + s * .7, GREY, 4))


def i_bus(cx, cy, s=40):
    return (R(cx - s, cy - s * .6, s * 2, s * 1.05, OCHRE, rx=10, stroke=INK, sw=3) +
            ''.join(R(cx - s * .85 + k * s * .45, cy - s * .45, s * .36, s * .4, SKY, rx=3) for k in range(4)) +
            C(cx - s * .55, cy + s * .5, s * .18, INK) + C(cx + s * .55, cy + s * .5, s * .18, INK))


def i_car(cx, cy, s=40, color=BLUE):
    return (f'<path d="M{cx - s},{cy + s * .35} V{cy} L{cx - s * .55},{cy - s * .05} L{cx - s * .3},{cy - s * .5} H{cx + s * .35} L{cx + s * .6},{cy - s * .05} L{cx + s},{cy + s * .05} V{cy + s * .35} Z" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            f'<path d="M{cx - s * .42},{cy - s * .08} L{cx - s * .22},{cy - s * .4} H{cx + s * .28} L{cx + s * .45},{cy - s * .08} Z" fill="{SKY}"/>' +
            C(cx - s * .55, cy + s * .38, s * .2, INK) + C(cx + s * .55, cy + s * .38, s * .2, INK))


def i_plane(cx, cy, s=40):
    return (f'<path d="M{cx - s},{cy + s * .05} L{cx + s * .6},{cy - s * .12} Q{cx + s},{cy - s * .05} {cx + s * .6},{cy + s * .12} Z" fill="{PAPER}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            f'<path d="M{cx - s * .1},{cy} L{cx - s * .5},{cy - s * .7} H{cx - s * .25} L{cx + s * .3},{cy - s * .05} Z" fill="{BLUE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            f'<path d="M{cx - s * .1},{cy + s * .05} L{cx - s * .5},{cy + s * .7} H{cx - s * .25} L{cx + s * .3},{cy + s * .08} Z" fill="{BLUE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            f'<path d="M{cx - s * .95},{cy + s * .04} L{cx - s * 1.1},{cy - s * .4} H{cx - s * .92} L{cx - s * .7},{cy} Z" fill="{RED}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')


def i_tshirt(cx, cy, s=40, color=RED):
    return f'<path d="M{cx - s * .35},{cy - s * .7} L{cx - s},{cy - s * .35} L{cx - s * .75},{cy} L{cx - s * .5},{cy - s * .15} V{cy + s * .8} H{cx + s * .5} V{cy - s * .15} L{cx + s * .75},{cy} L{cx + s},{cy - s * .35} L{cx + s * .35},{cy - s * .7} Q{cx},{cy - s * .4} {cx - s * .35},{cy - s * .7} Z" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'


def i_pants(cx, cy, s=40, color=BLUE):
    return f'<path d="M{cx - s * .5},{cy - s * .85} H{cx + s * .5} L{cx + s * .6},{cy + s * .85} H{cx + s * .15} L{cx},{cy - s * .3} L{cx - s * .15},{cy + s * .85} H{cx - s * .6} Z" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'


def i_skirt(cx, cy, s=40, color=OCHRE):
    return f'<path d="M{cx - s * .4},{cy - s * .6} H{cx + s * .4} L{cx + s * .85},{cy + s * .6} H{cx - s * .85} Z" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' + R(cx - s * .42, cy - s * .72, s * .84, s * .16, INK, rx=3)


def i_dress(cx, cy, s=40, color=GREEN):
    return f'<path d="M{cx - s * .3},{cy - s * .9} L{cx - s * .15},{cy - s * .55} H{cx + s * .15} L{cx + s * .3},{cy - s * .9} L{cx + s * .45},{cy - s * .6} L{cx + s * .28},{cy - s * .2} L{cx + s * .8},{cy + s * .85} H{cx - s * .8} L{cx - s * .28},{cy - s * .2} L{cx - s * .45},{cy - s * .6} Z" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>'


def i_shoe(cx, cy, s=40, color='#7A4B2A'):
    return (f'<path d="M{cx - s * .9},{cy - s * .4} H{cx - s * .3} L{cx + s * .2},{cy} Q{cx + s * .9},{cy + s * .05} {cx + s * .9},{cy + s * .4} H{cx - s * .9} Z" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            L(cx - s * .9, cy + s * .42, cx + s * .9, cy + s * .42, INK, 6))


def i_hat(cx, cy, s=40, color=SAND):
    return (f'<ellipse cx="{cx}" cy="{cy + s * .3}" rx="{s}" ry="{s * .25}" fill="{color}" stroke="{INK}" stroke-width="3"/>' +
            f'<path d="M{cx - s * .5},{cy + s * .3} Q{cx - s * .5},{cy - s * .6} {cx},{cy - s * .6} Q{cx + s * .5},{cy - s * .6} {cx + s * .5},{cy + s * .3} Z" fill="{color}" stroke="{INK}" stroke-width="3"/>' +
            f'<path d="M{cx - s * .5},{cy + s * .12} Q{cx},{cy + s * .32} {cx + s * .5},{cy + s * .12}" fill="none" stroke="{RED}" stroke-width="7"/>')


def i_jacket(cx, cy, s=40, color='#5B4A6B'):
    return (i_tshirt(cx, cy, s, color) + L(cx, cy - s * .5, cx, cy + s * .8, INK, 3) +
            P(f'M{cx - s * .35},{cy - s * .7} L{cx},{cy - s * .15} L{cx + s * .35},{cy - s * .7}', sw=3) +
            f'<path d="M{cx - s},{cy - s * .35} L{cx - s * 1.05},{cy + s * .55} L{cx - s * .75},{cy + s * .6} L{cx - s * .5},{cy - s * .15}" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            f'<path d="M{cx + s},{cy - s * .35} L{cx + s * 1.05},{cy + s * .55} L{cx + s * .75},{cy + s * .6} L{cx + s * .5},{cy - s * .15}" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')


def i_house(cx, cy, s=40, color=SAND):
    return (R(cx - s * .7, cy - s * .15, s * 1.4, s * 1.0, color, rx=4, stroke=INK, sw=3) +
            f'<polygon points="{cx - s * .95},{cy - s * .12} {cx},{cy - s * .95} {cx + s * .95},{cy - s * .12}" fill="{RED}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            R(cx - s * .15, cy + s * .3, s * .3, s * .55, '#7A4B2A', rx=3))


def i_building(cx, cy, s=40, color=SAND, roof=RED, sign=None):
    out = R(cx - s * .8, cy - s * .7, s * 1.6, s * 1.5, color, rx=6, stroke=INK, sw=3)
    out += R(cx - s * .88, cy - s * .86, s * 1.76, s * .22, roof, rx=5)
    for dx in (-.48, 0, .48):
        out += R(cx + dx * s - s * .14, cy - s * .45, s * .28, s * .3, SKY, rx=3)
    out += R(cx - s * .16, cy + s * .25, s * .32, s * .55, '#7A4B2A', rx=3)
    if sign:
        out += T(cx, cy + s * .1, sign, s * .3, 700, INK, 'middle')
    return out


def i_tree(cx, cy, s=40):
    return R(cx - s * .1, cy, s * .2, s * .8, '#7A4B2A', rx=3) + C(cx, cy - s * .2, s * .55, '#5FA47A')


def i_phone(cx, cy, s=40):
    return R(cx - s * .45, cy - s * .9, s * .9, s * 1.8, INK, rx=10) + R(cx - s * .37, cy - s * .72, s * .74, s * 1.36, SKY, rx=4) + C(cx, cy + s * .77, s * .07, GREY)


def i_mail(cx, cy, s=40):
    return (R(cx - s, cy - s * .6, s * 2, s * 1.2, PAPER, rx=8, stroke=INK, sw=3) +
            P(f'M{cx - s},{cy - s * .55} L{cx},{cy + s * .1} L{cx + s},{cy - s * .55}'))


def i_heart(cx, cy, s=40, color=RED):
    return f'<path d="M{cx},{cy + s * .7} C{cx - s * 1.4},{cy - s * .2} {cx - s * .5},{cy - s * 1.1} {cx},{cy - s * .35} C{cx + s * .5},{cy - s * 1.1} {cx + s * 1.4},{cy - s * .2} {cx},{cy + s * .7} Z" fill="{color}"/>'


def i_bed(cx, cy, s=40):
    return (R(cx - s, cy - s * .1, s * 2, s * .5, BLUE, rx=6, stroke=INK, sw=3) + R(cx - s, cy - s * .55, s * .22, s * 1.2, '#7A4B2A', rx=4) +
            R(cx - s * .7, cy - s * .3, s * .5, s * .26, PAPER, rx=8, stroke=INK, sw=2) + R(cx + s * .82, cy - s * .1, s * .18, s * .75, '#7A4B2A', rx=4))


def i_briefcase(cx, cy, s=40):
    return (R(cx - s * .85, cy - s * .4, s * 1.7, s * 1.1, '#7A4B2A', rx=8, stroke=INK, sw=3) +
            P(f'M{cx - s * .3},{cy - s * .4} V{cy - s * .7} H{cx + s * .3} V{cy - s * .4}') + R(cx - s * .12, cy, s * .24, s * .2, OCHRE, rx=3))


def i_cap(cx, cy, s=40):
    return (f'<polygon points="{cx - s},{cy - s * .1} {cx},{cy - s * .55} {cx + s},{cy - s * .1} {cx},{cy + s * .35}" fill="{INK}"/>' +
            f'<path d="M{cx - s * .5},{cy + s * .12} V{cy + s * .5} Q{cx},{cy + s * .8} {cx + s * .5},{cy + s * .5} V{cy + s * .12} L{cx},{cy + s * .35} Z" fill="{INK}"/>' +
            L(cx + s, cy - s * .1, cx + s, cy + s * .5, OCHRE, 4) + C(cx + s, cy + s * .55, s * .09, OCHRE))


def i_cross(cx, cy, s=40, color=GREEN):
    return R(cx - s * .22, cy - s * .7, s * .44, s * 1.4, color, rx=4) + R(cx - s * .7, cy - s * .22, s * 1.4, s * .44, color, rx=4)


def i_plate(cx, cy, s=40):
    return (C(cx, cy, s * .75, PAPER, INK, 3) + C(cx, cy, s * .5, 'none', GREY, 2) +
            L(cx - s * 1.05, cy - s * .6, cx - s * 1.05, cy + s * .7, INK, 4) + L(cx - s * 1.15, cy - s * .6, cx - s * 1.15, cy - s * .2, INK, 3) + L(cx - s * .95, cy - s * .6, cx - s * .95, cy - s * .2, INK, 3) +
            L(cx + s * 1.05, cy - s * .1, cx + s * 1.05, cy + s * .7, INK, 4) + f'<ellipse cx="{cx + s * 1.05}" cy="{cy - s * .35}" rx="{s * .1}" ry="{s * .28}" fill="{INK}"/>')


def i_gift(cx, cy, s=40):
    return (R(cx - s * .7, cy - s * .2, s * 1.4, s * .9, RED, rx=4, stroke=INK, sw=3) + R(cx - s * .8, cy - s * .45, s * 1.6, s * .3, RED, rx=4, stroke=INK, sw=3) +
            R(cx - s * .1, cy - s * .45, s * .2, s * 1.15, OCHRE, rx=0) + P(f'M{cx},{cy - s * .45} q-{s * .5},-{s * .5} -{s * .1},-{s * .1} M{cx},{cy - s * .45} q{s * .5},-{s * .5} {s * .1},-{s * .1}', stroke=OCHRE, sw=5))


def i_euro(cx, cy, s=40):
    return C(cx, cy, s * .8, OCHRE, '#B5811F', 4) + T(cx, cy + s * .32, '€', s * .95, 700, PAPER, 'middle')


def i_globe(cx, cy, s=40):
    return (C(cx, cy, s * .8, SKY, BLUE, 3) + f'<ellipse cx="{cx}" cy="{cy}" rx="{s * .35}" ry="{s * .8}" fill="none" stroke="{BLUE}" stroke-width="3"/>' +
            L(cx - s * .8, cy, cx + s * .8, cy, BLUE, 3) + P(f'M{cx - s * .68},{cy - s * .4} Q{cx},{cy - s * .2} {cx + s * .68},{cy - s * .4} M{cx - s * .68},{cy + s * .4} Q{cx},{cy + s * .2} {cx + s * .68},{cy + s * .4}', stroke=BLUE, sw=3))


def i_pen(cx, cy, s=40):
    return (f'<g transform="rotate(-40 {cx} {cy})">' + R(cx - s * .13, cy - s * .9, s * .26, s * 1.4, BLUE, rx=3, stroke=INK, sw=3) +
            f'<polygon points="{cx - s * .13},{cy + s * .5} {cx + s * .13},{cy + s * .5} {cx},{cy + s * .9}" fill="{SAND}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/></g>')


def i_mic(cx, cy, s=40):
    return (R(cx - s * .28, cy - s * .9, s * .56, s * 1.0, GREY, rx=s * .28, stroke=INK, sw=3) + P(f'M{cx - s * .5},{cy - s * .2} Q{cx - s * .5},{cy + s * .4} {cx},{cy + s * .4} Q{cx + s * .5},{cy + s * .4} {cx + s * .5},{cy - s * .2}') +
            L(cx, cy + s * .4, cx, cy + s * .8, INK, 4) + L(cx - s * .35, cy + s * .8, cx + s * .35, cy + s * .8, INK, 4))


def i_scale(cx, cy, s=40):
    return (L(cx, cy - s * .8, cx, cy + s * .7, INK, 4) + L(cx - s * .8, cy - s * .55, cx + s * .8, cy - s * .55, INK, 4) + L(cx - s * .4, cy + s * .75, cx + s * .4, cy + s * .75, INK, 5) +
            P(f'M{cx - s * .8},{cy - s * .55} L{cx - s * 1.05},{cy + s * .1} H{cx - s * .55} Z M{cx + s * .8},{cy - s * .55} L{cx + s * .55},{cy + s * .1} H{cx + s * 1.05} Z', fill=OCHRE, sw=3))


def i_flask(cx, cy, s=40):
    return (f'<path d="M{cx - s * .2},{cy - s * .85} V{cy - s * .2} L{cx - s * .7},{cy + s * .75} H{cx + s * .7} L{cx + s * .2},{cy - s * .2} V{cy - s * .85} Z" fill="{PAPER}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            f'<path d="M{cx - s * .42},{cy + s * .25} L{cx - s * .66},{cy + s * .72} H{cx + s * .66} L{cx + s * .42},{cy + s * .25} Z" fill="{GREEN}"/>')


def i_stamp(cx, cy, s=40):
    return (R(cx - s * .3, cy - s * .9, s * .6, s * .8, '#7A4B2A', rx=8, stroke=INK, sw=3) + R(cx - s * .7, cy - s * .1, s * 1.4, s * .4, '#7A4B2A', rx=4, stroke=INK, sw=3) +
            R(cx - s * .8, cy + s * .45, s * 1.6, s * .12, RED, rx=2))


def i_speech(cx, cy, s=40, color=GREEN):
    return (R(cx - s, cy - s * .7, s * 2, s * 1.2, color, rx=s * .3) + f'<polygon points="{cx - s * .5},{cy + s * .45} {cx - s * .7},{cy + s * .95} {cx - s * .1},{cy + s * .45}" fill="{color}"/>' +
            ''.join(C(cx + dx * s, cy - s * .1, s * .1, PAPER) for dx in (-.45, 0, .45)))


def i_calendar(cx, cy, s=40, day='15'):
    return (R(cx - s * .8, cy - s * .7, s * 1.6, s * 1.5, PAPER, rx=8, stroke=INK, sw=3) + R(cx - s * .8, cy - s * .7, s * 1.6, s * .42, RED, rx=8) +
            T(cx, cy + s * .55, day, s * .8, 700, INK, 'middle'))


def i_thermo(cx, cy, s=40):
    return (R(cx - s * .13, cy - s * .9, s * .26, s * 1.3, PAPER, rx=s * .13, stroke=INK, sw=3) + C(cx, cy + s * .6, s * .3, RED, INK, 3) + R(cx - s * .06, cy - s * .3, s * .12, s * .8, RED, rx=2))


def i_pill(cx, cy, s=40):
    return (f'<g transform="rotate(-35 {cx} {cy})">' + R(cx - s * .8, cy - s * .3, s * 1.6, s * .6, PAPER, rx=s * .3, stroke=INK, sw=3) +
            f'<path d="M{cx},{cy - s * .3} H{cx + s * .5} A{s * .3},{s * .3} 0 0 1 {cx + s * .5},{cy + s * .3} H{cx} Z" fill="{RED}"/></g>')


def i_suitcase(cx, cy, s=40):
    return (R(cx - s * .7, cy - s * .5, s * 1.4, s * 1.3, GREEN, rx=10, stroke=INK, sw=3) + P(f'M{cx - s * .25},{cy - s * .5} V{cy - s * .85} H{cx + s * .25} V{cy - s * .5}') +
            L(cx - s * .3, cy - s * .5, cx - s * .3, cy + s * .8, '#1F5C42', 4) + L(cx + s * .3, cy - s * .5, cx + s * .3, cy + s * .8, '#1F5C42', 4))


def i_key(cx, cy, s=40):
    return C(cx - s * .5, cy, s * .35, 'none', OCHRE, 7) + L(cx - s * .15, cy, cx + s * .9, cy, OCHRE, 7) + L(cx + s * .6, cy, cx + s * .6, cy + s * .3, OCHRE, 7) + L(cx + s * .85, cy, cx + s * .85, cy + s * .25, OCHRE, 7)


def i_wolf(cx, cy, s=40):
    return (f'<path d="M{cx - s * .7},{cy - s * .8} L{cx - s * .35},{cy - s * .3} H{cx + s * .35} L{cx + s * .7},{cy - s * .8} L{cx + s * .75},{cy + s * .1} L{cx},{cy + s * .85} L{cx - s * .75},{cy + s * .1} Z" fill="{GREY}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            C(cx - s * .3, cy - s * .02, s * .09, INK) + C(cx + s * .3, cy - s * .02, s * .09, INK) + f'<polygon points="{cx - s * .13},{cy + s * .5} {cx + s * .13},{cy + s * .5} {cx},{cy + s * .68}" fill="{INK}"/>')


def i_cat(cx, cy, s=40, color=OCHRE):
    return (f'<path d="M{cx - s * .6},{cy - s * .75} L{cx - s * .25},{cy - s * .4} H{cx + s * .25} L{cx + s * .6},{cy - s * .75} L{cx + s * .65},{cy + s * .1} Q{cx + s * .6},{cy + s * .7} {cx},{cy + s * .7} Q{cx - s * .6},{cy + s * .7} {cx - s * .65},{cy + s * .1} Z" fill="{color}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>' +
            C(cx - s * .26, cy, s * .08, INK) + C(cx + s * .26, cy, s * .08, INK) + f'<polygon points="{cx - s * .08},{cy + s * .2} {cx + s * .08},{cy + s * .2} {cx},{cy + s * .3}" fill="{RED}"/>' +
            L(cx - s * .35, cy + s * .25, cx - s * .85, cy + s * .15, INK, 2) + L(cx + s * .35, cy + s * .25, cx + s * .85, cy + s * .15, INK, 2))


# ---------- page ----------
def page(unit, title, body, h=640, subtitle=None):
    out = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" font-family="{FONT}">'
    out += R(0, 0, W, h, CREAM, rx=28)
    out += f'<path d="M0,28 A28,28 0 0 1 28,0 H{W - 28} A28,28 0 0 1 {W},28 V78 H0 Z" fill="{GREEN}"/>'
    out += R(W - 128, 78, 32, 6, STRIPE[0], rx=0) + R(W - 96, 78, 32, 6, STRIPE[1], rx=0) + R(W - 64, 78, 32, 6, STRIPE[2], rx=0)
    if unit:
        out += T(36, 51, unit, 24, 700, HEADTINT)
        out += T(36 + len(unit) * 15 + 18, 51, title, 30, 700, PAPER)
    else:
        out += T(36, 51, title, 30, 700, PAPER)
    if subtitle:
        out += T(W - 36, 50, subtitle, 20, 400, HEADTINT, 'end')
    out += body + '</svg>'
    return out


def timeline(x0, x1, y, marks, color=INK):
    """marks: list of (frac, label, sublabel, color)."""
    out = arrow(x0, y, x1, y, color, 4)
    for f, lab, sub, c in marks:
        x = x0 + (x1 - x0 - 30) * f
        out += C(x, y, 11, c or color) + T(x, y + 42, lab, 22, 700, c or color, 'middle')
        if sub:
            out += T(x, y + 68, sub, 19, 400, INK, 'middle')
    return out
