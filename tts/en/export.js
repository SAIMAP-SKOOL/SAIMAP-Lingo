const fs = require("fs"), path = require("path"), root = "/home/claude/lingo/src";
globalThis.window = globalThis;
for (const f of ["en/data.js", "en/data-a2.js", "en/data-b1.js", "en/data-b2.js", "en/data-c1.js", "en/data-c2.js", "engine.js"]) eval(fs.readFileSync(path.join(root, f), "utf8"));
const KEEP = new Set(["PM", "MP", "TV", "CV", "GP", "RP", "UK", "BBC", "I"]);
const limpio = t => {
  t = String(t).replace(/\([^)]*\)/g, " ").replace(/[→=+]/g, ", ").replace(/…/g, ", ").replace(/&/g, " and ").replace(/[«»_]/g, " ").replace(/ \/ /g, ", ").replace(/—/g, " ");
  if (/[A-Z]{3}/.test(t) && t === t.toUpperCase()) t = t.split(" ").map((w, i) => KEEP.has(w) ? w : i ? w.toLowerCase() : w[0] + w.slice(1).toLowerCase()).join(" ");
  return t.replace(/,\s*\?/g, "?").replace(/\s+,/g, ",").replace(/,\s*,/g, ",").replace(/\s+/g, " ").replace(/^[, ]+|[, ]+$/g, "").trim();
};
const lista = Engine.ITEMS.map(i => ({ k: i.k, texto: limpio(i.it) }));
fs.writeFileSync("lista.json", JSON.stringify(lista, null, 1));
console.log(lista.length, "frases");
for (const k of ["1.3.v0", "4.3.v0", "11.2.v8", "34.4.s0", "34.4.g0", "46.4.g0", "46.4.g2", "28.4.g0", "44.4.g2", "36.4.g0", "48.3.v6", "12.4.v0", "2.3.g2"]) console.log(k, "→", lista.find(x => x.k === k).texto);
