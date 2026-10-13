# SAIMAP Lingo · plataforma con todos los idiomas

Italiano, inglés, portugués, francés y alemán en una sola web. Al entrar se elige idioma; la bandera de arriba permite cambiarlo.
La racha y los XP son comunes a todos los idiomas; cada curso guarda sus unidades, estrellas y puntos flojos.

## Estructura
- `index.html`, `platform.js` (pantalla de idiomas y carga del curso), `engine.js` y `app.js` (comunes a todos los cursos).
- `courses.js`: lista de cursos (nombre, niveles, dónde guarda cada uno su progreso).
- `courses/<idioma>/`: datos, escenarios (`scenes.js`), ilustraciones (`img/`) y audio grabado (`audio/`).
- Enlaces directos a un idioma: `…/#it`, `…/#en`, `…/#pt`, `…/#fr`, `…/#de`.

## Publicar en GitHub Pages
1. Sube el contenido de esta carpeta a un repositorio (incluido `.nojekyll`).
2. Settings › Pages › Deploy from a branch › `main` / raíz.
3. Si las apps de cada idioma están en el mismo usuario de GitHub (misma dirección `usuario.github.io`), el progreso guardado en el navegador se comparte: la plataforma lo encuentra solo.

## Cuenta y sincronización (opcional)
Rellena `firebase-config.js` con la configuración de tu proyecto de Firebase y publica `firestore.rules`.
El progreso se guarda en `users/<uid>` (italiano) y `users/<uid>/courses/<idioma>` (resto), igual que en las apps sueltas, así que comparten cuenta.

## Actualizar
Cada vez que publiques cambios, sube el número de `VERSION` en `sw.js` para que la app instalada se actualice.
