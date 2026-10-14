const fs = require("fs"), path = require("path"), root = "/home/claude/lingo/src";
globalThis.window = globalThis;
for (const f of ["fr/data.js", "fr/data-a2.js", "fr/data-b1.js", "fr/data-b2.js", "fr/data-c1.js", "fr/data-c2.js", "engine.js"]) eval(fs.readFileSync(path.join(root, f), "utf8"));
const ROM = { XVIIᵉ: "dix-septième", XIXᵉ: "dix-neuvième", XXᵉ: "vingtième", XXIᵉ: "vingt et unième", XVIᵉ: "seizième", XVIIIᵉ: "dix-huitième" };
const SIG = { TGV: "tégévé", CDI: "cédéi", CDD: "cédédé", BD: "bédé", DELF: "delf", DALF: "dalf", GSM: "géessèm", VO: "véo", ABAB: "a, b, a, b", AABB: "a, a, b, b", ABBA: "a, b, b, a", C1: "cé un", C2: "cé deux", B2: "bé deux", B1: "bé un", A1: "a un", A2: "a deux" };
const limpio = t => {
  t = String(t).replace(/ | /g, " ");
  t = t.replace(/^«[^»]*»\s*(\([^)]*\)\s*)?(ou [a-zñáéíóú ]+)?(se dit|=)\s*/, "")            // «español» se dit / =
       .replace(/^«[^»]*»\s*\((familiar|lítote|de pila|de cocina)\)\s*[:=]\s*/, "")
       .replace(/^«[^»]*»\s*en français\s*:\s*/, "")
       .replace(/^(Hablado|Escrito|Para cerrar un correo formal)\s*:\s*/, "");
  t = t.replace(/[¿¡]/g, "").replace(/\([^)]*\)/g, " ").replace(/[→=+]/g, ", ").replace(/…/g, ", ").replace(/[«»_]/g, " ").replace(/ \/ /g, ", ").replace(/[—–]/g, " ");
  t = t.replace(/\b(XVIIIᵉ|XVIIᵉ|XVIᵉ|XIXᵉ|XXIᵉ|XXᵉ)/g, m => ROM[m]).replace(/Louis XIV/g, "Louis quatorze")
       .replace(/\b(TGV|CDI|CDD|BD|DELF|DALF|GSM|VO|ABAB|AABB|ABBA|C1|C2|B1|B2|A1|A2)\b/g, m => SIG[m])
       .replace(/\b[A-Z]{4,}\b/g, m => m.toLowerCase());
  t = t.replace(/([.!?])\s*,/g, "$1").replace(/^\d+(?: h \d+)?\s*,\s*(?=\D)/, "");
  return t.replace(/,\s*\?/g, " ?").replace(/\s+,/g, ",").replace(/,\s*,/g, ",").replace(/\s+([.!?:;])/g, "$1").replace(/:\s*([.!?])/g, "$1").replace(/\s+/g, " ").replace(/^[,: ]+|[,: ]+$/g, "").trim();
};
const lista = Engine.ITEMS.map(i => ({ k: i.k, texto: limpio(i.it) }));
fs.writeFileSync("lista.json", JSON.stringify(lista, null, 1));
console.log(lista.length, "frases", lista.filter(x => !x.texto).length, "vacías");
if (process.argv[2] === "q") {
  Engine.ITEMS.filter(i => /^«/.test(i.it)).forEach(i => console.log(" ", i.k, "|", i.it, "→", limpio(i.it)));
  const raros = lista.filter(x => /[0-9A-Z]{2,}|[^\wÀ-ÿœŒ\s.,!?;:'’\-]/.test(x.texto));
  console.log(raros.length, "raros:"); raros.forEach(x => console.log(" ", x.k, "→", x.texto));
}
