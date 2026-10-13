---
modulo: M17
titulo: "Proyecto final integrador"
bloque: V
nivel: general
horas_teoria: 5
horas_practica: 45
---

# M17 · Proyecto final integrador

**Bloque V** · 50 h (5 h de teoría y 45 h de práctica) · 8 lecciones

## Objetivo

Diseñar, construir, evaluar y documentar una solución completa que integre los conocimientos del curso, con calidad profesional.

## Antes de empezar

- **Prerrequisitos:** [M16](../m16-produccion/index.md) (duro).
- **Herramientas:** a elección, justificadas.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U17.1 · Diseño

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L17.1.1 | Elección del problema y definición de requisitos, métricas de éxito y restricciones (costo, privacidad). | M | — |
| L17.1.2 | Arquitectura y decisiones técnicas documentadas (ADR): qué es determinista, qué es agente, qué es RAG, qué es MCP y qué es n8n. | M | — |
| L17.1.3 | Modelo de amenazas y plan de evaluación antes de construir. | M | — |

### U17.2 · Construcción

Iterativa, con revisión en cada hito: tutor, par o autoevaluación con la rúbrica.

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L17.2.1 | Hito 1: núcleo funcional mínimo con evals. | P | — |
| L17.2.2 | Hito 2: integraciones (MCP, n8n y datos). | P | — |
| L17.2.3 | Hito 3: seguridad, observabilidad y costos. | P | — |

### U17.3 · Cierre

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L17.3.1 | Evaluación final, informe de métricas y análisis de costos. | P | — |
| L17.3.2 | Documentación, demostración y retrospectiva. | M | — |

## Proyecto o entregable

**Proyecto P10 · Proyecto final integrador. Opciones (o una propia):**

- **A · Asistente personal de ingeniería:** agente con RAG sobre tus repositorios y documentación, servidores MCP propios hacia tus herramientas, skills de tu flujo de trabajo y automatizaciones n8n, con evals y observabilidad.
- **B · Plataforma de automatización para un dominio:** sistema multiagente con n8n como orquestador de eventos, agentes especializados, aprobación humana y panel de costos.
- **C · Producto de IA en Java:** servicio Spring AI con agente, RAG sobre pgvector, servidor MCP propio, interoperabilidad A2A y despliegue en contenedor con CI de evals.

## Cómo se aprueba

P10 ≥ 80% en la rúbrica; demostración funcional; documentación que permita a otra persona entender, ejecutar y mantener el sistema.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).
