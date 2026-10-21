import os, shutil, json, re, sys
R=os.path.dirname(os.path.abspath(__file__)); src=lambda n: open(os.path.join(R,'src',n),encoding='utf8').read()
FILES=('pics.js','scenes.js','data.js','data-a2.js','data-b1.js','data-b2.js','data-c1.js','data-c2.js','engine.js','app.js')
SHARED=('engine.js','app.js')   # el motor y la interfaz son comunes; el contenido cambia con el curso
COURSES={
 'it': dict(id='it', dir='', img='/tmp/claude-0/-home-claude/cfd6ae6c-c1ad-59b2-85f6-b4a9eb174ac8/scratchpad/book/out', artifact='artifact', html='saimap-lingo.html', web='web',
            title='SAIMAP Lingo', app='SAIMAP Lingo', desc='SAIMAP Lingo: aprende italiano desde cero con lecciones cortas y repaso continuo.', sw='saimap-lingo-c2-v12', pkg='com.saimap.lingo', adj='italiana'),
 'en': dict(id='en', dir='en/', img='/home/claude/books/english/img', artifact='artifact-en', html='saimap-lingo-ingles.html', web='web-en',
            title='SAIMAP Lingo Inglés', app='SAIMAP Lingo Inglés', desc='SAIMAP Lingo: aprende inglés británico desde cero con lecciones cortas y repaso continuo.', sw='saimap-lingo-en-v4', pkg='com.saimap.lingo.en', adj='inglesa'),
    'pt': dict(id='pt', dir='pt/', img='/home/claude/books/portugues/img', artifact='artifact-pt', html='saimap-lingo-portugues.html', web='web-pt',
            title='SAIMAP Lingo Portugués', app='SAIMAP Lingo Portugués', desc='SAIMAP Lingo: aprende portugués europeo desde cero con lecciones cortas y repaso continuo.', sw='saimap-lingo-pt-v4', pkg='com.saimap.lingo.pt', adj='portuguesa'),
  'fr': dict(id='fr', dir='fr/', img='/home/claude/books/francais/img', artifact='artifact-fr', html='saimap-lingo-frances.html', web='web-fr', title='SAIMAP Lingo Francés', app='SAIMAP Lingo Francés', desc='SAIMAP Lingo: aprende francés de Francia desde cero con lecciones cortas y repaso continuo.', sw='saimap-lingo-fr-v4', pkg='com.saimap.lingo.fr', adj='francesa'),
  'de': dict(id='de', dir='de/', img='/home/claude/books/deutsch/img', artifact='artifact-de', html='saimap-lingo-aleman.html', web='web-de', title='SAIMAP Lingo Alemán', app='SAIMAP Lingo Alemán', desc='SAIMAP Lingo: aprende alemán estándar desde cero con lecciones cortas y repaso continuo.', sw='saimap-lingo-de-v4', pkg='com.saimap.lingo.de', adj='alemana'),
  'el': dict(id='el', dir='el/', img='/home/claude/books/ellinika/img', artifact='artifact-el', html='saimap-lingo-griego.html', web='web-el', title='SAIMAP Lingo Griego', app='SAIMAP Lingo Griego', desc='SAIMAP Lingo: aprende griego moderno desde cero con lecciones cortas y repaso continuo.', sw='saimap-lingo-el-v1', pkg='com.saimap.lingo.el', adj='griega'),
  'ca': dict(id='ca', dir='ca/', img='/home/claude/books/catala/img', artifact='artifact-ca', html='saimap-lingo-catalan.html', web='web-ca', title='SAIMAP Lingo Catalán', app='SAIMAP Lingo Catalán', desc='SAIMAP Lingo: aprende catalán desde cero con lecciones cortas y repaso continuo.', sw='saimap-lingo-ca-v1', pkg='com.saimap.lingo.ca', adj='catalana'),
}
def build(K):
    csrc=lambda n: src(n if n in SHARED else K['dir']+n) if n in SHARED or os.path.exists(os.path.join(R,'src',K['dir']+n)) else 'window.SCENES = {};'
    page=src('app.html').replace('<title>SAIMAP Lingo</title>','<title>%s</title>'%K['title'])
    # 1) Artefacto: un solo HTML con los scripts dentro
    A=R+'/'+K['artifact']; os.makedirs(A+'/img',exist_ok=True)
    inl='<script>window.LINGO_AUDIO = { base: "audio/" };</script>\n'+''.join('<script>\n%s\n</script>\n'%csrc(n) for n in FILES)
    open(A+'/'+K['html'],'w',encoding='utf8').write(page.replace('<!--SCRIPTS-->',inl))
    # 2) Web / PWA
    W=R+'/'+K['web']; os.makedirs(W+'/img',exist_ok=True); os.makedirs(W+'/icons',exist_ok=True); os.makedirs(W+'/.well-known',exist_ok=True)
    for i in range(1,51):
        for d in (A+'/img',W+'/img'): shutil.copy(f"{K['img']}/u{i:02d}.png",f'{d}/u{i:02d}.png')
    for n in FILES: open(W+'/'+n,'w',encoding='utf8').write(csrc(n))
    title,rest=re.match(r'(<title>.*?</title>)\n(.*)',page,re.S).groups()
    head=f'''<!doctype html>
    <html lang="es">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
    {title}
    <meta name="description" content="{K['desc']}">
    <meta name="theme-color" content="#1F5FD1">
    <link rel="manifest" href="manifest.webmanifest">
    <link rel="icon" href="icons/icon-192.png">
    <link rel="apple-touch-icon" href="icons/icon-192.png">
    <style>:root{{padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
    '''
    scripts='''<script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>
    <script src="firebase-config.js"></script>
    <script src="audio-config.js"></script>
    <script src="pics.js"></script>
    <script src="scenes.js"></script>
    <script src="data.js"></script>
    <script src="data-a2.js"></script>
    <script src="data-b1.js"></script>
    <script src="data-b2.js"></script>
    <script src="data-c1.js"></script>
    <script src="data-c2.js"></script>
    <script src="engine.js"></script>
    <script src="app.js"></script>
    <script>if("serviceWorker" in navigator) addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));</script>
    '''
    link,body=re.match(r'(<link[^>]*>)\n(.*)',rest,re.S).groups()
    style,markup=re.match(r'(<style>.*?</style>)\n(.*)',body,re.S).groups()
    open(W+'/index.html','w',encoding='utf8').write(head+link+'\n'+style+'\n</head>\n<body>\n'+markup.replace('<!--SCRIPTS-->',scripts)+'</body>\n</html>\n')
    if not os.path.exists(W+'/firebase-config.js'):
        open(W+'/firebase-config.js','w').write('''// Pega aquí la configuración de tu proyecto de Firebase (Consola > Configuración del proyecto > Tus apps > Web).
    // Mientras apiKey esté vacío, la app funciona en modo invitado y guarda el progreso solo en el navegador.
    window.SAIMAP_FIREBASE = {
      apiKey: "",
      authDomain: "",
      projectId: "",
      appId: ""
    };
    ''')
    json.dump({"name":K["app"],"short_name":K["app"],"description":K["desc"],"lang":"es","start_url":"./","scope":"./","display":"standalone","orientation":"portrait","background_color":"#F2F5FB","theme_color":"#1F5FD1","categories":["education"],
     "icons":[{"src":"icons/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icons/icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icons/maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},open(W+'/manifest.webmanifest','w'),ensure_ascii=False,indent=1)
    shell=["./","index.html","pics.js","scenes.js","data.js","data-a2.js","data-b1.js","data-b2.js","data-c1.js","data-c2.js","engine.js","app.js","firebase-config.js","audio-config.js","manifest.webmanifest","icons/icon-192.png"]+[f"img/u{i:02d}.png" for i in range(1,51)]
    open(W+'/sw.js','w').write('''// Caché sencilla para que la app abra sin conexión. Sube el número de versión en cada publicación.
    const VERSION = "%s";
    const SHELL = %s;
    self.addEventListener("install", e => e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())));
    self.addEventListener("activate", e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())));
    self.addEventListener("fetch", e => {
      const u = new URL(e.request.url);
      if (e.request.method !== "GET" || u.origin !== location.origin) return;   // Firebase y Google van siempre a la red
      e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(VERSION).then(c => c.put(e.request, copy)); return r; }).catch(() => caches.match(e.request).then(r => r || caches.match("index.html"))));
    });
    ''' % (K['sw'], json.dumps(shell)))
    open(W+'/firestore.rules','w').write('''rules_version = '2';
    service cloud.firestore {
      match /databases/{database}/documents {
        // Cada persona solo puede leer y escribir su propio progreso.
        match /users/{uid}/{document=**} {
          allow read, write: if request.auth != null && request.auth.uid == uid;
        }
      }
    }
    ''')
    open(W+'/.well-known/assetlinks.json','w').write('''[{
      "relation": ["delegate_permission/common.handle_all_urls"],
      "target": { "namespace": "android_app", "package_name": "%s",
                  "sha256_cert_fingerprints": ["PEGA_AQUI_LA_HUELLA_SHA256_DE_TU_CLAVE_DE_FIRMA"] }
    }]
    ''' % K['pkg'])
    open(W+'/audio-config.js','w').write('''// Audio grabado con voz %s: un archivo por unidad en audio/ (u01.js … u50.js).
    // Para volver a la voz del dispositivo, pon dos barras delante de la línea siguiente.
    window.LINGO_AUDIO = { base: "audio/" };
    ''' % K['adj'])
    print('ok', K['id'])

COURSES['it-scn']=dict(COURSES['it'], artifact='artifact-it-scn', web='web-it-scn', html='saimap-lingo-escenarios.html', title='SAIMAP Lingo · Escenarios')   # prueba de fondos ilustrados
for c in (sys.argv[1:] or [k for k in COURSES if k != 'it-scn']): build(COURSES[c])
