# Formación Integral en Inteligencia Artificial

**De fundamentos a agentes y automatización avanzada.** Curso abierto, progresivo y autodidacta para aprender a usar, configurar, integrar y desarrollar soluciones con IA: modelos de lenguaje, prompt y context engineering, asistentes, agentes de programación, RAG, agentes, MCP, skills y plugins, n8n, sistemas multiagente y operación en producción.

### 📘 Leé el curso en **[caminosmarina.github.io/curso-ia](https://caminosmarina.github.io/curso-ia/)**

> [!WARNING]
> **En construcción.** El programa completo está disponible; el material de las lecciones se escribe de a un módulo por vez. Ver [estado de publicación](#estado-de-publicación).

## ¿Para quién es?

Para personas con **experiencia en programación** (idealmente backend: API REST, bases de datos, Python o Java) que **no tienen conocimientos previos de IA**. Está escrito en español rioplatense (voseo).

Es **autodidacta**: cada lección tiene teoría clara y concisa, práctica paso a paso cuando hace falta y una autoevaluación con soluciones aparte. Un asistente de IA como tutor es opcional. Tu progreso lo llevás en un **cuaderno privado**, fuera de este repositorio.

**Empezá por [Cómo empezar](docs/empezar/index.md)** (o en el [sitio](https://caminosmarina.github.io/curso-ia/empezar/)).

## Módulos

18 módulos en 5 bloques. El detalle de cada lección está en el [índice de lecciones](docs/programa/indice.md); el mapa de dependencias y las horas, en [El programa](docs/programa/index.md).

<!-- modulos:inicio -->
| Módulo | Bloque | Horas | Lecciones | Con material |
|---|:-:|---:|---:|---:|
| [M0 · Orientación, entorno y método](docs/m00-orientacion/index.md) | I | 6 | 4 | 1 |
| [M1 · Fundamentos de IA generativa y LLM](docs/m01-fundamentos-llm/index.md) | I | 24 | 16 | 0 |
| [M2 · Prompt Engineering](docs/m02-prompt-engineering/index.md) | I | 20 | 15 | 0 |
| [M3 · Asistentes de IA: uso profesional, contexto y delegación](docs/m03-asistentes/index.md) | I | 36 | 25 | 0 |
| [M4 · Agentes de programación: uso guiado](docs/m04-agentes-programacion/index.md) | I | 21 | 14 | 0 |
| [M5 · Automatización con n8n: workflows deterministas](docs/m05-n8n/index.md) | I | 18 | 11 | 0 |
| [M6 · Desarrollo con APIs de modelos](docs/m06-apis-modelos/index.md) | II | 30 | 14 | 0 |
| [M7 · Context Engineering](docs/m07-context-engineering/index.md) | II | 20 | 11 | 0 |
| [M8 · Embeddings, búsqueda semántica y RAG](docs/m08-rag/index.md) | II | 34 | 14 | 0 |
| [M9 · Agentes desde cero](docs/m09-agentes-desde-cero/index.md) | III | 30 | 13 | 0 |
| [M10 · Model Context Protocol: desarrollo](docs/m10-mcp/index.md) | III | 32 | 16 | 0 |
| [M11 · Agentes de programación: arquitectura y configuración avanzada](docs/m11-agentes-programacion-avanzado/index.md) | III | 25 | 14 | 0 |
| [M12 · Skills y plugins: desarrollo](docs/m12-skills-plugins/index.md) | III | 18 | 10 | 0 |
| [M13 · n8n con IA y agentes](docs/m13-n8n-ia/index.md) | IV | 24 | 10 | 0 |
| [M14 · Frameworks y SDK de agentes para producción](docs/m14-frameworks-agentes/index.md) | IV | 36 | 11 | 0 |
| [M15 · Sistemas multiagente](docs/m15-multiagente/index.md) | IV | 26 | 11 | 0 |
| [M16 · Seguridad, evaluación, observabilidad y operación](docs/m16-produccion/index.md) | V | 36 | 16 | 0 |
| [M17 · Proyecto final integrador](docs/m17-proyecto-final/index.md) | V | 50 | 8 | 0 |
| **Núcleo** | | **486** | **233** | **1** |
<!-- modulos:fin -->

Además: tres [electivas](docs/electivas.md) y diez [proyectos](docs/programa/proyectos.md).

## Estado de publicación

**Versión académica del programa:** 1.2 · **Versión de publicación:** sin publicar. La primera, `v0.1.0`, sale cuando M0 esté completo y revisado. Estados editoriales de una lección: 📝 borrador · 🔍 revisada · 📗 publicada. Cambios en [`CHANGELOG.md`](CHANGELOG.md).

## Cómo está organizado el repositorio

| Carpeta o archivo | Contenido |
|---|---|
| [`docs/`](docs/) | Todo el curso en Markdown; es lo que se publica como sitio |
| [`docs/mNN-*/`](docs/m00-orientacion/) | Un módulo: su portada (`index.md`), una página por lección, `soluciones/` e `img/` |
| [`docs/programa/`](docs/programa/) | Programa, índice de lecciones, proyectos, evaluación y versiones |
| [`plantillas/`](plantillas/) | Plantillas de lección y de evaluación, y el **cuaderno del estudiante** |
| [`scripts/`](scripts/) | `generar.py` (índice, menú y tablas) y `verificar.py` (consistencia y privacidad) |
| `mkdocs.yml`, `hooks/`, `requirements.txt` | Configuración del sitio |

**Vista previa local del sitio:** `pip install -r requirements.txt` y después `mkdocs serve`.

## Licencias

| Material | Licencia | Archivo |
|---|---|---|
| Contenido educativo original: programa, lecciones, ejercicios, evaluaciones, soluciones, glosario, plantillas y guías | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es) | [`LICENSE`](LICENSE) |
| Código y scripts originales: `scripts/`, `hooks/` y fragmentos de código de las lecciones | [MIT](https://opensource.org/license/mit) | [`LICENSE-CODE`](LICENSE-CODE) |

Estas licencias cubren **solo el material original**. El material de terceros conserva su licencia y se identifica junto con su fuente.

**Atribución sugerida:** "Formación Integral en Inteligencia Artificial", de Marina Caminos, CC BY-SA 4.0, con enlace a este repositorio.

## Autoría y uso de IA

Autoría: **Marina Caminos**.

Este material se redacta y revisa con asistencia de herramientas de IA. Cada lección pasa por revisión humana antes de publicarse: verificación de las afirmaciones técnicas en fuentes oficiales, ejecución de los ejercicios desde cero y revisión pedagógica.

## Privacidad

Este repositorio no contiene ni debe contener datos de estudiantes: ni progreso, ni respuestas, ni credenciales. Si encontrás información personal o una credencial publicada por error, no la difundas: avisá a la persona que mantiene el repositorio.

## Contribuciones

Por ahora no se aceptan contribuciones externas.
