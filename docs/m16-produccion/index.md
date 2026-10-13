---
modulo: M16
titulo: "Seguridad, evaluación, observabilidad y operación"
bloque: V
nivel: general
horas_teoria: 14
horas_practica: 22
---

# M16 · Seguridad, evaluación, observabilidad y operación en producción

**Bloque V** · 36 h (14 h de teoría y 22 h de práctica) · 16 lecciones

## Objetivo

Consolidar y profundizar las prácticas que hacen que un sistema de IA sea seguro, medible, observable, económico y mantenible en producción.

## Qué vas a aprender

Modelado de amenazas para sistemas con LLM; OWASP Top 10 LLM 2026 y Top 10 de aplicaciones agénticas; defensa en profundidad contra *prompt injection*; identidad y credenciales de agentes; privacidad; evals automatizadas e integración continua; LLM como juez; observabilidad con OpenTelemetry y herramientas LLMOps; depuración de agentes; optimización de costo y latencia; confiabilidad; mantenimiento ante deprecaciones.

## Antes de empezar

- **Prerrequisitos:** [M13](../m13-n8n-ia/index.md) y [M14](../m14-frameworks-agentes/index.md) (duros); [M12](../m12-skills-plugins/index.md) y [M15](../m15-multiagente/index.md) (recomendados).
- **Herramientas:** promptfoo, Langfuse autohospedado o Arize Phoenix, OpenTelemetry, escáneres de secretos, herramientas de *red teaming*.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U16.1 · Seguridad

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L16.1.1 | Modelado de amenazas para aplicaciones y agentes con LLM: activos, fronteras de confianza y la "tríada letal" (datos privados + contenido no confiable + capacidad de comunicación externa). | M | — |
| L16.1.2 | OWASP Top 10 LLM 2026 y Top 10 de aplicaciones agénticas: recorrido con ejemplos sobre tus proyectos. | M | — |
| L16.1.3 | Defensa contra *prompt injection*: por qué no hay solución completa; aislamiento, permisos, confirmación humana y separación de privilegios. | M | — |
| L16.1.4 | Identidad y credenciales de agentes: secretos, tokens de corta duración y permisos mínimos por herramienta. | P | — |
| L16.1.5 | Privacidad: datos personales, minimización, anonimización y retención en proveedores. | C | — |

### U16.2 · Evaluación

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L16.2.1 | Estrategia de evaluación: tipos (deterministas, basados en modelo, humanos) y qué medir en cada tipo de sistema. | C | — |
| L16.2.2 | LLM como juez: diseño de rúbricas, calibración con humanos y sesgos. | P | — |
| L16.2.3 | Evals en integración continua: regresión al cambiar prompts, modelos o herramientas. | P | — |
| L16.2.4 | *Red teaming* y evaluación adversarial. | P | — |

### U16.3 · Observabilidad y depuración

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L16.3.1 | Trazas de LLM y agentes con OpenTelemetry: spans, atributos y convenciones. | P | — |
| L16.3.2 | Plataformas LLMOps (Langfuse o Phoenix): trazas, *datasets*, evaluaciones en línea y *feedback*. | P | — |
| L16.3.3 | Depurar agentes: leer trayectorias, reproducir fallos y análisis de errores sistemático. | P | — |

### U16.4 · Costos, confiabilidad y mantenimiento

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L16.4.1 | 💰 Optimización: enrutamiento por modelo, caché, *batch*, compresión de contexto y presupuestos. | P | — |
| L16.4.2 | Confiabilidad: *fallbacks* entre proveedores, límites de tasa, *timeouts* y degradación controlada. | P | — |
| L16.4.3 | Mantenimiento: deprecación de modelos, API y herramientas (casos reales: Assistants API, Agent Builder), migraciones y deriva. | M | — |
| L16.4.4 | Gobernanza mínima: registro de decisiones, auditoría y documentación de sistemas de IA. | C | — |

## Práctica del módulo

- Guiado: modelo de amenazas completo de P8 o P9.
- Guiado: instrumentar P5 o P9 con OpenTelemetry y Langfuse o Phoenix.
- Independiente: suite de evals en CI para P4 con umbrales que bloquean regresiones.
- Desafío: *red teaming* sobre tus propios proyectos y plan de remediación.

## Proyecto o entregable

**Actividad integradora (no es proyecto numerado).** auditoría de producción de P4, P8 y P9: modelo de amenazas, evals en CI, instrumentación, costos y plan de remediación.

## Cómo se aprueba

Actividad integradora revisada; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

todos, en profundidad.
