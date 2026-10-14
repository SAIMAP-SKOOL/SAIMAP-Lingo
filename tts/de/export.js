const fs = require("fs"), path = require("path"), root = "/home/claude/lingo/src";
globalThis.window = globalThis;
for (const f of ["de/data.js", "de/data-a2.js", "de/data-b1.js", "de/data-b2.js", "de/data-c1.js", "de/data-c2.js", "engine.js"]) eval(fs.readFileSync(path.join(root, f), "utf8"));
const ONE = ["", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn", "zwanzig"];
const TENS = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"];
const card = n => n <= 20 ? ONE[n] : (n % 10 ? ONE[n % 10].replace(/^eins$/, "ein") + "und" : "") + TENS[Math.floor(n / 10)];
const year = y => y >= 1100 && y < 2000 ? card(Math.floor(y / 100)).replace(/^eins$/, "ein") + "hundert" + (y % 100 ? card(y % 100) : "") : String(y);
const ordStem = n => ({ 1: "erst", 3: "dritt", 7: "siebt", 8: "acht" })[n] || (n < 20 ? card(n) + "t" : card(n) + "st");
const SIG = { "z. B.": "zum Beispiel", "d. h.": "das heißt", "u. a.": "unter anderem", "usw.": "und so weiter", "ca.": "circa", "Dr.": "Doktor", "Pat.": "Patient", "§": "Paragraf" };
const ACR = { ABAB: "A B A B", AABB: "A A B B", ABBA: "A B B A", EKG: "E K G", ICE: "I C E", TÜV: "Tüf", KI: "K I", EU: "E U", DDR: "D D R", BRD: "B R D", WG: "W G", TU: "T U", DSH: "D S H", ÖSD: "Ö S D", TDN: "T D N", RR: "R R", BZ: "B Z", CDU: "C D U", SPD: "S P D", UNESCO: "Unesco", TestDaF: "Test D A F", "Steuer-ID": "Steuer I D", "U-Bahn": "U-Bahn", "C1": "C eins", "C2": "C zwei", "B1": "B eins", "B2": "B zwei", "A1": "A eins", "A2": "A zwei" };
const limpio = t => {
  t = String(t).replace(/ | /g, " ");
  t = t.replace(/^«[^»]*»\s*(\([^)]*\)\s*)?(ou [a-zñáéíóú ]+)?=\s*/, "")
       .replace(/^(Formal|Coloquial|Ironía|Irónico|Suabo|Hablado)\s*:\s*/i, "");
  t = t.replace(/(\d{1,2}):(\d{2}) Uhr/g, (m, h, mi) => card(+h) + " Uhr" + (+mi ? " " + card(+mi) : ""))
       .replace(/(\d+),(\d{2}) Euro/g, (m, e, c) => e + " Euro " + (+c ? card(+c) : ""))
       .replace(/(\d{1,3})\.(\d{3})\b/g, "$1$2")
       .replace(/\b(1[1-9]\d\d)\b/g, m => year(+m));
  t = t.replace(/\b(am|Am|vom|zum|im|Im|bis zum|ab dem|seit dem) (\d{1,2})\. /g, (m, p, n) => p + " " + ordStem(+n) + "en ")
       .replace(/\b(der|Der|den|die|Die|das) (\d{1,2})\. /g, (m, p, n) => p + " " + ordStem(+n) + "e ")
       .replace(/^(\d{1,2})\. ?=/, (m, n) => "");
  for (const k in SIG) t = t.split(k).join(SIG[k]);
  t = t.replace(/[¿¡]/g, "").replace(/\([^)]*\)/g, " ").replace(/[→=+]/g, ", ").replace(/…/g, ", ").replace(/[«»„“”_]/g, " ").replace(/ \/ /g, ", ").replace(/[—–]/g, " ");
  t = t.replace(/\b[A-ZÄÖÜa-zß][A-Za-zÄÖÜß\-]*\d?\b/g, w => ACR[w] || w);
  t = t.replace(/([.!?])\s*,/g, "$1").replace(/^\d+(?::\d+)?\s*,\s*(?=\D)/, "");
  return t.replace(/,\s*\?/g, "?").replace(/\s+,/g, ",").replace(/,\s*,/g, ",").replace(/\s+([.!?:;])/g, "$1").replace(/:\s*([.!?])/g, "$1").replace(/\s+/g, " ").replace(/^[,: ]+|[,: ]+$/g, "").trim();
};
const lista = Engine.ITEMS.map(i => ({ k: i.k, texto: limpio(i.it) }));
fs.writeFileSync("lista.json", JSON.stringify(lista, null, 1));
console.log(lista.length, "frases", lista.filter(x => !x.texto).length, "vacías");
if (process.argv[2] === "q") {
  Engine.ITEMS.filter(i => /^«|^[A-Z][a-zíó]+:/.test(i.it)).forEach(i => console.log(" ", i.k, "|", i.it, "→", limpio(i.it)));
  const raros = lista.filter(x => /[0-9]|[A-ZÄÖÜ]{2,}|[^\wÀ-ÿ\s.,!?;:'’\-]/.test(x.texto));
  console.log(raros.length, "raros:"); raros.forEach(x => console.log(" ", x.k, "→", x.texto));
}
