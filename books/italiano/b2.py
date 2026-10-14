from lib import *

IM = {}

# 30 Concordanza
b = ''
def conc(y, main, mcolor, rows):
    o = R(60, y, 300, 190, mcolor, rx=16) + T(210, y + 85, main[0], 26, 700, PAPER, 'middle') + T(210, y + 122, main[1], 18, 400, PAPER, 'middle')
    for i, (when, tense, ex) in enumerate(rows):
        yy = y + i * 100
        o += arrow(370, y + 95, 440, yy + 45, GREY, 3)
        o += R(450, yy, 690, 88, PAPER, stroke=SAND)
        o += T(470, yy + 34, when, 18, 700, GREY) + T(470, yy + 66, tense, 20, 700, mcolor) + T(1120, yy + 52, ex, 22, 700, INK, 'end')
    return o
b += conc(120, ('Credo che…', 'principale al presente'), BLUE, [('nello stesso momento o dopo', 'congiuntivo presente', '…Luca venga.'), ('prima', 'congiuntivo passato', '…Luca sia venuto.')])
b += conc(360, ('Credevo che…', 'principale al passato'), RED, [('nello stesso momento o dopo', 'congiuntivo imperfetto', '…Luca venisse.'), ('prima', 'congiuntivo trapassato', '…Luca fosse venuto.')])
IM['u30'] = page('Unità 30', 'Credevo che…', b, 590)

# 31 Periodo ipotetico
b = ''
types = [('1 · REALTÀ', GREEN, 1.0, 'Se ho tempo,', 'vengo.', 'se + indicativo  →  indicativo'),
         ('2 · POSSIBILITÀ', OCHRE, 0.45, 'Se avessi tempo,', 'verrei.', 'se + congiuntivo imperfetto  →  condizionale presente'),
         ('3 · IRREALTÀ', RED, 0.0, 'Se avessi avuto tempo,', 'sarei venuto.', 'se + congiuntivo trapassato  →  condizionale passato')]
for i, (t, c, pr, a, z, rule) in enumerate(types):
    y = 115 + i * 165
    b += R(60, y, 1080, 148, PAPER, stroke=c, sw=3)
    b += T(85, y + 40, t, 23, 700, c)
    b += R(85, y + 62, 220, 22, '#E6E6E6', rx=11) + (R(85, y + 62, max(22, 220 * pr), 22, c, rx=11) if pr > 0 else '')
    b += T(85, y + 118, ['molto probabile', 'poco probabile', 'impossibile: è passato'][i], 18, 400, GREY)
    b += T(360, y + 62, a, 26, 400, INK) + T(360 + len(a) * 13.6 + 12, y + 62, z, 26, 700, c)
    b += T(360, y + 112, rule, 19, 400, GREY)
IM['u31'] = page('Unità 31', 'Se fossi…', b, 630)

# 32 Passivo
b = ''
b += T(60, 140, 'FRASE ATTIVA', 20, 700, GREY)
b += R(60, 160, 250, 70, '#CFE4F4', rx=14) + T(185, 205, 'Il cuoco', 26, 700, BLUE, 'middle')
b += R(330, 160, 250, 70, PAPER, rx=14, stroke=SAND) + T(455, 205, 'prepara', 26, 700, INK, 'middle')
b += R(600, 160, 250, 70, ROSE, rx=14) + T(725, 205, 'la cena.', 26, 700, RED, 'middle')
b += T(185, 258, 'soggetto', 17, 400, GREY, 'middle') + T(725, 258, 'oggetto', 17, 400, GREY, 'middle')
b += P('M185,270 C185,330 780,295 780,352', stroke=BLUE, sw=4) + P('M725,270 C725,330 185,295 185,352', stroke=RED, sw=4)
b += T(60, 390, 'FRASE PASSIVA', 20, 700, GREY)
b += R(60, 405, 250, 70, ROSE, rx=14) + T(185, 450, 'La cena', 26, 700, RED, 'middle')
b += R(330, 405, 300, 70, PAPER, rx=14, stroke=SAND) + T(480, 450, 'è preparata', 26, 700, INK, 'middle')
b += R(650, 405, 260, 70, '#CFE4F4', rx=14) + T(780, 450, 'dal cuoco.', 26, 700, BLUE, 'middle')
b += T(185, 503, 'soggetto', 17, 400, GREY, 'middle') + T(480, 503, 'essere + participio', 17, 400, GREY, 'middle') + T(780, 503, 'da + agente', 17, 400, GREY, 'middle')
b += R(940, 130, 200, 380, PAPER, stroke=GREEN)
b += T(1040, 172, 'Tre ausiliari', 20, 700, GREEN, 'middle')
for i, (aux, note) in enumerate((('essere', 'sempre'), ('venire', 'tempi semplici'), ('andare', 'necessità'))):
    b += R(960, 195 + i * 96, 160, 80, LEAF, rx=12) + T(1040, 230 + i * 96, aux, 23, 700, INK, 'middle') + T(1040, 258 + i * 96, note, 16, 400, GREY, 'middle')
b += R(60, 540, 1080, 60, LEAF, rx=12) + T(600, 578, 'La cena viene servita alle otto.   ·   Il modulo va firmato.', 21, 700, GREEN, 'middle')
IM['u32'] = page('Unità 32', 'È stato detto', b, 630)

# 33 Discorso indiretto
b = ''
b += person(140, 330, 190, RED, 2, '#6B3E1E', long=True)
b += bubble(240, 120, 520, ['«Domani vengo qui', 'con mio fratello.»'], 26, 'left')
b += arrow(600, 270, 600, 330, GREY, 5)
b += R(240, 345, 900, 100, PAPER, stroke=GREEN, sw=3)
b += T(265, 388, 'Anna ha detto che il giorno dopo sarebbe venuta lì', 24, 700, INK) + T(265, 424, 'con suo fratello.', 24, 700, INK)
b += T(830, 150, 'DISCORSO DIRETTO', 19, 700, GREY) + T(1140, 330, 'DISCORSO INDIRETTO', 19, 700, GREEN, 'end')
sh = [('oggi', 'quel giorno'), ('domani', 'il giorno dopo'), ('ieri', 'il giorno prima'), ('qui', 'lì'), ('questo', 'quello'), ('presente', 'imperfetto'), ('passato prossimo', 'trapassato'), ('futuro', 'condizionale passato')]
for i, (a, z) in enumerate(sh):
    x = 60 + (i % 3) * 365; y = 480 + (i // 3) * 68
    b += R(x, y, 345, 56, PAPER, stroke=SAND) + T(x + 14, y + 36, a, 18, 400, INK) + T(x + 331, y + 36, z, 18, 700, GREEN, 'end')
    b += T(x + 14 + len(a) * 9.6 + 16, y + 36, '→', 18, 700, GREY, 'middle')
IM['u33'] = page('Unità 33', 'Disse che…', b, 710)

# 34 Passato remoto
b = ''
b += i_book(160, 220, 80, '#7A4B2A') + T(160, 340, '«C\'era una volta', 22, 400, INK, 'middle', True) + T(160, 370, 'un re che partì', 22, 400, INK, 'middle', True) + T(160, 400, 'per un lungo viaggio…»', 22, 400, INK, 'middle', True)
y = 190
b += arrow(340, y, 1130, y, INK, 4)
b += C(450, y, 13, '#7A4B2A') + T(450, y - 30, '1265', 20, 700, '#7A4B2A', 'middle') + T(450, y + 40, 'Dante nacque a Firenze.', 19, 700, INK, 'middle') + T(450, y + 68, 'passato remoto', 17, 400, '#7A4B2A', 'middle')
b += C(820, y, 13, RED) + T(820, y - 30, 'stamattina', 20, 700, RED, 'middle') + T(820, y + 40, 'Ho visto Luca.', 19, 700, INK, 'middle') + T(820, y + 68, 'passato prossimo', 17, 400, RED, 'middle')
b += C(1040, y, 16, INK) + T(1040, y - 30, 'adesso', 20, 700, INK, 'middle')
tb = [('', 'parlare', 'credere', 'partire'), ('io', 'parlai', 'credei / credetti', 'partii'), ('tu', 'parlasti', 'credesti', 'partisti'), ('lui / lei', 'parlò', 'credé / credette', 'partì'),
      ('noi', 'parlammo', 'credemmo', 'partimmo'), ('voi', 'parlaste', 'credeste', 'partiste'), ('loro', 'parlarono', 'crederono / credettero', 'partirono')]
xs = [340, 460, 640, 960]
for i, row in enumerate(tb):
    yy = 320 + i * 42
    if i == 0:
        b += R(330, yy - 28, 810, 40, '#7A4B2A', rx=8)
    for j, cell in enumerate(row):
        b += T(xs[j], yy, cell, 20, 700 if i == 0 or j == 0 else 400, PAPER if i == 0 else (GREY if j == 0 else INK))
IM['u34'] = page('Unità 34', "C'era una volta", b, 620)

# 35 Congiunzioni + congiuntivo
b = ''
cats = [('Concessive', 'anche se è così…', ['benché', 'sebbene', 'nonostante', 'malgrado'], BLUE, 'Benché piova, esco.'),
        ('Finali', 'con uno scopo', ['affinché', 'perché'], GREEN, 'Parlo piano perché tu capisca.'),
        ('Condizionali', 'solo se…', ['purché', 'a patto che', 'a condizione che'], OCHRE, 'Vengo, purché ci sia Anna.'),
        ('Temporali', 'non è ancora successo', ['prima che', 'finché non'], RED, 'Torna prima che faccia buio.'),
        ('Eccettuative', 'tranne se…', ['a meno che (non)', 'salvo che'], '#5B4A6B', 'Esco, a meno che non piova.'),
        ('Modali', 'in che modo', ['senza che', 'come se'], '#7A4B2A', 'Parla come se sapesse tutto.')]
for i, (t, sub, conj, c, ex) in enumerate(cats):
    x = 60 + (i % 3) * 365; y = 115 + (i // 3) * 265
    b += R(x, y, 345, 245, PAPER, stroke=c, sw=3) + R(x, y, 345, 62, c, rx=14) + R(x, y + 40, 345, 22, c, rx=0)
    b += T(x + 18, y + 40, t, 23, 700, PAPER) + T(x + 327, y + 40, sub, 16, 400, PAPER, 'end')
    xx, yy = x + 16, y + 78
    for cj in conj:
        ch, w_ = chip(xx, yy, cj, LEAF, INK, 18, 700, 12)
        if xx + w_ > x + 335:
            xx, yy = x + 16, yy + 44
            ch, w_ = chip(xx, yy, cj, LEAF, INK, 18, 700, 12)
        b += ch
        xx += w_ + 8
    b += T(x + 18, y + 220, ex, 18, 400, INK, italic=True)
IM['u35'] = page('Unità 35', 'Benché, purché, affinché', b, 660)

# 36 Suffissi
b = ''
b += T(60, 135, 'I suffissi cambiano la sfumatura', 22, 700, GREEN)
cats_ = [('gatto', 44, OCHRE, 'neutro'), ('gattino', 26, OCHRE, 'piccolo, carino'), ('gattone', 62, OCHRE, 'grande'), ('gattaccio', 44, '#6C6C6C', 'brutto, cattivo')]
for i, (w_, s_, c, note) in enumerate(cats_):
    x = 170 + i * 285
    b += R(x - 125, 155, 250, 240, PAPER, stroke=SAND) + i_cat(x, 265, s_, c) + T(x, 355, w_, 24, 700, INK, 'middle') + T(x, 382, note, 17, 400, GREY, 'middle')
b += T(60, 445, 'I prefissi cambiano il significato', 22, 700, BLUE)
pre = [('ri-', 'fare', 'rifare', 'di nuovo'), ('dis-', 'fare', 'disfare', 'il contrario'), ('in-', 'utile', 'inutile', 'negazione'), ('s-', 'contento', 'scontento', 'negazione'), ('pre-', 'vedere', 'prevedere', 'prima'), ('stra-', 'pieno', 'strapieno', 'moltissimo')]
for i, (p_, base, res, note) in enumerate(pre):
    x = 60 + (i % 3) * 365; y = 465 + (i // 3) * 82
    b += R(x, y, 345, 68, PAPER, stroke=SAND)
    b += T(x + 16, y + 42, p_, 22, 700, RED) + T(x + 78, y + 42, '+ ' + base, 19, 400, INK) + T(x + 230, y + 30, res, 20, 700, BLUE, 'middle') + T(x + 230, y + 54, note, 15, 400, GREY, 'middle')
IM['u36'] = page('Unità 36', 'Parole che crescono', b, 660)

# 37 Testo argomentativo
b = ''
steps = [('1', 'Introduzione', 'Presento il tema.', 'Oggi si discute molto di…', GREY),
         ('2', 'Tesi', 'Dico la mia opinione.', 'A mio parere… · Ritengo che…', GREEN),
         ('3', 'Argomenti', 'Porto prove ed esempi.', 'In primo luogo… · Inoltre… · Ad esempio…', BLUE),
         ('4', 'Antitesi e confutazione', "Considero l'opinione contraria.", 'È vero che…, tuttavia… · Alcuni sostengono che…', OCHRE),
         ('5', 'Conclusione', 'Riassumo e confermo la tesi.', 'In conclusione… · Per questi motivi…', RED)]
for i, (n, t, what, conn, c) in enumerate(steps):
    y = 112 + i * 104
    x = 60 + i * 26
    b += R(x, y, 1080 - i * 26, 90, PAPER, stroke=c, sw=3)
    b += C(x + 46, y + 45, 26, c) + T(x + 46, y + 54, n, 26, 700, PAPER, 'middle')
    b += T(x + 90, y + 38, t, 23, 700, c) + T(x + 90, y + 68, what, 18, 400, INK)
    b += T(1120, y + 52, conn, 18, 400, GREY, 'end', True)
    if i < 4:
        b += arrow(x + 46, y + 73, x + 46 + 26, y + 104 + 17, c, 3, 10)
IM['u37'] = page('Unità 37', 'Dire la propria', b, 650)
