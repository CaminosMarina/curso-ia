#!/usr/bin/env python3
"""Verificaciones del repositorio del curso.

Uso:
    python scripts/verificar.py              # verificación normal (la ejecuta también la CI)
    python scripts/verificar.py --publicar   # además, exige lo necesario para publicar una versión

Variables de entorno opcionales:
    VERIFICAR_TERMINOS=<ruta>   Archivo de texto con términos personales a buscar (uno por línea).
                                Debe estar FUERA del repositorio: la lista misma es privada.

Qué revisa:
    1. Archivos obligatorios.
    2. Programa: IDs únicos, unidades, lecciones y horas por módulo contra la tabla del programa, proyectos.
    3. Partes generadas al día (scripts/generar.py --comprobar).
    4. Lecciones: front matter, coherencia con el programa, secciones obligatorias, soluciones separadas,
       frases que dependen de contexto externo y notas de herramientas con fecha y fuente.
    5. Enlaces internos y anclas (con las reglas de GitHub; el sitio las vuelve a revisar con mkdocs --strict).
    6. Privacidad: secretos, rutas personales, correos y términos de la lista privada.

Solo usa la biblioteca estándar de Python (3.9 o superior). Código bajo licencia MIT (ver LICENSE-CODE).
"""
from __future__ import annotations

import datetime as dt
import os
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar  # noqa: E402  (mismo directorio)

RAIZ = generar.RAIZ
DOCS = generar.DOCS
OBLIGATORIOS = [
    "README.md", "CHANGELOG.md", "LICENSE", "LICENSE-CODE", ".gitignore", "mkdocs.yml", "requirements.txt",
    "hooks/callouts.py", ".github/workflows/sitio.yml",
    "docs/index.md", "docs/empezar/index.md", "docs/empezar/tutor.md", "docs/glosario.md", "docs/electivas.md",
    "docs/programa/index.md", "docs/programa/indice.md", "docs/programa/proyectos.md",
    "docs/programa/evaluacion.md", "docs/programa/versiones.md",
    "plantillas/leccion.md", "plantillas/evaluacion.md",
    "plantillas/cuaderno-estudiante/README.md", "plantillas/cuaderno-estudiante/PROGRESO.md",
    "plantillas/cuaderno-estudiante/REFUERZO.md", "plantillas/cuaderno-estudiante/PUNTO-DE-PARTIDA.md",
    "plantillas/cuaderno-estudiante/.gitignore",
]
SECCIONES_LECCION = ["Teoría", "Práctica", "Autoevaluación", "Resumen", "Para profundizar"]
CLAVES_LECCION = ["id", "titulo", "titulo_corto", "modulo", "unidad", "tipo", "horas_estimadas", "costo",
                  "estado", "ultima_revision", "version_academica", "soluciones"]
FRASES_DEPENDIENTES = [
    "como hablamos", "como charlamos", "como vimos en la conversación", "en nuestra conversación",
    "como te expliqué", "según tu experiencia personal", "tu profesor", "tu profesora",
]
SECRETOS = {
    "clave tipo sk-": r"\bsk-[A-Za-z0-9_-]{20,}",
    "token de GitHub": r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{20,}",
    "clave de AWS": r"\bAKIA[0-9A-Z]{16}\b",
    "clave de Google": r"\bAIza[0-9A-Za-z_-]{35}\b",
    "token de Slack": r"\bxox[abprs]-[A-Za-z0-9-]{10,}",
    "clave privada": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
}
RUTAS_PERSONALES = {
    "ruta de usuario de Windows": r"[A-Za-z]:\\+Users\\+[^\\\s]+",
    "ruta de usuario de Linux": r"/home/[a-z_][a-z0-9_-]*/",
    "ruta de usuario de macOS": r"/Users/[A-Za-z][^/\s]*/",
}
EMAIL = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
EMAIL_PERMITIDO = re.compile(r"(noreply|no-reply)@|@example\.(com|org|net)$", re.I)
EXCLUIR_DIRS = {".git", "site", "__pycache__", ".venv", "venv", "node_modules"}
DIAS_VIGENCIA_NOTA = 180

errores: list[str] = []
avisos: list[str] = []


def error(msg: str) -> None:
    errores.append(msg)


def aviso(msg: str) -> None:
    avisos.append(msg)


def rel(p: Path) -> str:
    return p.relative_to(RAIZ).as_posix()


def leer(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def archivos_del_repo():
    """Archivos que se versionan: excluye carpetas generadas y notas locales (*.local.md)."""
    for p in sorted(RAIZ.rglob("*")):
        if not p.is_file() or EXCLUIR_DIRS & set(p.relative_to(RAIZ).parts) or p.name.endswith(".local.md"):
            continue
        yield p


def encabezados(texto: str, nivel: int = 2) -> list[str]:
    marca = "#" * nivel + " "
    return [l[len(marca):].strip() for l in sin_bloques_de_codigo(texto).splitlines() if l.startswith(marca)]


def slug(titulo: str) -> str:
    """Aproxima el ancla que genera GitHub para un encabezado."""
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", titulo.strip().lower())
    t = "".join(c for c in t if c.isalnum() or c in " -_" or unicodedata.category(c) == "Mn")
    return t.replace(" ", "-")


def sin_bloques_de_codigo(texto: str) -> str:
    return re.sub(r"^ *(```|~~~).*?^ *\1", "", texto, flags=re.S | re.M)


# ── 1. Archivos obligatorios ─────────────────────────────────────────────────
def verificar_estructura() -> None:
    for nombre in OBLIGATORIOS:
        if not (RAIZ / nombre).exists():
            error(f"Falta el archivo obligatorio {nombre}")


# ── 2. Programa ─────────────────────────────────────────────────────────────
def verificar_programa() -> dict[str, generar.Leccion]:
    modulos = generar.leer_modulos()
    lecciones: dict[str, generar.Leccion] = {}
    for mod in modulos:
        unidades = {u for u, _ in mod.unidades}
        for lec in mod.lecciones:
            if lec.id in lecciones:
                error(f"{rel(mod.carpeta / 'index.md')}: ID duplicado {lec.id}")
            lecciones[lec.id] = lec
            m = re.match(r"L(\d+)\.(\d+)\.\d+$", lec.id)
            if int(m.group(1)) != mod.n:
                error(f"{rel(mod.carpeta / 'index.md')}: {lec.id} no pertenece al módulo {mod.id}")
            if lec.unidad != f"U{m.group(1)}.{m.group(2)}" or lec.unidad not in unidades:
                error(f"{rel(mod.carpeta / 'index.md')}: {lec.id} está bajo la unidad {lec.unidad or '(ninguna)'}")

    texto = leer(DOCS / "programa" / "index.md")
    if not re.search(r"\*\*Versión académica 1\.\d+", texto):
        error("docs/programa/index.md: no se encontró la versión académica en el encabezado")
    tabla = {}
    for m in re.finditer(r"^\| M(\d+) \| [^|]+\| [^|]*\| +(\d+) \| +(\d+) \| +(\d+) \| +(\d+) \|$", texto, re.M):
        tabla[int(m.group(1))] = tuple(map(int, m.groups()[1:]))
    suma = [0, 0, 0, 0]
    for mod in modulos:
        fila = tabla.get(mod.n)
        if not fila:
            error(f"docs/programa/index.md: falta {mod.id} en la tabla de módulos y horas")
            continue
        n, teo, pra, tot = fila
        if n != len(mod.lecciones):
            error(f"{mod.id}: la tabla del programa declara {n} lecciones y la portada tiene {len(mod.lecciones)}")
        if (teo, pra) != (mod.horas_teoria, mod.horas_practica):
            error(f"{mod.id}: horas de la portada ({mod.horas_teoria}+{mod.horas_practica}) ≠ tabla ({teo}+{pra})")
        if teo + pra != tot:
            error(f"{mod.id}: teoría + práctica ({teo}+{pra}) ≠ total ({tot}) en la tabla del programa")
        suma = [a + b for a, b in zip(suma, fila)]
    if set(tabla) - {m.n for m in modulos}:
        error(f"docs/programa/index.md: la tabla tiene módulos sin portada: {sorted(set(tabla) - {m.n for m in modulos})}")
    m = re.search(r"\*\*Núcleo obligatorio\*\* \| +\| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\*", texto)
    if not m:
        error("docs/programa/index.md: no se encontró la fila 'Núcleo obligatorio'")
    elif list(map(int, m.groups())) != suma:
        error(f"docs/programa/index.md: totales del núcleo {list(map(int, m.groups()))} ≠ suma de módulos {suma}")

    proyectos = set(re.findall(r"^\| (P\d+) \|", leer(DOCS / "programa" / "proyectos.md"), re.M))
    faltan = {f"P{i}" for i in range(1, 11)} - proyectos
    if faltan:
        error(f"docs/programa/proyectos.md: faltan proyectos: {sorted(faltan)}")
    print(f"  Programa: {len(lecciones)} lecciones, {len(modulos)} módulos, "
          f"{suma[3]} h de núcleo, {len(proyectos)} proyectos")
    return lecciones


# ── 3. Partes generadas ─────────────────────────────────────────────────────
def verificar_generados() -> None:
    for archivo, contenido in generar.calcular().items():
        if not archivo.exists() or leer(archivo) != contenido:
            error(f"{rel(archivo)} está desactualizado: ejecutá python scripts/generar.py")


# ── 4. Lecciones ────────────────────────────────────────────────────────────
def verificar_comunes(p: Path, texto: str, hoy: dt.date) -> None:
    cuerpo = sin_bloques_de_codigo(texto).lower()
    for frase in FRASES_DEPENDIENTES:
        if frase in cuerpo:
            error(f"{rel(p)}: contiene una frase que depende de contexto externo: '{frase}'")
    for m in re.finditer(r"Específico de herramienta\**\s*· verificado el (\d{4}-\d{2}-\d{2})([^\n]*)", texto):
        fecha = dt.date.fromisoformat(m.group(1))
        if "http" not in m.group(2):
            error(f"{rel(p)}: nota de herramienta sin fuente (URL) en la misma línea")
        if (hoy - fecha).days > DIAS_VIGENCIA_NOTA:
            aviso(f"{rel(p)}: nota de herramienta verificada hace más de {DIAS_VIGENCIA_NOTA} días ({fecha})")


def verificar_lecciones(programa: dict[str, generar.Leccion], publicar: bool) -> None:
    hoy = dt.date.today()
    archivos = sorted(DOCS.glob("m[0-9][0-9]-*/l*.md"))
    for p in archivos:
        texto = leer(p)
        fm = generar.front_matter(texto)
        for clave in CLAVES_LECCION:
            if clave not in fm:
                error(f"{rel(p)}: falta '{clave}' en el front matter")
        lec = programa.get(fm.get("id", ""))
        if not lec:
            error(f"{rel(p)}: el ID '{fm.get('id')}' no existe en ninguna portada de módulo")
            continue
        if lec.archivo is None or lec.archivo.resolve() != p.resolve():
            error(f"{rel(p)}: la lección {lec.id} está en la carpeta de otro módulo")
        if fm.get("modulo") != f"M{lec.id.split('.')[0][1:]}":
            error(f"{rel(p)}: módulo '{fm.get('modulo')}' no coincide con el ID {lec.id}")
        if fm.get("unidad") != lec.unidad:
            error(f"{rel(p)}: unidad '{fm.get('unidad')}' distinta de la portada ('{lec.unidad}')")
        if fm.get("tipo") != lec.tipo:
            error(f"{rel(p)}: tipo '{fm.get('tipo')}' distinto de la portada ('{lec.tipo}')")
        if fm.get("titulo") != lec.titulo:
            error(f"{rel(p)}: 'titulo' no coincide con el de la portada del módulo")
        estado = fm.get("estado")
        if estado not in generar.ESTADOS:
            error(f"{rel(p)}: estado '{estado}' inválido (borrador, revisada o publicada)")
        if publicar and estado != "publicada":
            error(f"{rel(p)}: está en '{estado}'; para publicar debe estar 'publicada'")
        if not (p.parent / fm.get("soluciones", "")).resolve().is_file():
            error(f"{rel(p)}: el archivo de soluciones '{fm.get('soluciones')}' no existe")
        presentes = encabezados(texto)
        for s in SECCIONES_LECCION:
            if s not in presentes:
                error(f"{rel(p)}: falta la sección '## {s}'")
        if presentes[: len(SECCIONES_LECCION)] != SECCIONES_LECCION:
            error(f"{rel(p)}: las secciones de nivel 2 deben ser, en orden: {', '.join(SECCIONES_LECCION)}")
        for h in encabezados(texto, 2) + encabezados(texto, 3):
            if re.match(r"(solución|soluciones|respuestas)\b", h, re.I):
                error(f"{rel(p)}: la lección contiene una sección de soluciones ('{h}'); van en soluciones/")
        verificar_comunes(p, texto, hoy)
    for p in sorted(DOCS.glob("m[0-9][0-9]-*/soluciones/*.md")):
        verificar_comunes(p, leer(p), hoy)
    print(f"  Lecciones con material: {len(archivos)}")


# ── 5. Enlaces internos ─────────────────────────────────────────────────────
def verificar_enlaces() -> None:
    total = 0
    cache: dict[Path, set[str]] = {}
    for p in archivos_del_repo():
        if p.suffix != ".md" or p.parent == RAIZ / "plantillas":
            continue  # las plantillas usan rutas de ejemplo
        texto = re.sub(r"<!--.*?-->", "", sin_bloques_de_codigo(leer(p)), flags=re.S)
        texto = re.sub(r"`[^`\n]*`", "", texto)
        for m in re.finditer(r"\]\(([^)\s]+)\)", texto):
            destino = m.group(1)
            if re.match(r"^(https?:|mailto:)", destino):
                continue
            total += 1
            ruta, _, ancla = destino.partition("#")
            objetivo = (p.parent / ruta).resolve() if ruta else p
            if not objetivo.exists():
                error(f"{rel(p)}: enlace roto → {destino}")
                continue
            if ancla and objetivo.is_file() and objetivo.suffix == ".md":
                if objetivo not in cache:
                    t = leer(objetivo)
                    cache[objetivo] = {slug(h) for n in range(1, 7) for h in encabezados(t, n)}
                if ancla not in cache[objetivo]:
                    error(f"{rel(p)}: el ancla '#{ancla}' no existe en {rel(objetivo)}")
    print(f"  Enlaces internos revisados: {total}")


# ── 6. Privacidad y secretos ────────────────────────────────────────────────
def verificar_privacidad(publicar: bool) -> None:
    terminos: list[str] = []
    ruta_terminos = os.environ.get("VERIFICAR_TERMINOS")
    if ruta_terminos:
        rt = Path(ruta_terminos).expanduser().resolve()
        if rt.is_relative_to(RAIZ):
            error("VERIFICAR_TERMINOS apunta a un archivo dentro del repositorio: movelo afuera")
        elif rt.is_file():
            terminos = [t.strip() for t in rt.read_text(encoding="utf-8").splitlines()
                        if t.strip() and not t.startswith("#")]
        else:
            error(f"VERIFICAR_TERMINOS: no existe el archivo {rt}")
    elif publicar:
        error("Para publicar, definí VERIFICAR_TERMINOS con tu lista privada de términos personales")
    else:
        aviso("VERIFICAR_TERMINOS no está definido: no se buscaron términos personales")

    marcador = 0
    revisados = 0
    for p in archivos_del_repo():
        if p.suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".ico", ".svg"}:
            continue
        try:
            texto = leer(p)
        except UnicodeDecodeError:
            continue
        revisados += 1
        if p.resolve() != Path(__file__).resolve():
            for nombre, patron in SECRETOS.items():
                if re.search(patron, texto):
                    error(f"{rel(p)}: posible {nombre}")
            for nombre, patron in RUTAS_PERSONALES.items():
                for m in re.finditer(patron, texto):
                    error(f"{rel(p)}: {nombre}: {m.group(0)}")
            for m in re.finditer(EMAIL, texto):
                if not EMAIL_PERMITIDO.search(m.group(0)):
                    error(f"{rel(p)}: dirección de correo: {m.group(0)}")
        for t in terminos:
            # palabra completa, sin distinguir mayúsculas: "Ana" no coincide con "análisis"
            if re.search(r"(?<!\w)" + re.escape(t) + r"(?!\w)", texto, re.I):
                error(f"{rel(p)}: contiene un término de tu lista privada (no se muestra)")
        marcador += texto.count("[AUTOR_PUBLICO]")
    if marcador:
        (error if publicar else aviso)(
            f"El marcador [AUTOR_PUBLICO] aparece {marcador} veces: definí la autoría pública antes de publicar")
    print(f"  Archivos revisados por privacidad: {revisados} · términos privados: {len(terminos)}")


def main() -> int:
    publicar = "--publicar" in sys.argv
    print(f"Verificando el curso ({'modo publicación' if publicar else 'modo normal'})")
    verificar_estructura()
    programa = verificar_programa()
    verificar_generados()
    verificar_lecciones(programa, publicar)
    verificar_enlaces()
    verificar_privacidad(publicar)
    for a in avisos:
        print(f"AVISO: {a}")
    for e in errores:
        print(f"ERROR: {e}")
    print(f"Resultado: {len(errores)} errores, {len(avisos)} avisos")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
