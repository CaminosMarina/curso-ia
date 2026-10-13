---
modulo: M13
titulo: "n8n con IA y agentes"
bloque: IV
nivel: N2
horas_teoria: 7
horas_practica: 17
---

# M13 · n8n con IA y agentes

**Bloque IV** · **Nivel 2 (construir y profundizar)** · 24 h (7 h de teoría y 17 h de práctica) · 10 lecciones

## Objetivo

Diseñar automatizaciones de producción en n8n que combinan lógica determinista, LLM, agentes, RAG y MCP, con supervisión humana y control de costos.

## Qué vas a aprender

Nodos de LLM con salida estructurada; patrones de workflows con LLM aplicados en n8n; nodo AI Agent (modelo, memoria y herramientas, incluidos workflows como herramientas); aprobación humana; RAG en n8n; MCP en n8n (MCP Client Tool y MCP Server Trigger); monitoreo, costos y límites; escalado y entornos.

## Antes de empezar

- **Prerrequisitos:** [M5](../m05-n8n/index.md), [M6](../m06-apis-modelos/index.md) y [M9](../m09-agentes-desde-cero/index.md) (duros); [M8](../m08-rag/index.md) y [M10](../m10-mcp/index.md) (recomendados, para L13.3.1 y L13.3.2).
- **Herramientas:** n8n Community autohospedado, PostgreSQL + pgvector, Ollama o API de LLM.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U13.1 · LLM en workflows

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L13.1.1 | Nodos de LLM con salida estructurada y validación: clasificación, extracción y resumen (amplía L5.3.3). | P | — |
| L13.1.2 | Patrones de workflows con LLM en n8n: encadenamiento, enrutamiento, paralelización y evaluador-optimizador (mapeo con L9.1.3). | M | — |

### U13.2 · Agentes en n8n

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L13.2.1 | Nodo AI Agent: modelo, memoria y herramientas. Mapeo con el bucle de M9. | M | — |
| L13.2.2 | Herramientas del agente: nodos, HTTP y workflows como herramientas. | P | — |
| L13.2.3 | Aprobación humana dentro de workflows (esperar confirmación por correo o chat). | P | — |

### U13.3 · Conocimiento e integración

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L13.3.1 | RAG en n8n: ingesta a un vector store y agente con recuperación. | P | — |
| L13.3.2 | MCP en n8n: consumir servidores MCP (MCP Client Tool) y exponer workflows como servidor MCP (MCP Server Trigger). | P | — |

### U13.4 · Operación

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L13.4.1 | Monitoreo de ejecuciones, 💰 costos de LLM y límites. | P | — |
| L13.4.2 | Escalado y entornos: modo cola, réplicas y consideraciones para endpoints MCP `[Verificar]`. | M | — |
| L13.4.3 | 🧭 Workflow determinista + LLM puntual vs. agente autónomo; n8n vs. código propio. | C | — |

## Práctica del módulo

- Guiado: clasificación y extracción con LLM de correos o issues entrantes, con validación.
- Guiado: agente en n8n con dos herramientas y memoria.
- Independiente: agente en n8n que usa tu servidor MCP de P6.
- Desafío: workflow con manejo completo de errores, idempotencia y aprobación humana.

## Proyecto o entregable

**Proyecto P8 · Automatización inteligente con n8n.** evolución del workflow de P2-C hacia un proceso de producción real (por ejemplo, triage de issues o correos con clasificación, enriquecimiento vía RAG, acción propuesta por un agente, aprobación humana y ejecución), con manejo de errores, registro de costos, versionado en Git y documentación.

## Cómo se aprueba

P8 ≥ 80% en la rúbrica con casos de error probados; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 credenciales, webhooks públicos, aislamiento · 📏 casos de prueba de workflows · 💰 costo por ejecución · 🧭 workflow vs. agente.
