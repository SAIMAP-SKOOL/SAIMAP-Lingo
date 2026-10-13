// SAIMAP Lingo · plataforma con todos los idiomas.
// Elige el curso (pantalla de idiomas), carga sus datos y después el motor y la app, que son comunes.
// La racha y los XP son globales: se calculan con el progreso guardado de todos los cursos.
(function () {
  const COURSES = window.LINGO_COURSES || [];
  const KEY = "sl.course";
  const LS = { get(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { } } };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const byId = id => COURSES.find(c => c.id === id);
  const fmt = d => d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  let current = null;

  // ---------- banderas (SVG, para que se vean igual en todos los sistemas) ----------
  function flag(id) {
    const box = inner => '<svg class="flag" viewBox="0 0 30 20" aria-hidden="true"><clipPath id="fc-' + id + '"><rect width="30" height="20" rx="3"/></clipPath><g clip-path="url(#fc-' + id + ')">' + inner + "</g></svg>";
    const v = (a, b, c) => '<rect width="10" height="20" fill="' + a + '"/><rect x="10" width="10" height="20" fill="' + b + '"/><rect x="20" width="10" height="20" fill="' + c + '"/>';
    if (id === "it") return box(v("#009246", "#fff", "#CE2B37"));
    if (id === "fr") return box(v("#0055A4", "#fff", "#EF4135"));
    if (id === "de") return box('<rect width="30" height="7" fill="#1A1A1A"/><rect y="6.6" width="30" height="7" fill="#DD0000"/><rect y="13.3" width="30" height="6.7" fill="#FFCE00"/>');
    if (id === "pt") return box('<rect width="12" height="20" fill="#046A38"/><rect x="12" width="18" height="20" fill="#DA291C"/><circle cx="12" cy="10" r="4.6" fill="#FFE000"/><circle cx="12" cy="10" r="3" fill="#DA291C"/><rect x="10.6" y="8.2" width="2.8" height="3.6" rx=".6" fill="#fff"/>');
    if (id === "en") return box('<rect width="30" height="20" fill="#012169"/><path d="M0 0L30 20M30 0L0 20" stroke="#fff" stroke-width="4"/><path d="M0 0L30 20M30 0L0 20" stroke="#C8102E" stroke-width="1.6"/><path d="M15 0V20M0 10H30" stroke="#fff" stroke-width="6"/><path d="M15 0V20M0 10H30" stroke="#C8102E" stroke-width="3.4"/>');
    return box('<rect width="30" height="20" fill="#9AA6B8"/>');
  }

  // ---------- progreso guardado ----------
  const stateOf = c => LS.get("sl." + c.store + "state");
  function daysOf(s) {
    const set = new Set(Array.isArray(s.days) ? s.days : []);
    if (s.day) {   // progreso antiguo sin lista de días: se reconstruye con la racha
      set.add(s.day); const d = new Date(s.day + "T12:00:00");
      for (let i = 1; i < (s.streak || 0); i++) { d.setDate(d.getDate() - 1); set.add(fmt(d)); }
    }
    return set;
  }
  function stats() {
    const today = fmt(new Date()), y = new Date(); y.setDate(y.getDate() - 1);
    let xp = 0, dx = 0; const days = new Set();
    COURSES.forEach(c => { const s = stateOf(c); if (!s) return; xp += s.xp || 0; if (s.day === today) dx += s.dx || 0; daysOf(s).forEach(d => days.add(d)); });
    let streak = 0; const d = new Date();
    if (!days.has(today)) { if (!days.has(fmt(y))) return { xp, today: dx, streak: 0 }; d.setDate(d.getDate() - 1); }
    while (days.has(fmt(d))) { streak++; d.setDate(d.getDate() - 1); }
    return { xp, today: dx, streak };
  }
  function courseInfo(c) {
    const s = stateOf(c) || {}, done = s.done ? Object.keys(s.done).length : 0, total = c.units * 5;
    let next = c.units;
    for (let u = 1; u <= c.units; u++) if ([1, 2, 3, 4, 5].some(m => !(s.done && s.done[u + "." + m]))) { next = u; break; }
    const lv = c.levels.find(l => next >= l.from && next <= l.to) || c.levels[0];
    return { done, total, xp: s.xp || 0, level: lv.id, started: !!(s.xp || done) };
  }
  // Progreso de otro curso que llega de la cuenta: se guarda si es más reciente que el de este dispositivo.
  function absorb(id, remote) {
    const c = byId(id); if (!c || !remote || typeof remote !== "object") return false;
    const local = stateOf(c);
    if (local && (local.t || 0) >= (remote.t || 0)) return false;
    LS.set("sl." + c.store + "state", remote); return true;
  }

  // ---------- pantalla de idiomas ----------
  function picker(closable) {
    let el = document.getElementById("langs");
    if (!el) { el = document.createElement("div"); el.id = "langs"; el.className = "langs"; el.setAttribute("role", "dialog"); el.setAttribute("aria-modal", "true"); el.setAttribute("aria-labelledby", "langs-title"); document.body.appendChild(el); }
    const g = stats(), GOAL = 30;
    el.innerHTML = '<div class="langs-in"><header class="langs-top"><span class="langs-brand">SAIMAP <i>Lingo</i></span>' +
      '<span class="stat fire' + (g.streak ? " lit" : "") + '" title="Racha de días (todos los idiomas)">' + FIRE + g.streak + '</span><span class="stat xp" title="XP de todos los idiomas">' + BOLT + g.xp + "</span>" +
      (closable ? '<button class="langs-x" data-close aria-label="Cerrar">' + X + "</button>" : "") + "</header>" +
      '<h1 id="langs-title">¿Qué idioma practicas hoy?</h1><p class="langs-sub">Tu racha y tus XP suman en todos los idiomas. Cada curso guarda sus unidades y sus estrellas.</p>' +
      '<div class="goal"><span>Hoy</span><div class="meter"><i style="width:' + Math.min(100, 100 * g.today / GOAL) + '%"></i></div><span>' + (g.today >= GOAL ? "Objetivo cumplido" : g.today + " / " + GOAL + " XP") + "</span></div>" +
      '<div class="langs-list">' + COURSES.map(c => {
        const i = courseInfo(c), here = current === c.id;
        return '<button class="lang' + (here ? " here" : "") + '" data-lang="' + c.id + '">' + flag(c.id) + '<span class="lang-txt"><b>' + esc(c.name) + "</b><small>" + esc(c.variety) + "</small>" +
          '<span class="lang-prog"><em>' + i.level + '</em><span class="meter"><i style="width:' + (100 * i.done / i.total) + '%"></i></span><span>' + i.done + "/" + i.total + "</span></span></span>" +
          '<span class="lang-go">' + (here ? "Estás aquí" : i.started ? "Continuar" : "Empezar") + "</span></button>";
      }).join("") + "</div></div>";
    el.hidden = false; document.documentElement.classList.add("langs-open");
    const f = el.querySelector(".lang.here") || el.querySelector(".lang"); if (f) f.focus({ preventScroll: true });
  }
  function closePicker() { const el = document.getElementById("langs"); if (el) el.hidden = true; document.documentElement.classList.remove("langs-open"); }
  const svgI = d => '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="' + d + '"/></svg>';
  const FIRE = svgI("M12 2c1 4 5 5.5 5 11a5 5 0 01-10 0c0-2 1-3.5 2-4.5.3 1.5 1 2.3 2 2.5C10.5 8 11 4.5 12 2z"), BOLT = svgI("M13 2L4 14h6l-1 8 9-12h-6z");
  const X = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>';

  function choose(id) {
    if (!byId(id)) return;
    LS.set(KEY, id);
    if (current && current !== id) { location.hash = ""; location.reload(); return; }
    closePicker(); if (!current) load(id);
  }
  document.addEventListener("click", ev => {
    const t = ev.target.closest("#langs [data-lang], #langs [data-close]"); if (!t) return;
    ev.stopPropagation();
    if (t.dataset.close != null) return closePicker();
    choose(t.dataset.lang);
  }, true);
  document.addEventListener("keydown", ev => { if (ev.key === "Escape" && current && !document.getElementById("langs")?.hidden) closePicker(); }, true);

  // ---------- carga del curso ----------
  function load(id) {
    const c = byId(id); current = id; const base = "courses/" + id + "/";
    window.LINGO_AUDIO = { base: base + "audio/" }; window.LINGO_IMG = base + "img/";
    document.documentElement.lang = "es";
    const files = c.files.map(f => base + f).concat(["engine.js", "app.js"]);
    files.forEach(src => { const s = document.createElement("script"); s.src = src; s.async = false; document.body.appendChild(s); });
  }

  addEventListener("hashchange", () => { const h = location.hash.replace("#", ""); if (byId(h) && h !== current) choose(h); });
  window.LingoPlatform = { courses: COURSES, get current() { return current; }, flag, stats, absorb, openPicker: () => picker(true), others: () => COURSES.filter(c => c.id !== current) };
  const fromHash = (location.hash || "").replace("#", ""), saved = LS.get(KEY);
  const start = byId(fromHash) ? fromHash : byId(saved) ? saved : null;
  if (start) { LS.set(KEY, start); load(start); } else picker(false);
})();
