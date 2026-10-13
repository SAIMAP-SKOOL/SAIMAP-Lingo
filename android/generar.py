"""Genera el proyecto Android (Trusted Web Activity) de SAIMAP Lingo a partir de la plantilla de Bubblewrap.
La app abre https://saimap-skool.github.io/SAIMAP-Lingo/ a pantalla completa, sin barra del navegador.
Uso: python3 android/generar.py <ruta a bubblewrap/packages/core/template_project>
Para publicar una versión nueva en Play: sube VERSION_CODE (y VERSION_NAME) y vuelve a generar."""
import os, re, sys, shutil
from PIL import Image

PACKAGE = 'com.saimap.lingo'
HOST = 'saimap-skool.github.io'
PATH = '/SAIMAP-Lingo/'
NAME = 'SAIMAP Lingo'
LAUNCHER = 'SAIMAP Lingo'
VERSION_CODE = 1
VERSION_NAME = '1.0.0'
THEME = '#1F5FD1'
BACKGROUND = '#F2F5FB'

HERE = os.path.dirname(os.path.abspath(__file__))
ICONS = os.path.join(HERE, '..', 'icons')
OUT = os.path.join(HERE, 'twa')
TPL = sys.argv[1]

V = dict(packageId=PACKAGE, host=HOST, startUrl=PATH, name=NAME, launcherName=LAUNCHER)
SIMPLE = {
    "<%= packageId %>": PACKAGE, "<%= host %>": HOST, "<%= startUrl %>": PATH,
    "<%= escapeGradleString(name) %>": NAME, "<%= escapeGradleString(launcherName) %>": LAUNCHER,
    "<%= themeColor.hex() %>": THEME, "<%= themeColorDark.hex() %>": '#0B1C3D',
    "<%= navigationColor.hex() %>": BACKGROUND, "<%= navigationColorDark.hex() %>": '#0E1626',
    "<%= navigationDividerColor.hex() %>": BACKGROUND, "<%= navigationDividerColorDark.hex() %>": '#0E1626',
    "<%= backgroundColor.hex() %>": BACKGROUND, "<%= enableNotifications %>": 'false',
    "<%= generateShortcuts() %>": '[]', "<%= splashScreenFadeOutDuration %>": '300',
    "<%= generatorApp %>": 'saimap-lingo', "<%= fallbackType %>": 'customtabs',
    "<%= enableSiteSettingsShortcut %>": 'true', "<%= orientation %>": 'portrait',
    "<%= minSdkVersion %>": '21', "<%= appVersionCode %>": str(VERSION_CODE), "<%= appVersionName %>": VERSION_NAME,
    "<%= toAndroidScreenOrientation(orientation) %>": 'ActivityInfo.SCREEN_ORIENTATION_PORTRAIT',
    "<%= webManifestUrl %>": f'https://{HOST}{PATH}manifest.webmanifest',
    "<%= fullScopeUrl %>": f'https://{HOST}{PATH}',
    "<%= fullScopeUrl.pathname %>": PATH,
}
# bloques condicionales de la plantilla: True = se mantienen, False = se quitan
COND = {
    "launchHandlerClientMode": False, "webManifestUrl": True, "fullScopeUrl": True, "shareTarget": False,
    "isMetaQuest": False, "isChromeOSOnly": False, "enableSiteSettingsShortcut": True,
    "additionalTrustedOrigins.length > 0": False, "displayOverride.length > 0": False, "shareTargetIntentFilter": False,
    "enableNotifications && (monochromeIconUrl || iconUrl)": False, "enableNotifications": False,
    "fullScopeUrl && fullScopeUrl.pathname !== '/'": True,
}
LISTS = {  # bucles de la plantilla → líneas generadas
    "buildGradle.configs": [], "buildGradle.repositories": ["google()", "mavenCentral()"],
    "buildGradle.dependencies": ["com.google.androidbrowserhelper:androidbrowserhelper:2.7.4"],
    "androidManifest.permissions": [], "androidManifest.applicationMetadata": [], "androidManifest.launcherActivityEntries": [],
    "androidManifest.components": [], "additionalTrustedOrigins": [],
}


def render(t, scope=None):
    """Intérprete mínimo de la plantilla EJS: if / else if / else, for...of y <%= expresiones %>."""
    scope = scope or {}
    toks = re.split(r'(<%.*?%>)', t, flags=re.S)
    out, i = [], 0
    def block(i):   # lee hasta el cierre del bloque; devuelve (ramas [(cond, toks)], índice tras el cierre)
        branches, cur, depth = [], [], 0
        while i < len(toks):
            k = toks[i]; c = k.strip()
            if re.match(r'<%\s*(if|for)\b.*\{\s*%>$', c, re.S): depth += 1; cur.append(k)
            elif re.match(r'<%\s*\}\s*%>$', c):
                if depth == 0: branches.append(cur); return branches, i + 1
                depth -= 1; cur.append(k)
            elif depth == 0 and re.match(r'<%\s*\}\s*else\b.*\{\s*%>$', c, re.S):
                branches.append(cur); cur = [k]
            else: cur.append(k)
            i += 1
        raise ValueError('bloque sin cerrar')
    while i < len(toks):
        k = toks[i]; c = k.strip()
        m_if = re.match(r'<%\s*if\s*\((.*)\)\s*\{\s*%>$', c, re.S)
        m_for = re.match(r'<%\s*for\s*\(\s*const\s+(\w+)\s+of\s+([\w.]+)\s*\)\s*\{\s*%>$', c, re.S)
        if m_if:
            branches, i = block(i + 1)
            conds = [m_if.group(1).strip()]; bodies = [branches[0]]
            for br in branches[1:]:
                mm = re.match(r'<%\s*\}\s*else\s+if\s*\((.*)\)\s*\{\s*%>$', br[0].strip(), re.S)
                conds.append(mm.group(1).strip() if mm else 'ELSE'); bodies.append(br[1:])
            for cnd, body in zip(conds, bodies):
                if cnd == 'ELSE' or evaluate(cnd):
                    out.append(render(''.join(body), scope)); break
            continue
        if m_for:
            branches, i = block(i + 1)
            for it in LISTS.get(m_for.group(2), []):
                out.append(render(''.join(branches[0]), dict(scope, **{m_for.group(1): it})))
            continue
        m_eq = re.match(r'<%=\s*(.*?)\s*%>$', c, re.S)
        if m_eq:
            e = m_eq.group(1)
            if e in scope: out.append(scope[e])
            else:
                key = '<%= ' + e + ' %>'
                assert key in SIMPLE, 'expresión desconocida: ' + e
                out.append(SIMPLE[key])
        else:
            assert not c.startswith('<%'), 'etiqueta inesperada: ' + c
            out.append(k)
        i += 1
    return ''.join(out)


def evaluate(c):
    if c.startswith("display ==="):
        return False   # display "standalone": sin metadato de modo de pantalla
    assert c in COND, 'condición desconocida: ' + c
    return COND[c]


if os.path.exists(OUT): shutil.rmtree(OUT)
for root, dirs, files in os.walk(TPL):
    for f in files:
        src = os.path.join(root, f); rel = os.path.relpath(src, TPL)
        if f.startswith('shortcut_') or f == 'enable-debug.sh': continue   # plantillas de atajos (no usamos atajos)
        if rel.endswith('.java'):
            rel = os.path.join('app/src/main/java', *PACKAGE.split('.'), os.path.basename(rel))
        dst = os.path.join(OUT, rel); os.makedirs(os.path.dirname(dst), exist_ok=True)
        if f.endswith(('.jar',)) or f in ('gradlew',):
            shutil.copy(src, dst); continue
        txt = open(src, encoding='utf8').read()
        if '<%' in txt: txt = render(txt)
        if rel == 'build.gradle': txt = txt.replace('jcenter()', 'mavenCentral()')
        open(dst, 'w', encoding='utf8').write(txt)
os.chmod(os.path.join(OUT, 'gradlew'), 0o755)

# iconos, icono adaptable y pantalla de carga
def png(src, size, dst, bg=None, pad=1.0):
    im = Image.open(src).convert('RGBA')
    if bg:
        canvas = Image.new('RGBA', (size, size), bg); inner = int(size * pad)
        canvas.alpha_composite(im.resize((inner, inner), Image.LANCZOS), ((size - inner) // 2, (size - inner) // 2)); im = canvas
    else:
        im = im.resize((size, size), Image.LANCZOS)
    os.makedirs(os.path.dirname(dst), exist_ok=True); im.save(dst)
R = OUT + '/app/src/main/res/'
for d, s in (('mdpi', 48), ('hdpi', 72), ('xhdpi', 96), ('xxhdpi', 144), ('xxxhdpi', 192)):
    png(ICONS + '/icon-512.png', s, f'{R}mipmap-{d}/ic_launcher.png')
for d, s in (('mdpi', 82), ('hdpi', 123), ('xhdpi', 164), ('xxhdpi', 246), ('xxxhdpi', 328)):
    png(ICONS + '/maskable-512.png', s, f'{R}mipmap-{d}/ic_maskable.png')
for d, s in (('mdpi', 300), ('hdpi', 450), ('xhdpi', 600), ('xxhdpi', 900), ('xxxhdpi', 1200)):
    png(ICONS + '/icon-512.png', s, f'{R}drawable-{d}/splash.png', bg=BACKGROUND, pad=.6)
print('ok', OUT)
