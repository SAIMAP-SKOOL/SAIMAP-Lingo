from lib import *

IM = {}

# 11 casa di essere + participi irregolari
b = ''
b += T(60, 130, 'I verbi con ESSERE', 24, 700, RED)
hx, hy = 300, 370
b += R(hx - 150, hy - 90, 300, 210, SAND, rx=6, stroke=INK, sw=4)
b += f'<polygon points="{hx - 185},{hy - 85} {hx},{hy - 205} {hx + 185},{hy - 85}" fill="{RED}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
b += R(hx - 30, hy + 30, 60, 90, '#7A4B2A', rx=4) + L(hx - 150, hy + 10, hx + 150, hy + 10, INK, 3)
b += L(hx + 60, hy + 115, hx + 120, hy + 15, '#7A4B2A', 6) + L(hx + 95, hy + 115, hx + 150, hy + 25, '#7A4B2A', 6)
b += T(hx - 85, hy + 75, 'restare', 19, 700, INK, 'middle') + T(hx - 85, hy + 98, 'rimanere', 19, 700, INK, 'middle')
b += T(hx - 70, hy - 30, 'nascere', 19, 700, INK, 'middle')
b += arrow(hx - 250, hy + 85, hx - 165, hy + 85, RED, 5) + T(hx - 250, hy + 70, 'entrare', 19, 700, RED)
b += arrow(hx - 165, hy + 140, hx - 250, hy + 140, BLUE, 5) + T(hx - 250, hy + 168, 'uscire', 19, 700, BLUE)
b += arrow(hx + 170, hy + 110, hx + 220, hy + 20, RED, 5) + T(hx + 235, hy + 40, 'salire', 19, 700, RED)
b += arrow(hx + 260, hy + 70, hx + 210, hy + 150, BLUE, 5) + T(hx + 262, hy + 140, 'scendere', 19, 700, BLUE)
b += T(hx, hy + 205, 'arrivare  ·  partire  ·  andare  ·  venire  ·  tornare', 19, 700, GREY, 'middle')
b += T(660, 130, 'Participi irregolari', 24, 700, BLUE)
irr = [('fare', 'fatto'), ('dire', 'detto'), ('leggere', 'letto'), ('scrivere', 'scritto'), ('vedere', 'visto'), ('prendere', 'preso'), ('mettere', 'messo'),
       ('aprire', 'aperto'), ('chiudere', 'chiuso'), ('bere', 'bevuto'), ('venire', 'venuto'), ('essere', 'stato')]
for i, (a, p) in enumerate(irr):
    x = 660 + (i % 2) * 250; y = 160 + (i // 2) * 66
    b += R(x, y, 230, 52, PAPER, stroke=SAND) + T(x + 16, y + 34, a, 21, 400, INK) + T(x + 118, y + 34, '→', 21, 700, GREY, 'middle') + T(x + 214, y + 34, p, 21, 700, BLUE, 'end')
IM['u11'] = page('Unità 11', 'Ieri e oggi', b, 590)

# 12 Da bambino
b = ''
b += R(50, 110, 530, 470, '#EEF5E6', stroke=GREEN) + R(620, 110, 530, 470, '#E8EEF4', stroke=BLUE)
b += T(315, 155, 'DA BAMBINO', 26, 700, GREEN, 'middle') + T(885, 155, 'ADESSO', 26, 700, BLUE, 'middle')
b += i_house(170, 270, 60) + i_tree(280, 270, 50) + i_sun(480, 210, 30)
b += person(380, 420, 130, RED, 0, '#3A2A1E') + i_ball(450, 400, 24)
b += TL(90, 470, ['Abitavo in campagna.', 'Giocavo sempre a calcio.', 'Avevo un cane.'], 22, weight=700, fill=INK)
b += i_building(740, 270, 62, '#E6E6E6', GREY) + i_building(860, 290, 48, SAND, RED) + i_cloud(1060, 210, 30)
b += person(1000, 430, 190, BLUE, 0, '#3A2A1E') + i_briefcase(1085, 395, 26)
b += TL(660, 470, ['Abito in città.', 'Lavoro in un ufficio.', 'Non ho animali.'], 22, weight=700, fill=INK)
IM['u12'] = page('Unità 12', 'Da bambino', b, 610)

# 13 PP vs imperfetto
b = ''
b += T(60, 135, '1. Un\'azione in corso (imperfetto) e un fatto (passato prossimo)', 22, 700, INK)
b += R(140, 175, 760, 46, '#CFE4F4', rx=23, stroke=BLUE) + T(200, 206, 'Leggevo un libro…', 23, 700, BLUE)
b += arrow(620, 290, 620, 228, RED, 5) + C(620, 198, 13, RED) + T(620, 322, '…quando è arrivato Marco.', 23, 700, RED, 'middle')
b += arrow(80, 250, 1120, 250, GREY, 3)
b += T(60, 400, '2. Un\'abitudine (imperfetto) e una volta sola (passato prossimo)', 22, 700, INK)
for k in range(7):
    b += C(170 + k * 80, 460, 11, BLUE)
b += T(410, 505, 'Ogni estate andavo al mare.', 23, 700, BLUE, 'middle')
b += C(920, 460, 14, RED) + T(920, 505, 'Nel 2019 sono andato in montagna.', 23, 700, RED, 'middle')
b += arrow(80, 460, 1120, 460, GREY, 3)
for k in range(7):
    b += C(170 + k * 80, 460, 11, BLUE)
b += C(920, 460, 14, RED)
b += R(60, 545, 520, 56, '#CFE4F4', rx=12) + T(320, 581, 'IMPERFETTO: descrizione, abitudine, durata', 20, 700, BLUE, 'middle')
b += R(620, 545, 520, 56, ROSE, rx=12) + T(880, 581, 'PASSATO PROSSIMO: fatto concluso', 20, 700, RED, 'middle')
IM['u13'] = page('Unità 13', 'Una storia', b, 630)

# 14 In viaggio
b = ''
b += R(50, 110, 640, 300, '#1F2A30', rx=16)
b += T(80, 155, 'PARTENZE', 26, 700, OCHRE)
hdr = [('ORA', 80), ('DESTINAZIONE', 190), ('BINARIO', 450), ('RITARDO', 570)]
for t, x in hdr:
    b += T(x, 195, t, 16, 700, '#8FA0AA')
rows = [('09:15', 'Firenze S.M.N.', '4', ''), ('09:40', 'Napoli Centrale', '11', "10'"), ('10:05', 'Milano Centrale', '7', ''), ('10:30', 'Venezia S. Lucia', '2', "25'"), ('10:50', 'Bologna Centrale', '9', '')]
for i, (o, d, bi, r) in enumerate(rows):
    y = 235 + i * 38
    b += T(80, y, o, 23, 700, PAPER) + T(190, y, d, 23, 400, PAPER) + T(480, y, bi, 23, 700, '#9FE0B8', 'middle') + T(600, y, r, 23, 700, '#FF8A80', 'middle')
# ticket
b += R(730, 110, 420, 300, PAPER, stroke=GREEN, dash='10 6')
b += T(760, 155, 'BIGLIETTO', 22, 700, GREEN) + T(760, 205, 'Roma Termini', 26, 700, INK) + arrow(760, 228, 900, 228, GREY, 3) + T(760, 270, 'Firenze S.M.N.', 26, 700, INK)
b += T(760, 315, 'andata e ritorno · 2ª classe', 19, 400, INK) + T(760, 345, 'carrozza 6 · posto 42', 19, 400, INK) + T(760, 385, '39,80 €', 26, 700, RED)
tr = [(i_train, 'il treno'), (i_plane, "l'aereo"), (i_bus, "l'autobus"), (i_car, 'la macchina'), (i_suitcase, 'la valigia'), (i_key, 'la chiave')]
for i, (ic, lab) in enumerate(tr):
    x = 140 + i * 184
    b += R(x - 82, 440, 164, 160, PAPER, stroke=SAND) + ic(x, 500, 38) + T(x, 580, lab, 20, 700, INK, 'middle')
IM['u14'] = page('Unità 14', 'In viaggio', b, 630)

# 15 Corpo
b = ''
cx, by = 420, 600
b += person(cx, by, 470, '#9CC7B0', 0, '#3A2A1E')
labs = [('la testa', 620, 150, cx + 40, 160), ("l'occhio", 620, 195, cx + 28, 208), ('la bocca', 620, 240, cx + 15, 235), ('il collo', 620, 285, cx + 10, 270),
        ('la pancia', 620, 345, cx + 40, 350), ('la mano', 620, 420, cx + 135, 425), ('il ginocchio', 620, 500, cx + 40, 510), ('il piede', 620, 575, cx + 45, 585),
        ('i capelli', 60, 150, cx - 45, 140), ("l'orecchio", 60, 205, cx - 70, 205), ('il naso', 60, 250, cx - 4, 220), ('la spalla', 60, 300, cx - 80, 290),
        ('il braccio', 60, 370, cx - 105, 360), ('la schiena', 60, 430, cx - 60, 380), ('la gamba', 60, 520, cx - 40, 500)]
for lab, lx, ly, px, py in labs:
    right = lx > cx
    b += L(lx - 8 if right else lx + len(lab) * 12.5 + 8, ly - 7, px, py, GREY, 2) + C(px, py, 4, RED)
    b += T(lx, ly, lab, 22, 700, INK)
b += R(830, 120, 320, 470, PAPER, stroke=RED)
b += T(990, 165, 'Come si sente?', 23, 700, RED, 'middle')
b += i_thermo(880, 235, 30) + T(925, 243, 'Ho la febbre.', 21, 700, INK)
b += i_pill(880, 320, 26) + T(925, 315, 'Prendo una', 21, 700, INK) + T(925, 342, 'medicina.', 21, 700, INK)
b += i_cross(880, 410, 24, RED) + T(925, 403, 'Mi fa male', 21, 700, INK) + T(925, 430, 'la testa.', 21, 700, INK)
b += i_bed(885, 505, 32) + T(935, 498, 'Devo restare', 21, 700, INK) + T(935, 525, 'a letto.', 21, 700, INK)
IM['u15'] = page('Unità 15', 'Dal medico', b, 640)

# 16 Vestiti
b = ''
cl = [(i_tshirt, 'la maglietta'), (i_pants, 'i pantaloni'), (i_skirt, 'la gonna'), (i_dress, 'il vestito'), (i_jacket, 'la giacca'), (i_shoe, 'le scarpe'), (i_hat, 'il cappello'), (lambda x, y, s: i_tshirt(x, y, s, BLUE) + L(x, y - s * .45, x, y + s * .8, PAPER, 3), 'la camicia')]
for i, (ic, lab) in enumerate(cl):
    x = 150 + (i % 4) * 215; y = 210 + (i // 4) * 225
    b += R(x - 95, y - 95, 190, 200, PAPER, stroke=SAND) + ic(x, y - 12, 50) + T(x, y + 82, lab, 21, 700, INK, 'middle')
b += R(940, 115, 210, 200, PAPER, stroke=GREEN) + T(1045, 155, 'la taglia', 21, 700, GREEN, 'middle')
for i, s_ in enumerate(('S', 'M', 'L', 'XL')):
    b += C(975 + i * 47, 215, 20, LEAF if s_ != 'M' else GREEN) + T(975 + i * 47, 222, s_, 17, 700, INK if s_ != 'M' else PAPER, 'middle')
b += T(1045, 285, 'il numero: 38', 19, 400, INK, 'middle')
b += R(940, 340, 210, 200, ROSE, stroke=RED) + T(1045, 385, 'i saldi', 21, 700, RED, 'middle') + T(1045, 450, '−30%', 46, 700, RED, 'middle') + T(1045, 505, 'lo sconto', 19, 400, INK, 'middle')
b += bubble(120, 560, 420, ['— Posso provare questa giacca?'], 22, 'left', LEAF, GREEN) + bubble(600, 560, 420, ['— Certo! La vuole provare ora?'], 22, 'right')
IM['u16'] = page('Unità 16', 'Facciamo shopping', b, 680)

# 17 A tavola
b = ''
b += R(60, 110, 660, 520, PAPER, stroke='#7A4B2A', sw=3)
b += T(390, 160, 'Trattoria «Da Elena»', 30, 700, '#7A4B2A', 'middle') + T(390, 190, 'MENÙ', 18, 700, GREY, 'middle')
menu = [('Antipasti', ['Bruschetta al pomodoro  6 €', 'Prosciutto e melone  9 €']), ('Primi', ['Spaghetti alla carbonara  11 €', 'Risotto ai funghi  12 €']),
        ('Secondi', ['Pollo arrosto  13 €', 'Pesce alla griglia  16 €']), ('Contorni', ['Insalata mista  5 €', 'Patate al forno  5 €']), ('Dolci', ['Tiramisù  6 €', 'Gelato  5 €'])]
y = 232
for i, (sec, items) in enumerate(menu):
    x = 90 if i % 2 == 0 else 410
    if i == 4:
        x = 250
    b += T(x, y, sec, 23, 700, RED)
    for k, it in enumerate(items):
        b += T(x, y + 30 + k * 28, it, 18, 400, INK)
    if i % 2 == 1:
        y += 130
b += i_plate(940, 210, 62)
b += T(940, 330, 'la forchetta · il piatto · il coltello', 19, 700, INK, 'middle')
b += i_glass(880, 420, 40, '#B33A3A') + i_bottle(1000, 415, 44, '#CFE8C8')
b += T(940, 500, 'il bicchiere · la bottiglia', 19, 700, INK, 'middle')
b += bubble(780, 540, 370, ['— Il conto, per favore!'], 22, 'right', LEAF, GREEN)
IM['u17'] = page('Unità 17', 'A tavola', b, 660)

# 18 Comparativi
b = ''
ppl = [('Luca', 300, 1.90, BLUE, '#3A2A1E', False), ('Anna', 250, 1.70, RED, '#6B3E1E', True), ('Piero', 215, 1.60, GREEN, '#2A2A2A', False), ('Sara', 250, 1.70, OCHRE, '#B58A3C', True)]
base = 470
b += L(60, base, 760, base, GREY, 3)
for i, (n, h_, m_, sh, hr, lg) in enumerate(ppl):
    x = 150 + i * 175
    b += person(x, base, h_, sh, i, hr, long=lg)
    b += L(x - 62, base - h_, x + 62, base - h_, GREY, 2, dash='5 5')
    b += T(x, base + 36, n, 23, 700, INK, 'middle') + T(x, base + 62, f'{m_:.2f} m'.replace('.', ','), 19, 400, GREY, 'middle')
sent = [('Luca è più alto di Anna.', BLUE), ('Piero è meno alto di Anna.', GREEN), ('Sara è alta come Anna.', OCHRE), ('Luca è il più alto.', RED), ('Luca è altissimo!', RED)]
for i, (s_, c) in enumerate(sent):
    b += R(800, 130 + i * 84, 350, 64, PAPER, stroke=c) + T(975, 170 + i * 84, s_, 22, 700, INK, 'middle')
IM['u18'] = page('Unità 18', 'Chi è più alto?', b, 570)

# 19 Lavoro
b = ''
jobs = [(i_cross, 'il medico', "l'ospedale"), (i_book, "l'insegnante", 'la scuola'), (i_pot, 'il cuoco', 'il ristorante'), (i_briefcase, "l'impiegato", "l'ufficio"),
        (i_car, 'il meccanico', "l'officina"), (i_cap, 'lo studente', "l'università")]
for i, (ic, lab, pl) in enumerate(jobs):
    x = 135 + i * 186
    b += R(x - 85, 115, 170, 205, PAPER, stroke=SAND) + ic(x, 185, 40) + T(x, 268, lab, 20, 700, INK, 'middle') + T(x, 296, pl, 17, 400, GREY, 'middle')
b += R(60, 350, 1080, 230, PAPER, stroke=GREEN)
b += T(90, 395, 'Che cosa stai facendo?', 24, 700, GREEN)
b += T(90, 450, 'STARE', 26, 700, BLUE) + T(210, 450, '+', 30, 700, GREY, 'middle') + T(240, 450, 'GERUNDIO', 26, 700, RED)
b += T(90, 495, 'sto · stai · sta · stiamo · state · stanno', 21, 400, INK)
for i, (inf, ger) in enumerate((('lavorare', 'lavorando'), ('scrivere', 'scrivendo'), ('dormire', 'dormendo'))):
    b += T(640, 420 + i * 46, inf, 22, 400, INK) + T(790, 420 + i * 46, '→', 22, 700, GREY, 'middle') + T(830, 420 + i * 46, ger, 22, 700, RED)
b += T(90, 550, 'Adesso sto lavorando.   ·   I bambini stanno dormendo.', 21, 700, INK)
IM['u19'] = page('Unità 19', 'Lavoro e studio', b, 610)

# 20 Ci vediamo
b = ''
b += R(90, 105, 460, 520, INK, rx=44) + R(108, 150, 424, 430, '#EAF0F3', rx=10) + C(320, 602, 12, GREY)
b += T(320, 136, 'Giulia', 18, 700, PAPER, 'middle')
msgs = [(0, ['Ciao! Ti va di andare', 'al cinema stasera?']), (1, ['Volentieri! A che ora?']), (0, ['Alle otto. Ci vediamo', 'davanti al cinema?']), (1, ["D'accordo. A dopo!"])]
y = 168
for side, ls in msgs:
    w_ = max(len(l) for l in ls) * 11.2 + 34; h_ = len(ls) * 27 + 20
    x = 124 if side == 0 else 516 - w_
    b += R(x, y, w_, h_, PAPER if side == 0 else '#CFEBD9', rx=16)
    for k, l in enumerate(ls):
        b += T(x + 16, y + 28 + k * 27, l, 20, 400, INK)
    y += h_ + 16
b += R(600, 115, 540, 240, PAPER, stroke=GREEN) + T(630, 160, 'Per invitare', 23, 700, GREEN)
b += TL(630, 200, ['Ti va di + infinito?', 'Vuoi venire a…?', 'Che ne dici di + infinito?', 'Perché non andiamo a…?'], 21, 34)
b += R(600, 380, 255, 245, LEAF, stroke=GREEN) + T(727, 422, 'Accettare', 22, 700, GREEN, 'middle')
b += TL(727, 462, ['Volentieri!', "D'accordo.", 'Buona idea!', 'Perché no?'], 20, 34, anchor='middle')
b += R(885, 380, 255, 245, ROSE, stroke=RED) + T(1012, 422, 'Rifiutare', 22, 700, RED, 'middle')
b += TL(1012, 462, ['Mi dispiace, non posso.', 'Purtroppo ho da fare.', 'Magari un\'altra volta.', 'Veramente preferirei…'], 19, 34, anchor='middle')
IM['u20'] = page('Unità 20', 'Ci vediamo!', b, 660)
