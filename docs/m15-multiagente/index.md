---
modulo: M15
titulo: "Sistemas multiagente"
bloque: IV
nivel: general
horas_teoria: 10
horas_practica: 16
---

# M15 · Sistemas multiagente

**Bloque IV** · 26 h (10 h de teoría y 16 h de práctica) · 11 lecciones

## Objetivo

Diseñar sistemas donde varios agentes especializados colaboran, sabiendo cuándo esa complejidad está justificada.

## Qué vas a aprender

Motivos para usar varios agentes (paralelismo, aislamiento de contexto, especialización); topologías; comunicación y estado compartido; delegación con contexto suficiente; A2A (Agent Cards, tareas, interoperabilidad); evaluación y costos; fallos típicos.

## Antes de empezar

- **Prerrequisitos:** [M14](../m14-frameworks-agentes/index.md) (duro).
- **Herramientas:** Claude Agent SDK, LangGraph u OpenAI Agents SDK; SDK de A2A; subagentes de Claude Code.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U15.1 · Fundamentos

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L15.1.1 | 🧭 Cuándo varios agentes superan a uno (y cuándo no): evidencia, costos y la regla de "empezar con uno". | C | — |
| L15.1.2 | Topologías y patrones de coordinación. | C | — |
| L15.1.3 | Delegación efectiva entre agentes: qué contexto pasar, formato de resultados y criterios de terminación (versión programática de L3.7.1). | M | — |

### U15.2 · Implementación

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L15.2.1 | Orquestador-trabajadores con investigación en paralelo. | P | — |
| L15.2.2 | *Handoffs* entre agentes especializados y estado compartido. | P | — |
| L15.2.3 | Evaluador-optimizador y revisión cruzada entre agentes. | P | — |

### U15.3 · Interoperabilidad: A2A

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L15.3.1 | El protocolo A2A 1.0: Agent Cards (incluidas las firmadas), tareas, mensajes y artefactos. | C | — |
| L15.3.2 | Exponer y consumir un agente vía A2A; A2A + MCP en una misma arquitectura. | P | — |

### U15.4 · Operación

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L15.4.1 | 📏 Evaluar sistemas multiagente: éxito global, contribución de cada agente y trazas. | P | — |
| L15.4.2 | Fallos típicos: duplicación de trabajo, delegación vaga, bucles entre agentes y explosión de costos. 💰 Presupuestos por agente. | M | — |
| L15.4.3 | 🔒 Confianza entre agentes: propagación de *prompt injection*, identidad y permisos por agente. | M | — |

## Práctica del módulo

- Guiado: sistema de investigación con orquestador y 3 trabajadores.
- Independiente: dos agentes que se comunican vía A2A.
- Desafío: comparar con datos el mismo problema resuelto por un agente y por un sistema multiagente.

## Proyecto o entregable

**Proyecto P9 · Sistema multiagente.** por ejemplo, un equipo de revisión de software (seguridad, rendimiento y estilo, más un orquestador que consolida) o de investigación técnica, con trazas, presupuesto por agente, evals y comparación con la línea base de un solo agente.

## Cómo se aprueba

P9 ≥ 80% en la rúbrica con comparación cuantitativa; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 confianza entre agentes · 📏 evaluación de sistemas · 💰 presupuestos · 🧭 uno vs. varios agentes.
