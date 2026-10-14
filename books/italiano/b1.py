from lib import *

IM = {}


def card(x, y, w, h, title, lines, color=GREEN, fill=PAPER, tsize=22, size=20, lh=30):
    o = R(x, y, w, h, fill, stroke=color)
    o += T(x + 20, y + 36, title, tsize, 700, color)
    for i, l in enumerate(lines):
        o += T(x + 20, y + 36 + tsize * .6 + (i + 1) * lh - 6, l, size, 400, INK)
    return o


# 21 Condizionale
b = ''
three = [('Un desiderio', 'Vorrei vivere al mare.', i_house, BLUE), ('Un consiglio', 'Dovresti riposare.', i_bed, GREEN), ('Una richiesta gentile', 'Potresti aiutarmi?', i_speech, RED)]
for i, (t, s_, ic, c) in enumerate(three):
    x = 60 + i * 370
    b += R(x, 110, 340, 230, PAPER, stroke=c) + T(x + 170, 150, t, 22, 700, c, 'middle') + ic(x + 170, 225, 42) + T(x + 170, 315, s_, 22, 700, INK, 'middle')
b += R(60, 370, 1080, 230, PAPER, stroke=SAND)
b += T(90, 412, 'Come si forma', 22, 700, GREEN)
b += T(90, 465, 'parlare', 26, 400, INK) + arrow(190, 457, 250, 457, GREY, 3) + T(265, 465, 'parler-', 26, 700, BLUE)
b += T(90, 515, 'prendere', 26, 400, INK) + arrow(205, 507, 250, 507, GREY, 3) + T(265, 515, 'prender-', 26, 700, BLUE)
b += T(90, 565, 'dormire', 26, 400, INK) + arrow(190, 557, 250, 557, GREY, 3) + T(265, 565, 'dormir-', 26, 700, BLUE)
b += T(420, 515, '+', 40, 700, GREY, 'middle')
ends = ['-ei', '-esti', '-ebbe', '-emmo', '-este', '-ebbero']
prs = ['io', 'tu', 'lui / lei', 'noi', 'voi', 'loro']
for i, (e, p_) in enumerate(zip(ends, prs)):
    x = 470 + (i % 3) * 220; y = 425 + (i // 3) * 85
    b += R(x, y, 200, 68, LEAF, rx=12) + T(x + 16, y + 28, p_, 17, 400, GREY) + T(x + 184, y + 48, e, 28, 700, RED, 'end')
IM['u21'] = page('Unità 21', 'Vorrei, potrei…', b, 630)

# 22 Tu / Lei
b = ''
b += R(50, 110, 530, 470, '#EEF5E6', stroke=GREEN) + R(620, 110, 530, 470, '#E8EEF4', stroke=BLUE)
b += T(315, 155, 'TU · tra amici', 26, 700, GREEN, 'middle') + T(885, 155, 'LEI · in ufficio', 26, 700, BLUE, 'middle')
b += person(150, 500, 200, RED, 2, '#6B3E1E', long=True) + person(480, 500, 200, OCHRE, 1, '#2A2A2A')
b += bubble(190, 185, 250, ['Entra! Siediti!', 'Dimmi tutto.'], 22, 'left')
b += T(315, 545, 'entra · siediti · dimmi · scusa', 19, 700, GREEN, 'middle')
b += person(720, 500, 200, '#5B4A6B', 0, '', old=True) + person(1050, 500, 200, BLUE, 0, '#3A2A1E')
b += bubble(760, 185, 270, ['Entri! Si accomodi!', 'Mi dica, prego.'], 22, 'left')
b += T(885, 545, 'entri · si accomodi · mi dica · scusi', 19, 700, BLUE, 'middle')
IM['u22'] = page('Unità 22', 'Si accomodi!', b, 610)

# 23 Pronomi combinati
b = ''
cols = ['lo', 'la', 'li', 'le', 'ne']
rows = [('mi', 'me'), ('ti', 'te'), ('gli / le', 'glie'), ('ci', 'ce'), ('vi', 've'), ('gli (loro)', 'glie')]
x0, y0, cw, rh = 330, 130, 160, 62
b += T(170, y0 + 40, 'indiretto', 20, 700, RED, 'middle') + T(170, y0 + 15, '+ diretto →', 18, 400, GREY, 'middle')
for j, c in enumerate(cols):
    b += R(x0 + j * cw, y0, cw - 10, rh - 10, BLUE, rx=10) + T(x0 + j * cw + (cw - 10) / 2, y0 + 36, c, 26, 700, PAPER, 'middle')
for i, (ind, comb) in enumerate(rows):
    y = y0 + (i + 1) * rh
    b += R(70, y, 240, rh - 10, RED, rx=10) + T(190, y + 36, ind, 24, 700, PAPER, 'middle')
    for j, c in enumerate(cols):
        txt = (comb + c) if comb == 'glie' else f'{comb} {c}'
        b += R(x0 + j * cw, y, cw - 10, rh - 10, PAPER, rx=10, stroke=SAND) + T(x0 + j * cw + (cw - 10) / 2, y + 36, txt, 24, 700, INK, 'middle')
b += R(70, 575, 1060, 62, LEAF, rx=12)
b += T(95, 614, 'Do il libro a Marco.', 21, 400, INK) + arrow(320, 606, 370, 606, GREY, 3) + T(385, 614, 'Glielo do.', 22, 700, GREEN)
b += T(600, 614, 'Mi porti le chiavi?', 21, 400, INK) + arrow(810, 606, 860, 606, GREY, 3) + T(875, 614, 'Me le porti?', 22, 700, GREEN)
IM['u23'] = page('Unità 23', 'Te lo dico io', b, 670)

# 24 Relativi
b = ''
def merge(y, s1, s2, res, hl, color):
    o = R(60, y, 420, 50, PAPER, stroke=SAND) + T(80, y + 33, s1, 20, 400, INK)
    o += R(60, y + 60, 420, 50, PAPER, stroke=SAND) + T(80, y + 93, s2, 20, 400, INK)
    o += arrow(495, y + 55, 570, y + 55, color, 5)
    o += R(585, y + 20, 555, 70, PAPER, stroke=color, sw=3)
    o += T(605, y + 64, res, 21, 700, INK)
    o += T(1120, y + 12, hl, 22, 700, color, 'end')
    return o
b += merge(120, 'Ho un amico.', "L'amico vive a Roma.", 'Ho un amico che vive a Roma.', 'CHE', GREEN)
b += merge(260, 'Questa è la città.', 'Io vivo in questa città.', 'Questa è la città in cui vivo.', 'preposizione + CUI', BLUE)
b += merge(400, 'Ecco la collega.', 'Ti ho parlato della collega.', 'Ecco la collega di cui ti ho parlato.', 'DI CUI', RED)
b += R(60, 540, 1080, 70, LEAF, rx=12) + T(600, 584, 'Chi dorme non piglia pesci.   ·   CHI = la persona che', 22, 700, GREEN, 'middle')
IM['u24'] = page('Unità 24', 'La persona che…', b, 640)

# 25 Congiuntivo
b = ''
b += R(50, 110, 530, 500, '#E8EEF4', stroke=BLUE) + R(620, 110, 530, 500, '#FBEDEA', stroke=RED)
b += T(315, 155, 'CERTEZZA', 26, 700, BLUE, 'middle') + T(315, 185, 'che + indicativo', 20, 400, INK, 'middle')
b += T(885, 155, 'OPINIONE · DUBBIO · DESIDERIO', 24, 700, RED, 'middle') + T(885, 185, 'che + congiuntivo', 20, 400, INK, 'middle')
b += C(315, 265, 44, PAPER, BLUE, 4) + P('M293,265 l16,16 l30,-34', stroke=BLUE, sw=7)
b += C(885, 265, 44, PAPER, RED, 4) + T(885, 285, '?', 56, 700, RED, 'middle')
left = ['So che Marco è a casa.', 'Sono sicura che viene.', 'È vero che parla italiano.', 'Vedo che hai fame.']
right = ['Penso che Marco sia a casa.', 'Spero che venga.', 'È possibile che parli italiano.', 'Ho paura che tu abbia fame.']
for i, l in enumerate(left):
    b += R(80, 335 + i * 64, 470, 52, PAPER, rx=12) + T(315, 369 + i * 64, l, 21, 700, INK, 'middle')
for i, l in enumerate(right):
    b += R(650, 335 + i * 64, 470, 52, PAPER, rx=12) + T(885, 369 + i * 64, l, 21, 700, INK, 'middle')
IM['u25'] = page('Unità 25', 'Penso che…', b, 640)

# 26 Trapassato / futuro anteriore
b = ''
y = 250
b += arrow(70, y, 1130, y, INK, 4)
marks = [(170, 'PRIMA', 'trapassato prossimo', 'il treno era partito', BLUE), (430, 'PASSATO', 'passato prossimo', 'sono arrivato', RED), (630, 'ADESSO', '', '', INK),
         (830, 'PRIMA', 'futuro anteriore', 'avrò finito', BLUE), (1030, 'FUTURO', 'futuro semplice', 'ti chiamerò', RED)]
for x, a, tname, ex, c in marks:
    b += C(x, y, 13 if a != 'ADESSO' else 17, c)
    b += T(x, y - 30, a, 19, 700, c, 'middle')
    if tname:
        b += T(x, y + 44, tname, 18, 700, c, 'middle') + T(x, y + 72, ex, 19, 400, INK, 'middle', True)
b += P(f'M170,{y - 60} Q300,{y - 130} 430,{y - 60}', stroke=GREY, sw=3) + T(300, y - 120, 'prima di', 18, 400, GREY, 'middle')
b += P(f'M830,{y - 60} Q930,{y - 130} 1030,{y - 60}', stroke=GREY, sw=3) + T(930, y - 120, 'prima di', 18, 400, GREY, 'middle')
b += R(60, 400, 520, 150, PAPER, stroke=BLUE) + T(320, 445, 'Quando sono arrivato alla stazione,', 21, 400, INK, 'middle') + T(320, 480, 'il treno era già partito.', 22, 700, BLUE, 'middle') + T(320, 525, 'imperfetto di avere / essere + participio', 17, 400, GREY, 'middle')
b += R(620, 400, 520, 150, PAPER, stroke=BLUE) + T(880, 445, 'Quando avrò finito il lavoro,', 22, 700, BLUE, 'middle') + T(880, 480, 'ti chiamerò.', 21, 400, INK, 'middle') + T(880, 525, 'futuro di avere / essere + participio', 17, 400, GREY, 'middle')
IM['u26'] = page('Unità 26', 'Prima e dopo', b, 590)

# 27 Ipotesi reali
b = ''
b += R(60, 115, 330, 110, RED, rx=16) + T(225, 160, 'SE + presente', 26, 700, PAPER, 'middle') + T(225, 195, 'SE + futuro', 22, 400, PAPER, 'middle')
b += arrow(400, 170, 480, 170, INK, 5)
for i, t in enumerate(('presente', 'futuro', 'imperativo')):
    b += R(495 + i * 215, 130, 200, 80, LEAF, rx=14, stroke=GREEN) + T(595 + i * 215, 180, t, 24, 700, GREEN, 'middle')
ex = [(i_sun, "Se c'è il sole,", 'andiamo al mare.'), (i_rain, 'Se pioverà,', 'resteremo a casa.'), (i_speech, 'Se vedi Marco,', 'salutalo!')]
for i, (ic, a, c) in enumerate(ex):
    x = 60 + i * 370
    b += R(x, 270, 340, 250, PAPER, stroke=SAND) + ic(x + 170, 345, 44) + T(x + 170, 440, a, 23, 400, INK, 'middle') + T(x + 170, 478, c, 23, 700, GREEN, 'middle')
b += T(600, 565, 'Un\'ipotesi reale: la condizione è possibile e la conseguenza è sicura.', 20, 400, GREY, 'middle', True)
IM['u27'] = page('Unità 27', 'Se posso, vengo', b, 600)

# 28 Media
b = ''
md = [(i_phone, 'lo smartphone', 'mandare un messaggio'), (i_screen, 'il computer', 'navigare in rete'), (i_mail, 'la posta elettronica', 'allegare un file'),
      (i_globe, 'i social network', 'condividere una foto'), (i_book, 'il giornale', 'leggere le notizie'), (i_mic, 'la radio · il podcast', 'ascoltare un programma')]
for i, (ic, lab, act) in enumerate(md):
    x = 235 + (i % 3) * 365; y = 205 + (i // 3) * 215
    b += R(x - 155, y - 90, 310, 195, PAPER, stroke=SAND) + ic(x, y - 20, 42) + T(x, y + 55, lab, 21, 700, INK, 'middle') + T(x, y + 84, act, 18, 400, GREEN, 'middle')
b += R(60, 550, 1080, 70, LEAF, rx=12) + T(600, 594, 'In Italia si guarda molta TV, ma si leggono pochi giornali.', 22, 700, GREEN, 'middle')
IM['u28'] = page('Unità 28', 'Si dice che…', b, 650)

# 29 E-mail
b = ''
b += R(60, 110, 720, 530, PAPER, stroke=INK, sw=3) + R(60, 110, 720, 44, INK, rx=14) + R(60, 135, 720, 20, INK, rx=0)
for k, c in enumerate((RED, OCHRE, GREEN)):
    b += C(88 + k * 26, 132, 8, c)
b += T(90, 190, 'A:', 18, 700, GREY) + T(180, 190, 'm.bianchi@scuolaitaliano.example', 18, 400, INK) + L(80, 204, 760, 204, SAND, 2)
b += T(90, 236, 'Oggetto:', 18, 700, GREY) + T(180, 236, 'Richiesta di informazioni sul corso B1', 18, 700, INK) + L(80, 250, 760, 250, SAND, 2)
body = [('Gentile dottoressa Bianchi,', 700), ('', 400), ('Le scrivo per chiedere alcune informazioni sul corso', 400), ('di italiano di livello B1 che inizierà a marzo.', 400),
        ('Vorrei sapere quali sono gli orari e il costo.', 400), ('', 400), ('La ringrazio in anticipo per la Sua disponibilità.', 400), ('', 400), ('Cordiali saluti,', 700), ('Lucía Fernández', 400)]
for i, (l, w_) in enumerate(body):
    b += T(90, 295 + i * 32, l, 19, w_, INK)
tags = [(190, "l'oggetto", BLUE, 236), (295, 'la formula di apertura', GREEN, 290), (390, 'il corpo del messaggio', GREY, 375), (485, 'i ringraziamenti', OCHRE, 487), (555, 'la formula di chiusura', RED, 550), (600, 'la firma', '#5B4A6B', 583)]
ys = [150, 235, 320, 405, 490, 575]
for (yy, lab, c, ty), y2 in zip(tags, ys):
    b += R(840, y2 - 26, 300, 50, c, rx=25) + T(990, y2 + 7, lab, 20, 700, PAPER, 'middle') + L(780, ty - 6, 840, y2, c, 3)
IM['u29'] = page('Unità 29', 'Scrivere bene', b, 670)
