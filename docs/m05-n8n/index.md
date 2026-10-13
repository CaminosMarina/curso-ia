---
modulo: M5
titulo: "Automatización con n8n: workflows deterministas"
bloque: I
nivel: N1
horas_teoria: 5
horas_practica: 13
---

# M5 · Automatización con n8n: workflows deterministas

**Bloque I** · **Nivel 1 (usar y configurar)** · 18 h (5 h de teoría y 13 h de práctica) · 11 lecciones

## Objetivo

Construir automatizaciones robustas con n8n basadas en lógica determinista, integradas con API, bases de datos y servicios, como base para las automatizaciones con IA de M13.

## Qué vas a aprender

Conceptos de n8n (workflows, nodos, ítems, *triggers*, ejecuciones, credenciales, expresiones); autohospedaje con Docker; webhooks y API; transformación de datos; nodo de código y subworkflows; manejo de errores, reintentos e idempotencia; seguridad de n8n 2.x; modelo Guardar/Publicar y versionado; primer nodo LLM dentro de un flujo determinista.

## Antes de empezar

- **Prerrequisitos:** [M0](../m00-orientacion/index.md) (duro), [M2](../m02-prompt-engineering/index.md) (recomendado, solo para L5.3.3).
- **Herramientas:** n8n Community autohospedado en Docker (gratuito), PostgreSQL; para L5.3.3, Ollama o una API con nivel gratuito; n8n Cloud opcional `[Pago]`.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U5.1 · Fundamentos

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L5.1.1 | Qué es n8n y cuándo conviene frente a código propio u otras plataformas. Workflow determinista vs. agente (anticipo). | C | — |
| L5.1.2 | Instalación con Docker y PostgreSQL; estructura de una instancia. | P | — |
| L5.1.3 | Modelo de datos: ítems, JSON, expresiones y *mapping*. | P | — |
| L5.1.4 | *Triggers*: manual, programado, webhook y eventos de aplicaciones. | P | — |

### U5.2 · Integraciones

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L5.2.1 | Webhooks entrantes y salientes; nodo HTTP Request contra API REST propias. | P | — |
| L5.2.2 | Bases de datos, archivos y servicios (correo, calendario, GitHub, Slack o Telegram). | P | — |
| L5.2.3 | Credenciales y 🔒 seguridad de n8n 2.x: *task runners*, aislamiento del nodo de código, variables de entorno bloqueadas, nodos deshabilitados por defecto y gestión de secretos. | M | — |
| L5.2.4 | Nodo de código (JavaScript/Python), subworkflows y reutilización. | P | — |

### U5.3 · Robustez y primer paso con IA

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L5.3.1 | Manejo de errores: *error workflows*, reintentos, idempotencia y alertas. | P | — |
| L5.3.2 | Guardar vs. publicar, exportación y versionado de workflows en Git. | P | — |
| L5.3.3 | Primer nodo LLM dentro de un workflow determinista (clasificar o resumir), con 💰 control de costo y validación de la salida. | M | — |

## Práctica del módulo

- Guiado: webhook → transformación → base de datos → notificación.
- Guiado: workflow programado que consulta una API propia y genera un reporte.
- Independiente: integración entre dos servicios con manejo de errores e idempotencia.
- Desafío: clasificar con un LLM los ítems de un flujo y enrutar según el resultado, validando la salida.

## Proyecto o entregable

**Proyecto P2 · Sistema personal de trabajo con IA (parte C).** un workflow de n8n útil para tu trabajo, publicado, versionado en Git, con manejo de errores y al menos un paso con LLM validado.

## Cómo se aprueba

P2-C ≥ 80% en la rúbrica; evaluación de módulo ≥ 80%. (P2 queda aprobado globalmente cuando sus tres partes lo están, en cualquier orden.)

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 credenciales y webhooks públicos · 📏 casos de prueba de workflows · 💰 costo por ejecución · 🧭 n8n vs. script propio.
