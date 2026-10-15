---
modulo: M14
titulo: "Frameworks de agentes"
bloque: IV
nivel: general
horas_teoria: 12
horas_practica: 24
---

# Módulo 14 · Frameworks de agentes

**Etapa 4** · 36 h (12 h de teoría y 24 h de práctica) · 11 lecciones

## Objetivo

Construir agentes de calidad de producción con frameworks y SDK actuales, eligiendo con criterio entre ellos y entendiendo lo que abstraen.

## Qué vas a aprender

Qué resuelve un framework (y qué esconde); Claude Agent SDK; OpenAI Agents SDK; LangGraph; opciones Java (Spring AI 2.0, LangChain4j, Google ADK); runtimes gestionados; ejecución durable, checkpoints y reanudación; memoria a largo plazo; *guardrails*; *streaming* de eventos; despliegue.

## Antes de empezar

- **Prerrequisitos:** [Módulo 9](../m09-agentes-desde-cero/index.md) (indispensable), [Módulo 10](../m10-mcp/index.md) (recomendado).
- **Herramientas:** Python; Java 21+ con Spring Boot 4; API de modelos `[Pago]` o modelos locales con soporte de herramientas; Docker.

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 14.1 · Panorama y criterio

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L14.1.1 | **Qué aporta un framework**<br>Qué aporta un framework sobre tu agente de P5: estado, herramientas, memoria, trazas y despliegue. El costo de la abstracción. | Conceptual | Esencial | Próximamente |
| L14.1.2 | **Mapa de opciones y matriz de decisión**<br>Mapa de opciones vigente (Python, TypeScript y Java), su estado de mantenimiento y matriz de decisión. | Conceptual | Esencial | Próximamente |

### 14.2 · SDK de proveedores

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L14.2.1 | **Claude Agent SDK**<br>El *harness* de Claude Code como librería. Herramientas, permisos, subagentes y MCP. Referencia: el SDK de Codex como enfoque equivalente del otro proveedor `[Verificar alcance]`. | Práctica | Esencial | Próximamente |
| L14.2.2 | **OpenAI Agents SDK**<br>Agentes, *handoffs*, *guardrails* y sesiones. | Práctica | Esencial | Próximamente |
| L14.2.3 | **Runtimes gestionados**<br>Runtimes gestionados (por ejemplo Claude Managed Agents): cuándo delegar la infraestructura `[Pago]`. | Mixta | Profundizar | Próximamente |

### 14.3 · Frameworks de orquestación

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L14.3.1 | **LangGraph**<br>Grafos de estado, nodos, aristas condicionales, checkpoints e interrupciones para aprobación humana. | Práctica | Esencial | Próximamente |
| L14.3.2 | **Agentes en Java**<br>Spring AI 2.0 (bucle en la cadena de *advisors*, herramientas y MCP) y comparación con LangChain4j y Google ADK para Java. | Práctica | Profundizar | Próximamente |

### 14.4 · Calidad de producción

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L14.4.1 | **Ejecución durable**<br>Persistencia del estado, reintentos y reanudación tras fallos. | Práctica | Esencial | Próximamente |
| L14.4.2 | **Memoria a largo plazo**<br>Estrategias y almacenamiento. | Mixta | Profundizar | Próximamente |
| L14.4.3 | **Guardrails**<br>*Guardrails* de entrada y salida, validación y límites. | Práctica | Esencial | Próximamente |
| L14.4.4 | **Exponer un agente como servicio**<br>API, *streaming* de eventos, autenticación y despliegue en contenedor. | Práctica | Esencial | Próximamente |

## Práctica del módulo

- Guiado: reimplementar el agente de P5 con dos frameworks distintos y comparar.
- Guiado: agente con checkpoints que sobrevive a un reinicio.
- Independiente: agente en Spring AI expuesto como API REST.
- Desafío: misma funcionalidad en Claude Agent SDK y OpenAI Agents SDK; informe comparativo (código, costo, calidad y control).

## Proyecto o entregable

**Proyecto.** base de P9 (agentes de producción que se combinan en M15).

## Cómo se aprueba

Informe comparativo de frameworks con datos; agente desplegado como servicio con ejecución durable y aprobación humana; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 *guardrails* y autenticación del servicio · 📏 regresión al migrar de framework · 💰 costo por tarea · 🧭 framework vs. código propio vs. runtime gestionado.
