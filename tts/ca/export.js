const fs = require("fs"), path = require("path"), root = "/home/claude/lingo/src";
globalThis.window = globalThis;
for (const f of ["ca/data.js", "ca/data-a2.js", "ca/data-b1.js", "ca/data-b2.js", "ca/data-c1.js", "ca/data-c2.js", "engine.js"]) eval(fs.readFileSync(path.join(root, f), "utf8"));
const N = { 1229: "mil dos-cents vint-i-nou", 1276: "mil dos-cents setanta-sis", 1859: "mil vuit-cents cinquanta-nou", 1983: "mil nou-cents vuitanta-tres", 1992: "mil nou-cents noranta-dos", 2027: "dos mil vint-i-set", 2020: "dos mil vint", 15: "quinze", 23: "vint-i-tres", 21: "vint-i-u", 32: "trenta-dos" };
const SIG = { "CO₂": "cê o dos", "Sra.": "senyora", "Sr.": "senyor", DNI: "dena", CAP: "cap", IEC: "i e ce", AVL: "a ve ela", DOGC: "de o ge ce", UNESCO: "unesco", C2: "ce dos", XIII: "tretze", XV: "quinze", XIX: "dinou", XX: "vint" };
const limpio = t => {
  t = String(t).replace(/ | /g, " ");
  t = t.replace(/[¿¡]/g, "").replace(/\([^)]*\)/g, " ").replace(/[→=+]/g, ", ").replace(/…/g, ", ").replace(/[«»„“”_]/g, " ").replace(/ \/ /g, ", ").replace(/[—–]/g, ", ");
  for (const k in SIG) t = t.replace(new RegExp("(^|[^\\p{L}])" + k.replace(/\./g, "\\.") + "(?![\\p{L}])", "gu"), "$1" + SIG[k]);
  t = t.replace(/\b\d+\b/g, n => N[n] || n);
  t = t.replace(/([.!?])\s*,/g, "$1");
  return t.replace(/\s+,/g, ",").replace(/,\s*,/g, ",").replace(/\s+([.!?:;])/g, "$1").replace(/\s+/g, " ").replace(/^[,: ]+|[,: ]+$/g, "").trim();
};
const lista = Engine.ITEMS.map(i => ({ k: i.k, texto: limpio(i.it) }));
fs.writeFileSync("lista.json", JSON.stringify(lista, null, 1));
console.log(lista.length, "frases", lista.filter(x => !x.texto).length, "vacías");
const raros = lista.filter(x => /[0-9]|[A-Z]{2,}|[^\p{L}\s.,!?;:'’·\-]/u.test(x.texto)); console.log(raros.length, "raros"); raros.slice(0, 40).forEach(x => console.log(" ", x.k, "→", x.texto));
