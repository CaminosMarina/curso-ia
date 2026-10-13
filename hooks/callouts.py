"""Hook de MkDocs: muestra los avisos con sintaxis de GitHub como recuadros del sitio.

En los archivos se escribe la sintaxis de GitHub, que también se ve bien al leer el repositorio:

    > [!NOTE]
    > Texto del aviso.

Al construir el sitio, este hook lo convierte en un recuadro (admonition) de Material for MkDocs.
Tipos: NOTE, TIP, IMPORTANT, WARNING y CAUTION. Si la primera línea del aviso es solo un texto en
negrita (por ejemplo **Antes de empezar**), se usa como título del recuadro. Los bloques de código
no se tocan.

Código bajo licencia MIT (ver LICENSE-CODE).
"""
from __future__ import annotations

import re

TIPOS = {
    "NOTE": ("note", "Nota"),
    "TIP": ("tip", "Consejo"),
    "IMPORTANT": ("info", "Importante"),
    "WARNING": ("warning", "Atención"),
    "CAUTION": ("danger", "Cuidado"),
}
INICIO = re.compile(r"^(\s*)> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$")
CERCA = re.compile(r"^\s*(```|~~~)")


def convertir(markdown: str) -> str:
    lineas = markdown.split("\n")
    salida: list[str] = []
    en_codigo = False
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        if CERCA.match(linea):
            en_codigo = not en_codigo
        m = None if en_codigo else INICIO.match(linea)
        if not m:
            salida.append(linea)
            i += 1
            continue
        sangria, tipo = m.group(1), m.group(2)
        clase, titulo = TIPOS[tipo]
        i += 1
        # Si la primera línea del aviso es solo un texto en negrita, se usa como título del recuadro:
        #   > [!NOTE]
        #   > **Antes de empezar**
        if i < len(lineas):
            mt = re.match(rf"^{re.escape(sangria)}> \*\*([^*]+)\*\*\s*$", lineas[i])
            if mt:
                titulo = mt.group(1).strip()
                i += 1
                if i < len(lineas) and re.match(rf"^{re.escape(sangria)}>\s*$", lineas[i]):
                    i += 1
        salida.append(f'{sangria}!!! {clase} "{titulo}"')
        while i < len(lineas) and re.match(rf"^{re.escape(sangria)}>( |$)", lineas[i]):
            contenido = re.sub(rf"^{re.escape(sangria)}> ?", "", lineas[i])
            salida.append(f"{sangria}    {contenido}" if contenido else "")
            i += 1
        salida.append("")
    return "\n".join(salida)


def on_page_markdown(markdown: str, **kwargs) -> str:  # noqa: D401 (firma de MkDocs)
    return convertir(markdown)
