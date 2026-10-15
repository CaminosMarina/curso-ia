"""Hook de MkDocs con las funciones interactivas del curso.

1. Autoevaluaciones: convierte los bloques ```quiz en preguntas de opción múltiple que se corrigen
   al instante (assets/curso.js). Formato, que en GitHub se ve como texto:

       ```quiz
       ¿Pregunta?
       - [ ] Opción incorrecta
       - [x] Opción correcta
       > Explicación que se muestra al responder.
       ```

2. Progreso: agrega a cada lección y a cada portada de módulo el lugar donde assets/curso.js muestra
   y guarda el avance (en el navegador de cada persona).
3. Glosario al pasar el mouse: define como abreviaturas los términos de docs/glosario.md.
4. Datos: publica assets/datos/curso.json (etapas, módulos, lecciones y sus direcciones) a partir de
   las portadas de los módulos, con scripts/generar.py.

Código bajo licencia MIT (ver LICENSE-CODE).
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

_RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_RAIZ / "scripts"))
import generar  # noqa: E402

_URLS: dict[str, str] = {}
_ABREVIATURAS = ""

# Términos del glosario que se marcan en el texto, con las variantes que aparecen en las lecciones.
_VARIANTES = {
    "LLM": ["LLM", "LLMs"],
    "Token": ["token", "tokens", "Token", "Tokens"],
    "Ventana de contexto": ["ventana de contexto", "Ventana de contexto"],
    "Context engineering": ["context engineering", "Context engineering", "Context Engineering"],
    "Embedding": ["embedding", "embeddings", "Embedding", "Embeddings"],
    "RAG": ["RAG"],
    "Tool calling": ["tool calling", "Tool calling"],
    "MCP": ["MCP"],
    "Skill": ["skill", "skills", "Skill", "Skills"],
    "A2A": ["A2A"],
    "Prompt injection": ["prompt injection", "Prompt injection"],
}


def _glosario() -> str:
    texto = (_RAIZ / "docs" / "glosario.md").read_text(encoding="utf-8")
    defs = {}
    for fila in re.finditer(r"^\| \*\*([^*]+)\*\*[^|]*\| ([^|]+) \|", texto, re.M):
        termino, definicion = fila.group(1).strip(), fila.group(2).strip()
        primera = re.split(r"(?<=\.)\s", definicion, maxsplit=1)[0]
        primera = re.sub(r"[*`]", "", primera)
        defs[termino] = primera.replace("\n", " ")
    lineas = []
    for termino, variantes in _VARIANTES.items():
        if termino in defs:
            lineas += [f"*[{v}]: {defs[termino]}" for v in variantes]
    return "\n" + "\n".join(lineas) + "\n"


def on_config(config, **kwargs):
    global _ABREVIATURAS
    _ABREVIATURAS = _glosario()
    return config


def on_files(files, config, **kwargs):
    _URLS.clear()
    for f in files.documentation_pages():
        _URLS[f.src_uri] = f.url
    return files


_QUIZ = re.compile(r"^```quiz[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def _quiz(m: re.Match) -> str:
    lineas = [l.rstrip() for l in m.group(1).strip().splitlines()]
    pregunta, opciones, explicacion = [], [], []
    for l in lineas:
        mo = re.match(r"^- \[( |x|X)\] (.+)$", l)
        if mo:
            opciones.append((mo.group(1).lower() == "x", mo.group(2)))
        elif l.startswith(">"):
            explicacion.append(l[1:].strip())
        elif l.strip():
            (explicacion if opciones else pregunta).append(l.strip())
    if not pregunta or len(opciones) < 2 or sum(c for c, _ in opciones) != 1:
        raise ValueError(f"Bloque quiz mal formado: {m.group(0)[:120]}")
    partes = ['<div class="cu-quiz" markdown>',
              f'<p class="cu-quiz-pregunta" markdown="span">{" ".join(pregunta)}</p>',
              '<div class="cu-quiz-opciones">']
    for correcta, texto in opciones:
        partes.append(f'<button type="button" class="cu-quiz-opcion" data-ok="{1 if correcta else 0}" markdown="span">{texto}</button>')
    partes.append("</div>")
    partes.append(f'<div class="cu-quiz-explicacion" hidden markdown="span">{" ".join(explicacion)}</div>')
    partes.append("</div>")
    return "\n".join(partes)


def on_page_markdown(markdown, page, config, files, **kwargs):
    markdown = _QUIZ.sub(_quiz, markdown)
    if page.file.src_uri != "glosario.md":
        markdown += _ABREVIATURAS
    return markdown


def on_page_content(html_text, page, config, files, **kwargs):
    meta = page.meta or {}
    if meta.get("id") and meta.get("modulo"):
        marca = (f'<div class="cu-leccion" data-id="{html.escape(str(meta["id"]))}" '
                 f'data-modulo="{html.escape(str(meta["modulo"]))}" data-tipo="{html.escape(str(meta.get("tipo", "")))}"></div>')
        html_text += marca
    elif meta.get("modulo"):
        marca = f'<div class="cu-modulo" data-modulo="{html.escape(str(meta["modulo"]))}"></div>'
        html_text = re.sub(r"(</h1>)", r"\1" + marca, html_text, count=1)
    return html_text


def on_post_build(config, **kwargs):
    datos = generar.datos()
    for m in datos["modulos"]:
        m["url"] = _URLS.get(m.pop("src"), "")
    for l in datos["lecciones"]:
        src = l.pop("src")
        l["url"] = _URLS.get(src, "") if src else ""
    destino = Path(config["site_dir"]) / "assets" / "datos" / "curso.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
