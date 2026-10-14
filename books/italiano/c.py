from lib import *

IM = {}

# 38 Registri
b = ''
b += f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{OCHRE}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient></defs>'
b += f'<rect x="60" y="120" width="1080" height="26" rx="13" fill="url(#g)"/>'
b += T(60, 180, 'più informale', 19, 700, '#B5811F') + T(1140, 180, 'più formale', 19, 700, BLUE, 'end')
regs = [('COLLOQUIALE', 'tra amici', 'Dai, dammi una mano!', OCHRE), ('NEUTRO', 'con conoscenti', 'Mi aiuti, per favore?', GREEN),
        ('FORMALE', 'con un cliente, un superiore', 'Potrebbe aiutarmi, per cortesia?', BLUE), ('BUROCRATICO', 'in un avviso pubblico', 'Si prega di prestare assistenza.', '#5B4A6B')]
for i, (r, ctx, ex, c) in enumerate(regs):
    y = 210 + i * 100
    b += R(60 + i * 40, y, 960, 84, PAPER, stroke=c, sw=3)
    b += T(85 + i * 40, y + 36, r, 21, 700, c) + T(85 + i * 40, y + 64, ctx, 17, 400, GREY)
    b += T(1000 + i * 40, y + 52, ex, 23, 700, INK, 'end')
IM['u38'] = page('Unità 38', 'Questione di registro', b, 630)

# 39 Frase marcata
b = ''
def seg(x, y, txt, fill, color=INK, size=23):
    w_ = len(txt) * size * .57 + 28
    return R(x, y, w_, 54, fill, rx=12) + T(x + w_ / 2, y + 36, txt, size, 700, color, 'middle'), w_
rowsd = [('Ordine normale', [('Marco', '#CFE4F4', BLUE), ('ha comprato', PAPER, INK), ('il giornale.', ROSE, RED)], 'frase neutra'),
         ('Dislocazione a sinistra', [('Il giornale,', ROSE, RED), ("l'", '#FFF3D6', '#B5811F'), ('ha comprato', PAPER, INK), ('Marco.', '#CFE4F4', BLUE)], "il tema va all'inizio + pronome"),
         ('Dislocazione a destra', [("L'", '#FFF3D6', '#B5811F'), ('ha comprato', PAPER, INK), ('Marco,', '#CFE4F4', BLUE), ('il giornale.', ROSE, RED)], 'pronome + tema alla fine'),
         ('Frase scissa', [('È', LEAF, GREEN), ('Marco', '#CFE4F4', BLUE), ('che', LEAF, GREEN), ('ha comprato', PAPER, INK), ('il giornale.', ROSE, RED)], 'essere + elemento in rilievo + che')]
for i, (name, segs, note) in enumerate(rowsd):
    y = 118 + i * 128
    b += T(60, y + 16, name, 21, 700, GREEN) + T(1140, y + 16, note, 17, 400, GREY, 'end', True)
    x = 60
    for txt, f, c in segs:
        s_, w_ = seg(x, y + 32, txt, f, c)
        b += s_
        x += w_ + 10
IM['u39'] = page('Unità 39', 'La frase marcata', b, 640)

# 40 Implicite
b = ''
b += T(330, 135, 'ESPLICITA · verbo coniugato', 20, 700, GREY, 'middle') + T(870, 135, 'IMPLICITA · modo indefinito', 20, 700, GREEN, 'middle')
pairs = [('Mentre camminavo, pensavo a te.', 'Camminando, pensavo a te.', 'gerundio', BLUE),
         ('Poiché era stanco, andò a letto.', 'Essendo stanco, andò a letto.', 'gerundio', BLUE),
         ('Dopo che ebbe finito il lavoro, uscì.', 'Finito il lavoro, uscì.', 'participio', RED),
         ('Prima che io parta, ti chiamo.', 'Prima di partire, ti chiamo.', 'infinito', OCHRE),
         ('Credo che io abbia ragione.', 'Credo di avere ragione.', 'infinito', OCHRE)]
for i, (e, im, mode, c) in enumerate(pairs):
    y = 160 + i * 92
    b += R(60, y, 540, 74, PAPER, stroke=SAND) + T(80, y + 46, e, 21, 400, INK)
    b += arrow(608, y + 37, 652, y + 37, c, 4)
    b += R(660, y, 480, 74, PAPER, stroke=c, sw=3) + T(680, y + 46, im, 21, 700, INK) + T(1125, y + 24, mode, 15, 700, c, 'end')
b += T(600, 648, 'La forma implicita è possibile quando il soggetto è lo stesso nelle due frasi.', 19, 400, GREY, 'middle', True)
IM['u40'] = page('Unità 40', 'Dire molto con poco', b, 680)

# 41 Congiuntivo avanzato
b = ''
b += R(60, 112, 520, 250, PAPER, stroke=BLUE) + T(85, 150, 'Nelle frasi indipendenti', 22, 700, BLUE)
ind = [('Desiderio', 'Magari piovesse!'), ('Dubbio', 'Che sia già partito?'), ('Esortazione', 'Che entri pure!'), ('Augurio', 'Che tu sia felice!')]
for i, (t, e) in enumerate(ind):
    b += T(85, 195 + i * 44, t, 19, 700, GREY) + T(555, 195 + i * 44, e, 21, 700, INK, 'end')
b += R(620, 112, 520, 250, PAPER, stroke=RED) + T(645, 150, 'Dopo espressioni particolari', 22, 700, RED)
sp = [('superlativo relativo', 'È il libro più bello che abbia letto.'), ('indefiniti', 'Chiunque venga, è benvenuto.'), ('frase negata', 'Non dico che sia facile.'), ('limitazione', 'Che io sappia, no.')]
for i, (t, e) in enumerate(sp):
    b += T(645, 193 + i * 44, t, 14, 700, GREY) + T(1115, 195 + i * 44, e, 17, 700, INK, 'end')
b += R(60, 392, 1080, 230, PAPER, stroke=GREEN) + T(85, 430, 'Indicativo o congiuntivo? Cambia il significato', 22, 700, GREEN)
pr = [('Cerco una segretaria che parla russo.', 'So che esiste: è una persona precisa.'), ('Cerco una segretaria che parli russo.', 'Non so se esiste: è un requisito.'),
      ('Dicono che è partito.', 'Riferisco un fatto.'), ('Dicono che sia partito.', 'Riferisco una voce, non sono sicuro.')]
for i, (e, n) in enumerate(pr):
    y = 475 + i * 40
    b += T(85, y, e, 20, 700, INK) + T(1115, y, n, 18, 400, GREY, 'end', True)
IM['u41'] = page('Unità 41', 'Sfumature del congiuntivo', b, 650)

# 42 Connettivi
b = ''
cn = [('Aggiungere', ['inoltre', 'per di più', 'oltretutto', 'del resto'], GREEN), ('Opporre', ['tuttavia', 'eppure', 'bensì', 'al contrario'], RED),
      ('Spiegare la causa', ['poiché', 'dato che', 'in quanto', 'visto che'], BLUE), ('Trarre la conseguenza', ['pertanto', 'dunque', 'di conseguenza', 'perciò'], OCHRE),
      ('Concedere', ['sebbene', 'pur + gerundio', 'per quanto', 'ciononostante'], '#5B4A6B'), ('Precisare', ['ossia', 'vale a dire', 'in altre parole', 'ad esempio'], '#7A4B2A'),
      ('Ordinare', ['innanzitutto', 'in secondo luogo', 'infine'], GREY), ('Concludere', ['insomma', 'in definitiva', 'in sintesi', 'tutto sommato'], INK)]
for i, (t, ws, c) in enumerate(cn):
    x = 60 + (i % 4) * 272; y = 115 + (i // 4) * 270
    b += R(x, y, 258, 250, PAPER, stroke=c, sw=3) + R(x, y, 258, 54, c, rx=14) + R(x, y + 34, 258, 20, c, rx=0)
    b += T(x + 129, y + 36, t, 19, 700, PAPER, 'middle')
    for k, w_ in enumerate(ws):
        b += T(x + 129, y + 96 + k * 40, w_, 21, 700, INK, 'middle')
IM['u42'] = page('Unità 42', 'Il filo del discorso', b, 670)

# 43 Modi di dire
b = ''
idi = [(i_wolf, 'In bocca al lupo!', 'Buona fortuna!'), (lambda x, y, s: ''.join(i_cat(x + dx, y + dy, s * .42) for dx, dy in ((-34, -18), (34, -18), (-34, 26), (34, 26))), "C'erano quattro gatti.", "C'era pochissima gente."),
       (i_rain, 'Piove sul bagnato.', 'I problemi arrivano a chi ne ha già.'), (i_euro, 'Costa un occhio della testa.', 'È carissimo.'),
       (lambda x, y, s: R(x - s * .8, y - s * .5, s * 1.6, s * 1.05, GREEN, rx=8, stroke=INK, sw=3) + R(x + s * .2, y - s * .1, s * .65, s * .3, '#1F5C42', rx=6), 'Sono al verde.', 'Non ho più soldi.'),
       (i_heart, 'Avere il cuore in gola.', 'Avere molta paura o emozione.')]
for i, (ic, idiom, mean) in enumerate(idi):
    x = 235 + (i % 3) * 365; y = 215 + (i // 3) * 255
    b += R(x - 172, y - 100, 344, 235, PAPER, stroke=SAND) + ic(x, y - 28, 44) + T(x, y + 62, idiom, 21, 700, INK, 'middle') + T(x, y + 96, mean, 16, 400, GREEN, 'middle')
IM['u43'] = page('Unità 43', 'In bocca al lupo!', b, 630)

# 44 Lavoro
b = ''
b += R(60, 112, 560, 520, PAPER, stroke=INK, sw=3)
b += T(340, 158, 'RELAZIONE', 24, 700, INK, 'middle') + L(90, 176, 590, 176, SAND, 2)
secs = [('Oggetto', 'Di che cosa tratta il documento', BLUE), ('Premessa', 'Contesto e obiettivi', GREEN), ('Analisi', 'Dati, fatti, problemi riscontrati', OCHRE), ('Proposte', 'Soluzioni e tempi', RED), ('Conclusioni', 'Sintesi e prossimi passi', '#5B4A6B')]
for i, (t, d, c) in enumerate(secs):
    y = 200 + i * 84
    b += R(90, y, 8, 62, c, rx=4) + T(116, y + 26, t, 22, 700, c) + T(116, y + 54, d, 18, 400, INK)
b += R(660, 112, 480, 520, PAPER, stroke=GREEN) + T(685, 152, 'In riunione', 23, 700, GREEN)
ph = [('Aprire', 'Direi di cominciare.'), ('Prendere la parola', 'Se posso aggiungere una cosa…'), ('Chiedere chiarimenti', 'Che cosa intende esattamente?'),
      ('Dissentire con garbo', 'Capisco, ma non sono del tutto d\'accordo.'), ('Riassumere', 'Ricapitolando, abbiamo deciso che…'), ('Chiudere', 'Direi che per oggi è tutto.')]
for i, (t, e) in enumerate(ph):
    y = 190 + i * 72
    b += T(685, y, t, 16, 700, GREY) + T(685, y + 28, e, 20, 700, INK)
IM['u44'] = page('Unità 44', 'Italiano per il lavoro', b, 660)

# 45 Varietà
b = ''
cx, cy = 400, 370
b += C(cx, cy, 230, '#EEF5E6', GREEN, 3) + C(cx, cy, 150, '#DCEEE3', GREEN, 3) + C(cx, cy, 78, GREEN)
b += T(cx, cy - 4, 'italiano', 20, 700, PAPER, 'middle') + T(cx, cy + 22, 'standard', 20, 700, PAPER, 'middle')
b += T(cx, cy - 105, 'italiano neostandard', 19, 700, GREEN, 'middle') + T(cx, cy - 185, 'italiani regionali · dialetti', 19, 700, GREEN, 'middle')
ax = [('DOVE', 'variazione geografica', 'Roma, Milano, Napoli…', BLUE), ('CHI', 'variazione sociale', 'età, istruzione, gruppo', RED), ('IN QUALE SITUAZIONE', 'registro', 'formale o informale', OCHRE), ('CON QUALE MEZZO', 'canale', 'parlato, scritto, digitale', '#5B4A6B')]
for i, (q, n, e, c) in enumerate(ax):
    y = 118 + i * 128
    b += R(700, y, 440, 110, PAPER, stroke=c, sw=3) + T(722, y + 36, q, 20, 700, c) + T(722, y + 66, n, 20, 700, INK) + T(722, y + 94, e, 17, 400, GREY)
    b += L(cx + 232 if i in (1, 2) else cx + 200, cy + (-110, -35, 35, 110)[i], 700, y + 55, c, 2, dash='5 5')
b += T(cx, 635, 'la stessa cosa, tre parole:  anguria (Nord) · cocomero (Centro) · melone d\'acqua (Sud)', 17, 400, INK, 'middle', True)
IM['u45'] = page('Unità 45', 'Tanti italiani', b, 660)

# 46 Storia della lingua
b = ''
y = 300
b += arrow(60, y, 1150, y, INK, 4)
ev = [(110, '960', 'Placito capuano', 'primo documento', 'in volgare', 0), (260, '1321', 'Dante', 'Divina', 'Commedia', 1), (400, '1525', 'Bembo', 'il toscano', 'come modello', 0),
      (540, '1612', 'Crusca', 'primo', 'Vocabolario', 1), (690, '1840', 'Manzoni', 'I promessi sposi', '(ed. definitiva)', 0), (830, '1861', "Unità d'Italia", 'pochi parlano', 'italiano', 1),
      (960, '1954', 'Televisione', "l'italiano entra", 'in tutte le case', 0), (1085, 'oggi', 'Neostandard', 'lingua di tutti', '', 1)]
cols_ = [BLUE, RED, GREEN, OCHRE, '#5B4A6B', RED, BLUE, GREEN]
for (x, yr, t, l1, l2, down), c in zip(ev, cols_):
    b += C(x, y, 12, c)
    if down:
        b += L(x, y + 12, x, y + 50, c, 2) + T(x, y + 76, yr, 22, 700, c, 'middle') + T(x, y + 104, t, 18, 700, INK, 'middle') + T(x, y + 128, l1, 15, 400, GREY, 'middle') + T(x, y + 148, l2, 15, 400, GREY, 'middle')
    else:
        b += L(x, y - 12, x, y - 50, c, 2) + T(x, y - 138, yr, 22, 700, c, 'middle') + T(x, y - 110, t, 18, 700, INK, 'middle') + T(x, y - 86, l1, 15, 400, GREY, 'middle') + T(x, y - 66, l2, 15, 400, GREY, 'middle')
IM['u46'] = page('Unità 46', 'La lingua letteraria', b, 500)

# 47 Linguaggi specialistici
b = ''
sp_ = [(i_scale, 'GIURIDICO', ['formule fisse', 'latinismi', 'frasi molto lunghe'], '«Il contratto si intende risolto di diritto.»', BLUE),
       (i_stamp, 'BUROCRATICO', ['nomi al posto dei verbi', 'forme impersonali', 'parole rare'], '«Si prega di obliterare il titolo di viaggio.»', '#5B4A6B'),
       (i_flask, 'SCIENTIFICO', ['termini con un solo senso', 'passivo e impersonale', 'dati e definizioni'], '«I campioni sono stati analizzati in triplo.»', GREEN)]
for i, (ic, t, feats, ex, c) in enumerate(sp_):
    x = 60 + i * 365
    b += R(x, 112, 345, 400, PAPER, stroke=c, sw=3) + ic(x + 172, 185, 44) + T(x + 172, 275, t, 23, 700, c, 'middle')
    for k, f in enumerate(feats):
        b += C(x + 34, 312 + k * 36, 5, c) + T(x + 50, 319 + k * 36, f, 19, 400, INK)
    words = ex.split(' '); lines = ['']
    for w_ in words:
        if len(lines[-1]) + len(w_) > 30:
            lines.append('')
        lines[-1] = (lines[-1] + ' ' + w_).strip()
    for k, l in enumerate(lines):
        b += T(x + 172, 440 + k * 26, l, 17, 400, GREY, 'middle', True)
b += R(60, 540, 1080, 70, LEAF, rx=12) + T(600, 584, 'In parole semplici:  «obliterare il titolo di viaggio»  =  timbrare il biglietto', 21, 700, GREEN, 'middle')
IM['u47'] = page('Unità 47', 'Linguaggi specialistici', b, 640)

# 48 Stile
b = ''
fg = [('Litote', '«Non è male.»', 'nego il contrario: è buono', i_speech, GREEN), ('Ironia', '«Che bella giornata!»', 'dico il contrario di ciò che penso', i_rain, BLUE),
      ('Iperbole', '«Te l\'ho detto mille volte!»', 'esagero per dare forza', i_mic, RED), ('Eufemismo', '«È venuto a mancare.»', 'attenuo una parola dura', i_heart, '#5B4A6B'),
      ('Metafora', '«Sei il mio sole.»', 'una cosa al posto di un\'altra', i_sun, OCHRE), ('Similitudine', '«Furbo come una volpe.»', 'un paragone con «come»', i_wolf, '#7A4B2A')]
for i, (t, ex, d, ic, c) in enumerate(fg):
    x = 60 + (i % 3) * 365; y = 112 + (i // 3) * 262
    b += R(x, y, 345, 244, PAPER, stroke=c, sw=3) + T(x + 20, y + 40, t, 23, 700, c)
    b += (ic(x + 290, y + 48, 26, c) if ic in (i_speech, i_heart) else ic(x + 290, y + 48, 26))
    b += T(x + 172, y + 135, ex, 22, 700, INK, 'middle') + T(x + 172, y + 195, d, 17, 400, GREY, 'middle')
IM['u48'] = page('Unità 48', 'Stile', b, 660)

# 49 Finezze
b = ''
b += T(330, 135, 'CORRETTO', 20, 700, GREEN, 'middle') + T(870, 135, 'ERRORE FREQUENTE', 20, 700, RED, 'middle')
du = [('qual è', "qual'è", 'troncamento, senza apostrofo'), ("un po'", 'un pò', 'apocope di «poco»: apostrofo'), ('perché, né, sé', 'perchè, nè, sè', 'accento acuto'),
      ('è, cioè, caffè', 'é, cioé, caffé', 'accento grave'), ("d'accordo", 'daccordo', 'due parole'), ('dà (verbo), sì, là', 'da, si, la', "l'accento distingue"), ('purtroppo, proprio', 'pultroppo, propio', 'attenzione alla r')]
for i, (ok, no, why) in enumerate(du):
    y = 158 + i * 66
    b += R(60, y, 540, 54, LEAF, rx=12) + C(92, y + 27, 15, GREEN) + P(f'M84,{y + 27} l6,6 l11,-12', stroke=PAPER, sw=4) + T(125, y + 36, ok, 23, 700, INK) + T(585, y + 34, why, 15, 400, GREY, 'end')
    b += R(640, y, 500, 54, ROSE, rx=12) + C(672, y + 27, 15, RED) + P(f'M665,{y + 20} l14,14 M679,{y + 20} l-14,14', stroke=PAPER, sw=4) + T(705, y + 36, no, 23, 700, INK)
IM['u49'] = page('Unità 49', 'Finezze', b, 650)

# 50 Discorso
b = ''
b += i_mic(120, 230, 70)
ph_ = [('1', 'Apertura', 'Catturo l\'attenzione', 'una domanda, un aneddoto, un dato', GREEN), ('2', 'Esposizione', 'Presento il tema e la tesi', 'chiaro, breve, ordinato', BLUE),
       ('3', 'Argomentazione', 'Dimostro con prove', 'esempi, dati, autorità', OCHRE), ('4', 'Confutazione', 'Rispondo alle obiezioni', 'riconosco e supero', RED), ('5', 'Chiusura', 'Lascio un messaggio', 'sintesi e appello finale', '#5B4A6B')]
import math as _m
for i, (n, t, d, how, c) in enumerate(ph_):
    y = 112 + i * 96
    b += R(250, y, 890, 82, PAPER, stroke=c, sw=3) + C(296, y + 41, 24, c) + T(296, y + 50, n, 24, 700, PAPER, 'middle')
    b += T(338, y + 36, t, 23, 700, c) + T(338, y + 64, d, 18, 400, INK) + T(1120, y + 50, how, 18, 400, GREY, 'end', True)
b += T(120, 380, 'il discorso', 20, 700, INK, 'middle') + T(120, 406, 'in pubblico', 20, 700, INK, 'middle')
b += R(60, 600, 1080, 60, LEAF, rx=12) + T(600, 638, 'Prima di consegnare: rileggi ad alta voce, taglia il superfluo, controlla i connettivi.', 20, 700, GREEN, 'middle')
IM['u50'] = page('Unità 50', 'Da maestri', b, 690)

# Intro: scala dei livelli
b = ''
lv = [('A1', 'Primi passi', 'Mi presento', '#8FBF9F'), ('A2', 'Sopravvivenza', 'Racconto e viaggio', '#5FA47A'), ('B1', 'Soglia', 'Esprimo opinioni', GREEN),
      ('B2', 'Progresso', 'Argomento', BLUE), ('C1', 'Efficacia', 'Uso i registri', '#5B4A6B'), ('C2', 'Padronanza', 'Padroneggio lo stile', RED)]
for i, (l, n, d, c) in enumerate(lv):
    x = 60 + i * 180; h_ = 110 + i * 62
    y = 560 - h_
    b += R(x, y, 172, h_, c, rx=12) + T(x + 86, y + 48, l, 38, 700, PAPER, 'middle') + T(x + 86, y + 78, n, 18, 700, PAPER, 'middle')
    if h_ > 150:
        b += T(x + 86, y + 108, d, 15, 400, PAPER, 'middle')
    b += T(x + 86, 592, ['unità 1–10', 'unità 11–20', 'unità 21–29', 'unità 30–37', 'unità 38–44', 'unità 45–50'][i], 17, 700, INK, 'middle')
b += person(110, 450 - 0, 0.1) if False else ''
b += T(60, 140, 'Base', 20, 700, '#5FA47A') + T(420, 140, 'Autonomia', 20, 700, BLUE) + T(780, 140, 'Padronanza', 20, 700, RED)
IM['intro_livelli'] = page('', 'I sei livelli del corso', b, 620, 'Quadro comune europeo (QCER)')

# Intro: pronuncia
b = ''
def snd(x, y, letters, sound, ex1, ex2, c):
    o = R(x, y, 345, 150, PAPER, stroke=c, sw=3)
    o += T(x + 20, y + 44, letters, 22, 700, c) + T(x + 325, y + 44, sound, 22, 700, INK, 'end')
    o += T(x + 20, y + 90, ex1, 20, 400, INK) + T(x + 20, y + 122, ex2, 20, 400, INK)
    return o
b += T(60, 135, 'C e G: due suoni', 22, 700, GREEN)
b += snd(60, 155, 'ca · co · cu · che · chi', '[k]', 'casa · amico · cuore', 'che · chiave · perché', BLUE)
b += snd(425, 155, 'ce · ci · cia · cio · ciu', '[tʃ]', 'cena · cinema · ciao', 'come «ch» in «chico»', RED)
b += snd(790, 155, 'sce · sci', '[ʃ]', 'pesce · uscire · sciarpa', 'come «sh» in inglese', '#5B4A6B')
b += snd(60, 325, 'ga · go · gu · ghe · ghi', '[g]', 'gatto · lago · gusto', 'spaghetti · ghiaccio', BLUE)
b += snd(425, 325, 'ge · gi · gia · gio · giu', '[dʒ]', 'gelato · giro · giorno', 'come «j» in inglese «job»', RED)
b += snd(790, 325, 'gn · gli', '[ɲ] [ʎ]', 'gnocchi · bagno = «ñ»', 'famiglia · figlio = «ll»', '#5B4A6B')
b += T(60, 520, 'Le doppie cambiano la parola', 22, 700, GREEN)
for i, (a, z) in enumerate((('casa', 'cassa'), ('pala', 'palla'), ('nono', 'nonno'), ('sete', 'sette'), ('capello', 'cappello'))):
    x = 60 + i * 218
    b += R(x, 540, 206, 64, LEAF, rx=12) + T(x + 103, 580, f'{a}  ≠  {z}', 21, 700, INK, 'middle')
IM['intro_suoni'] = page('', 'Suoni e lettere', b, 640, 'guida rapida alla pronuncia')
