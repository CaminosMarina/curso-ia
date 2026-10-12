#!/usr/bin/env python3
"""Verificaciones del repositorio del curso.

Uso:
    python scripts/verificar.py              # verificación normal
    python scripts/verificar.py --publicar   # además, exige lo necesario para publicar

Variables de entorno opcionales:
    VERIFICAR_TERMINOS=<ruta>   Archivo de texto con términos personales a buscar (uno por línea).
                                Debe estar FUERA del repositorio: la lista misma es privada.

Solo usa la biblioteca estándar de Python (3.9 o superior).
Código bajo licencia MIT (ver LICENSE-CODE).
"""
from __future__ import annotations

import datetime as dt
import os
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARCHIVOS_RAIZ = ["README.md", "PROGRAMA.md", "COMO-EMPEZAR.md", "TUTOR.md", "GLOSARIO.md",
                 "LICENSE", "LICENSE-CODE", "CHANGELOG.md", ".gitignore"]
CUADERNO = ["README.md", "PROGRESO.md", "REFUERZO.md", "PUNTO-DE-PARTIDA.md", ".gitignore"]
SECCIONES_LECCION = [
    "Objetivos", "Prerrequisitos", "1. Conceptos y definiciones", "2. Propósito y casos de uso",
    "3. Explicación paso a paso", "4. Ejemplos", "5. Aplicación con herramientas reales",
    "6. Práctica guiada", "7. Ejercicio independiente", "8. Autoevaluación",
    "9. Errores frecuentes", "10. Resumen", "11. Referencias", "Términos nuevos",
    "Registrar en tu cuaderno",
]
SECCIONES_EJERCICIO = ["Objetivo", "Requisitos", "Preparación", "Consigna", "Criterios de aceptación",
                       "Cómo verificar", "Qué guardar en tu cuaderno", "Pistas", "Solución"]
CLAVES_LECCION = ["id", "titulo", "modulo", "unidad", "tipo", "horas_estimadas", "costo", "estado",
                  "version_leccion", "ultima_revision", "version_academica", "soluciones"]
CLAVES_EJERCICIO = ["id", "leccion", "titulo", "nivel", "tiempo_estimado", "costo", "estado",
                    "ultima_revision", "soluciones"]
ESTADOS = {"borrador": "📝", "revisada": "🔍", "publicada": "📗"}
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


def encabezados(texto: str, nivel: int = 2) -> list[str]:
    marca = "#" * nivel + " "
    return [l[len(marca):].strip() for l in texto.splitlines() if l.startswith(marca)]


def slug(titulo: str) -> str:
    """Aproxima el ancla que genera GitHub para un encabezado."""
    t = titulo.strip().lower()
    t = "".join(c for c in t if c.isalnum() or c in " -_" or unicodedata.category(c) == "Mn")
    return t.replace(" ", "-")


def sin_bloques_de_codigo(texto: str) -> str:
    return re.sub(r"```.*?```", "", texto, flags=re.S)


# ── 1. Archivos obligatorios ─────────────────────────────────────────────────
def verificar_estructura() -> None:
    for nombre in ARCHIVOS_RAIZ:
        if not (RAIZ / nombre).exists():
            error(f"Falta el archivo obligatorio {nombre}")
    for nombre in CUADERNO:
        if not (RAIZ / "plantillas" / "cuaderno-estudiante" / nombre).exists():
            error(f"Falta plantillas/cuaderno-estudiante/{nombre}")
    for nombre in ["leccion.md", "ejercicio.md", "evaluacion.md"]:
        if not (RAIZ / "plantillas" / nombre).exists():
            error(f"Falta plantillas/{nombre}")


# ── 2. Programa académico ───────────────────────────────────────────────────
def verificar_programa() -> dict[str, dict]:
    texto = leer(RAIZ / "PROGRAMA.md")
    mv = re.search(r"\*\*Versión académica:\*\*\s*([0-9.]+)", texto)
    version = mv.group(1) if mv else "?"
    if not mv:
        error("PROGRAMA.md: no se encontró la versión académica en el encabezado")
    i6, i7 = texto.find("## 6. Temario detallado"), texto.find("## 7. Módulos electivos")
    if i6 == -1 or i7 == -1:
        error("PROGRAMA.md: no se encontraron las secciones 6 y 7")
        return {}
    temario = texto[i6:i7]

    lecciones: dict[str, dict] = {}
    unidades = set(re.findall(r"^\*\*(U\d+\.\d+) ", temario, flags=re.M))
    patron = re.compile(r"^- (L(\d+)\.(\d+)\.(\d+)) \[([CPM])\] (.+)$", re.M)
    for m in patron.finditer(temario):
        lid, mod, uni, _, tipo, resto = m.groups()
        if lid in lecciones:
            error(f"PROGRAMA.md: ID duplicado {lid}")
        if f"U{mod}.{uni}" not in unidades:
            error(f"PROGRAMA.md: {lid} pertenece a la unidad U{mod}.{uni}, que no existe")
        enlace = re.search(r" · (📝|🔍|📗) \[(Borrador|Revisada|Publicada)\]\(([^)]+)\)$", resto)
        titulo = resto[: enlace.start()] if enlace else resto
        lecciones[lid] = {"modulo": f"M{mod}", "tipo": tipo, "titulo": titulo.strip(),
                          "enlace": enlace.group(3) if enlace else None,
                          "marca": enlace.group(1) if enlace else None}

    # Tabla de la sección 4
    i4, i5 = texto.find("## 4. Resumen"), texto.find("## 5. Hilos")
    tabla = texto[i4:i5]
    conteo: dict[str, int] = {}
    for lec in lecciones.values():
        conteo[lec["modulo"]] = conteo.get(lec["modulo"], 0) + 1
    suma = [0, 0, 0, 0]
    for m in re.finditer(r"^\| (M\d+) \| [^|]+\| [^|]*\| +(\d+) \| +(\d+) \| +(\d+) \| +(\d+) \|$", tabla, re.M):
        mod, n, teo, pra, tot = m.group(1), *map(int, m.groups()[1:])
        if conteo.get(mod, 0) != n:
            error(f"PROGRAMA.md: {mod} declara {n} lecciones y el temario tiene {conteo.get(mod, 0)}")
        if teo + pra != tot:
            error(f"PROGRAMA.md: {mod} teoría + práctica ({teo}+{pra}) ≠ total ({tot})")
        suma = [a + b for a, b in zip(suma, [n, teo, pra, tot])]
    m = re.search(r"\*\*Núcleo obligatorio\*\* \| +\| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\* \| \*\*(\d+)\*\*", tabla)
    if not m:
        error("PROGRAMA.md: no se encontró la fila 'Núcleo obligatorio' en la sección 4")
    elif list(map(int, m.groups())) != suma:
        error(f"PROGRAMA.md: totales del núcleo {list(map(int, m.groups()))} ≠ suma de módulos {suma}")
    if len(lecciones) != suma[0]:
        error(f"PROGRAMA.md: {len(lecciones)} lecciones en el temario y {suma[0]} en la tabla")

    proyectos = set(re.findall(r"^\| (P\d+) \|", texto, re.M))
    faltan = {f"P{i}" for i in range(1, 11)} - proyectos
    if faltan:
        error(f"PROGRAMA.md: faltan proyectos en la sección 8: {sorted(faltan)}")

    print(f"  Programa: versión académica {version}, "
          f"{len(lecciones)} lecciones, {len(conteo)} módulos, horas del núcleo {suma[3]}, "
          f"{len(proyectos & {f'P{i}' for i in range(1, 11)})} proyectos")
    return lecciones


# ── 3. Lecciones y ejercicios ───────────────────────────────────────────────
def verificar_secciones(p: Path, texto: str, requeridas: list[str]) -> None:
    presentes = encabezados(texto)
    for s in requeridas:
        if s not in presentes:
            error(f"{rel(p)}: falta la sección '## {s}'")


def verificar_comunes(p: Path, texto: str, hoy: dt.date) -> None:
    cuerpo = sin_bloques_de_codigo(texto).lower()
    for frase in FRASES_DEPENDIENTES:
        if frase in cuerpo:
            error(f"{rel(p)}: contiene una frase que depende de contexto externo: '{frase}'")
    for m in re.finditer(r"Específico de herramienta · verificado el (\d{4}-\d{2}-\d{2})([^\n]*)", texto):
        fecha = dt.date.fromisoformat(m.group(1))
        if "http" not in m.group(2):
            error(f"{rel(p)}: nota de herramienta sin fuente (URL) en la misma línea")
        if (hoy - fecha).days > DIAS_VIGENCIA_NOTA:
            aviso(f"{rel(p)}: nota de herramienta verificada hace más de {DIAS_VIGENCIA_NOTA} días ({fecha})")


def verificar_lecciones(programa: dict[str, dict], publicar: bool) -> None:
    hoy = dt.date.today()
    archivos = sorted((RAIZ / "modulos").glob("m*/l*.md"))
    enlazados = {}
    for lid, lec in programa.items():
        if lec["enlace"]:
            enlazados[(RAIZ / lec["enlace"]).resolve()] = lid
    for p in archivos:
        texto = leer(p)
        fm = front_matter(texto)
        for clave in CLAVES_LECCION:
            if clave not in fm:
                error(f"{rel(p)}: falta '{clave}' en el front matter")
        lid = fm.get("id", "")
        lec = programa.get(lid)
        if not lec:
            error(f"{rel(p)}: el ID '{lid}' no existe en PROGRAMA.md")
            continue
        if fm.get("tipo") != lec["tipo"]:
            error(f"{rel(p)}: tipo '{fm.get('tipo')}' distinto del programa ('{lec['tipo']}')")
        if fm.get("modulo") != lec["modulo"]:
            error(f"{rel(p)}: módulo '{fm.get('modulo')}' distinto del programa ('{lec['modulo']}')")
        if fm.get("titulo") != lec["titulo"]:
            error(f"{rel(p)}: el título no coincide con PROGRAMA.md")
        estado = fm.get("estado")
        if estado not in ESTADOS:
            error(f"{rel(p)}: estado '{estado}' inválido (borrador, revisada o publicada)")
        elif lec["marca"] != ESTADOS[estado]:
            error(f"{rel(p)}: estado '{estado}' no coincide con la marca de PROGRAMA.md ({lec['marca'] or 'sin enlace'})")
        if publicar and estado != "publicada":
            error(f"{rel(p)}: está en '{estado}'; para publicar debe estar 'publicada'")
        if p.resolve() not in enlazados:
            error(f"{rel(p)}: no está enlazada desde PROGRAMA.md")
        sol = (p.parent / fm.get("soluciones", "")).resolve()
        if not sol.is_file():
            error(f"{rel(p)}: el archivo de soluciones '{fm.get('soluciones')}' no existe")
        verificar_secciones(p, texto, SECCIONES_LECCION)
        for h in encabezados(texto, 2) + encabezados(texto, 3):
            if re.match(r"(solución|soluciones|respuestas)\b", h, re.I):
                error(f"{rel(p)}: la lección contiene una sección de soluciones ('{h}'); van en soluciones/")
        verificar_comunes(p, texto, hoy)
    for destino, lid in enlazados.items():
        if not destino.is_file():
            error(f"PROGRAMA.md: el enlace de {lid} apunta a un archivo inexistente")

    for p in sorted((RAIZ / "modulos").glob("m*/ejercicios/*.md")):
        texto = leer(p)
        fm = front_matter(texto)
        for clave in CLAVES_EJERCICIO:
            if clave not in fm:
                error(f"{rel(p)}: falta '{clave}' en el front matter")
        if fm.get("leccion") not in programa:
            error(f"{rel(p)}: la lección '{fm.get('leccion')}' no existe en PROGRAMA.md")
        if fm.get("estado") not in ESTADOS:
            error(f"{rel(p)}: estado '{fm.get('estado')}' inválido")
        if publicar and fm.get("estado") != "publicada":
            error(f"{rel(p)}: está en '{fm.get('estado')}'; para publicar debe estar 'publicada'")
        if not (p.parent / fm.get("soluciones", "")).resolve().is_file():
            error(f"{rel(p)}: el archivo de soluciones '{fm.get('soluciones')}' no existe")
        verificar_secciones(p, texto, SECCIONES_EJERCICIO)
        sec = re.search(r"^## Solución\n(.*?)(?=^## |\Z)", texto, re.S | re.M)
        if sec and ("soluciones/" not in sec.group(1) or len(sec.group(1).strip()) > 400):
            error(f"{rel(p)}: la sección 'Solución' solo debe enlazar a soluciones/, no contener la solución")
        verificar_comunes(p, texto, hoy)
    print(f"  Lecciones con material: {len(archivos)} · ejercicios: "
          f"{len(list((RAIZ / 'modulos').glob('m*/ejercicios/*.md')))}")


# ── 4. Enlaces internos ─────────────────────────────────────────────────────
def verificar_enlaces() -> None:
    total = 0
    for p in sorted(RAIZ.rglob("*.md")):
        if ".git" in p.parts or p.is_relative_to(RAIZ / "plantillas") and p.parent.name == "plantillas":
            continue  # las plantillas de lección/ejercicio/evaluación usan rutas de ejemplo
        texto = sin_bloques_de_codigo(leer(p))
        texto = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
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
                anclas = {slug(h) for n in range(1, 7) for h in encabezados(leer(objetivo), n)}
                if ancla not in anclas:
                    error(f"{rel(p)}: el ancla '#{ancla}' no existe en {rel(objetivo)}")
    print(f"  Enlaces internos revisados: {total}")


# ── 5. Privacidad y secretos ────────────────────────────────────────────────
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
    for p in sorted(RAIZ.rglob("*")):
        if not p.is_file() or ".git" in p.parts or p.suffix in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".ico"}:
            continue
        try:
            texto = leer(p)
        except UnicodeDecodeError:
            continue
        revisados += 1
        es_este_script = p.resolve() == Path(__file__).resolve()
        if not es_este_script:
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
            f"El marcador [AUTOR_PUBLICO] aparece {marcador} veces: reemplazalo por el seudónimo antes de publicar")
    print(f"  Archivos revisados por privacidad: {revisados} · términos privados: {len(terminos)}")


def main() -> int:
    publicar = "--publicar" in sys.argv
    print(f"Verificando {RAIZ.name} ({'modo publicación' if publicar else 'modo normal'})")
    verificar_estructura()
    programa = verificar_programa()
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
