// node check_course.js <dir>   Valida el formato de un curso (src/<dir>/data*.js)
const fs = require("fs"), path = require("path"), dir = process.argv[2];
global.window = globalThis;
const files = fs.readdirSync(dir).filter(f => /^data.*\.js$/.test(f)).sort((a, b) => (a === "data.js" ? -1 : b === "data.js" ? 1 : a < b ? -1 : 1));
for (const f of files) eval(fs.readFileSync(path.join(dir, f), "utf8"));
const C = window.COURSE; let err = 0, n = { v: 0, s: 0, g: 0, m: 0 };
const bad = (...a) => { err++; console.log("  ✗", ...a); };
const norm = s => s.toLowerCase().replace(/[.!?¿¡]/g, "").trim();
C.units.forEach((u, i) => {
  if (u.n !== i + 1) bad("unidad fuera de orden", u.n);
  if (u.mods.length !== 4) bad("unidad", u.n, "tiene", u.mods.length, "módulos");
  u.mods.forEach((m, mi) => {
    const id = u.n + "." + (mi + 1); n.m++;
    if (!m.t || !m.es || !m.tip) bad(id, "falta título/tip");
    if (m.v.length < 7) bad(id, "pocas palabras", m.v.length);
    if (m.s.length < 5) bad(id, "pocas frases", m.s.length);
    if (m.g.length < 4) bad(id, "pocos huecos", m.g.length);
    const vi = new Set(), ve = new Set();
    m.v.forEach(x => { n.v++; const p = x.indexOf("="); if (p < 1) return bad(id, "v sin =", x); const a = x.slice(0, p), b = x.slice(p + 1); if (!b) bad(id, "v sin glosa", x); if (vi.has(norm(a))) bad(id, "v repetida", a); if (ve.has(norm(b))) bad(id, "glosa repetida", b); vi.add(norm(a)); ve.add(norm(b)); });
    const si = new Set();
    m.s.forEach(x => { n.s++; const a = x.split("|"); if (a.length !== 2) bad(id, "s mal formada", x); if (si.has(a[0])) bad(id, "s repetida", x); si.add(a[0]); if (a[0].split(/\s+/).length > 14) bad(id, "s larga", a[0]); });
    m.g.forEach(x => { n.g++; const a = x.split("|"); if (a.length !== 5) return bad(id, "g con", a.length, "campos:", x); if ((a[0].match(/___/g) || []).length !== 1) bad(id, "g sin un único hueco", x); const o = [a[1], a[2], a[3]].map(x => x.trim()); if (new Set(o).size !== 3) bad(id, "g opciones repetidas", x); });
  });
});
C.levels.forEach(l => { if (l.to > C.units.length) bad("nivel", l.id, "acaba en", l.to, "pero hay", C.units.length, "unidades"); });
console.log(files.join(", "), "→", C.units.length, "unidades,", n.m, "módulos,", n.v + n.s + n.g, "ítems (", n.v, "palabras,", n.s, "frases,", n.g, "huecos ).", err ? err + " ERRORES" : "Sin errores.");
process.exit(err ? 1 : 0);
