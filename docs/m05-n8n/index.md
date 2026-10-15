---
modulo: M5
titulo: "Automatización con n8n"
bloque: I
nivel: N1
horas_teoria: 5
horas_practica: 13
---

# Módulo 5 · Automatización con n8n

**Etapa 1** · **Nivel 1 (usar y configurar)** · 18 h (5 h de teoría y 13 h de práctica) · 11 lecciones

## Objetivo

Construir automatizaciones robustas con n8n basadas en lógica determinista, integradas con API, bases de datos y servicios, como base para las automatizaciones con IA de M13.

## Qué vas a aprender

Conceptos de n8n (workflows, nodos, ítems, *triggers*, ejecuciones, credenciales, expresiones); autohospedaje con Docker; webhooks y API; transformación de datos; nodo de código y subworkflows; manejo de errores, reintentos e idempotencia; seguridad de n8n 2.x; modelo Guardar/Publicar y versionado; primer nodo LLM dentro de un flujo determinista.

## Antes de empezar

- **Prerrequisitos:** [Módulo 0](../m00-orientacion/index.md) (indispensable), [Módulo 2](../m02-prompt-engineering/index.md) (recomendado, solo para L5.3.3).
- **Herramientas:** n8n Community autohospedado en Docker (gratuito), PostgreSQL; para L5.3.3, Ollama o una API con nivel gratuito; n8n Cloud opcional `[Pago]`.

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 5.1 · Fundamentos

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L5.1.1 | **Qué es n8n y cuándo conviene**<br>Qué es n8n y cuándo conviene frente a código propio u otras plataformas. Workflow determinista vs. agente (anticipo). | Conceptual | Esencial | Próximamente |
| L5.1.2 | **Instalación con Docker y PostgreSQL**<br>Instalación con Docker y PostgreSQL; estructura de una instancia. | Práctica | Esencial | Próximamente |
| L5.1.3 | **Modelo de datos**<br>Ítems, JSON, expresiones y *mapping*. | Práctica | Esencial | Próximamente |
| L5.1.4 | **Triggers**<br>*Triggers*: manual, programado, webhook y eventos de aplicaciones. | Práctica | Esencial | Próximamente |

### 5.2 · Integraciones

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L5.2.1 | **Webhooks y HTTP Request**<br>Webhooks entrantes y salientes; nodo HTTP Request contra API REST propias. | Práctica | Esencial | Próximamente |
| L5.2.2 | **Bases de datos, archivos y servicios**<br>Bases de datos, archivos y servicios (correo, calendario, GitHub, Slack o Telegram). | Práctica | Esencial | Próximamente |
| L5.2.3 | **Credenciales y seguridad en n8n**<br>Credenciales y seguridad de n8n 2.x: *task runners*, aislamiento del nodo de código, variables de entorno bloqueadas, nodos deshabilitados por defecto y gestión de secretos. | Mixta | Esencial | Próximamente |
| L5.2.4 | **Nodo de código y subworkflows**<br>Nodo de código (JavaScript/Python), subworkflows y reutilización. | Práctica | Profundizar | Próximamente |

### 5.3 · Robustez y primer paso con IA

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L5.3.1 | **Manejo de errores**<br>*error workflows*, reintentos, idempotencia y alertas. | Práctica | Esencial | Próximamente |
| L5.3.2 | **Guardar, publicar y versionar workflows**<br>Guardar vs. publicar, exportación y versionado de workflows en Git. | Práctica | Profundizar | Próximamente |
| L5.3.3 | **Primer nodo LLM en un workflow**<br>Primer nodo LLM dentro de un workflow determinista (clasificar o resumir), con control de costo y validación de la salida. | Mixta | Esencial | Próximamente |

## Práctica del módulo

- Guiado: webhook → transformación → base de datos → notificación.
- Guiado: workflow programado que consulta una API propia y genera un reporte.
- Independiente: integración entre dos servicios con manejo de errores e idempotencia.
- Desafío: clasificar con un LLM los ítems de un flujo y enrutar según el resultado, validando la salida.

## Proyecto o entregable

**Proyecto P2 · Sistema personal de trabajo con IA (parte C).** un workflow de n8n útil para tu trabajo, publicado, versionado en Git, con manejo de errores y al menos un paso con LLM validado.

## Cómo se aprueba

P2-C ≥ 80% en la rúbrica; evaluación de módulo ≥ 80%. (P2 queda aprobado globalmente cuando sus tres partes lo están, en cualquier orden.)

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 credenciales y webhooks públicos · 📏 casos de prueba de workflows · 💰 costo por ejecución · 🧭 n8n vs. script propio.
