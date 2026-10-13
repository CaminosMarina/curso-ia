---
modulo: M14
titulo: "Frameworks y SDK de agentes para producción"
bloque: IV
nivel: general
horas_teoria: 12
horas_practica: 24
---

# M14 · Frameworks y SDK de agentes para producción

**Bloque IV** · 36 h (12 h de teoría y 24 h de práctica) · 11 lecciones

## Objetivo

Construir agentes de calidad de producción con frameworks y SDK actuales, eligiendo con criterio entre ellos y entendiendo lo que abstraen.

## Qué vas a aprender

Qué resuelve un framework (y qué esconde); Claude Agent SDK; OpenAI Agents SDK; LangGraph; opciones Java (Spring AI 2.0, LangChain4j, Google ADK); runtimes gestionados; ejecución durable, checkpoints y reanudación; memoria a largo plazo; *guardrails*; *streaming* de eventos; despliegue.

## Antes de empezar

- **Prerrequisitos:** [M9](../m09-agentes-desde-cero/index.md) (duro), [M10](../m10-mcp/index.md) (recomendado).
- **Herramientas:** Python; Java 21+ con Spring Boot 4; API de modelos `[Pago]` o modelos locales con soporte de herramientas; Docker.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U14.1 · Panorama y criterio

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L14.1.1 | Qué aporta un framework sobre tu agente de P5: estado, herramientas, memoria, trazas y despliegue. El costo de la abstracción. | C | — |
| L14.1.2 | 🧭 Mapa de opciones vigente (Python, TypeScript y Java), su estado de mantenimiento y matriz de decisión. | C | — |

### U14.2 · SDK de proveedores

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L14.2.1 | Claude Agent SDK: el *harness* de Claude Code como librería. Herramientas, permisos, subagentes y MCP. Referencia: el SDK de Codex como enfoque equivalente del otro proveedor `[Verificar alcance]`. | P | — |
| L14.2.2 | OpenAI Agents SDK: agentes, *handoffs*, *guardrails* y sesiones. | P | — |
| L14.2.3 | Runtimes gestionados (por ejemplo Claude Managed Agents): cuándo delegar la infraestructura `[Pago]`. | M | — |

### U14.3 · Frameworks de orquestación

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L14.3.1 | LangGraph: grafos de estado, nodos, aristas condicionales, checkpoints e interrupciones para aprobación humana. | P | — |
| L14.3.2 | Agentes en Java: Spring AI 2.0 (bucle en la cadena de *advisors*, herramientas y MCP) y comparación con LangChain4j y Google ADK para Java. | P | — |

### U14.4 · Calidad de producción

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L14.4.1 | Ejecución durable: persistencia del estado, reintentos y reanudación tras fallos. | P | — |
| L14.4.2 | Memoria a largo plazo: estrategias y almacenamiento. | M | — |
| L14.4.3 | *Guardrails* de entrada y salida, validación y límites. | P | — |
| L14.4.4 | Exponer un agente como servicio: API, *streaming* de eventos, autenticación y despliegue en contenedor. | P | — |

## Práctica del módulo

- Guiado: reimplementar el agente de P5 con dos frameworks distintos y comparar.
- Guiado: agente con checkpoints que sobrevive a un reinicio.
- Independiente: agente en Spring AI expuesto como API REST.
- Desafío: misma funcionalidad en Claude Agent SDK y OpenAI Agents SDK; informe comparativo (código, costo, calidad y control).

## Proyecto o entregable

**Proyecto.** base de P9 (agentes de producción que se combinan en M15).

## Cómo se aprueba

Informe comparativo de frameworks con datos; agente desplegado como servicio con ejecución durable y aprobación humana; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 *guardrails* y autenticación del servicio · 📏 regresión al migrar de framework · 💰 costo por tarea · 🧭 framework vs. código propio vs. runtime gestionado.
