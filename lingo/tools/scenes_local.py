"""Toques locales y plantillas nuevas para inglés, portugués, francés y alemán.
Se ejecuta dentro del espacio de nombres del motor (después de scenes_it.py, scenes_lib2.py, scenes_more.py).
Todas las plantillas nuevas se dibujan con el lado libre a la IZQUIERDA (como las unidades impares);
el generador las refleja cuando la unidad es par."""

LOC = globals().get('LOC') or {}

# ---------------------------------------------------------------- fachadas según el país
_facade_it = facade


def facade(x, y, w, h, col, shut='#3E8A52', rows=2, cols=2, roof='#C0583F', door=False):
    a = LOC.get('arch')
    if not a:
        return _facade_it(x, y, w, h, col, shut, rows, cols, roof, door)
    k = int(x * 7 + w) % 3
    ww, wh = 13, 18
    if a == 'brick':
        col = ['#B5523B', '#A8573F', '#BE6A4B'][k]
        out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/>'
        out += ''.join(f'<path d="M{x} {yy} H{x + w}" stroke="#8E3F2C" stroke-width=".8" opacity=".5"/>' for yy in range(int(y) + 8, int(y + h), 8))
        out += f'<rect x="{x - 2}" y="{y - 8}" width="{w + 4}" height="9" fill="#4A4F5C"/><rect x="{x + w * .7}" y="{y - 22}" width="10" height="16" fill="#8E3F2C"/>'
        for r in range(rows):
            for c in range(cols):
                wx = x + (c + .5) * w / cols - ww / 2; wy = y + 12 + r * (wh + 14)
                out += f'<rect x="{wx - 2}" y="{wy - 2}" width="{ww + 4}" height="{wh + 4}" fill="#F4F1EA"/><rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="#3B4F6B" opacity=".6"/><path d="M{wx} {wy + wh / 2} H{wx + ww}" stroke="#F4F1EA" stroke-width="1.6"/>'
        if door:
            dc = ['#26323A', '#C0392B', '#2F5DA8'][k]
            out += f'<rect x="{x + w / 2 - 8}" y="{y + h - 24}" width="16" height="24" fill="{dc}"/><path d="M{x + w / 2 - 8} {y + h - 24} a8 6 0 0 1 16 0 z" fill="#F4F1EA"/>'
        return out
    if a == 'haussmann':
        col = '#EFE4CF'
        out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/>'
        out += f'<path d="M{x - 2} {y} L{x + 6} {y - 18} L{x + w - 6} {y - 18} L{x + w + 2} {y} Z" fill="#7F8A99"/><rect x="{x + w / 2 - 5}" y="{y - 16}" width="10" height="12" fill="#C9D3DE"/>'
        for r in range(rows):
            for c in range(cols):
                wx = x + (c + .5) * w / cols - ww / 2; wy = y + 10 + r * (wh + 14)
                out += f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh + 2}" fill="#3B4F6B" opacity=".55"/><path d="M{wx - 3} {wy + wh} H{wx + ww + 3}" stroke="#26323A" stroke-width="2"/>' + ''.join(f'<path d="M{wx - 2 + i * 4} {wy + wh} v-5" stroke="#26323A" stroke-width=".8"/>' for i in range(5))
        out += f'<path d="M{x} {y + 6 + wh + 10} H{x + w}" stroke="#D9CCB4" stroke-width="2"/>'
        if door:
            out += f'<path d="M{x + w / 2 - 9} {y + h} v-22 a9 9 0 0 1 18 0 v22 z" fill="#2F4F6B"/>'
        return out
    if a == 'azulejo':
        tile = ['#5B8FC9', '#3E8A9A', '#C98A3E'][k]
        _ids[0] += 1; pid = 'az%d' % _ids[0]
        out = (f'<defs><pattern id="{pid}" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#F4F1EA"/>'
               f'<path d="M4 0 L8 4 L4 8 L0 4 Z" fill="{tile}" opacity=".55"/></pattern></defs>'
               f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{pid})"/><rect x="{x - 3}" y="{y - 6}" width="{w + 6}" height="7" rx="2" fill="#C0583F"/>')
        for r in range(rows):
            for c in range(cols):
                wx = x + (c + .5) * w / cols - ww / 2; wy = y + 12 + r * (wh + 14)
                out += f'<rect x="{wx - 2}" y="{wy - 2}" width="{ww + 4}" height="{wh + 4}" fill="#fff"/><rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" fill="#3B4F6B" opacity=".55"/><path d="M{wx - 4} {wy + wh + 2} H{wx + ww + 4}" stroke="#26323A" stroke-width="1.6"/>'
        if door:
            out += f'<path d="M{x + w / 2 - 9} {y + h} v-20 a9 9 0 0 1 18 0 v20 z" fill="#3E6B4F"/>'
        return out
    if a == 'cycladic':
        # Cícladas: cubos encalados, puertas y contraventanas azules, alguna buganvilla
        blue = ['#1F6FB2', '#2A86C9', '#195C96'][k]
        out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#FBFAF6"/><rect x="{x - 2}" y="{y - 5}" width="{w + 4}" height="6" rx="3" fill="#F1EEE6"/>'
        out += f'<path d="M{x} {y + h} H{x + w}" stroke="#E4DED2" stroke-width="3"/>'
        for r in range(rows):
            for c in range(cols):
                wx = x + (c + .5) * w / cols - ww / 2; wy = y + 12 + r * (wh + 14)
                out += f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="2" fill="{blue}"/><path d="M{wx + ww / 2} {wy} V{wy + wh}" stroke="#FBFAF6" stroke-width="1.2"/>'
        if k == 1:
            out += f'<path d="M{x + w - 4} {y + 2} q10 10 4 26 q-8 -6 -10 -16 z" fill="#D63C83"/><circle cx="{x + w - 2}" cy="{y + 10}" r="4" fill="#E4589A"/><circle cx="{x + w + 3}" cy="{y + 20}" r="3" fill="#C23275"/>'
        if door:
            out += f'<path d="M{x + w / 2 - 8} {y + h} v-20 a8 8 0 0 1 16 0 v20 z" fill="{blue}"/>'
        return out
    if a == 'fachwerk':
        out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#F5EEDF"/><path d="M{x - 6} {y} L{x + w / 2} {y - w * .45} L{x + w + 6} {y} Z" fill="#B5473A"/>'
        beam = '#6B4429'
        out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{beam}" stroke-width="4"/>'
        for r in range(rows + 1):
            yy = y + 6 + r * (wh + 14)
            if yy < y + h:
                out += f'<path d="M{x} {yy} H{x + w}" stroke="{beam}" stroke-width="3"/>'
        out += ''.join(f'<path d="M{x + i * w / cols} {y} V{y + h}" stroke="{beam}" stroke-width="3"/>' for i in range(1, cols))
        out += f'<path d="M{x} {y + h} L{x + w / cols / 2} {y + h - 26} M{x + w} {y + h} L{x + w - w / cols / 2} {y + h - 26}" stroke="{beam}" stroke-width="3"/>'
        for r in range(rows):
            for c in range(cols):
                wx = x + (c + .5) * w / cols - ww / 2; wy = y + 12 + r * (wh + 14)
                out += f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh - 2}" fill="#3B4F6B" opacity=".6"/><rect x="{wx - 2}" y="{wy + wh - 3}" width="{ww + 4}" height="4" fill="#E2574C"/>'
        if door:
            out += f'<rect x="{x + w / 2 - 8}" y="{y + h - 24}" width="16" height="24" rx="3" fill="{beam}"/>'
        return out
    return _facade_it(x, y, w, h, col, shut, rows, cols, roof, door)


# ---------------------------------------------------------------- monumentos (sustituyen a la cúpula de Florencia)
def big_ben(x, y, s=1):
    o = ('<rect x="-90" y="-60" width="110" height="60" fill="#D9C08A"/>' + ''.join(f'<rect x="{-84 + i * 14}" y="-50" width="7" height="34" fill="#B39A62"/>' for i in range(8))
         + ''.join(f'<path d="M{-90 + i * 11} -60 l5 -8 l5 8" fill="#B39A62"/>' for i in range(10))
         + '<rect x="20" y="-150" width="40" height="150" fill="#D9C08A"/>' + ''.join(f'<rect x="{26 + i * 9}" y="-110" width="4" height="100" fill="#B39A62"/>' for i in range(4))
         + '<rect x="16" y="-176" width="48" height="30" fill="#CDB37A"/><circle cx="40" cy="-161" r="12" fill="#F4EBD0" stroke="#5E4A26" stroke-width="2"/>'
           '<path d="M40 -161 V-169 M40 -161 L46 -159" stroke="#26323A" stroke-width="2"/><path d="M18 -176 L40 -214 L62 -176 Z" fill="#3B5A4A"/><path d="M40 -214 V-226" stroke="#3B5A4A" stroke-width="3"/>')
    return g(o, x, y, s)


def eiffel(x, y, s=1):
    c = '#8A6B4A'
    o = (f'<path d="M-56 0 Q-30 -40 -14 -120 L-8 -190 L8 -190 L14 -120 Q30 -40 56 0 L38 0 Q20 -40 0 -54 Q-20 -40 -38 0 Z" fill="{c}"/>'
         f'<rect x="-30" y="-66" width="60" height="7" fill="{c}"/><rect x="-18" y="-128" width="36" height="6" fill="{c}"/>'
         f'<path d="M-6 -190 L0 -222 L6 -190 Z" fill="{c}"/><path d="M0 -222 V-234" stroke="{c}" stroke-width="2"/>'
         + ''.join(f'<path d="M{-30 + i * 10} -59 L{-20 + i * 10} -20" stroke="#B89A72" stroke-width="1.2"/>' for i in range(6)))
    return g(o, x, y, s)


def belem(x, y, s=1):
    o = ('<path d="M-70 0 L-70 -60 L70 -60 L70 0 Z" fill="#EDE3CF"/>' + ''.join(f'<path d="M{-66 + i * 12} -60 v-8 h6 v8" fill="#EDE3CF"/>' for i in range(12))
         + '<rect x="-30" y="-150" width="60" height="92" fill="#F3EBDA"/>' + ''.join(f'<path d="M{-28 + i * 10} -150 v-8 h5 v8" fill="#F3EBDA"/>' for i in range(6))
         + '<rect x="-16" y="-128" width="32" height="16" rx="3" fill="#7FA6DB" opacity=".5"/><path d="M-30 -112 H30" stroke="#D3C3A3" stroke-width="2"/>'
         '<path d="M-10 -96 v-16 a10 10 0 0 1 20 0 v16 z" fill="#C9B793"/><circle cx="-38" cy="-70" r="7" fill="#F3EBDA"/><path d="M-45 -70 L-38 -84 L-31 -70" fill="#C9B793"/>'
         '<circle cx="38" cy="-70" r="7" fill="#F3EBDA"/><path d="M31 -70 L38 -84 L45 -70" fill="#C9B793"/>'
         '<path d="M-90 0 Q0 16 90 0 V12 H-90 Z" fill="#7FC3E8"/>')
    return g(o, x, y, s)


def brandenburg(x, y, s=1):
    o = '<rect x="-80" y="-104" width="160" height="22" fill="#E9DDC2"/><rect x="-86" y="-110" width="172" height="8" fill="#D9CBAA"/>'
    o += ''.join(f'<rect x="{-76 + i * 30}" y="-82" width="12" height="82" fill="#EFE5CE"/>' for i in range(6))
    o += '<rect x="-24" y="-130" width="48" height="20" fill="#E9DDC2"/>'
    o += '<g fill="#5E8C7A"><rect x="-16" y="-142" width="32" height="10" rx="3"/><path d="M-12 -142 l-4 -12 l6 6 z M-4 -142 l-2 -14 l6 8 z M4 -142 l2 -14 l4 8 z M12 -142 l4 -12 l2 8 z"/><path d="M0 -150 v-16 M-6 -162 h12" stroke="#5E8C7A" stroke-width="3"/></g>'
    return g(o, x, y, s)


def parthenon(x, y, s=1):
    # Acrópolis: la roca y el Partenón (frontón, columnas dóricas)
    o = '<path d="M-110 0 Q-96 -30 -60 -36 L60 -38 Q98 -32 112 0 Z" fill="#C9B48E"/><path d="M-60 -36 L60 -38" stroke="#B39C74" stroke-width="2"/>'
    o += '<rect x="-64" y="-46" width="128" height="9" fill="#EFE6D2"/><rect x="-60" y="-50" width="120" height="5" fill="#E2D6BC"/>'
    o += ''.join(f'<rect x="{-58 + i * 14.5}" y="-104" width="8" height="54" fill="#F3EBD9"/><path d="M{-58 + i * 14.5} -104 h8 M{-58 + i * 14.5} -52 h8" stroke="#D8CCB0" stroke-width="2"/>' for i in range(9))
    o += '<rect x="-64" y="-114" width="128" height="10" fill="#E9DFC8"/><path d="M-66 -114 L0 -136 L66 -114 Z" fill="#F0E7D3" stroke="#D8CCB0" stroke-width="2"/>'
    o += '<path d="M-64 -109 H64" stroke="#D8CCB0" stroke-width="1.2"/>'
    return g(o, x, y, s)


_dome_it = dome


def dome(x, y, s=1):
    lm = LOC.get('landmark')
    f = {'bigben': big_ben, 'eiffel': eiffel, 'belem': belem, 'tor': brandenburg, 'parthenon': parthenon}.get(lm)
    return f(x, y, s) if f else _dome_it(x, y, s)


# ---------------------------------------------------------------- dulces, autobuses, buzones
_cornetto_it = cornetto


def croissant(x, y, s=1):
    return g('<path d="M-20 0 Q-22 -14 -8 -16 Q0 -20 8 -16 Q22 -14 20 0 Q12 -6 0 -6 Q-12 -6 -20 0 Z" fill="#D9913A"/>'
             '<path d="M-10 -6 Q-8 -14 -4 -16 M0 -6 V-18 M10 -6 Q8 -14 4 -16" stroke="#A86420" stroke-width="2" fill="none"/>', x, y, s)


def nata(x, y, s=1):
    return g('<path d="M-16 -2 L-13 -12 L13 -12 L16 -2 Q0 4 -16 -2 Z" fill="#D9A15A"/><ellipse cx="0" cy="-12" rx="13" ry="4" fill="#F6C94A"/>'
             '<circle cx="-4" cy="-12" r="2.2" fill="#7A4A1E"/><circle cx="5" cy="-13" r="1.6" fill="#7A4A1E"/><circle cx="1" cy="-10.5" r="1.2" fill="#7A4A1E"/>', x, y, s)


def pretzel(x, y, s=1):
    return g('<path d="M0 -4 C-26 -30 -26 2 -6 -8 C8 -16 18 -24 10 -30 C2 -36 -8 -24 0 -14 C8 -24 -2 -36 -10 -30 C-18 -24 -8 -16 6 -8 C26 2 26 -30 0 -4" '
             'stroke="#9C5A26" stroke-width="5.5" fill="none" stroke-linecap="round"/><circle cx="-12" cy="-14" r="1" fill="#fff"/><circle cx="12" cy="-16" r="1" fill="#fff"/><circle cx="2" cy="-22" r="1" fill="#fff"/>', x, y, s)


def scone(x, y, s=1):
    return g('<path d="M-14 0 Q-16 -12 0 -14 Q16 -12 14 0 Z" fill="#E3B26E"/><rect x="-14" y="-8" width="28" height="3" fill="#F7EBD0"/><ellipse cx="0" cy="-14" rx="10" ry="3" fill="#C0392B"/>', x, y, s)


def koulouri(x, y, s=1):
    # Κουλούρι Θεσσαλονίκης: rosca de sésamo
    seeds = ''.join(f'<ellipse cx="{13 * math.cos(a):.1f}" cy="{-11 + 9 * math.sin(a):.1f}" rx="1.4" ry=".8" fill="#FFF3D6" transform="rotate({int(a * 57)} {13 * math.cos(a):.1f} {-11 + 9 * math.sin(a):.1f})"/>' for a in [i * .55 for i in range(12)])
    return g('<ellipse cx="0" cy="-11" rx="13" ry="9" fill="none" stroke="#C98536" stroke-width="9"/>' + seeds, x, y, s)


def cornetto(x, y, s=1):
    f = {'croissant': croissant, 'nata': nata, 'pretzel': pretzel, 'scone': scone, 'koulouri': koulouri}.get(LOC.get('pastry'))
    return f(x, y, s) if f else _cornetto_it(x, y, s)


_bus_it = bus


def bus(x, y, s=1, c='#FFB72B'):
    if LOC.get('bus') == 'double':
        o = ('<rect x="-46" y="-70" width="92" height="64" rx="8" fill="#D2322D"/>'
             + ''.join(f'<rect x="{-40 + i * 22}" y="-64" width="18" height="12" rx="2" fill="#BFE4F7"/><rect x="{-40 + i * 22}" y="-36" width="18" height="12" rx="2" fill="#BFE4F7"/>' for i in range(4))
             + '<rect x="-46" y="-46" width="92" height="4" fill="#F4E04D"/><circle cx="-26" cy="-6" r="7" fill="#26323A"/><circle cx="26" cy="-6" r="7" fill="#26323A"/>'
               '<circle cx="-26" cy="-6" r="3" fill="#C9CFD6"/><circle cx="26" cy="-6" r="3" fill="#C9CFD6"/>')
        return g(o, x, y, s)
    if LOC.get('bus') == 'tram':
        return tram(x, y, s)
    return _bus_it(x, y, s, c)


def tram(x, y, s=1):
    o = ('<path d="M-30 -86 L30 -86" stroke="#26323A" stroke-width="2"/><path d="M0 -86 L-8 -64" stroke="#26323A" stroke-width="2"/>'
         '<rect x="-48" y="-64" width="96" height="56" rx="8" fill="#F2C230"/><rect x="-48" y="-30" width="96" height="22" fill="#F4F1EA"/>'
         + ''.join(f'<rect x="{-42 + i * 21}" y="-58" width="16" height="20" rx="2" fill="#BFE4F7"/>' for i in range(4))
         + '<rect x="-48" y="-68" width="96" height="6" rx="3" fill="#D9A520"/><circle cx="-26" cy="-6" r="6" fill="#26323A"/><circle cx="26" cy="-6" r="6" fill="#26323A"/>'
         + txt(0, -16, '28', 10, '#26323A', weight=900))
    return g(o, x, y, s)


_mailbox_it = mailbox


def mailbox(x, y, s=1):
    k = LOC.get('mail')
    if k == 'pillar':
        return g('<rect x="-14" y="-62" width="28" height="62" rx="3" fill="#C8102E"/><path d="M-16 -62 a16 10 0 0 1 32 0 z" fill="#A50D26"/><rect x="-9" y="-48" width="18" height="3" fill="#26323A"/><rect x="-16" y="-4" width="32" height="4" fill="#26323A"/>'
                 + txt(0, -30, 'GR', 8, '#F4E04D', weight=900), x, y, s)
    if k == 'yellow':
        return g('<rect x="-3" y="-40" width="6" height="40" fill="#5B6676"/><rect x="-18" y="-68" width="36" height="30" rx="5" fill="#F7C531"/><rect x="-10" y="-60" width="20" height="4" rx="2" fill="#26323A"/>'
                 '<circle cy="-48" r="5" fill="none" stroke="#26323A" stroke-width="1.6"/>', x, y, s)
    if k == 'red':
        return g('<rect x="-12" y="-60" width="24" height="60" rx="4" fill="#D9352B"/><rect x="-8" y="-48" width="16" height="3" fill="#26323A"/><rect x="-14" y="-64" width="28" height="6" rx="3" fill="#B52A22"/>', x, y, s)
    return _mailbox_it(x, y, s)


_pinocchio_it = pinocchio


def pinocchio(x, y, s=1, begin=0):
    if not LOC.get('tale'):
        return _pinocchio_it(x, y, s, begin)
    # Caperucita Roja (cuento popular europeo: Perrault, los Grimm)
    o = person(0, 0, '#E2574C', 2, '#B58A3C', pose='hold', legs='#3F6FA8', hs='long', skirt=True, begin=begin)
    o += '<g transform="scale(1.15)"><path d="M-10 -50 Q-12 -70 0 -72 Q12 -70 10 -50 L7 -54 Q8 -66 0 -66 Q-8 -66 -7 -54 Z" fill="#C0392B"/><path d="M-9 -52 L-14 -28 L14 -28 L9 -52 Z" fill="#C0392B" opacity=".85"/></g>'
    o += '<g transform="translate(18 -26)"><path d="M-10 0 L10 0 L8 10 L-8 10 Z" fill="#C8955E"/><path d="M-8 0 Q0 -12 8 0" stroke="#8A5A3B" stroke-width="2" fill="none"/><circle cx="-3" cy="-1" r="3" fill="#E2574C"/><circle cx="3" cy="-2" r="3" fill="#FFC94A"/></g>'
    return g(o, x, y, s)


# ---------------------------------------------------------------- piezas nuevas
def flag_rect(x, y, cols, w=36, h=24, horiz=False, pole=True):
    n = len(cols)
    o = ''.join(f'<rect x="{x + (0 if horiz else i * w / n)}" y="{y + (i * h / n if horiz else 0)}" width="{w if horiz else w / n}" height="{h / n if horiz else h}" fill="{c}"/>' for i, c in enumerate(cols))
    return (f'<path d="M{x} {y} V{y + 80}" stroke="#5B6676" stroke-width="3"/>' if pole else '') + o


def union_jack(x, y, w=40, h=24):
    return (f'<g transform="translate({x} {y})"><rect width="{w}" height="{h}" fill="#1D3E8A"/><path d="M0 0 L{w} {h} M{w} 0 L0 {h}" stroke="#fff" stroke-width="5"/>'
            f'<path d="M0 0 L{w} {h} M{w} 0 L0 {h}" stroke="#C8102E" stroke-width="2"/><path d="M{w / 2} 0 V{h} M0 {h / 2} H{w}" stroke="#fff" stroke-width="8"/>'
            f'<path d="M{w / 2} 0 V{h} M0 {h / 2} H{w}" stroke="#C8102E" stroke-width="4.5"/></g>')


def country_flag(x, y, w=40, h=26):
    f = LOC.get('flag', 'it')
    if f == 'uk':
        return union_jack(x, y, w, h)
    if f == 'gr':
        # nueve franjas azules y blancas con la cruz blanca en el cantón
        o = ''.join(f'<rect x="{x}" y="{y + i * h / 9:.2f}" width="{w}" height="{h / 9 + .2:.2f}" fill="{"#0D5EAF" if i % 2 == 0 else "#fff"}"/>' for i in range(9))
        cw, ch = w * .4, h * 5 / 9
        o += f'<rect x="{x}" y="{y}" width="{cw:.1f}" height="{ch:.1f}" fill="#0D5EAF"/><rect x="{x + cw / 2 - h / 18:.1f}" y="{y}" width="{h / 9:.1f}" height="{ch:.1f}" fill="#fff"/><rect x="{x}" y="{y + ch / 2 - h / 18:.1f}" width="{cw:.1f}" height="{h / 9:.1f}" fill="#fff"/>'
        return o
    cols = {'it': (['#2F8F4E', '#fff', '#D9352B'], False), 'fr': (['#1F4FA0', '#fff', '#D9352B'], False), 'de': (['#26323A', '#D9352B', '#F2C230'], True),
            'pt': (['#2F7A3E', '#2F7A3E', '#D9352B', '#D9352B', '#D9352B'], False)}[f]
    o = flag_rect(x, y, cols[0], w, h, cols[1], pole=False)
    if f == 'pt':
        o += f'<circle cx="{x + w * .4}" cy="{y + h / 2}" r="{h * .24}" fill="#F2C230"/><circle cx="{x + w * .4}" cy="{y + h / 2}" r="{h * .12}" fill="#D9352B"/>'
    return o


def bunting(x0, x1, y, cols=None, sag=24):
    cols = cols or LOC.get('bunting') or ['#E2574C', '#FFC94A', '#5BAA6A', '#3F6FA8', '#C77DBA']
    n = int((x1 - x0) / 20)
    o = f'<path d="M{x0} {y} Q{(x0 + x1) / 2} {y + sag * 2} {x1} {y}" stroke="#5B6676" stroke-width="1.5" fill="none"/>'
    for i in range(n):
        t = (i + .5) / n; px = x0 + (x1 - x0) * t; py = y + sag * 4 * t * (1 - t)
        o += f'<path d="M{px - 7} {py} L{px + 7} {py} L{px} {py + 14} Z" fill="{cols[i % len(cols)]}"/>'
    return o


def firework(x, y, r=26, c='#FFC94A', begin=0):
    rays = ''.join(f'<path d="M0 0 L{r * math.cos(a * math.pi / 6):.1f} {r * math.sin(a * math.pi / 6):.1f}" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>' for a in range(12))
    return (f'<g transform="translate({x} {y})"><g>{rays}<animateTransform attributeName="transform" type="scale" values=".2;1;1.1" dur="2.4s" begin="{begin}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;1;0" dur="2.4s" begin="{begin}s" repeatCount="indefinite"/></g></g>')


def cake(x, y, s=1):
    return g('<rect x="-26" y="-26" width="52" height="26" rx="4" fill="#F2B8C6"/><rect x="-26" y="-30" width="52" height="8" rx="4" fill="#fff"/>'
             '<rect x="-14" y="-44" width="4" height="14" fill="#7FA6DB"/><rect x="-2" y="-46" width="4" height="16" fill="#FFC94A"/><rect x="10" y="-44" width="4" height="14" fill="#5BAA6A"/>'
             '<circle cx="-12" cy="-48" r="2.5" fill="#FFB25B"/><circle cx="0" cy="-50" r="2.5" fill="#FFB25B"/><circle cx="12" cy="-48" r="2.5" fill="#FFB25B"/>', x, y, s)


def gift(x, y, s=1, c='#5BAA6A'):
    return g(f'<rect x="-14" y="-24" width="28" height="24" fill="{c}"/><rect x="-16" y="-30" width="32" height="8" fill="{c}"/><rect x="-3" y="-30" width="6" height="30" fill="#FFC94A"/>'
             '<path d="M0 -30 q-12 -12 -12 -2 z M0 -30 q12 -12 12 -2 z" fill="#FFC94A"/>', x, y, s)


def lantern(x, y, c='#E2574C'):
    return f'<g transform="translate({x} {y})"><path d="M0 -14 V-4" stroke="#5B6676"/><ellipse cy="6" rx="9" ry="11" fill="{c}"/><rect x="-5" y="-6" width="10" height="3" fill="#5B6676"/><ellipse cy="6" rx="4" ry="9" fill="#fff" opacity=".25"/></g>'


def turbine(x, y, s=1, begin=0):
    blades = '<path d="M0 0 L-3 -46 L3 -46 Z" fill="#fff"/><path d="M0 0 L-3 -46 L3 -46 Z" fill="#fff" transform="rotate(120)"/><path d="M0 0 L-3 -46 L3 -46 Z" fill="#fff" transform="rotate(240)"/>'
    return g(f'<path d="M-4 0 L-2 -110 L2 -110 L4 0 Z" fill="#E9EEF2"/><g transform="translate(0 -110)"><g>{blades}<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="6s" begin="{begin}s" repeatCount="indefinite"/></g><circle r="4" fill="#C9CFD6"/></g>', x, y, s)


def solar(x, y, s=1):
    return g('<path d="M-30 0 L-20 -30 L30 -30 L20 0 Z" fill="#2F4F86"/>' + ''.join(f'<path d="M{-25 + i * 10} 0 L{-15 + i * 10} -30" stroke="#7FA6DB" stroke-width="1"/>' for i in range(5))
             + '<path d="M-25 -15 H25" stroke="#7FA6DB" stroke-width="1"/><rect x="-2" y="0" width="4" height="12" fill="#5B6676"/>', x, y, s)


def bins(x, y, s=1):
    o = ''
    for i, (c, t) in enumerate((('#3F6FA8', 'P'), ('#FFC94A', 'V'), ('#5BAA6A', 'O'))):
        o += f'<g transform="translate({i * 30} 0)"><rect x="-12" y="-36" width="24" height="36" rx="3" fill="{c}"/><rect x="-14" y="-40" width="28" height="6" rx="2" fill="{c}"/><path d="M-4 -22 l4 -6 l4 6 m-2 6 l-4 0" stroke="#fff" stroke-width="2" fill="none"/></g>'
    return g(o, x, y, s)


def bicycle(x, y, s=1, c='#E2574C', face=1):
    b = (f'<circle cx="-18" cy="-12" r="11" fill="none" stroke="#26323A" stroke-width="2.5"/><circle cx="18" cy="-12" r="11" fill="none" stroke="#26323A" stroke-width="2.5"/>'
         f'<path d="M-18 -12 L-4 -12 L8 -30 L-8 -30 Z M8 -30 L18 -12 M-8 -30 L-10 -36 M8 -30 L10 -38 h6" stroke="{c}" stroke-width="3" fill="none" stroke-linejoin="round"/><rect x="-15" y="-38" width="10" height="3" rx="1.5" fill="#26323A"/>')
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{b}</g>'


def gear(x, y, r=18, c='#9AA6B8', dur=8, rev=False):
    teeth = ''.join(f'<rect x="-3.5" y="{-r - 6}" width="7" height="9" fill="{c}" transform="rotate({a})"/>' for a in range(0, 360, 40))
    return (f'<g transform="translate({x} {y})"><g>{teeth}<circle r="{r}" fill="{c}"/><circle r="{r * .38}" fill="#fff"/>'
            f'<animateTransform attributeName="transform" type="rotate" from="0" to="{-360 if rev else 360}" dur="{dur}s" repeatCount="indefinite"/></g></g>')


def robot(x, y, s=1):
    return g('<rect x="-18" y="-50" width="36" height="34" rx="6" fill="#C9D3DE"/><rect x="-14" y="-82" width="28" height="26" rx="6" fill="#C9D3DE"/><circle cx="-6" cy="-70" r="3.5" fill="#3F6FA8"/><circle cx="6" cy="-70" r="3.5" fill="#3F6FA8"/>'
             '<path d="M0 -82 V-92" stroke="#5B6676" stroke-width="2"/><circle cx="0" cy="-94" r="3" fill="#E2574C"><animate attributeName="opacity" values="1;.2;1" dur="1.4s" repeatCount="indefinite"/></circle>'
             '<rect x="-8" y="-62" width="16" height="3" rx="1.5" fill="#5B6676"/><rect x="-14" y="-16" width="8" height="16" fill="#9AA6B8"/><rect x="6" y="-16" width="8" height="16" fill="#9AA6B8"/>'
             '<path d="M-18 -44 L-28 -30 M18 -44 L28 -30" stroke="#9AA6B8" stroke-width="5" stroke-linecap="round"/><rect x="-10" y="-44" width="20" height="10" rx="2" fill="#5BAA6A"/>', x, y, s)


def bulb(x, y, s=1):
    return g('<path d="M-12 -30 a14 14 0 1 1 24 0 q-4 6 -5 12 h-14 q-1 -6 -5 -12 z" fill="#FFE08A"/><rect x="-7" y="-18" width="14" height="8" rx="2" fill="#9AA6B8"/>'
             + ''.join(f'<path d="M{18 * math.cos(a):.1f} {-40 + 18 * math.sin(a):.1f} l{6 * math.cos(a):.1f} {6 * math.sin(a):.1f}" stroke="#FFC94A" stroke-width="2.5" stroke-linecap="round"/>' for a in (-2.6, -2.0, -1.57, -1.1, -.5)), x, y, s)


def wrench(x, y, s=1, rot=30):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-3" y="-22" width="6" height="34" rx="3" fill="#9AA6B8"/><path d="M-9 -28 a9 9 0 1 1 18 0 l-4 0 l0 -6 l-10 0 l0 6 z" fill="#9AA6B8"/></g>'


def popcorn(x, y, s=1):
    return g('<path d="M-12 0 L-15 -26 L15 -26 L12 0 Z" fill="#fff"/>' + ''.join(f'<path d="M{-12 + i * 6} 0 L{-15 + i * 7.5} -26" stroke="#E2574C" stroke-width="3"/>' for i in range(0, 5, 2))
             + ''.join(f'<circle cx="{dx}" cy="{dy}" r="5" fill="#FFF3C4"/>' for dx, dy in ((-10, -28), (-2, -32), (8, -29), (3, -36), (-7, -35))), x, y, s)


def film_reel(x, y, r=20):
    return f'<g transform="translate({x} {y})"><g><circle r="{r}" fill="#3B4F6B"/>' + ''.join(f'<circle cx="{r * .55 * math.cos(a * 1.2566):.1f}" cy="{r * .55 * math.sin(a * 1.2566):.1f}" r="{r * .2}" fill="#C9D3DE"/>' for a in range(5)) + f'<circle r="{r * .15}" fill="#C9D3DE"/><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="10s" repeatCount="indefinite"/></g></g>'


def screen(x, y, w=150, h=90):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#F4F1EA" stroke="#26323A" stroke-width="4"/>'
            f'<path d="M{x + 4} {y + h - 4} L{x + w * .3} {y + h * .45} L{x + w * .5} {y + h * .7} L{x + w * .7} {y + h * .35} L{x + w - 4} {y + h - 4} Z" fill="#9ED3F0"/><circle cx="{x + w * .8}" cy="{y + h * .25}" r="8" fill="#FFC94A"/>')


def pot(x, y, s=1):
    steam = ''.join(f'<path d="M{dx} -40 q4 -6 0 -12 q-4 -6 0 -12" stroke="#C9CFD6" stroke-width="2" fill="none"><animate attributeName="opacity" values="0;1;0" dur="2.5s" begin="{b}s" repeatCount="indefinite"/></path>' for dx, b in ((-8, 0), (2, .8), (12, 1.5)))
    return g('<path d="M-26 -36 L-22 0 L22 0 L26 -36 Z" fill="#9AA6B8"/><rect x="-30" y="-40" width="60" height="6" rx="3" fill="#7A8699"/><rect x="-38" y="-32" width="10" height="4" rx="2" fill="#26323A"/><rect x="28" y="-32" width="10" height="4" rx="2" fill="#26323A"/>' + steam, x, y, s)


def stove(x, y, s=1):
    return g('<rect x="-50" y="-60" width="100" height="60" fill="#E9EEF2"/><rect x="-50" y="-64" width="100" height="6" fill="#C9CFD6"/><rect x="-36" y="-44" width="72" height="34" rx="4" fill="#3B4F6B" opacity=".75"/>'
             '<circle cx="-30" cy="-54" r="3" fill="#5B6676"/><circle cx="-18" cy="-54" r="3" fill="#5B6676"/><circle cx="18" cy="-54" r="3" fill="#5B6676"/><circle cx="30" cy="-54" r="3" fill="#5B6676"/>', x, y, s)


def veg(x, y, s=1):
    return g('<path d="M-22 -2 L-10 -26 L-6 -24 L-16 0 Z" fill="#FF8A3D"/><path d="M-10 -26 l-4 -8 M-10 -26 l2 -9 M-10 -26 l6 -6" stroke="#5BAA6A" stroke-width="2"/>'
             '<circle cx="6" cy="-10" r="10" fill="#E2574C"/><path d="M6 -20 l-3 -4 M6 -20 l4 -3" stroke="#3E8A52" stroke-width="2"/><ellipse cx="22" cy="-6" rx="7" ry="6" fill="#F3E2C4"/><path d="M22 -12 v-6" stroke="#5BAA6A" stroke-width="2"/>', x, y, s)


def recipe_card(x, y, title='RICETTA', s=1, rot=-5):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-40" y="-54" width="80" height="54" fill="#fff" stroke="#E0C97A"/>' + txt(0, -38, title, 10, '#B03A4A', weight=900)
            + ''.join(f'<path d="M-30 {-28 + i * 8} H{24 - (i % 2) * 14}" stroke="#C9CFD6" stroke-width="2"/>' for i in range(4)) + '</g>')


def comic_panel(x, y, w, h, inner, c='#fff'):
    return f'<g transform="translate({x} {y})"><rect width="{w}" height="{h}" fill="{c}" stroke="#26323A" stroke-width="3"/>{inner}</g>'


def wall_segment(x, y, s=1):
    cols = ['#E2574C', '#3F6FA8', '#FFC94A', '#5BAA6A', '#C77DBA']
    o = '<rect x="-60" y="-110" width="120" height="110" fill="#C9C6BE"/><rect x="-64" y="-118" width="128" height="12" rx="6" fill="#B5B2AA"/>'
    o += ''.join(f'<path d="M{-60 + i * 30} -106 V0" stroke="#AEABA3" stroke-width="2"/>' for i in range(1, 4))
    o += '<path d="M-50 -40 q14 -30 28 0 t28 0" stroke="#E2574C" stroke-width="6" fill="none" stroke-linecap="round"/><circle cx="20" cy="-70" r="14" fill="#FFC94A"/><path d="M34 -40 l14 -20 l8 22" stroke="#3F6FA8" stroke-width="6" fill="none"/>'
    o += '<path d="M-44 -86 h30" stroke="#5BAA6A" stroke-width="6" stroke-linecap="round"/><path d="M-30 -20 l40 0" stroke="#C77DBA" stroke-width="5" stroke-linecap="round"/>'
    return g(o, x, y, s)


def mountains(y0=320, snow=True):
    o = f'<path d="M-20 {y0} L80 {y0 - 170} L150 {y0 - 80} L220 {y0 - 210} L300 {y0 - 100} L360 {y0 - 160} L430 {y0} Z" fill="#9AA9C2"/>'
    if snow:
        o += f'<path d="M80 {y0 - 170} L60 {y0 - 135} L74 {y0 - 140} L84 {y0 - 128} L100 {y0 - 140} Z M220 {y0 - 210} L196 {y0 - 168} L212 {y0 - 172} L224 {y0 - 160} L242 {y0 - 176} Z M360 {y0 - 160} L344 {y0 - 132} L358 {y0 - 136} L374 {y0 - 130} Z" fill="#fff"/>'
    o += f'<path d="M-20 {y0} Q100 {y0 - 60} 200 {y0 - 20} T430 {y0 - 30} V{y0 + 10} H-20 Z" fill="#8DBF6E"/>'
    return o


def chalet(x, y, s=1):
    return g('<rect x="-34" y="-40" width="68" height="40" fill="#B97A4E"/><path d="M-44 -36 L0 -66 L44 -36 Z" fill="#7A4A2E"/><rect x="-24" y="-30" width="14" height="12" fill="#BFE4F7"/><rect x="10" y="-30" width="14" height="12" fill="#BFE4F7"/>'
             '<rect x="-24" y="-18" width="14" height="4" fill="#E2574C"/><rect x="10" y="-18" width="14" height="4" fill="#E2574C"/><rect x="-6" y="-22" width="12" height="22" fill="#5E3E28"/>', x, y, s)


def cow(x, y, s=1, face=1):
    b = ('<ellipse cx="0" cy="-20" rx="24" ry="14" fill="#fff"/><circle cx="-8" cy="-24" r="6" fill="#26323A"/><circle cx="10" cy="-16" r="5" fill="#26323A"/>'
         '<ellipse cx="26" cy="-28" rx="9" ry="8" fill="#fff"/><ellipse cx="31" cy="-24" rx="5" ry="4" fill="#F2B8C6"/><path d="M22 -36 l-3 -5 M30 -36 l3 -5" stroke="#C9A24A" stroke-width="2"/>'
         '<rect x="-18" y="-8" width="5" height="10" fill="#fff"/><rect x="12" y="-8" width="5" height="10" fill="#fff"/><circle cx="24" cy="-12" r="3.5" fill="#C9A24A"/>')
    return f'<g transform="translate({x} {y}) scale({s * face} {s})">{b}</g>'


def guitarra_pt(x, y, s=1, rot=-20):
    """Guitarra portuguesa (fado): caja en forma de pera y clavijero en abanico."""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0 -40 C-22 -40 -24 -6 -18 6 C-12 20 12 20 18 6 C24 -6 22 -40 0 -40 Z" fill="#C8955E"/>'
            '<circle cy="-14" r="6" fill="#5E3E28"/><rect x="-2.5" y="-88" width="5" height="50" fill="#5E3E28"/><path d="M-10 -100 L0 -86 L10 -100 Q0 -106 -10 -100 Z" fill="#C9A24A"/></g>')


def carnation(x, y, s=1, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0 0 Q2 -20 0 -40" stroke="#3E8A52" stroke-width="2.5" fill="none"/>'
            '<path d="M-8 -40 Q-10 -50 -4 -52 Q0 -58 4 -52 Q10 -50 8 -40 Q4 -36 0 -38 Q-4 -36 -8 -40 Z" fill="#D9352B"/><path d="M-4 -38 L0 -44 L4 -38" fill="#3E8A52"/></g>')


def beetle(x, y, s=1):
    legs = ''.join(f'<path d="M{dx} -14 l{-14 if dx < 0 else 14} {dy}" stroke="#3A2A1E" stroke-width="2.5"/>' for dx, dy in ((-10, -8), (-12, 2), (-10, 10), (10, -8), (12, 2), (10, 10)))
    return g(f'<g>{legs}{anim_rot(-4, 4, 0, -14, 1.2)}</g><ellipse cy="-14" rx="16" ry="22" fill="#5B4A2E"/><path d="M0 -36 V8" stroke="#3A2A1E" stroke-width="1.5"/>'
             '<circle cy="-38" r="8" fill="#3A2A1E"/><path d="M-4 -44 q-6 -10 -12 -8 M4 -44 q6 -10 12 -8" stroke="#3A2A1E" stroke-width="1.6" fill="none"/>', x, y, s)


def sachertorte(x, y, s=1):
    return g('<path d="M-22 0 L-22 -16 L22 -16 L22 0 Z" fill="#4A2A1A"/><path d="M-22 -16 L0 -26 L22 -16 Z" fill="#5E3420"/><rect x="-22" y="-9" width="44" height="2.5" fill="#E8A040"/>'
             '<ellipse cx="14" cy="-4" rx="9" ry="5" fill="#fff"/><ellipse cx="0" cy="2" rx="28" ry="4" fill="#fff" opacity=".7"/>', x, y, s)


def chandelier(x, y, s=1):
    return g('<path d="M0 0 V24" stroke="#C9A24A" stroke-width="2"/><path d="M-30 30 Q0 50 30 30" stroke="#C9A24A" stroke-width="3" fill="none"/>'
             + ''.join(f'<rect x="{dx - 2}" y="{dy - 12}" width="4" height="10" fill="#FFF3C4"/><circle cx="{dx}" cy="{dy - 14}" r="2.5" fill="#FFC94A"/>' for dx, dy in ((-30, 30), (-15, 38), (0, 40), (15, 38), (30, 30))), x, y, s)


def tophat_person(x, y, shirt='#26323A', skin=0, face=1, s=1, hat='top', beard=False, glasses=False, hair='#3A2A1E'):
    o = person(x, y, shirt, skin, hair, s=s, face=face, beard=beard, glasses=glasses, legs='#26323A')
    k = s * 1.15
    hats = {'top': '<rect x="-8" y="-82" width="16" height="16" fill="#26323A"/><rect x="-12" y="-68" width="24" height="3" rx="1.5" fill="#26323A"/>',
            'fedora': '<path d="M-9 -66 Q-8 -78 0 -78 Q8 -78 9 -66 Z" fill="#3A3A3A"/><ellipse cy="-66" rx="13" ry="2.6" fill="#3A3A3A"/><rect x="-9" y="-69" width="18" height="2" fill="#7A6A4A"/>',
            'wig': '<path d="M-10 -58 Q-12 -76 0 -78 Q12 -76 10 -58 Q12 -50 8 -46 L8 -58 Q0 -64 -8 -58 L-8 -46 Q-12 -50 -10 -58 Z" fill="#E9E4DA"/>',
            'eyepatch': '<path d="M-9 -60 L9 -56" stroke="#26323A" stroke-width="1.2"/><ellipse cx="3.6" cy="-57.4" rx="3.2" ry="2.6" fill="#26323A"/>',
            'ruff': '<path d="M-10 -48 Q0 -40 10 -48 Q12 -44 0 -42 Q-12 -44 -10 -48 Z" fill="#fff" stroke="#C9CFD6"/>'}
    return o + f'<g transform="translate({x} {y}) scale({k * face} {k})">{hats.get(hat, "")}</g>'


# ---------------------------------------------------------------- plantillas nuevas (lado libre a la izquierda)
def t_festival():
    o = env_night('#2C2F6B', '#6A4E9A') + '<path d="M0 420 Q200 390 400 420 V700 H0 Z" fill="#3A3F7A"/>'
    o += firework(90, 110, 30, '#FFC94A') + firework(300, 80, 26, '#E2574C', .8) + firework(200, 170, 22, '#7FD0E8', 1.6)
    bg, o = o, ''
    o += bunting(10, 190, 250) + bunting(10, 190, 470)
    o += ''.join(lantern(x, y, c) for x, y, c in ((40, 296, '#E2574C'), (100, 312, '#FFC94A'), (160, 300, '#5BAA6A')))
    o += person(50, 440, '#E2574C', 1, pose='wave', hs='curly') + person(110, 440, '#FFC94A', 2, '#6B3E1E', pose='wave', hs='long', skirt=True, begin=.4, face=-1)
    o += bubble(80, 360, 'Buona festa!', '#fff', side=0, size=11)
    o += cake(60, 620, 1.1) + gift(120, 620) + gift(150, 640, .8, '#E2574C') + country_flag(30, 520)
    o += person(140, 690, '#3F6FA8', 3, '#1E1A18', pose='hold', s=.9, face=-1) + bubble(90, 680, 'Auguri!', '#FFF3C4', side=0, size=11)
    return done(bg, o, 'carpet', '#4A4A8A', True)


def t_eco():
    o = sky('#CDEBFA', '#EEF8EA', 330) + '<path d="M0 260 Q120 220 220 250 T400 240 V700 H0 Z" fill="#AED596"/>'
    o += turbine(60, 270, .9) + turbine(140, 250, .7, 1) + turbine(330, 260, .8, 2) + sun(300, 70, 22)
    bg, o = o, ''
    o += solar(60, 360, 1.1) + solar(130, 380, .9)
    o += bicycle(60, 480, 1.1, '#5BAA6A') + person(110, 480, '#5BAA6A', 1, pose='point', hs='curly', face=-1)
    o += bubble(90, 400, 'Ricicliamo!', '#fff', side=0, size=11)
    o += bins(40, 620, 1) + tree(150, 640, .8, fruit='#E2574C') + bubble(80, 560, 'Meno plastica!', '#E8F4EC', side=0, size=11)
    o += plant(40, 700)
    return done(bg, o, 'trail', '#E2F1DA')


def t_workshop():
    o = '<rect width="400" height="700" fill="#E9EEF3"/><rect y="330" width="400" height="370" fill="#CFD6DF"/>'
    o += ''.join(f'<path d="M0 {y} H400" stroke="#BFC8D3" stroke-width="2"/>' for y in range(360, 700, 40))
    o += whiteboard(52, 90, 120, 80, ('1. ...', '2. ...', '3. ...'))
    bg, o = o, ''
    o += gear(50, 260, 20, '#9AA6B8', 8) + gear(84, 280, 13, '#7FA6DB', 6, True) + bulb(150, 270, 1)
    o += desk(80, 450) + laptop(70, 404, .8) + wrench(120, 400, 1)
    o += robot(40, 600, 1) + person(110, 600, '#3F6FA8', 1, pose='point', face=-1, glasses=True)
    o += bubble(90, 500, 'Come funziona?', '#fff', side=0, size=11) + bubble(90, 680, 'Si accende così', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'hall', '#E2E7ED')


def t_uni():
    o = sky('#D7ECFA', '#F2F4EE', 330) + '<rect y="300" width="400" height="400" fill="#C9E0AE"/>'
    o += '<rect x="20" y="150" width="200" height="150" fill="#E9DDC2"/><path d="M10 150 L120 90 L230 150 Z" fill="#D9CBAA"/>' + ''.join(column(x, 300, 120, .8) for x in (40, 80, 120, 160, 200))
    o += '<path d="M120 400 Q160 500 120 700" stroke="#E2C79A" stroke-width="40" fill="none" opacity=".5"/>'
    bg, o = o, ''
    o += person(50, 440, '#3B4F6B', 1, pose='wave', hs='curly') + cap(50, 372, .7) + person(110, 440, '#C77DBA', 2, '#6B3E1E', pose='wave', hs='long', face=-1, begin=.4) + cap(110, 372, .7)
    o += bubble(80, 330, 'Ci siamo laureati!', '#fff', side=0, size=10)
    o += books(50, 600, 1.1) + open_book(120, 600, .8) + bubble(80, 650, 'Esame superato!', '#E8F4EC', side=0, size=10) + tree(30, 700, .8)
    return done(bg, o, 'stone', '#E5F0DA')


def t_cinema():
    o = '<rect width="400" height="700" fill="#2B2440"/>' + curtain_stage(400, 0, 420, '#8A2E3B') + screen(110, 60, 180, 110)
    o += ''.join(f'<path d="M0 {y} Q200 {y - 20} 400 {y}" stroke="#3B3458" stroke-width="16" fill="none"/>' for y in range(460, 700, 50))
    bg, o = o, ''
    o += film_reel(60, 250, 24) + film_reel(110, 280, 16) + notes(150, 240, 1.2, '#FFC94A')
    o += person(60, 480, '#E2574C', 1, pose='hold', hs='long', skirt=True) + popcorn(88, 446, .9) + person(120, 480, '#3F6FA8', 2, pose='point', face=-1, glasses=True)
    o += bubble(90, 380, 'Che bel film!', '#fff', side=0, size=11)
    o += microphone(60, 690, 1) + guitar(120, 680, .6, -20) + bubble(90, 600, 'E che canzone!', '#FFF3C4', side=0, size=11)
    return done(bg, o, 'carpet', '#4A3F66', True)


def t_kitchen():
    o = '<rect width="400" height="700" fill="#FBF1E1"/><rect y="320" width="400" height="380" fill="#E8D3B5"/>'
    o += ''.join(f'<rect x="{x}" y="{y}" width="20" height="20" fill="#fff" stroke="#F0DFC4"/>' for x in range(0, 400, 20) for y in range(180, 320, 20))
    o += '<rect x="20" y="70" width="140" height="90" fill="#B97A4E"/><rect x="26" y="76" width="62" height="78" fill="#C88A5E"/><rect x="92" y="76" width="62" height="78" fill="#C88A5E"/>'
    bg, o = o, ''
    o += stove(80, 420, 1) + pot(70, 356, .9) + recipe_card(150, 330, 'RICETTA', .8)
    o += person(60, 600, '#fff', 1, pose='hold', face=1, beard=True) + '<path d="M50 524 Q48 506 60 504 Q72 506 70 524 Z" fill="#fff" transform="translate(-1 2)"/>'
    o += veg(120, 600, 1.2) + bubble(90, 500, 'Prima si taglia…', '#fff', side=0, size=10)
    o += table(90, 700, 1, '#B97A4E', 110) + bread(70, 656) + cheese(110, 658) + bubble(80, 680, 'Buonissimo!', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'tiles', '#F3E4CC')


def t_comic():
    o = '<rect width="400" height="700" fill="#FFF7DC"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="2" fill="#F2D27A"/>' for x in range(10, 400, 16) for y in range(10, 700, 16))
    bg, o = o, ''
    p1 = person(40, 116, '#3F6FA8', 1, pose='point', s=.8, hs='curly') + bubble(60, 26, 'Tonnerre !', '#fff', side=0, size=10)
    o += comic_panel(20, 140, 120, 130, p1)
    p2 = '<path d="M60 70 l10 -30 l8 22 l14 -16 l-2 24 l20 -6 l-14 18 l18 10 l-24 2 Z" fill="#FFC94A"/>' + txt(60, 64, 'BAM!', 16, '#E2574C', weight=900)
    o += comic_panel(20, 290, 120, 110, p2, '#E8F4FF')
    p3 = person(30, 116, '#E2574C', 2, '#6B3E1E', pose='wave', s=.8, hs='long') + dog(90, 116, .8, -1) + bubble(60, 28, 'Et voilà !', '#fff', side=0, size=10)
    o += comic_panel(20, 420, 120, 130, p3, '#FFF0F0')
    o += easel(80, 690, .9) + pencil(150, 660, 1)
    return done(bg, o, 'paper', '#FFF4D0')


def t_wall():
    o = sky('#3A4A7A', '#8A7AB0', 400) + '<rect y="380" width="400" height="320" fill="#6E6A80"/>'
    o += wall_segment(90, 400, 1.2) + wall_segment(330, 400, 1.2) + brandenburg(200, 300, .9)
    o += firework(70, 90, 26, '#FFC94A') + firework(330, 120, 22, '#E2574C', 1)
    bg, o = o, ''
    o += person(50, 560, '#E2574C', 1, pose='wave', hs='curly') + person(100, 560, '#3F6FA8', 2, '#6B3E1E', pose='wave', hs='long', face=-1, begin=.4)
    o += person(150, 560, '#5BAA6A', 0, '#B58A3C', pose='wave', begin=.8, beard=True)
    o += bubble(90, 470, 'Die Mauer ist offen!', '#fff', side=0, size=10) + txt(80, 640, '9.11.1989', 18, '#FFF3C4', weight=900)
    o += country_flag(40, 680, 40, 24)
    return done(bg, o, 'stone', '#6E6A90', True)


def t_alps():
    o = sky('#BFE0F7', '#EEF7FB', 330) + mountains(330) + '<rect y="330" width="400" height="120" fill="#6FB6DD"/><path d="M0 450 Q200 420 400 450 V700 H0 Z" fill="#9CCB7E"/>'
    o += ''.join(f'<path d="M{x} {y} q8 -4 16 0 q8 4 16 0" stroke="#BFE4F7" stroke-width="2.5" fill="none"/>' for x, y in ((40, 370), (220, 400), (300, 360)))
    bg, o = o, ''
    o += boat(70, 400, 1.1, '#E2574C') + boat(140, 420, .7, '#3F6FA8')
    o += chalet(60, 560, 1.1) + cow(140, 600, .9, -1) + pine(20, 600, .8)
    o += person(80, 690, '#E2574C', 1, pose='wave', hs='curly') + bubble(90, 470, 'Grüezi!', '#fff', side=0, size=12)
    o += bubble(110, 640, 'Was für eine Aussicht!', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'trail', '#DCEFE3')


def t_fado():
    o = env_night('#1E2448', '#4A3A6A') + '<rect y="380" width="400" height="320" fill="#5A4A3E"/>'
    o += ''.join(f'<path d="M0 {y} H400" stroke="#4A3A30" stroke-width="2"/>' for y in range(400, 700, 30))
    o += facade(0, 200, 90, 180, '#E8C08A', rows=4, door=True) + facade(310, 180, 90, 200, '#9ED3F0', rows=4)
    bg, o = o, ''
    o += lamp(40, 380, 1.1) + person(70, 520, '#26323A', 1, '#1E1A18', pose='stand', hs='long', skirt=True)
    o += '<path d="M54 470 Q70 490 86 470 L90 500 Q70 510 50 500 Z" fill="#26323A"/>'
    o += chair(130, 560, 1, '#8A5A3B', -1) + person(130, 560, '#3B4F6B', 2, s=.9, face=-1, beard=True) + guitarra_pt(118, 520, .55, -30)
    o += notes(100, 420, 1, '#FFC94A') + bubble(80, 400, 'Ó gente da minha terra…', '#fff', side=0, size=9)
    o += wine_glass(50, 680) + candle(80, 680) + bubble(100, 640, 'Que saudade!', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'stone', '#5A4A6E', True)


def t_carnation():
    o = sky('#DDEFFA', '#F7F1E6', 330) + '<rect y="300" width="400" height="400" fill="#E6DDCF"/>'
    o += facade(0, 140, 80, 160, '#F2D3A6', rows=3, door=True) + facade(320, 130, 80, 170, '#9ED3F0', rows=3)
    bg, o = o, ''
    o += txt(90, 120, '25 DE ABRIL', 20, '#D9352B', weight=900) + country_flag(40, 140, 50, 32)
    o += person(40, 380, '#3E6B4F', 1, pose='wave', hs='short') + carnation(52, 340, 1, 10) + person(100, 380, '#E2574C', 2, '#6B3E1E', pose='wave', hs='long', face=-1, begin=.3) + carnation(90, 344, 1, -10)
    o += person(150, 380, '#3F6FA8', 0, '#B58A3C', pose='wave', begin=.6, beard=True)
    o += bubble(90, 290, '25 de Abril, sempre!', '#fff', side=0, size=10)
    o += ''.join(carnation(x, 600 + (i % 2) * 10, 1.1, (i - 2) * 12) for i, x in enumerate((30, 60, 90, 120, 150)))
    o += bubble(90, 680, 'Liberdade!', '#FFF3C4', side=0, size=11)
    return done(bg, o, 'stone', '#EFE5D6')


def t_republic():
    o = sky('#D7ECFA', '#F4F1EA', 330) + '<rect y="300" width="400" height="400" fill="#E3DACB"/>'
    o += '<rect x="20" y="130" width="200" height="170" fill="#EFE4CF"/><path d="M10 130 L120 80 L230 130 Z" fill="#7F8A99"/>' + ''.join(column(x, 300, 110, .7) for x in (50, 90, 150, 190))
    o += '<path d="M112 40 V120" stroke="#5B6676" stroke-width="3"/>' + country_flag(112, 40, 36, 24) + txt(120, 152, 'MAIRIE', 13, '#5B6676', weight=900)
    bg, o = o, ''
    o += txt(90, 340, 'LIBERTÉ', 13, '#1F4FA0', weight=900) + txt(90, 360, 'ÉGALITÉ', 13, '#5B6676', weight=900) + txt(90, 380, 'FRATERNITÉ', 13, '#D9352B', weight=900)
    o += f'<g transform="translate(70 520)"><rect x="-26" y="-50" width="52" height="50" rx="4" fill="#C9D3DE"/><rect x="-14" y="-56" width="28" height="6" fill="#26323A"/>' + txt(0, -20, 'VOTE', 10, '#26323A', weight=900) + '</g>'
    o += person(130, 540, '#3F6FA8', 1, pose='hold', face=-1, glasses=True) + envelope(140, 500, .6)
    o += bubble(90, 440, 'Aux urnes, citoyens !', '#fff', side=0, size=10)
    o += stamp_(50, 680, 1, 'RF') + clipboard(140, 690, .9)
    return done(bg, o, 'hall', '#ECE6DC')


def t_salon():
    o = '<rect width="400" height="700" fill="#EADCC4"/><rect y="340" width="400" height="360" fill="#8A5A3B"/>' + ''.join(f'<path d="M{x} 340 L{x - 40} 700" stroke="#7A4A2E" stroke-width="2"/>' for x in range(0, 460, 50))
    o += chandelier(120, 0, 1.2) + frame(30, 130, 70, 56, '#F7C9A0') + bookshelf(130, 330, 1, 90, 180)
    bg, o = o, ''
    o += tophat_person(50, 470, '#5B4A6B', 2, 1, 1, 'wig') + tophat_person(120, 470, '#3E6B4F', 0, -1, 1, 'wig')
    o += bubble(90, 370, 'Sapere aude!', '#fff', side=0, size=11) + table(80, 560, 1, '#5E3E28', 100) + candle(60, 518) + quill(100, 512, .7) + books(130, 518, .6)
    o += scroll(70, 680, 1) + bubble(110, 630, 'Les Lumières', '#FFF3C4', side=0, size=11)
    return done(bg, o, 'ink', '#E3D3B8')


def t_kafka():
    o = env_room('#D8D3C4', '#8A7A62', 320, True, 40)
    bg, o = o, ''
    o += bed(70, 460, 1.2) + beetle(80, 420, 1.1)
    o += bubble(90, 330, 'Was ist mit mir geschehen?', '#fff', side=0, size=9)
    o += alarm(140, 400, .8) + open_book(70, 640, 1.1) + txt(70, 580, 'Die Verwandlung', 11, '#5E3E28', extra='font-style="italic"')
    o += txt(70, 600, 'Franz Kafka, 1915', 9, '#7A6A52')
    return done(bg, o, 'ink', '#DCD5C3')


def t_coffeehouse():
    o = '<rect width="400" height="700" fill="#F3E3C8"/><rect y="360" width="400" height="340" fill="#7A4A2E"/>' + ''.join(f'<rect x="{x}" y="{y}" width="30" height="30" fill="#6A3E26"/>' for y in range(360, 700, 60) for x in range(0 if (y // 60) % 2 else 30, 400, 60))
    o += chandelier(120, 0, 1.2) + chandelier(300, 0, 1) + '<rect x="20" y="100" width="200" height="160" rx="80" fill="#E9D3A8" stroke="#C9A24A" stroke-width="5"/>'
    bg, o = o, ''
    o += f'<g transform="translate(70 470)"><ellipse cy="-40" rx="40" ry="10" fill="#F4F1EA"/><rect x="-3" y="-40" width="6" height="40" fill="#26323A"/><ellipse cy="-1" rx="16" ry="3" fill="#26323A"/></g>'
    o += sachertorte(60, 428, .9) + cup(92, 428, .8) + newspaper(150, 430, .8, 4, 'ZEITUNG')
    o += person(30, 500, '#5B4A6B', 1, pose='hold', s=.95, glasses=True, hs='bun') + person(140, 520, '#fff', 0, '#1E1A18', pose='hold', face=-1, beard=True) + '<path d="M136 482 l4 6 l4 -6" fill="#26323A"/>'
    o += bubble(90, 350, 'Eine Melange, bitte!', '#fff', side=0, size=10) + bubble(110, 610, 'Sehr gerne!', '#FFF3C4', side=0, size=11)
    o += plant(40, 690) + armchair(130, 690, .8, '#8A2E3B', -1)
    return done(bg, o, 'carpet', '#E8D2AE')


def t_idioms():
    o = env_park('#E2F0FA', '#F4F7EA', '#C9E2B0', '#BCD9A2', 280)
    bg, o = o, ''
    k = LOC.get('idiom', 'catsdogs')
    pic = ''
    if k == 'catsdogs':
        pic = (raincloud(90, 120, 1.3) + dog(60, 230, .9) + f'<g transform="translate(120 228)"><ellipse cx="0" cy="-10" rx="16" ry="10" fill="#F2B880"/><circle cx="13" cy="-22" r="9" fill="#F2B880"/><path d="M7 -29 l3 -8 l4 6 M14 -30 l4 -7 l2 8" fill="#F2B880"/></g>')
    elif k == 'ropes':
        pic = raincloud(90, 110, 1.3) + ''.join(f'<path d="M{x} 130 q6 20 0 40 q-6 20 0 40" stroke="#C8955E" stroke-width="4" fill="none"/>' for x in (60, 90, 120))
    elif k == 'station':
        pic = train(90, 230, .55) + bubble_think(90, 120, txt(0, 6, '???', 18, '#3F6FA8', weight=900), 90, 50)
    elif k == 'sea':
        pic = (f'<g transform="translate(90 230)"><path d="M-60 0 q10 -8 20 0 t20 0 t20 0 t20 0 t20 0 t20 0" stroke="#4FA9DD" stroke-width="5" fill="none" stroke-linecap="round"/>'
               '<path d="M-50 12 q10 -8 20 0 t20 0 t20 0 t20 0 t20 0" stroke="#7FC3E8" stroke-width="4" fill="none" stroke-linecap="round"/>'
               '<path d="M-14 -30 L14 -30 L10 -2 L-10 -2 Z" fill="#E9EEF3" stroke="#9AA6B8" stroke-width="2" transform="rotate(70)"/></g>'
               + bubble_think(90, 120, txt(0, 6, '!!!', 18, '#2A86C9', weight=900), 90, 50))
    elif k == 'petisca':
        pic = f'<g transform="translate(90 220)">' + '<ellipse rx="40" ry="8" fill="#fff" stroke="#C9CFD6"/><path d="M-20 -4 q10 -14 20 0 q10 -14 20 0" fill="#E2A43A"/><circle cx="-6" cy="-8" r="4" fill="#3E8A52"/></g>' + bubble_think(90, 120, txt(0, 6, '€€€ ?', 16, '#2F7A4E', weight=900), 90, 50)
    o += pic
    o += person(50, 400, '#3F6FA8', 1, pose='point', glasses=True) + person(120, 400, '#E2574C', 2, '#6B3E1E', pose='hold', face=-1, hs='long')
    o += bubble(90, 300, 'In bocca al lupo!', '#fff', side=0, size=10)
    o += bubble(90, 470, 'Crepi!', '#FFF3C4', side=0, size=11) + open_book(60, 640, 1) + magnifier(130, 650, .9) + tree(30, 700, .7)
    return done(bg, o, 'trail', '#E4F0DA')


def t_shakespeare():
    """Globe Theatre: teatro isabelino redondo con techo de paja."""
    o = sky('#D7ECFA', '#F4EEE4', 330) + '<rect y="300" width="400" height="400" fill="#D9CBB0"/>'
    o += '<path d="M10 300 L10 170 Q120 140 230 170 L230 300 Z" fill="#F1E8DA"/>' + ''.join(f'<path d="M{x} 170 V300" stroke="#6B4429" stroke-width="5"/>' for x in range(20, 230, 30))
    o += '<path d="M10 200 H230 M10 250 H230" stroke="#6B4429" stroke-width="4"/><path d="M0 172 Q120 120 240 172 L230 160 Q120 112 10 160 Z" fill="#C9A24A"/>'
    o += '<path d="M120 140 V100 L146 110 L120 120" fill="#C0392B" stroke="#5B6676" stroke-width="2"/>'
    bg, o = o, ''
    o += tophat_person(60, 440, '#2F3E5A', 1, 1, 1, 'ruff', beard=True) + bubble(90, 340, 'To be, or not to be…', '#fff', side=0, size=10)
    o += scroll(130, 460, .9) + quill(150, 420, .8) + open_book(70, 640, 1.1) + txt(70, 590, 'HAMLET', 12, '#B03A4A', weight=900)
    return done(bg, o, 'ink', '#EDE3CF')


# ---------------------------------------------------------------- mapa genérico (Natural Earth, dominio público)
_GEO = {}


def geo_features():
    if 'f' not in _GEO:
        import json as _j
        d = _j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo', 'ne_50m_admin_0_countries.geojson')))
        _GEO['f'] = [(f['properties'].get('NAME_EN') or f['properties']['NAME'], f['geometry']) for f in d['features']]
    return _GEO['f']


def map_projector(lon0, lon1, lat1):
    K = 400 / math.radians(lon1 - lon0)
    merc = lambda la: math.log(math.tan(math.pi / 4 + math.radians(max(-80, min(80, la))) / 2))
    return lambda lon, lat: ((lon - lon0) * math.pi / 180 * K, (merc(lat1) - merc(lat)) * K)


def map_paths(P, hi, tol=.8, base='#EDE6D3'):
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo'))
    import europe
    o = ''
    for name, gm in geo_features():
        polys = [gm['coordinates']] if gm['type'] == 'Polygon' else gm['coordinates']
        segs = []
        for poly in polys:
            ring = [P(lo, la) for lo, la in poly[0]]
            xs = [p[0] for p in ring]; ys = [p[1] for p in ring]
            if max(xs) < -40 or min(xs) > 440 or max(ys) < -40 or min(ys) > 740:
                continue
            ring = europe.clip(ring)
            if len(ring) < 4:
                continue
            k = max(range(len(ring)), key=lambda j: (ring[j][0] - ring[0][0]) ** 2 + (ring[j][1] - ring[0][1]) ** 2)
            r = europe.dp(ring[:k + 1], tol)[:-1] + europe.dp(ring[k:], tol)
            if len(r) < 3:
                continue
            segs.append('M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in r) + 'Z')
        if segs:
            o += f'<path d="{"".join(segs)}" fill="{hi.get(name, base)}" stroke="#fff" stroke-width="1.1" stroke-linejoin="round"/>'
    return o


def t_map(cfg, side=1):
    """cfg: lon0, lon1, lat1, hi{país: color}, cities[(nombre, lon, lat)], pills[(texto, lon, lat, color)], title, tint, path, tol."""
    P = map_projector(cfg['lon0'], cfg['lon1'], cfg['lat1'])
    o = f'<rect width="400" height="700" fill="{cfg.get("sea", "#9ED3F0")}"/>' + map_paths(P, cfg.get('hi', {}), cfg.get('tol', .8))
    for name, lon, lat in cfg.get('cities', ()):
        x, y = P(lon, lat)
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#26323A"/>' + txt(x + 5, y + 4, name, 9, '#26323A', 'start')
    for t, lon, lat, size in cfg.get('labels', ()):
        x, y = P(lon, lat)
        o += txt(x, y, t, size, '#7A6A4A', extra='letter-spacing="2" opacity=".75"')
    bg, o = o, ''
    inv = lambda x, y: (200 + (x - 200) / .86, 360 + (y - 360) / .86)
    pills = cfg.get('pills', ())
    n = len(pills)
    lx = 84 if side == 1 else 316
    for i, (t, lon, lat, c) in enumerate(pills):
        x, y = inv(*P(lon, lat))
        ly = 130 + i * (480 / max(1, n - 1 if n > 1 else 1)) if n > 1 else 360
        w = max(70, len(t) * 8 + 20)
        o += f'<path d="M{lx + (w / 2 if side == 1 else -w / 2)} {ly} Q{(lx + x) / 2} {ly} {x:.1f} {y:.1f}" stroke="{c}" stroke-width="2" stroke-dasharray="4 4" fill="none"/>'
        o += f'<g transform="translate({lx} {ly})"><rect x="{-w / 2}" y="-14" width="{w}" height="28" rx="14" fill="{c}"/>' + txt(0, 5, t, 12, '#fff', weight=900) + '</g>'
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{c}" stroke="#fff" stroke-width="2"/>'
    if cfg.get('title'):
        t = cfg['title']
        size = min(14, 150 / (len(t) * .6))
        o += txt(110 if side == 1 else 290, 40, t, round(size, 1), '#26323A', weight=900)
    return dict(path=cfg.get('path', 'flight'), svg=svg(bg + fg(o)), tint=cfg.get('tint', '#9ED3F0'))


def t_stonehenge():
    o = sky('#F7C59F', '#FBE9D7', 330) + sun(110, 250, 30, '#FFB25B') + '<path d="M0 290 Q200 260 400 290 V700 H0 Z" fill="#A9C98A"/>'
    for x, h in ((20, 70), (60, 80), (130, 76), (170, 66)):
        o += f'<rect x="{x}" y="{300 - h}" width="24" height="{h}" fill="#9A9488"/>'
    o += '<rect x="56" y="214" width="102" height="14" fill="#8A8478"/><rect x="200" y="250" width="22" height="50" fill="#9A9488"/><rect x="300" y="240" width="26" height="60" fill="#9A9488"/>'
    bg, o = o, ''
    o += person(50, 440, '#3F6FA8', 1, pose='point', glasses=True) + person(110, 440, '#E2574C', 2, '#6B3E1E', pose='hold', face=-1, hs='long') + magnifier(140, 400, .6)
    o += bubble(80, 340, 'Ciao!', '#fff', side=0, size=11) + bubble(90, 500, 'Piacere!', '#FFF3C4', side=0, size=11)
    o += scroll(60, 660, .9) + tree(150, 690, .8)
    return done(bg, o, 'trail', '#F2E4CF')


# ---------------------------------------------------------------- plantillas griegas (lado libre a la izquierda)
def bouzouki(x, y, s=1, rot=-30):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0 -26 C-20 -24 -22 10 0 14 C22 10 20 -24 0 -26 Z" fill="#A8672E"/>'
            '<path d="M0 -26 C-12 -24 -14 6 0 10" stroke="#7A4419" stroke-width="1.5" fill="none"/><circle cy="-6" r="4" fill="#3A2A1E"/>'
            '<rect x="-2.5" y="-86" width="5" height="62" fill="#5E3E28"/><rect x="-5" y="-96" width="10" height="12" rx="2" fill="#3A2A1E"/>'
            '<path d="M-1 -84 V8 M1 -84 V8" stroke="#E9E4DA" stroke-width=".5"/></g>')


def ferry(x, y, s=1):
    o = ('<path d="M-80 0 L80 0 L64 26 L-70 26 Z" fill="#F4F1EA" stroke="#C9CFD6" stroke-width="2"/><rect x="-70" y="16" width="134" height="6" fill="#0D5EAF"/>'
         '<rect x="-50" y="-26" width="96" height="26" rx="4" fill="#fff" stroke="#C9CFD6" stroke-width="2"/>'
         + ''.join(f'<rect x="{-44 + i * 16}" y="-20" width="10" height="9" rx="2" fill="#7FB7E3"/>' for i in range(6))
         + '<rect x="-24" y="-46" width="44" height="20" rx="3" fill="#fff" stroke="#C9CFD6" stroke-width="2"/><rect x="2" y="-64" width="12" height="20" fill="#E2574C"/><rect x="2" y="-58" width="12" height="4" fill="#fff"/>')
    return g(o, x, y, s)


def gull(x, y, s=1, begin=0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-12 0 q6 -8 12 0 q6 -8 12 0" stroke="#5B6676" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
            f'<animateTransform attributeName="transform" type="translate" values="{x} {y};{x + 14} {y - 6};{x} {y}" dur="5s" begin="{begin}s" repeatCount="indefinite" additive="replace"/></g>')


def t_ferry():
    o = env_sea(300) + sun(320, 70, 24) + '<path d="M250 300 Q300 250 360 268 Q390 276 400 300 Z" fill="#C9B48E"/>'
    o += ''.join(f'<rect x="{x}" y="{yy}" width="14" height="12" fill="#FBFAF6"/>' for x, yy in ((300, 276), (316, 282), (330, 274), (346, 284)))
    o += '<path d="M318 262 a10 10 0 0 1 20 0 z" fill="#1F6FB2"/><rect x="318" y="262" width="20" height="14" fill="#FBFAF6"/>'
    bg, o = o, ''
    o += ferry(100, 330, 1) + gull(60, 210, 1) + gull(140, 190, .8, 1.5)
    o += bubble(90, 260, 'Πάμε στη Νάξο!', '#fff', side=0, size=11)
    o += person(50, 560, '#2A86C9', 1, pose='wave', hs='long', skirt=True) + person(110, 560, '#E2574C', 3, '#1E1A18', pose='point', face=-1)
    o += bubble(90, 470, 'Καλό ταξίδι!', '#FFF3C4', side=0, size=11)
    o += '<g transform="translate(60 660)"><rect x="-26" y="-34" width="52" height="34" rx="5" fill="#E2A43A"/><rect x="-8" y="-42" width="16" height="10" rx="3" fill="none" stroke="#9C6B1E" stroke-width="3"/></g>'
    o += '<g transform="translate(140 676)"><path d="M-24 0 L24 0 L0 -40 Z" fill="#E2574C"/><path d="M0 -40 V6" stroke="#5B6676" stroke-width="2"/></g>'
    return done(bg, o, 'sea', '#D6EEF9')


def t_rebetiko():
    o = '<rect width="400" height="700" fill="#3B2A2E"/><rect y="380" width="400" height="320" fill="#5E3E28"/>'
    o += ''.join(f'<path d="M0 {yy} H400" stroke="#4E3322" stroke-width="2"/>' for yy in range(410, 700, 34))
    o += ''.join(f'<g transform="translate({x} 40)"><path d="M0 0 V30" stroke="#C9A24A" stroke-width="1.5"/><circle cy="38" r="9" fill="#FFD66B" opacity=".9"/><circle cy="38" r="20" fill="#FFD66B" opacity=".15"/></g>' for x in (60, 180, 300))
    o += '<rect x="20" y="120" width="200" height="130" rx="6" fill="#4A3436" stroke="#7A5A3E" stroke-width="4"/>' + txt(120, 196, 'ΡΕΜΠΕΤΙΚΑ', 18, '#E9C46A', weight=900)
    bg, o = o, ''
    o += chair(60, 470, 1, '#8A5A3B') + person(60, 470, '#26323A', 1, '#1E1A18', pose='hold', s=1, beard=True) + bouzouki(80, 440, .9, -40)
    o += chair(130, 470, 1, '#8A5A3B', -1) + person(130, 470, '#8A2E3B', 2, '#3A2A1E', pose='hold', face=-1, hs='long') + guitar(112, 446, .7, 30)
    o += bubble(90, 360, 'Όπα!', '#fff', side=0, size=13)
    o += table(80, 620, 1, '#7A4A2E', 110) + cup(60, 578, .7, False) + cup(100, 578, .7, False)
    o += ''.join(f'<circle cx="{x}" cy="{yy}" r="4" fill="{c}"/>' for x, yy, c in ((40, 660, '#E2574C'), (52, 668, '#FFC94A'), (140, 650, '#E2574C'), (150, 662, '#F2F2F2')))
    o += bubble(110, 690, 'Γεια σου, Νίκο!', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'carpet', '#4A3436', True)


def t_theatre():
    # Teatro antiguo (Epidauro): gradas en semicírculo y la orchestra
    o = sky('#F9D9A6', '#FBEFD9', 300) + sun(90, 90, 26, '#FFB25B') + '<path d="M0 250 Q200 200 400 250 V700 H0 Z" fill="#9DBA7A"/>'
    o += ''.join(f'<path d="M{20 + i * 6} {300 + i * 16} Q200 {220 + i * 22} {380 - i * 6} {300 + i * 16}" stroke="#D9CBAA" stroke-width="12" fill="none"/>' for i in range(8))
    o += '<ellipse cx="200" cy="470" rx="110" ry="30" fill="#E9DDC2"/>'
    bg, o = o, ''
    o += '<g transform="translate(70 470)"><path d="M-22 -60 Q0 -76 22 -60 Q24 -36 0 -24 Q-24 -36 -22 -60 Z" fill="#F4F1EA" stroke="#5E3E28" stroke-width="2"/><path d="M-12 -56 q4 -4 8 0 M4 -56 q4 -4 8 0" stroke="#26323A" stroke-width="2" fill="none"/><path d="M-8 -38 q8 -8 16 0" stroke="#26323A" stroke-width="2" fill="none"/></g>'
    o += '<g transform="translate(120 480)"><path d="M-22 -60 Q0 -76 22 -60 Q24 -36 0 -24 Q-24 -36 -22 -60 Z" fill="#F4F1EA" stroke="#5E3E28" stroke-width="2"/><path d="M-12 -54 q4 4 8 0 M4 -54 q4 4 8 0" stroke="#26323A" stroke-width="2" fill="none"/><path d="M-8 -34 q8 8 16 0" stroke="#26323A" stroke-width="2" fill="none"/></g>'
    o += bubble(90, 360, 'Αντιγόνη', '#fff', side=0, size=12)
    o += person(60, 620, '#C77DBA', 2, '#6B3E1E', pose='wave', hs='long', skirt=True) + person(120, 620, '#3F6FA8', 1, pose='wave', face=-1, begin=.4)
    o += bubble(90, 540, 'Μπράβο!', '#FFF3C4', side=0, size=12) + plant(40, 700)
    return done(bg, o, 'stone', '#F2E4CF')


def t_byzantine():
    # Iglesia bizantina: cúpula, ladrillo y mosaico dorado
    o = sky('#D7ECFA', '#F4EEE4', 320) + '<rect y="300" width="400" height="400" fill="#E6DCC8"/>'
    o += '<rect x="30" y="170" width="180" height="130" fill="#C9845A"/>' + ''.join(f'<path d="M30 {yy} H210" stroke="#B06F48" stroke-width="2"/>' for yy in range(180, 300, 10))
    o += '<rect x="80" y="130" width="80" height="44" fill="#C9845A"/><path d="M80 130 a40 34 0 0 1 80 0 z" fill="#8A6B4A"/><path d="M120 96 V80 M114 86 h12" stroke="#C9A24A" stroke-width="3"/>'
    o += ''.join(f'<path d="M{x} 300 v-40 a12 12 0 0 1 24 0 v40 z" fill="#5E3E28"/>' for x in (54, 108, 162))
    bg, o = o, ''
    o += '<g transform="translate(90 430)"><rect x="-56" y="-70" width="112" height="90" rx="6" fill="#C9A24A"/><rect x="-50" y="-64" width="100" height="78" rx="4" fill="#E8C766"/>'
    o += ''.join(f'<rect x="{-48 + (i % 12) * 8}" y="{-62 + (i // 12) * 8}" width="7" height="7" fill="{["#E8C766", "#D9B24E", "#F2D98A"][i % 3]}"/>' for i in range(108))
    o += '<circle cy="-26" r="20" fill="#F2D98A" stroke="#B88A2E" stroke-width="2"/><circle cy="-28" r="9" fill="#E9C9A0"/><path d="M-14 -4 Q0 -18 14 -4 V8 H-14 Z" fill="#3F5A9A"/></g>'
    o += bubble(90, 330, 'Αγία Σοφία, 537', '#fff', side=0, size=10)
    o += candle(50, 600) + candle(70, 610) + candle(130, 600) + person(100, 640, '#5B4A6B', 2, '#3A2A1E', pose='hold', hs='bun', face=-1)
    o += bubble(90, 690, 'Τι ψηφιδωτά!', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'stone', '#EDE3CF')


def t_whitetower():
    # Θεσσαλονίκη: el Λευκός Πύργος junto al mar y las «Ομπρέλες»
    o = env_sea(330) + '<rect y="440" width="400" height="260" fill="#DCD6C8"/>'
    o += '<g transform="translate(120 330)"><rect x="-34" y="-150" width="68" height="150" fill="#F2EFE6"/><rect x="-40" y="-160" width="80" height="12" fill="#E4DED2"/>'
    o += ''.join(f'<rect x="{-38 + i * 12}" y="-170" width="8" height="10" fill="#E4DED2"/>' for i in range(7))
    o += '<rect x="-14" y="-196" width="28" height="30" fill="#F2EFE6"/><path d="M-16 -196 H16" stroke="#E4DED2" stroke-width="3"/>'
    o += ''.join(f'<rect x="{-20 + i * 16}" y="{-130 + j * 36}" width="6" height="12" rx="3" fill="#5B6676"/>' for i in range(3) for j in range(3)) + '<path d="M-8 0 v-20 a8 8 0 0 1 16 0 v20 z" fill="#5E3E28"/></g>'
    o += '<g transform="translate(300 420)"><path d="M0 0 V-70" stroke="#9AA6B8" stroke-width="3"/>' + ''.join(f'<path d="M{dx} {-70 - dy} q16 -12 32 0 z" fill="#C9CFD6" stroke="#9AA6B8" stroke-width="1.5"/>' for dx, dy in ((-28, 0), (-8, 18), (6, 4))) + '</g>'
    bg, o = o, ''
    o += person(50, 560, '#E2574C', 1, pose='point', hs='long', skirt=True) + person(110, 560, '#3F6FA8', 3, '#1E1A18', pose='hold', face=-1, glasses=True)
    o += bubble(90, 470, 'Λευκός Πύργος!', '#fff', side=0, size=11)
    o += cornetto(60, 660, 1.4) + bubble(110, 650, 'Μια μπουγάτσα;', '#FFF3C4', side=0, size=10) + tree(30, 700, .7)
    return done(bg, o, 'road', '#E8E3D8')


# ================================================================ CATALÁN
_facade_prev_ca = facade


def facade(x, y, w, h, col, shut='#3E8A52', rows=2, cols=2, roof='#C0583F', door=False):
    if LOC.get('arch') != 'eixample':
        return _facade_prev_ca(x, y, w, h, col, shut, rows, cols, roof, door)
    # Eixample: piedra clara u ocre, balcones de hierro forjado, persianas verdes
    k = int(x * 7 + w) % 3
    col = ['#EBDDC2', '#E3C79A', '#F0E2C8'][k]
    ww, wh = 13, 19
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/><rect x="{x - 3}" y="{y - 7}" width="{w + 6}" height="8" fill="#CDB892"/>'
    out += f'<path d="M{x} {y - 7} q{w / 4} -10 {w / 2} 0 q{w / 4} -10 {w / 2} 0" fill="#D9C49C"/>'
    for r in range(rows):
        for c in range(cols):
            wx = x + (c + .5) * w / cols - ww / 2; wy = y + 10 + r * (wh + 14)
            out += f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="1" fill="{["#3E8A52", "#4C7A5B", "#5E8C6A"][k]}"/><path d="M{wx + ww / 2} {wy} V{wy + wh}" stroke="{col}" stroke-width="1.2"/>'
            out += f'<path d="M{wx - 4} {wy + wh - 6} H{wx + ww + 4} M{wx - 4} {wy + wh + 1} H{wx + ww + 4}" stroke="#26323A" stroke-width="1.4"/>' + ''.join(f'<path d="M{wx - 3 + i * 4} {wy + wh - 6} v7" stroke="#26323A" stroke-width=".8"/>' for i in range(6))
    if door:
        out += f'<path d="M{x + w / 2 - 9} {y + h} v-22 a9 9 0 0 1 18 0 v22 z" fill="#6B4429"/>'
    return out


def sagrada(x, y, s=1):
    # Sagrada Família: cuatro campanarios en forma de huso y la torre central con la cruz
    o = '<rect x="-80" y="-60" width="160" height="60" fill="#D8C29C"/>'
    o += ''.join(f'<path d="M{-50 + i * 10} -60 v-30 a5 5 0 0 1 10 0 v30" fill="#C9AF84"/>' for i in range(10))
    for i, (dx, hh) in enumerate(((-66, 150), (-38, 172), (38, 172), (66, 150))):
        o += f'<path d="M{dx - 11} -60 Q{dx - 13} {-60 - hh * .6} {dx} {-60 - hh} Q{dx + 13} {-60 - hh * .6} {dx + 11} -60 Z" fill="#CDB48A"/>'
        o += ''.join(f'<circle cx="{dx}" cy="{-74 - j * 16}" r="1.8" fill="#8A6B4A"/>' for j in range(int(hh / 18)))
        o += f'<circle cx="{dx}" cy="{-62 - hh}" r="4" fill="{["#E2574C", "#FFC94A", "#5BAA6A", "#FFC94A"][i]}"/>'
    o += '<path d="M-14 -60 Q-16 -170 0 -230 Q16 -170 14 -60 Z" fill="#D9C7A2"/><path d="M0 -230 V-252 M-8 -244 H8" stroke="#E9E4DA" stroke-width="4"/>'
    o += '<path d="M-20 0 v-34 a20 20 0 0 1 40 0 v34 z" fill="#8A6B4A"/>'
    return g(o, x, y, s)


_dome_prev_ca = dome


def dome(x, y, s=1):
    if LOC.get('landmark') == 'sagrada':
        return sagrada(x, y, s * .8)
    return _dome_prev_ca(x, y, s)


def ensaimada(x, y, s=1):
    spiral = 'M0 -9 m-2 0 a2 2 0 1 1 4 0 a5 4 0 1 1 -9 0 a8 6 0 1 1 15 1 a12 8 0 1 1 -22 0'
    return g(f'<ellipse cx="0" cy="-9" rx="18" ry="9" fill="#E9B46A"/><path d="{spiral}" stroke="#C98536" stroke-width="2.2" fill="none"/>'
             '<ellipse cx="0" cy="-11" rx="15" ry="6" fill="#fff" opacity=".55"/>', x, y, s)


_cornetto_prev_ca = cornetto


def cornetto(x, y, s=1):
    if LOC.get('pastry') == 'ensaimada':
        return ensaimada(x, y, s)
    return _cornetto_prev_ca(x, y, s)


_flag_prev_ca = country_flag


def country_flag(x, y, w=40, h=26):
    if LOC.get('flag') != 'ca':
        return _flag_prev_ca(x, y, w, h)
    # Senyera: nueve franjas, cinco amarillas y cuatro rojas
    return ''.join(f'<rect x="{x}" y="{y + i * h / 9:.2f}" width="{w}" height="{h / 9 + .2:.2f}" fill="{"#F2C230" if i % 2 == 0 else "#D9352B"}"/>' for i in range(9))


def rose(x, y, s=1, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0 0 V-30" stroke="#3E8A52" stroke-width="2.4"/><path d="M0 -14 q-9 -2 -10 -9 q8 0 10 6" fill="#5BAA6A"/>'
            '<path d="M-7 -32 q0 -10 7 -11 q7 1 7 11 q-7 5 -14 0 z" fill="#D9352B"/><path d="M-3 -38 q3 -4 6 0" stroke="#A8231C" stroke-width="1.4" fill="none"/></g>')


_t_idioms_prev_ca = t_idioms


def t_idioms():
    if LOC.get('idiom') != 'bots':
        return _t_idioms_prev_ca()
    # «Ploure a bots i barrals»: núvol de pluja i dos barrils
    o = env_park('#E2F0FA', '#F4F7EA', '#C9E2B0', '#BCD9A2', 280)
    bg, o = o, ''
    barrel = lambda bx, by: (f'<g transform="translate({bx} {by})"><path d="M-14 0 Q-18 -18 -14 -36 H14 Q18 -18 14 0 Z" fill="#A8672E"/>'
                             '<path d="M-15 -8 H15 M-16 -28 H16" stroke="#5E3E28" stroke-width="3"/><path d="M-6 -36 V0 M6 -36 V0" stroke="#7A4419" stroke-width="1" opacity=".6"/></g>')
    o += raincloud(90, 120, 1.3) + barrel(62, 236) + barrel(118, 236)
    o += person(50, 400, '#3F6FA8', 1, pose='point', glasses=True) + person(120, 400, '#E2574C', 2, '#6B3E1E', pose='hold', face=-1, hs='long')
    o += bubble(90, 300, 'In bocca al lupo!', '#fff', side=0, size=10)
    o += bubble(90, 470, 'Crepi!', '#FFF3C4', side=0, size=11) + open_book(60, 640, 1) + magnifier(130, 650, .9) + tree(30, 700, .7)
    return done(bg, o, 'trail', '#E4F0DA')


def t_santjordi():
    o = env_street('#CDEBFA', '#FBEFD9', '#E6E1D6', y0=260)
    bg, o = o, ''
    o += stall(100, 420, 1.1, '#D9352B')
    o += books(70, 372, .8) + books(110, 372, .8) + ''.join(rose(x, 378, .7, r) for x, r in ((136, -10), (146, 8), (156, -4)))
    o += country_flag(40, 270) + country_flag(140, 270)
    o += bubble(90, 300, 'Bon Sant Jordi!', '#fff', side=0, size=12)
    o += person(50, 560, '#3F6FA8', 1, pose='hold') + rose(66, 520, .8, 20) + person(120, 560, '#C77DBA', 2, '#6B3E1E', pose='wave', hs='long', skirt=True, face=-1, begin=.4)
    o += bubble(90, 470, 'Una rosa per a tu!', '#FFF3C4', side=0, size=11)
    o += open_book(60, 660, 1) + rose(130, 676, 1, -15) + bubble(110, 610, 'I un llibre per a mi!', '#E8F4EC', side=0, size=10)
    return done(bg, o, 'road', '#F3E6DA')


def t_castells():
    o = env_street('#CDEBFA', '#F7EEDC', '#E3D9C6', y0=300)
    o += dome(330, 300, .9)
    bg, o = o, ''
    shirt = '#C0392B'
    # la pinya i els pisos del castell, de baix a dalt
    o += ''.join(person(x, 620, shirt, (i % 3), pose='stand', s=.85, face=1 if x < 100 else -1) for i, x in enumerate((20, 46, 72, 128, 154, 180)))
    for lvl, (n, yy, sc) in enumerate(((3, 570, .9), (3, 515, .85), (2, 462, .8), (2, 412, .75), (1, 366, .7))):
        xs = [100] if n == 1 else ([82, 118] if n == 2 else [70, 100, 130])
        o += ''.join(person(x, yy, shirt, (lvl + j) % 3, pose='stand', s=sc) for j, x in enumerate(xs))
        o += f'<path d="M{xs[0] - 8} {yy - 30 * sc} H{xs[-1] + 8}" stroke="#26323A" stroke-width="5" stroke-linecap="round" opacity=".85"/>'
    o += person(100, 326, '#FFC94A', 1, pose='wave', s=.55, begin=.2) + '<g transform="translate(100 286)"><rect x="-6" y="-6" width="12" height="10" rx="5" fill="#F4F1EA"/></g>'
    o += bubble(90, 250, "L'enxaneta fa l'aleta!", '#fff', side=0, size=10)
    o += bubble(70, 680, 'Força, equilibri, valor i seny!', '#FFF3C4', side=0, size=9)
    return done(bg, o, 'stone', '#F1E6D2')


def t_gaudi():
    o = sky('#BFE4F7', '#FBEFD9', 300) + sagrada(300, 310, .9) + '<rect y="300" width="400" height="400" fill="#E8D9B8"/>'
    bg, o = o, ''
    tiles = ['#3F6FA8', '#E2574C', '#FFC94A', '#5BAA6A', '#F4F1EA', '#C77DBA']
    # banc ondulat de trencadís
    o += '<path d="M8 440 q22 -16 44 0 t44 0 t44 0 t44 0 V478 H8 Z" fill="#F4F1EA" stroke="#C9B48E" stroke-width="2"/>'
    o += ''.join(f'<path d="M{12 + (i % 22) * 8} {446 + (i // 22) * 9 - 7 * math.sin((i % 22) * .71):.1f} l6 -2 l2 6 l-6 2 z" fill="{tiles[(i * 5) % 6]}"/>' for i in range(66) if 446 + (i // 22) * 9 < 476)
    o += '<rect x="8" y="478" width="176" height="10" fill="#D9C49C"/>'
    # el drac (salamandra) de les escales
    o += '<g transform="translate(90 600)"><path d="M-60 0 Q-40 -30 0 -26 Q40 -22 56 -6 Q40 4 0 4 Q-30 6 -60 0 Z" fill="#5BAA6A"/>'
    o += ''.join(f'<circle cx="{-46 + i * 10}" cy="{-12 + (i % 2) * 5}" r="4" fill="{tiles[i % 6]}"/>' for i in range(10))
    o += '<circle cx="46" cy="-12" r="3" fill="#26323A"/><path d="M-60 0 q-16 -4 -22 -16" stroke="#5BAA6A" stroke-width="8" stroke-linecap="round" fill="none"/>'
    o += '<path d="M-30 4 v14 M10 4 v14 M30 0 v16" stroke="#3E8A52" stroke-width="6" stroke-linecap="round"/></g>'
    o += bubble(90, 380, 'Quin trencadís!', '#fff', side=0, size=12)
    o += person(60, 540, '#E2574C', 2, '#3A2A1E', pose='point', hs='long', skirt=True) + person(130, 540, '#3F6FA8', 1, pose='wave', face=-1, glasses=True)
    o += bubble(100, 670, 'El drac del Park Güell', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'stone', '#F2E6CF')
