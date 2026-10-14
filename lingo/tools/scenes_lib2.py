"""Piezas adicionales para los fondos (se cargan después de scenes_it.py)."""
# Este archivo se ejecuta dentro del espacio de nombres de scenes_it.py (helpers: g, person, tree, cloud, sun…).

FONT = 'font-family="Nunito,Arial,sans-serif" font-weight="800"'


def txt(x, y, t, size=12, fill='#26323A', anchor='middle', weight=800, extra=''):
    t = tr(t)
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Nunito,Arial,sans-serif" font-weight="{weight}" font-size="{size}" fill="{fill}" {extra}>{t}</text>'


# ------------------------------------------------------------ fondos base
def env_street(sky1='#BFE4F7', sky2='#FBEFD9', ground='#E6E1D6', walls=('#F2B880', '#E8846B', '#F6D27A', '#E59A6F', '#D9B48F'), y0=250, road=False):
    o = sky(sky1, sky2, y0 + 20) + f'<rect y="{y0}" width="400" height="{700 - y0}" fill="{ground}"/>'
    xs = [(0, 70, 120), (70, 60, 95), (262, 68, 108), (330, 70, 128)]
    for i, (x, w, h) in enumerate(xs):
        o += facade(x, y0 - h, w, h, walls[i % len(walls)], rows=max(2, h // 40), cols=2, door=(i % 2 == 0), shut=['#3E8A52', '#3F6FA8', '#8A5A3B'][i % 3])
    if road:
        o += f'<rect y="{y0 + 40}" width="400" height="10" fill="#C9C2B3"/>'
    o += ''.join(f'<path d="M0 {y} H400" stroke="#DCD5C6" stroke-width="1.3"/>' for y in range(y0 + 40, 700, 36))
    return o


def env_room(wall='#F6E7D2', floor='#D9B48F', y0=300, window=True, wx=40):
    o = f'<rect width="400" height="{y0}" fill="{wall}"/><rect y="{y0}" width="400" height="{700 - y0}" fill="{floor}"/>'
    o += f'<rect y="{y0 - 8}" width="400" height="10" fill="#FFFFFF" opacity=".55"/>'
    o += ''.join(f'<path d="M0 {y} H400" stroke="#000" stroke-opacity=".06" stroke-width="2"/>' for y in range(y0 + 40, 700, 44))
    o += ''.join(f'<path d="M{x} {y0} V700" stroke="#000" stroke-opacity=".04" stroke-width="1.5"/>' for x in range(60, 400, 90))
    if window:
        o += window_(wx, 70, 90, 110)
    return o


def window_(x, y, w, h, sky_='#BFE4F7', curtains='#E2574C'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{sky_}" stroke="#fff" stroke-width="6"/>'
            f'<path d="M{x + w / 2} {y} V{y + h} M{x} {y + h / 2} H{x + w}" stroke="#fff" stroke-width="4"/>'
            f'<circle cx="{x + w * .7}" cy="{y + h * .3}" r="9" fill="#FFC94A"/>'
            f'<path d="M{x - 10} {y - 8} Q{x + 6} {y + h / 2} {x - 4} {y + h + 6} L{x - 14} {y + h + 6} L{x - 14} {y - 8} Z" fill="{curtains}"/>'
            f'<path d="M{x + w + 10} {y - 8} Q{x + w - 6} {y + h / 2} {x + w + 4} {y + h + 6} L{x + w + 14} {y + h + 6} L{x + w + 14} {y - 8} Z" fill="{curtains}"/>'
            f'<rect x="{x - 18}" y="{y - 14}" width="{w + 36}" height="6" rx="3" fill="#8A5A3B"/>')


def env_park(sky1='#CDEBFA', sky2='#EAF6EA', g1='#A9D69A', g2='#9BCB8A', y0=230):
    return (sky(sky1, sky2, y0 + 40) + f'<path d="M0 {y0} Q100 {y0 - 30} 200 {y0 - 2} T400 {y0 - 8} V700 H0 Z" fill="{g1}"/>'
            f'<path d="M0 {y0 + 70} Q120 {y0 + 40} 230 {y0 + 66} T400 {y0 + 60} V700 H0 Z" fill="{g2}"/>')


def env_country(y0=240):
    o = env_park(y0=y0)
    o += f'<path d="M0 {y0 - 10} Q80 {y0 - 70} 160 {y0 - 20} Q240 {y0 - 80} 320 {y0 - 24} Q370 {y0 - 50} 400 {y0 - 30} V{y0 + 10} H0 Z" fill="#B8D99C"/>'
    o += ''.join(f'<path d="M{x} {y0 + 10} Q{x + 40} {y0 + 120} {x + 30} 700" stroke="#8DBF6E" stroke-width="5" fill="none" opacity=".5"/>' for x in range(-40, 440, 46))
    return o


def env_night(c1='#1F2C55', c2='#3E4A8A'):
    o = sky(c1, c2) + moon(330, 70, 22)
    o += ''.join(star(x, y, s, b) for x, y, s, b in ((60, 50, 1, 0), (150, 90, .8, .7), (240, 40, .9, 1.3), (380, 140, .7, .4), (30, 180, .8, 2), (200, 160, .6, 1)))
    return o


def env_sea(y0=330):
    o = sky('#9FD3F5', '#E2F2FB', y0 + 10) + f'<rect y="{y0}" width="400" height="160" fill="#4FA9DD"/>'
    o += ''.join(f'<path d="M{x} {y} q8 -5 16 0 q8 5 16 0" stroke="#BFE4F7" stroke-width="2.5" fill="none" stroke-linecap="round"/>' for x, y in ((30, y0 + 30), (180, y0 + 60), (300, y0 + 25), (90, y0 + 100), (330, y0 + 120)))
    o += f'<path d="M0 {y0 + 150} Q200 {y0 + 120} 400 {y0 + 150} V700 H0 Z" fill="#F3DFB2"/>'
    return o


# ------------------------------------------------------------ ciudad
def lamp(x, y, s=1):
    return g('<rect x="-2.5" y="-90" width="5" height="90" fill="#3B4F6B"/><path d="M0 -90 Q0 -100 12 -100" stroke="#3B4F6B" stroke-width="4" fill="none"/>'
             '<path d="M6 -100 L18 -100 L15 -92 L9 -92 Z" fill="#3B4F6B"/><ellipse cx="12" cy="-90" rx="5" ry="3" fill="#FFE08A"/><rect x="-6" y="-4" width="12" height="4" fill="#3B4F6B"/>', x, y, s)


def traffic_light(x, y, s=1):
    blink = '<animate attributeName="opacity" values="1;.25;1" dur="3s" repeatCount="indefinite"/>'
    return g(f'<rect x="-2.5" y="-70" width="5" height="70" fill="#4A5566"/><rect x="-9" y="-100" width="18" height="40" rx="5" fill="#26323A"/>'
             f'<circle cy="-91" r="5" fill="#E2574C">{blink}</circle><circle cy="-79" r="5" fill="#FFC94A" opacity=".35"/><circle cy="-67" r="5" fill="#5BAA6A" opacity=".35"/>', x, y, s)


def zebra(x, y, w=90, n=6):
    return ''.join(f'<rect x="{x}" y="{y + i * 12}" width="{w}" height="7" fill="#fff" opacity=".9"/>' for i in range(n))


def sign(x, y, t, c='#3F6FA8', s=1, arrow=None):
    t = tr(t)
    w = len(t) * 6.8 + 22
    ar = ''
    if arrow == 'r':
        ar = f'<path d="M{w / 2 - 2} -32 l8 9 l-8 9 z" fill="{c}"/>'
    elif arrow == 'l':
        ar = f'<path d="M{-w / 2 + 2} -32 l-8 9 l8 9 z" fill="{c}"/>'
    return g(f'<rect x="-2" y="-28" width="4" height="28" fill="#5B6676"/><rect x="{-w / 2}" y="-41" width="{w}" height="18" rx="4" fill="{c}"/>{ar}'
             + txt(0, -28, t, 11, '#fff'), x, y, s)


def vespa(x, y, s=1, c='#5BB9B0', face=1):
    b = (f'<circle cx="-18" cy="-8" r="8" fill="#26323A"/><circle cx="20" cy="-8" r="8" fill="#26323A"/><circle cx="-18" cy="-8" r="3" fill="#C9CFD6"/><circle cx="20" cy="-8" r="3" fill="#C9CFD6"/>'
         f'<path d="M-28 -14 Q-28 -30 -8 -30 L6 -30 L12 -14 Z" fill="{c}"/><path d="M10 -14 L18 -44 L24 -44 L22 -14 Z" fill="{c}"/>'
         f'<rect x="-16" y="-36" width="22" height="6" rx="3" fill="#5B3A2A"/><path d="M14 -48 h14" stroke="#26323A" stroke-width="3" stroke-linecap="round"/>'
         f'<circle cx="25" cy="-38" r="3.5" fill="#FFE08A"/>')
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{b}</g>'


def car(x, y, s=1, c='#E2574C', face=1):
    b = (f'<path d="M-40 -12 L-40 -24 Q-38 -30 -30 -30 L-20 -30 L-10 -44 L18 -44 L30 -30 L38 -28 Q42 -26 42 -18 L42 -12 Z" fill="{c}"/>'
         f'<path d="M-7 -40 L16 -40 L25 -30 L-14 -30 Z" fill="#BFE4F7"/><path d="M5 -40 V-30" stroke="{c}" stroke-width="3"/>'
         f'<circle cx="-24" cy="-12" r="8" fill="#26323A"/><circle cx="26" cy="-12" r="8" fill="#26323A"/><circle cx="-24" cy="-12" r="3" fill="#C9CFD6"/><circle cx="26" cy="-12" r="3" fill="#C9CFD6"/>'
         f'<rect x="36" y="-26" width="6" height="4" rx="1" fill="#FFE08A"/>')
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{b}</g>'


def dome(x, y, s=1):
    """Silueta de catedral con cúpula (estilo Florencia)."""
    return g('<rect x="-60" y="-50" width="120" height="50" fill="#F1E3CF"/><rect x="-60" y="-50" width="120" height="6" fill="#3E8A52" opacity=".7"/>'
             '<rect x="-36" y="-76" width="72" height="26" fill="#F1E3CF"/><path d="M-30 -76 Q-30 -118 0 -124 Q30 -118 30 -76 Z" fill="#D9734E"/>'
             '<path d="M0 -124 V-76 M-15 -120 Q-18 -96 -18 -76 M15 -120 Q18 -96 18 -76" stroke="#fff" stroke-width="2" opacity=".75"/>'
             '<rect x="-4" y="-136" width="8" height="12" fill="#F1E3CF"/><circle cy="-139" r="3" fill="#C9A24A"/>'
             '<rect x="76" y="-120" width="20" height="120" fill="#F1E3CF"/><rect x="76" y="-120" width="20" height="5" fill="#3E8A52" opacity=".7"/>'
             '<path d="M-10 0 v-22 a10 10 0 0 1 20 0 v22 z" fill="#6B3E26"/><circle cx="-36" cy="-30" r="7" fill="#3B4F6B" opacity=".5"/><circle cx="36" cy="-30" r="7" fill="#3B4F6B" opacity=".5"/>', x, y, s)


def shopfront(x, y, w, t, wall='#F2B880', aw=('#E2574C', '#fff'), s=1):
    o = (f'<rect x="0" y="-90" width="{w}" height="90" fill="{wall}"/><rect x="8" y="-60" width="{w - 16}" height="44" fill="#BFE4F7" opacity=".85"/>'
         f'<rect x="{w / 2 - 9}" y="-36" width="18" height="36" fill="#6B3E26"/>')
    o += awning(4, -76, w - 8, aw[0], aw[1], max(4, int(w // 18)))
    o += f'<rect x="10" y="-100" width="{w - 20}" height="18" rx="4" fill="#26323A"/>' + txt(w / 2, -86, t, 11, '#fff')
    return g(o, x, y, s)


def bus_stop(x, y, s=1):
    return g('<rect x="-2" y="-70" width="4" height="70" fill="#5B6676"/><circle cy="-76" r="11" fill="#FFB72B" stroke="#fff" stroke-width="3"/>' + txt(0, -72, 'BUS', 7, '#26323A'), x, y, s)


# ------------------------------------------------------------ casa
def sofa(x, y, s=1, c='#5BAA6A'):
    return g(f'<rect x="-50" y="-34" width="100" height="22" rx="8" fill="{c}"/><rect x="-56" y="-44" width="14" height="38" rx="6" fill="{c}"/>'
             f'<rect x="42" y="-44" width="14" height="38" rx="6" fill="{c}"/><rect x="-44" y="-56" width="88" height="26" rx="10" fill="{c}"/>'
             '<rect x="-30" y="-50" width="22" height="16" rx="5" fill="#FFC94A"/><rect x="-50" y="-8" width="6" height="8" fill="#5E3E28"/><rect x="44" y="-8" width="6" height="8" fill="#5E3E28"/>', x, y, s)


def floor_lamp(x, y, s=1):
    return g('<rect x="-2" y="-80" width="4" height="78" fill="#5B6676"/><ellipse cx="0" cy="-1" rx="12" ry="3" fill="#5B6676"/>'
             '<path d="M-16 -80 L-10 -104 L10 -104 L16 -80 Z" fill="#FFE08A"/>', x, y, s)


def plant(x, y, s=1):
    return g('<path d="M-12 0 L-10 -20 L10 -20 L12 0 Z" fill="#C0583F"/><path d="M0 -20 Q-20 -40 -16 -58 Q-4 -46 0 -20 Q4 -50 16 -60 Q20 -40 0 -20 Q-8 -36 -26 -38 Q-18 -26 0 -20" fill="#3E8A52"/>', x, y, s)


def bookshelf(x, y, s=1, w=70, h=110):
    o = f'<rect x="0" y="{-h}" width="{w}" height="{h}" fill="#8A5A3B"/>'
    cols = ['#E2574C', '#3F6FA8', '#FFC94A', '#5BAA6A', '#C77DBA', '#F2B880']
    for r in range(3):
        yy = -h + 8 + r * (h - 10) / 3
        o += f'<rect x="4" y="{yy + (h - 10) / 3 - 6}" width="{w - 8}" height="4" fill="#5E3E28"/>'
        xx = 6
        i = r
        while xx < w - 12:
            bw = 6 + (i * 7) % 5
            bh = (h - 10) / 3 - 12 - (i * 5) % 6
            o += f'<rect x="{xx}" y="{yy + (h - 10) / 3 - 6 - bh}" width="{bw}" height="{bh}" fill="{cols[i % 6]}"/>'
            xx += bw + 1.5; i += 1
    return g(o, x, y, s)


def frame(x, y, w=40, h=30, art='#9ED3F0'):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#C9A24A"/><rect x="{x + 4}" y="{y + 4}" width="{w - 8}" height="{h - 8}" fill="{art}"/>'
            f'<path d="M{x + 4} {y + h - 4} L{x + w * .4} {y + h * .45} L{x + w * .6} {y + h * .65} L{x + w * .75} {y + h * .5} L{x + w - 4} {y + h - 4} Z" fill="#5BAA6A"/>')


def rug(x, y, w=120, c='#C77DBA'):
    return f'<ellipse cx="{x}" cy="{y}" rx="{w / 2}" ry="{w / 6}" fill="{c}" opacity=".7"/><ellipse cx="{x}" cy="{y}" rx="{w / 2 - 10}" ry="{w / 6 - 6}" fill="none" stroke="#fff" stroke-width="2" opacity=".6"/>'


def table(x, y, s=1, c='#B97A4E', w=80):
    return g(f'<rect x="{-w / 2}" y="-42" width="{w}" height="8" rx="3" fill="{c}"/><rect x="{-w / 2 + 6}" y="-34" width="6" height="34" fill="{c}"/><rect x="{w / 2 - 12}" y="-34" width="6" height="34" fill="{c}"/>', x, y, s)


def chair(x, y, s=1, c='#8A5A3B', face=1):
    b = f'<rect x="-12" y="-28" width="24" height="5" rx="2" fill="{c}"/><rect x="8" y="-56" width="5" height="56" fill="{c}"/><rect x="-12" y="-23" width="4" height="23" fill="{c}"/><rect x="8" y="-60" width="5" height="34" rx="2" fill="{c}"/>'
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{b}</g>'


def tv(x, y, s=1):
    return g('<rect x="-40" y="-56" width="80" height="50" rx="5" fill="#26323A"/><rect x="-35" y="-51" width="70" height="40" fill="#3F6FA8"/>'
             '<path d="M-35 -20 L-14 -38 L2 -26 L16 -40 L35 -24 V-11 H-35 Z" fill="#5BAA6A"/><rect x="-14" y="-6" width="28" height="6" fill="#5B6676"/>', x, y, s)


def laptop(x, y, s=1):
    return g('<rect x="-26" y="-36" width="52" height="34" rx="3" fill="#3B4F6B"/><rect x="-22" y="-32" width="44" height="26" fill="#BFE4F7"/>'
             '<rect x="-8" y="-28" width="26" height="3" fill="#3F6FA8"/><rect x="-18" y="-22" width="30" height="3" fill="#9AA6B8"/><rect x="-18" y="-16" width="24" height="3" fill="#9AA6B8"/>'
             '<path d="M-32 -2 L32 -2 L28 2 L-28 2 Z" fill="#5B6676"/>', x, y, s)


def phone(x, y, s=1, c='#26323A'):
    return g(f'<rect x="-11" y="-38" width="22" height="38" rx="4" fill="{c}"/><rect x="-8.5" y="-34" width="17" height="28" rx="1.5" fill="#BFE4F7"/>'
             '<rect x="-6" y="-31" width="10" height="4" rx="2" fill="#5BAA6A"/><rect x="-3" y="-25" width="9" height="4" rx="2" fill="#fff"/><rect x="-6" y="-19" width="8" height="4" rx="2" fill="#5BAA6A"/>'
             '<circle cy="-3" r="1.5" fill="#5B6676"/>', x, y, s)


def books(x, y, s=1):
    return g('<rect x="-22" y="-10" width="44" height="10" rx="2" fill="#3F6FA8"/><rect x="-20" y="-20" width="40" height="10" rx="2" fill="#E2574C"/>'
             '<rect x="-24" y="-30" width="46" height="10" rx="2" fill="#5BAA6A"/><rect x="-18" y="-28" width="30" height="2" fill="#fff" opacity=".6"/>', x, y, s)


def open_book(x, y, s=1):
    return g('<path d="M0 -4 Q-18 -14 -34 -8 L-34 -36 Q-18 -42 0 -32 Z" fill="#fff" stroke="#C9CFD6"/><path d="M0 -4 Q18 -14 34 -8 L34 -36 Q18 -42 0 -32 Z" fill="#fff" stroke="#C9CFD6"/>'
             + ''.join(f'<path d="M{a} {b} q8 -3 22 0" stroke="#9AA6B8" stroke-width="1.5" fill="none"/>' for a, b in ((-28, -28), (-28, -22), (-28, -16), (6, -28), (6, -22), (6, -16))), x, y, s)


def pencil(x, y, s=1, rot=-30):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-24" y="-3.5" width="40" height="7" fill="#FFC94A"/><path d="M16 -3.5 L26 0 L16 3.5 Z" fill="#F2C9A5"/><path d="M23 -1 L26 0 L23 1 Z" fill="#26323A"/><rect x="-28" y="-3.5" width="5" height="7" fill="#E2574C"/></g>'


def envelope(x, y, s=1, c='#fff'):
    return g(f'<rect x="-22" y="-30" width="44" height="30" rx="3" fill="{c}" stroke="#C9CFD6"/><path d="M-22 -30 L0 -12 L22 -30" stroke="#C9CFD6" stroke-width="2" fill="none"/><rect x="10" y="-26" width="9" height="10" fill="#E2574C"/>', x, y, s)


def calendar(x, y, s=1, day='12'):
    return g('<rect x="-22" y="-44" width="44" height="44" rx="5" fill="#fff" stroke="#C9CFD6"/><rect x="-22" y="-44" width="44" height="13" rx="5" fill="#E2574C"/>'
             '<circle cx="-11" cy="-46" r="2.5" fill="#5B6676"/><circle cx="11" cy="-46" r="2.5" fill="#5B6676"/>' + txt(0, -10, day, 18, '#26323A', weight=900), x, y, s)


def camera(x, y, s=1):
    return g('<rect x="-20" y="-26" width="40" height="26" rx="5" fill="#3B4F6B"/><rect x="-8" y="-31" width="14" height="6" rx="2" fill="#3B4F6B"/>'
             '<circle cy="-13" r="9" fill="#26323A"/><circle cy="-13" r="5" fill="#7FA6DB"/><circle cx="13" cy="-21" r="2" fill="#FFE08A"/>', x, y, s)


def ticket(x, y, s=1, t='TICKET', c='#FFC94A', rot=-10):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M-30 -14 H30 V-5 a5 5 0 0 0 0 10 V14 H-30 V5 a5 5 0 0 0 0 -10 Z" fill="{c}"/>'
            f'<path d="M14 -14 V14" stroke="#fff" stroke-dasharray="3 3" stroke-width="1.5"/>' + txt(-8, 4, t, 9, '#26323A') + '</g>')


def guitar(x, y, s=1, rot=-25):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><ellipse cx="0" cy="0" rx="16" ry="14" fill="#C8955E"/><ellipse cx="0" cy="-16" rx="12" ry="11" fill="#C8955E"/>'
            '<circle cy="-4" r="5" fill="#5E3E28"/><rect x="-2.5" y="-62" width="5" height="46" fill="#5E3E28"/><rect x="-4" y="-70" width="8" height="10" rx="2" fill="#3A2A1E"/></g>')


def notes(x, y, s=1, c='#5B4A6B'):
    return (f'<g transform="translate({x} {y}) scale({s})"><g><path d="M0 0 v-22 l14 -4 v20" stroke="{c}" stroke-width="2.5" fill="none"/><ellipse cx="-3" cy="0" rx="5" ry="3.5" fill="{c}"/>'
            f'<ellipse cx="11" cy="-6" rx="5" ry="3.5" fill="{c}"/>{anim_move(4, -8, 3)}</g></g>')


def ball(x, y, r=10, c='#E2574C'):
    return f'<g transform="translate({x} {y})"><circle r="{r}" fill="#fff"/><path d="M{-r} 0 Q0 {-r * .7} {r} 0 M0 {-r} Q{r * .5} 0 0 {r}" stroke="{c}" stroke-width="2" fill="none"/></g>'


def kite(x, y, s=1, c='#E2574C'):
    return (f'<g transform="translate({x} {y}) scale({s})"><g><path d="M0 -24 L16 0 L0 22 L-16 0 Z" fill="{c}"/><path d="M0 -24 V22 M-16 0 H16" stroke="#fff" stroke-width="1.5"/>'
            '<path d="M0 22 q8 14 0 28 q-8 14 0 28" stroke="#5B6676" stroke-width="1.5" fill="none"/>' + anim_rot(-8, 8, 0, 22, 3) + '</g></g>')


def umbrella(x, y, s=1, c='#E2574C', broken=False):
    can = f'<path d="M-24 -40 Q0 -64 24 -40 Q18 -44 12 -40 Q6 -44 0 -40 Q-6 -44 -12 -40 Q-18 -44 -24 -40 Z" fill="{c}"/>'
    if broken:
        can = f'<path d="M-24 -36 Q-6 -64 20 -48 L26 -30 Q18 -40 10 -36 Q4 -44 -2 -38 Q-10 -44 -24 -36 Z" fill="{c}"/>'
    return g(can + '<path d="M0 -50 V-6 q0 6 -6 6" stroke="#3A2A1E" stroke-width="2.5" fill="none"/>', x, y, s)


def raincloud(x, y, s=1):
    drops = ''.join(f'<path d="M{dx} 8 l-3 9" stroke="#7FA6DB" stroke-width="2.5" stroke-linecap="round"><animateTransform attributeName="transform" type="translate" values="0 0;-4 22" dur=".8s" begin="{b}s" repeatCount="indefinite"/>'
                    f'<animate attributeName="opacity" values="1;0" dur=".8s" begin="{b}s" repeatCount="indefinite"/></path>' for dx, b in ((-14, 0), (-2, .3), (10, .55), (20, .15)))
    return g('<ellipse cx="0" cy="0" rx="30" ry="13" fill="#8A97AB"/><circle cx="-12" cy="-8" r="13" fill="#8A97AB"/><circle cx="8" cy="-11" r="16" fill="#8A97AB"/>' + drops, x, y, s)


def bubble_think(x, y, inner, w=120, h=80):
    return (f'<g transform="translate({x} {y})"><ellipse cx="0" cy="0" rx="{w / 2}" ry="{h / 2}" fill="#fff" stroke="#C9CFD6" stroke-width="2"/>'
            f'<circle cx="{-w / 4}" cy="{h / 2 + 10}" r="7" fill="#fff" stroke="#C9CFD6" stroke-width="2"/><circle cx="{-w / 3}" cy="{h / 2 + 24}" r="4" fill="#fff" stroke="#C9CFD6" stroke-width="2"/>{inner}</g>')


# ------------------------------------------------------------ comida, mercado, tiendas
def crate(x, y, fruit='#E2574C', s=1, n=7):
    o = '<rect x="-26" y="-18" width="52" height="18" fill="#C8955E"/><path d="M-26 -9 H26" stroke="#A8743E" stroke-width="2"/>'
    o += ''.join(f'<circle cx="{-20 + i * 6.5}" cy="{-21 - (i % 2) * 4}" r="5.5" fill="{fruit}"/>' for i in range(n))
    return g(o, x, y, s)


def stall(x, y, s=1, a='#E2574C'):
    o = awning(-60, -110, 120, a, '#fff', 7) + '<rect x="-58" y="-86" width="4" height="86" fill="#8A5A3B"/><rect x="54" y="-86" width="4" height="86" fill="#8A5A3B"/>'
    o += '<rect x="-60" y="-40" width="120" height="40" fill="#B97A4E"/>'
    o += crate(-32, -40, '#E2574C', .9) + crate(0, -40, '#FFC94A', .9) + crate(32, -40, '#5BAA6A', .9)
    return g(o, x, y, s)


def scale_(x, y, s=1):
    return g('<rect x="-16" y="-10" width="32" height="10" rx="3" fill="#C9CFD6"/><rect x="-10" y="-26" width="20" height="16" rx="3" fill="#E9EEF2"/>'
             '<path d="M-20 -30 Q0 -22 20 -30" stroke="#A9B1BB" stroke-width="4" fill="none"/><circle cy="-18" r="4" fill="#fff" stroke="#5B6676"/><path d="M0 -18 L3 -21" stroke="#E2574C" stroke-width="1.5"/>', x, y, s)


def bread(x, y, s=1):
    return g('<ellipse cx="0" cy="-8" rx="24" ry="9" fill="#D9984A"/><path d="M-12 -14 l6 8 M-2 -16 l6 8 M8 -15 l6 8" stroke="#F3C987" stroke-width="2.5" stroke-linecap="round"/>', x, y, s)


def cheese(x, y, s=1):
    return g('<path d="M-20 0 L-20 -14 L18 -24 L22 -14 L22 0 Z" fill="#FFD66B"/><path d="M-20 -14 L18 -24 L22 -14 Z" fill="#FFE59A"/>'
             '<circle cx="-8" cy="-6" r="2.5" fill="#E8B83A"/><circle cx="8" cy="-8" r="2" fill="#E8B83A"/>', x, y, s)


def bottle(x, y, s=1, c='#3E8A52', label='#F3E2C4'):
    return g(f'<path d="M-7 0 L-7 -26 Q-7 -32 -3 -36 L-3 -46 L3 -46 L3 -36 Q7 -32 7 -26 L7 0 Z" fill="{c}"/><rect x="-7" y="-20" width="14" height="10" fill="{label}"/><rect x="-3" y="-50" width="6" height="5" fill="#8A5A3B"/>', x, y, s)


def bag(x, y, s=1, c='#F2B880', items=True):
    it = '<circle cx="-6" cy="-34" r="5" fill="#E2574C"/><rect x="2" y="-46" width="6" height="16" rx="2" fill="#3E8A52"/><path d="M-12 -32 q4 -14 10 -6" stroke="#5BAA6A" stroke-width="3" fill="none"/>' if items else ''
    return g(it + f'<path d="M-14 0 L-16 -30 L16 -30 L14 0 Z" fill="{c}"/><path d="M-6 -30 q6 -10 12 0" stroke="#8A5A3B" stroke-width="2" fill="none"/>', x, y, s)


def plate_pasta(x, y, s=1):
    return g('<ellipse cx="0" cy="0" rx="22" ry="6" fill="#fff" stroke="#C9CFD6"/><path d="M-12 -2 Q-6 -12 0 -4 Q6 -12 12 -2 Q4 -8 -2 -2 Q-8 -8 -12 -2" fill="#F3C25A" stroke="#E2A43A"/>'
             '<circle cx="-3" cy="-6" r="2.5" fill="#E2574C"/><circle cx="4" cy="-5" r="2" fill="#5BAA6A"/>', x, y, s)


def pizza(x, y, s=1):
    return g('<circle r="20" fill="#E8B060"/><circle r="16" fill="#E2574C"/><circle cx="-6" cy="-5" r="4" fill="#FFF3C4"/><circle cx="7" cy="2" r="4" fill="#FFF3C4"/><circle cx="-3" cy="8" r="3.5" fill="#FFF3C4"/>'
             '<circle cx="6" cy="-8" r="2" fill="#3E8A52"/><circle cx="-8" cy="5" r="2" fill="#3E8A52"/>', x, y, s)


def wine_glass(x, y, s=1, c='#B03A4A'):
    return g(f'<path d="M-7 -30 Q-8 -16 0 -14 Q8 -16 7 -30 Z" fill="#fff" stroke="#C9CFD6"/><path d="M-6.5 -24 Q-6 -16 0 -15 Q6 -16 6.5 -24 Z" fill="{c}"/><rect x="-1" y="-14" width="2" height="12" fill="#C9CFD6"/><ellipse cy="-1" rx="6" ry="1.8" fill="#C9CFD6"/>', x, y, s)


def candle(x, y, s=1):
    return g('<rect x="-3" y="-20" width="6" height="20" fill="#FFF3C4"/><path d="M0 -30 Q4 -24 0 -20 Q-4 -24 0 -30 Z" fill="#FFB25B"><animate attributeName="opacity" values="1;.6;1" dur=".9s" repeatCount="indefinite"/></path>', x, y, s)


def rack(x, y, s=1):
    cols = ['#E2574C', '#3F6FA8', '#FFC94A', '#5BAA6A', '#C77DBA']
    o = '<rect x="-50" y="-100" width="100" height="4" fill="#5B6676"/><rect x="-48" y="-100" width="4" height="100" fill="#5B6676"/><rect x="44" y="-100" width="4" height="100" fill="#5B6676"/>'
    for i, c in enumerate(cols):
        cx = -36 + i * 18
        o += f'<g><path d="M{cx} -98 l0 6" stroke="#5B6676" stroke-width="2"/><path d="M{cx - 9} -92 L{cx + 9} -92 L{cx + 11} -50 L{cx - 11} -50 Z" fill="{c}"/>{anim_rot(-3, 3, cx, -96, 3, i * .4)}</g>'
    return g(o, x, y, s)


def mannequin(x, y, s=1, c='#C77DBA'):
    return g(f'<rect x="-2" y="-20" width="4" height="20" fill="#5B6676"/><ellipse cy="-1" rx="12" ry="3" fill="#5B6676"/><path d="M-12 -66 Q-14 -40 -18 -20 L18 -20 Q14 -40 12 -66 Z" fill="{c}"/>'
             '<rect x="-12" y="-72" width="24" height="10" rx="5" fill="#E9DCCB"/><circle cy="-80" r="7" fill="#E9DCCB"/>', x, y, s)


def mirror(x, y, s=1):
    return g('<ellipse cx="0" cy="-60" rx="22" ry="40" fill="#8A5A3B"/><ellipse cx="0" cy="-60" rx="17" ry="35" fill="#DCEBF5"/><path d="M-8 -84 l12 -8 M-10 -70 l18 -12" stroke="#fff" stroke-width="3" opacity=".7"/>'
             '<rect x="-3" y="-20" width="6" height="20" fill="#8A5A3B"/>', x, y, s)


def tag(x, y, t, c='#5BAA6A'):
    t = tr(t)
    w = len(t) * 6 + 12
    return f'<g transform="translate({x} {y})"><rect x="{-w / 2}" y="-10" width="{w}" height="18" rx="4" fill="{c}"/>' + txt(0, 3, t, 10, '#fff', weight=900) + '</g>'


# ------------------------------------------------------------ viajes, salud, trabajo
def train(x, y, s=1, c='#E2574C'):
    o = (f'<path d="M-90 -10 L-90 -46 Q-90 -56 -80 -56 L60 -56 Q86 -56 96 -30 L100 -10 Z" fill="{c}"/>'
         '<rect x="-84" y="-48" width="22" height="16" rx="3" fill="#BFE4F7"/><rect x="-56" y="-48" width="22" height="16" rx="3" fill="#BFE4F7"/>'
         '<rect x="-28" y="-48" width="22" height="16" rx="3" fill="#BFE4F7"/><rect x="0" y="-48" width="22" height="16" rx="3" fill="#BFE4F7"/>'
         '<path d="M60 -50 Q80 -50 88 -32 L60 -32 Z" fill="#BFE4F7"/><rect x="-90" y="-26" width="190" height="5" fill="#fff" opacity=".8"/>'
         '<circle cx="-70" cy="-8" r="7" fill="#26323A"/><circle cx="-40" cy="-8" r="7" fill="#26323A"/><circle cx="40" cy="-8" r="7" fill="#26323A"/><circle cx="70" cy="-8" r="7" fill="#26323A"/>')
    return g(o, x, y, s)


def board(x, y, rows=(('ROMA', '10:15'), ('MILANO', '10:40'), ('NAPOLI', '11:05')), s=1):
    o = '<rect x="-60" y="-62" width="120" height="62" rx="5" fill="#26323A"/>'
    for i, (a, b) in enumerate(rows):
        o += txt(-50, -42 + i * 17, a, 10, '#FFD34D', 'start') + txt(50, -42 + i * 17, b, 10, '#FFD34D', 'end')
    return g(o + '<rect x="-3" y="0" width="6" height="30" fill="#5B6676"/>', x, y, s)


def hotel(x, y, s=1):
    o = '<rect x="-60" y="-160" width="120" height="160" fill="#F3D9A8"/><rect x="-40" y="-178" width="80" height="22" rx="4" fill="#3F6FA8"/>' + txt(0, -162, 'HOTEL', 13, '#fff', weight=900)
    for r in range(4):
        for c in range(3):
            o += f'<rect x="{-48 + c * 36}" y="{-148 + r * 32}" width="24" height="20" fill="#BFE4F7" stroke="#fff" stroke-width="2"/>'
    o += '<rect x="-14" y="-30" width="28" height="30" fill="#6B3E26"/><path d="M-30 -30 h60 l-6 -10 h-48 z" fill="#E2574C"/>'
    return g(o, x, y, s)


def key(x, y, s=1, rot=-30):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><circle cx="-14" cy="0" r="8" fill="none" stroke="#C9A24A" stroke-width="4"/><path d="M-6 0 H18 M12 0 v6 M18 0 v6" stroke="#C9A24A" stroke-width="4" stroke-linecap="round"/></g>'


def clinic(x, y, s=1):
    o = '<rect x="-70" y="-120" width="140" height="120" fill="#fff"/><rect x="-70" y="-120" width="140" height="10" fill="#9ED3F0"/>'
    o += '<rect x="-14" y="-104" width="28" height="28" rx="4" fill="#E2574C"/><rect x="-4" y="-100" width="8" height="20" fill="#fff"/><rect x="-10" y="-94" width="20" height="8" fill="#fff"/>'
    o += '<rect x="-56" y="-66" width="34" height="26" fill="#BFE4F7"/><rect x="22" y="-66" width="34" height="26" fill="#BFE4F7"/><rect x="-14" y="-40" width="28" height="40" fill="#9ED3F0"/>'
    return g(o, x, y, s)


def doctor(x, y, s=1, skin=1, face=1, hs='short', begin=0, hair='#3A2A1E', pose='stand'):
    p = person(x, y, '#fff', skin, hair, pose=pose, s=s, legs='#3F6FA8', face=face, hs=hs, begin=begin)
    steth = f'<g transform="translate({x} {y}) scale({s * 1.15 * face} {s * 1.15})"><path d="M-6 -44 Q-8 -32 0 -30 Q8 -32 6 -44" stroke="#26323A" stroke-width="1.6" fill="none"/><circle cx="0" cy="-30" r="2.4" fill="#5B6676"/></g>'
    return p + steth


def pill_bottle(x, y, s=1):
    return g('<rect x="-10" y="-28" width="20" height="28" rx="4" fill="#FFB25B"/><rect x="-11" y="-34" width="22" height="7" rx="2" fill="#fff"/><rect x="-10" y="-20" width="20" height="10" fill="#fff"/>'
             '<circle cx="18" cy="-4" r="4" fill="#E2574C"/><circle cx="26" cy="-3" r="4" fill="#fff" stroke="#C9CFD6"/>', x, y, s)


def thermo(x, y, s=1, rot=20):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-3.5" y="-34" width="7" height="30" rx="3.5" fill="#fff" stroke="#C9CFD6"/><rect x="-1.5" y="-24" width="3" height="20" fill="#E2574C"/><circle cy="-2" r="6" fill="#E2574C"/></g>'


def desk(x, y, s=1, c='#B97A4E'):
    return g(f'<rect x="-60" y="-46" width="120" height="8" rx="2" fill="{c}"/><rect x="-56" y="-38" width="30" height="38" fill="{c}"/><rect x="-52" y="-32" width="22" height="10" rx="2" fill="#8A5A3B"/><rect x="50" y="-38" width="6" height="38" fill="{c}"/>', x, y, s)


def whiteboard(x, y, w=110, h=70, lines=('', '', '')):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#fff" stroke="#9AA6B8" stroke-width="3"/>'
    for i, t in enumerate(lines):
        o += txt(x + 10, y + 22 + i * 18, t, 11, ['#3F6FA8', '#E2574C', '#2F7A4E'][i % 3], 'start')
    return o


def chart(x, y, w=120, h=80, up=True):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#fff" stroke="#C9CFD6" stroke-width="2"/>'
    vals = (.3, .45, .4, .6, .75) if up else (.75, .6, .65, .45, .35)
    for i, v in enumerate(vals):
        bh = (h - 20) * v
        o += f'<rect x="{x + 12 + i * (w - 24) / 5}" y="{y + h - 8 - bh}" width="{(w - 24) / 5 - 6}" height="{bh}" fill="{["#3F6FA8", "#5BAA6A", "#FFC94A", "#E2574C", "#C77DBA"][i]}"/>'
    o += f'<path d="M{x + 14} {y + h - 20} L{x + w - 14} {y + 18}" stroke="#E2574C" stroke-width="2.5" stroke-dasharray="4 4"/>' if up else ''
    return o


def briefcase(x, y, s=1, c='#8A5A3B'):
    return g(f'<rect x="-18" y="-24" width="36" height="24" rx="3" fill="{c}"/><path d="M-7 -24 v-5 h14 v5" stroke="{c}" stroke-width="3" fill="none"/><rect x="-18" y="-15" width="36" height="3" fill="#5E3E28"/>', x, y, s)


def cap(x, y, s=1):
    return g('<path d="M-26 -12 L0 -22 L26 -12 L0 -2 Z" fill="#26323A"/><path d="M-14 -7 V2 Q0 8 14 2 V-7" fill="#3B4F6B"/><path d="M22 -11 V2" stroke="#FFC94A" stroke-width="2"/><circle cx="22" cy="4" r="2.5" fill="#FFC94A"/>', x, y, s)


def coins(x, y, s=1):
    return g('<ellipse cx="0" cy="-3" rx="10" ry="4" fill="#C9A24A"/><ellipse cx="0" cy="-7" rx="10" ry="4" fill="#E0B94F"/><ellipse cx="0" cy="-11" rx="10" ry="4" fill="#F2CF63"/>'
             '<rect x="8" y="-22" width="30" height="16" rx="2" fill="#7FBF8A"/><circle cx="23" cy="-14" r="4" fill="#5BAA6A"/>' + txt(23, -11, '€', 7, '#fff'), x, y, s)


def atm(x, y, s=1):
    return g('<rect x="-26" y="-90" width="52" height="90" rx="5" fill="#5B6676"/><rect x="-18" y="-80" width="36" height="24" rx="2" fill="#BFE4F7"/>'
             '<rect x="-14" y="-48" width="28" height="18" rx="2" fill="#9AA6B8"/><rect x="-14" y="-22" width="28" height="4" rx="2" fill="#26323A"/>' + txt(0, -64, '€', 13, '#3F6FA8', weight=900), x, y, s)


def newspaper(x, y, s=1, rot=0, t='NOTIZIE'):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-26" y="-34" width="52" height="34" fill="#fff" stroke="#C9CFD6"/>'
            + txt(0, -24, t, 8, '#26323A', weight=900) + '<rect x="-22" y="-20" width="20" height="14" fill="#9AA6B8"/>'
            + ''.join(f'<rect x="2" y="{-20 + i * 4}" width="20" height="2" fill="#C9CFD6"/>' for i in range(4)) + '</g>')


def kiosk(x, y, s=1):
    o = '<rect x="-50" y="-90" width="100" height="90" fill="#3E8A52"/><path d="M-58 -90 L58 -90 L50 -112 L-50 -112 Z" fill="#2F7A4E"/>'
    o += txt(0, -96, 'EDICOLA', 11, '#fff', weight=900) + '<rect x="-42" y="-80" width="84" height="46" fill="#F3E2C4"/>'
    o += newspaper(-22, -42, .7) + newspaper(14, -44, .7, 6, 'SPORT') + '<rect x="-42" y="-30" width="84" height="30" fill="#2F7A4E"/>'
    return g(o, x, y, s)


def wifi(x, y, s=1, c='#3F6FA8'):
    return g(f'<path d="M-14 -10 Q0 -22 14 -10" stroke="{c}" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M-8 -4 Q0 -11 8 -4" stroke="{c}" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="0" cy="2" r="2.5" fill="{c}"/>', x, y, s)


def mailbox(x, y, s=1):
    return g('<rect x="-3" y="-40" width="6" height="40" fill="#5B6676"/><rect x="-18" y="-66" width="36" height="28" rx="12" fill="#E2574C"/><rect x="-10" y="-56" width="20" height="4" rx="2" fill="#26323A"/>', x, y, s)


def easel(x, y, s=1):
    return g('<path d="M-24 0 L-6 -100 M24 0 L6 -100 M0 -100 V-6" stroke="#8A5A3B" stroke-width="4"/>' + frame(-34, -96, 68, 54, '#F7C9A0') + '<rect x="-36" y="-42" width="72" height="5" fill="#8A5A3B"/>', x, y, s)


def gallery_frame(x, y, w, h, art):
    arts = {'sea': '#7FC3E8', 'sun': '#F7C9A0', 'night': '#3E4A8A', 'field': '#B8D99C'}
    return frame(x, y, w, h, arts.get(art, art))


def column(x, y, h=120, s=1):
    return g(f'<rect x="-14" y="{-h}" width="28" height="{h}" fill="#F1E8DA"/>' + ''.join(f'<path d="M{dx} {-h + 8} V-8" stroke="#D8CDBB" stroke-width="2"/>' for dx in (-7, 0, 7))
             + f'<rect x="-18" y="{-h - 8}" width="36" height="10" fill="#E6DCC9"/><rect x="-18" y="-8" width="36" height="8" fill="#E6DCC9"/>', x, y, s)


def gavel(x, y, s=1):
    return g('<rect x="-20" y="-6" width="40" height="6" rx="2" fill="#8A5A3B"/><g transform="rotate(-30)"><rect x="-2" y="-34" width="4" height="30" fill="#8A5A3B"/><rect x="-12" y="-44" width="24" height="12" rx="3" fill="#5E3E28"/></g>', x, y, s)


def scales(x, y, s=1):
    return g('<rect x="-2" y="-60" width="4" height="56" fill="#C9A24A"/><rect x="-14" y="-6" width="28" height="6" rx="2" fill="#C9A24A"/><path d="M-30 -56 H30" stroke="#C9A24A" stroke-width="3"/>'
             '<path d="M-30 -56 L-40 -34 M-30 -56 L-20 -34 M30 -56 L20 -34 M30 -56 L40 -34" stroke="#C9A24A" stroke-width="1.5"/>'
             '<path d="M-42 -34 Q-30 -24 -18 -34 Z M18 -34 Q30 -24 42 -34 Z" fill="#E0B94F"/>', x, y, s)


def flask(x, y, s=1, c='#5BAA6A'):
    return g(f'<path d="M-6 -40 V-26 L-18 -4 Q-20 0 -14 0 H14 Q20 0 18 -4 L6 -26 V-40 Z" fill="#E9F4F8" stroke="#9AA6B8" stroke-width="2"/><path d="M-13 -10 L13 -10 L17 -3 Q18 0 14 0 H-14 Q-18 0 -17 -3 Z" fill="{c}"/>'
             '<circle cx="-3" cy="-16" r="2.5" fill="#fff"><animate attributeName="cy" values="-6;-30" dur="2s" repeatCount="indefinite"/></circle><rect x="-8" y="-44" width="16" height="5" rx="2" fill="#9AA6B8"/>', x, y, s)


def podium(x, y, s=1, c='#3F6FA8'):
    return g(f'<path d="M-30 0 L-24 -60 L24 -60 L30 0 Z" fill="{c}"/><rect x="-34" y="-68" width="68" height="10" rx="3" fill="#2F4F86"/><circle cx="0" cy="-34" r="10" fill="#fff" opacity=".3"/>'
             '<path d="M0 -68 Q6 -82 14 -84" stroke="#26323A" stroke-width="2.5" fill="none"/><rect x="12" y="-92" width="8" height="12" rx="4" fill="#26323A"/>', x, y, s)


def curtain_stage(w=400, top=0, h=700, c='#B03A4A'):
    return (f'<path d="M0 {top} H{w} V{top + 26} Q{w / 2} {top + 50} 0 {top + 26} Z" fill="{c}"/>'
            f'<path d="M0 {top} Q40 {top + h * .4} 18 {top + h * .7} L0 {top + h * .7} Z" fill="{c}"/><path d="M{w} {top} Q{w - 40} {top + h * .4} {w - 18} {top + h * .7} L{w} {top + h * .7} Z" fill="{c}"/>')


def star_rating(x, y, n=4, s=1):
    o = ''
    for i in range(5):
        o += f'<path transform="translate({i * 18} 0) scale(.9)" d="M0 -9 L2.6 -3 L9 -2.8 L4 1.4 L5.6 8 L0 4.4 L-5.6 8 L-4 1.4 L-9 -2.8 L-2.6 -3 Z" fill="{"#FFC94A" if i < n else "#E3E7EE"}"/>'
    return g(o, x, y, s)


def quill(x, y, s=1, rot=25):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0 0 Q-6 -30 6 -60 Q12 -30 0 0 Z" fill="#fff" stroke="#C9CFD6"/><path d="M0 0 L4 -50" stroke="#C9CFD6" stroke-width="1.2"/><path d="M-1 0 L1 8" stroke="#26323A" stroke-width="2"/></g>'


def scroll(x, y, s=1, lines=3):
    o = '<rect x="-34" y="-50" width="68" height="50" fill="#F6E7C3"/><rect x="-38" y="-56" width="76" height="10" rx="5" fill="#E6D2A0"/><rect x="-38" y="-4" width="76" height="10" rx="5" fill="#E6D2A0"/>'
    o += ''.join(f'<path d="M-26 {-40 + i * 10} H{20 - (i % 2) * 10}" stroke="#A8916A" stroke-width="2"/>' for i in range(lines))
    return g(o, x, y, s)


def laurel(x, y, s=1):
    leaves = ''.join(f'<ellipse cx="{-14 + i * 3}" cy="{-4 - i * 6}" rx="6" ry="3" fill="#5BAA6A" transform="rotate({-50 + i * 10} {-14 + i * 3} {-4 - i * 6})"/>'
                     f'<ellipse cx="{14 - i * 3}" cy="{-4 - i * 6}" rx="6" ry="3" fill="#5BAA6A" transform="rotate({50 - i * 10} {14 - i * 3} {-4 - i * 6})"/>' for i in range(5))
    return g(leaves, x, y, s)


def blackboard(x, y, w=150, h=90, lines=()):
    o = f'<rect x="{x - 6}" y="{y - 6}" width="{w + 12}" height="{h + 12}" rx="4" fill="#8A5A3B"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#2F5A48"/>'
    for i, t in enumerate(lines):
        o += txt(x + 12, y + 24 + i * 22, t, 13, '#F3F1E8', 'start', extra='font-style="italic"')
    return o + f'<rect x="{x + w - 34}" y="{y + h}" width="22" height="6" rx="2" fill="#F3F1E8"/>'


def check(x, y, ok=True, s=1):
    if ok:
        return g('<circle r="11" fill="#5BAA6A"/><path d="M-5 0 L-1 4 L6 -4" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>', x, y, s)
    return g('<circle r="11" fill="#E2574C"/><path d="M-4 -4 L4 4 M4 -4 L-4 4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>', x, y, s)


def wolf(x, y, s=1, face=1):
    b = ('<path d="M-30 -10 Q-34 -30 -14 -34 L14 -34 Q30 -34 32 -20 L40 -26 L38 -14 Q34 -2 20 -4 L-20 -4 Q-30 -4 -30 -10 Z" fill="#8A97AB"/>'
         '<path d="M18 -34 L22 -50 L28 -34 Z M28 -32 L34 -46 L36 -30 Z" fill="#6E7A8E"/><path d="M30 -26 L46 -22 L36 -16 Z" fill="#6E7A8E"/>'
         '<circle cx="32" cy="-26" r="1.8" fill="#26323A"/><path d="M-30 -14 Q-46 -20 -44 -34" stroke="#8A97AB" stroke-width="6" fill="none" stroke-linecap="round"/>'
         '<rect x="-24" y="-6" width="6" height="8" fill="#6E7A8E"/><rect x="14" y="-6" width="6" height="8" fill="#6E7A8E"/>')
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{b}</g>'


def pinocchio(x, y, s=1, begin=0):
    """Marioneta de madera con nariz larga (Collodi, 1883)."""
    o = person(0, 0, '#E2574C', 2, '#5E3E28', pose='wave', legs='#3F6FA8', hs='short', begin=begin)
    o += '<g transform="scale(1.15)"><path d="M0 -55 L26 -57 L0 -52 Z" fill="#E9B98A"><animateTransform attributeName="transform" type="scale" values="1 1;1.25 1;1 1" dur="3s" repeatCount="indefinite"/></path>'
    o += '<path d="M-10 -67 L10 -67 L4 -84 Z" fill="#E2574C"/><circle cx="4" cy="-86" r="2.5" fill="#FFC94A"/></g>'
    return g(o, x, y, s)


def castle(x, y, s=1):
    o = '<rect x="-60" y="-80" width="120" height="80" fill="#D9CBEB"/><rect x="-74" y="-110" width="30" height="110" fill="#CBB9E2"/><rect x="44" y="-110" width="30" height="110" fill="#CBB9E2"/>'
    o += '<path d="M-78 -110 L-59 -140 L-40 -110 Z M40 -110 L59 -140 L78 -110 Z" fill="#7A5B8A"/>'
    o += ''.join(f'<rect x="{-60 + i * 20}" y="-90" width="12" height="10" fill="#D9CBEB"/>' for i in range(6))
    o += '<path d="M-14 0 v-30 a14 14 0 0 1 28 0 v30 z" fill="#6B3E26"/><rect x="-64" y="-90" width="10" height="14" fill="#5B4A6B"/><rect x="54" y="-90" width="10" height="14" fill="#5B4A6B"/>'
    o += '<path d="M-59 -140 V-156 L-46 -150 L-59 -144" fill="#E2574C"/><path d="M59 -140 V-156 L72 -150 L59 -144" fill="#E2574C"/>'
    return g(o, x, y, s)


def bridge(x, y, w=260, c='#D9B48F', s=1):
    o = f'<path d="M{-w / 2} -20 Q0 -70 {w / 2} -20 L{w / 2} -6 L{-w / 2} -6 Z" fill="{c}"/>'
    o += ''.join(f'<path d="M{-w / 2 + 10 + i * (w - 20) / 6} -22 V-6" stroke="#B9946A" stroke-width="3"/>' for i in range(7))
    o += f'<path d="M{-w / 3} -6 Q{-w / 6} -40 0 -6 Q{w / 6} -40 {w / 3} -6" fill="#9ED3F0"/>'
    return g(o, x, y, s)


def boat(x, y, s=1, c='#E2574C'):
    return g(f'<g><path d="M-30 -8 L30 -8 L22 4 L-22 4 Z" fill="{c}"/><path d="M0 -8 V-50 L24 -14 Z" fill="#fff"/><path d="M0 -50 V-8" stroke="#5B6676" stroke-width="2"/>{anim_rot(-4, 4, 0, 0, 3)}</g>', x, y, s)


def house_small(x, y, s=1, wall='#F6D9A8', roof='#C0583F', lit=False):
    win = '#FFD66B' if lit else '#BFE4F7'
    return g(f'<rect x="-30" y="-44" width="60" height="44" fill="{wall}"/><path d="M-36 -42 L0 -70 L36 -42 Z" fill="{roof}"/>'
             f'<rect x="-22" y="-34" width="14" height="12" fill="{win}"/><rect x="8" y="-34" width="14" height="12" fill="{win}"/><rect x="-6" y="-22" width="12" height="22" fill="#6B3E26"/>', x, y, s)


def farmhouse(x, y, s=1):
    return g('<rect x="-60" y="-60" width="120" height="60" fill="#F2D3A6"/><path d="M-68 -58 L-30 -86 L68 -86 L68 -58 Z" fill="#C0583F"/>'
             '<rect x="-50" y="-44" width="16" height="16" fill="#3E8A52"/><rect x="34" y="-44" width="16" height="16" fill="#3E8A52"/><path d="M-12 0 v-28 a12 12 0 0 1 24 0 v28 z" fill="#6B3E26"/>'
             '<rect x="40" y="-100" width="10" height="18" fill="#B97A4E"/>', x, y, s)


def hay(x, y, s=1):
    return g('<ellipse cx="0" cy="-16" rx="24" ry="17" fill="#E8C46A"/><path d="M-16 -20 q6 -6 12 0 M2 -12 q6 -6 12 0 M-10 -6 q6 -6 12 0" stroke="#C9A24A" stroke-width="2" fill="none"/>', x, y, s)


def chicken(x, y, s=1, face=1):
    b = ('<ellipse cx="0" cy="-10" rx="10" ry="8" fill="#fff"/><circle cx="8" cy="-18" r="5.5" fill="#fff"/><path d="M8 -24 l2 -4 l2 4 l2 -3 l1 4 Z" fill="#E2574C"/>'
         '<path d="M13 -18 l5 1.5 l-5 1.5 z" fill="#FFB25B"/><circle cx="9.5" cy="-19" r="1" fill="#26323A"/><path d="M-2 -2 v4 M3 -2 v4" stroke="#FFB25B" stroke-width="1.5"/>')
    return f'<g transform="translate({x} {y}) scale({s * face} {s})"><g>{b}{anim_rot(-6, 6, 0, -2, 1.4)}</g></g>'


def owl(x, y, s=1):
    return g('<ellipse cx="0" cy="-16" rx="12" ry="15" fill="#8A5A3B"/><circle cx="-5" cy="-22" r="5" fill="#fff"/><circle cx="5" cy="-22" r="5" fill="#fff"/>'
             '<circle cx="-5" cy="-22" r="2.2" fill="#26323A"><animate attributeName="r" values="2.2;.3;2.2" dur="4s" repeatCount="indefinite"/></circle><circle cx="5" cy="-22" r="2.2" fill="#26323A"><animate attributeName="r" values="2.2;.3;2.2" dur="4s" repeatCount="indefinite"/></circle>'
             '<path d="M-2 -16 L0 -12 L2 -16 Z" fill="#FFB25B"/><path d="M-12 -30 L-8 -24 M12 -30 L8 -24" stroke="#8A5A3B" stroke-width="3"/>', x, y, s)


def boxes(x, y, s=1):
    return g('<rect x="-30" y="-30" width="34" height="30" fill="#C8955E"/><rect x="-2" y="-46" width="30" height="46" fill="#D9A86E"/><rect x="-24" y="-56" width="26" height="26" fill="#E3B57E"/>'
             '<path d="M-30 -20 H4 M-2 -30 H28 M-24 -46 H2" stroke="#A8743E" stroke-width="2"/>', x, y, s)


def flyer(x, y, lines=('CERCASI', 'COINQUILINO'), s=1, rot=-4):
    o = f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-40" y="-56" width="80" height="56" fill="#FFF8D6" stroke="#E0C97A"/><circle cy="-56" r="3.5" fill="#E2574C"/>'
    o += ''.join(txt(0, -38 + i * 15, t, 10 if i else 11, '#26323A', weight=900) for i, t in enumerate(lines))
    o += ''.join(f'<rect x="{-34 + i * 10}" y="-10" width="6" height="10" fill="#fff" stroke="#E0C97A"/>' for i in range(7))
    return o + '</g>'


def letter_blocks(x, y, word, s=1):
    word = tr(word)
    if globals().get('MIRROR'):        # la escena se reflejará: se invierte el orden para que se lea bien
        word = word[::-1]
    cols = ['#E2574C', '#3F6FA8', '#FFC94A', '#5BAA6A', '#C77DBA', '#F2B880', '#5BB9B0']
    o = ''.join(f'<g transform="translate({i * 26} {-((i % 2) * 4)})"><rect x="-12" y="-24" width="24" height="24" rx="4" fill="{cols[i % 7]}"/>' + txt(0, -6, ch, 15, '#fff', weight=900) + '</g>' for i, ch in enumerate(word))
    return g(o, x, y, s)


def magnifier(x, y, s=1):
    return g('<circle cx="0" cy="-20" r="16" fill="#DCEBF5" opacity=".7" stroke="#5B6676" stroke-width="5"/><path d="M11 -9 L26 6" stroke="#5B6676" stroke-width="7" stroke-linecap="round"/>', x, y, s)


def microphone(x, y, s=1):
    return g('<rect x="-2" y="-60" width="4" height="60" fill="#5B6676"/><ellipse cy="-1" rx="12" ry="3" fill="#5B6676"/><rect x="-6" y="-80" width="12" height="20" rx="6" fill="#26323A"/>', x, y, s)


def apartment(x, y, s=1, wall='#F2D3A6', floors=4):
    o = f'<rect x="-70" y="{-floors * 40 - 10}" width="140" height="{floors * 40 + 10}" fill="{wall}"/><rect x="-74" y="{-floors * 40 - 16}" width="148" height="8" fill="#C0583F"/>'
    for f in range(floors):
        for c in range(3):
            yy = -floors * 40 + f * 40
            o += f'<rect x="{-56 + c * 42}" y="{yy}" width="28" height="22" fill="#BFE4F7" stroke="#fff" stroke-width="2"/><rect x="{-60 + c * 42}" y="{yy + 22}" width="36" height="5" fill="#9AA6B8"/>'
    o += '<rect x="-12" y="-34" width="24" height="34" fill="#6B3E26"/>'
    return g(o, x, y, s)


def noticeboard(x, y, s=1):
    return g('<rect x="-40" y="-60" width="80" height="56" fill="#C8955E"/><rect x="-34" y="-54" width="30" height="22" fill="#fff"/><rect x="4" y="-52" width="30" height="20" fill="#FFF3C4"/><rect x="-20" y="-28" width="34" height="20" fill="#E8F4EC"/>'
             '<circle cx="-19" cy="-54" r="2" fill="#E2574C"/><circle cx="19" cy="-52" r="2" fill="#3F6FA8"/><circle cx="-3" cy="-28" r="2" fill="#5BAA6A"/>', x, y, s)


def clipboard(x, y, s=1):
    return g('<rect x="-20" y="-50" width="40" height="50" rx="4" fill="#B97A4E"/><rect x="-15" y="-44" width="30" height="40" fill="#fff"/><rect x="-8" y="-54" width="16" height="8" rx="2" fill="#5B6676"/>'
             + ''.join(f'<path d="M-10 {-34 + i * 8} H10" stroke="#9AA6B8" stroke-width="2"/>' for i in range(4)) + '<path d="M-10 -36 l2 2 l4 -4" stroke="#5BAA6A" stroke-width="2" fill="none"/>', x, y, s)


def stamp_(x, y, s=1, t='OK'):
    return g('<rect x="-10" y="-34" width="20" height="18" rx="4" fill="#8A5A3B"/><rect x="-16" y="-16" width="32" height="10" rx="2" fill="#5E3E28"/>'
             f'<rect x="-22" y="-2" width="44" height="14" rx="2" fill="none" stroke="#E2574C" stroke-width="2" transform="translate(30 0) rotate(-8)"/>' + f'<g transform="translate(30 0) rotate(-8)">' + txt(0, 9, t, 9, '#E2574C', weight=900) + '</g>', x, y, s)


def globe(x, y, s=1):
    return g('<circle cy="-30" r="22" fill="#7FC3E8"/><path d="M-14 -44 q10 6 6 14 q-6 4 -2 12 q8 4 4 12 M8 -48 q-4 10 6 14 q8 0 4 12" fill="none" stroke="#5BAA6A" stroke-width="6" stroke-linecap="round"/>'
             '<path d="M-26 -30 a26 26 0 0 0 52 0" stroke="#8A5A3B" stroke-width="3" fill="none"/><rect x="-3" y="-6" width="6" height="6" fill="#8A5A3B"/><rect x="-12" y="-2" width="24" height="4" rx="2" fill="#8A5A3B"/>', x, y, s)


def armchair(x, y, s=1, c='#B03A4A', face=1):
    b = f'<rect x="-26" y="-30" width="52" height="18" rx="6" fill="{c}"/><rect x="-32" y="-42" width="12" height="36" rx="5" fill="{c}"/><rect x="20" y="-42" width="12" height="36" rx="5" fill="{c}"/><rect x="-24" y="-66" width="48" height="40" rx="12" fill="{c}"/><rect x="-26" y="-6" width="5" height="6" fill="#5E3E28"/><rect x="21" y="-6" width="5" height="6" fill="#5E3E28"/>'
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{b}</g>'


def italy_map(x0=0, y0=0, w=400, h=700, hi=None):
    """Mapa real de Italia (Natural Earth, dominio público) ajustado al lienzo."""
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo'))
    import europe, importlib
    europe = importlib.reload(europe)
    europe.LON0, europe.LON1, europe.LAT1 = 5.0, 20.0, 47.6
    europe.K = 400 / math.radians(europe.LON1 - europe.LON0)
    paths = europe.country_paths(tol=.6)
    o = ''
    for name, d in paths.items():
        o += f'<path d="{d}" fill="{"#F7DDBE" if name == "Italy" else "#EFE7D3"}" stroke="#fff" stroke-width="1.4" stroke-linejoin="round"/>'
    return o, europe.proj
