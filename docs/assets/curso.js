/* Funciones interactivas del curso: progreso, mapa de la ruta, autoevaluaciones y listas tildables.
   El progreso se guarda solo en el navegador (localStorage); no se envía a ningún servidor.
   Código bajo licencia MIT (ver LICENSE-CODE). */
(function () {
  "use strict";

  var CLAVE = "cursoIA.progreso.v1";
  var ESTADOS = [
    { id: "por-hacer", nombre: "Por hacer" },
    { id: "en-curso", nombre: "En curso" },
    { id: "completada", nombre: "Completada" }
  ];
  var datosPromesa = null;

  // ── Almacenamiento ─────────────────────────────────────────────────────────
  function leer() {
    try {
      var v = JSON.parse(localStorage.getItem(CLAVE) || "{}");
      if (!v || typeof v !== "object") v = {};
      v.lecciones = v.lecciones || {};
      return v;
    } catch (e) { return { lecciones: {} }; }
  }
  function guardar(v) {
    try { localStorage.setItem(CLAVE, JSON.stringify(v)); return true; } catch (e) { return false; }
  }
  function estadoDe(id) {
    var l = leer().lecciones[id];
    return (l && l.estado) || "por-hacer";
  }
  function fijarEstado(id, estado) {
    var v = leer();
    if (estado === "por-hacer") delete v.lecciones[id];
    else v.lecciones[id] = { estado: estado, fecha: new Date().toISOString().slice(0, 10) };
    guardar(v);
    document.dispatchEvent(new CustomEvent("cu:progreso"));
  }

  // ── Utilidades ─────────────────────────────────────────────────────────────
  function base() {
    try {
      var cfg = JSON.parse(document.getElementById("__config").textContent);
      return new URL(cfg.base.replace(/\/?$/, "/"), location.href);
    } catch (e) { return new URL("./", location.href); }
  }
  function urlSitio(rel) { return new URL(rel || "", base()).href; }
  function cargarDatos() {
    if (!datosPromesa) {
      datosPromesa = fetch(urlSitio("assets/datos/curso.json")).then(function (r) {
        if (!r.ok) throw new Error("No se pudieron cargar los datos del curso");
        return r.json();
      });
    }
    return datosPromesa;
  }
  function el(tag, attrs, hijos) {
    var e = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "texto") e.textContent = attrs[k];
      else if (k === "clase") e.className = attrs[k];
      else e.setAttribute(k, attrs[k]);
    });
    (hijos || []).forEach(function (h) { if (h) e.appendChild(typeof h === "string" ? document.createTextNode(h) : h); });
    return e;
  }
  function nombreEstado(id) {
    for (var i = 0; i < ESTADOS.length; i++) if (ESTADOS[i].id === id) return ESTADOS[i].nombre;
    return id;
  }
  function chip(estado) {
    return el("span", { clase: "cu-chip cu-chip--" + estado, texto: nombreEstado(estado) });
  }
  function barra(hechas, total, etiqueta) {
    var pct = total ? Math.round((hechas / total) * 100) : 0;
    var b = el("div", { clase: "cu-barra", role: "progressbar", "aria-valuemin": "0", "aria-valuemax": String(total),
                        "aria-valuenow": String(hechas), "aria-label": etiqueta || "Avance" });
    var r = el("span", { clase: "cu-barra-relleno" });
    r.style.width = pct + "%";
    b.appendChild(r);
    return b;
  }
  function resumen(lecciones) {
    var c = 0, e = 0;
    lecciones.forEach(function (l) {
      var s = estadoDe(l.id);
      if (s === "completada") c++; else if (s === "en-curso") e++;
    });
    return { completadas: c, enCurso: e, total: lecciones.length };
  }
  function selector(id, alCambiar) {
    var grupo = el("div", { clase: "cu-selector", role: "radiogroup", "aria-label": "Estado de la lección " + id });
    function pintar() {
      var actual = estadoDe(id);
      Array.prototype.forEach.call(grupo.children, function (b) {
        b.setAttribute("aria-checked", String(b.dataset.estado === actual));
      });
    }
    ESTADOS.forEach(function (s) {
      var b = el("button", { type: "button", role: "radio", clase: "cu-selector-op cu-selector-op--" + s.id, texto: s.nombre });
      b.dataset.estado = s.id;
      b.addEventListener("click", function () { fijarEstado(id, s.id); pintar(); if (alCambiar) alCambiar(s.id); });
      grupo.appendChild(b);
    });
    pintar();
    document.addEventListener("cu:progreso", pintar);
    return grupo;
  }

  // ── Lección ────────────────────────────────────────────────────────────────
  function iniciarLeccion(marca) {
    var id = marca.dataset.id;
    var v = leer();
    v.ultima = { id: id, url: location.href.split("#")[0] };
    if (!v.lecciones[id]) v.lecciones[id] = { estado: "en-curso", fecha: new Date().toISOString().slice(0, 10) };
    guardar(v);

    var h1 = document.querySelector(".md-content h1");
    if (h1 && !h1.parentNode.querySelector(".cu-estado-titulo")) {
      var c = el("div", { clase: "cu-estado-titulo" }, [chip(estadoDe(id))]);
      h1.insertAdjacentElement("afterend", c);
      document.addEventListener("cu:progreso", function () { c.replaceChildren(chip(estadoDe(id))); });
    }
    var tarjeta = el("section", { clase: "cu-tarjeta cu-leccion-cierre", "aria-label": "Tu avance en esta lección" }, [
      el("h2", { clase: "cu-tarjeta-titulo", texto: "¿Cómo vas con esta lección?" }),
      el("p", { clase: "cu-nota", texto: "Marcala como completada cuando hayas superado la autoevaluación o hecho la práctica. Se guarda en este navegador." }),
      selector(id),
      el("p", { clase: "cu-nota" }, [el("a", { href: urlSitio("progreso/"), texto: "Ver todo mi progreso" })])
    ]);
    marca.replaceWith(tarjeta);
    arreglarEnlaceProgreso(tarjeta);
  }

  // En la vista previa con URLs de archivo, "progreso/" es "progreso.html".
  function arreglarEnlaceProgreso(raiz) {
    if (!/\.html$/.test(location.pathname)) return;
    raiz.querySelectorAll('a[href$="progreso/"]').forEach(function (a) { a.href = urlSitio("progreso.html"); });
  }

  // ── Portada de módulo ──────────────────────────────────────────────────────
  function iniciarModulo(marca) {
    var mod = marca.dataset.modulo;
    cargarDatos().then(function (d) {
      var lecs = d.lecciones.filter(function (l) { return l.modulo === mod; });
      var caja = el("div", { clase: "cu-modulo-avance" });
      function pintar() {
        var r = resumen(lecs);
        caja.replaceChildren(
          barra(r.completadas, r.total, "Avance del módulo"),
          el("span", { clase: "cu-nota", texto: r.completadas + " de " + r.total + " lecciones completadas" + (r.enCurso ? " · " + r.enCurso + " en curso" : "") })
        );
        document.querySelectorAll(".md-content table td:first-child").forEach(function (td) {
          var id = (td.dataset.id || td.textContent).trim();
          if (!/^L\d+\.\d+\.\d+$/.test(id)) return;
          td.dataset.id = id;
          var s = estadoDe(id);
          td.replaceChildren(document.createTextNode(id));
          if (s !== "por-hacer") td.appendChild(chip(s));
        });
      }
      pintar();
      document.addEventListener("cu:progreso", pintar);
      marca.replaceWith(caja);
    }).catch(function () { marca.remove(); });
  }

  // ── Mi progreso ────────────────────────────────────────────────────────────
  function iniciarProgreso(raiz) {
    cargarDatos().then(function (d) {
      function pintar() {
        raiz.replaceChildren();
        var total = resumen(d.lecciones);
        var v = leer();
        var cabecera = el("section", { clase: "cu-tarjeta cu-progreso-total" }, [
          el("div", { clase: "cu-cifra" }, [
            el("span", { clase: "cu-cifra-num", texto: String(total.completadas) }),
            el("span", { clase: "cu-cifra-de", texto: " de " + total.total + " lecciones completadas" })
          ]),
          barra(total.completadas, total.total, "Avance del curso"),
          el("p", { clase: "cu-nota", texto: total.enCurso + " en curso · " + (total.total - total.completadas - total.enCurso) + " por hacer" })
        ]);
        var esenciales = d.lecciones.filter(function (l) { return l.ruta !== "Profundizar"; });
        var res = resumen(esenciales);
        cabecera.appendChild(el("div", { clase: "cu-ruta-esencial" }, [
          el("span", { texto: "Ruta esencial: " + res.completadas + " de " + res.total + " lecciones" }),
          barra(res.completadas, res.total, "Avance de la ruta esencial")
        ]));
        var filtro = el("label", { clase: "cu-filtro" }, [
          el("input", { type: "checkbox", id: "cu-solo-esenciales" }), " Mostrar solo la ruta esencial"
        ]);
        var soloEsenciales = false;
        try { soloEsenciales = localStorage.getItem("cursoIA.soloEsenciales") === "1"; } catch (e) {}
        filtro.firstChild.checked = soloEsenciales;
        filtro.firstChild.addEventListener("change", function () {
          try { localStorage.setItem("cursoIA.soloEsenciales", this.checked ? "1" : "0"); } catch (e) {}
          raiz.classList.toggle("cu-solo-esenciales", this.checked);
        });
        raiz.classList.toggle("cu-solo-esenciales", soloEsenciales);
        cabecera.appendChild(filtro);
        if (v.ultima && v.ultima.url) {
          var ult = d.lecciones.filter(function (l) { return l.id === v.ultima.id; })[0];
          cabecera.appendChild(el("p", {}, [
            el("strong", { texto: "Seguir donde quedaste: " }),
            el("a", { href: v.ultima.url, texto: ult ? ult.titulo : v.ultima.id })
          ]));
        }
        raiz.appendChild(cabecera);

        d.etapas.forEach(function (et) {
          var mods = d.modulos.filter(function (m) { return m.etapa === et.n; });
          var lecsEtapa = d.lecciones.filter(function (l) { return mods.some(function (m) { return m.id === l.modulo; }); });
          var re = resumen(lecsEtapa);
          var sec = el("section", { clase: "cu-etapa" }, [
            el("h2", { texto: "Etapa " + et.n + " · " + et.titulo }),
            el("div", { clase: "cu-fila-avance" }, [barra(re.completadas, re.total, "Avance de la etapa " + et.n),
              el("span", { clase: "cu-nota", texto: re.completadas + "/" + re.total })])
          ]);
          mods.forEach(function (m) {
            var lecs = d.lecciones.filter(function (l) { return l.modulo === m.id; });
            var rm = resumen(lecs);
            var det = el("details", { clase: "cu-mod" });
            var sum = el("summary", {}, [
              el("span", { clase: "cu-mod-nombre", texto: "Módulo " + m.n + " · " + m.titulo }),
              el("span", { clase: "cu-mod-cuenta", texto: rm.completadas + "/" + rm.total }),
              barra(rm.completadas, rm.total, "Avance del módulo " + m.n)
            ]);
            det.appendChild(sum);
            var lista = el("ul", { clase: "cu-lista" });
            lecs.forEach(function (l) {
              var nombre = l.url ? el("a", { href: urlSitio(l.url), texto: l.titulo }) : el("span", { texto: l.titulo });
              lista.appendChild(el("li", { clase: l.ruta === "Profundizar" ? "cu-profundizar" : "" }, [
                el("span", { clase: "cu-lista-id", texto: l.id }), nombre,
                l.ruta === "Profundizar" ? el("span", { clase: "cu-etiqueta", texto: "Profundizar" }) : null,
                l.url ? null : el("span", { clase: "cu-nota", texto: " (próximamente)" }),
                selector(l.id)
              ]));
            });
            det.appendChild(lista);
            det.appendChild(el("p", {}, [el("a", { href: urlSitio(m.url), texto: "Ir al módulo" })]));
            sec.appendChild(det);
          });
          raiz.appendChild(sec);
        });
        raiz.appendChild(herramientas());
      }
      pintar();
      document.addEventListener("cu:progreso", function () {
        // Actualiza contadores sin perder los <details> abiertos.
        var abiertos = Array.prototype.map.call(raiz.querySelectorAll("details[open] .cu-mod-nombre"), function (s) { return s.textContent; });
        pintar();
        raiz.querySelectorAll("details .cu-mod-nombre").forEach(function (s) {
          if (abiertos.indexOf(s.textContent) >= 0) s.closest("details").open = true;
        });
      });
    }).catch(function () {
      raiz.replaceChildren(el("p", { texto: "No se pudieron cargar los datos del curso. Probá recargar la página." }));
    });
  }

  function herramientas() {
    var msg = el("p", { clase: "cu-nota", role: "status" });
    var bajar = el("button", { type: "button", clase: "md-button", texto: "Descargar copia" });
    bajar.addEventListener("click", function () {
      try {
        var blob = new Blob([JSON.stringify(leer(), null, 2)], { type: "application/json" });
        var a = el("a", { href: URL.createObjectURL(blob), download: "progreso-curso-ia.json" });
        document.body.appendChild(a); a.click(); a.remove();
        msg.textContent = "Copia descargada.";
      } catch (e) { msg.textContent = "Este navegador no permitió descargar el archivo."; }
    });
    var archivo = el("input", { type: "file", accept: "application/json,.json", id: "cu-importar", clase: "cu-oculto" });
    var subir = el("label", { for: "cu-importar", clase: "md-button", texto: "Cargar copia" });
    archivo.addEventListener("change", function () {
      var f = archivo.files && archivo.files[0];
      if (!f) return;
      f.text().then(function (t) {
        var v = JSON.parse(t);
        if (!v || typeof v.lecciones !== "object") throw new Error();
        guardar(v);
        msg.textContent = "Progreso cargado.";
        document.dispatchEvent(new CustomEvent("cu:progreso"));
      }).catch(function () { msg.textContent = "El archivo no es una copia de progreso válida."; });
    });
    var borrar = el("button", { type: "button", clase: "md-button cu-peligro", texto: "Borrar mi progreso" });
    var confirmar = el("span", { clase: "cu-confirmar", hidden: "" }, [
      el("span", { texto: "¿Seguro? No se puede deshacer. " }),
      el("button", { type: "button", clase: "md-button cu-peligro", texto: "Sí, borrar" }),
      el("button", { type: "button", clase: "md-button", texto: "Cancelar" })
    ]);
    borrar.addEventListener("click", function () { confirmar.hidden = false; borrar.hidden = true; });
    confirmar.children[1].addEventListener("click", function () {
      guardar({ lecciones: {} }); confirmar.hidden = true; borrar.hidden = false;
      msg.textContent = "Progreso borrado.";
      document.dispatchEvent(new CustomEvent("cu:progreso"));
    });
    confirmar.children[2].addEventListener("click", function () { confirmar.hidden = true; borrar.hidden = false; });
    return el("section", { clase: "cu-tarjeta cu-herramientas" }, [
      el("h2", { clase: "cu-tarjeta-titulo", texto: "Copia de seguridad" }),
      el("p", { clase: "cu-nota", texto: "Tu progreso vive en este navegador. Descargá una copia para no perderlo o para pasarlo a otra computadora." }),
      el("div", { clase: "cu-botones" }, [bajar, subir, archivo, borrar, confirmar]),
      msg
    ]);
  }

  // ── Mapa de la ruta ────────────────────────────────────────────────────────
  var SVG = "http://www.w3.org/2000/svg";
  function s(tag, attrs) {
    var e = document.createElementNS(SVG, tag);
    Object.keys(attrs || {}).forEach(function (k) { e.setAttribute(k, attrs[k]); });
    return e;
  }

  function iniciarMapa(raiz) {
    cargarDatos().then(function (d) {
      function pintar() {
        raiz.replaceChildren();
        var ancho = raiz.clientWidth || 800;
        if (ancho < 720) return pintarLista(raiz, d);
        var cols = d.etapas.length, gapX = 26, colW = (ancho - gapX * (cols - 1)) / cols;
        var nodoH = 64, gapY = 14, cabH = 46;
        var maxFilas = Math.max.apply(null, d.etapas.map(function (et) {
          return d.modulos.filter(function (m) { return m.etapa === et.n; }).length;
        }));
        var alto = cabH + maxFilas * (nodoH + gapY);
        var svg = s("svg", { viewBox: "0 0 " + ancho + " " + alto, width: "100%", class: "cu-mapa-svg", role: "img",
                             "aria-label": "Mapa de módulos del curso con sus prerrequisitos" });
        var pos = {}, recortar = [];
        d.etapas.forEach(function (et, i) {
          var x = i * (colW + gapX);
          var t = s("text", { x: x, y: 16, class: "cu-mapa-etapa" });
          t.textContent = "Etapa " + et.n;
          svg.appendChild(t);
          var t2 = s("text", { x: x, y: 34, class: "cu-mapa-etapa-nombre" });
          t2.textContent = et.titulo;
          svg.appendChild(t2);
          recortar.push([t2, colW - 4]);
          d.modulos.filter(function (m) { return m.etapa === et.n; }).forEach(function (m, j) {
            pos[m.id] = { x: x, y: cabH + j * (nodoH + gapY), w: colW, h: nodoH };
          });
        });
        var aristas = s("g", { class: "cu-mapa-aristas" });
        svg.appendChild(aristas);
        function arista(desde, hasta, tipo) {
          var a = pos[desde], b = pos[hasta];
          if (!a || !b) return;
          var x1, y1, x2, y2, dpath;
          if (a.x === b.x) { // misma columna: conexión por el costado izquierdo
            x1 = a.x; y1 = a.y + a.h / 2; x2 = b.x; y2 = b.y + b.h / 2;
            dpath = "M" + x1 + "," + y1 + " C" + (x1 - 16) + "," + y1 + " " + (x2 - 16) + "," + y2 + " " + x2 + "," + y2;
          } else {
            x1 = a.x + a.w; y1 = a.y + a.h / 2; x2 = b.x; y2 = b.y + b.h / 2;
            var mx = (x1 + x2) / 2;
            dpath = "M" + x1 + "," + y1 + " C" + mx + "," + y1 + " " + mx + "," + y2 + " " + x2 + "," + y2;
          }
          var p = s("path", { d: dpath, class: "cu-arista cu-arista--" + tipo, "data-desde": desde, "data-hasta": hasta });
          aristas.appendChild(p);
        }
        d.modulos.forEach(function (m) {
          m.requiere.forEach(function (r) { arista(r, m.id, "requiere"); });
          m.recomienda.forEach(function (r) { arista(r, m.id, "recomienda"); });
        });
        var tip = el("div", { clase: "cu-mapa-tip", hidden: "" });
        d.modulos.forEach(function (m) {
          var p = pos[m.id];
          var lecs = d.lecciones.filter(function (l) { return l.modulo === m.id; });
          var r = resumen(lecs);
          var estado = r.completadas === r.total ? "completo" : (r.completadas || r.enCurso) ? "en-curso" : "nuevo";
          var a = s("a", { href: urlSitio(m.url), class: "cu-nodo cu-nodo--" + estado, "data-id": m.id, tabindex: "0" });
          a.appendChild(s("rect", { x: p.x, y: p.y, width: p.w, height: p.h, rx: 10 }));
          var t = s("text", { x: p.x + 12, y: p.y + 22, class: "cu-nodo-num" });
          t.textContent = "Módulo " + m.n + (m.nivel === "N1" ? " · Nivel 1" : m.nivel === "N2" ? " · Nivel 2" : "");
          a.appendChild(t);
          var t2 = s("text", { x: p.x + 12, y: p.y + 42, class: "cu-nodo-titulo" });
          t2.textContent = m.titulo;
          a.appendChild(t2);
          // Barra de avance dentro del nodo.
          var bw = p.w - 24;
          a.appendChild(s("rect", { x: p.x + 12, y: p.y + p.h - 12, width: bw, height: 4, rx: 2, class: "cu-nodo-barra" }));
          a.appendChild(s("rect", { x: p.x + 12, y: p.y + p.h - 12, width: Math.max(0, bw * (r.completadas / r.total)), height: 4, rx: 2, class: "cu-nodo-relleno" }));
          svg.appendChild(a);
          recortar.push([t2, p.w - 24]);
          function mostrar() {
            svg.classList.add("cu-mapa--foco");
            svg.querySelectorAll(".cu-nodo").forEach(function (n) {
              var id = n.getAttribute("data-id");
              var rel = id === m.id || m.requiere.indexOf(id) >= 0 || m.recomienda.indexOf(id) >= 0;
              n.classList.toggle("cu-activo", rel);
            });
            svg.querySelectorAll(".cu-arista").forEach(function (e) {
              e.classList.toggle("cu-activo", e.getAttribute("data-hasta") === m.id);
            });
            tip.replaceChildren(
              el("strong", { texto: "Módulo " + m.n + " · " + m.titulo }),
              el("span", { texto: m.horas + " h · " + r.completadas + " de " + r.total + " lecciones completadas" }),
              el("span", { texto: m.requiere.length ? "Necesitás: " + m.requiere.map(nombreMod).join(", ") : "No necesita módulos previos" }),
              m.recomienda.length ? el("span", { texto: "Conviene: " + m.recomienda.map(nombreMod).join(", ") }) : null
            );
            tip.hidden = false;
            var rect = raiz.getBoundingClientRect(), escala = rect.width / ancho;
            var x = (p.x + p.w) * escala + 8, y = p.y * escala;
            if (x + 260 > rect.width) x = Math.max(0, p.x * escala - 268);
            tip.style.left = x + "px"; tip.style.top = y + "px";
          }
          function ocultar() {
            svg.classList.remove("cu-mapa--foco");
            svg.querySelectorAll(".cu-activo").forEach(function (n) { n.classList.remove("cu-activo"); });
            tip.hidden = true;
          }
          a.addEventListener("mouseenter", mostrar);
          a.addEventListener("focus", mostrar);
          a.addEventListener("mouseleave", ocultar);
          a.addEventListener("blur", ocultar);
        });
        function nombreMod(id) {
          var mm = d.modulos.filter(function (x) { return x.id === id; })[0];
          return mm ? "Módulo " + mm.n : id;
        }
        raiz.appendChild(svg);
        // Recorta los textos que no entran en su caja (hay que medirlos ya insertados).
        var escalaSvg = (svg.getBoundingClientRect().width || ancho) / ancho;
        recortar.forEach(function (r) {
          var txt = r[0], max = r[1], completo = txt.textContent;
          if (txt.getComputedTextLength() <= max) return;
          var ti = s("title", {}); ti.textContent = completo; txt.appendChild(ti);
          var corto = completo;
          while (corto.length > 4 && txt.getComputedTextLength() > max) {
            corto = corto.slice(0, -1);
            txt.firstChild.nodeValue = corto.replace(/[\s·,:]+$/, "") + "…";
          }
        });
        void escalaSvg;
        raiz.appendChild(tip);
        raiz.appendChild(el("div", { clase: "cu-mapa-leyenda" }, [
          el("span", {}, [el("i", { clase: "cu-ley cu-ley--requiere" }), "Prerrequisito indispensable"]),
          el("span", {}, [el("i", { clase: "cu-ley cu-ley--recomienda" }), "Recomendado"]),
          el("span", {}, [el("i", { clase: "cu-ley-nodo cu-nodo--en-curso" }), "En curso"]),
          el("span", {}, [el("i", { clase: "cu-ley-nodo cu-nodo--completo" }), "Completado"])
        ]));
      }
      pintar();
      var t;
      window.addEventListener("resize", function () { clearTimeout(t); t = setTimeout(pintar, 150); });
      document.addEventListener("cu:progreso", pintar);
    }).catch(function () {
      raiz.replaceChildren(el("p", { texto: "No se pudo cargar el mapa. La lista de etapas está abajo." }));
    });
  }

  function pintarLista(raiz, d) {
    d.etapas.forEach(function (et) {
      var sec = el("section", { clase: "cu-mapa-lista" }, [el("h3", { texto: "Etapa " + et.n + " · " + et.titulo })]);
      d.modulos.filter(function (m) { return m.etapa === et.n; }).forEach(function (m) {
        var r = resumen(d.lecciones.filter(function (l) { return l.modulo === m.id; }));
        sec.appendChild(el("a", { href: urlSitio(m.url), clase: "cu-mapa-item" }, [
          el("strong", { texto: "Módulo " + m.n + " · " + m.titulo }),
          el("span", { clase: "cu-nota", texto: m.requiere.length ? "Necesitás: " + m.requiere.map(function (x) { return "Módulo " + x.slice(1); }).join(", ") : "Sin prerrequisitos" }),
          barra(r.completadas, r.total, "Avance del módulo " + m.n)
        ]));
      });
      raiz.appendChild(sec);
    });
  }

  // ── Autoevaluaciones ───────────────────────────────────────────────────────
  function iniciarQuizzes() {
    var quizzes = document.querySelectorAll(".cu-quiz");
    if (!quizzes.length) return;
    var clavePagina = "cursoIA.quiz." + location.pathname;
    var guardadas = {};
    try { guardadas = JSON.parse(localStorage.getItem(clavePagina) || "{}"); } catch (e) { guardadas = {}; }
    var res = null;
    function actualizarResumen() {
      if (!res) return;
      var resp = 0, ok = 0;
      quizzes.forEach(function (q) { if (q.dataset.respondida) { resp++; if (q.dataset.correcta === "1") ok++; } });
      if (!resp) { res.hidden = true; return; }
      res.hidden = false;
      var pct = Math.round(ok / quizzes.length * 100);
      var txt = "Respondiste " + resp + " de " + quizzes.length + " · " + ok + " correctas";
      if (resp === quizzes.length) txt += pct >= 80 ? " (" + pct + "%: ¡superada!)" : " (" + pct + "%: repasá y volvé a intentar)";
      res.querySelector(".cu-quiz-resumen-texto").textContent = txt;
      var marca = document.querySelector(".cu-leccion-cierre");
      res.querySelector(".cu-quiz-aprobar").hidden = !(resp === quizzes.length && pct >= 80 && marca);
    }
    quizzes.forEach(function (q, i) {
      var opciones = q.querySelectorAll(".cu-quiz-opcion");
      var expl = q.querySelector(".cu-quiz-explicacion");
      q.insertBefore(el("span", { clase: "cu-quiz-num", texto: "Pregunta " + (i + 1) + " de " + quizzes.length }), q.firstChild);
      function responder(btn, guardar_) {
        opciones.forEach(function (o) {
          o.disabled = true;
          if (o.dataset.ok === "1") o.classList.add("cu-ok");
        });
        var bien = btn.dataset.ok === "1";
        if (!bien) btn.classList.add("cu-mal");
        btn.classList.add("cu-elegida");
        q.dataset.respondida = "1";
        q.dataset.correcta = bien ? "1" : "0";
        expl.hidden = false;
        expl.insertBefore(el("strong", { texto: bien ? "¡Correcto! " : "No es esa. " }), expl.firstChild);
        if (guardar_) {
          guardadas[i] = Array.prototype.indexOf.call(opciones, btn);
          try { localStorage.setItem(clavePagina, JSON.stringify(guardadas)); } catch (e) {}
        }
        actualizarResumen();
      }
      opciones.forEach(function (o) { o.addEventListener("click", function () { responder(o, true); }); });
      if (guardadas[i] != null && opciones[guardadas[i]]) responder(opciones[guardadas[i]], false);
    });
    var ultimo = quizzes[quizzes.length - 1];
    var reiniciar = el("button", { type: "button", clase: "md-button", texto: "Volver a intentar" });
    reiniciar.addEventListener("click", function () {
      try { localStorage.removeItem(clavePagina); } catch (e) {}
      location.reload();
    });
    var aprobar = el("button", { type: "button", clase: "md-button md-button--primary cu-quiz-aprobar", texto: "Marcar la lección como completada", hidden: "" });
    aprobar.addEventListener("click", function () {
      var m = document.querySelector(".cu-leccion-cierre .cu-selector");
      var id = m && m.getAttribute("aria-label").replace("Estado de la lección ", "");
      if (id) fijarEstado(id, "completada");
      aprobar.hidden = true;
    });
    res = el("div", { clase: "cu-tarjeta cu-quiz-resumen", hidden: "" }, [
      el("p", { clase: "cu-quiz-resumen-texto" }), el("div", { clase: "cu-botones" }, [aprobar, reiniciar])
    ]);
    ultimo.insertAdjacentElement("afterend", res);
    actualizarResumen();
  }

  // ── Listas tildables ───────────────────────────────────────────────────────
  function iniciarListas() {
    var cajas = document.querySelectorAll(".md-content .task-list-control input[type=checkbox]");
    if (!cajas.length) return;
    var clave = "cursoIA.lista." + location.pathname;
    var estado = {};
    try { estado = JSON.parse(localStorage.getItem(clave) || "{}"); } catch (e) { estado = {}; }
    cajas.forEach(function (c, i) {
      c.disabled = false;
      if (estado[i] != null) c.checked = !!estado[i];
      c.addEventListener("change", function () {
        estado[i] = c.checked ? 1 : 0;
        try { localStorage.setItem(clave, JSON.stringify(estado)); } catch (e) {}
      });
    });
  }

  // ── Tablas de lecciones: más espacio para el título y etiquetas compactas ──
  function iniciarTablasLecciones() {
    document.querySelectorAll(".md-content table").forEach(function (tabla) {
      var ths = Array.prototype.map.call(tabla.querySelectorAll("thead th"), function (th) { return th.textContent.trim(); });
      if (ths[0] !== "ID" || ths[1] !== "Lección") return;
      (tabla.closest(".md-typeset__table") || tabla.parentElement).classList.add("cu-tabla-lecciones");
      var iRuta = ths.indexOf("Ruta"), iMat = ths.indexOf("Material");
      tabla.querySelectorAll("tbody tr").forEach(function (tr) {
        var celdas = tr.children;
        if (iRuta >= 0 && celdas[iRuta]) {
          var v = celdas[iRuta].textContent.trim();
          celdas[iRuta].replaceChildren(el("span", { clase: "cu-etiqueta" + (v === "Esencial" ? " cu-etiqueta--esencial" : ""), texto: v }));
        }
        if (iMat >= 0 && celdas[iMat] && celdas[iMat].textContent.trim() === "Próximamente") celdas[iMat].classList.add("cu-tenue");
      });
    });
  }

  // ── Arranque ───────────────────────────────────────────────────────────────
  function iniciar() {
    iniciarTablasLecciones();
    var l = document.querySelector(".cu-leccion");
    if (l) iniciarLeccion(l);
    var m = document.querySelector(".cu-modulo");
    if (m) iniciarModulo(m);
    var p = document.getElementById("cu-progreso");
    if (p) iniciarProgreso(p);
    var mapa = document.getElementById("cu-mapa");
    if (mapa) iniciarMapa(mapa);
    iniciarQuizzes();
    iniciarListas();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar);
  else iniciar();
})();
