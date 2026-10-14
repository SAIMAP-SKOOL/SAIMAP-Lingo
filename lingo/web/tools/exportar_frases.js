// Genera audio/lista.json con todas las palabras y frases italianas del curso (clave → texto a leer).
// Uso: node tools/exportar_frases.js   (desde la carpeta de la app)
const fs = require("fs"), path = require("path"), root = path.join(__dirname, "..");
globalThis.window = globalThis;
for (const f of ["pics.js", "data.js", "data-a2.js", "data-b1.js", "data-b2.js", "data-c1.js", "data-c2.js", "engine.js"]) require(path.join(root, f));
const limpio = t => String(t).replace(/\([^)]*\)/g, " ").replace(/[→=+]/g, ", ").replace(/[«»_]/g, " ").replace(/\s+/g, " ").trim();
const lista = Engine.ITEMS.map(i => ({ k: i.k, texto: limpio(i.it) }));
fs.mkdirSync(path.join(root, "audio"), { recursive: true });
fs.writeFileSync(path.join(root, "audio", "lista.json"), JSON.stringify(lista, null, 1));
console.log(lista.length + " frases en audio/lista.json");
