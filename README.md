# SAIMAP Lingo · código fuente y herramientas

Rama `fuente`: todo lo necesario para crear libros y cursos nuevos y reconstruir la plataforma.
La rama `main` contiene solo la web publicada (GitHub Pages) y el proyecto Android (`android/`).

## Restaurar en una sesión nueva
```bash
git clone -b fuente https://github.com/SAIMAP-SKOOL/SAIMAP-Lingo.git /tmp/fuente
cp -r /tmp/fuente/lingo /home/claude/lingo
cp -r /tmp/fuente/books /home/claude/books
cp -r /tmp/fuente/tts   /home/claude/tts
git clone https://github.com/SAIMAP-SKOOL/SAIMAP-Lingo.git /home/claude/saimap-lingo   # web publicada
# audio grabado e imágenes ya están en la web publicada: copiar a lingo/platform antes de reconstruir
mkdir -p /home/claude/lingo/platform && cp -r /home/claude/saimap-lingo/courses /home/claude/lingo/platform/
```

## Estructura
- `lingo/src/` — app común (`app.html`, `app.js`, `engine.js`, `platform.js`, páginas legales) y un directorio por idioma (`en/ pt/ fr/ de/ el/`; el italiano está en la raíz de `src/`): `data*.js`, `pics.js`, `scenes.js`.
- `lingo/tools/` — escenarios ilustrados: `scenes_courses.py` (LOCS y PLANS por idioma), `scenes_local.py` (piezas locales), `scenes_build.py <idioma>`.
- `lingo/build.py <idioma>` — app suelta por idioma; `lingo/build_platform.py` — plataforma con todos los idiomas.
- `lingo/check_course.js src/<idioma>` — valida el formato del curso.
- `books/kit/` — motor de libros (lib.py con temas por idioma, render, PDF). `books/<idioma>/` — fuentes de cada libro (md, book.json, art.py, img/).
- `tts/<idioma>/export.js` (lista de frases) y `gen.py` (voz Piper con sherpa-onnx), empaquetado con `lingo/web/tools/empaquetar_audio.py`.
