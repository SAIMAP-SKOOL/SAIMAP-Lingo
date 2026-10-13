// SAIMAP Lingo · interfaz
(function () {
  const E = Engine, C = COURSE;
  // Textos y ajustes que dependen del curso (COURSE.ui). Los valores por defecto son los del curso de italiano.
  const T = Object.assign({ store: "", cloud: "progress", badge: "IT", unit: "Unità", review: "Ripasso", reviewDone: "Ripasso fatto!", unitDone: "Unità {n} completata!", lessonDone: "Lezione completata!", bravo: "Complimenti!",
    lang: "italiano", langAdj: "italiana", sysLang: "Italiano", voiceRe: "^it([-_]|$)", voicePref: "^it[-_]it", voiceLang: "it-IT", voiceNames: "alice|federica|elsa|isabella|luca|diego|paola|emma|cosimo",
    keys: "àèéìòù", book: "Italiano dalla A alla Z", hello: "Ciao! Benvenuto in SAIMAP Lingo. Oggi impariamo l'italiano insieme.", greet: ["Buongiorno!", "Buon pomeriggio!", "Buonasera!"] }, C.ui || {});
  const KS = "sl." + T.store + "state", KP = "sl." + T.store + "pref", $ = s => document.querySelector(s), app = $("#app"), veil = $("#veil");
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const svg = (d, stroke) => '<svg viewBox="0 0 24 24" aria-hidden="true" ' + (stroke ? 'fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"' : 'fill="currentColor"') + '><path d="' + d + '"/></svg>';
  const I = {
    star: svg("M12 2l3 6.5 7 .9-5.1 4.8 1.3 7L12 17.8 5.8 21.2l1.3-7L2 9.4l7-.9z"),
    fire: svg("M12 2c1 4 5 5.5 5 11a5 5 0 01-10 0c0-2 1-3.5 2-4.5.3 1.5 1 2.3 2 2.5C10.5 8 11 4.5 12 2z"),
    bolt: svg("M13 2L4 14h6l-1 8 9-12h-6z"),
    user: svg("M12 12a4.5 4.5 0 100-9 4.5 4.5 0 000 9zm0 2c-4.4 0-8 2.2-8 5v2h16v-2c0-2.8-3.6-5-8-5z"),
    lock: svg("M7 10V8a5 5 0 0110 0v2h1a2 2 0 012 2v8a2 2 0 01-2 2H6a2 2 0 01-2-2v-8a2 2 0 012-2h1zm2 0h6V8a3 3 0 00-6 0v2z"),
    check: svg("M5 12.5l4.5 4.5L19 7.5", 1), x: svg("M6 6l12 12M18 6L6 18", 1), back: svg("M15 5l-7 7 7 7", 1),
    vol: svg("M4 9v6h4l5 4V5L8 9H4zm12.5 3a4 4 0 00-2-3.5v7a4 4 0 002-3.5zM14.5 4.2v2.1a6 6 0 010 11.4v2.1a8 8 0 000-15.6z"),
    book: svg("M5 3h11a3 3 0 013 3v15H7a2 2 0 01-2-2V3zm2 14.2c.3-.1.7-.2 1-.2h9V6a1 1 0 00-1-1H7v12.2z"),
    mic: svg("M12 14a3.5 3.5 0 003.5-3.5v-5a3.5 3.5 0 00-7 0v5A3.5 3.5 0 0012 14zm6-3.5a6 6 0 01-12 0H4a8 8 0 007 7.9V21h2v-2.6a8 8 0 007-7.9h-2z"),
    play: svg("M8 5v14l11-7z"), crown: svg("M3 8l4.5 4L12 5l4.5 7L21 8l-2 11H5L3 8z"),
  };
  // La mascota: un zorro ártico (blanco) sentado, con bufanda.
  function moka(mood) {
    const k = "#16223B", ln = "#8FA3C4", sad = mood === "sad", wow = mood === "wow", calm = mood === "calm";
    const o = 'stroke="' + ln + '" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"';
    const ear = (s) => { // s = 1 izquierda, -1 derecha (espejo sobre x=60)
      const X = x => 60 - s * (60 - x), dr = sad ? 5 : 0;
      return '<path d="M' + X(29) + ' 47C' + X(24) + ' 32 ' + X(24 - dr) + ' ' + (16 + dr) + ' ' + X(29 - dr) + ' ' + (5 + dr) + 'C' + X(40) + ' 12 ' + X(50) + ' 22 ' + X(54) + ' 33z" fill="url(#fxW)" ' + o + '/>' +
        '<path d="M' + X(32) + ' 41C' + X(29) + ' 31 ' + X(29 - dr) + ' ' + (21 + dr) + ' ' + X(31 - dr) + ' ' + (13 + dr) + 'C' + X(38) + ' 19 ' + X(44) + ' 26 ' + X(47) + ' 34z" fill="#3B4A6B"/>' +
        '<path d="M' + X(34) + ' 41C' + X(32) + ' 33 ' + X(32 - dr) + ' ' + (25 + dr) + ' ' + X(33 - dr) + ' ' + (19 + dr) + 'C' + X(38) + ' 24 ' + X(42) + ' 29 ' + X(45) + ' 35z" fill="#F2A9B8"/>' +
        '<path d="M' + X(36) + ' 42l' + (s * 1) + ' -8M' + X(40) + ' 40l' + (s * 1.5) + ' -7M' + X(44) + ' 38l' + (s * 1) + ' -5" stroke="#fff" stroke-width="1.6" stroke-linecap="round" fill="none"/>';
    };
    const eye = (s) => {
      const X = x => 60 - s * (60 - x);
      if (wow) return '<ellipse cx="' + X(45) + '" cy="58" rx="6.2" ry="6.8" fill="' + k + '"/><ellipse cx="' + X(45) + '" cy="58.6" rx="4.4" ry="5" fill="#D98A1E"/><circle cx="' + X(45) + '" cy="58.6" r="2.8" fill="' + k + '"/><circle cx="' + (X(45) + 2) + '" cy="56" r="1.9" fill="#fff"/>';
      if (calm) return '<path d="M' + X(38.5) + ' 58Q' + X(45) + ' 63 ' + X(51.5) + ' 59" fill="none" stroke="' + k + '" stroke-width="2.6" stroke-linecap="round"/>';
      // ojo almendrado, rasgado hacia la oreja
      return '<g transform="translate(' + X(45) + ' 58.5) scale(1.32) translate(' + (-X(45)) + ' -58.5)"><path d="M' + X(37.5) + ' ' + (sad ? 58 : 56) + 'Q' + X(44) + ' ' + (sad ? 54.5 : 51.5) + ' ' + X(52) + ' 60.5Q' + X(45) + ' ' + (sad ? 65 : 64.5) + ' ' + X(37.5) + ' ' + (sad ? 58 : 56) + 'z" fill="' + k + '"/>' +
        '<ellipse cx="' + X(45) + '" cy="' + (sad ? 60 : 58.6) + '" rx="3.6" ry="3.5" fill="#D98A1E"/><ellipse cx="' + X(45) + '" cy="' + (sad ? 60.3 : 58.8) + '" rx="1.7" ry="2.6" fill="' + k + '"/>' +
        '<circle cx="' + (X(45) + 1.6) + '" cy="' + (sad ? 58.6 : 57.2) + '" r="1.25" fill="#fff"/>' +
        (sad ? '<path d="M' + X(37) + ' 52L' + X(51) + ' 49" stroke="' + k + '" stroke-width="2" stroke-linecap="round"/>' : "") + "</g>";
    };
    const mouth = wow ? '<ellipse cx="60" cy="81.5" rx="3.6" ry="4.2" fill="' + k + '"/><ellipse cx="60" cy="83.2" rx="2" ry="1.7" fill="#E8798C"/>'
      : sad ? '<path d="M60 76.5v3M54.5 83.5q5.5-5 11 0" fill="none" stroke="' + k + '" stroke-width="2" stroke-linecap="round"/>'
        : calm ? '<path d="M60 76.5v3.2M55 80.5q2.5 1.6 5-.8q2.5 2.4 5 .8" fill="none" stroke="' + k + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
          : '<path d="M60 76.5v3.2M53.5 79.5q3 4 6.5.2q3.5 3.8 6.500-.2" fill="none" stroke="' + k + '" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M57.300 81.800q2.700 3.600 5.400 0z" fill="#E8798C"/>';
    return '<svg class="moka" viewBox="0 0 120 130" aria-hidden="true"><defs>' +
      '<linearGradient id="fxW" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".62" stop-color="#F7FAFF"/><stop offset="1" stop-color="#D7E2F4"/></linearGradient>' +
      '<linearGradient id="fxT" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#C9D7EE"/><stop offset=".5" stop-color="#F4F8FF"/><stop offset="1" stop-color="#fff"/></linearGradient>' +
      '<radialGradient id="fxB" cx=".5" cy=".3" r=".8"><stop offset="0" stop-color="#fff"/><stop offset=".7" stop-color="#F3F7FE"/><stop offset="1" stop-color="#CFDCF1"/></radialGradient></defs>' +
      '<ellipse cx="62" cy="124.500" rx="38" ry="4.500" fill="#0B1730" opacity=".13"/>' +
      // cola: penacho grande que sube por la derecha, con mechones y punta
      '<path d="M74 119C92 124 110 116 114 98C117 85 113 72 104 64C103 71 100 75 96 77C99 82 98 88 94 91C96 96 92 101 86 103C84 109 79 113 74 119z" fill="url(#fxT)" ' + o + '/>' +
      '<path d="M104 64C112 72 115 84 113 95C109 90 106 84 104 78C102 80 99 79 96 77C100 75 103 71 104 64z" fill="#fff"/>' +
      '<path d="M100 86q5 6 4 14M94 96q4 5 2 12M88 106q2 4-1 8" fill="none" stroke="' + ln + '" stroke-width="1.4" stroke-linecap="round" opacity=".8"/>' +
      // cuerpo sentado
      '<path d="M44 84C34 93 31 108 36 119C40 123 52 123 60 123C70 123 82 123 86 119C90 108 86 93 76 84z" fill="url(#fxB)" ' + o + '/>' +
      '<path d="M36 119C33 111 35 101 41 95C44 103 45 112 46 122C42 122 38 121 36 119z" fill="#DCE6F6" opacity=".75"/><path d="M86 119C89 111 87 101 81 95C78 103 77 112 76 122C80 122 84 121 86 119z" fill="#DCE6F6" opacity=".75"/>' +
      // patas delanteras
      '<path d="M50 92C49 103 49 112 48 119C48 123 59 123 59 119L59 96z" fill="#fff" ' + o + '/><path d="M70 92C71 103 71 112 72 119C72 123 61 123 61 119L61 96z" fill="#fff" ' + o + '/>' +
      '<path d="M51.500 121v-3M55.500 121.500v-3M64.500 121.500v-3M68.500 121v-3" stroke="' + ln + '" stroke-width="1.3" stroke-linecap="round"/>' +
      // pechera de pelo
      '<path d="M45 86L49 97L53 91L57 101L60 93L63 101L67 91L71 97L75 86z" fill="#fff" stroke="' + ln + '" stroke-width="1.4" stroke-linejoin="round"/>' +
      // orejas
      ear(1) + ear(-1) +
      // cabeza: mejillas con mechones que se estrechan hacia el hocico
      '<path d="M60 30C72 30 84 35 91 45C95 51 99 55 106 58C101 61 99 63 101 68C95 68 93 70 92 74C84 82 72 90 60 91C48 90 36 82 28 74C27 70 25 68 19 68C21 63 19 61 14 58C21 55 25 51 29 45C36 35 48 30 60 30z" fill="url(#fxW)" ' + o + '/>' +
      // máscara gris azulada: frente y puente del hocico
      '<path d="M60 31C67 31 73 33 78 36C73 42 68 50 66 60L60 72L54 60C52 50 47 42 42 36C47 33 53 31 60 31z" fill="#DFE8F6"/>' +
      '<path d="M60 36l-3 6M60 36l3 6M54 40l-2 5M66 40l2 5" stroke="#fff" stroke-width="1.5" stroke-linecap="round" opacity=".9"/>' +
      // hocico
      '<path d="M60 62C67 62 73 68 74 76C72 84 66 88 60 88.500C54 88 48 84 46 76C47 68 53 62 60 62z" fill="#fff"/>' +
      '<path d="M46.500 77C49 84 54 87.500 60 88.200C66 87.500 71 84 73.500 77" fill="none" stroke="' + ln + '" stroke-width="1.2" opacity=".55"/>' +
      '<circle cx="34" cy="70" r="5" fill="#F4B8C4" opacity=".55"/><circle cx="86" cy="70" r="5" fill="#F4B8C4" opacity=".55"/>' +
      eye(1) + eye(-1) +
      '<path d="M54.800 70.500C54.800 68.300 57 67.300 60 67.300C63 67.300 65.200 68.300 65.200 70.500C65.200 73.500 62 77 60 77C58 77 54.800 73.500 54.800 70.500z" fill="' + k + '"/><ellipse cx="58.600" cy="69.600" rx="1.700" ry=".9" fill="#fff" opacity=".55"/>' +
      mouth +
      '<path d="M50 77.500h.01M48.500 80.500h.01M70 77.500h.01M71.500 80.500h.01" stroke="' + ln + '" stroke-width="1.5" stroke-linecap="round"/>' +
      // bufanda
      '<path d="M39 86C52 95 68 95 81 86C83 89 84 92 83 95C68 104 52 104 37 95C36 92 37 89 39 86z" fill="var(--brand)"/>' +
      '<path d="M39.500 90.500C53 99 67 99 80.500 90.500" fill="none" stroke="var(--brand-deep)" stroke-width="1.3" opacity=".7"/>' +
      '<path d="M66 97L78 95L84 113L78 111.500L75 116L72 110.500z" fill="var(--brand-deep)"/><path d="M67 96.500l7.500-2 2 6.500-8 1z" fill="var(--brand)"/>' +
      "</svg>";
  }
  const emo = (p, cls) => p ? '<span class="emo' + (cls ? " " + cls : "") + '" aria-hidden="true">' + p + "</span>" : "";
  const LS = { get(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } }, set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { } } };
  const IMG = window.LINGO_IMG || "img/", unitImg = u => IMG + "u" + String(u).padStart(2, "0") + ".png";
  const pick = a => a[Math.floor(Math.random() * a.length)];

  let S = E.merge(E.blank(), LS.get(KS)), P = Object.assign({ audio: true, sfx: true, slow: false, free: false, voice: "", speak: true, micOff: 0 }, LS.get(KP) || {});
  let view = "home", L = null, cur = null, R = null, formErr = "";
  let toastTimer = 0;
  function toast(msg) { const t = $("#toast"); t.textContent = msg; t.hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => { t.hidden = true; }, 5000); }

  // ---------- cuenta y sincronización ----------
  const Cloud = { mode: "local", ready: false, uid: null, name: "", photo: "", email: "", write: null, err: "", auth: null };
  let pushTimer = 0;
  function save() {
    LS.set(KS, S);
    if (!Cloud.write) return;
    clearTimeout(pushTimer);
    pushTimer = setTimeout(() => { Promise.resolve().then(() => Cloud.write(JSON.parse(JSON.stringify(S)))).then(() => { Cloud.err = ""; }, () => { Cloud.err = "No se ha podido guardar en la cuenta. Se reintentará al terminar la próxima lección."; }); }, 1200);
  }
  function pulled(remote) { const before = JSON.stringify(S); S = E.merge(S, remote); LS.set(KS, S); if (!remote || JSON.stringify(E.merge(E.blank(), remote)) !== JSON.stringify(S) || before !== JSON.stringify(S)) save(); }
  const refresh = () => { if (view === "home" || view === "me") render(); };
  async function initCloud() {
    try {
      if (window.firebase && window.SAIMAP_FIREBASE && window.SAIMAP_FIREBASE.apiKey) return initFirebase();
      if (window.claude && window.claude.use) {
        const got = await Promise.all([window.claude.use("user"), window.claude.use("db")]), user = got[0], db = got[1];
        if (user && db) {
          const me = await user.me();
          if (me.id) {
            const ref = db.doc("data/users/" + me.id + "/" + T.cloud);
            Cloud.mode = "claude"; Cloud.uid = me.id; Cloud.name = me.name || ""; Cloud.photo = me.avatarUrl || "";
            Cloud.write = d => ref.set(d);
            const snap = await ref.get(); pulled(snap.exists ? snap.data() : null);
            if (PF) syncOthers(c => db.doc("data/users/" + me.id + "/" + c.cloud).get().then(x => x.exists ? x.data() : null), (c, d) => db.doc("data/users/" + me.id + "/" + c.cloud).set(d));
          }
        }
      }
    } catch (e) { Cloud.err = "No se ha podido cargar el progreso de la cuenta."; }
    Cloud.ready = true; refresh();
  }
  // Trae el progreso de los otros idiomas (solo lectura) para que la racha y los XP comunes estén al día en este dispositivo.
  // Se mezcla con lo que haya en este dispositivo (por ejemplo, progreso de invitado) y, si cambia, se sube a la cuenta.
  function syncOthers(get, put) {
    Promise.all(PF.others().map(c => get(c).then(remote => {
      const key = "sl." + c.store + "state", local = LS.get(key);
      if (!local && !remote) return false;
      const merged = E.merge(local || E.blank(), remote), changed = JSON.stringify(merged) !== JSON.stringify(local);
      if (changed) LS.set(key, merged);
      if (put && JSON.stringify(merged) !== JSON.stringify(remote ? E.merge(E.blank(), remote) : null)) put(c, merged).catch(() => { });
      return changed;
    }, () => false))).then(r => { if (r.some(Boolean)) refresh(); });
  }
  // Borra del dispositivo el progreso de todos los idiomas (al cerrar sesión o borrar la cuenta).
  function clearLocal() { S = E.blank(); LS.set(KS, S); if (PF) PF.courses.forEach(c => { try { localStorage.removeItem("sl." + c.store + "state"); } catch (e) { } }); LS.set(KS, S); }
  function initFirebase() {
    firebase.initializeApp(window.SAIMAP_FIREBASE);
    const auth = firebase.auth(), fs = firebase.firestore();
    Cloud.mode = "firebase"; Cloud.auth = auth; Cloud.fs = fs; auth.languageCode = "es";
    auth.onAuthStateChanged(async u => {
      if (u) {
        Cloud.uid = u.uid; Cloud.name = u.displayName || ""; Cloud.email = u.email || ""; Cloud.photo = u.photoURL || "";
        const base = fs.collection("users").doc(u.uid), ref = C.id ? base.collection("courses").doc(C.id) : base; Cloud.write = d => ref.set(d);
        try { const s = await ref.get(); pulled(s.exists ? s.data() : null); Cloud.err = ""; } catch (e) { Cloud.err = "No se ha podido cargar el progreso de la cuenta."; }
        const docOf = c => c.id === "it" ? base : base.collection("courses").doc(c.id);
        if (PF) syncOthers(c => docOf(c).get().then(x => x.exists ? x.data() : null), (c, d) => docOf(c).set(d));
      } else { Cloud.uid = null; Cloud.write = null; Cloud.name = Cloud.email = Cloud.photo = ""; }
      Cloud.ready = true; refresh();
    });
  }
  const authMsg = e => ({ "auth/invalid-credential": "Correo o contraseña incorrectos.", "auth/wrong-password": "Correo o contraseña incorrectos.", "auth/user-not-found": "No hay ninguna cuenta con ese correo.", "auth/email-already-in-use": "Ya existe una cuenta con ese correo. Pulsa «Entrar».", "auth/weak-password": "La contraseña debe tener al menos 6 caracteres.", "auth/invalid-email": "Escribe un correo válido.", "auth/popup-closed-by-user": "Has cerrado la ventana de Google antes de terminar." }[e && e.code] || "No se ha podido iniciar sesión. Inténtalo de nuevo.");
  function google() { const p = new firebase.auth.GoogleAuthProvider(); Cloud.auth.signInWithPopup(p).catch(e => { if (e && (e.code === "auth/popup-blocked" || e.code === "auth/operation-not-supported-in-this-environment")) return Cloud.auth.signInWithRedirect(p); formErr = authMsg(e); refresh(); }); }
  function emailAuth(create) { const m = $("#email").value.trim(), p = $("#pass").value; formErr = ""; Cloud.auth[create ? "createUserWithEmailAndPassword" : "signInWithEmailAndPassword"](m, p).catch(e => { formErr = authMsg(e); refresh(); }); }
  function signOut() { clearTimeout(pushTimer); const w = Cloud.write, snap = JSON.parse(JSON.stringify(S)); Promise.resolve(w && w(snap)).catch(() => { }).then(() => Cloud.auth.signOut()).then(() => { clearLocal(); refresh(); }); }
  function resetPass() {
    const m = ($("#email") || {}).value; formErr = "";
    if (!m || !/.+@.+\..+/.test(m.trim())) { formErr = "Escribe tu correo arriba y vuelve a pulsar «¿Olvidaste la contraseña?»."; return refresh(); }
    Cloud.auth.sendPasswordResetEmail(m.trim()).then(() => { formErr = "Te hemos enviado un correo a " + m.trim() + " para crear una contraseña nueva. Mira también en spam."; refresh(); }, e => { formErr = authMsg(e); refresh(); });
  }
  // Borra la cuenta: primero el progreso de todos los idiomas en Firestore y después el usuario.
  async function deleteAccount() {
    const u = Cloud.auth && Cloud.auth.currentUser; if (!u) return hide();
    const msg = t => { const el = $("#delmsg"); if (el) el.textContent = t; }, btn = $("#delgo"); if (btn) btn.disabled = true;
    msg("Borrando…");
    try {
      const pass = ($("#delpass") || {}).value;
      const isPass = u.providerData.some(p => p.providerId === "password"), isGoogle = u.providerData.some(p => p.providerId === "google.com");
      // Firebase pide un inicio de sesión reciente para borrar la cuenta: se confirma antes de tocar nada.
      if (isPass && !isGoogle) await u.reauthenticateWithCredential(firebase.auth.EmailAuthProvider.credential(u.email, pass || ""));
      else if (isGoogle) await u.reauthenticateWithPopup(new firebase.auth.GoogleAuthProvider());
      clearTimeout(pushTimer); Cloud.write = null;
      const base = Cloud.fs.collection("users").doc(u.uid), ids = PF ? PF.courses.map(c => c.id) : [C.id || "it"];
      await Promise.all(ids.filter(id => id !== "it").map(id => base.collection("courses").doc(id).delete()));
      await base.delete();
      await u.delete();
      clearLocal(); hide(); formErr = "Tu cuenta y tu progreso se han borrado."; view = "me"; render();
    } catch (e) {
      if (btn) btn.disabled = false;
      msg(e && (e.code === "auth/wrong-password" || e.code === "auth/invalid-credential") ? "La contraseña no es correcta." : e && e.code === "auth/popup-closed-by-user" ? "Has cerrado la ventana de Google sin confirmar." : e && e.code === "auth/requires-recent-login" ? "Por seguridad, cierra sesión, vuelve a entrar y repite el borrado." : "No se ha podido borrar la cuenta. Comprueba la conexión e inténtalo de nuevo.");
    }
  }
  function askDelete() {
    const u = Cloud.auth && Cloud.auth.currentUser; if (!u) return;
    const needPass = u.providerData.some(p => p.providerId === "password") && !u.providerData.some(p => p.providerId === "google.com");
    show('<h2>¿Borrar tu cuenta?</h2><p class="sub">Se borran tu cuenta y el progreso de todos los idiomas, en la nube y en este dispositivo. No se puede deshacer.</p>' +
      (needPass ? '<input id="delpass" class="field" type="password" autocomplete="current-password" placeholder="Tu contraseña, para confirmar">' : '<p class="sub">Te pediremos confirmar con tu cuenta de Google.</p>') +
      '<p class="err" id="delmsg" aria-live="polite"></p><button class="btn warn" id="delgo" data-act="delacct">Borrar mi cuenta</button><button class="btn plain" data-act="hide">Cancelar</button>');
  }

  // ---------- voz ----------
  // Solo se habla con una voz real del idioma del curso. Si el dispositivo no tiene ninguna, se avisa en vez de leer con otra voz.
  const synth = window.speechSynthesis, CLIPS = window.LINGO_AUDIO || null;
  let voices = [], itVoice = null, anyVoices = false, warned = false, clip = null;
  const rank = v => { const n = (v.name || "").toLowerCase(); let s = 0; if (new RegExp(T.voicePref, "i").test(v.lang)) s += 10; if (/natural|neural|premium|enhanced|siri/.test(n)) s += 6; if (/google/.test(n)) s += 5; if (new RegExp(T.voiceNames).test(n)) s += 2; if (/compact|espeak/.test(n)) s -= 4; return s; };
  function loadVoices() {
    let all = []; try { all = synth.getVoices() || []; } catch (e) { }
    anyVoices = all.length > 0;
    voices = all.filter(v => new RegExp(T.voiceRe, "i").test(v.lang || "")).sort((a, b) => rank(b) - rank(a));
    itVoice = voices.find(v => v.voiceURI === P.voice) || voices[0] || null;
  }
  if (synth) { loadVoices(); try { synth.addEventListener("voiceschanged", () => { const had = !!itVoice; loadVoices(); if (!had && itVoice && view === "me") render(); }); } catch (e) { } }
  const spoken = t => String(t).replace(/\([^)]*\)/g, " ").replace(/[→=+]/g, ", ").replace(/[«»_]/g, " ").replace(/\s+/g, " ").trim();
  function tts(t) {
    if (!synth) return; loadVoices();
    if (!itVoice && anyVoices) { if (!warned) { warned = true; toast("Este dispositivo no tiene voz " + T.langAdj + " instalada. En tu perfil te explico cómo añadirla."); } return; }
    try {
      synth.cancel(); const u = new SpeechSynthesisUtterance(spoken(t)); u.lang = itVoice ? String(itVoice.lang).replace("_", "-") : T.voiceLang; if (itVoice) u.voice = itVoice; u.rate = P.slow ? 0.7 : 0.92;
      setTimeout(() => { try { synth.speak(u); } catch (e) { } }, 60);
    } catch (e) { }
  }
  // Audio grabado: un archivo por unidad (audio/u01.js …) con todos sus MP3 dentro. Se carga con <script>, así funciona también abriendo index.html desde el disco.
  const PACKS = window.LINGO_PACK = window.LINGO_PACK || {}, packWait = {};
  function loadPack(u) {
    if (PACKS[u]) return Promise.resolve(PACKS[u]);
    return packWait[u] = packWait[u] || new Promise(res => { const sc = document.createElement("script"); sc.src = CLIPS.base + "u" + String(u).padStart(2, "0") + ".js"; sc.onload = () => res(PACKS[u] || null); sc.onerror = () => { delete packWait[u]; res(null); }; document.head.appendChild(sc); });
  }
  let sayTurn = 0;
  function say(t, key) {
    if (!P.audio) return;
    if (CLIPS && key) {
      const u = String(key).split(".")[0], turn = ++sayTurn;
      loadPack(u).then(p => {
        if (turn !== sayTurn) return; const b64 = p && p[String(key).slice(u.length + 1)]; if (!b64) return tts(t);
        try { if (clip) clip.pause(); clip = new Audio("data:audio/mpeg;base64," + b64); clip.playbackRate = P.slow ? 0.75 : 1; clip.play().catch(() => { }); } catch (e) { tts(t); }
      });
      return;
    }
    tts(t);
  }
  const stopClip = () => { sayTurn++; if (clip) try { clip.pause(); } catch (e) { } };
  // ---------- hablar: reconocimiento de voz del navegador (Chrome, Edge, Safari) ----------
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  const policy = document.permissionsPolicy || document.featurePolicy;
  const micPolicy = !policy || !policy.allowsFeature || policy.allowsFeature("microphone");
  const srSupported = () => !!SR && micPolicy && window.isSecureContext !== false;
  let micBlocked = false, rec = null;
  const canSpeak = () => srSupported() && P.speak && !micBlocked && Date.now() > (P.micOff || 0);
  const opts0 = () => ({ voice: canListen(), speak: canSpeak() });
  function stopRec() { if (rec) { try { rec.onresult = rec.onerror = rec.onend = null; rec.abort(); } catch (e) { } rec = null; } const b = $("#mic"); if (b) b.classList.remove("on"); }
  function listen() {
    if (!cur || cur.checked || cur.ex.type !== "speak") return;
    if (rec) return stopRec();
    if (synth) synth.cancel(); stopClip();
    const r = new SR(); rec = r; r.lang = T.voiceLang; r.interimResults = true; r.maxAlternatives = 5; r.continuous = false;
    const b = $("#mic"), out = $("#heard"); b.classList.add("on"); out.className = "heard"; out.textContent = "Te escucho…";
    let finalAlts = null;
    r.onresult = ev => {
      const res = ev.results[ev.results.length - 1]; out.textContent = "«" + res[0].transcript + "»";
      if (res.isFinal) finalAlts = Array.from(res).map(a => a.transcript);
    };
    r.onerror = ev => {
      stopRec();
      if (ev.error === "not-allowed" || ev.error === "service-not-allowed") { micBlocked = true; toast("No hay permiso para usar el micrófono. Quito los ejercicios de hablar de esta sesión."); return skipSpeak(true, true); }
      out.className = "heard err"; out.textContent = ev.error === "no-speech" ? "No te he oído. Toca el micrófono y habla." : ev.error === "network" ? "El reconocimiento de voz necesita conexión a internet." : ev.error === "audio-capture" ? "No encuentro ningún micrófono." : "No he podido escucharte. Inténtalo otra vez.";
    };
    r.onend = () => { rec = null; b.classList.remove("on"); if (finalAlts) heardIt(finalAlts); else if (out.textContent === "Te escucho…") { out.className = "heard err"; out.textContent = "No te he oído. Toca el micrófono y habla."; } };
    try { r.start(); } catch (e) { stopRec(); }
  }
  function heardIt(alts) {
    if (!cur || cur.checked) return;
    const r = E.checkSpeech(cur.ex, alts), out = $("#heard"); cur.tries = (cur.tries || 0) + 1;
    if (r.ok) return settleSpeak(true, r.heard);
    if (cur.tries < 3) { out.className = "heard err"; out.textContent = "He entendido «" + r.heard + "». Inténtalo otra vez."; sfx("bad"); return; }
    settleSpeak(false, r.heard);
  }
  // Un fallo de pronunciación no cuenta como error del elemento: el reconocedor también se equivoca.
  function settleSpeak(ok, heard) {
    const it = cur.ex.item; cur.checked = true; L.n++;
    if (ok) { E.record(S, it.k, true); L.combo++; if (cur.tries === 1) L.firstOk++; } else L.combo = 0;
    $("#mic").disabled = true;
    verdict(ok, ok ? pick(YES) : "Casi, sigue practicando", (ok ? "" : "Has dicho «" + esc(heard) + "». ") + esc(it.it) + " — " + esc(it.es));
    const m = app.querySelector(".lbar .meter i"); if (m) m.style.width = (100 * L.n / L.total) + "%";
    if (!ok) say(it.it, it.k);
  }
  // Saltar el ejercicio actual; con «all», también los demás de hablar (una hora, o la sesión si no hay permiso).
  function skipSpeak(all, quiet) {
    stopRec();
    if (all) {
      if (!quiet) { P.micOff = Date.now() + 36e5; LS.set(KP, P); toast("Vale: nada de hablar durante una hora. Puedes volver a activarlo en el inicio."); }
      L.q = L.q.map((x, i) => i && x.type === "speak" ? E.build(x.item, x.item.kind === "v" ? "mcEI" : "order", x.review) : x);
    }
    L.q.shift(); L.total = Math.max(1, L.total - 1);
    if (L.q.length) { render(); window.scrollTo(0, 0); } else finishLesson();
  }
  const hasAudio = () => !!(CLIPS || synth);
  const canListen = () => !!(P.audio && (CLIPS || (synth && itVoice)));
  const sayBtn = (t, key, big) => hasAudio() ? '<button class="' + (big ? "bigsay" : "say") + '" data-say="' + esc(t) + '" data-k="' + (key || "") + '" aria-label="Escuchar">' + I.vol + "</button>" : "<span></span>";

  // ---------- efectos de sonido ----------
  let ac = null;
  const SFX = { ok: [[660, .12], [880, .2]], bad: [[230, .14], [180, .22]], win: [[523, .12], [659, .12], [784, .12], [1047, .34]], pair: [[740, .09]] };
  function sfx(name) {
    if (!P.sfx) return;
    try {
      ac = ac || new (window.AudioContext || window.webkitAudioContext)(); if (ac.state === "suspended") ac.resume(); let t = ac.currentTime;
      SFX[name].forEach(n => { const o = ac.createOscillator(), g = ac.createGain(); o.type = "triangle"; o.frequency.value = n[0]; g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.16, t + .02); g.gain.exponentialRampToValueAtTime(.0001, t + n[1]); o.connect(g); g.connect(ac.destination); o.start(t); o.stop(t + n[1] + .03); t += n[1] * .8; });
    } catch (e) { }
  }
  function confetti() {
    const cv = $("#confetti"); if (!cv || (window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches)) return;
    const cs = getComputedStyle(document.documentElement), cols = ["--u1", "--u2", "--u3", "--u4", "--sun"].map(v => cs.getPropertyValue(v).trim() || "#F5B81F");
    const W = cv.width = innerWidth, H = cv.height = innerHeight, g = cv.getContext("2d"), t0 = performance.now();
    const ps = Array.from({ length: 90 }, () => ({ x: Math.random() * W, y: -20 - Math.random() * H * .5, vx: (Math.random() - .5) * 3, vy: 2 + Math.random() * 4, s: 6 + Math.random() * 7, r: Math.random() * 6, c: pick(cols) }));
    (function step(now) {
      if (!cv.isConnected) return; g.clearRect(0, 0, W, H);
      ps.forEach(p => { p.x += p.vx; p.y += p.vy; p.r += .12; g.save(); g.translate(p.x, p.y); g.rotate(p.r); g.fillStyle = p.c; g.fillRect(-p.s / 2, -p.s / 3, p.s, p.s * .6); g.restore(); });
      if (now - t0 < 2600) requestAnimationFrame(step); else g.clearRect(0, 0, W, H);
    })(t0);
  }

  // ---------- hojas ----------
  function show(html) { veil.innerHTML = '<div class="sheet" role="dialog" aria-modal="true">' + html + "</div>"; veil.hidden = false; }
  function hide() { veil.hidden = true; veil.innerHTML = ""; }
  const wordRows = (u, m) => E.ITEMS.filter(x => x.u === u && x.m === m && x.kind === "v").map(x => sayBtn(x.it, x.k) + emo(x.pic) + (x.pic ? "" : "<span></span>") + '<span class="it">' + esc(x.it) + '</span><span class="es">' + esc(x.es) + "</span>").join("");
  function modSheet(u, m) {
    const info = E.modInfo(u, m), id = E.modId(u, m), d = S.done[id], open = E.unlocked(S, u, m, P.free), first = E.ord(u, m) === 1;
    const mix = m === 5 ? (u === 1 ? "15 ejercicios de toda la unidad." : "15 ejercicios: 9 de esta unidad y 6 de las unidades anteriores.") : first ? "13 ejercicios." : "13 ejercicios: 9 nuevos y 4 de repaso de módulos anteriores.";
    show('<div class="sheethead">' + emo(window.UNIT_PICS[u - 1]) + '<div><p class="sub">' + T.unit + ' ' + u + " · módulo " + m + ' de 5</p><h2 class="it">' + esc(info.t) + '</h2><p class="sub">' + esc(info.es) + "</p></div></div>" +
      (info.tip ? '<div class="tip"><b>Clave</b>' + esc(info.tip) + "</div>" : "") + "<p>" + mix + "</p>" +
      (open ? '<button class="btn" data-start="' + id + '">' + (d ? "Repetir" : "Empezar") + "</button>" : '<p class="sub">Completa el módulo anterior para abrir este.</p>') +
      '<button class="btn plain" data-act="hide">Cerrar</button>');
  }
  function guideSheet(u) {
    const unit = C.units[u - 1];
    let h = '<div class="sheethead">' + emo(window.UNIT_PICS[u - 1]) + '<div><p class="sub">Guía · ' + T.unit + ' ' + u + '</p><h2 class="it">' + esc(unit.t) + '</h2></div></div><img class="pic" alt="Ilustración de la unidad ' + u + '" src="' + unitImg(u) + '" width="1200" loading="lazy">';
    unit.mods.forEach((m, i) => { h += '<h3 class="it">' + (i + 1) + ". " + esc(m.t) + '</h3><div class="tip"><b>Clave</b>' + esc(m.tip) + '</div><div class="words">' + wordRows(u, i + 1) + "</div>"; });
    show(h + '<button class="btn plain" data-act="hide">Cerrar</button>');
  }

  // ---------- vistas ----------
  const GOAL = 30;
  // En la plataforma con todos los idiomas, la racha y los XP son comunes.
  const PF = window.LingoPlatform;
  const gStreak = () => PF ? PF.stats().streak : E.liveStreak(S), gXp = () => PF ? PF.stats().xp : S.xp, gToday = () => PF ? PF.stats().today : E.todayXp(S);
  function topbar() {
    const st = gStreak();
    return '<header class="top' + (PF ? " pf" : "") + '"><div class="brand">' + moka("happy") + '<span>SAIMAP <i>Lingo</i></span>' + (PF ? '' : '<b class="cbadge">' + T.badge + '</b>') + '</div>' + (PF ? '<button class="langbtn" data-act="lang" aria-label="Cambiar de idioma" title="Cambiar de idioma">' + PF.flag(PF.current) + '<span>' + T.badge + '</span></button>' : '') +
      '<span class="stat fire' + (st ? " lit" : "") + '" title="Racha de días">' + I.fire + st + '</span><span class="stat xp" title="Puntos de experiencia">' + I.bolt + gXp() + "</span>" +
      '<button class="avatar" data-act="me" aria-label="Cuenta y ajustes">' + (Cloud.photo ? '<img alt="" src="' + esc(Cloud.photo) + '">' : I.user) + "</button></header>";
  }
  function home() {
    const nx = E.nextUp(S), weak = E.weakItems(S).length, h0 = new Date().getHours(), today = gToday();
    const hi = h0 < 13 ? T.greet[0] : h0 < 19 ? T.greet[1] : T.greet[2];
    let h = topbar() + '<section class="hero">' + moka(today >= GOAL ? "wow" : "happy") + "<div><h1 class=\"it\">" + hi + "</h1><p>" +
      (nx ? "Te toca «" + esc(E.modInfo(nx.u, nx.m).t) + "», en la " + T.unit + " " + nx.u + "." : "Has completado todo el curso. " + T.bravo) + "</p>" +
      '<div class="goal"><span>Hoy</span><div class="meter" role="progressbar" aria-valuemin="0" aria-valuemax="' + GOAL + '" aria-valuenow="' + Math.min(today, GOAL) + '"><i style="width:' + Math.min(100, 100 * today / GOAL) + '%"></i></div><span>' + (today >= GOAL ? "Objetivo cumplido" : today + " / " + GOAL + " XP") + "</span></div>" +
      (nx ? '<button class="btn small" data-start="' + E.modId(nx.u, nx.m) + '">' + (S.xp ? "Continuar" : "Empezar") + "</button>" : "") + "</div></section>";
    if (Cloud.mode === "firebase" && Cloud.ready && !Cloud.uid) h += '<div class="notice"><span>Inicia sesión para guardar tu progreso en tu cuenta.</span><button class="ghost" data-act="me">Entrar</button></div>';
    if (srSupported()) h += '<div class="speakrow"><span>' + I.mic + "<span>Ejercicios de hablar" + (P.speak && Date.now() < (P.micOff || 0) ? "<small>En pausa hasta las " + new Date(P.micOff).toTimeString().slice(0, 5) + "</small>" : "<small>" + (P.speak ? "Activados: usarás el micrófono" : "Desactivados") + "</small>") + '</span></span><button class="switch" role="switch" aria-checked="' + !!(P.speak && Date.now() >= (P.micOff || 0)) + '" data-pref="speak" aria-label="Ejercicios de hablar"></button></div>';
    if (E.dailyReady(S)) { const dd = E.dailyDone(S); h += '<section class="daily' + (dd ? " done" : "") + '"><span class="dico">' + (dd ? I.check : I.fire) + '</span><div><b>Repaso del día</b><p>' + (dd ? "Hecho hoy. Puedes repetirlo cuando quieras." : E.DAILY_SIZE + " ejercicios con un poco de todo lo que has visto" + (canSpeak() ? ", también hablando" : "") + ". +20 XP") + '</p></div><button class="btn small' + (dd ? " plain" : "") + '" data-act="daily">' + (dd ? "Repetir" : "Empezar") + "</button></section>"; }
    if (weak >= 4) h += '<div class="notice"><span>Tienes ' + weak + ' puntos flojos. Un repaso corto los refuerza.</span><button class="ghost" data-act="weak">Repasar</button></div>';
    C.units.forEach(u => {
      const lv = C.levels.find(l => l.from === u.n);
      if (lv) { const tot = (lv.to - lv.from + 1) * 5, dn = Object.keys(S.done).filter(k => { const x = +k.split(".")[0]; return x >= lv.from && x <= lv.to; }).length; h += '<section class="level"><b>' + lv.id + '</b><h2 class="it">' + lv.it + '</h2><div class="meter" role="progressbar" aria-valuemin="0" aria-valuemax="' + tot + '" aria-valuenow="' + dn + '"><i style="width:' + (100 * dn / tot) + '%"></i></div><small>' + dn + "/" + tot + "</small></section>"; }
      const uOpen = E.unlocked(S, u.n, 1, P.free);
      const scn = window.SCENES && window.SCENES[u.n];
      h += '<section class="unit c' + ((u.n - 1) % 5 + 1) + (u.n % 2 ? "" : " flip") + (scn ? " scened" : "") + '"><div class="uhead' + (uOpen ? "" : " locked") + '">' + emo(window.UNIT_PICS[u.n - 1], "badge") + '<div><small>' + T.unit + ' ' + u.n + '</small><h2 class="it">' + esc(u.t) + "</h2><p>" + esc(u.es) + '</p></div><button class="ghost" data-guide="' + u.n + '">' + I.book + 'Guía</button></div>' + (scn ? '<div class="path scn' + (scn.night ? " night" : "") + '" data-road="' + scn.path + '" style="--tint:' + scn.tint + '"><div class="scene">' + scn.svg + '</div><svg class="road" aria-hidden="true"></svg>' : '<div class="path">');
      for (let m = 1; m <= 5; m++) {
        const id = E.modId(u.n, m), d = S.done[id], open = E.unlocked(S, u.n, m, P.free), now = nx && nx.u === u.n && nx.m === m;
        h += '<button class="node ' + (d ? "done" : open ? "open" : "shut") + (now ? " now" : "") + '" data-mod="' + id + '"><span class="disc">' + (d ? I.check : !open ? I.lock : m === 5 ? I.crown : I.play) + "</span><b>" + esc(E.modInfo(u.n, m).t) + '</b><span class="stars">' + (d ? [1, 2, 3].map(i => I.star.replace("<svg", '<svg class="' + (i <= d.s ? "on" : "") + '"')).join("") : "") + "</span></button>";
      }
      h += "</div></section>";
    });
    requestAnimationFrame(drawRoads);
    app.innerHTML = h + '<p class="foot">Curso completo de A1 a C2, según el libro «' + T.book + '».</p>';
  }
  const sw = (key, title, sub) => '<div class="row"><span>' + title + "<small>" + sub + '</small></span><button class="switch" role="switch" aria-checked="' + !!P[key] + '" data-pref="' + key + '" aria-label="' + title + '"></button></div>';
  function me() {
    const seen = Object.keys(S.it).length, mods = Object.keys(S.done).length;
    let acct;
    if (Cloud.mode === "firebase" && !Cloud.uid) {
      acct = '<h3>Inicia sesión</h3><p class="sub">Tu progreso se guarda en tu cuenta y te sigue en cualquier dispositivo.</p><button class="btn" data-act="google">Entrar con Google</button>' +
        '<form class="form" id="mailform"><input id="email" type="email" autocomplete="email" placeholder="Correo electrónico" required><input id="pass" type="password" autocomplete="current-password" placeholder="Contraseña" required minlength="6">' +
        '<button class="btn plain" type="submit">Entrar con correo</button><button class="btn plain" type="button" data-act="signup">Crear cuenta</button><button class="linkbtn" type="button" data-act="resetpass">¿Olvidaste la contraseña?</button></form>' + (formErr ? '<p class="err">' + esc(formErr) + "</p>" : "");
    } else {
      const status = Cloud.mode === "claude" ? "Progreso guardado en tu cuenta de Claude" : Cloud.mode === "firebase" ? "Sesión iniciada · progreso sincronizado" : Cloud.ready ? "El progreso se guarda solo en este navegador" : "Conectando con tu cuenta…";
      acct = '<div class="who"><span class="avatar">' + (Cloud.photo ? '<img alt="" src="' + esc(Cloud.photo) + '">' : I.user) + '</span><div><b id="whoname"></b><span class="sub">' + status + "</span></div></div>" +
        (Cloud.mode === "firebase" ? '<button class="btn plain" data-act="signout">Cerrar sesión</button><button class="linkbtn danger" data-act="askdelete">Borrar mi cuenta</button>' : "");
    }
    loadVoices();
    const voiceInfo = CLIPS ? "<p>Audio grabado con voz " + T.langAdj + ". Funciona igual en todos los dispositivos, también sin conexión.</p>" : !synth ? '<p class="err">Este navegador no puede leer en voz alta.</p>' :
      itVoice ? '<p>Voz ' + T.langAdj + ': <b id="voicename"></b></p>' + (voices.length > 1 ? '<select class="pick" id="voice" aria-label="Elegir voz"></select>' : "") :
        anyVoices ? '<p class="err">Este dispositivo no tiene ninguna voz ' + T.langAdj + ' instalada, así que la app no lee en voz alta (antes lo hacía con una voz de otro idioma).</p><p class="sub">Para añadirla, busca «voces» o «síntesis de voz» en los ajustes del sistema y descarga ' + T.sysLang + '. En Android suele estar en Ajustes › Sistema › Idiomas › Salida de síntesis de voz; en Windows, en Hora e idioma › Voz; en iPhone y Mac, en Accesibilidad › Contenido leído › Voces. Después vuelve a abrir la app.</p>' :
          '<p class="sub">El navegador todavía no ha dado su lista de voces. Pulsa «Probar la voz».</p>';
    app.innerHTML = '<button class="back" data-act="home">' + I.back + 'Volver al curso</button><div class="stack"><div class="card">' + acct + (Cloud.err ? '<p class="err">' + esc(Cloud.err) + "</p>" : "") + "</div>" +
      '<div class="tiles"><div class="tilebox"><b>' + gXp() + '</b><small>XP' + (PF ? " (todos los idiomas)" : "") + '</small></div><div class="tilebox"><b>' + gStreak() + '</b><small>días de racha</small></div><div class="tilebox"><b>' + mods + "</b><small>módulos</small></div></div>" +
      '<div class="card"><h3>Voz</h3>' + voiceInfo + '<button class="btn plain" data-act="testvoice">Probar la voz</button>' +
      sw("audio", "Audio en " + T.lang, "Lee palabras y frases, y activa los ejercicios de escucha") + sw("slow", "Voz lenta", "Para oír cada sílaba con calma") + sw("sfx", "Efectos de sonido", "Aciertos, fallos y final de lección") + "</div>" +
      '<div class="card"><h3>Hablar</h3>' + (srSupported() ? sw("speak", "Ejercicios de hablar", "Lees frases en voz alta y la app comprueba tu pronunciación con el micrófono") : '<p class="sub">' + (SR ? "Aquí no se puede usar el micrófono. Abre la app desde su web o instálala para practicar hablando." : "Este navegador no reconoce la voz. Para practicar hablando, usa Chrome, Edge o Safari.") + "</p>") + "</div>" +
      '<div class="card">' + sw("free", "Modo libre", "Abre todos los módulos sin seguir el orden") + "</div>" +
      '<div class="card"><div class="row"><span>Has practicado ' + seen + " de " + E.ITEMS.length + ' elementos del curso<small>Palabras, frases y huecos de gramática</small></span></div><button class="btn plain" data-act="askreset">Borrar mi progreso</button></div>' +
      '<p class="sub legal"><a href="https://saimap-skool.github.io/SAIMAP-Lingo/privacidad.html" target="_blank" rel="noopener">Política de privacidad</a> · soloaimaproject@gmail.com</p></div>';
    const w = $("#whoname"); if (w) w.textContent = Cloud.name || Cloud.email || (Cloud.mode === "local" ? "Invitado" : "Tu cuenta");
    const vn = $("#voicename"); if (vn) vn.textContent = itVoice.name;
    const sel = $("#voice"); if (sel) voices.forEach(v => { const o = document.createElement("option"); o.value = v.voiceURI; o.textContent = v.name + " (" + v.lang + ")"; o.selected = v === itVoice; sel.appendChild(o); });
  }

  // ---------- lección ----------
  function start(u, m) {
    hide(); loadVoices(); const q = E.gen(S, u, m, opts0()), id = E.modId(u, m);
    if (CLIPS) { loadPack(u); q.forEach(x => x.item && loadPack(x.item.u)); }
    L = { u, m, id, q, total: q.length, n: 0, firstOk: 0, combo: 0, intro: m <= 4 && !S.done[id] }; view = "lesson"; render(); window.scrollTo(0, 0);
  }
  function startWeak() { loadVoices(); const q = E.genWeak(S, opts0()); if (!q.length) return; L = { u: 0, m: 0, id: null, q, total: q.length, n: 0, firstOk: 0, combo: 0, intro: false }; view = "lesson"; render(); window.scrollTo(0, 0); }
  function startDaily() {
    loadVoices(); const q = E.genDaily(S, opts0()); if (!q.length) return;
    if (CLIPS) q.forEach(x => (x.items || [x.item]).forEach(i => i && loadPack(i.u)));
    L = { u: 0, m: 0, id: null, daily: true, q, total: q.length, n: 0, firstOk: 0, combo: 0, intro: false }; view = "lesson"; render(); window.scrollTo(0, 0);
  }
  const bar = () => '<div class="lbar"><button class="x" data-act="askquit" aria-label="Salir de la lección">' + I.x + '</button><div class="meter"><i style="width:' + (100 * L.n / L.total) + '%"></i></div>' + (L.combo >= 3 ? '<span class="combo">' + I.fire + L.combo + " seguidas</span>" : "") + "</div>";
  function lesson() {
    if (L.intro) {
      const info = E.modInfo(L.u, L.m);
      app.innerHTML = '<div class="lesson">' + bar() + '<div class="lbody"><div class="intro">' + moka("happy") + '<div><p class="sub">' + T.unit + ' ' + L.u + " · módulo " + L.m + '</p><h2 class="ask it">' + esc(info.t) + '</h2></div></div><img class="pic" alt="Ilustración de la unidad ' + L.u + '" src="' + unitImg(L.u) + '" width="1200"><div class="tip"><b>Clave</b>' + esc(info.tip) + '</div><h3>Palabras nuevas</h3><div class="words">' + wordRows(L.u, L.m) +
        '</div></div><div class="lfoot"><button class="btn" data-act="begin">Empezar</button></div></div>';
      return;
    }
    const ex = L.q[0], it = ex.item; cur = { ex, sel: null, checked: false, chosen: [], miss: 0 };
    const fresh = it && !(E.st(S, it.k)[0] + E.st(S, it.k)[1]);
    const opts = (list) => '<div class="opts">' + list.map((o, i) => '<button class="opt" data-opt="' + i + '"><kbd>' + (i + 1) + "</kbd><span>" + esc(o) + "</span></button>").join("") + "</div>";
    let ask, body, auto = "";
    if (ex.type === "mcIE") { ask = "¿Qué significa?"; body = '<div class="cue">' + sayBtn(it.it, it.k) + (fresh ? emo(it.pic) : "") + '<div class="t">' + esc(it.it) + "</div></div>" + opts(ex.options); auto = 1; }
    else if (ex.type === "mcEI") { ask = "¿Cómo se dice en " + T.lang + "?"; body = '<div class="cue">' + emo(it.pic) + '<div class="t">' + esc(it.es) + "</div></div>" + opts(ex.options); }
    else if (ex.type === "picIE") { ask = "Toca la imagen correcta"; body = '<div class="cue">' + sayBtn(it.it, it.k) + '<div class="t">' + esc(it.it) + '</div></div><div class="opts pics">' + ex.options.map((o, i) => '<button class="opt" data-opt="' + i + '" aria-label="Imagen ' + (i + 1) + '"><kbd>' + (i + 1) + "</kbd>" + emo(o) + "</button>").join("") + "</div>"; auto = 1; }
    else if (ex.type === "picEI") { ask = "¿Qué es esto en " + T.lang + "?"; body = '<div class="cue big">' + emo(it.pic) + "</div>" + opts(ex.options); }
    else if (ex.type === "listen") { ask = "Escucha y elige lo que oyes"; body = '<div class="cue">' + sayBtn(it.it, it.k, 1) + '<div class="t"><small>Pulsa para volver a escuchar</small></div></div>' + opts(ex.options); auto = 1; }
    else if (ex.type === "mcS") { ask = "¿Qué significa esta frase?"; body = '<div class="cue">' + sayBtn(it.it, it.k) + '<div class="t">' + esc(it.it) + "</div></div>" + opts(ex.options); auto = 1; }
    else if (ex.type === "gap") { ask = "Completa"; body = '<div class="cue"><div class="t">' + esc(it.q).replace("___", '<span class="blank" id="blank">&nbsp;</span>') + "<small>" + esc(it.es) + "</small></div></div>" + opts(ex.options); }
    else if (ex.type === "speak") { ask = "Lee en voz alta"; body = '<div class="cue">' + sayBtn(it.it, it.k) + '<div class="t">' + esc(it.it) + "<small>" + esc(it.es) + '</small></div></div><div class="speak"><button class="mic" id="mic" data-act="mic" aria-label="Pulsa y habla">' + I.mic + '</button><p class="heard" id="heard" aria-live="polite">Toca el micrófono y lee la frase</p></div>'; auto = 1; }
    else if (ex.type === "type") { ask = "Escribe en " + T.lang; body = '<div class="cue">' + emo(it.pic) + '<div class="t">' + esc(it.es) + '</div></div><input class="field" id="answer" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="Escribe aquí"><div class="keys">' + T.keys.split("").map(c => '<button data-key="' + c + '" aria-label="Insertar ' + c + '">' + c + "</button>").join("") + "</div>"; }
    else if (ex.type === "order" || ex.type === "listenOrder") {
      const heard = ex.type === "listenOrder"; ask = heard ? "Escucha y ordena lo que oyes" : "Traduce al " + T.lang;
      body = '<div class="cue">' + (heard ? sayBtn(it.it, it.k, 1) + '<div class="t"><small>Pulsa para volver a escuchar</small></div>' : '<div class="t">' + esc(it.es) + "</div>") + '</div><div class="line" id="line" aria-label="Tu respuesta"></div><div class="bank" id="bank">' + ex.bank.map((t, i) => '<button class="tile" data-tile="' + i + '">' + esc(t) + "</button>").join("") + "</div>"; if (heard) auto = 1;
    } else {
      ask = "Empareja cada palabra con su traducción"; const a = E.shuffle(ex.items), b = E.shuffle(ex.items); cur.left = null; cur.right = null; cur.pairs = 0;
      body = '<div class="opts two">' + a.map((x, i) => '<button class="opt" data-ml="' + x.k + '">' + esc(x.it) + '</button><button class="opt" data-mr="' + b[i].k + '">' + esc(b[i].es) + "</button>").join("") + "</div>";
    }
    app.innerHTML = '<div class="lesson">' + bar() + '<div class="lbody">' + (ex.review ? '<span class="chip">Repaso · ' + T.unit + ' ' + (it ? it.u : "") + "</span>" : "") + '<h2 class="ask">' + ask + "</h2>" + body + '</div><div class="lfoot" id="foot">' + (ex.type === "match" ? "" : ex.type === "speak" ? '<div class="skips"><button class="btn plain" data-act="skipspeak">Saltar</button><button class="btn plain" data-act="nomic">Ahora no puedo hablar</button></div>' : '<button class="btn" id="go" data-act="check" disabled>Comprobar</button>') + "</div></div>";
    const f = $("#answer"); if (f) { f.focus(); f.addEventListener("input", () => { $("#go").disabled = !f.value.trim(); }); }
    if (auto) say(it.it, it.k);
  }
  const YES = ["Bravissimo!", "Ottimo!", "Perfetto!", "Esatto!", "Grande!", "Benissimo!"], NO = ["Quasi!", "Peccato!", "Ci siamo quasi!"];
  function verdict(ok, title, detail) {
    const foot = $("#foot"); foot.className = "lfoot " + (ok ? "ok" : "bad");
    foot.innerHTML = '<div class="verdict" role="status">' + moka(ok ? (L.combo >= 3 ? "wow" : "happy") : "sad") + "<div><b>" + title + "</b>" + (detail ? "<span>" + detail + "</span>" : "") + '</div></div><button class="btn ' + (ok ? "good" : "warn") + '" id="go" data-act="next">Continuar</button>';
    $("#go").focus({ preventScroll: true }); sfx(ok ? "ok" : "bad");
  }
  function settle(ok, note) {
    const ex = cur.ex, it = ex.item; cur.checked = true; E.record(S, it.k, ok);
    if (ok) { L.n++; L.combo++; if (!ex.retry) L.firstOk++; }
    else { L.combo = 0; const again = E.build(it, ex.type === "listen" || ex.type === "listenOrder" ? (it.kind === "v" ? "mcIE" : "order") : ex.type, ex.review); again.retry = true; L.q.push(again); }
    const full = (it.pic ? it.pic + " " : "") + esc(it.it) + (it.kind === "v" ? " = " : " — ") + esc(it.es);
    verdict(ok, ok ? (note || pick(YES)) : pick(NO), (ok ? "" : "Solución: ") + full);
    const m = app.querySelector(".lbar .meter i"); if (m) m.style.width = (100 * L.n / L.total) + "%";
    if (!ok || !/^(mcIE|mcS|listen|listenOrder|picIE)$/.test(ex.type)) say(it.it, it.k);
  }
  function check() {
    const ex = cur.ex; if (cur.checked) return;
    if (ex.options) {
      if (cur.sel == null) return; const ok = ex.options[cur.sel] === ex.answer;
      app.querySelectorAll("[data-opt]").forEach((b, i) => { b.classList.remove("sel"); if (ex.options[i] === ex.answer) b.classList.add("right"); else if (i === cur.sel) b.classList.add("wrong"); b.disabled = true; });
      settle(ok);
    } else if (ex.type === "type") {
      const f = $("#answer"), r = E.checkType(ex, f.value); f.disabled = true; settle(r !== "no", r === "accent" ? "Bene, pero revisa los acentos" : "");
    } else { app.querySelectorAll(".tile").forEach(b => b.disabled = true); settle(E.checkOrder(ex, cur.chosen.map(i => ex.bank[i]))); }
  }
  function next() { stopRec(); L.q.shift(); if (L.q.length) { render(); window.scrollTo(0, 0); } else finishLesson(); }
  function finishLesson() {
    const acc = L.total ? Math.min(1, L.firstOk / L.total) : 1, r = E.finish(S, L.id, acc, L.daily); save();
    R = { stars: r.stars, gain: r.gain, acc: Math.round(acc * 100), unitDone: L.m === 5, u: L.u, weak: !L.id, daily: !!L.daily }; view = "result"; render(); window.scrollTo(0, 0); sfx("win"); confetti();
  }
  function result() {
    app.innerHTML = '<div class="center"><canvas id="confetti"></canvas>' + moka(R.stars === 3 ? "wow" : "happy") + '<div class="bigstars">' + [1, 2, 3].map(i => I.star.replace("<svg", '<svg class="' + (i <= R.stars ? "on" : "") + '"')).join("") + '</div><div>' + (R.daily ? '<p class="sub">Repaso del día</p>' : "") + '<h1 class="it">' + (R.weak ? T.reviewDone : R.unitDone ? T.unitDone.replace("{n}", R.u) : T.lessonDone) + '</h1><p class="sub">' + (R.acc >= 90 ? "Casi sin fallos. Sigue así." : R.acc >= 70 ? "Buen trabajo. Lo fallado volverá en los próximos repasos." : "Lo fallado volverá en los próximos repasos hasta que salga solo.") + "</p></div>" +
      '<div class="tiles"><div class="tilebox"><b>+' + R.gain + '</b><small>XP</small></div><div class="tilebox"><b>' + R.acc + '%</b><small>a la primera</small></div><div class="tilebox"><b>' + gStreak() + '</b><small>días de racha</small></div></div><button class="btn" data-act="home" id="go">Continuar</button></div>';
  }
  function render() { cur = null; ({ home, me, lesson, result })[view](); }
  // Caminos ilustrados: se trazan por el centro de los nodos (que se desplazan en zigzag) una vez colocados.
  const ROADS = {
    stone: d => '<path d="' + d + '" stroke="#D2B98C" stroke-width="46" fill="none" stroke-linecap="round"/><path d="' + d + '" stroke="#EEDFC2" stroke-width="38" fill="none" stroke-linecap="round"/><path d="' + d + '" stroke="#D9C49C" stroke-width="30" fill="none" stroke-dasharray="1 11" stroke-linecap="round"/>',
    flight: d => '<path d="' + d + '" stroke="#fff" stroke-width="34" fill="none" stroke-linecap="round" opacity=".35"/><path d="' + d + '" stroke="#fff" stroke-width="5" fill="none" stroke-dasharray="2 12" stroke-linecap="round"/>',
    steps: d => '<path d="' + d + '" stroke="#7DB86C" stroke-width="34" fill="none" stroke-linecap="round" opacity=".45"/>',
    tiles: d => '<path d="' + d + '" stroke="#6B3E26" stroke-width="40" fill="none"/><path d="' + d + '" stroke="#2E2A28" stroke-width="34" fill="none"/><path d="' + d + '" stroke="#FFF8EC" stroke-width="34" fill="none" stroke-dasharray="17 17"/>',
    road: d => '<path d="' + d + '" stroke="#E9EEF2" stroke-width="48" fill="none" stroke-linecap="round"/><path d="' + d + '" stroke="#4A5566" stroke-width="40" fill="none" stroke-linecap="round"/><path d="' + d + '" stroke="#FFD34D" stroke-width="3.5" fill="none" stroke-dasharray="14 12"/>',
    rail: d => '<path d="' + d + '" stroke="#B9A38A" stroke-width="44" fill="none" opacity=".55"/><path d="' + d + '" stroke="#7A5B3F" stroke-width="34" fill="none" stroke-dasharray="6 9"/><path d="' + d + '" stroke="#6E7A8E" stroke-width="26" fill="none"/><path d="' + d + '" stroke="#B9A38A" stroke-width="20" fill="none"/><path d="' + d + '" stroke="#7A5B3F" stroke-width="20" fill="none" stroke-dasharray="6 9" opacity=".8"/>',
    plank: d => '<path d="' + d + '" stroke="#8A5A3B" stroke-width="42" fill="none"/><path d="' + d + '" stroke="#D9A86E" stroke-width="36" fill="none"/><path d="' + d + '" stroke="#B97A4E" stroke-width="36" fill="none" stroke-dasharray="2 13"/>',
    trail: d => '<path d="' + d + '" stroke="#C8A170" stroke-width="40" fill="none" stroke-linecap="round" opacity=".55"/><path d="' + d + '" stroke="#E2C79A" stroke-width="30" fill="none" stroke-linecap="round"/><path d="' + d + '" stroke="#C8A170" stroke-width="22" fill="none" stroke-dasharray="3 16" stroke-linecap="round"/>',
    carpet: d => '<path d="' + d + '" stroke="#C9A24A" stroke-width="42" fill="none"/><path d="' + d + '" stroke="#B03A4A" stroke-width="36" fill="none"/><path d="' + d + '" stroke="#C9A24A" stroke-width="26" fill="none" opacity=".35" stroke-dasharray="1 10" stroke-linecap="round"/>',
    paper: d => '<path d="' + d + '" stroke="#C9CFD6" stroke-width="42" fill="none"/><path d="' + d + '" stroke="#FFFDF6" stroke-width="38" fill="none"/><path d="' + d + '" stroke="#9EC3E6" stroke-width="38" fill="none" stroke-dasharray="1.2 9" opacity=".7"/><path d="' + d + '" stroke="#E2574C" stroke-width="1.5" fill="none" transform="translate(-12 0)" opacity=".6"/>',
    hall: d => '<path d="' + d + '" stroke="#9AA6B8" stroke-width="44" fill="none"/><path d="' + d + '" stroke="#E9EEF2" stroke-width="40" fill="none"/><path d="' + d + '" stroke="#CBD3DD" stroke-width="40" fill="none" stroke-dasharray="20 20"/>',
    water: d => '<path d="' + d + '" stroke="#7FC3E8" stroke-width="46" fill="none" stroke-linecap="round" opacity=".8"/><path d="' + d + '" stroke="#BFE4F7" stroke-width="4" fill="none" stroke-dasharray="10 18" stroke-linecap="round"/>',
    ink: d => '<path d="' + d + '" stroke="#26323A" stroke-width="40" fill="none" stroke-linecap="round" opacity=".12"/><path d="' + d + '" stroke="#26323A" stroke-width="3" fill="none" stroke-dasharray="1 0" opacity=".6"/><path d="' + d + '" stroke="#C9A24A" stroke-width="30" fill="none" stroke-dasharray="1 22" stroke-linecap="round" opacity=".7"/>'
  };
  function drawRoads() {
    const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
    document.querySelectorAll(".path.scn").forEach(p => {
      const r = p.getBoundingClientRect(), svg = p.querySelector("svg.road");
      if (!r.width) return;
      const sv = p.querySelector(".scene svg"); if (sv) sv.setAttribute("preserveAspectRatio", r.width / r.height > .62 ? "xMidYMid meet" : "xMidYMid slice");
      if (still) p.querySelectorAll(".scene svg").forEach(s => s.pauseAnimations && s.pauseAnimations());
      const pts = [...p.querySelectorAll(".node")].map(n => { const b = n.getBoundingClientRect(); return [b.left + b.width / 2 - r.left, b.top + 34 - r.top]; });
      if (!pts.length) return;
      pts.unshift([pts[0][0], -10]); pts.push([pts[pts.length - 1][0], r.height + 10]);
      let d = "M" + pts[0][0].toFixed(1) + " " + pts[0][1].toFixed(1);
      for (let i = 0; i < pts.length - 1; i++) {   // Catmull-Rom → Bézier
        const p0 = pts[Math.max(0, i - 1)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(pts.length - 1, i + 2)];
        const c1 = [p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6], c2 = [p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6];
        d += " C" + c1.map(v => v.toFixed(1)).join(" ") + " " + c2.map(v => v.toFixed(1)).join(" ") + " " + p2.map(v => v.toFixed(1)).join(" ");
      }
      svg.setAttribute("viewBox", "0 0 " + r.width + " " + r.height);
      const kind = p.dataset.road;
      svg.innerHTML = (ROADS[kind] || ROADS.stone)(d);
      if (kind === "steps") {   // piedras pasaderas a lo largo del camino
        const g = svg.querySelector("path"), L = g.getTotalLength();
        let stones = "";
        for (let t = 18, i = 0; t < L; t += 34, i++) { const q = g.getPointAtLength(t); stones += '<ellipse cx="' + (q.x + (i % 2 ? 5 : -5)).toFixed(1) + '" cy="' + q.y.toFixed(1) + '" rx="15" ry="9" fill="#F1EADB" stroke="#C9BCA2" stroke-width="2"/>'; }
        svg.insertAdjacentHTML("beforeend", stones);
      }
      if (kind === "flight") {   // un avioncito que recorre la ruta
        svg.insertAdjacentHTML("beforeend", '<g><path d="M-9 -3 L7 -3 Q12 0 7 3 L-9 3 Z M-2 -3 L-6 -10 L-2 -10 L4 -3 Z M-2 3 L-6 10 L-2 10 L4 3 Z" fill="#fff" stroke="#3F6FA8" stroke-width="1.2"/>' + (still ? "" : '<animateMotion dur="14s" repeatCount="indefinite" rotate="auto" path="' + d + '"/>') + "</g>");
      }
    });
  }
  let roadT; addEventListener("resize", () => { clearTimeout(roadT); roadT = setTimeout(drawRoads, 120); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => drawRoads());

  function goHome() { view = "home"; L = null; render(); const n = $(".node.now"); if (n) n.scrollIntoView({ block: "center" }); }

  // ---------- eventos ----------
  document.addEventListener("click", ev => {
    const t = ev.target.closest("button,[data-act]"); if (ev.target === veil) return hide(); if (!t) return;
    const d = t.dataset;
    if (d.say) return say(d.say, d.k);
    if (d.mod) { const p = d.mod.split("."); return modSheet(+p[0], +p[1]); }
    if (d.guide) return guideSheet(+d.guide);
    if (d.start) { const p = d.start.split("."); return start(+p[0], +p[1]); }
    if (d.pref === "speak" && P.speak && Date.now() < (P.micOff || 0)) { P.micOff = 0; LS.set(KP, P); return render(); }   // estaba en pausa: se reanuda
    if (d.pref) { P[d.pref] = !P[d.pref]; LS.set(KP, P); if (d.pref === "sfx" && P.sfx) sfx("ok"); return render(); }
    if (d.key) { const f = $("#answer"); if (f && !f.disabled) { f.value += d.key; f.focus(); $("#go").disabled = false; } return; }
    if (d.opt != null && cur && !cur.checked) { cur.sel = +d.opt; app.querySelectorAll("[data-opt]").forEach((b, i) => b.classList.toggle("sel", i === cur.sel)); const bl = $("#blank"); if (bl) bl.textContent = cur.ex.options[cur.sel]; $("#go").disabled = false; return; }
    if (d.tile != null && cur && !cur.checked) {
      const i = +d.tile, at = cur.chosen.indexOf(i); if (at >= 0) cur.chosen.splice(at, 1); else cur.chosen.push(i);
      $("#line").innerHTML = cur.chosen.map(j => '<button class="tile" data-tile="' + j + '">' + esc(cur.ex.bank[j]) + "</button>").join("");
      $("#bank").querySelectorAll(".tile").forEach((b, j) => b.classList.toggle("used", cur.chosen.includes(j))); $("#go").disabled = !cur.chosen.length; return;
    }
    if ((d.ml || d.mr) && cur && cur.ex.type === "match") {
      const side = d.ml ? "left" : "right"; app.querySelectorAll(d.ml ? "[data-ml]" : "[data-mr]").forEach(b => b.classList.remove("sel")); t.classList.add("sel"); cur[side] = t;
      if (d.ml) say(E.BY[d.ml].it, d.ml);
      if (cur.left && cur.right) {
        const a = cur.left, b = cur.right, ok = a.dataset.ml === b.dataset.mr; cur.left = cur.right = null; E.record(S, a.dataset.ml, ok);
        [a, b].forEach(x => { x.classList.remove("sel"); x.classList.add(ok ? "right" : "wrong"); });
        if (ok) { cur.pairs++; setTimeout(() => [a, b].forEach(x => x.classList.add("gone")), 250); if (cur.pairs === cur.ex.items.length) { cur.checked = true; L.n++; L.combo++; if (!cur.miss) L.firstOk++; verdict(true, pick(YES), ""); } else sfx("pair"); }
        else { cur.miss++; L.combo = 0; sfx("bad"); setTimeout(() => [a, b].forEach(x => x.classList.remove("wrong")), 500); }
      }
      return;
    }
    switch (d.act) {
      case "hide": return hide();
      case "home": hide(); return goHome();
      case "me": formErr = ""; view = "me"; render(); return window.scrollTo(0, 0);
      case "weak": return startWeak();
      case "daily": return startDaily();
      case "lang": return PF && PF.openPicker();
      case "mic": return listen();
      case "skipspeak": return skipSpeak(false);
      case "nomic": return skipSpeak(true);
      case "begin": L.intro = false; return render();
      case "check": return check();
      case "next": return next();
      case "testvoice": warned = false; if (CLIPS) say(E.BY["1.2.s0"].it, "1.2.s0"); else say(T.hello); return setTimeout(() => { if (view === "me") render(); }, 400);
      case "askquit": return show('<h2>¿Salir de la lección?</h2><p class="sub">Lo que ya has respondido cuenta para tus repasos, pero el módulo no quedará completado.</p><button class="btn" data-act="hide">Seguir aquí</button><button class="btn plain" data-act="quit">Salir</button>');
      case "quit": stopRec(); save(); hide(); return goHome();
      case "askreset": return show('<h2>¿Borrar todo tu progreso?</h2><p class="sub">Se eliminan los puntos, la racha y los módulos completados' + (Cloud.write ? ", también en tu cuenta" : "") + '. No se puede deshacer.</p><button class="btn warn" data-act="reset">Borrar</button><button class="btn plain" data-act="hide">Cancelar</button>');
      case "reset": S = E.blank(); S.t = Date.now(); LS.set(KS, S); if (Cloud.write) Promise.resolve(Cloud.write(JSON.parse(JSON.stringify(S)))).catch(() => { }); hide(); return render();
      case "google": return google();
      case "signup": return emailAuth(true);
      case "signout": return signOut();
      case "resetpass": return resetPass();
      case "askdelete": return askDelete();
      case "delacct": return deleteAccount();
    }
  });
  document.addEventListener("change", ev => { if (ev.target.id === "voice") { P.voice = ev.target.value; LS.set(KP, P); loadVoices(); say("Ciao! Questa è la mia voce."); render(); } });
  document.addEventListener("submit", ev => { ev.preventDefault(); if (ev.target.id === "mailform") emailAuth(false); });
  document.addEventListener("keydown", ev => {
    if (!veil.hidden) { if (ev.key === "Escape") hide(); return; }
    if (view !== "lesson" && view !== "result") return;
    const typing = ev.target && ev.target.id === "answer";
    if (ev.key === "Enter") { const b = $("#go") || $('[data-act="begin"]'); if (b && !b.disabled) { ev.preventDefault(); b.click(); } }
    else if (!typing && /^[1-9]$/.test(ev.key)) { const b = app.querySelector('[data-opt="' + (ev.key - 1) + '"]'); if (b && !b.disabled) b.click(); }
  });

  window.SaimapLingo = { get state() { return S; }, get lesson() { return L; }, get current() { return cur; }, cloud: Cloud, voices: () => voices.map(v => v.name) };
  render(); initCloud();
})();
