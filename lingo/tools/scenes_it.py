"""Genera src/scenes.js: fondos ilustrados (SVG) y tipo de camino para las 50 unidades del italiano.
Lienzo 400 × 700. Los nodos del camino van por el centro y se desplazan hacia la derecha en las
unidades impares (1, 3, 5) y hacia la izquierda en las pares (2, 4): la ilustración ocupa el lado libre."""
import json, math, os

W, H = 400, 700
SK = ['#F2C9A5', '#D9A47A', '#F6D7BC', '#B9825A', '#8D5A3B']


def g(inner, tx=0, ty=0, s=1, extra=''):
    return f'<g transform="translate({tx} {ty}) scale({s})" {extra}>{inner}</g>'


def anim_rot(a0, a1, cx, cy, dur, begin=0):
    return (f'<animateTransform attributeName="transform" type="rotate" values="{a0} {cx} {cy};{a1} {cx} {cy};{a0} {cx} {cy}" '
            f'dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>')


def anim_move(dx, dy, dur, begin=0):
    return (f'<animateTransform attributeName="transform" type="translate" additive="sum" values="0 0;{dx} {dy};0 0" '
            f'dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>')


_ids = [0]
TR = globals().get('TR', {})      # traducciones de los textos (otros idiomas)
SEEN = globals().get('SEEN')      # si es un set, recoge los textos usados


def tr(t):
    if SEEN is not None:
        SEEN.add(t)
    return TR.get(t, t)


def sky(c1, c2, h=H):
    _ids[0] += 1; i = 'scn-sky%d' % _ids[0]
    return (f'<defs><linearGradient id="{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/>'
            f'<stop offset="1" stop-color="{c2}"/></linearGradient></defs><rect width="{W}" height="{h}" fill="url(#{i})"/>')


def cloud(x, y, s=1, dur=40, dx=30):
    c = ('<ellipse cx="0" cy="0" rx="26" ry="12" fill="#fff"/><circle cx="-10" cy="-8" r="12" fill="#fff"/>'
         '<circle cx="9" cy="-11" r="15" fill="#fff"/>')
    return f'<g transform="translate({x} {y}) scale({s})" opacity=".92"><g>{c}{anim_move(dx, 0, dur)}</g></g>'


def sun(x, y, r=26, col='#FFC94A'):
    rays = ''.join(f'<rect x="-3" y="{-r - 16}" width="6" height="11" rx="3" fill="{col}" transform="rotate({a})"/>' for a in range(0, 360, 30))
    return (f'<g transform="translate({x} {y})"><g>{rays}<animateTransform attributeName="transform" type="rotate" '
            f'from="0" to="360" dur="60s" repeatCount="indefinite"/></g><circle r="{r}" fill="{col}"/></g>')


def _arm(sk, sleeve, x0, y0, x1, y1, x2, y2):
    return (f'<path d="M{x0} {y0} L{x1} {y1}" stroke="{sleeve}" stroke-width="6.5" stroke-linecap="round"/>'
            f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{sk}" stroke-width="4.6" stroke-linecap="round"/>'
            f'<circle cx="{x2}" cy="{y2}" r="2.9" fill="{sk}"/>')


def person(x, y, shirt, skin=0, hair='#3A2A1E', pose='stand', long=False, s=1, legs='#33415C', face=1, begin=0, old=False,
           hs=None, skirt=False, glasses=False, beard=False, shoes='#3A2E2A'):
    """Figura de frente, unos 62 px de alto, con los pies en (x, y)."""
    sk = SK[skin % len(SK)]
    hc = '#D3D6DB' if old else hair
    hs = hs or ('long' if long else 'short')
    dark = 'rgba(0,0,0,.14)'
    o = ''
    # pelo de detrás (melena)
    if hs == 'long':
        o += f'<path d="M-10 -58 Q-12 -38 -9 -36 L9 -36 Q12 -38 10 -58 Z" fill="{hc}"/>'
    # piernas y zapatos
    if skirt:
        o += (f'<rect x="-6" y="-20" width="4" height="18" rx="2" fill="{sk}"/><rect x="2" y="-20" width="4" height="18" rx="2" fill="{sk}"/>'
              f'<path d="M-10 -27 L-13 -16 Q0 -13 13 -16 L10 -27 Z" fill="{legs}"/>')
    else:
        o += (f'<path d="M-9 -27 L-8.5 -3 L-1.5 -3 L0 -20 L1.5 -3 L8.5 -3 L9 -27 Z" fill="{legs}"/>'
              f'<path d="M0 -20 L0 -26" stroke="{dark}" stroke-width="1"/>')
    o += (f'<ellipse cx="-5" cy="-1.8" rx="4.6" ry="2.4" fill="{shoes}"/><ellipse cx="5" cy="-1.8" rx="4.6" ry="2.4" fill="{shoes}"/>')
    # brazo izquierdo (siempre abajo)
    o += _arm(sk, shirt, -10.5, -42, -12.5, -32, -13, -23)
    # torso
    o += (f'<path d="M-10 -45 Q-12.5 -45 -12 -40 L-10 -25 Q0 -23 10 -25 L12 -40 Q12.5 -45 10 -45 Z" fill="{shirt}"/>'
          f'<path d="M-10 -25 Q0 -23 10 -25 L10 -28 Q0 -26 -10 -28 Z" fill="{dark}"/>'
          f'<path d="M-3.5 -45 L0 -40.5 L3.5 -45" fill="{sk}"/>')
    # brazo derecho según la postura
    if pose == 'wave':
        o += f'<g>{_arm(sk, shirt, 10.5, -42, 16, -50, 18, -59)}{anim_rot(-14, 18, 10.5, -42, 1.1, begin)}</g>'
    elif pose == 'shake':
        o += _arm(sk, shirt, 10.5, -42, 14, -33, 21, -31)
    elif pose == 'hold':
        o += _arm(sk, shirt, 10.5, -42, 13, -33, 20, -36)
    elif pose == 'point':
        o += _arm(sk, shirt, 10.5, -42, 17, -41, 24, -44)
    else:
        o += _arm(sk, shirt, 10.5, -42, 12.5, -32, 13, -23)
    # cuello, orejas y cabeza
    o += (f'<rect x="-2.6" y="-48.5" width="5.2" height="5" fill="{sk}"/><rect x="-2.6" y="-48.5" width="5.2" height="2" fill="{dark}"/>'
          f'<circle cx="-8.6" cy="-56" r="2.2" fill="{sk}"/><circle cx="8.6" cy="-56" r="2.2" fill="{sk}"/>'
          f'<ellipse cx="0" cy="-57" rx="8.6" ry="9.6" fill="{sk}"/>')
    # pelo de delante
    if hs == 'short':
        o += f'<path d="M-8.8 -58 Q-9.5 -68.5 0 -68.5 Q9.5 -68.5 8.8 -58 Q7 -63 2 -63.5 Q-3 -64 -5 -61.5 Q-7 -61 -8.8 -58 Z" fill="{hc}"/>'
    elif hs == 'long':
        o += f'<path d="M-9.4 -55 Q-11 -69 0 -69 Q11 -69 9.4 -55 Q8 -62 3 -63 Q-1 -60 -6 -62.5 Q-8.5 -60 -9.4 -55 Z" fill="{hc}"/>'
    elif hs == 'bun':
        o += (f'<circle cx="0" cy="-70" r="4.6" fill="{hc}"/><path d="M-8.8 -57 Q-9.5 -68 0 -68 Q9.5 -68 8.8 -57 Q6 -63 0 -63 Q-6 -63 -8.8 -57 Z" fill="{hc}"/>')
    elif hs == 'curly':
        o += ''.join(f'<circle cx="{cx}" cy="{cy}" r="3.6" fill="{hc}"/>' for cx, cy in ((-7, -61), (-4, -66), (1, -67.5), (6, -65), (8, -60), (-8.5, -57)))
    elif hs == 'bald':
        o += f'<path d="M-8.8 -55 Q-9.5 -60 -7 -61 L-7.5 -54 Z M8.8 -55 Q9.5 -60 7 -61 L7.5 -54 Z" fill="{hc}"/>'
    # cara
    o += (f'<path d="M-5 -60.5 h2.8 M2.2 -60.5 h2.8" stroke="{hc if not old else "#9AA0A8"}" stroke-width="1.1" stroke-linecap="round"/>'
          f'<circle cx="-3.4" cy="-57.4" r="1.25" fill="#26323A"/><circle cx="3.4" cy="-57.4" r="1.25" fill="#26323A"/>'
          f'<circle cx="-5.2" cy="-53.6" r="1.9" fill="#F08A7E" opacity=".35"/><circle cx="5.2" cy="-53.6" r="1.9" fill="#F08A7E" opacity=".35"/>'
          f'<path d="M-2.4 -52.6 Q0 -50.4 2.4 -52.6" stroke="#8A3B2E" stroke-width="1.2" fill="none" stroke-linecap="round"/>')
    if glasses or old:
        o += '<circle cx="-3.4" cy="-57.4" r="2.7" fill="none" stroke="#26323A" stroke-width=".9"/><circle cx="3.4" cy="-57.4" r="2.7" fill="none" stroke="#26323A" stroke-width=".9"/><path d="M-.7 -57.4 h1.4" stroke="#26323A" stroke-width=".9"/>'
    if beard:
        o += f'<path d="M-8 -56 Q-8 -47 0 -46.5 Q8 -47 8 -56 Q6 -51 2.5 -51.5 Q0 -50 -2.5 -51.5 Q-6 -51 -8 -56 Z" fill="{hc}"/>'
    s *= 1.15
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{o}</g>'


def bubble(x, y, text, col='#fff', ink='#26323A', side=1, size=12):
    text = tr(text)
    if len(text) * size * .58 + 16 > 176:      # textos largos (traducciones): se reduce la letra para que quepan
        size = round((176 - 16) / (len(text) * .58), 1)
    w = len(text) * size * .58 + 16
    x = min(max(x, 22 + w / 2), 378 - w / 2)   # que no se salga por los lados del lienzo
    tail = f'M{-6 * side} 10 L{-14 * side} 20 L{2 * side} 10' if side else ''
    return (f'<g transform="translate({x} {y})"><rect x="{-w / 2}" y="-12" width="{w}" height="24" rx="12" fill="{col}" stroke="#26323A" stroke-opacity=".18"/>'
            f'<path d="{tail}" fill="{col}"/><text x="0" y="4.5" text-anchor="middle" font-family="Nunito,Arial,sans-serif" font-weight="800" '
            f'font-size="{size}" fill="{ink}">{text}</text></g>')


def tree(x, y, s=1, c='#5BAA6A', c2='#3E8A52', kind='round', fruit=None):
    """Árbol con tronco ramificado, copa en tres tonos y brillos."""
    lite = '#8FD08F' if kind != 'olive' else '#C3D6A8'
    if kind == 'olive':
        c, c2 = '#8FAF7A', '#6E9060'
    o = ('<path d="M-4 0 Q-3 -14 -5 -24 L-1 -24 Q1 -16 3 -24 L6 -23 Q3 -12 4 0 Z" fill="#7A5236"/>'
         '<path d="M-3 -20 Q-10 -26 -14 -30 M2 -22 Q9 -27 13 -32" stroke="#7A5236" stroke-width="3" fill="none" stroke-linecap="round"/>'
         '<path d="M0 -4 Q-2 -12 0 -20" stroke="#5E3E28" stroke-width="1.2" fill="none"/>')
    o += (f'<circle cx="-14" cy="-34" r="12" fill="{c2}"/><circle cx="14" cy="-36" r="13" fill="{c2}"/>'
          f'<circle cx="0" cy="-46" r="17" fill="{c}"/><circle cx="-10" cy="-38" r="12" fill="{c}"/><circle cx="11" cy="-40" r="12" fill="{c}"/>'
          f'<circle cx="-5" cy="-52" r="7" fill="{lite}" opacity=".7"/><circle cx="8" cy="-46" r="4" fill="{lite}" opacity=".6"/>'
          f'<circle cx="-13" cy="-40" r="3.5" fill="{lite}" opacity=".55"/>')
    o += ''.join(f'<circle cx="{fx}" cy="{fy}" r="2.6" fill="{fruit}"/>' for fx, fy in ((-8, -32), (6, -34), (12, -44), (-2, -40), (-14, -44))) if fruit else ''
    o += f'<ellipse cx="0" cy="1" rx="18" ry="3.5" fill="rgba(0,0,0,.10)"/>'
    return g(o, x, y, s)


def pine(x, y, s=1):
    return g('<rect x="-3" y="-14" width="6" height="14" fill="#7A5236"/>'
             '<path d="M0 -70 L16 -38 L8 -38 L20 -14 L-20 -14 L-8 -38 L-16 -38 Z" fill="#2F7A4E"/>'
             '<path d="M0 -70 L6 -56 L-2 -50 Z M-6 -34 L4 -30 L-12 -18 Z" fill="#4E9A6A" opacity=".8"/>', x, y, s)


def cypress(x, y, s=1):
    return g('<rect x="-3" y="-12" width="6" height="12" fill="#7A5236"/><path d="M0 -78 Q12 -40 9 -12 L-9 -12 Q-12 -40 0 -78 Z" fill="#2F7A4E"/>', x, y, s)


def facade(x, y, w, h, col, shut='#3E8A52', rows=2, cols=2, roof='#C0583F', door=False):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/><rect x="{x - 3}" y="{y - 6}" width="{w + 6}" height="7" rx="2" fill="{roof}"/>'
    ww, wh = 13, 18
    for r in range(rows):
        for c in range(cols):
            wx = x + (c + .5) * w / cols - ww / 2
            wy = y + 12 + r * (wh + 14)
            out += (f'<rect x="{wx - 5}" y="{wy}" width="5" height="{wh}" fill="{shut}"/><rect x="{wx + ww}" y="{wy}" width="5" height="{wh}" fill="{shut}"/>'
                    f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="#3B4F6B" opacity=".55"/>')
    if door:
        out += f'<path d="M{x + w / 2 - 9} {y + h} v-20 a9 9 0 0 1 18 0 v20 z" fill="#6B3E26"/>'
    return out


def flowerpot(x, y, c='#E2574C'):
    return g(f'<path d="M-7 0 L-5 -10 L5 -10 L7 0 Z" fill="#C0583F"/><circle cx="-4" cy="-14" r="4" fill="{c}"/><circle cx="4" cy="-14" r="4" fill="{c}"/>'
             '<circle cy="-18" r="4" fill="#FFC94A"/><circle cx="0" cy="-12" r="3" fill="#3E8A52"/>', x, y)


def bench(x, y, s=1):
    return g('<rect x="-26" y="-14" width="52" height="5" rx="2" fill="#8A5A3B"/><rect x="-26" y="-24" width="52" height="5" rx="2" fill="#8A5A3B"/>'
             '<rect x="-22" y="-10" width="4" height="10" fill="#4A3A30"/><rect x="18" y="-10" width="4" height="10" fill="#4A3A30"/>', x, y, s)


def dog(x, y, s=1, face=1):
    body = ('<ellipse cx="0" cy="-10" rx="14" ry="7" fill="#C8955E"/><circle cx="13" cy="-18" r="7" fill="#C8955E"/>'
            '<path d="M10 -24 L8 -16 L13 -19 Z" fill="#8A5A3B"/><circle cx="16" cy="-19" r="1.2" fill="#26323A"/>'
            '<rect x="-10" y="-6" width="3.5" height="6" fill="#C8955E"/><rect x="6" y="-6" width="3.5" height="6" fill="#C8955E"/>'
            '<g><path d="M-14 -12 Q-22 -18 -20 -24" stroke="#C8955E" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
            + anim_rot(-12, 14, -14, -12, .5) + '</g>')
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{body}</g>'


def fountain(x, y):
    drops = ''.join(f'<circle cx="{dx}" cy="-46" r="2.2" fill="#BFE4F7"><animate attributeName="cy" values="-46;-20" dur="1.2s" begin="{b}s" repeatCount="indefinite"/>'
                    f'<animate attributeName="opacity" values="1;0" dur="1.2s" begin="{b}s" repeatCount="indefinite"/></circle>' for dx, b in ((-8, 0), (8, .4), (0, .8)))
    return g('<ellipse cx="0" cy="-6" rx="40" ry="10" fill="#9DB4C8"/><ellipse cx="0" cy="-10" rx="36" ry="8" fill="#7FC3E8"/>'
             '<rect x="-5" y="-40" width="10" height="30" fill="#C9CFD6"/><ellipse cx="0" cy="-40" rx="15" ry="5" fill="#B0B8C2"/>' + drops, x, y)


def suitcase(x, y, c='#E2574C', s=1):
    return g(f'<rect x="-12" y="-26" width="24" height="26" rx="4" fill="{c}"/><rect x="-6" y="-31" width="12" height="6" rx="2" fill="none" stroke="#4A3A30" stroke-width="2.5"/>'
             '<rect x="-12" y="-16" width="24" height="3" fill="#fff" opacity=".6"/><circle cx="-7" cy="1" r="2.5" fill="#4A3A30"/><circle cx="7" cy="1" r="2.5" fill="#4A3A30"/>', x, y, s)


def plane(x, y, s=1, c='#fff'):
    return g(f'<path d="M-30 0 Q-30 -6 -22 -6 L22 -6 Q32 -6 34 0 Q32 6 22 6 L-22 6 Q-30 6 -30 0 Z" fill="{c}" stroke="#9DB4C8"/>'
             '<path d="M-4 -4 L-14 -24 L-6 -24 L10 -4 Z" fill="#E2574C"/><path d="M-4 4 L-14 22 L-6 22 L10 4 Z" fill="#C0583F"/>'
             '<path d="M-28 -2 L-34 -16 L-26 -16 L-20 -4 Z" fill="#E2574C"/><circle cx="20" cy="-1" r="2" fill="#3B4F6B"/>'
             '<circle cx="12" cy="-1" r="2" fill="#3B4F6B"/><circle cx="4" cy="-1" r="2" fill="#3B4F6B"/>', x, y, s)


def flag(x, y, cols, horiz=False, s=1):
    if horiz:
        bands = ''.join(f'<rect x="0" y="{-26 + i * 18 / len(cols)}" width="26" height="{18 / len(cols) + .3}" fill="{c}"/>' for i, c in enumerate(cols))
    else:
        bands = ''.join(f'<rect x="{i * 26 / len(cols)}" y="-26" width="{26 / len(cols) + .3}" height="18" fill="{c}"/>' for i, c in enumerate(cols))
    return g(f'<rect x="-2" y="-28" width="2.5" height="28" fill="#5B6676"/>{bands}<rect x="0" y="-26" width="26" height="18" fill="none" stroke="#26323A" stroke-opacity=".2"/>', x, y, s)


def pin(x, y, c='#E2574C'):
    return g(f'<path d="M0 0 Q-11 -14 -11 -22 A11 11 0 0 1 11 -22 Q11 -14 0 0 Z" fill="{c}"/><circle cy="-22" r="4.5" fill="#fff"/>', x, y)


def number_balloon(x, y, n, c, begin=0):
    return (f'<g transform="translate({x} {y})"><g><path d="M0 18 Q-3 30 2 40" stroke="#9AA6B8" stroke-width="1.5" fill="none"/>'
            f'<ellipse cx="0" cy="0" rx="15" ry="18" fill="{c}"/><text y="6" text-anchor="middle" font-family="Nunito,Arial,sans-serif" font-weight="900" font-size="15" fill="#fff">{n}</text>'
            f'{anim_move(0, -8, 4, begin)}</g></g>')


def house(x, y, s=1, wall='#F6D9A8', roof='#C0583F'):
    return g(f'<rect x="-50" y="-70" width="100" height="70" fill="{wall}"/><path d="M-60 -68 L0 -112 L60 -68 Z" fill="{roof}"/>'
             '<rect x="-12" y="-36" width="24" height="36" rx="3" fill="#6B3E26"/><circle cx="7" cy="-18" r="2" fill="#FFC94A"/>'
             '<rect x="-40" y="-56" width="20" height="18" fill="#BFE4F7" stroke="#fff" stroke-width="3"/><rect x="20" y="-56" width="20" height="18" fill="#BFE4F7" stroke="#fff" stroke-width="3"/>'
             '<rect x="22" y="-104" width="12" height="22" fill="#8A5A3B"/>', x, y, s)


def clothesline(x, y, w=110):
    items = ''
    cols = ['#E2574C', '#3F6FA8', '#FFC94A', '#5BAA6A', '#C77DBA']
    for i in range(5):
        cx = x + 12 + i * (w - 24) / 4
        items += (f'<g><rect x="{cx - 8}" y="{y + 2}" width="16" height="18" rx="3" fill="{cols[i]}"/>'
                  f'{anim_rot(-6, 6, cx, y + 2, 2.4, i * .3)}</g>')
    return (f'<rect x="{x}" y="{y - 30}" width="4" height="62" fill="#8A5A3B"/><rect x="{x + w}" y="{y - 30}" width="4" height="62" fill="#8A5A3B"/>'
            f'<path d="M{x + 2} {y} Q{x + w / 2} {y + 8} {x + w + 2} {y}" stroke="#5B6676" stroke-width="1.5" fill="none"/>{items}')


def picnic(x, y):
    check = ''.join(f'<rect x="{x - 45 + (i % 6) * 15}" y="{y - 24 + (i // 6) * 12}" width="15" height="12" fill="{"#E2574C" if (i + i // 6) % 2 else "#fff"}"/>' for i in range(18))
    return (check + f'<g transform="translate({x + 6} {y - 30})"><path d="M-12 0 h24 l-3 10 h-18 z" fill="#C8955E"/><path d="M-10 0 q10 -14 20 0" stroke="#8A5A3B" stroke-width="2.5" fill="none"/></g>')


def awning(x, y, w, a='#E2574C', b='#fff', n=7):
    sw = w / n
    stripes = ''.join(f'<path d="M{x + i * sw} {y} h{sw} v22 q{-sw / 2} 8 {-sw} 0 z" fill="{a if i % 2 == 0 else b}"/>' for i in range(n))
    return f'<rect x="{x - 4}" y="{y - 6}" width="{w + 8}" height="7" rx="3" fill="#7A3A2E"/>{stripes}'


def cup(x, y, s=1, steam=True):
    st = ''
    if steam:
        for i, dx in enumerate((-4, 4)):
            st += (f'<path d="M{dx} -16 q-4 -6 0 -12 q4 -6 0 -12" stroke="#fff" stroke-width="2.2" fill="none" stroke-linecap="round" opacity=".9">'
                   f'<animate attributeName="opacity" values="0;.9;0" dur="2.4s" begin="{i * 1.2}s" repeatCount="indefinite"/>'
                   f'<animateTransform attributeName="transform" type="translate" values="0 4;0 -4" dur="2.4s" begin="{i * 1.2}s" repeatCount="indefinite"/></path>')
    return g(f'{st}<ellipse cx="0" cy="0" rx="14" ry="3.5" fill="#fff" stroke="#C9CFD6"/><path d="M-9 -14 h18 l-2 13 h-14 z" fill="#fff" stroke="#C9CFD6"/>'
             '<path d="M9 -11 q7 0 6 5 q-1 4 -7 3" stroke="#C9CFD6" stroke-width="2" fill="none"/><ellipse cx="0" cy="-14" rx="9" ry="2" fill="#6B3E26"/>', x, y, s)


def espresso_machine(x, y, s=1):
    return g('<rect x="-40" y="-60" width="80" height="60" rx="8" fill="#C9CFD6"/><rect x="-40" y="-60" width="80" height="14" rx="6" fill="#A9B1BB"/>'
             '<rect x="-30" y="-40" width="18" height="10" rx="2" fill="#5B6676"/><rect x="12" y="-40" width="18" height="10" rx="2" fill="#5B6676"/>'
             '<circle cx="0" cy="-35" r="7" fill="#E2574C"/><rect x="-26" y="-30" width="10" height="8" fill="#26323A"/><rect x="16" y="-30" width="10" height="8" fill="#26323A"/>'
             '<rect x="-36" y="-8" width="72" height="5" rx="2" fill="#7A8592"/>', x, y, s)


def cornetto(x, y, s=1):
    return g('<path d="M-16 0 Q-14 -14 0 -16 Q14 -14 16 0 Q8 -4 0 -4 Q-8 -4 -16 0 Z" fill="#E0A04A"/>'
             '<path d="M-8 -4 Q-6 -12 0 -14 M8 -4 Q6 -12 0 -14" stroke="#B87628" stroke-width="2" fill="none"/>', x, y, s)


def cafe_table(x, y, s=1, cups=1):
    out = ('<ellipse cx="0" cy="-34" rx="26" ry="7" fill="#fff" stroke="#C9CFD6"/><rect x="-2.5" y="-33" width="5" height="30" fill="#5B6676"/>'
           '<ellipse cx="0" cy="-2" rx="13" ry="3" fill="#5B6676"/>'
           '<path d="M-44 -2 L-40 -26 L-30 -26 L-32 -2 M-40 -26 L-40 -46" stroke="#5B6676" stroke-width="3" fill="none"/>'
           '<path d="M44 -2 L40 -26 L30 -26 L32 -2 M40 -26 L40 -46" stroke="#5B6676" stroke-width="3" fill="none"/>')
    if cups:
        out += cup(-8, -36, .55, False) + cup(10, -36, .55, True)
    return g(out, x, y, s)


def clock(x, y, r=18, h=8, m=0, spin=False):
    ah = math.radians(h * 30 + m / 2 - 90); am = math.radians(m * 6 - 90)
    hand_m = f'<path d="M0 0 L{r * .78 * math.cos(am):.1f} {r * .78 * math.sin(am):.1f}" stroke="#26323A" stroke-width="2" stroke-linecap="round">'
    hand_m += ('<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="12s" repeatCount="indefinite"/>' if spin else '') + '</path>'
    ticks = ''.join(f'<circle cx="{r * .78 * math.cos(math.radians(a)):.1f}" cy="{r * .78 * math.sin(math.radians(a)):.1f}" r="1.2" fill="#9AA6B8"/>' for a in range(0, 360, 30))
    return (f'<g transform="translate({x} {y})"><circle r="{r}" fill="#fff" stroke="#3F6FA8" stroke-width="3.5"/>{ticks}'
            f'<path d="M0 0 L{r * .5 * math.cos(ah):.1f} {r * .5 * math.sin(ah):.1f}" stroke="#26323A" stroke-width="3" stroke-linecap="round"/>{hand_m}<circle r="2" fill="#E2574C"/></g>')


def alarm(x, y, s=1):
    bells = '<circle cx="-12" cy="-30" r="6" fill="#E2574C"/><circle cx="12" cy="-30" r="6" fill="#E2574C"/>'
    return (f'<g transform="translate({x} {y}) scale({s})"><g>{bells}<circle cy="-14" r="17" fill="#E2574C"/><circle cy="-14" r="12" fill="#fff"/>'
            '<path d="M0 -14 V-22 M0 -14 L6 -11" stroke="#26323A" stroke-width="2" stroke-linecap="round"/>'
            '<path d="M-12 0 l-4 6 M12 0 l4 6" stroke="#26323A" stroke-width="3" stroke-linecap="round"/>'
            f'{anim_rot(-8, 8, 0, -14, .25)}</g></g>')


def bed(x, y, s=1):
    return g('<rect x="-40" y="-20" width="80" height="16" rx="4" fill="#3F6FA8"/><rect x="-44" y="-36" width="8" height="36" rx="3" fill="#8A5A3B"/>'
             '<rect x="36" y="-26" width="8" height="26" rx="3" fill="#8A5A3B"/><rect x="-34" y="-28" width="20" height="9" rx="4" fill="#fff"/>'
             '<path d="M-14 -21 Q10 -32 36 -21 Z" fill="#7FA6DB"/>', x, y, s)


def bus(x, y, s=1, c='#FFB72B'):
    return g(f'<rect x="-46" y="-40" width="92" height="34" rx="8" fill="{c}"/><rect x="-40" y="-34" width="18" height="12" rx="2" fill="#BFE4F7"/>'
             '<rect x="-18" y="-34" width="18" height="12" rx="2" fill="#BFE4F7"/><rect x="4" y="-34" width="18" height="12" rx="2" fill="#BFE4F7"/>'
             '<rect x="28" y="-34" width="14" height="22" rx="2" fill="#BFE4F7"/><circle cx="-26" cy="-6" r="7" fill="#26323A"/><circle cx="26" cy="-6" r="7" fill="#26323A"/>'
             '<circle cx="-26" cy="-6" r="3" fill="#C9CFD6"/><circle cx="26" cy="-6" r="3" fill="#C9CFD6"/>', x, y, s)


def moon(x, y, r=20):
    return f'<g transform="translate({x} {y})"><circle r="{r}" fill="#FFF3C4"/><circle cx="{r * .45}" cy="{-r * .2}" r="{r * .85}" fill="#2C3E73"/></g>'


def star(x, y, s=1, begin=0):
    return (f'<path transform="translate({x} {y}) scale({s})" d="M0 -6 L1.6 -1.6 L6 0 L1.6 1.6 L0 6 L-1.6 1.6 L-6 0 L-1.6 -1.6 Z" fill="#FFF3C4">'
            f'<animate attributeName="opacity" values="1;.25;1" dur="2.6s" begin="{begin}s" repeatCount="indefinite"/></path>')


def fg(inner, k=.86):
    """Primer plano: se acerca al centro para que no lo recorten los móviles estrechos."""
    return f'<g transform="translate(200 360) scale({k}) translate(-200 -360)">{inner}</g>'


def svg(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">{inner}</svg>')


# ---------------------------------------------------------------- 1 · Ciao! (piazza) — nodos a la derecha: lado libre izquierdo
def s1():
    o = sky('#BFE4F7', '#FBEFD9', 300)
    o += '<rect y="250" width="400" height="450" fill="#F3E2C4"/>'
    o += sun(330, 52, 22) + cloud(90, 60, 1, 46, 40) + cloud(250, 105, .8, 38, -30)
    # fachadas al fondo
    o += facade(0, 130, 78, 120, '#F2B880', rows=3, cols=2, door=True) + facade(78, 150, 64, 100, '#E8846B', rows=2, cols=2)
    o += facade(262, 140, 70, 110, '#F6D27A', rows=3, cols=2, shut='#3F6FA8') + facade(332, 120, 68, 130, '#E59A6F', rows=3, cols=2, door=True)
    o += cypress(150, 252, .9) + cypress(250, 252, .8)
    o += flowerpot(20, 252) + flowerpot(372, 252, '#C77DBA')
    # adoquines (líneas suaves)
    o += ''.join(f'<path d="M0 {y} H400" stroke="#E7D2AE" stroke-width="1.5"/>' for y in range(290, 700, 34))
    bg, o = o, ''
    o += tree(36, 300, .9, kind='olive') + fountain(70, 430)
    # parejas que se saludan (lado izquierdo y abajo)
    o += person(32, 356, '#3F6FA8', 1, '#2A1E18', pose='wave', begin=0, beard=True) + person(80, 356, '#E2574C', 2, '#6B3E1E', pose='wave', hs='long', skirt=True, legs='#3B4F6B', face=-1, begin=.4)
    o += bubble(40, 276, 'Ciao!', side=1) + bubble(104, 296, 'Ciao!', '#FFF3C4', side=-1)
    o += person(28, 580, '#5BAA6A', 0, '#B58A3C', pose='shake', hs='curly') + person(68, 580, '#5B4A6B', 3, '#1E1A18', pose='shake', face=-1, hs='bun', skirt=True, legs='#C77DBA')
    o += bubble(48, 506, 'Piacere!', '#E8F4EC', side=0)
    o += person(330, 670, '#B9821F', 1, pose='wave', old=True, hs='bald', begin=.2) + bubble(330, 592, 'Arrivederci!', side=0, size=11)
    o += person(52, 690, '#C77DBA', 2, '#3A2A1E', hs='long', pose='wave', begin=.7) + bubble(84, 616, 'Buongiorno!', '#FFF3C4', side=-1, size=11)
    o += dog(370, 410, .9, -1) + bench(352, 480, .9) + tree(372, 330, .75)
    return dict(path='stone', svg=svg(bg + fg(o)), tint='#F3E2C4')


# ---------------------------------------------------------------- 2 · Di dove sei? — mapa real de Europa (Natural Earth, dominio público)
def s2():
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo'))
    import europe
    paths = europe.country_paths()
    hi = {'Italy': '#F7C9A0', 'Spain': '#F6E08F', 'France': '#BFD7F2', 'Germany': '#D9CBEB', 'United Kingdom': '#C9E5C2', 'Portugal': '#F5C2C9'}
    o = '<rect width="400" height="700" fill="#9ED3F0"/>'
    # olas suaves en el mar
    o += ''.join(f'<path d="M{x} {y} q6 -4 12 0 q6 4 12 0" stroke="#C8E8F8" stroke-width="2" fill="none" stroke-linecap="round"/>' for x, y in ((40, 600), (330, 520), (20, 330), (250, 640), (360, 380), (60, 150), (210, 470)))
    for name, d in paths.items():
        o += f'<path d="{d}" fill="{hi.get(name, "#EFE7D3")}" stroke="#fff" stroke-width="1.2" stroke-linejoin="round"/>'
    o += cloud(300, 120, .9, 42, -40) + cloud(70, 650, .8, 44, 30) + cloud(250, 30, .7, 38, 30)
    P = {k: europe.proj(*v) for k, v in dict(Roma=(12.5, 41.9), Madrid=(-3.7, 40.4), Parigi=(2.35, 48.85), Berlino=(13.4, 52.5), Londra=(-0.13, 51.5), Lisbona=(-9.14, 38.72)).items()}
    # ruta de vuelo Madrid → Roma
    (mx, my), (rx, ry) = P['Madrid'], P['Roma']
    o += f'<path d="M{mx:.0f} {my:.0f} Q{(mx + rx) / 2:.0f} {min(my, ry) - 110:.0f} {rx:.0f} {ry:.0f}" stroke="#fff" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round" fill="none"/>'
    o += f'<g>{plane((mx + rx) / 2, min(my, ry) - 56, .55)}{anim_move(8, -4, 4)}</g>'
    flags = dict(Roma=['#009246', '#fff', '#CE2B37'], Madrid=['#AA151B', '#F1BF00', '#AA151B'], Parigi=['#002654', '#fff', '#CE1126'],
                 Berlino=['#000', '#DD0000', '#FFCE00'], Londra=['#012169', '#fff', '#C8102E'], Lisbona=['#046A38', '#DA291C', '#DA291C'])
    horiz = {'Madrid', 'Berlino'}
    # nombres de los países sobre el mapa, como en un atlas
    names = [('SPAGNA', -4.2, 38.9, 0, 15), ('FRANCIA', 2.6, 46.6, 0, 15), ('ITALIA', 13.2, 43.4, 52, 13), ('GERMANIA', 10.2, 51.0, 0, 12),
             ('REGNO UNITO', -2.2, 53.6, -62, 10), ('PORTOGALLO', -8.0, 39.6, -78, 8.5), ('MAROCCO', -6.5, 32.0, 0, 12), ('ALGERIA', 3.0, 32.0, 0, 12)]
    for t, lo, la, rot, fs in names:
        x, y = europe.proj(lo, la)
        o += (f'<text transform="translate({x:.0f} {y:.0f}) rotate({rot})" text-anchor="middle" font-family="Nunito,Arial,sans-serif" font-weight="900" '
              f'font-size="{fs}" letter-spacing="2" fill="#5B6676" opacity=".55">{t}</text>')
    for c, (x, y) in P.items():
        o += pin(x, y, '#E2574C') + flag(x + 7, y - 14, flags[c], horiz=c in horiz, s=.6)
        o += (f'<text x="{x:.0f}" y="{y + 13:.0f}" text-anchor="middle" font-family="Nunito,Arial,sans-serif" font-weight="800" font-size="10" '
              f'fill="#26323A" stroke="#fff" stroke-width="3" paint-order="stroke">{c}</text>')
    bg, o = o, ''
    # números en globos y viajeros
    o += number_balloon(368, 300, 7, '#E2574C', 0) + number_balloon(352, 560, 12, '#3F6FA8', 1) + number_balloon(372, 650, 20, '#5BAA6A', 2)
    o += person(320, 690, '#E2574C', 1, '#2A1E18', hs='long', pose='hold', skirt=True, legs='#3B4F6B') + suitcase(342, 692, '#3F6FA8')
    o += person(292, 610, '#3F6FA8', 3, pose='wave', face=-1, hs='curly') + bubble(256, 534, 'Di dove sei?', side=1, size=11)
    o += person(60, 690, '#B9821F', 0, '#C9A24A', pose='point', glasses=True) + suitcase(36, 692, '#FFB72B', .9) + bubble(76, 614, 'Sono spagnolo!', '#FFF3C4', side=0, size=11)
    return dict(path='flight', svg=svg(bg + fg(o)), tint='#9ED3F0')


# ---------------------------------------------------------------- 3 · La mia famiglia (casa y jardín) — lado libre izquierdo
def s3():
    o = sky('#CDEBFA', '#EAF6EA', 260)
    o += '<path d="M0 230 Q100 200 200 228 T400 222 V700 H0 Z" fill="#A9D69A"/><path d="M0 300 Q120 270 230 296 T400 290 V700 H0 Z" fill="#9BCB8A"/>'
    o += sun(60, 60, 22) + cloud(260, 70, 1, 44, -40) + cloud(150, 120, .7, 40, 30)
    o += house(80, 240, .95)
    o += tree(330, 240, 1.25, fruit='#E2574C') + tree(372, 262, .8, '#6DBA74') + pine(250, 236, .8)
    o += clothesline(250, 140, 120)
    bg, o = o, ''
    # familia en el jardín
    o += person(30, 366, '#5B4A6B', 1, old=True, pose='stand', hs='bald') + person(66, 366, '#C77DBA', 1, old=True, face=-1, hs='bun', skirt=True, legs='#7A5B8A')
    o += bench(47, 376, 1.1)
    o += bubble(48, 286, 'I nonni', side=0, size=11)
    o += picnic(70, 520)
    o += person(26, 510, '#3F6FA8', 2, pose='wave', beard=True) + person(112, 510, '#E2574C', 2, '#6B3E1E', hs='long', face=-1, pose='stand', skirt=True, legs='#F2B880')
    o += person(66, 476, '#FFB72B', 2, '#6B3E1E', s=.66, pose='wave', begin=.5, hs='curly') + bubble(70, 418, 'Mamma!', '#FFF3C4', side=0, size=11)
    o += dog(40, 610, 1) + person(84, 646, '#5BAA6A', 3, '#1E1A18', s=.66, pose='wave', face=-1, begin=.3, hs='bun', skirt=True, legs='#E2574C')
    o += tree(350, 470, .95, kind='olive') + flowerpot(372, 640) + flowerpot(340, 660, '#FFC94A')
    o += ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x, y, c in ((150, 600, '#fff'), (170, 650, '#FFC94A'), (300, 620, '#fff'), (120, 420, '#E2574C'), (320, 560, '#fff')))
    return dict(path='steps', svg=svg(bg + fg(o)), tint='#A9D69A')


# ---------------------------------------------------------------- 4 · Al bar (bar italiano) — lado libre derecho
def s4():
    o = '<rect width="400" height="700" fill="#F7E7CF"/>'
    o += '<rect width="400" height="250" fill="#E9C9A4"/>'
    o += awning(20, 40, 360, '#2F7A4E', '#fff', 10)
    o += ('<rect x="20" y="70" width="360" height="160" fill="#7A3A2E"/><rect x="34" y="84" width="150" height="110" rx="6" fill="#F3D9A8"/>'
          '<rect x="216" y="84" width="150" height="110" rx="6" fill="#F3D9A8"/>')
    o += ('<text x="200" y="66" text-anchor="middle" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="20" fill="#fff" '
          'stroke="#2F7A4E" stroke-width="5" paint-order="stroke">BAR</text>')
    o += espresso_machine(110, 194, .9) + cup(250, 194, .9) + cup(290, 194, .9, False) + cornetto(332, 192, .9)
    o += '<rect x="20" y="194" width="360" height="12" fill="#5B2A20"/>'
    # baldosas en damero suave
    o += ''.join(f'<rect x="{x}" y="{y}" width="40" height="40" fill="#EBD7B8"/>' for y in range(250, 700, 40) for x in range(0 if (y // 40) % 2 else 40, 400, 80))
    bg, o = o, ''
    o += cafe_table(330, 380, 1.0) + cafe_table(342, 560, .95)
    o += person(300, 366, '#3F6FA8', 1, pose='point', glasses=True) + bubble(300, 290, 'Un caffè!', '#fff', side=0, size=11)
    o += person(370, 552, '#E2574C', 2, '#6B3E1E', hs='long', face=-1, pose='stand', skirt=True, legs='#3B4F6B')
    # camarero con bandeja
    o += (person(290, 486, '#fff', 0, '#3A2A1E', pose='hold', legs='#26323A', beard=True) + '<path d="M286 448 l4 6 l4 -6" fill="#26323A"/>'
          + '<ellipse cx="311" cy="450" rx="14" ry="3" fill="#C9CFD6"/>' + cup(307, 448, .45, True))
    o += bubble(334, 420, 'Prego!', '#FFF3C4', side=1, size=11)
    o += person(300, 688, '#5B4A6B', 3, '#1E1A18', pose='hold', hs='bun', skirt=True, legs='#2F7A4E') + bubble(320, 612, "Quant'è?", side=0, size=11)
    o += '<g transform="translate(372 660)"><rect x="-14" y="-12" width="28" height="18" rx="4" fill="#5BAA6A"/><text y="2" text-anchor="middle" font-family="Nunito,Arial" font-weight="900" font-size="10" fill="#fff">€1,20</text></g>'
    return dict(path='tiles', svg=svg(bg + fg(o)), tint='#F7E7CF')


# ---------------------------------------------------------------- 5 · La mia giornata (de la mañana a la noche) — lado libre izquierdo
def s5():
    o = ('<defs><linearGradient id="scn-day" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD9A8"/><stop offset=".3" stop-color="#BFE4F7"/>'
         '<stop offset=".62" stop-color="#F7B58A"/><stop offset=".8" stop-color="#6E6AA8"/><stop offset="1" stop-color="#2C3E73"/></linearGradient></defs>'
         '<rect width="400" height="700" fill="url(#scn-day)"/>')
    # mañana: sol naciente, despertador, cama
    o += sun(330, 70, 24, '#FFB25B') + '<rect x="250" y="76" width="160" height="40" fill="#FFD9A8"/>'
    bg, o = o, ''
    o += bed(70, 120, .9) + person(56, 104, '#7FA6DB', 1, pose='wave', s=.62, hs='curly') + alarm(130, 70, .9)
    o += bubble(60, 40, 'Buongiorno!', '#fff', side=0, size=11)
    # mediodía: café, autobús, reloj
    o += clock(50, 230, 22, 8, 0, True) + cup(110, 255, 1.1)
    o += cloud(300, 220, 1, 40, -30) + cloud(150, 300, .8, 36, 30)
    o += bus(70, 380, .95) + person(132, 378, '#E2574C', 2, '#6B3E1E', hs='long', pose='wave', face=-1, begin=.3) + tree(30, 330, .7)
    # tarde: clase, trabajo
    o += clock(40, 470, 20, 6, 30) + '<g transform="translate(96 500)"><rect x="-24" y="-30" width="48" height="32" rx="4" fill="#3B4F6B"/><rect x="-20" y="-26" width="40" height="22" rx="2" fill="#BFE4F7"/><rect x="-30" y="2" width="60" height="5" rx="2" fill="#5B6676"/></g>'
    # noche: luna, estrellas, edificios con ventanas encendidas
    o += moon(330, 560, 20) + ''.join(star(x, y, s, b) for x, y, s, b in ((270, 600, 1, 0), (370, 630, .8, .8), (60, 590, .9, 1.4), (200, 650, .7, .4), (130, 620, .8, 2)))
    o += ''.join(f'<rect x="{x}" y="{700 - h}" width="{w}" height="{h}" fill="#1E2B52"/>' for x, w, h in ((0, 60, 60), (60, 44, 40), (330, 70, 50)))
    o += ''.join(f'<rect x="{x}" y="{y}" width="8" height="9" fill="#FFD66B"/>' for x, y in ((14, 652), (34, 668), (72, 672), (346, 664), (368, 680)))
    o += clock(110, 660, 16, 11, 0) + bubble(60, 556, 'Buonanotte!', '#FFF3C4', side=0, size=11)
    return dict(path='road', svg=svg(bg + fg(o)), tint='#BFE4F7', night=True)


_here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_here, 'scenes_lib2.py'), encoding='utf8').read())
exec(open(os.path.join(_here, 'scenes_more.py'), encoding='utf8').read())
if not globals().get('NO_WRITE'):
    SCENES = {1: s1(), 2: s2(), 3: s3(), 4: s4(), 5: s5()}
    SCENES.update(MORE)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'scenes.js')
    open(out, 'w', encoding='utf8').write(
        '// SAIMAP Lingo · Italiano · fondos ilustrados y tipo de camino por unidad (generado por tools/scenes_it.py)\n'
        'window.SCENES = ' + json.dumps(SCENES, ensure_ascii=False) + ';\n')
    print('ok', {k: len(v['svg']) for k, v in SCENES.items()})
