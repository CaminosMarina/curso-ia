# Formación Integral en Inteligencia Artificial

**De fundamentos a agentes y automatización avanzada.** Curso abierto, progresivo y autodidacta para aprender a usar, configurar, integrar y desarrollar soluciones con IA: modelos de lenguaje, prompt y context engineering, asistentes, agentes de programación, RAG, agentes, MCP, skills y plugins, n8n, sistemas multiagente y operación en producción.

### 📘 Leé el curso en **[caminosmarina.github.io/curso-ia](https://caminosmarina.github.io/curso-ia/)**

> [!WARNING]
> **En construcción.** El programa completo está disponible; el material de las lecciones se escribe de a un módulo por vez. Ver [estado de publicación](#estado-de-publicación).

## ¿Para quién es?

Para personas con **experiencia en programación** (idealmente backend: API REST, bases de datos, Python o Java) que **no tienen conocimientos previos de IA**. Está escrito en español rioplatense (voseo).

Es **autodidacta** e **interactivo**: cada lección tiene teoría clara y concisa, práctica paso a paso y una autoevaluación que se corrige al instante. El sitio guarda tu avance en tu navegador (*Mi progreso*) y tiene un mapa interactivo de la ruta. Un asistente de IA como tutor es opcional.

**Empezá por [Cómo empezar](docs/empezar/index.md)** (o en el [sitio](https://caminosmarina.github.io/curso-ia/empezar/)).

## Módulos

18 módulos en 5 etapas. El detalle de cada lección está en [Todas las lecciones](docs/ruta/lecciones.md); los principios y las horas, en [Sobre el curso](docs/sobre/index.md).

<!-- modulos:inicio -->
| Módulo | Etapa | Horas | Lecciones | Esenciales | Con material |
|---|:-:|---:|---:|---:|---:|
| [Módulo 0 · Orientación y entorno de trabajo](docs/m00-orientacion/index.md) | 1 | 6 | 4 | 4 | 4 |
| [Módulo 1 · Fundamentos de IA generativa y LLM](docs/m01-fundamentos-llm/index.md) | 1 | 24 | 16 | 13 | 4 |
| [Módulo 2 · Prompt Engineering](docs/m02-prompt-engineering/index.md) | 1 | 20 | 15 | 12 | 0 |
| [Módulo 3 · Asistentes de IA en la práctica](docs/m03-asistentes/index.md) | 1 | 36 | 25 | 20 | 0 |
| [Módulo 4 · Agentes de programación](docs/m04-agentes-programacion/index.md) | 1 | 21 | 14 | 11 | 0 |
| [Módulo 5 · Automatización con n8n](docs/m05-n8n/index.md) | 1 | 18 | 11 | 9 | 0 |
| [Módulo 6 · Desarrollo con APIs de modelos](docs/m06-apis-modelos/index.md) | 2 | 30 | 14 | 10 | 0 |
| [Módulo 7 · Context Engineering](docs/m07-context-engineering/index.md) | 2 | 20 | 11 | 9 | 0 |
| [Módulo 8 · Embeddings y RAG](docs/m08-rag/index.md) | 2 | 34 | 14 | 9 | 0 |
| [Módulo 9 · Agentes desde cero](docs/m09-agentes-desde-cero/index.md) | 3 | 30 | 13 | 11 | 0 |
| [Módulo 10 · Model Context Protocol (MCP)](docs/m10-mcp/index.md) | 3 | 32 | 16 | 12 | 0 |
| [Módulo 11 · Agentes de programación avanzados](docs/m11-agentes-programacion-avanzado/index.md) | 3 | 25 | 14 | 10 | 0 |
| [Módulo 12 · Desarrollo de skills y plugins](docs/m12-skills-plugins/index.md) | 3 | 18 | 10 | 7 | 0 |
| [Módulo 13 · n8n con IA y agentes](docs/m13-n8n-ia/index.md) | 4 | 24 | 10 | 9 | 0 |
| [Módulo 14 · Frameworks de agentes](docs/m14-frameworks-agentes/index.md) | 4 | 36 | 11 | 8 | 0 |
| [Módulo 15 · Sistemas multiagente](docs/m15-multiagente/index.md) | 4 | 26 | 11 | 8 | 0 |
| [Módulo 16 · Seguridad, evaluación y operación](docs/m16-produccion/index.md) | 5 | 36 | 16 | 13 | 0 |
| [Módulo 17 · Proyecto final integrador](docs/m17-proyecto-final/index.md) | 5 | 50 | 8 | 8 | 0 |
| **Total** | | **486** | **233** | **183** | **8** |
<!-- modulos:fin -->

Además: tres [electivas](docs/ruta/electivas.md) y diez [proyectos](docs/ruta/proyectos.md).

## Estado de publicación

**Versión académica del programa:** 1.3.1 · **Versión de publicación:** sin publicar. La primera, `v0.1.0`, sale cuando M0 esté completo y revisado. Estados editoriales de una lección: 📝 borrador · 🔍 revisada · 📗 publicada. Cambios en [`CHANGELOG.md`](CHANGELOG.md).

## Cómo está organizado el repositorio

| Carpeta o archivo | Contenido |
|---|---|
| [`docs/`](docs/) | Todo el curso en Markdown; es lo que se publica como sitio |
| [`docs/mNN-*/`](docs/m00-orientacion/) | Un módulo: su portada (`index.md`), una página por lección, `soluciones/` e `img/` |
| [`docs/ruta/`](docs/ruta/) | Ruta de aprendizaje, todas las lecciones, proyectos y electivas |
| [`docs/sobre/`](docs/sobre/) | Principios del programa, cómo se aprueba y versiones |
| `docs/assets/` | Estilo Latte, funciones interactivas (`curso.js`, `curso.css`) y logo |
| [`plantillas/`](plantillas/) | Plantillas de lección y de evaluación, y el **cuaderno del estudiante** |
| [`scripts/`](scripts/) | `generar.py` (índice, menú y tablas) y `verificar.py` (consistencia y privacidad) |
| `mkdocs.yml`, `hooks/`, `overrides/`, `requirements.txt` | Configuración del sitio |

**Vista previa local del sitio:** `pip install -r requirements.txt` y después `mkdocs serve`.

## Licencias

| Material | Licencia | Archivo |
|---|---|---|
| Contenido educativo original: programa, lecciones, ejercicios, evaluaciones, soluciones, glosario, plantillas y guías | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es) | [`LICENSE`](LICENSE) |
| Código y scripts originales: `scripts/`, `hooks/`, `docs/assets/curso.js` y fragmentos de código de las lecciones | [MIT](https://opensource.org/license/mit) | [`LICENSE-CODE`](LICENSE-CODE) |

Estas licencias cubren **solo el material original**. El material de terceros conserva su licencia y se identifica junto con su fuente.

**Atribución sugerida:** "Formación Integral en Inteligencia Artificial", de Marina Caminos, CC BY-SA 4.0, con enlace a este repositorio.

## Autoría y uso de IA

Autoría: **Marina Caminos**.

Este material se redacta y revisa con asistencia de herramientas de IA. Cada lección pasa por revisión humana antes de publicarse: verificación de las afirmaciones técnicas en fuentes oficiales, ejecución de los ejercicios desde cero y revisión pedagógica.

## Privacidad

Este repositorio no contiene ni debe contener datos de estudiantes: ni progreso, ni respuestas, ni credenciales. Si encontrás información personal o una credencial publicada por error, no la difundas: avisá a la persona que mantiene el repositorio.

## Contribuciones

Por ahora no se aceptan contribuciones externas.
