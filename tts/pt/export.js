const fs = require("fs"), path = require("path"), root = "/home/claude/lingo/src";
globalThis.window = globalThis;
for (const f of ["pt/data.js", "pt/data-a2.js", "pt/data-b1.js", "pt/data-b2.js", "pt/data-c1.js", "pt/data-c2.js", "engine.js"]) eval(fs.readFileSync(path.join(root, f), "utf8"));
const ROM = { XII: "doze", XVI: "dezasseis", XVII: "dezassete", XIX: "dezanove", XX: "vinte" };
const limpio = t => {
  t = String(t).replace(/^«[^»]*»\s*=\s*/, "").replace(/[¿¡]/g, "").replace(/\([^)]*\)/g, " ").replace(/[→=+]/g, ", ").replace(/…/g, ", ").replace(/[«»_]/g, " ").replace(/ \/ /g, ", ").replace(/—/g, " ");
  t = t.replace(/\bExmo\./g, "Excelentíssimo").replace(/\bExma\./g, "Excelentíssima").replace(/\bq\.b\./g, "quanto baste").replace(/\bT2\b/g, "tê dois").replace(/\bA2\b/g, "á dois").replace(/\bC2\b/g, "cê dois")
       .replace(/(\d+)\s*%/g, "$1 por cento").replace(/\b12\.º/g, "décimo segundo").replace(/\b5\.º/g, "quinto").replace(/\b(XII|XVII|XVI|XIX|XX)\b/g, m => ROM[m])
       .replace(/\b(CIPLE|DUPLE|DAPLE|ACESSO)\b/g, m => m[0] + m.slice(1).toLowerCase()).replace(/\bIRS\b/g, "i érre ésse").replace(/\bNIF\b/g, "nife");
  return t.replace(/,\s*\?/g, "?").replace(/\s+,/g, ",").replace(/,\s*,/g, ",").replace(/\s+([.!?:;])/g, "$1").replace(/\s+/g, " ").replace(/^[, ]+|[, ]+$/g, "").trim();
};
const lista = Engine.ITEMS.map(i => ({ k: i.k, texto: limpio(i.it) }));
fs.writeFileSync("lista.json", JSON.stringify(lista, null, 1));
console.log(lista.length, "frases", lista.filter(x => !x.texto).length, "vacías");
const raros = lista.filter(x => /[0-9A-Z]{2,}|[^\wÀ-ÿ\s.,!?;:'’\-]/.test(x.texto));
console.log(raros.length, "con cifras/siglas/símbolos:"); raros.forEach(x => console.log(" ", x.k, "→", x.texto));
