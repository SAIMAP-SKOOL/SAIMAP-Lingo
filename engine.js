// SAIMAP Lingo · motor de lecciones (sin DOM: se puede probar con Node)
(function (g) {
  const C = g.COURSE;
  const REVIEW_RATIO = 0.3;   // parte de cada lección que sale de módulos anteriores
  const LESSON_SIZE = 13, CHECKPOINT_SIZE = 15, CHECKPOINT_REVIEW = 6, DAILY_SIZE = 26;   // el repaso del día tiene el doble que una lección
  const PROPER = new Set("Marco Lucía Paolo Rossi Siviglia Pierre Anna Hans Berlino Milano Roma Madrid Franco Giulia Sofia Luca Carlo Matteo Rita Elena Lei Italia Spagna Diego Marie TV Firenze Chiara Venezia Briciola Sicilia Sara Piero Natale Uffizi Marta Gino San Lorenzo Bianchi Dante Bologna Lisbona Napoli Parigi Comune Conti Carlo Calvino Manzoni Petrarca Boccaccio Alghero Toscana Sud Nord Irene Giorgio Juan Commedia Decameron Alto Adige Torino Novecento Trecento Ottocento Cinquecento".split(" ").concat((C.proper || "").split(" ")));

  const ITEMS = [], BY = {};
  C.units.forEach(u => u.mods.forEach((m, mi) => {
    const NB = (C.ui && C.ui.nbsp) ? t => String(t).replace(/ ([?!:;])/g, "\u202f$1") : t => t;   // tipografía francesa: espacio fino antes de ? ! : ;
    const add = (kind, i, o) => { ["it", "q"].forEach(f => { if (o[f]) o[f] = NB(o[f]); }); const it = Object.assign({ k: u.n + "." + (mi + 1) + "." + kind + i, kind, u: u.n, m: mi + 1 }, o); ITEMS.push(it); BY[it.k] = it; };
    m.v.forEach((x, i) => { const p = x.indexOf("="), it = x.slice(0, p); add("v", i, { it, es: x.slice(p + 1), pic: (g.PICS || {})[it] || "" }); });
    m.s.forEach((x, i) => { const a = x.split("|"); add("s", i, { it: a[0], es: a[1] }); });
    m.g.forEach((x, i) => { const a = x.split("|"); // «—» como respuesta = hueco vacío (sin artículo, sin preposición): la frase completa se forma quitando el hueco.
      const full = a[1] === "—" ? a[0].replace(/___ ?/, "").replace(/^./, c => c.toUpperCase()) : a[0].replace("___", a[1]).replace(/(^|[\s(])((?:[a-zA-Z]{1,2}|qu|jusqu|lorsqu|puisqu|de l|à l)')\s+/g, "$1$2");
      add("g", i, { q: a[0], a: a[1], o: [a[2], a[3]], es: a[4], it: full }); });
  }));

  const ord = (u, m) => (u - 1) * 5 + m;
  const modId = (u, m) => u + "." + m;
  const modInfo = (u, m) => {
    const unit = C.units[u - 1];
    return m <= 4 ? unit.mods[m - 1] : { t: (C.ui && C.ui.review) || "Ripasso", es: "Repaso de la unidad " + u + " y de las anteriores", tip: "" };
  };
  const rnd = n => Math.floor(Math.random() * n);
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = rnd(i + 1); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const st = (S, k) => S.it[k] || [0, 0, 0];
  const ranked = (arr, score) => arr.map(i => [score(i), i]).sort((a, b) => b[0] - a[0]).map(x => x[1]);

  // ui.keepCase (alemán): los sustantivos conservan la mayúscula; la primera palabra solo si en el curso aparece con mayúscula a mitad de frase.
  const CAPS = new Set(), LOWER = new Set();
  if (C.ui && C.ui.keepCase) for (const u of C.units) for (const m of u.mods) for (const x of [].concat(m.v, m.s, m.g)) {
    const t = String(x).split(/[|=]/)[0].split(/\s+/).filter(Boolean);
    t.forEach((w, i) => { const c = w.replace(/[.,!?;:—–„“”"«»()]/g, ""); if (i > 0 && !/[.!?:…]["“”»]?$/.test(t[i - 1]) && !/^[„“"«(]/.test(w)) (/^[A-ZÄÖÜ]/.test(c) ? CAPS : LOWER).add(c); });
    if (/[=]/.test(String(x)) && /^(der|die|das) /.test(x)) { const n = String(x).split("=")[0].split(" ")[1]; if (n) CAPS.add(n.replace(/,$/, "")); }
  }
  function tokens(text) {
    const ws = text.replace(/[.,!?;:—–„“”«»·\u0387\u037E]/g, " ").split(/\s+/).filter(Boolean);
    if (C.ui && C.ui.keepCase) return ws.map((w, i) => i > 0 || PROPER.has(w) || (CAPS.has(w) && !LOWER.has(w.toLowerCase())) ? w : w.toLowerCase());
    return ws.map(w => PROPER.has(w) ? w : w.toLowerCase());
  }
  // Griego: «;» es la interrogación, la σ final se acepta en lugar de ς y se unifica la composición (NFC).
  const norm = s => s.normalize("NFC").toLowerCase().replace(/ß/g, "ss").replace(/[’`´]/g, "'").replace(/[.!?¿¡„“”«»;·\u0387\u037E]/g, "").replace(/\s+/g, " ").trim().replace(/σ(?=[\s',]|$)/g, "ς");
  const DE = C.ui && C.ui.keepCase;
  const bare = s => { const b = norm(s).normalize("NFD").replace(/[̀-ͯ]/g, ""); return DE ? b.replace(/([aou])e/g, "$1") : b; };
  const typable = it => !/[\/,(?=→]/.test(it.it) && it.it.split(" ").length <= 3;
  // Se puede leer en voz alta: sin barras, paréntesis ni cifras, y no demasiado larga.
  const speakable = it => !/[\/(=→…_\d]/.test(it.it) && it.it.split(/\s+/).length <= 10;

  function distract(pool, correct, n, field) {
    const out = [], seen = new Set([norm(correct)]);
    for (const p of shuffle(pool)) { const t = p[field]; if (!seen.has(norm(t))) { seen.add(norm(t)); out.push(t); if (out.length === n) break; } }
    return out;
  }
  // Construye el ejercicio concreto (opciones, fichas) a partir de un ítem.
  function build(item, type, review) {
    const ex = { type, item, review: !!review };
    const sameMod = ITEMS.filter(i => i.kind === item.kind && i.u === item.u && i.m === item.m && i !== item);
    const sameUnit = ITEMS.filter(i => i.kind === item.kind && i.u === item.u && i.m !== item.m);
    const pool = n => { let d = distract(sameMod, type === "mcIE" || type === "mcS" ? item.es : item.it, n, type === "mcIE" || type === "mcS" ? "es" : "it"); if (d.length < n) d = d.concat(distract(sameUnit, "", n * 3, type === "mcIE" || type === "mcS" ? "es" : "it").filter(x => !d.includes(x) && norm(x) !== norm(type === "mcIE" || type === "mcS" ? item.es : item.it)).slice(0, n - d.length)); return d; };
    if (type === "picIE") {
      const near = ITEMS.filter(i => i.pic && i.pic !== item.pic).sort((a, b) => Math.abs(a.u - item.u) - Math.abs(b.u - item.u)).slice(0, 14), d = distract(near, item.pic, 3, "pic");
      if (d.length < 3) return build(item, "mcIE", review);
      ex.answer = item.pic; ex.options = shuffle([item.pic].concat(d)); return ex;
    }
    if (type === "picEI") { ex.answer = item.it; ex.options = shuffle([item.it].concat(pool(3))); return ex; }
    if (type === "mcIE") { ex.answer = item.es; ex.options = shuffle([item.es].concat(pool(3))); }
    else if (type === "mcEI" || type === "listen") { ex.answer = item.it; ex.options = shuffle([item.it].concat(pool(3))); }
    else if (type === "mcS") { ex.answer = item.es; ex.options = shuffle([item.es].concat(pool(2))); }
    else if (type === "gap") { ex.answer = item.a; ex.options = shuffle([item.a].concat(item.o)); }
    else if (type === "type" || type === "speak") { ex.answer = item.it; }
    else if (type === "order" || type === "listenOrder") {
      ex.tokens = tokens(item.it);
      const have = new Set(ex.tokens.map(t => t.toLowerCase())), extra = [];
      for (const s of shuffle(sameMod.concat(sameUnit))) for (const t of shuffle(tokens(s.it))) {
        if (extra.length < 3 && !have.has(t.toLowerCase())) { have.add(t.toLowerCase()); extra.push(t); }
      }
      ex.bank = shuffle(ex.tokens.concat(extra)); ex.answer = item.it;
    }
    return ex;
  }
  function typeFor(item, S, o) {
    if (item.kind === "g") return "gap";
    const seen = st(S, item.k)[0] + st(S, item.k)[1];
    if (item.kind === "v") {
      if (!seen) return "mcIE";
      const t = ["mcIE", "mcEI", "mcEI"]; if (typable(item)) t.push("type"); if (o.voice) t.push("listen"); if (item.pic) t.push("picIE", "picIE", "picEI");
      return t[rnd(t.length)];
    }
    const t = ["order", "order", "mcS"]; if (o.voice) t.push("listenOrder");
    return t[rnd(t.length)];
  }
  const weakScore = (S, now) => i => { const [c, w, t] = st(S, i.k); return w * 3 - c + Math.min(t ? (now - t) / 864e5 : 3, 14) * 0.5 + Math.random() * 2; };
  const freshScore = S => i => { const [c, w] = st(S, i.k); return w * 2 - (c + w) + Math.random(); };

  function gen(S, u, m, o) {
    o = o || {};
    const now = Date.now(), checkpoint = m === 5;
    const own = ITEMS.filter(i => i.u === u && (checkpoint || i.m === m));
    const before = ITEMS.filter(i => checkpoint ? i.u < u : ord(i.u, i.m) < ord(u, m));
    const total = checkpoint ? CHECKPOINT_SIZE : LESSON_SIZE;
    const nRev = before.length ? (checkpoint ? CHECKPOINT_REVIEW : Math.round(total * REVIEW_RATIO)) : 0;
    const nOwn = total - nRev;
    const score = checkpoint ? weakScore(S, now) : freshScore(S);
    const V = ranked(own.filter(i => i.kind === "v"), score), Sn = ranked(own.filter(i => i.kind === "s"), score), G = ranked(own.filter(i => i.kind === "g"), score);
    const ex = [];
    if (V.length >= 4) ex.push({ type: "match", items: V.slice(0, 5), review: false });
    let nG = Math.min(G.length, Math.round(nOwn * 0.3)), nS = Math.min(Sn.length, Math.round(nOwn * 0.3));
    let nV = Math.min(V.length, nOwn - ex.length - nG - nS);
    while (ex.length + nG + nS + nV < nOwn && (nG < G.length || nS < Sn.length)) { if (nG < G.length) nG++; else nS++; }
    V.slice(0, nV).forEach(i => ex.push(build(i, typeFor(i, S, o))));
    const gs = G.slice(0, nG), ss = Sn.slice(0, nS);
    while (gs.length || ss.length) { if (gs.length) { const i = gs.shift(); ex.push(build(i, "gap")); } if (ss.length) { const i = ss.shift(); ex.push(build(i, typeFor(i, S, o))); } }
    // Repaso continuo: lo más fallado y lo que hace más tiempo que no se ve.
    if (nRev) {
      const pick = [], maxV = Math.ceil(nRev / 2); let nv = 0;
      for (const i of ranked(before, weakScore(S, now))) {
        if (i.kind === "v" && nv >= maxV) continue;
        if (i.kind === "v") nv++;
        pick.push(i); if (pick.length === nRev) break;
      }
      pick.forEach(i => { const s = Object.assign({}, S, { it: Object.assign({}, S.it, { [i.k]: [1, 0, 0] }) }); ex.splice(Math.min(ex.length, 3 + rnd(Math.max(1, ex.length - 2))), 0, build(i, typeFor(i, st(S, i.k)[0] + st(S, i.k)[1] ? S : s, o), true)); });
    }
    if (o.speak) addSpeak(ex, checkpoint ? 2 : 1);
    return ex;
  }
  // Convierte algunos ejercicios de frase (de la segunda mitad) en ejercicios de hablar.
  function addSpeak(ex, n) {
    const cand = ex.map((e, i) => [e, i]).filter(([e, i]) => i >= ex.length / 3 && e.item && e.item.kind !== "v" && /^(order|mcS|gap)$/.test(e.type) && speakable(e.item));
    shuffle(cand).slice(0, n).forEach(([e, i]) => { ex[i] = build(e.item, "speak", e.review); });
  }
  // Repaso del día: un poco de todo lo visto, repartido por unidades y con prioridad para lo flojo.
  function seenItems(S) { return ITEMS.filter(i => S.it[i.k] || S.done[modId(i.u, i.m)]); }
  const dailyReady = S => seenItems(S).length >= 12;
  function genDaily(S, o) {
    o = o || {};
    const now = Date.now(), pool = seenItems(S);
    if (pool.length < 12) return [];
    const vocab = ranked(pool.filter(i => i.kind === "v"), weakScore(S, now));
    const match = vocab.length >= 9 ? vocab.slice(0, 5) : null;
    const rest = match ? pool.filter(i => !match.includes(i)) : pool;
    const units = [...new Set(rest.map(i => i.u))];
    const groups = units.map(u => ranked(rest.filter(i => i.u === u), weakScore(S, now)));
    const n = DAILY_SIZE - (match ? 1 : 0), quota = { v: Math.round(n * 0.4), s: Math.round(n * 0.35) }, cnt = { v: 0, s: 0, g: 0 };
    quota.g = n - quota.v - quota.s;
    const picks = [];
    while (picks.length < n && groups.some(g => g.length)) {
      let added = false;
      for (const gq of shuffle(groups)) {
        if (picks.length >= n) break;
        const at = gq.findIndex(i => cnt[i.kind] < quota[i.kind]);
        if (at >= 0) { const it = gq.splice(at, 1)[0]; picks.push(it); cnt[it.kind]++; added = true; }
      }
      if (!added) { quota.v = quota.s = quota.g = n; }   // si falta de un tipo, se completa con lo que haya
    }
    const out = shuffle(picks).map(i => build(i, typeFor(i, S, o), true));
    if (o.speak) addSpeak(out, 3);
    if (match) out.unshift({ type: "match", items: match, review: true });
    return out;
  }
  function weakItems(S) { return ITEMS.filter(i => { const [c, w] = st(S, i.k); return w > 0 && w >= c; }); }
  function genWeak(S, o) {
    return ranked(weakItems(S), weakScore(S, Date.now())).slice(0, 12).map(i => build(i, typeFor(i, S, o || {}), true));
  }
  function checkOrder(ex, chosen) { return chosen.map(t => t.toLowerCase()).join(" ") === ex.tokens.map(t => t.toLowerCase()).join(" "); }
  // Pronunciación: se compara lo que ha entendido el reconocedor de voz con la frase (orden de palabras, con tolerancia).
  const words = t => bare(String(t)).replace(/['’]/g, " ").replace(/[^\p{L}\p{N}\s-]/gu, " ").split(/[\s-]+/).filter(Boolean);
  function lev(a, b) {
    const d = Array.from({ length: a.length + 1 }, (_, i) => [i].concat(Array(b.length).fill(0)));
    for (let j = 1; j <= b.length; j++) d[0][j] = j;
    for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    return d[a.length][b.length];
  }
  const close = (a, b) => a === b || (Math.min(a.length, b.length) >= 4 && lev(a, b) <= 1);
  function speechScore(target, heard) {
    const t = words(target), h = words(heard);
    if (!t.length) return 0;
    const d = Array.from({ length: t.length + 1 }, () => Array(h.length + 1).fill(0));
    for (let i = 1; i <= t.length; i++) for (let j = 1; j <= h.length; j++) d[i][j] = close(t[i - 1], h[j - 1]) ? d[i - 1][j - 1] + 1 : Math.max(d[i - 1][j], d[i][j - 1]);
    return d[t.length][h.length] / t.length;
  }
  function checkSpeech(ex, alts) {
    let best = 0, heard = alts[0] || "";
    for (const a of alts) { const sc = speechScore(ex.answer, a); if (sc > best) { best = sc; heard = a; } }
    const n = words(ex.answer).length;
    return { ok: best >= (n <= 2 ? 1 : n <= 5 ? 0.8 : 0.75), heard, score: best };
  }
  function checkType(ex, text) { return norm(text) === norm(ex.answer) ? "ok" : bare(text) === bare(ex.answer) ? "accent" : "no"; }

  // ---------- progreso ----------
  const dayStr = (d) => { d = d || new Date(); return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); };
  const blank = () => ({ v: 1, xp: 0, dx: 0, streak: 0, day: "", dr: "", days: [], done: {}, it: {}, t: 0 });
  function merge(a, b) {
    if (!b || typeof b !== "object") return a;
    const out = blank();
    out.xp = Math.max(a.xp || 0, b.xp || 0);
    const late = (a.day || "") >= (b.day || "") ? a : b;
    out.dr = (a.dr || "") > (b.dr || "") ? a.dr || "" : b.dr || "";
    out.days = [...new Set([].concat(a.days || [], b.days || []))].sort().slice(-400);   // días con práctica (para la racha común)
    out.day = late.day || ""; out.streak = late.streak || 0; out.dx = late.dx || 0; out.t = Math.max(a.t || 0, b.t || 0);
    for (const src of [a.done || {}, b.done || {}]) for (const k in src) { const x = out.done[k], y = src[k]; out.done[k] = x ? { s: Math.max(x.s, y.s || 0), n: Math.max(x.n, y.n || 0) } : { s: y.s || 0, n: y.n || 0 }; }
    for (const src of [a.it || {}, b.it || {}]) for (const k in src) { if (!BY[k] || !Array.isArray(src[k])) continue; const x = out.it[k], y = src[k]; out.it[k] = x ? [Math.max(x[0], y[0] || 0), Math.max(x[1], y[1] || 0), Math.max(x[2], y[2] || 0)] : [y[0] || 0, y[1] || 0, y[2] || 0]; }
    return out;
  }
  function record(S, k, ok) { const a = S.it[k] ? S.it[k].slice() : [0, 0, 0]; a[ok ? 0 : 1]++; a[2] = Date.now(); S.it[k] = a; }
  function finish(S, id, accuracy, daily) {
    const stars = accuracy >= 0.9 ? 3 : accuracy >= 0.7 ? 2 : 1, gain = daily ? 20 + (stars === 3 ? 10 : 0) : 10 + (stars === 3 ? 5 : 0);
    if (daily) S.dr = dayStr();
    S.xp += gain; S.dx = (S.day === dayStr() ? S.dx || 0 : 0) + gain;
    if (id) { const d = S.done[id] || { s: 0, n: 0 }; S.done[id] = { s: Math.max(d.s, stars), n: d.n + 1 }; }
    const today = dayStr(), y = new Date(); y.setDate(y.getDate() - 1);
    if (S.day !== today) { S.streak = S.day === dayStr(y) ? S.streak + 1 : 1; S.day = today; }
    S.days = (S.days || []).filter(d => d !== today).concat(today).slice(-400);
    S.t = Date.now();
    return { stars, gain };
  }
  const todayXp = S => S.day === dayStr() ? S.dx || 0 : 0;
  function liveStreak(S) { const y = new Date(); y.setDate(y.getDate() - 1); return S.day === dayStr() || S.day === dayStr(y) ? S.streak : 0; }
  function unlocked(S, u, m, free) { if (free || ord(u, m) === 1) return true; const p = ord(u, m) - 1; return !!S.done[modId(Math.floor((p - 1) / 5) + 1, ((p - 1) % 5) + 1)]; }
  function nextUp(S) { for (const u of C.units) for (let m = 1; m <= 5; m++) if (!S.done[modId(u.n, m)]) return { u: u.n, m }; return null; }

  const dailyDone = S => S.dr === dayStr();
  g.Engine = { ITEMS, BY, REVIEW_RATIO, DAILY_SIZE, ord, modId, modInfo, gen, genWeak, genDaily, dailyReady, dailyDone, seenItems, checkSpeech, speechScore, speakable, weakItems, build, tokens, checkOrder, checkType, norm, shuffle, blank, merge, record, finish, liveStreak, todayXp, unlocked, nextUp, dayStr, st };
})(typeof window !== "undefined" ? window : globalThis);
