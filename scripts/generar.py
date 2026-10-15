#!/usr/bin/env python3
"""Genera las partes derivadas del curso a partir de sus fuentes.

Fuentes de verdad:
- docs/mNN-*/index.md   Portada de cada módulo: datos del módulo, unidades y lecciones del programa.
- docs/mNN-*/l*.md      Lecciones con material: su front matter define el estado editorial.

Partes generadas (no se editan a mano):
- En cada portada de módulo: el enlace y la columna "Material" de la tabla de lecciones.
- docs/ruta/lecciones.md: índice completo de lecciones.
- mkdocs.yml: el bloque "nav" (menú del sitio).
- README.md y docs/index.md: la tabla de módulos, entre <!-- modulos:inicio --> y <!-- modulos:fin -->.

Además, `datos()` devuelve la estructura del curso que el hook hooks/curso.py publica como
assets/datos/curso.json para las funciones interactivas del sitio.

Uso:
    python scripts/generar.py              # regenera los archivos
    python scripts/generar.py --comprobar  # solo comprueba que estén al día (lo usa verificar.py)

Solo usa la biblioteca estándar de Python (3.9 o superior). Código bajo licencia MIT (ver LICENSE-CODE).
"""
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
ETAPAS = {
    "I": (1, "Fundamentos y uso profesional"),
    "II": (2, "Construir con modelos"),
    "III": (3, "Agentes e interoperabilidad"),
    "IV": (4, "Automatización y sistemas avanzados"),
    "V": (5, "Producción e integración"),
}
TIPOS = {"Conceptual": "C", "Práctica": "P", "Mixta": "M"}
TIPOS_INV = {v: k for k, v in TIPOS.items()}
ESTADOS = {"borrador": "📝 Borrador", "revisada": "🔍 Revisada", "publicada": "📗 Publicada"}
SIN_MATERIAL = "Próximamente"
MARCA_NAV = "# ── Menú del sitio: generado por scripts/generar.py, no editar a mano ──"
INDICE = DOCS / "ruta" / "lecciones.md"


def front_matter(texto: str) -> dict[str, str]:
    """Lee las claves de primer nivel de un front matter YAML simple."""
    if not texto.startswith("---\n"):
        return {}
    fin = texto.find("\n---\n", 4)
    if fin == -1:
        return {}
    datos = {}
    for linea in texto[4:fin].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*?)\s*(#.*)?$", linea)
        if m:
            datos[m.group(1)] = m.group(2).strip().strip('"')
    return datos


def etapa_nombre(bloque: str) -> str:
    n, nombre = ETAPAS[bloque]
    return f"Etapa {n} · {nombre}"


@dataclass
class Leccion:
    id: str
    tipo: str              # C, P o M
    titulo: str            # título corto
    descripcion: str       # detalle del programa
    unidad: str
    ruta: str = "Esencial"   # Esencial o Profundizar
    archivo: Path | None = None
    estado: str = ""

    @property
    def modulo(self) -> str:
        return "M" + self.id[1:].split(".")[0]


@dataclass
class Modulo:
    n: int
    carpeta: Path
    titulo: str
    bloque: str
    nivel: str
    horas_teoria: int
    horas_practica: int
    prerrequisitos: str
    unidades: list[tuple[str, str]] = field(default_factory=list)
    lecciones: list[Leccion] = field(default_factory=list)
    soluciones: list[Path] = field(default_factory=list)

    @property
    def id(self) -> str:
        return f"M{self.n}"

    @property
    def nombre(self) -> str:
        return f"Módulo {self.n} · {self.titulo}"

    @property
    def horas(self) -> int:
        return self.horas_teoria + self.horas_practica

    @property
    def con_material(self) -> list[Leccion]:
        return [l for l in self.lecciones if l.archivo]

    def dependencias(self) -> tuple[list[str], list[str]]:
        """Prerrequisitos (indispensables, recomendados) como IDs de módulo, en orden de aparición."""
        duros, recom, pendientes = [], [], []
        for m in re.finditer(r"\[Módulo (\d+)\]|\((indispensables?|recomendados?)", self.prerrequisitos):
            if m.group(1):
                pendientes.append(f"M{m.group(1)}")
            else:
                (duros if m.group(2).startswith("indispensable") else recom).extend(pendientes)
                pendientes = []
        return duros, recom


FILA = re.compile(r"^\| (L\d+\.\d+\.\d+) \| (.+) \| (Conceptual|Práctica|Mixta) \| (Esencial|Profundizar) \| ([^|]*) \|$")
ENCABEZADO_TABLA = "| ID | Lección | Tipo | Ruta | Material |\n|---|---|---|---|---|"


def leer_celda(celda: str) -> tuple[str, str]:
    """'**[Título](x.md)**<br>Descripción' → (título, descripción)."""
    m = re.fullmatch(r"\*\*(?:\[(.+?)\]\([^)]+\)|(.+?))\*\*(?:<br>(.*))?", celda.strip())
    if not m:
        raise ValueError(f"Celda de lección con formato inesperado: {celda[:80]}")
    titulo = (m.group(1) or m.group(2)).replace("\\|", "|")
    return titulo, (m.group(3) or "").replace("\\|", "|")


def celda(lec: Leccion, enlace: str | None) -> str:
    t = f"[{lec.titulo}]({enlace})" if enlace else lec.titulo
    c = f"**{t}**" + (f"<br>{lec.descripcion}" if lec.descripcion else "")
    return c.replace("|", "\\|")


def leer_modulos() -> list[Modulo]:
    modulos = []
    for carpeta in sorted(DOCS.glob("m[0-9][0-9]-*")):
        texto = (carpeta / "index.md").read_text(encoding="utf-8")
        fm = front_matter(texto)
        mp = re.search(r"^- \*\*Prerrequisitos:\*\* (.+)$", texto, re.M)
        mod = Modulo(n=int(fm["modulo"][1:]), carpeta=carpeta, titulo=fm["titulo"], bloque=fm["bloque"],
                     nivel=fm["nivel"], horas_teoria=int(fm["horas_teoria"]),
                     horas_practica=int(fm["horas_practica"]), prerrequisitos=mp.group(1) if mp else "")
        unidad = ""
        for linea in texto.splitlines():
            mu = re.match(r"^### (\d+\.\d+) · (.+)$", linea)
            if mu:
                unidad = "U" + mu.group(1)
                mod.unidades.append((unidad, mu.group(2)))
                continue
            mf = FILA.match(linea)
            if mf:
                titulo, desc = leer_celda(mf.group(2))
                mod.lecciones.append(Leccion(id=mf.group(1), titulo=titulo, descripcion=desc,
                                             tipo=TIPOS[mf.group(3)], unidad=unidad, ruta=mf.group(4)))
        por_id = {l.id: l for l in mod.lecciones}
        for archivo in sorted(carpeta.glob("l*.md")):
            fl = front_matter(archivo.read_text(encoding="utf-8"))
            lec = por_id.get(fl.get("id", ""))
            if lec:
                lec.archivo = archivo
                lec.estado = fl.get("estado", "")
        mod.soluciones = sorted((carpeta / "soluciones").glob("*.md"))
        modulos.append(mod)
    return modulos


def rel(desde: Path, hacia: Path) -> str:
    return Path(os.path.relpath(hacia, desde.parent)).as_posix()


# ── Generadores ─────────────────────────────────────────────────────────────
def portada_actualizada(mod: Modulo) -> str:
    por_id = {l.id: l for l in mod.lecciones}
    salida = []
    for linea in (mod.carpeta / "index.md").read_text(encoding="utf-8").splitlines():
        mf = FILA.match(linea)
        if mf:
            lec = por_id[mf.group(1)]
            material = ESTADOS.get(lec.estado, "❓ Estado inválido") if lec.archivo else SIN_MATERIAL
            enlace = lec.archivo.name if lec.archivo else None
            linea = f"| {lec.id} | {celda(lec, enlace)} | {TIPOS_INV[lec.tipo]} | {lec.ruta} | {material} |"
        salida.append(linea)
    return "\n".join(salida) + "\n"


def indice(modulos: list[Modulo]) -> str:
    total = sum(len(m.lecciones) for m in modulos)
    con = sum(len(m.con_material) for m in modulos)
    hay = (f"**{con} tiene material**: es la que lleva enlace." if con == 1
           else f"**{con} tienen material**: son las que llevan enlace.")
    out = [
        "<!-- Generado por scripts/generar.py a partir de las portadas de los módulos. No editar a mano. -->",
        "",
        "# Todas las lecciones",
        "",
        f"Las {total} lecciones del curso, etapa por etapa. {hay} Las demás ya forman parte del programa "
        "y se están escribiendo.",
        "",
        "**Tipo de lección:** *Conceptual* (se comprueba con preguntas), *Práctica* (con un ejercicio) o "
        "*Mixta* (las dos cosas). **Ruta:** las lecciones *esenciales* son el núcleo de cada módulo; "
        "las marcadas para *profundizar* amplían el tema y se pueden hacer después.",
        "",
    ]
    etapa = None
    for mod in modulos:
        if mod.bloque != etapa:
            etapa = mod.bloque
            out += [f"## {etapa_nombre(etapa)}", ""]
        out += [f"### [{mod.nombre}]({rel(INDICE, mod.carpeta / 'index.md')})", ""]
        nivel = {"N1": " · Nivel 1", "N2": " · Nivel 2"}.get(mod.nivel, "")
        out += [f"{mod.horas} h{nivel} · {len(mod.lecciones)} lecciones · **Prerrequisitos:** {mod.prerrequisitos}", ""]
        out += ENCABEZADO_TABLA.split("\n")
        for lec in mod.lecciones:
            enlace = rel(INDICE, lec.archivo) if lec.archivo else None
            material = ESTADOS.get(lec.estado, "—") if lec.archivo else SIN_MATERIAL
            out.append(f"| {lec.id} | {celda(lec, enlace)} | {TIPOS_INV[lec.tipo]} | {lec.ruta} | {material} |")
        out.append("")
    out += ["## Electivas", "", "Especializaciones opcionales, sin lecciones numeradas: ver [Electivas](electivas.md).", ""]
    return "\n".join(out)


def nav(modulos: list[Modulo]) -> str:
    def q(s: str) -> str:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

    out = [MARCA_NAV, "nav:",
           "  - Inicio: index.md",
           "  - Empezar:",
           "      - empezar/index.md",
           "      - Cómo estudiar: empezar/metodo.md",
           "      - Estudiar con un tutor de IA: empezar/tutor.md",
           "  - Ruta:",
           "      - ruta/index.md",
           "      - Todas las lecciones: ruta/lecciones.md",
           "      - Proyectos: ruta/proyectos.md",
           "      - Electivas: ruta/electivas.md",
           "  - Módulos:"]
    etapa = None
    for mod in modulos:
        if mod.bloque != etapa:
            etapa = mod.bloque
            out.append(f"      - {q(etapa_nombre(etapa))}:")
        base = mod.carpeta.relative_to(DOCS).as_posix()
        out.append(f"          - {q(f'{mod.n} · {mod.titulo}')}:")
        out.append(f"              - {base}/index.md")
        for lec in mod.con_material:
            out.append(f"              - {q(lec.titulo)}: {base}/{lec.archivo.name}")
        if (mod.carpeta / "evaluacion.md").exists():
            out.append(f"              - Evaluación del módulo: {base}/evaluacion.md")
        if mod.soluciones:
            out.append("              - Soluciones:")
            for s in mod.soluciones:
                lid = "L" + s.stem[1:].replace("-", ".") if s.stem.startswith("l") else ""
                lec = next((l for l in mod.lecciones if l.id == lid), None)
                etiqueta = lec.titulo if lec else s.stem.capitalize()
                out.append(f"                  - {q(etiqueta)}: {base}/soluciones/{s.name}")
    out += ["  - Mi progreso: progreso.md",
            "  - Glosario: glosario.md",
            "  - Sobre el curso:",
            "      - sobre/index.md",
            "      - Cómo se aprueba: sobre/evaluacion.md",
            "      - Versiones y cambios: sobre/versiones.md"]
    return "\n".join(out) + "\n"


def tabla_modulos(modulos: list[Modulo], prefijo: str) -> str:
    out = ["| Módulo | Etapa | Horas | Lecciones | Esenciales | Con material |", "|---|:-:|---:|---:|---:|---:|"]
    for mod in modulos:
        enlace = f"{prefijo}{mod.carpeta.relative_to(DOCS).as_posix()}/index.md"
        esenciales = sum(1 for l in mod.lecciones if l.ruta == "Esencial")
        out.append(f"| [{mod.nombre}]({enlace}) | {ETAPAS[mod.bloque][0]} | {mod.horas} | "
                   f"{len(mod.lecciones)} | {esenciales} | {len(mod.con_material)} |")
    th = sum(m.horas for m in modulos)
    tl = sum(len(m.lecciones) for m in modulos)
    tc = sum(len(m.con_material) for m in modulos)
    te = sum(1 for m in modulos for l in m.lecciones if l.ruta == "Esencial")
    out.append(f"| **Total** | | **{th}** | **{tl}** | **{te}** | **{tc}** |")
    return "\n".join(out)


def reemplazar_entre_marcadores(texto: str, nuevo: str) -> str:
    patron = re.compile(r"(<!-- modulos:inicio -->\n).*?(<!-- modulos:fin -->)", re.S)
    if not patron.search(texto):
        raise SystemExit("No se encontraron los marcadores <!-- modulos:inicio --> y <!-- modulos:fin -->")
    return patron.sub(lambda m: m.group(1) + nuevo + "\n" + m.group(2), texto)


def datos(modulos: list[Modulo] | None = None) -> dict:
    """Estructura del curso para las funciones interactivas. Las rutas son de archivos fuente (docs/)."""
    modulos = modulos or leer_modulos()
    etapas = [{"id": b, "n": n, "titulo": t} for b, (n, t) in ETAPAS.items()]
    mods, lecs = [], []
    for mod in modulos:
        duros, recom = mod.dependencias()
        mods.append({"id": mod.id, "n": mod.n, "titulo": mod.titulo, "etapa": ETAPAS[mod.bloque][0],
                     "nivel": mod.nivel, "horas": mod.horas, "src": mod.carpeta.relative_to(DOCS).as_posix() + "/index.md",
                     "requiere": duros, "recomienda": recom})
        for lec in mod.lecciones:
            lecs.append({"id": lec.id, "modulo": mod.id, "titulo": lec.titulo, "tipo": lec.tipo, "ruta": lec.ruta,
                         "src": lec.archivo.relative_to(DOCS).as_posix() if lec.archivo else None,
                         "estado": lec.estado or None})
    return {"etapas": etapas, "modulos": mods, "lecciones": lecs}


def calcular() -> dict[Path, str]:
    modulos = leer_modulos()
    resultado: dict[Path, str] = {}
    for mod in modulos:
        resultado[mod.carpeta / "index.md"] = portada_actualizada(mod)
    resultado[INDICE] = indice(modulos)
    mk = (RAIZ / "mkdocs.yml").read_text(encoding="utf-8")
    i = mk.find(MARCA_NAV)
    if i == -1:
        raise SystemExit(f"mkdocs.yml: falta la línea marcadora del menú:\n{MARCA_NAV}")
    resultado[RAIZ / "mkdocs.yml"] = mk[:i] + nav(modulos)
    for archivo, prefijo in [(RAIZ / "README.md", "docs/"), (DOCS / "index.md", "")]:
        resultado[archivo] = reemplazar_entre_marcadores(archivo.read_text(encoding="utf-8"),
                                                          tabla_modulos(modulos, prefijo))
    return resultado


def main() -> int:
    comprobar = "--comprobar" in sys.argv
    desactualizados = []
    for archivo, contenido in calcular().items():
        actual = archivo.read_text(encoding="utf-8") if archivo.exists() else None
        if actual != contenido:
            desactualizados.append(archivo.relative_to(RAIZ).as_posix())
            if not comprobar:
                archivo.parent.mkdir(parents=True, exist_ok=True)
                archivo.write_text(contenido, encoding="utf-8", newline="\n")
    if comprobar:
        for a in desactualizados:
            print(f"Desactualizado: {a} (ejecutá python scripts/generar.py)")
        return 1 if desactualizados else 0
    print(f"Archivos regenerados: {len(desactualizados)}" + (f" ({', '.join(desactualizados)})" if desactualizados else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
