// Caché para que la app abra sin conexión. Las imágenes y el audio se guardan al usarlos. Sube el número de versión en cada publicación.
const VERSION = "saimap-lingo-plataforma-v5";
const SHELL = ["./", "index.html", "engine.js", "app.js", "platform.js", "courses.js", "firebase-config.js", "manifest.webmanifest", "icons/icon-192.png", "courses/it/course.js", "courses/en/course.js", "courses/pt/course.js", "courses/fr/course.js", "courses/de/course.js", "courses/el/course.js", "courses/ca/course.js"];
self.addEventListener("install", e => e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())));
self.addEventListener("activate", e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return;   // Firebase y Google van siempre a la red
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(VERSION).then(c => c.put(e.request, copy)); return r; }).catch(() => caches.match(e.request, { ignoreSearch: true }).then(r => r || caches.match("index.html"))));
});
