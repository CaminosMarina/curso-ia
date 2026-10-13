---
modulo: M6
titulo: "Desarrollo con APIs de modelos"
bloque: II
nivel: general
horas_teoria: 10
horas_practica: 20
---

# M6 · Desarrollo con APIs de modelos

**Bloque II** · 30 h (10 h de teoría y 20 h de práctica) · 14 lecciones

## Objetivo

Integrar LLM en software propio mediante sus API, con salidas estructuradas, herramientas, manejo de errores, control de costos y portabilidad entre proveedores.

## Qué vas a aprender

Messages/Responses API; SDK de Python y Java; *streaming*; salidas estructuradas con JSON Schema; **tool calling** (herramientas ejecutadas por tu código y herramientas ejecutadas por el proveedor); manejo de errores, reintentos y límites de tasa; caché de prompts; *batch*; API compatibles con OpenAI y abstracciones multiproveedor; Spring AI.

## Antes de empezar

- **Prerrequisitos:** [M2](../m02-prompt-engineering/index.md) (duro), [M3](../m03-asistentes/index.md) (recomendado).
- **Herramientas:** Anthropic SDK, OpenAI SDK, Google GenAI SDK, Ollama (API compatible con OpenAI), Pydantic, Spring AI 2.0; crédito mínimo de API opcional `[Pago]` con límite de gasto (alternativas gratuitas: Ollama y nivel gratuito de Gemini).

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U6.1 · La API por dentro

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L6.1.1 | Anatomía de una llamada: endpoint, autenticación, modelo, mensajes, parámetros y respuesta. Lo que hace el SDK por vos (con `curl` primero). | P | — |
| L6.1.2 | Conversaciones sin estado: por qué el cliente reenvía el historial y qué implica en costo y diseño. Variantes con estado del lado del proveedor. | C | — |
| L6.1.3 | *Streaming* (SSE): cuándo usarlo y cómo procesarlo. | P | — |
| L6.1.4 | Comparativa de API: Anthropic Messages, OpenAI Responses y Gemini. Conceptos equivalentes y diferencias. | M | — |

### U6.2 · Salidas confiables

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L6.2.1 | Salidas estructuradas: JSON Schema, modo estricto, validación con Pydantic o Bean Validation. | P | — |
| L6.2.2 | Manejo de errores: límites de tasa, *timeouts*, reintentos con *backoff*, errores de contenido y respuestas truncadas. | P | — |
| L6.2.3 | Pruebas de código que llama a un LLM: *mocks*, *fixtures* grabadas y tests de contrato vs. evals. | P | — |

### U6.3 · Tool calling: el puente hacia los agentes

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L6.3.1 | Qué es tool calling: el modelo no ejecuta tu función, propone una llamada y tu código la ejecuta. El ciclo completo. | M | — |
| L6.3.2 | Diseño de herramientas: nombres, descripciones, esquemas y errores devueltos al modelo. | P | — |
| L6.3.3 | Llamadas paralelas, elección forzada de herramienta y herramientas ejecutadas por el proveedor (búsqueda web, ejecución de código): quién ejecuta qué y dónde. | M | — |
| L6.3.4 | 🔒 Riesgos de tool calling: validar argumentos, permisos mínimos y confirmación humana para acciones destructivas. | M | — |

### U6.4 · Costos, rendimiento y portabilidad

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L6.4.1 | 💰 Caché de prompts, procesamiento por lotes (*batch*) y selección de modelo por tarea. | P | — |
| L6.4.2 | Portabilidad: API compatibles con OpenAI, Ollama, routers (por ejemplo LiteLLM u OpenRouter) y el costo de la abstracción. | M | — |
| L6.4.3 | LLM en Java con Spring AI 2.0: `ChatClient`, *advisors*, salidas estructuradas y herramientas. | P | — |

## Práctica del módulo

- Guiado: la misma funcionalidad con `curl`, SDK de Python y Spring AI.
- Guiado: extracción de datos estructurados desde texto libre (por ejemplo, incidentes o logs) con validación.
- Independiente: herramienta de consulta a una base de datos propia mediante tool calling (solo lectura).
- Desafío: cliente multiproveedor con *fallback* automático y registro de costo por llamada.

## Proyecto o entregable

**Proyecto P3 · DevAssist CLI.** CLI (Python o Java) que resuelve tareas de desarrollo (resumir diffs, generar mensajes de *commit*, explicar errores) con salida estructurada, al menos una herramienta, soporte para dos proveedores (uno local), manejo de errores, tests y registro de tokens y costo. Reutiliza prompts de P1.

## Cómo se aprueba

P3 (versión base) ≥ 80% en la rúbrica; evaluación de módulo ≥ 80% incluyendo explicar el ciclo de tool calling.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 validación de argumentos y secretos · 📏 tests vs. evals · 💰 caché y *batch* · 🧭 SDK directo vs. abstracción.
