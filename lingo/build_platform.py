"""Construye la plataforma única de SAIMAP Lingo (todos los idiomas):
   platform/            → web / PWA para GitHub Pages
   artifact-platform/   → página para publicar como artefacto (las imágenes y el audio se copian de los artefactos de cada curso)
Uso: python3 build_platform.py"""
import os, re, json, shutil, subprocess

R = os.path.dirname(os.path.abspath(__file__))
SRC = R + '/src'
src = lambda n: open(SRC + '/' + n, encoding='utf8').read()
code = open(R + '/build.py', encoding='utf8').read()
ns = {}
exec(code[:code.index("COURSES['it-scn']")].replace('def build(K):', 'def _unused(K):'), {'__file__': R + '/build.py', '__name__': 'x'}, ns)
COURSES = ns['COURSES']
VERSION = 'saimap-lingo-plataforma-v4'
ORDER = ['it', 'en', 'pt', 'fr', 'de', 'el']
NAMES = {'it': ('Italiano', 'Italiano de Italia'), 'en': ('Inglés', 'Inglés británico'), 'pt': ('Portugués', 'Portugués europeo'),
         'fr': ('Francés', 'Francés de Francia'), 'de': ('Alemán', 'Alemán estándar'), 'el': ('Griego', 'Griego moderno')}
FILES = ['pics.js', 'scenes.js', 'data.js', 'data-a2.js', 'data-b1.js', 'data-b2.js', 'data-c1.js', 'data-c2.js']


def course_meta(cid):
    d = COURSES[cid]['dir']
    js = 'global.window=global;' + ''.join(f'require({json.dumps(SRC + "/" + d + f)});' for f in FILES if f.startswith('data')) + \
         'const C=window.COURSE;console.log(JSON.stringify({ui:C.ui||{},levels:C.levels,units:C.units.length,book:(C.ui&&C.ui.book)||"Italiano dalla A alla Z"}))'
    m = json.loads(subprocess.check_output(['node', '-e', js]))
    ui = m['ui']
    return dict(id=cid, name=NAMES[cid][0], variety=NAMES[cid][1], store=ui.get('store', ''), cloud=ui.get('cloud', 'progress'),
                book=m['book'], units=m['units'], levels=[dict(id=l['id'], **{'from': l['from'], 'to': l['to']}) for l in m['levels']], files=['course.js'])


META = [course_meta(c) for c in ORDER]
COURSES_JS = '// Cursos de la plataforma (generado por build_platform.py)\nwindow.LINGO_COURSES = ' + json.dumps(META, ensure_ascii=False, indent=1) + ';\n'
page = src('app.html').replace('<title>SAIMAP Lingo</title>', '<title>SAIMAP Lingo</title>')
DESC = 'SAIMAP Lingo: aprende italiano, inglés, portugués, francés, alemán y griego desde cero con lecciones cortas y repaso continuo.'

# ------------------------------------------------------------------ web / PWA
W = R + '/platform'
os.makedirs(W + '/icons', exist_ok=True); os.makedirs(W + '/.well-known', exist_ok=True)
for n in ('engine.js', 'app.js', 'platform.js', 'privacidad.html', 'borrar-cuenta.html'):
    shutil.copy(SRC + '/' + n, W + '/' + n)
open(W + '/courses.js', 'w', encoding='utf8').write(COURSES_JS)
for f in os.listdir(R + '/web/icons'):
    shutil.copy(R + '/web/icons/' + f, W + '/icons/' + f)
for cid in ORDER:
    K = COURSES[cid]; C = f'{W}/courses/{cid}'
    os.makedirs(C + '/img', exist_ok=True); os.makedirs(C + '/audio', exist_ok=True)
    # un solo archivo por curso con todos sus datos (menos peticiones y menos archivos publicados)
    parts = []
    for f in FILES:
        p = SRC + '/' + K['dir'] + f
        parts.append('// ---- ' + f + '\n' + (open(p, encoding='utf8').read() if os.path.exists(p) else 'window.SCENES = {};'))
    for f in FILES:
        if os.path.exists(C + '/' + f): os.remove(C + '/' + f)
    open(C + '/course.js', 'w', encoding='utf8').write('\n;\n'.join(parts) + '\n')
    for i in range(1, 51):
        shutil.copy(f"{K['img']}/u{i:02d}.png", f'{C}/img/u{i:02d}.png')
        a = f"{R}/{K['web']}/audio/u{i:02d}.js"
        if os.path.exists(a) and not os.path.exists(f'{C}/audio/u{i:02d}.js'):
            shutil.copy(a, f'{C}/audio/u{i:02d}.js')
title, rest = re.match(r'(<title>.*?</title>)\n(.*)', page, re.S).groups()
link, body = re.match(r'(<link[^>]*>)\n(.*)', rest, re.S).groups()
style, markup = re.match(r'(<style>.*?</style>)\n(.*)', body, re.S).groups()
head = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{title}
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#1F5FD1">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-192.png">
<style>:root{{padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
'''
scripts = '''<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>
<script src="firebase-config.js"></script>
<script src="courses.js"></script>
<script src="platform.js"></script>
<script>if("serviceWorker" in navigator) addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));</script>
'''
open(W + '/index.html', 'w', encoding='utf8').write(head + link + '\n' + style + '\n</head>\n<body>\n' + markup.replace('<!--SCRIPTS-->', scripts) + '</body>\n</html>\n')
open(W + '/firebase-config.js', 'w').write('''// Configuración del proyecto de Firebase "saimap-lingo" (cuentas y progreso sincronizado).
// Estos datos no son secretos: identifican el proyecto. La seguridad la dan las reglas de Firestore (firestore.rules).
window.SAIMAP_FIREBASE = {
  apiKey: "AIzaSyCTG8BsDihN0vsz7JvZz64XJgeU7kMp7V8",
  authDomain: "saimap-lingo.firebaseapp.com",
  projectId: "saimap-lingo",
  messagingSenderId: "103281447895",
  appId: "1:103281447895:web:26e32613437784b78df192"
};
''')
json.dump({"name": "SAIMAP Lingo", "short_name": "SAIMAP Lingo", "description": DESC, "lang": "es", "start_url": "./", "scope": "./", "display": "standalone", "orientation": "portrait",
           "background_color": "#F2F5FB", "theme_color": "#1F5FD1", "categories": ["education"],
           "shortcuts": [{"name": m['name'], "url": "./#" + m['id']} for m in META],
           "icons": [{"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
                     {"src": "icons/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]},
          open(W + '/manifest.webmanifest', 'w'), ensure_ascii=False, indent=1)
shell = ["./", "index.html", "engine.js", "app.js", "platform.js", "courses.js", "firebase-config.js", "manifest.webmanifest", "icons/icon-192.png"] + \
        [f'courses/{c}/course.js' for c in ORDER]
open(W + '/sw.js', 'w').write('''// Caché para que la app abra sin conexión. Las imágenes y el audio se guardan al usarlos. Sube el número de versión en cada publicación.
const VERSION = "%s";
const SHELL = %s;
self.addEventListener("install", e => e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())));
self.addEventListener("activate", e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return;   // Firebase y Google van siempre a la red
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(VERSION).then(c => c.put(e.request, copy)); return r; }).catch(() => caches.match(e.request, { ignoreSearch: true }).then(r => r || caches.match("index.html"))));
});
''' % (VERSION, json.dumps(shell)))
open(W + '/firestore.rules', 'w').write('''rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Cada persona solo puede leer, escribir y borrar su propio progreso:
    //   users/<uid>                 → italiano
    //   users/<uid>/courses/<idioma> → resto de idiomas
    match /users/{uid} {
      allow read, delete: if request.auth != null && request.auth.uid == uid;
      allow create, update: if request.auth != null && request.auth.uid == uid;
      match /courses/{course} {
        allow read, delete: if request.auth != null && request.auth.uid == uid;
        allow create, update: if request.auth != null && request.auth.uid == uid
                              && course in ["it", "en", "pt", "fr", "de", "el"];
      }
    }
  }
}
''')
open(W + '/.nojekyll', 'w').write('')
open(W + '/.well-known/assetlinks.json', 'w').write('''[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": { "namespace": "android_app", "package_name": "com.saimap.lingo.plataforma",
              "sha256_cert_fingerprints": ["PEGA_AQUI_LA_HUELLA_SHA256_DE_TU_CLAVE_DE_FIRMA"] }
}]
''')
open(W + '/README.md', 'w', encoding='utf8').write('''# SAIMAP Lingo · plataforma con todos los idiomas

Italiano, inglés, portugués, francés, alemán y griego en una sola web. Al entrar se elige idioma; la bandera de arriba permite cambiarlo.
La racha y los XP son comunes a todos los idiomas; cada curso guarda sus unidades, estrellas y puntos flojos.

## Estructura
- `index.html`, `platform.js` (pantalla de idiomas y carga del curso), `engine.js` y `app.js` (comunes a todos los cursos).
- `courses.js`: lista de cursos (nombre, niveles, dónde guarda cada uno su progreso).
- `courses/<idioma>/`: datos, escenarios (`scenes.js`), ilustraciones (`img/`) y audio grabado (`audio/`).
- Enlaces directos a un idioma: `…/#it`, `…/#en`, `…/#pt`, `…/#fr`, `…/#de`, `…/#el`.

## Publicar en GitHub Pages
1. Sube el contenido de esta carpeta a un repositorio (incluido `.nojekyll`).
2. Settings › Pages › Deploy from a branch › `main` / raíz.
3. Política de privacidad: `privacidad.html` (enlazada desde Ajustes y necesaria para Google Play).
4. Si las apps de cada idioma están en el mismo usuario de GitHub (misma dirección `usuario.github.io`), el progreso guardado en el navegador se comparte: la plataforma lo encuentra solo.

## Cuenta y sincronización (opcional)
Rellena `firebase-config.js` con la configuración de tu proyecto de Firebase y publica `firestore.rules`.
El progreso se guarda en `users/<uid>` (italiano) y `users/<uid>/courses/<idioma>` (resto), igual que en las apps sueltas, así que comparten cuenta.

## Actualizar
Cada vez que publiques cambios, sube el número de `VERSION` en `sw.js` para que la app instalada se actualice.
''')

# ------------------------------------------------------------------ artefacto
A = R + '/artifact-platform'
if os.path.exists(A): shutil.rmtree(A)
os.makedirs(A)
open(A + '/saimap-lingo-idiomas.html', 'w', encoding='utf8').write(page.replace('<!--SCRIPTS-->', '<script src="courses.js"></script>\n<script src="platform.js"></script>\n'))
for n in ('engine.js', 'app.js', 'platform.js', 'courses.js'):
    shutil.copy(W + '/' + n, A + '/' + n)
for cid in ORDER:
    os.makedirs(f'{A}/courses/{cid}', exist_ok=True)
    shutil.copy(f'{W}/courses/{cid}/course.js', f'{A}/courses/{cid}/course.js')
print('ok plataforma', [(m['id'], m['store'], m['cloud'], len(m['levels'])) for m in META])
