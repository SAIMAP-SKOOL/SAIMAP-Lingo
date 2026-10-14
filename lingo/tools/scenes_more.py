"""Escenas 6–50 del italiano (se ejecuta dentro de scenes_it.py, después de scenes_lib2.py).
Unidades impares: nodos a la derecha → ilustración a la izquierda. Pares: al revés.
Cada escena se escribe pensando en el lado libre a la IZQUIERDA; en las pares, X() la refleja."""


def mk(n, flip=False):
    """m: 1 si el lado libre es el izquierdo (impares). X: identidad, o reflejo si la escena se dibujó en el lado contrario."""
    m = 1 if n % 2 else -1
    X = (lambda x: 400 - x) if flip else (lambda x: x)
    return m, X


def done(bg, o, path, tint, night=False):
    d = dict(path=path, svg=svg(bg + fg(o)), tint=tint)
    if night:
        d['night'] = True
    return d


# 6 · In città
def s6():
    m, X = mk(6)
    o = env_street('#BFE4F7', '#FBEFD9', '#D8D3C8', y0=240)
    o += sun(70, 50, 20) + cloud(300, 70, .9, 40, -30) + cloud(150, 40, .7, 36, 30)
    o += '<rect y="300" width="400" height="120" fill="#5D6878"/>' + ''.join(f'<rect x="{x}" y="357" width="26" height="5" fill="#FFD34D"/>' for x in range(10, 400, 52))
    o += '<rect y="292" width="400" height="8" fill="#C9C2B3"/><rect y="420" width="400" height="8" fill="#C9C2B3"/>'
    bg, o = o, ''
    o += zebra(X(320) - 45, 306, 90, 9)
    o += traffic_light(X(372), 296) + lamp(X(330), 292) + sign(X(320), 520, 'Duomo', '#3F6FA8', 1, 'r' if m == 1 else 'l')
    o += car(X(330), 400, .9, '#E2574C', -m) + vespa(X(250), 350, .9, '#5BB9B0', m)
    o += bus_stop(X(370), 520)
    o += person(X(300), 600, '#E2574C', 1, '#3A2A1E', pose='point', face=-m, hs='long', skirt=True) + person(X(350), 600, '#3F6FA8', 3, '#1E1A18', pose='stand', face=m, glasses=True)
    o += bubble(X(320), 470, "Scusi, dov'è…?", '#fff', side=0, size=11)
    o += bubble(X(310), 650, 'Sempre dritto!', '#FFF3C4', side=0, size=11)
    o += tree(X(370), 690, .8) + flowerpot(X(240), 690)
    o += shopfront(X(300) - 50, 220, 100, 'FARMACIA', '#E8F4EC', ('#5BAA6A', '#fff'))
    return done(bg, o, 'road', '#DDE3EA')


# 7 · A casa
def s7():
    m, X = mk(7)
    o = env_room('#F6E7D2', '#D9B48F', 300, True, X(30) if m == 1 else 280)
    o += frame(X(150) - 25, 90, 50, 38, '#F7C9A0') + frame(X(120) - 18, 150, 36, 30)
    bg, o = o, ''
    o += bookshelf(X(10) - (70 if m == -1 else 0), 300, 1, 70, 120)
    o += rug(X(90), 420, 140) + sofa(X(80), 410, .95, '#5BAA6A') + floor_lamp(X(150), 410)
    o += person(X(70), 400, '#C77DBA', 2, '#6B3E1E', pose='hold', hs='long', face=m) + open_book(X(84), 352, .4)
    o += plant(X(30), 520) + table(X(90), 560, 1, '#B97A4E', 90) + cup(X(70), 518, .8, True) + books(X(110), 518, .6)
    o += dog(X(120), 640, .9, m) + tv(X(60), 690, .9)
    o += bubble(X(80), 260, 'Benvenuti!', '#fff', side=0, size=11)
    o += tag(X(360), 620, 'SOGGIORNO', '#C77DBA') + tag(X(360), 120, 'CUCINA', '#3F6FA8')
    return done(bg, o, 'plank', '#F3E3CD')


# 8 · Fare la spesa
def s8():
    m, X = mk(8, True)
    o = env_street('#CDEBFA', '#FCEFD9', '#EADFC9', y0=230)
    o += sun(330 if m == 1 else 70, 46, 20) + cloud(200, 60, .9)
    bg, o = o, ''
    o += stall(X(70), 330, 1, '#E2574C') + stall(X(80), 560, .95, '#3E8A52')
    o += person(X(150), 330, '#fff', 1, '#3A2A1E', pose='hold', face=-m, beard=True) + bubble(X(110), 200, 'Quanto costa?', '#fff', side=0, size=11)
    o += person(X(160), 580, '#F2B880', 2, '#6B3E1E', pose='point', hs='bun', skirt=True, face=-m)
    o += bubble(X(100), 440, 'Un chilo di mele!', '#FFF3C4', side=0, size=11)
    o += bag(X(30), 680, 1) + bread(X(80), 680) + cheese(X(130), 682) + bottle(X(360), 690) + scale_(X(40), 330)
    o += tag(X(40), 380, '€2/kg', '#E2574C') + tag(X(110), 610, '€1,50', '#3E8A52')
    o += crate(X(360), 440, '#FFB25B') + crate(X(360), 300, '#C77DBA')
    return done(bg, o, 'stone', '#F3E7D2')


# 9 · Il tempo libero
def s9():
    m, X = mk(9)
    o = env_park(y0=240) + sun(X(60), 60, 22) + cloud(X(300), 80, .9, 40, -30)
    bg, o = o, ''
    o += kite(X(80), 150, 1, '#E2574C') + raincloud(X(330), 210, .8)
    o += person(X(60), 330, '#5BAA6A', 1, pose='hold', hs='curly', face=m) + guitar(X(70), 314, .5, -30 * m) + notes(X(110), 250, 1)
    o += bench(X(80), 460) + person(X(70), 452, '#3F6FA8', 3, '#1E1A18', s=.95, glasses=True) + open_book(X(72), 420, .45)
    o += ball(X(140), 520, 11) + person(X(40), 600, '#E2574C', 2, '#B58A3C', pose='wave', hs='long', skirt=True, begin=.3)
    o += umbrella(X(350), 340, 1, '#3F6FA8') + tree(X(370), 520, .8) + tree(X(30), 700, .9, kind='round', fruit='#E2574C')
    o += bubble(X(90), 540, 'Che tempo fa?', '#fff', side=0, size=11) + bubble(X(330), 640, 'Piove!', '#E9F2FB', side=0, size=11)
    o += camera(X(140), 690, .9)
    return done(bg, o, 'trail', '#DFF0DA')


# 10 · Che cosa hai fatto?
def s10():
    m, X = mk(10)
    o = '<rect width="400" height="700" fill="#FFF8E7"/>' + ''.join(f'<path d="M0 {y} H400" stroke="#BFD9EE" stroke-width="1.2"/>' for y in range(40, 700, 28))
    o += '<path d="M44 0 V700" stroke="#F2A1A1" stroke-width="1.5"/>' if m == 1 else '<path d="M356 0 V700" stroke="#F2A1A1" stroke-width="1.5"/>'
    bg, o = o, ''
    o += calendar(X(330), 110, 1, '11') + txt(X(330), 128, 'IERI', 11, '#E2574C') + calendar(X(330), 330, 1, '12') + txt(X(330), 348, 'OGGI', 11, '#3F6FA8')
    o += calendar(X(330), 560, 1, '13') + txt(X(330), 578, 'DOMANI', 11, '#2F7A4E')
    o += camera(X(280), 180, .9) + ticket(X(370), 210, .9, 'CINEMA', '#FFC94A', 12) + ticket(X(290), 260, .8, 'MUSEO', '#9ED3F0', -8)
    o += person(X(300), 470, '#3F6FA8', 1, pose='wave', face=-m, begin=.2) + bubble(X(320), 390, 'Ho visto un film!', '#fff', side=0, size=11)
    o += pencil(X(360), 640, 1.2, -40) + bubble(X(300), 660, 'Domani studio.', '#E8F4EC', side=0, size=11)
    o += frame(X(250) - 22, 40, 44, 34)
    return done(bg, o, 'paper', '#FFF8E7')


# 11 · Ieri e oggi (una giornata a Firenze)
def s11():
    m, X = mk(11)
    o = sky('#F7D7A8', '#FBEFD9', 330) + sun(X(80), 70, 24, '#FFB25B')
    o += '<path d="M0 230 Q90 170 180 210 Q270 160 400 200 V330 H0 Z" fill="#C9D9A0"/>' + '<rect y="300" width="400" height="400" fill="#EBD9BC"/>'
    o += dome(200, 300, 1) + ''.join(cypress(x, 240, .7) for x in (30, 60, 340, 370))
    o += ''.join(f'<path d="M0 {y} H400" stroke="#DFCAA6" stroke-width="1.4"/>' for y in range(330, 700, 34))
    bg, o = o, ''
    o += person(X(50), 400, '#E2574C', 2, '#6B3E1E', pose='hold', hs='long', face=m) + camera(X(62), 352, .6)
    o += person(X(100), 400, '#3F6FA8', 0, '#B58A3C', pose='point', face=m, glasses=True) + bubble(X(80), 316, 'Che bella Firenze!', '#fff', side=0, size=11)
    o += clock(X(60), 470, 20, 9, 0) + txt(X(60), 506, 'IERI', 10, '#8A5A3B') + clock(X(120), 470, 20, 4, 0, True) + txt(X(120), 506, 'OGGI', 10, '#8A5A3B')
    o += cafe_table(X(70), 620, 1, 2) + person(X(130), 620, '#5BAA6A', 1, pose='hold', face=-m, hs='bun', skirt=True) + cornetto(X(50), 576, .8)
    o += suitcase(X(360), 680, '#3F6FA8') + flowerpot(X(370), 360, '#C77DBA')
    return done(bg, o, 'stone', '#F1E2C8')


# 12 · Da bambino (campagna)
def s12():
    m, X = mk(12)
    o = env_country(240) + sun(X(330), 60, 22) + cloud(X(120), 70, .9)
    o += farmhouse(X(320), 250, .9)
    bg, o = o, ''
    o += tree(X(350), 370, .9, fruit='#E2574C') + hay(X(300), 450) + chicken(X(360), 470, 1, -m) + chicken(X(330), 490, .8, m)
    o += person(X(300), 580, '#FFC94A', 1, '#5E3E28', pose='wave', s=.75, hs='curly', begin=.1) + person(X(350), 580, '#C77DBA', 2, '#3A2A1E', pose='wave', s=.72, hs='long', skirt=True, begin=.5)
    o += ball(X(320), 610, 9) + kite(X(260), 160, .9, '#3F6FA8')
    o += bubble(X(300), 510, 'Da bambino giocavo qui!', '#fff', side=0, size=10)
    o += dog(X(250), 680, .9, -m) + clothesline(X(250) - 55, 640, 110)
    return done(bg, o, 'trail', '#E4F1D6')


# 13 · Una storia (un rumore strano di notte)
def s13():
    m, X = mk(13)
    o = env_night('#1B2550', '#3A4682') + '<path d="M0 420 Q200 380 400 420 V700 H0 Z" fill="#26375F"/>'
    o += house_small(X(80), 420, 1.5, '#E6D3B3', '#8A4A3B', True)
    bg, o = o, ''
    o += owl(X(150), 320, 1) + '<path d="M%s 330 H%s" stroke="#4A3A2E" stroke-width="5"/>' % (X(120), X(185))
    o += pine(X(30), 520, 1) + pine(X(380), 640, .8)
    o += person(X(80), 600, '#3F6FA8', 1, pose='point', face=m, hs='curly')
    o += f'<path d="M{X(96)} 560 L{X(170)} 520 L{X(176)} 580 Z" fill="#FFF3B0" opacity=".55"/>'
    o += bubble(X(90), 470, "Che cos'era?", '#FFF3C4', side=0, size=11)
    o += txt(X(60), 690, 'BUM!', 16, '#FFC94A', extra='transform="rotate(-12 %s 690)"' % X(60))
    o += '<g opacity=".8">' + ''.join(f'<text x="{X(40) + i * 14 * m}" y="{240 - i * 16}" font-size="{12 + i * 3}" fill="#BFD0FF" font-family="Nunito,Arial" font-weight="900">z</text>' for i in range(3)) + '</g>'
    return done(bg, o, 'trail', '#2C3E73', True)


# 14 · In viaggio (stazione, albergo)
def s14():
    m, X = mk(14)
    o = sky('#BFE4F7', '#EAF2F6', 300) + '<rect y="240" width="400" height="460" fill="#D6D9DE"/>'
    o += '<path d="M0 120 L200 70 L400 120 V140 H0 Z" fill="#9AA6B8"/>' + ''.join(f'<rect x="{x}" y="140" width="6" height="100" fill="#9AA6B8"/>' for x in (20, 120, 274, 374))
    o += '<rect y="330" width="400" height="12" fill="#7A5B3F"/>' + ''.join(f'<rect x="{x}" y="326" width="6" height="20" fill="#5E3E28"/>' for x in range(0, 400, 20))
    o += train(200, 330, 1, '#E2574C')
    bg, o = o, ''
    o += board(X(330), 210, (('ROMA', '10:15'), ('VENEZIA', '10:40'), ('NAPOLI', '11:05')), .9) + clock(X(370), 90, 16, 10, 10, True)
    o += person(X(320), 470, '#5BAA6A', 1, pose='hold', face=-m, hs='long') + suitcase(X(350), 470, '#3F6FA8') + ticket(X(270), 420, .8, 'TRENO', '#FFC94A')
    o += bubble(X(300), 390, 'Un biglietto, per favore', '#fff', side=0, size=10)
    o += hotel(X(330), 690, .7) + key(X(260), 650, 1)
    o += person(X(270), 690, '#C77DBA', 3, '#1E1A18', pose='wave', face=-m, glasses=True, begin=.3)
    return done(bg, o, 'rail', '#E3E7EC')


# 15 · Dal medico
def s15():
    m, X = mk(15)
    o = '<rect width="400" height="700" fill="#EAF6F8"/><rect y="320" width="400" height="380" fill="#DCEFF2"/>' + clinic(X(80), 320, 1.1)
    o += ''.join(f'<path d="M0 {y} H400" stroke="#C7E2E8" stroke-width="2"/>' for y in range(360, 700, 40))
    bg, o = o, ''
    o += doctor(X(60), 450, 1, 0, m, 'bun', hair='#6B3E1E') + doctor(X(150), 680, .95, 3, -m, 'short', hair='#1E1A18')
    o += person(X(110), 450, '#F2B880', 2, pose='point', face=-m, beard=True) + thermo(X(122), 400, 1, 30)
    o += bubble(X(90), 370, 'Mi fa male la testa', '#fff', side=0, size=10)
    o += pill_bottle(X(40), 560) + bubble(X(90), 600, 'Due volte al giorno', '#E8F4EC', side=0, size=10)
    o += bench(X(345), 300, .9) + bench(X(345), 520, .9) + plant(X(365), 700)
    o += clipboard(X(40), 690, .9)
    return done(bg, o, 'hall', '#E1F1F4')


# 16 · Facciamo shopping
def s16():
    m, X = mk(16)
    o = '<rect width="400" height="700" fill="#FBEFF3"/><rect y="320" width="400" height="380" fill="#F1DCE4"/>'
    o += shopfront(X(320) - 70, 300, 140, 'MODA', '#F6D9E3', ('#C77DBA', '#fff'))
    bg, o = o, ''
    o += rack(X(320), 450) + mannequin(X(370), 450, 1, '#E2574C')
    o += mirror(X(260), 450) + person(X(320), 640, '#C77DBA', 2, '#6B3E1E', pose='hold', hs='long', skirt=True, legs='#3F6FA8', face=-m)
    o += bag(X(270), 690, 1, '#E2574C', False) + bag(X(370), 690, .9, '#3F6FA8', False)
    o += bubble(X(320), 560, 'Posso provarlo?', '#fff', side=0, size=11) + tag(X(370), 330, '-30%', '#E2574C') + tag(X(260), 330, 'TAGLIA M', '#5BAA6A')
    o += person(X(370), 140, '#3F6FA8', 1, pose='point', face=-m, glasses=True) + bubble(X(300), 70, 'Quanto costa?', '#FFF3C4', side=0, size=11)
    return done(bg, o, 'tiles', '#F7E3EA')


# 17 · A tavola (ristorante)
def s17():
    m, X = mk(17)
    o = '<rect width="400" height="700" fill="#F6E3C8"/><rect y="300" width="400" height="400" fill="#B97A4E"/>'
    o += ''.join(f'<path d="M0 {y} H400" stroke="#8A5A3B" stroke-width="2"/>' for y in range(330, 700, 30))
    o += awning(0, 220, 400, '#2F7A4E', '#fff', 16) + '<rect y="200" width="400" height="20" fill="#26323A"/>' + txt(200, 215, 'TRATTORIA DA MARIO', 13, '#fff')
    o += window_(X(40) if m == 1 else 270, 60, 90, 100)
    bg, o = o, ''

    def tavolo(x, y):
        return (f'<g transform="translate({x} {y})"><ellipse cx="0" cy="0" rx="50" ry="14" fill="#fff"/><path d="M-50 0 L-46 30 L46 30 L50 0" fill="#E2574C"/>'
                + ''.join(f'<rect x="{-46 + i * 12}" y="2" width="6" height="28" fill="#fff" opacity=".8"/>' for i in range(8)) + '</g>')
    o += tavolo(X(80), 400) + plate_pasta(X(60), 398) + wine_glass(X(100), 398) + candle(X(80), 390)
    o += person(X(30), 440, '#5B4A6B', 1, pose='hold', s=.9, face=m, hs='long')
    o += tavolo(X(90), 600) + pizza(X(80), 596, .9) + wine_glass(X(116), 598, 1, '#F3E2A0') + bottle(X(50), 598, .8, '#3E8A52')
    o += person(X(160), 560, '#fff', 2, '#1E1A18', pose='hold', face=-m, beard=True) + bubble(X(120), 480, 'Buon appetito!', '#FFF3C4', side=0, size=11)
    o += bubble(X(70), 320, 'Il conto, per favore', '#fff', side=0, size=10)
    o += plant(X(370), 690)
    return done(bg, o, 'plank', '#EFD8BB')


# 18 · Chi è più alto?
def s18():
    m, X = mk(18)
    o = env_park('#D7EEFA', '#F1F8EC', '#BFE1A9', '#AED596', 260) + sun(X(60), 60, 20) + cloud(X(200), 70, .8)
    bg, o = o, ''
    ruler = ''.join(f'<path d="M0 {-i * 10} h{8 if i % 5 == 0 else 4}" stroke="#26323A" stroke-width="1.5"/>' for i in range(16))
    o += f'<g transform="translate({X(250)} 450)"><rect x="-4" y="-160" width="16" height="160" fill="#FFE59A"/>{ruler}</g>'
    o += person(X(290), 450, '#3F6FA8', 1, pose='stand', s=1.35, face=-m, glasses=True) + person(X(340), 450, '#E2574C', 2, '#6B3E1E', pose='wave', s=.95, face=-m, hs='bun', skirt=True)
    o += person(X(380), 450, '#FFC94A', 0, '#B58A3C', s=.7, hs='curly', pose='wave', begin=.4)
    o += bubble(X(300), 300, 'Sono più alto di te!', '#fff', side=0, size=10)
    o += person(X(300), 650, '#5BAA6A', 3, '#1E1A18', hs='long', s=1, face=-m) + person(X(350), 650, '#C77DBA', 1, '#D9A35A', hs='curly', s=1, face=m, pose='wave')
    o += bubble(X(320), 560, 'Ha i capelli ricci', '#E8F4EC', side=0, size=10) + tree(X(370), 340, .7)
    return done(bg, o, 'stone', '#E2F1DA')


# 19 · Lavoro e studio
def s19():
    m, X = mk(19)
    o = '<rect width="400" height="700" fill="#EEF1F5"/><rect y="320" width="400" height="380" fill="#D9DEE6"/>'
    o += whiteboard(X(46) if m == 1 else 250, 90, 110, 80, ('Lavoro:', 'medico', 'architetta'))
    o += window_(X(260) - 45, 80, 90, 100, '#BFE4F7', '#3F6FA8')
    bg, o = o, ''
    o += desk(X(80), 420) + laptop(X(80), 374) + cup(X(130), 378, .7, True) + chair(X(50), 440, 1, '#3B4F6B', m)
    o += person(X(40), 450, '#3F6FA8', 1, pose='hold', s=.95, face=m, hs='short', glasses=True)
    o += briefcase(X(140), 450) + bubble(X(90), 300, 'Che lavoro fai?', '#fff', side=0, size=11)
    o += person(X(60), 640, '#C77DBA', 2, '#6B3E1E', pose='wave', hs='long', face=m) + cap(X(60), 570, .8) + books(X(120), 640)
    o += bubble(X(110), 690, 'Studio ingegneria', '#E8F4EC', side=0, size=10) + plant(X(370), 690)
    return done(bg, o, 'hall', '#E4E8EE')


# 20 · Ci vediamo!
def s20():
    m, X = mk(20)
    o = sky('#F7B58A', '#6E6AA8', 360) + '<rect y="330" width="400" height="370" fill="#4C4E72"/>'
    o += ''.join(f'<rect x="{x}" y="{330 - h}" width="{w}" height="{h}" fill="#3B3F66"/>' for x, w, h in ((0, 60, 120), (60, 50, 90), (300, 50, 100), (350, 50, 140)))
    o += ''.join(f'<rect x="{x}" y="{y}" width="8" height="10" fill="#FFD66B"/>' for x, y in ((14, 230), (34, 260), (74, 260), (314, 250), (366, 210), (366, 250)))
    o += moon(X(330), 70, 18)
    bg, o = o, ''
    o += person(X(300), 470, '#E2574C', 1, pose='hold', face=-m, hs='curly') + phone(X(316), 420, .7)
    o += bubble(X(320), 380, 'Ci vediamo alle 8?', '#fff', side=0, size=11)
    o += person(X(330), 660, '#5BAA6A', 2, '#6B3E1E', pose='wave', hs='long', face=-m, begin=.3) + bubble(X(320), 580, 'Va bene, a dopo!', '#FFF3C4', side=0, size=11)
    o += ticket(X(260), 520, .9, 'CINEMA', '#FFC94A', -14) + calendar(X(352), 300, .9, 'SAB')
    o += lamp(X(380), 700) + lamp(X(380), 470, .9)
    return done(bg, o, 'road', '#9C8FC4', True)


# 21 · Vorrei, potrei… (la casa dei sogni)
def s21():
    m, X = mk(21)
    o = env_sea(320) + sun(X(330), 70, 22) + cloud(X(240), 80, .8)
    bg, o = o, ''
    o += boat(X(60), 380, 1) + boat(X(130), 410, .7, '#3F6FA8')
    inner = house_small(0, 34, .9, '#fff', '#3F6FA8') + tree(36, 34, .4) + sun(-34, -20, 8)
    o += bubble_think(X(100), 200, inner, 120, 90)
    o += person(X(40), 620, '#FFC94A', 1, pose='point', face=m, hs='curly') + bubble(X(112), 540, 'Vorrei una casa al mare…', '#fff', side=0, size=10)
    o += f'<g transform="translate({X(110)} 640)"><path d="M-14 0 L0 -60 L14 0 Z" fill="#E2574C"/><path d="M-14 0 Q0 -10 14 0" fill="#fff"/></g>' + umbrella(X(130), 640, 1.2, '#E2574C')
    o += ball(X(80), 690, 9, '#3F6FA8') + tree(X(360), 680, .8, kind='olive')
    return done(bg, o, 'plank', '#D6ECF6')


# 22 · Si accomodi! (banca)
def s22():
    m, X = mk(22)
    o = '<rect width="400" height="700" fill="#F2EEE6"/><rect y="330" width="400" height="370" fill="#D9CFBE"/>'
    o += ''.join(column(x, 330, 200, .9) for x in (40, 360)) + '<path d="M0 120 L200 50 L400 120 Z" fill="#E6DCC9"/>' + txt(200, 108, 'BANCA', 18, '#8A5A3B', weight=900)
    bg, o = o, ''
    o += f'<rect x="{X(400) if m == -1 else 0}" y="380" width="0" height="0"/>'
    o += f'<g transform="translate({X(320)} 470)"><rect x="-70" y="-40" width="140" height="40" fill="#8A5A3B"/><rect x="-74" y="-46" width="148" height="8" fill="#5E3E28"/><rect x="-60" y="-120" width="120" height="74" fill="#DCEBF5" opacity=".5"/></g>'
    o += person(X(320), 430, '#3B4F6B', 1, pose='wave', face=-m, glasses=True) + bubble(X(300), 330, 'Buongiorno, si accomodi!', '#fff', side=0, size=10)
    o += person(X(270), 650, '#C77DBA', 2, '#6B3E1E', pose='hold', face=-m, hs='bun', skirt=True) + coins(X(330), 640) + atm(X(370), 690, .9)
    o += bubble(X(300), 560, 'Vorrei aprire un conto', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'hall', '#EAE3D6')


# 23 · Te lo dico io (prestare e restituire)
def s23():
    m, X = mk(23)
    o = '<rect width="400" height="700" fill="#F3E7D8"/>' + ''.join(f'<rect x="0" y="{y}" width="400" height="6" fill="#E6D5BF"/>' for y in range(320, 700, 46))
    o += f'<rect x="{X(30) - (0 if m == 1 else 60)}" y="120" width="60" height="200" fill="#8A5A3B"/><circle cx="{X(80) - (0 if m == 1 else 60)}" cy="230" r="3" fill="#C9A24A"/>'
    o += f'<rect x="{X(220) - 40}" y="80" width="80" height="60" fill="#fff" stroke="#C9CFD6"/>' + txt(X(220), 116, 'Interno 4', 11, '#5B6676')
    bg, o = o, ''
    o += person(X(40), 450, '#5BAA6A', 1, pose='hold', face=m, hs='curly') + books(X(80), 420, .6)
    o += person(X(120), 450, '#E2574C', 2, '#6B3E1E', pose='hold', face=-m, hs='long')
    o += bubble(X(70), 340, 'Me lo presti?', '#fff', side=0, size=11) + bubble(X(110), 520, 'Te lo do domani!', '#FFF3C4', side=0, size=11)
    o += umbrella(X(40), 690, 1, '#3F6FA8') + key(X(100), 670, 1) + camera(X(150), 690, .8)
    o += plant(X(370), 690) + mailbox(X(370), 320, .8)
    return done(bg, o, 'plank', '#EEDFCB')


# 24 · La persona che… (il mio quartiere)
def s24():
    m, X = mk(24)
    o = env_street('#CDEBFA', '#FBEFD9', '#E3DCCD', y0=250)
    bg, o = o, ''
    o += apartment(X(330), 360, .8) + kiosk(X(320), 560, .9)
    o += person(X(250), 560, '#C77DBA', 1, pose='wave', face=-m, old=True, hs='bun', skirt=True) + bubble(X(290), 440, 'La signora che vive qui', '#fff', side=0, size=10)
    o += person(X(370), 690, '#3F6FA8', 3, '#1E1A18', pose='hold', face=-m) + newspaper(X(380), 650, .5)
    o += dog(X(280), 690, .9, -m) + lamp(X(260), 380) + tree(X(380), 420, .7)
    o += shopfront(X(320) - 45, 160, 90, 'PANETTERIA', '#F6E2B8', ('#B97A4E', '#fff'))
    o += bread(X(260), 690)
    return done(bg, o, 'stone', '#EFE6D6')


# 25 · Penso che…
def s25():
    m, X = mk(25)
    o = env_park('#E2F0FA', '#F2F6E8', '#C8E2B1', '#BAD9A2', 260) + cloud(X(260), 60, .9) + sun(X(330), 50, 18)
    bg, o = o, ''
    o += cafe_table(X(80), 470, 1.1, 2) + person(X(30), 470, '#3F6FA8', 1, pose='point', face=m, glasses=True) + person(X(140), 470, '#E2574C', 2, '#6B3E1E', pose='hold', face=-m, hs='long')
    o += bubble_think(X(60), 300, check(-26, 0, True) + txt(10, 5, 'Sì!', 14, '#2F7A4E', weight=900), 100, 60)
    o += bubble_think(X(130), 180, check(-26, 0, False) + txt(10, 5, 'Mah…', 14, '#B03A4A', weight=900), 100, 60)
    o += bubble(X(80), 560, 'Penso che sia vero', '#fff', side=0, size=11) + bubble(X(100), 610, 'Secondo me, no', '#FFF3C4', side=0, size=11)
    o += tree(X(40), 700, .9, kind='round') + bench(X(360), 690)
    return done(bg, o, 'trail', '#E3F0DB')


# 26 · Prima e dopo (una giornata storta)
def s26():
    m, X = mk(26)
    o = sky('#AEB8C8', '#DDE3EA', 330) + '<rect y="300" width="400" height="400" fill="#BFC6CF"/>'
    o += ''.join(f'<rect x="{x}" y="{300 - h}" width="{w}" height="{h}" fill="#9AA6B8"/>' for x, w, h in ((0, 70, 140), (70, 50, 100), (290, 60, 120), (350, 50, 160)))
    bg, o = o, ''
    o += raincloud(X(320), 120, 1.1) + raincloud(X(260), 200, .8)
    o += bus(X(318), 390, .9) + txt(X(318), 410, 'ops!', 13, '#B03A4A')
    o += person(X(300), 520, '#E2574C', 1, pose='wave', face=-m, hs='curly') + umbrella(X(330), 500, 1, '#3F6FA8', True)
    o += bubble(X(300), 440, 'Che giornataccia!', '#fff', side=0, size=11)
    o += alarm(X(370), 600, .9) + cup(X(270), 640, 1, False) + f'<path d="M{X(282)} 640 q20 6 36 -2 q10 8 -6 10 z" fill="#8A5A3B" opacity=".6"/>'
    o += bubble(X(320), 690, 'Prima di uscire…', '#FFF3C4', side=0, size=10)
    return done(bg, o, 'road', '#D3D9E1')


# 27 · Se posso, vengo (il ponte)
def s27():
    m, X = mk(27)
    o = sky('#BFE4F7', '#F4EAD8', 300) + '<rect y="300" width="400" height="400" fill="#6FB6DD"/>'
    o += ''.join(f'<path d="M{x} {y} q8 -4 16 0 q8 4 16 0" stroke="#BFE4F7" stroke-width="2.5" fill="none"/>' for x, y in ((30, 360), (200, 420), (300, 340), (90, 520), (320, 600), (40, 650)))
    o += facade(0, 150, 80, 150, '#E8C08A', rows=3) + facade(320, 140, 80, 160, '#E59A6F', rows=3, shut='#3F6FA8')
    o += bridge(200, 310, 320, '#E6CFA6')
    bg, o = o, ''
    o += boat(X(60), 440, 1.1, '#E2574C') + boat(X(110), 620, .9, '#FFC94A')
    o += person(X(70), 280, '#3F6FA8', 1, pose='wave', s=.8, face=m) + person(X(110), 280, '#C77DBA', 2, '#6B3E1E', pose='wave', s=.8, hs='long', face=-m, begin=.3)
    o += bubble(X(90), 200, 'Se posso, vengo!', '#fff', side=0, size=11) + sun(X(330), 60, 20)
    return done(bg, o, 'plank', '#CFE7F3')


# 28 · Si dice che… (notizie, tecnologia)
def s28():
    m, X = mk(28)
    o = env_street('#CDE0F7', '#EEF2F8', '#DCDFE5', ('#C9D2E3', '#E3C9B8', '#BFD6CF', '#D8C9E3'), y0=250)
    bg, o = o, ''
    o += kiosk(X(320), 420, 1) + tv(X(330), 600, 1.1) + txt(X(330), 556, 'TG', 12, '#fff')
    o += person(X(260), 680, '#3F6FA8', 1, pose='hold', face=-m, glasses=True) + phone(X(274), 636, .6) + wifi(X(250), 610)
    o += person(X(360), 690, '#5BAA6A', 2, '#6B3E1E', hs='long', face=-m, pose='hold') + newspaper(X(366), 650, .5)
    o += bubble(X(310), 290, 'Si dice che…', '#fff', side=0, size=11) + bubble(X(320), 500, 'Hai letto la notizia?', '#FFF3C4', side=0, size=10)
    o += laptop(X(345), 300, .8)
    return done(bg, o, 'road', '#E1E6EE')


# 29 · Scrivere bene (email e messaggi)
def s29():
    m, X = mk(29)
    o = '<rect width="400" height="700" fill="#F5F1E8"/>' + ''.join(f'<path d="M0 {y} H400" stroke="#E3DACA" stroke-width="1"/>' for y in range(30, 700, 26))
    bg, o = o, ''
    o += desk(X(80), 330) + laptop(X(80), 284) + cup(X(130), 288, .7, True)
    o += person(X(40), 360, '#E2574C', 1, pose='hold', s=.95, face=m, hs='bun') + bubble(X(80), 200, 'Gentile dottoressa…', '#fff', side=0, size=10)
    o += envelope(X(50), 470) + envelope(X(110), 500, .8, '#FFF3C4') + mailbox(X(130), 640) + phone(X(50), 640, 1)
    o += bubble(X(90), 560, 'Cordiali saluti', '#E8F4EC', side=0, size=11) + pencil(X(60), 690, 1, -20)
    o += f'<path d="M{X(160)} 430 q30 -40 60 0" stroke="#9AA6B8" stroke-width="2" stroke-dasharray="4 5" fill="none"/>'
    return done(bg, o, 'paper', '#F5F1E8')


# 30 · Credevo che… (il primo giorno)
def s30():
    m, X = mk(30)
    o = sky('#D7ECFA', '#F4F7FB', 330) + '<rect y="300" width="400" height="400" fill="#E2E5EA"/>'
    o += f'<rect x="{X(330) - 70}" y="60" width="140" height="240" fill="#B8C9DE"/>' + ''.join(f'<rect x="{X(330) - 60 + c * 32}" y="{74 + r * 36}" width="24" height="26" fill="#E3EEF8"/>' for r in range(6) for c in range(4))
    bg, o = o, ''
    o += person(X(300), 450, '#3F6FA8', 1, pose='hold', face=-m, hs='short') + briefcase(X(330), 450)
    o += bubble_think(X(310), 350, txt(0, 5, 'Credevo che fosse…', 10, '#26323A'), 130, 44)
    o += person(X(360), 640, '#C77DBA', 2, '#6B3E1E', pose='wave', face=-m, hs='long', begin=.3) + bubble(X(320), 560, 'Benvenuto in ufficio!', '#FFF3C4', side=0, size=10)
    o += clock(X(370), 300, 18, 9, 0) + plant(X(270), 690)
    return done(bg, o, 'hall', '#E6EBF1')


# 31 · Se fossi… (tornare indietro nel tempo)
def s31():
    m, X = mk(31)
    o = sky('#4A3F7A', '#C97FA0', 700)
    o += ''.join(star(x, y, .8, b) for x, y, b in ((40, 50, 0), (330, 90, .6), (250, 30, 1.2), (370, 300, .4), (20, 400, 1)))
    o += '<circle cx="200" cy="360" r="190" fill="none" stroke="#fff" stroke-opacity=".12" stroke-width="30"/>'
    bg, o = o, ''
    o += clock(X(70), 120, 34, 10, 10, True) + clock(X(140), 220, 20, 3, 40, True)
    o += castle(X(70), 420, .8) + column(X(150), 420, 100, .7)
    o += person(X(60), 600, '#FFC94A', 1, pose='point', face=m, hs='curly', glasses=True) + bubble(X(104), 520, 'Se fossi nel 1500…', '#fff', side=0, size=10)
    o += scroll(X(130), 690, .8) + txt(X(130), 300, '1492', 16, '#FFF3C4', weight=900)
    return done(bg, o, 'ink', '#8E6FA8', True)


# 32 · È stato detto (il quadro ritrovato)
def s32():
    m, X = mk(32)
    o = '<rect width="400" height="700" fill="#F2ECE2"/><rect y="340" width="400" height="360" fill="#C8A57E"/>'
    o += ''.join(f'<path d="M{x} 340 V700" stroke="#B48F66" stroke-width="2"/>' for x in range(0, 400, 40))
    o += gallery_frame(X(330) - 40, 80, 80, 100, 'sun') + gallery_frame(X(250) - 25, 110, 50, 60, 'sea')
    bg, o = o, ''
    o += easel(X(320), 470, 1) + person(X(370), 470, '#fff', 2, '#3A2A1E', pose='hold', face=-m, glasses=True, hs='bun')
    o += magnifier(X(270), 420, .8) + bubble(X(300), 300, 'È stato restaurato!', '#fff', side=0, size=10)
    o += flyer(X(300), 640, ('AFFITTASI', 'bilocale'), 1, -6) + flyer(X(345), 690, ('CERCASI', 'restauratore'), .85, 5)
    return done(bg, o, 'carpet', '#EDE4D6')


# 33 · Disse che… (il colloquio)
def s33():
    m, X = mk(33)
    o = '<rect width="400" height="700" fill="#EDEFF3"/><rect y="320" width="400" height="380" fill="#CFD5DE"/>' + window_(X(50) - 45 if m == 1 else 300, 80, 90, 100, '#BFE4F7', '#5B6676')
    bg, o = o, ''
    o += desk(X(80), 450) + clipboard(X(60), 404, .7) + laptop(X(110), 404, .7)
    o += person(X(30), 470, '#3B4F6B', 1, pose='hold', face=m, glasses=True, beard=True) + person(X(150), 470, '#C77DBA', 2, '#6B3E1E', pose='point', face=-m, hs='long')
    o += bubble(X(100), 330, 'Disse: «Sono pronta»', '#fff', side=0, size=10)
    o += bubble(X(100), 560, 'Disse che era pronta', '#FFF3C4', side=0, size=10)
    o += briefcase(X(150), 690) + plant(X(40), 690)
    return done(bg, o, 'hall', '#E1E5EC')


# 34 · C'era una volta (favola)
def s34():
    m, X = mk(34, True)
    o = sky('#F6D6E8', '#E7F2E1', 320) + '<path d="M0 260 Q100 220 200 250 T400 240 V700 H0 Z" fill="#B9DDA2"/>'
    o += castle(X(320), 260, .8) + ''.join(pine(x, y, s) for x, y, s in ((20, 330, 1), (60, 340, .8), (380, 330, .9)))
    bg, o = o, ''
    o += pinocchio(X(80), 460, 1.1) + bubble(X(80), 360, 'Non ho detto bugie!', '#fff', side=0, size=10)
    o += wolf(X(80), 620, 1.1, m) + pine(X(150), 560, .8) + pine(X(30), 700, .9)
    o += open_book(X(130), 690, .8) + txt(X(80), 300, "C'era una volta…", 13, '#7A5B8A', extra='font-style="italic"')
    o += star(X(160), 200, .9) + star(X(40), 230, .7, .5)
    return done(bg, o, 'trail', '#EFE7EE')


# 35 · Benché, purché… (cercasi coinquilino)
def s35():
    m, X = mk(35)
    o = env_room('#EAF0F4', '#C8A57E', 310, True, X(40) if m == 1 else 270)
    bg, o = o, ''
    o += boxes(X(60), 420, 1.1) + flyer(X(130), 300, ('CERCASI', 'COINQUILINO'), .9)
    o += person(X(50), 600, '#5BAA6A', 1, pose='point', face=m, hs='curly') + person(X(120), 600, '#E2574C', 3, '#1E1A18', pose='hold', face=-m, hs='long', skirt=True)
    o += bubble(X(100), 510, 'Purché sia ordinato!', '#fff', side=0, size=10)
    o += key(X(40), 680, 1) + plant(X(130), 690) + armchair(X(370), 690, .9)
    return done(bg, o, 'plank', '#E8EDF0')


# 36 · Parole che crescono (formazione delle parole)
def s36():
    m, X = mk(36)
    o = '<rect width="400" height="700" fill="#FFF7E6"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#F2D9A8"/>' for x in range(20, 400, 40) for y in range(20, 700, 40))
    bg, o = o, ''
    o += letter_blocks(250, 140, 'GATTO', .85) + letter_blocks(228, 240, 'GATTINO', .75)
    o += f'<g transform="translate({X(320)} 300)">' + '<ellipse cx="0" cy="-10" rx="18" ry="11" fill="#F2B880"/><circle cx="14" cy="-24" r="10" fill="#F2B880"/><path d="M8 -32 l3 -9 l4 7 M16 -33 l4 -8 l2 9" fill="#F2B880"/><circle cx="17" cy="-25" r="1.5" fill="#26323A"/><path d="M-18 -12 q-14 -6 -10 -22" stroke="#F2B880" stroke-width="5" fill="none" stroke-linecap="round"/></g>'
    o += letter_blocks(250, 440, 'LIBRO', .85) + letter_blocks(228, 540, 'LIBRONE', .75)
    o += books(X(330), 620, 1.4) + txt(X(300), 380, '-ino -one -etto -accio', 11, '#8A5A3B') + pencil(X(360), 690, 1)
    return done(bg, o, 'paper', '#FFF4DE')


# 37 · Dire la propria (dibattito)
def s37():
    m, X = mk(37)
    o = '<rect width="400" height="700" fill="#2E3A5A"/>' + curtain_stage(400, 0, 700, '#8A2E3B') + '<rect y="560" width="400" height="140" fill="#5E3E28"/>'
    o += '<circle cx="200" cy="300" r="180" fill="#FFF3C4" opacity=".08"/>'
    bg, o = o, ''
    o += podium(X(70), 420, 1, '#3F6FA8') + person(X(70), 360, '#E2574C', 1, pose='point', s=.85, face=m, hs='long')
    o += bubble(X(90), 250, 'Secondo me…', '#fff', side=0, size=11)
    o += podium(X(80), 680, 1, '#2F7A4E') + person(X(80), 620, '#FFC94A', 2, pose='point', s=.85, face=m, glasses=True, beard=True)
    o += bubble(X(90), 510, 'Non sono d\'accordo!', '#FFF3C4', side=0, size=10) + microphone(X(150), 600, .8)
    return done(bg, o, 'carpet', '#55507A', True)


# 38 · Questione di registro (il condominio)
def s38():
    m, X = mk(38)
    o = sky('#D7ECFA', '#F4EEE4', 300) + '<rect y="290" width="400" height="410" fill="#E3D9C8"/>' + apartment(200, 300, 1.2, '#F0D2B0', 5)
    bg, o = o, ''
    o += noticeboard(X(340), 420, 1) + txt(X(340), 340, 'AVVISO', 11, '#B03A4A')
    o += person(X(270), 600, '#3B4F6B', 1, pose='point', face=-m, old=True, glasses=True, beard=True) + bubble(X(300), 500, 'Gentili condòmini…', '#fff', side=0, size=10)
    o += person(X(360), 600, '#5BAA6A', 2, '#6B3E1E', pose='wave', face=-m, hs='curly') + bubble(X(318), 680, 'Ciao, come va?', '#FFF3C4', side=0, size=10)
    o += mailbox(X(380), 700, .8) + plant(X(260), 700)
    return done(bg, o, 'stone', '#EEE6D9')


# 39 · La frase marcata (al mercato: «Le fragole le prendo io»)
def s39():
    m, X = mk(39)
    o = env_street('#CDEBFA', '#FCEFD9', '#EADFC9', ('#F2B880', '#F6D27A', '#E8846B', '#D9B48F'), y0=230)
    bg, o = o, ''
    o += stall(X(70), 380, 1.05, '#C77DBA')
    o += f'<g transform="translate({X(70)} 334)">' + ''.join(f'<path d="M{-50 + i * 14} 0 q-6 -12 0 -16 q6 4 0 16 Z" fill="#E2574C"/>' for i in range(8)) + '</g>'
    o += person(X(60), 560, '#3F6FA8', 1, pose='point', face=m, hs='bun', skirt=True) + bubble(X(105), 470, 'Le fragole le prendo io!', '#fff', side=0, size=10)
    o += person(X(140), 560, '#F2B880', 3, '#1E1A18', pose='hold', face=-m, beard=True) + bag(X(140), 690)
    o += bubble(X(90), 640, 'È lui che le vende', '#FFF3C4', side=0, size=10) + crate(X(40), 690, '#FFC94A') + crate(X(360), 690, '#5BAA6A')
    return done(bg, o, 'stone', '#F1E5D2')


# 40 · Dire molto con poco (il verbale, l'ispezione)
def s40():
    m, X = mk(40)
    o = '<rect width="400" height="700" fill="#EEF0EC"/><rect y="320" width="400" height="380" fill="#D7DBD2"/>' + apartment(X(330), 320, .9, '#E6D9C6')
    bg, o = o, ''
    o += person(X(270), 520, '#2F4F86', 1, pose='hold', face=-m, glasses=True) + clipboard(X(296), 480, .7)
    o += bubble(X(310), 420, 'Sopralluogo: ore 10', '#fff', side=0, size=10)
    o += stamp_(X(285), 640, 1, 'VISTO') + f'<g transform="translate({X(320)} 690)"><rect x="-50" y="-40" width="100" height="40" fill="#fff" stroke="#C9CFD6"/>' + txt(0, -24, 'VERBALE', 10, '#26323A') + ''.join(f'<path d="M-40 {-16 + i * 6} H40" stroke="#C9CFD6" stroke-width="2"/>' for i in range(3)) + '</g>'
    o += txt(X(300), 590, 'Breve. Chiaro. Preciso.', 10, '#2F7A4E')
    return done(bg, o, 'paper', '#E9ECE6')


# 41 · Sfumature del congiuntivo (lettera a un traduttore)
def s41():
    m, X = mk(41)
    o = env_room('#E9E2F2', '#B9946A', 320, True, X(40) if m == 1 else 270)
    bg, o = o, ''
    o += desk(X(90), 440) + open_book(X(70), 394, .7) + quill(X(120), 390, .8) + globe(X(150), 394, .6)
    o += person(X(42), 470, '#5B4A6B', 1, pose='hold', face=m, glasses=True, hs='bun') + envelope(X(80), 560, 1, '#FFF3C4')
    o += bubble(X(105), 330, 'Caro traduttore…', '#fff', side=0, size=11) + bubble(X(110), 640, 'Spero che tu stia bene', '#E8F4EC', side=0, size=10)
    o += bookshelf(X(330) - 35, 690, .8, 70, 100) + candle(X(40), 690)
    return done(bg, o, 'paper', '#ECE6F1')


# 42 · Il filo del discorso (perché leggiamo romanzi — biblioteca)
def s42():
    m, X = mk(42)
    o = '<rect width="400" height="700" fill="#5E3E28"/>'
    for i, x in enumerate((0, 80, 160, 240, 320)):
        o += bookshelf(x, 330, 1.14, 70, 280)
    o += '<rect y="330" width="400" height="370" fill="#B97A4E"/>' + rug(200, 520, 300, '#B03A4A')
    bg, o = o, ''
    o += armchair(X(320), 520, 1.1, '#3E8A52', -m) + person(X(320), 512, '#FFC94A', 2, '#6B3E1E', pose='hold', s=.9, face=-m, hs='long') + open_book(X(326), 468, .45)
    o += f'<path d="M{X(260)} 600 C{X(320)} 560 {X(240)} 640 {X(330)} 660 S{X(380)} 700 {X(360)} 640" stroke="#E2574C" stroke-width="2.5" fill="none"/>'
    o += bubble(X(300), 400, 'Un romanzo ti cambia', '#fff', side=0, size=10) + floor_lamp(X(380), 520) + books(X(270), 690)
    return done(bg, o, 'carpet', '#D9B48F', True)


# 43 · In bocca al lupo! (modi di dire, falsi amici)
def s43():
    m, X = mk(43)
    o = env_park('#E4F1FA', '#F5F2E6', '#C9E0AE', '#BBD79E', 270) + sun(X(330), 60, 20)
    bg, o = o, ''
    o += wolf(X(90), 310, 1.3, m) + bubble(X(98), 220, 'In bocca al lupo!', '#fff', side=0, size=11) + bubble(X(120), 380, 'Crepi!', '#FFF3C4', side=0, size=11)
    o += f'<g transform="translate({X(70)} 500)"><rect x="-30" y="-18" width="60" height="18" rx="3" fill="#FFE59A"/><rect x="-30" y="-24" width="60" height="8" rx="3" fill="#fff"/></g>' + txt(X(92), 530, 'burro = mantequilla', 11, '#8A5A3B')
    o += f'<g transform="translate({X(60)} 640)">' + ''.join(f'<rect x="{-30 + i * 14}" y="{-i * 12}" width="18" height="{12 + i * 12}" fill="#D9B48F"/>' for i in range(5)) + '</g>' + person(X(110), 590, '#3F6FA8', 1, s=.6, face=m, pose='wave')
    o += txt(X(70), 670, 'salire = subir', 11, '#8A5A3B') + tree(X(370), 690, .8)
    return done(bg, o, 'trail', '#E5F0DC')


# 44 · Italiano per il lavoro (riunione, grafici)
def s44():
    m, X = mk(44)
    o = '<rect width="400" height="700" fill="#EEF2F6"/><rect y="320" width="400" height="380" fill="#D3DAE3"/>'
    o += chart(X(296) - 60, 70, 120, 90, True) + f'<rect x="{X(260) - 20}" y="190" width="40" height="40" fill="#fff" stroke="#C9CFD6" stroke-width="2" rx="4"/><circle cx="{X(260)}" cy="210" r="13" fill="#3F6FA8"/><path d="M{X(260)} 210 V197 A13 13 0 0 1 {X(272)} 214 Z" fill="#FFC94A"/>'
    bg, o = o, ''
    o += f'<g transform="translate({X(320)} 470)"><ellipse cx="0" cy="-40" rx="80" ry="18" fill="#8A5A3B"/><rect x="-6" y="-40" width="12" height="40" fill="#5E3E28"/></g>'
    o += laptop(X(300), 434, .6) + cup(X(350), 436, .6, True)
    o += person(X(250), 470, '#3B4F6B', 1, pose='point', face=-m, glasses=True) + person(X(372), 470, '#C77DBA', 2, '#6B3E1E', face=-m, hs='bun', pose='hold')
    o += bubble(X(310), 340, 'Il fatturato è cresciuto', '#fff', side=0, size=10)
    o += chart(X(320) - 50, 580, 100, 70, False) + briefcase(X(260), 690)
    return done(bg, o, 'hall', '#E3E8EF')


# 45 · Tanti italiani (varietà: anguria / cocomero / melone)
def s45():
    m, X = mk(45)
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'geo'))
    import europe
    L0, L1, LA = europe.LON0, europe.LON1, europe.LAT1
    europe.LON0, europe.LON1, europe.LAT1 = 4.6, 24.6, 51.2
    europe.K = 400 / math.radians(europe.LON1 - europe.LON0)
    paths = europe.country_paths(tol=.5)
    P = europe.proj
    o = '<rect width="400" height="700" fill="#9ED3F0"/>'
    for name, d in paths.items():
        o += f'<path d="{d}" fill="{"#FBE3C0" if name == "Italy" else "#EDE6D3"}" stroke="#fff" stroke-width="1.3" stroke-linejoin="round"/>'
    o += txt(*P(16.5, 44.6), 'ADRIATICO', 9, '#5E8FB5', extra='font-style="italic" letter-spacing="2"') if False else ''
    pts = dict(Milano=(9.19, 45.46), Venezia=(12.33, 45.44), Firenze=(11.25, 43.77), Roma=(12.5, 41.9), Napoli=(14.27, 40.85), Palermo=(13.36, 38.12), Bari=(16.87, 41.12), Torino=(7.68, 45.07), Cagliari=(9.11, 39.22))
    for k, v in pts.items():
        x, y = P(*v)
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="#26323A"/>' + txt(x + 6, y + 4, k, 9, '#26323A', 'start')
    labels = [((9.6, 45.4), 'anguria', '#2F7A4E', 150), ((12.0, 42.6), 'cocomero', '#E2574C', 300), ((14.6, 40.6), 'mellone', '#3F6FA8', 450), ((13.8, 37.9), 'muluni', '#C77DBA', 560)]
    europe.LON0, europe.LON1, europe.LAT1 = L0, L1, LA
    europe.K = 400 / math.radians(L1 - L0)
    bg, o = o, ''
    for (lon, lat), word, c, ly in labels:
        x, y = P2 = (None, None)
    return bg, labels, pts


def s45b():
    m, X = mk(45)
    bg, labels, _ = s45()
    import europe
    L0, L1, LA = europe.LON0, europe.LON1, europe.LAT1
    europe.LON0, europe.LON1, europe.LAT1 = 4.6, 24.6, 51.2
    europe.K = 400 / math.radians(europe.LON1 - europe.LON0)
    o = ''
    # en primer plano (fg, escala .86 hacia el centro) hay que convertir: x_fg = 200 + (x - 200) / .86
    inv = lambda x, y: (200 + (x - 200) / .86, 360 + (y - 360) / .86)
    for (lon, lat), word, c, ly in labels:
        x, y = inv(*europe.proj(lon, lat))
        lx = 84
        o += f'<path d="M{lx + 34} {ly} Q{(lx + x) / 2} {ly} {x:.1f} {y:.1f}" stroke="{c}" stroke-width="2" stroke-dasharray="4 4" fill="none"/>'
        o += f'<g transform="translate({lx} {ly})"><rect x="-44" y="-14" width="88" height="28" rx="14" fill="{c}"/>' + txt(0, 5, word, 13, '#fff', weight=900) + '</g>'
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{c}" stroke="#fff" stroke-width="2"/>'
    europe.LON0, europe.LON1, europe.LAT1 = L0, L1, LA
    europe.K = 400 / math.radians(L1 - L0)
    # una sandía
    o += '<g transform="translate(60 660)"><path d="M-30 -4 A30 30 0 0 0 30 -4 Z" fill="#3E8A52"/><path d="M-26 -4 A26 26 0 0 0 26 -4 Z" fill="#E2574C"/>' + ''.join(f'<ellipse cx="{dx}" cy="{dy}" rx="1.5" ry="2.5" fill="#26323A"/>' for dx, dy in ((-12, 4), (0, 10), (12, 4), (-5, 2), (6, 1))) + '</g>'
    o += txt(96, 60, 'Come si dice?', 14, '#26323A', weight=900)
    return done(bg, o, 'flight', '#9ED3F0')


# 46 · La lingua letteraria (Dante)
def s46():
    m, X = mk(46)
    o = '<rect width="400" height="700" fill="#F3EAD7"/>' + ''.join(column(x, 700, 560, .9) for x in (24, 376)) + '<path d="M0 60 Q200 0 400 60 V90 H0 Z" fill="#E6D2A0"/>'
    bg, o = o, ''
    PT = globals().get('POET')
    if PT:
        o += (f'<g transform="translate({X(320)} 260)"><circle r="46" fill="{PT.get("bg", "#3F6FA8")}" opacity=".15"/>'
              + tophat_person(0, 40, PT.get('coat', '#26323A'), PT.get('skin', 1), -m, 1.1, PT.get('hat'), beard=PT.get('beard', False), glasses=PT.get('glasses', False), hair=PT.get('hair', '#3A2A1E'))
              + (laurel(0, -44, 1.2) if PT.get('laurel') else '') + '</g>')
    else:
        o += f'<g transform="translate({X(320)} 260)">' + '<circle r="46" fill="#B03A4A" opacity=".15"/>' + person(0, 40, '#B03A4A', 1, '#3A2A1E', s=1.1, face=-m) + '<path d="M-14 -40 Q0 -62 14 -40 L10 -34 Q0 -44 -10 -34 Z" fill="#B03A4A" transform="scale(1.26)"/>' + laurel(0, -44, 1.2) + '</g>'
    o += txt(X(320), 340, 'Dante Alighieri', 12, '#5E3E28')
    o += scroll(X(310), 470, 1.1) + txt(X(310), 440, 'Nel mezzo del cammin', 8, '#5E3E28', extra='font-style="italic"')
    o += quill(X(370), 470, 1) + open_book(X(300), 650, 1.1) + txt(X(300), 600, 'INFERNO', 11, '#B03A4A', weight=900)
    return done(bg, o, 'ink', '#EFE3CB')


# 47 · Linguaggi specialistici
def s47():
    m, X = mk(47, True)
    o = '<rect width="400" height="700" fill="#EEF0F3"/>' + ''.join(column(x, 330, 220, .8) for x in (X(300), X(370))) + f'<path d="M{X(240)} 140 L{X(330)} 90 L{X(420)} 140 Z" fill="#D8CDBB"/>'
    o += '<rect y="330" width="400" height="370" fill="#DCE1E7"/>'
    bg, o = o, ''
    o += scales(X(320), 450, 1.3) + txt(X(320), 470, 'GIURIDICO', 10, '#5B6676')
    o += gavel(X(270), 520, 1) + flask(X(356), 560, 1.2) + flask(X(330), 560, .8, '#7FA6DB') + txt(X(350), 580, 'SCIENTIFICO', 10, '#5B6676')
    o += stamp_(X(290), 670, 1, 'PROT. 15') + txt(X(330), 700, 'BUROCRATICO', 10, '#5B6676')
    o += bubble(X(300), 330, 'Ai sensi dell\'art. 3…', '#fff', side=0, size=10)
    return done(bg, o, 'hall', '#E3E7EC')


# 48 · Stile (recensione, ironia)
def s48():
    m, X = mk(48, True)
    o = '<rect width="400" height="700" fill="#2A2238"/>' + curtain_stage(400, 0, 700, '#B03A4A') + '<rect y="600" width="400" height="100" fill="#5E3E28"/>'
    o += ''.join(f'<circle cx="{x}" cy="{690}" r="14" fill="#1A1424"/>' for x in range(20, 400, 32))
    bg, o = o, ''
    o += f'<path d="M{X(80)} 60 L{X(20)} 500 L{X(160)} 500 Z" fill="#FFF3C4" opacity=".14"/>'
    o += person(X(80), 500, '#26323A', 1, pose='wave', face=m, hs='bun', glasses=True) + bubble(X(110), 410, 'Bravissimi… si fa per dire', '#fff', side=0, size=9)
    o += newspaper(X(80), 600, 1.3, -6, 'RECENSIONE') + star_rating(X(125), 640, 3, 1)
    o += txt(X(80), 200, 'Che stile!', 15, '#FFC94A', weight=900)
    return done(bg, o, 'carpet', '#4A3C60', True)


# 49 · Finezze (i dubbi dei madrelingua)
def s49():
    m, X = mk(49)
    o = '<rect width="400" height="700" fill="#F4F1EA"/>'
    bg, o = o, ''
    o += blackboard(36, 120, 150, 100, ("qual è", "qual'è", "un po'"))
    o += check(158, 140, True, .8) + check(158, 162, False, .8) + check(158, 184, True, .8)
    o += blackboard(36, 380, 150, 76, ("un pò", "sé stesso"))
    o += check(158, 400, False, .8) + check(158, 424, True, .8)
    o += magnifier(X(80), 620, 1.4) + person(X(140), 640, '#5B4A6B', 1, pose='point', face=m, glasses=True, old=True, hs='bald')
    o += bubble(X(90), 520, 'Si scrive così?', '#fff', side=0, size=11)
    return done(bg, o, 'paper', '#F1EDE3')


# 50 · Da maestri (discorso finale)
def s50():
    m, X = mk(50)
    o = sky('#2F3E73', '#7A6BB0', 700) + curtain_stage(400, 0, 600, '#B03A4A') + '<rect y="560" width="400" height="140" fill="#3A2A1E"/>'
    conf = ''.join(f'<rect x="{x}" y="-10" width="6" height="10" fill="{c}" transform="rotate({r} {x} 0)"><animateTransform attributeName="transform" type="translate" values="0 0;{d} 720" dur="{t}s" begin="{b}s" repeatCount="indefinite"/></rect>'
                   for x, c, r, d, t, b in ((40, '#FFC94A', 20, 20, 7, 0), (120, '#E2574C', -30, -10, 8, 1), (210, '#5BAA6A', 10, 14, 6.5, 2), (300, '#7FA6DB', 40, -16, 7.5, .5), (360, '#C77DBA', -10, 10, 6, 3), (80, '#fff', 30, -8, 9, 4)))
    o += conf
    bg, o = o, ''
    o += podium(X(310), 450, 1.1, '#C9A24A') + person(X(310), 386, '#26323A', 1, pose='wave', s=.9, face=-m, glasses=True) + laurel(X(310), 300, 1)
    o += bubble(X(310), 250, 'Grazie a tutti!', '#fff', side=0, size=12)
    o += ''.join(person(X(x), 690, c, k, hs=h, pose='wave', s=.8, begin=b, face=-m) for x, c, k, h, b in ((240, '#E2574C', 2, 'long', 0), (282, '#3F6FA8', 0, 'short', .3), (324, '#5BAA6A', 3, 'curly', .6), (364, '#FFC94A', 1, 'bun', .9)))
    o += cap(X(270), 560, 1) + scroll(X(370), 560, .8) + star(X(380), 200, 1.2) + star(X(250), 160, .9, .7)
    return done(bg, o, 'carpet', '#5B4F8A', True)


if not globals().get('NO_WRITE'):
    MORE = {i: globals()['s%d' % i]() for i in range(6, 51) if i != 45}
    MORE[45] = s45b()
