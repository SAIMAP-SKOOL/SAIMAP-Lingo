from lib import *

IM = {}

# 1 Ciao!
b = ''
b += person(170, 520, 250, BLUE, 0, '#3A2A1E')
b += bubble(250, 130, 330, ['Ciao! Io sono Marco.', 'E tu, come ti chiami?'], 24, 'left')
b += person(1020, 520, 250, RED, 2, '#6B3E1E', long=True)
b += bubble(640, 250, 330, ['Piacere, Marco!', 'Mi chiamo Lucía.'], 24, 'right')
for i, (ic, lab, sub) in enumerate(((i_sun, 'Buongiorno!', 'la mattina'), (i_cloud, 'Buon pomeriggio!', 'dopo pranzo'), (i_moon, 'Buonasera!', 'la sera'))):
    x = 330 + i * 190
    b += R(x, 420, 170, 150, PAPER if i < 2 else '#27364A', stroke=GREEN)
    b += (ic(x + 85, 470, 34) if i != 1 else i_sun(x + 70, 462, 26) + i_cloud(x + 95, 478, 30))
    b += T(x + 85, 532, lab, 19, 700, INK if i < 2 else PAPER, 'middle') + T(x + 85, 556, sub, 16, 400, GREY if i < 2 else '#CFD6DC', 'middle')
IM['u01'] = page('Unità 1', 'Ciao!', b, 620)

# 2 Di dove sei?
b = ''
data = [('Paolo', 'Sono italiano.', "Sono di Roma.", [GREEN, PAPER, RED], False, BLUE, False),
        ('Lucía', 'Sono spagnola.', 'Sono di Siviglia.', [RED, OCHRE, OCHRE, RED], True, RED, True),
        ('Pierre', 'Sono francese.', 'Sono di Lione.', ['#2B4C9B', PAPER, '#D8323A'], False, GREEN, False),
        ('Anna', 'Sono tedesca.', 'Sono di Berlino.', ['#222', '#D8323A', OCHRE], True, '#5B4A6B', True),
        ('Diego', 'Sono argentino.', 'Sono di Rosario.', ['#7CB6E0', PAPER, '#7CB6E0'], True, OCHRE, False)]
for i, (n, l1, l2, cols, hor, shirt, lg) in enumerate(data):
    x = 130 + i * 235
    b += R(x - 105, 110, 210, 470, PAPER, stroke=SAND)
    b += flag(x - 45, 130, 90, 58, cols, hor)
    b += person(x, 440, 200, shirt, i, ['#3A2A1E', '#5A3A1E', '#B58A3C', '#D9B35A', '#2A2A2A'][i], long=lg)
    b += T(x, 480, n, 24, 700, GREEN, 'middle') + T(x, 515, l1, 21, 700, INK, 'middle') + T(x, 545, l2, 19, 400, INK, 'middle')
IM['u02'] = page('Unità 2', 'Di dove sei?', b, 610)

# 3 Famiglia
b = ''
def node(x, y, name, role, shirt, sk, hair, lg=False, old=False, me=False):
    o = R(x - 78, y - 8, 156, 168, LEAF if me else PAPER, stroke=GREEN if me else SAND)
    o += person(x, y + 108, 108, shirt, sk, hair, long=lg, old=old)
    o += T(x, y + 132, role, 19, 700, GREEN, 'middle') + T(x, y + 153, name, 16, 400, GREY, 'middle')
    return o
# lines
b += L(420, 190, 560, 190, GREY, 3) + L(490, 190, 490, 290, GREY, 3) + L(260, 290, 760, 290, GREY, 3)
b += L(260, 290, 260, 310, GREY, 3) + L(760, 290, 760, 310, GREY, 3)
b += L(340, 390, 420, 390, GREY, 3) + L(380, 390, 380, 470, GREY, 3) + L(180, 470, 580, 470, GREY, 3)
for x in (180, 380, 580):
    b += L(x, 470, x, 490, GREY, 3)
b += L(840, 390, 920, 390, GREY, 3) + L(880, 390, 880, 470, GREY, 3) + L(880, 470, 880, 490, GREY, 3)
b += node(340, 110, 'Giuseppe', 'il nonno', GREEN, 0, '', old=True)
b += node(640, 110, 'Maria', 'la nonna', '#5B4A6B', 2, '', lg=True, old=True)
b += node(260, 310, 'Franco', 'il padre', BLUE, 0, '#3A2A1E')
b += node(500, 310, 'Elena', 'la madre', RED, 2, '#6B3E1E', lg=True)
b += node(760, 310, 'Carlo', 'lo zio', OCHRE, 1, '#2A2A2A')
b += node(1000, 310, 'Rita', 'la zia', GREEN, 0, '#B58A3C', lg=True)
b += node(180, 490, 'Luca', 'il fratello', GREEN, 0, '#3A2A1E')
b += node(380, 490, 'Sofia', 'IO', RED, 2, '#6B3E1E', lg=True, me=True)
b += node(580, 490, 'Giulia', 'la sorella', OCHRE, 2, '#6B3E1E', lg=True)
b += node(880, 490, 'Matteo', 'il cugino', BLUE, 1, '#2A2A2A')
IM['u03'] = page('Unità 3', 'La mia famiglia', b, 690)

# 4 Al bar
b = ''
b += R(60, 110, 520, 460, '#2F3E46', rx=18)
b += T(320, 160, 'LISTINO PREZZI', 28, 700, OCHRE, 'middle')
menu = [('un caffè', '1,20 €'), ('un cappuccino', '1,60 €'), ('un tè', '2,00 €'), ('una spremuta', '3,50 €'), ("un'acqua minerale", '1,00 €'), ('un cornetto', '1,30 €'), ('un panino', '4,50 €'), ('una pizzetta', '2,50 €')]
for i, (a, p) in enumerate(menu):
    y = 215 + i * 44
    b += T(100, y, a, 25, 400, PAPER) + T(540, y, p, 25, 700, PAPER, 'end')
    b += L(100 + len(a) * 13.5 + 10, y - 6, 440, y - 6, '#6C7B84', 2, dash='2 8')
items = [(i_cup, 'il caffè'), (i_cornetto, 'il cornetto'), (i_panino, 'il panino'), (lambda x, y, s: i_glass(x, y, s, '#F2A23A'), 'la spremuta'), (i_bottle, "l'acqua"), (i_pizza, 'la pizzetta')]
for i, (ic, lab) in enumerate(items):
    x = 720 + (i % 3) * 170; y = 190 + (i // 3) * 200
    b += R(x - 75, y - 75, 150, 180, PAPER, stroke=SAND) + ic(x, y - 5, 42) + T(x, y + 82, lab, 21, 700, INK, 'middle')
b += bubble(640, 505, 500, ['— Vorrei un caffè e un cornetto, per favore.'], 22, 'left', LEAF, GREEN)
IM['u04'] = page('Unità 4', 'Al bar', b, 610)

# 5 Giornata
b = ''
day = [(7, 0, 'Mi sveglio', 'alle sette'), (7, 30, 'Faccio colazione', 'alle sette e mezza'), (8, 15, 'Vado al lavoro', 'alle otto e un quarto'),
       (13, 0, 'Pranzo', "all'una"), (18, 45, 'Torno a casa', 'alle sette meno un quarto'), (23, 0, 'Vado a letto', 'alle undici')]
for i, (h_, m_, act, t) in enumerate(day):
    x = 210 + (i % 3) * 390; y = 210 + (i // 3) * 250
    night = i in (0, 5)
    b += R(x - 175, y - 100, 350, 225, PAPER, stroke=SAND)
    b += clock(x - 95, y - 5, 62, h_, m_)
    b += T(x - 20, y - 25, act, 21, 700, INK) + T(x - 20, y + 5, t, 16, 400, GREEN)
    b += T(x - 20, y + 36, f'{h_:02d}:{m_:02d}', 20, 700, GREY)
    b += (i_moon(x + 135, y + 85, 20) if night else i_sun(x + 135, y + 85, 18))
b += L(60, 595, 1140, 595, GREY, 3)
for i, lab in enumerate(('la mattina', 'il pomeriggio', 'la sera', 'la notte')):
    b += T(195 + i * 270, 630, lab, 21, 700, GREEN, 'middle')
IM['u05'] = page('Unità 5', 'La mia giornata', b, 660)

# 6 In città
b = ''
b += R(40, 100, 1120, 520, '#E9E4D6', rx=18)
# streets
b += R(40, 320, 1120, 70, '#B9BEC2', rx=0) + R(540, 100, 70, 520, '#B9BEC2', rx=0)
b += L(60, 355, 1140, 355, PAPER, 3, dash='22 18') + L(575, 115, 575, 605, PAPER, 3, dash='22 18')
blds = [(170, 200, 'la stazione', '#F0D9B5', BLUE), (400, 200, 'la banca', '#E6E6E6', GREY), (760, 200, 'la farmacia', PAPER, GREEN), (1010, 200, 'il museo', '#F3E3C3', '#7A4B2A'),
        (170, 500, 'il supermercato', '#FBE3DF', RED), (400, 500, 'il bar', '#FFF3D6', OCHRE), (1010, 500, "l'ufficio postale", '#FFF3D6', OCHRE)]
for x, y, lab, col, roof in blds:
    b += i_building(x, y, 62, col, roof) + T(x, y + 100, lab, 20, 700, INK, 'middle')
b += i_cross(760, 175, 12)
# piazza
b += C(760, 500, 78, '#DDE9D6', GREEN, 3) + C(760, 500, 22, SKY, BLUE, 3) + T(760, 600, 'la piazza', 20, 700, INK, 'middle')
b += i_tree(690, 470, 26) + i_tree(830, 470, 26)
# you
b += C(575, 355, 20, RED) + T(575, 363, 'IO', 16, 700, PAPER, 'middle')
b += arrow(605, 355, 700, 355, RED, 5) + T(650, 382, 'a destra', 18, 700, RED, 'middle')
b += arrow(545, 355, 450, 355, RED, 5) + T(497, 382, 'a sinistra', 18, 700, RED, 'middle')
b += arrow(575, 325, 575, 240, RED, 5) + T(540, 232, 'dritto', 18, 700, RED, 'middle')
IM['u06'] = page('Unità 6', 'In città', b, 650)

# 7 Casa
b = ''
x0, y0 = 50, 110
b += R(x0, y0, 640, 500, PAPER, rx=6, stroke=INK, sw=5)
b += L(x0 + 360, y0, x0 + 360, y0 + 280, INK, 5) + L(x0, y0 + 280, x0 + 640, y0 + 280, INK, 5) + L(x0 + 260, y0 + 280, x0 + 260, y0 + 500, INK, 5) + L(x0 + 460, y0 + 280, x0 + 460, y0 + 500, INK, 5)
# doors gaps
for (gx, gy, gw, gh) in ((x0 + 357, y0 + 180, 6, 60), (x0 + 120, y0 + 277, 60, 6), (x0 + 520, y0 + 277, 60, 6), (x0 + 300, y0 + 277, 60, 6)):
    b += R(gx, gy, gw, gh, PAPER, rx=0)
rooms = [(x0 + 180, y0 + 40, 'il soggiorno'), (x0 + 500, y0 + 40, 'la cucina'), (x0 + 130, y0 + 320, 'la camera da letto'), (x0 + 360, y0 + 320, 'il bagno'), (x0 + 550, y0 + 320, "l'ingresso")]
for x, y, lab in rooms:
    b += T(x, y, lab, 20, 700, GREEN, 'middle')
# furniture
b += R(x0 + 40, y0 + 90, 180, 60, BLUE, rx=14) + T(x0 + 130, y0 + 175, 'il divano', 17, 400, INK, 'middle')
b += R(x0 + 110, y0 + 200, 80, 44, '#C99A6B', rx=6) + T(x0 + 250, y0 + 228, 'il tavolino', 17, 400, INK, 'middle')
b += R(x0 + 420, y0 + 80, 190, 40, GREY, rx=6) + T(x0 + 515, y0 + 145, 'il frigorifero · il forno', 16, 400, INK, 'middle')
b += C(x0 + 500, y0 + 215, 40, '#C99A6B') + T(x0 + 500, y0 + 222, 'il tavolo', 15, 400, INK, 'middle')
b += R(x0 + 40, y0 + 350, 150, 110, RED, rx=10) + R(x0 + 50, y0 + 358, 55, 34, PAPER, rx=8) + T(x0 + 115, y0 + 485, 'il letto', 17, 400, INK, 'middle')
b += R(x0 + 290, y0 + 380, 60, 90, SKY, rx=20, stroke=BLUE) + T(x0 + 360, y0 + 485, 'la doccia', 17, 400, INK, 'middle')
b += R(x0 + 520, y0 + 420, 70, 26, '#7A4B2A', rx=4) + T(x0 + 555, y0 + 470, 'la porta', 17, 400, INK, 'middle')
# prepositions
b += T(740, 135, 'Dov\'è la palla?', 24, 700, INK)
preps = [('sopra', 0, -34), ('sotto', 0, 46), ('dentro', 0, 4), ('accanto a', 52, 14), ('davanti a', 0, 30), ('dietro', 0, -10)]
for i, (lab, dx, dy) in enumerate(preps):
    x = 800 + (i % 3) * 150; y = 230 + (i // 3) * 190
    if lab == 'dietro':
        b += C(x + dx - 20, y + dy - 18, 16, RED)
    if lab == 'sotto':
        b += R(x - 34, y - 28, 68, 10, '#C99A6B', rx=3) + L(x - 28, y - 18, x - 28, y + 62, '#C99A6B', 6) + L(x + 28, y - 18, x + 28, y + 62, '#C99A6B', 6)
    else:
        b += R(x - 32, y - 20, 64, 54, '#C99A6B', rx=6, stroke=INK, sw=2)
        if lab == 'dentro':
            b += R(x - 24, y - 12, 48, 38, '#8A6238', rx=4)
    if lab != 'dietro':
        b += C(x + dx, y + dy, 14 if lab != 'davanti a' else 16, RED)
    b += T(x, y + 95, lab, 20, 700, GREEN, 'middle')
IM['u07'] = page('Unità 7', 'A casa', b, 650)

# 8 Spesa
b = ''
goods = [(lambda x, y, s: i_apple(x, y, s), 'un chilo di mele'), (i_bread, 'mezzo chilo di pane'), (i_milk, 'un litro di latte'), (i_cheese, 'due etti di formaggio'),
         (i_ham, 'un etto di prosciutto'), (i_eggs, 'sei uova'), (i_pasta, 'un pacco di pasta'), (i_tomato, 'dei pomodori')]
for i, (ic, lab) in enumerate(goods):
    x = 175 + (i % 4) * 283; y = 215 + (i // 4) * 235
    b += R(x - 125, y - 100, 250, 210, PAPER, stroke=SAND) + ic(x, y - 15, 48) + T(x, y + 82, lab, 20, 700, INK, 'middle')
b += bubble(120, 600, 430, ['— Quanto costa il formaggio?'], 22, 'left', LEAF, GREEN)
b += bubble(650, 600, 430, ['— Costa due euro all\'etto.'], 22, 'right', PAPER, INK)
IM['u08'] = page('Unità 8', 'Fare la spesa', b, 720)

# 9 Tempo libero e tempo
b = ''
b += T(60, 130, 'Che tempo fa?', 24, 700, GREEN)
wx = [(i_sun, "C'è il sole."), (i_cloud, 'È nuvoloso.'), (i_rain, 'Piove.'), (i_snow, 'Nevica.'), (i_wind, 'Tira vento.')]
for i, (ic, lab) in enumerate(wx):
    x = 150 + i * 225
    b += R(x - 95, 150, 190, 170, PAPER, stroke=SAND) + ic(x, 215, 40) + T(x, 298, lab, 21, 700, INK, 'middle')
b += T(60, 375, 'Che cosa ti piace fare?', 24, 700, GREEN)
hb = [(i_book, 'leggere'), (i_note, 'ascoltare musica'), (i_ball, 'giocare a calcio'), (i_bike, 'andare in bicicletta'), (i_pot, 'cucinare'), (i_screen, 'guardare un film')]
for i, (ic, lab) in enumerate(hb):
    x = 135 + i * 186
    b += R(x - 85, 395, 170, 180, PAPER, stroke=SAND) + ic(x, 465, 38) + T(x, 552, lab, 17, 700, INK, 'middle')
IM['u09'] = page('Unità 9', 'Il tempo libero', b, 610)

# 10 Passato prossimo
b = ''
b += timeline(80, 1120, 170, [(0.12, 'ieri', 'Ho mangiato una pizza.', RED), (0.5, 'oggi', 'Mangio un panino.', GREEN), (0.9, 'domani', '', GREY)])
def aux(x, title, forms, parts, color):
    o = R(x, 290, 510, 290, PAPER, stroke=color) + T(x + 24, 330, title, 24, 700, color)
    for k, f in enumerate(forms):
        o += T(x + 40, 372 + k * 33, f, 23, 700, INK)
    o += T(x + 215, 455, '+', 34, 700, color, 'middle')
    for k, pz in enumerate(parts):
        o += T(x + 270, 405 + k * 40, pz, 23, 400, INK)
    return o
b += aux(70, 'AVERE + participio', ['ho', 'hai', 'ha', 'abbiamo', 'avete', 'hanno'], ['mangiato', 'venduto', 'dormito'], BLUE)
b += aux(620, 'ESSERE + participio', ['sono', 'sei', 'è', 'siamo', 'siete', 'sono'], ['andato / andata', '', 'andati / andate'], RED)
b += T(325, 610, 'mangiare · vendere · dormire · fare…', 19, 400, GREY, 'middle', True)
b += T(875, 610, 'andare · venire · partire · restare…', 19, 400, GREY, 'middle', True)
IM['u10'] = page('Unità 10', 'Che cosa hai fatto?', b, 640)
