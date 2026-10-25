# Sobre el curso

> [!NOTE]
> **Versión académica 1.3.1** (24/10/2026) · 5 etapas · 18 módulos · 233 lecciones (183 en la ruta esencial) · 10 proyectos · 486 h, unas 390 h en la ruta esencial (526 h con electivas).

Esta sección explica cómo está pensado el curso: sus principios, cuánto tiempo lleva y qué vas a poder hacer al terminar. Para recorrerlo, usá la [Ruta](../ruta/index.md).

| Página | Qué contiene |
|---|---|
| [Cómo se aprueba](evaluacion.md) | Cuándo una lección, un módulo o un proyecto están completos |
| [Versiones y cambios](versiones.md) | Cómo cambia el programa y qué hacer con tu avance |

## Principios de diseño

1. **Usar con criterio antes de construir.** Cada herramienta importante se aprende primero a usar y configurar (Nivel 1) y después a desarrollar (Nivel 2). Ver [Nivel 1 y Nivel 2](#usar-antes-de-construir-nivel-1-y-nivel-2).
2. **Modelo mental antes que receta.** Se explica qué resuelve cada herramienta, cómo funciona por dentro y cuándo no conviene, para que puedas evaluar herramientas nuevas sin depender de tutoriales.
3. **Concepto general, después implementación.** Se separa lo transferible (por ejemplo, *tool calling*) de cómo lo implementa cada plataforma. No se atribuye a una herramienta una función sin verificarla en su documentación.
4. **Desde cero antes que frameworks.** Primero un agente con un bucle propio y un servidor MCP con el SDK; después, los frameworks y las abstracciones de alto nivel.
5. **Multiplataforma y estándares abiertos.** Las prácticas usan Claude y ChatGPT (asistentes) y Claude Code y Codex (agentes de programación), con Gemini y modelos locales donde aportan. Se priorizan los estándares abiertos (MCP, Agent Skills, AGENTS.md, A2A, OpenTelemetry). Una actividad se repite en otra plataforma solo si la comparación enseña una diferencia técnica; si no, las plataformas se alternan. Ninguna herramienta entra solo por ser popular, y el tutor de IA es opcional.
6. **Seguridad, evaluación y costos desde el inicio**, en todos los módulos.
7. **Python como lenguaje principal y Java como segundo lenguaje** en los módulos de integración (M6, M8 opcional, M10 y M14).
8. **Gratis o barato por defecto.** Ollama, niveles gratuitos de API, n8n y pgvector autohospedados. Lo pago se avisa siempre.

## Usar antes de construir: Nivel 1 y Nivel 2

| Herramienta o capacidad | Nivel 1: utilización y configuración | Nivel 2: desarrollo y profundización |
|---|---|---|
| Asistentes (Claude, ChatGPT, Gemini) | **M3** | Base conceptual en M6, M7 y M9 |
| Proyectos, instrucciones, memoria y contexto | **M3** (como persona usuaria) | **M7** Context Engineering |
| Connectors y servidores MCP | **M3** (conectar y configurar existentes) | **M10** (construir servidores y clientes) |
| Skills y plugins | **M3** y **M4** (instalar, usar, evaluar, revisar) | **M11** (primera skill propia en el agente de programación) y **M12** (crear, empaquetar, distribuir) |
| Agentes de programación (**Claude Code y Codex**; Gemini CLI u OpenCode como opciones locales) | **M4** (uso guiado y configuración básica de ambos) | **M11** (arquitectura, permisos, MCP, skills, automatización y CI en ambos) |
| Automatización con n8n | **M5** (workflows deterministas) | **M13** (LLM, agentes, RAG y MCP en n8n) |
| Delegación de tareas complejas | **M3** y **M4** (especificar, supervisar, verificar) | **M9**, **M14** y **M15** (construir agentes que delegan) |
| Multimodalidad y agentes de computadora/navegador | **M3** (usar con criterio y seguridad) | Electiva **E1** (desarrollar) |

**Regla pedagógica:** un módulo de Nivel 2 empieza repasando en 15 minutos lo usado en Nivel 1 y después "abre la caja": cómo está construido, cómo construir un equivalente propio y cuándo conviene cada opción.

## Mapa de aprendizaje

El mapa interactivo de módulos y prerrequisitos está en [Ruta](../ruta/index.md).

## Módulos y horas

Las horas son estimaciones realistas para estudio autónomo con práctica real (no lectura pasiva). Incluyen ejercicios y proyectos.

| # | Módulo | Nivel | Lecciones | Teoría | Práctica | Total |
|---|---|:-:|---:|---:|---:|---:|
| M0 | [Orientación y entorno de trabajo](../m00-orientacion/index.md) | — | 4 | 2 | 4 | 6 |
| M1 | [Fundamentos de IA generativa y LLM](../m01-fundamentos-llm/index.md) | — | 16 | 12 | 12 | 24 |
| M2 | [Prompt Engineering](../m02-prompt-engineering/index.md) | — | 15 | 8 | 12 | 20 |
| M3 | [Asistentes de IA en la práctica](../m03-asistentes/index.md) | N1 | 25 | 11 | 25 | 36 |
| M4 | [Agentes de programación](../m04-agentes-programacion/index.md) | N1 | 14 | 5 | 16 | 21 |
| M5 | [Automatización con n8n](../m05-n8n/index.md) | N1 | 11 | 5 | 13 | 18 |
| M6 | [Desarrollo con APIs de modelos](../m06-apis-modelos/index.md) | — | 14 | 10 | 20 | 30 |
| M7 | [Context Engineering](../m07-context-engineering/index.md) | N2 | 11 | 8 | 12 | 20 |
| M8 | [Embeddings y RAG](../m08-rag/index.md) | — | 14 | 12 | 22 | 34 |
| M9 | [Agentes desde cero](../m09-agentes-desde-cero/index.md) | — | 13 | 12 | 18 | 30 |
| M10 | [Model Context Protocol (MCP)](../m10-mcp/index.md) | N2 | 16 | 11 | 21 | 32 |
| M11 | [Agentes de programación avanzados](../m11-agentes-programacion-avanzado/index.md) | N2 | 14 | 7 | 18 | 25 |
| M12 | [Desarrollo de skills y plugins](../m12-skills-plugins/index.md) | N2 | 10 | 5 | 13 | 18 |
| M13 | [n8n con IA y agentes](../m13-n8n-ia/index.md) | N2 | 10 | 7 | 17 | 24 |
| M14 | [Frameworks de agentes](../m14-frameworks-agentes/index.md) | — | 11 | 12 | 24 | 36 |
| M15 | [Sistemas multiagente](../m15-multiagente/index.md) | — | 11 | 10 | 16 | 26 |
| M16 | [Seguridad, evaluación y operación](../m16-produccion/index.md) | — | 16 | 14 | 22 | 36 |
| M17 | [Proyecto final integrador](../m17-proyecto-final/index.md) | — | 8 | 5 | 45 | 50 |
| | **Núcleo obligatorio** | | **233** | **156** | **330** | **486** |
| E1 | [Multimodalidad avanzada y agentes de computadora/navegador](../ruta/electivas.md) | N2 | — | 4 | 8 | 12 |
| E2 | [Modelos abiertos, ejecución local y fine-tuning](../ruta/electivas.md) | — | — | 8 | 14 | 22 |
| E3 | [Ética, marco legal y gobernanza de IA](../ruta/electivas.md) | — | — | 5 | 1 | 6 |
| | **Total con electivas** | | | **173** | **353** | **526** |

Las electivas no tienen lecciones numeradas: su desglose se define al elegirlas.

**Margen realista:** sumá alrededor de un 10% para repasos espaciados, refuerzos y actualizaciones del ecosistema: **unas 580 horas** con electivas.

| Dedicación semanal | Núcleo (486 h) | Con electivas y margen (~580 h) |
|---|---|---|
| 6 h/semana | ~19 meses | ~22 meses |
| 10 h/semana | ~11 meses | ~13 meses |
| 15 h/semana | ~7,5 meses | ~9 meses |

## Hilos transversales

| Hilo | Qué se trabaja en cada módulo |
|---|---|
| 🔒 **Seguridad y privacidad** | Qué datos entran al modelo, manejo de credenciales, permisos mínimos y amenazas específicas del tema. |
| 📏 **Evaluación** | Cómo saber si funciona: desde comparar resultados a mano (M2, M3) hasta suites de evals automatizadas (M16). |
| 💰 **Costos y rendimiento** | Tokens, latencia, planes, elección de modelo y caché. Cada proyecto registra su costo. |
| 🧭 **Criterio técnico** | Cuándo usar esto, cuándo no y qué alternativas hay. Cada módulo cierra con una "matriz de decisión". |

## Perfil de egreso

**Uso profesional**
- Usar con eficacia, seguridad y criterio asistentes (Claude, ChatGPT, Gemini y opciones locales), agentes de programación (Claude Code y Codex) y automatizaciones, configurando proyectos, memoria, connectors, servidores MCP, skills y plugins en cada plataforma.
- Delegar tareas complejas con especificación clara, supervisión y verificación de resultados.

**Comprensión**
- Explicar cómo funciona un LLM (tokens, atención, contexto, muestreo, entrenamiento) y usar ese modelo mental para predecir y diagnosticar comportamientos.
- Distinguir modelo, producto, *harness*, workflow, agente y sistema multiagente.

**Diseño y criterio**
- Elegir entre prompt, RAG, herramientas, agente, workflow, *fine-tuning* o una combinación, justificando costo, riesgo y beneficio.
- Elegir plataformas, modelos, frameworks y mecanismos de extensión (skill, MCP, subagente, hook, plugin o A2A) con criterios explícitos, y evaluar herramientas nuevas sin depender de tutoriales.

**Construcción**
- Integrar LLM en software propio (Python y Java) con salidas estructuradas, tool calling, manejo de errores y portabilidad.
- Diseñar y gestionar el contexto; construir RAG evaluado; construir agentes desde cero y con frameworks; construir y desplegar servidores y clientes MCP; crear y distribuir skills y plugins; automatizar procesos con n8n combinando lógica determinista, LLM y agentes; diseñar sistemas multiagente cuando estén justificados.

**Producción**
- Modelar amenazas y mitigar los riesgos del OWASP Top 10 LLM y agéntico; gestionar credenciales, permisos y privacidad.
- Diseñar suites de evaluación e integrarlas en CI; instrumentar sistemas con trazas y medir costo, latencia y calidad.
- Mantener sistemas ante cambios de modelos, API y especificaciones.
