#!/usr/bin/env python3
"""Genera las partes derivadas del curso a partir de sus fuentes.

Fuentes de verdad:
- docs/mNN-*/index.md   Portada de cada módulo: datos del módulo, unidades y lecciones del programa.
- docs/mNN-*/l*.md      Lecciones con material: su front matter define el estado editorial.

Partes generadas (no se editan a mano):
- En cada portada de módulo: la columna "Material" de la tabla de lecciones.
- docs/programa/indice.md: índice completo de lecciones.
- mkdocs.yml: el bloque "nav" (menú del sitio).
- README.md y docs/index.md: la tabla de módulos, entre los marcadores <!-- modulos:inicio --> y <!-- modulos:fin -->.

Uso:
    python scripts/generar.py              # regenera los archivos
    python scripts/generar.py --comprobar  # solo comprueba que estén al día (lo usa verificar.py y la CI)

Solo usa la biblioteca estándar de Python (3.9 o superior). Código bajo licencia MIT (ver LICENSE-CODE).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
BLOQUES = {
    "I": "Bloque I · Fundamentos y uso profesional",
    "II": "Bloque II · Construir con modelos",
    "III": "Bloque III · Agentes e interoperabilidad",
    "IV": "Bloque IV · Automatización y sistemas avanzados",
    "V": "Bloque V · Producción e integración",
}
ESTADOS = {"borrador": "📝 Borrador", "revisada": "🔍 Revisada", "publicada": "📗 Publicada"}
MARCA_NAV = "# ── Menú del sitio: generado por scripts/generar.py, no editar a mano ──"


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


@dataclass
class Leccion:
    id: str
    tipo: str
    titulo: str            # título del programa
    unidad: str
    archivo: Path | None = None   # archivo de la lección, si tiene material
    titulo_corto: str = ""
    estado: str = ""


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
    def horas(self) -> int:
        return self.horas_teoria + self.horas_practica

    @property
    def con_material(self) -> list[Leccion]:
        return [l for l in self.lecciones if l.archivo]


FILA = re.compile(r"^\| (L\d+\.\d+\.\d+) \| (.+) \| ([CPM]) \| ([^|]*) \|$")


def titulo_de_celda(celda: str) -> str:
    m = re.fullmatch(r"\[(.+)\]\([^)]+\)", celda.strip())
    t = m.group(1) if m else celda.strip()
    return t.replace("\\|", "|")


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
            mu = re.match(r"^### (U\d+\.\d+) · (.+)$", linea)
            if mu:
                unidad = mu.group(1)
                mod.unidades.append((mu.group(1), mu.group(2)))
                continue
            mf = FILA.match(linea)
            if mf:
                mod.lecciones.append(Leccion(id=mf.group(1), titulo=titulo_de_celda(mf.group(2)),
                                             tipo=mf.group(3), unidad=unidad))
        por_id = {l.id: l for l in mod.lecciones}
        for archivo in sorted(carpeta.glob("l*.md")):
            fl = front_matter(archivo.read_text(encoding="utf-8"))
            lec = por_id.get(fl.get("id", ""))
            if lec:
                lec.archivo = archivo
                lec.titulo_corto = fl.get("titulo_corto") or lec.titulo
                lec.estado = fl.get("estado", "")
        mod.soluciones = sorted((carpeta / "soluciones").glob("*.md"))
        modulos.append(mod)
    return modulos


def rel(desde: Path, hacia: Path) -> str:
    """Ruta relativa con barras, de un archivo a otro dentro de docs/."""
    import os
    return Path(os.path.relpath(hacia, desde.parent)).as_posix()


# ── Generadores ─────────────────────────────────────────────────────────────
def portada_actualizada(mod: Modulo) -> str:
    """Reescribe la columna 'Material' y el enlace de cada lección en la portada del módulo."""
    por_id = {l.id: l for l in mod.lecciones}
    salida = []
    for linea in (mod.carpeta / "index.md").read_text(encoding="utf-8").splitlines():
        mf = FILA.match(linea)
        if mf:
            lec = por_id[mf.group(1)]
            celda = lec.titulo.replace("|", "\\|")
            if lec.archivo:
                celda = f"[{celda}]({lec.archivo.name})"
                material = ESTADOS.get(lec.estado, "❓ Estado inválido")
            else:
                material = "—"
            linea = f"| {lec.id} | {celda} | {lec.tipo} | {material} |"
        salida.append(linea)
    return "\n".join(salida) + "\n"


def indice(modulos: list[Modulo]) -> str:
    destino = DOCS / "programa" / "indice.md"
    total = sum(len(m.lecciones) for m in modulos)
    con = sum(len(m.con_material) for m in modulos)
    out = [
        "<!-- Generado por scripts/generar.py a partir de las portadas de los módulos. No editar a mano. -->",
        "",
        "# Índice de lecciones",
        "",
        f"Las {total} lecciones del núcleo, módulo por módulo. "
        + (f"**{con} tiene material**: es la que lleva enlace. " if con == 1 else f"**{con} tienen material**: son las que llevan enlace. ")
        + 
        "Las demás forman parte del programa, pero su material todavía se está escribiendo.",
        "",
        "**Tipo de lección:** `C` conceptual (se verifica con preguntas) · `P` práctica (se verifica con un ejercicio) · "
        "`M` mixta (las dos cosas). Detalle en [Evaluación y estados](evaluacion.md).",
        "",
    ]
    bloque_actual = None
    for mod in modulos:
        if mod.bloque != bloque_actual:
            bloque_actual = mod.bloque
            out += [f"## {BLOQUES[mod.bloque]}", ""]
        out += [f"### [{mod.id} · {mod.titulo}]({rel(destino, mod.carpeta / 'index.md')})", ""]
        nivel = {"N1": " · Nivel 1", "N2": " · Nivel 2"}.get(mod.nivel, "")
        out += [f"{mod.horas} h{nivel} · {len(mod.lecciones)} lecciones · **Prerrequisitos:** {mod.prerrequisitos}", ""]
        out += ["| ID | Lección | Tipo | Material |", "|---|---|:-:|---|"]
        for lec in mod.lecciones:
            celda = lec.titulo.replace("|", "\\|")
            if lec.archivo:
                celda = f"[{celda}]({rel(destino, lec.archivo)})"
            out.append(f"| {lec.id} | {celda} | {lec.tipo} | {ESTADOS.get(lec.estado, '—') if lec.archivo else '—'} |")
        out.append("")
    out += ["## Electivas", "", "Especializaciones opcionales, sin lecciones numeradas: ver [Electivas](../electivas.md).", ""]
    return "\n".join(out)


def nav(modulos: list[Modulo]) -> str:
    def q(s: str) -> str:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

    out = [MARCA_NAV, "nav:",
           "  - Inicio: index.md",
           "  - Cómo empezar:",
           "      - empezar/index.md",
           "      - Estudiar con un tutor de IA: empezar/tutor.md",
           "  - Programa:",
           "      - programa/index.md",
           "      - Índice de lecciones: programa/indice.md",
           "      - Proyectos: programa/proyectos.md",
           "      - Evaluación y estados: programa/evaluacion.md",
           "      - Versiones y cambios: programa/versiones.md",
           "  - Módulos:"]
    bloque_actual = None
    for mod in modulos:
        if mod.bloque != bloque_actual:
            bloque_actual = mod.bloque
            out.append(f"      - {q(BLOQUES[mod.bloque])}:")
        base = mod.carpeta.relative_to(DOCS).as_posix()
        out.append(f"          - {q(f'{mod.id} · {mod.titulo}')}:")
        out.append(f"              - {base}/index.md")
        for lec in mod.con_material:
            out.append(f"              - {q(f'{lec.id} · {lec.titulo_corto}')}: {base}/{lec.archivo.name}")
        if (mod.carpeta / "evaluacion.md").exists():
            out.append(f"              - Evaluación del módulo: {base}/evaluacion.md")
        if mod.soluciones:
            out.append("              - Soluciones:")
            for s in mod.soluciones:
                etiqueta = s.stem.upper().replace("-", ".") if s.stem.startswith("l") else s.stem.capitalize()
                out.append(f"                  - {q(etiqueta)}: {base}/soluciones/{s.name}")
    out += ["  - Electivas: electivas.md", "  - Glosario: glosario.md"]
    return "\n".join(out) + "\n"


def tabla_modulos(modulos: list[Modulo], prefijo: str) -> str:
    out = ["| Módulo | Bloque | Horas | Lecciones | Con material |", "|---|:-:|---:|---:|---:|"]
    for mod in modulos:
        enlace = f"{prefijo}{mod.carpeta.relative_to(DOCS).as_posix()}/index.md"
        out.append(f"| [{mod.id} · {mod.titulo}]({enlace}) | {mod.bloque} | {mod.horas} | "
                   f"{len(mod.lecciones)} | {len(mod.con_material)} |")
    th = sum(m.horas for m in modulos)
    tl = sum(len(m.lecciones) for m in modulos)
    tc = sum(len(m.con_material) for m in modulos)
    out.append(f"| **Núcleo** | | **{th}** | **{tl}** | **{tc}** |")
    return "\n".join(out)


def reemplazar_entre_marcadores(texto: str, nuevo: str) -> str:
    patron = re.compile(r"(<!-- modulos:inicio -->\n).*?(<!-- modulos:fin -->)", re.S)
    if not patron.search(texto):
        raise SystemExit("No se encontraron los marcadores <!-- modulos:inicio --> y <!-- modulos:fin -->")
    return patron.sub(lambda m: m.group(1) + nuevo + "\n" + m.group(2), texto)


def calcular() -> dict[Path, str]:
    modulos = leer_modulos()
    resultado: dict[Path, str] = {}
    for mod in modulos:
        resultado[mod.carpeta / "index.md"] = portada_actualizada(mod)
    resultado[DOCS / "programa" / "indice.md"] = indice(modulos)
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
                archivo.write_text(contenido, encoding="utf-8", newline="\n")
    if comprobar:
        for a in desactualizados:
            print(f"Desactualizado: {a} (ejecutá python scripts/generar.py)")
        return 1 if desactualizados else 0
    print(f"Archivos regenerados: {len(desactualizados)}" + (f" ({', '.join(desactualizados)})" if desactualizados else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
