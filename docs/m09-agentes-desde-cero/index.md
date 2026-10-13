---
modulo: M9
titulo: "Agentes desde cero"
bloque: III
nivel: general
horas_teoria: 12
horas_practica: 18
---

# M9 · Agentes desde cero

**Bloque III** · 30 h (12 h de teoría y 18 h de práctica) · 13 lecciones

## Objetivo

Entender qué es un agente y construir uno sin frameworks, para dominar el bucle, las herramientas, la planificación, la memoria y la supervisión humana.

## Qué vas a aprender

Agente vs. workflow y niveles de autonomía; bucle agéntico (razonar → actuar → observar); ReAct; planificación y re-planificación; memoria del agente; condiciones de parada; *human-in-the-loop*; manejo de errores; patrones de workflows (encadenamiento, enrutamiento, paralelización, orquestador-trabajadores, evaluador-optimizador); riesgos de la autonomía.

## Antes de empezar

- **Prerrequisitos:** [M6](../m06-apis-modelos/index.md) y [M7](../m07-context-engineering/index.md) (duros), [M8](../m08-rag/index.md) (recomendado).
- **Herramientas:** Python (sin frameworks), API de un proveedor o modelo local con soporte de herramientas.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U9.1 · Qué es un agente

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L9.1.1 | Workflows vs. agentes: control determinístico vs. control del modelo. Niveles de autonomía (de sugerir a actuar sin supervisión). | C | — |
| L9.1.2 | 🧭 Cuándo NO construir un agente: el costo de la autonomía (latencia, gasto, impredecibilidad). | C | — |
| L9.1.3 | Patrones de workflows con LLM: encadenamiento, enrutamiento, paralelización, orquestador-trabajadores y evaluador-optimizador. | M | — |

### U9.2 · Construir el bucle

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L9.2.1 | El bucle agéntico mínimo en ~100 líneas: modelo, herramientas, observación y parada. | P | — |
| L9.2.2 | ReAct y razonamiento intercalado; uso de *thinking* entre llamadas a herramientas. | M | — |
| L9.2.3 | Diseño de herramientas para agentes: granularidad, idempotencia y errores informativos. | P | — |
| L9.2.4 | Condiciones de parada, límites de pasos y presupuesto, bucles infinitos y recuperación de errores. | P | — |

### U9.3 · Planificación y memoria

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L9.3.1 | Planificación explícita: planes, listas de tareas y re-planificación. | P | — |
| L9.3.2 | Memoria del agente: *scratchpad*, archivos de estado y memoria a largo plazo con RAG. | P | — |
| L9.3.3 | Tareas de larga duración: checkpoints y reanudación (concepto; se implementa en M14). | C | — |

### U9.4 · Supervisión humana y confiabilidad

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L9.4.1 | *Human-in-the-loop*: aprobaciones, puntos de control e interrupciones. | P | — |
| L9.4.2 | 🔒 Agencia excesiva: permisos mínimos, *sandboxing*, acciones reversibles vs. irreversibles. | M | — |
| L9.4.3 | 📏 Evaluar agentes: éxito de la tarea, trayectoria, costo y pasos. | P | — |

## Práctica del módulo

- Guiado: agente de búsqueda de archivos y respuestas sobre un repositorio local.
- Guiado: implementar los cinco patrones de workflow con un mismo caso de uso.
- Independiente: agente con planificación explícita y aprobación humana antes de escribir.
- Desafío: hacer que el agente se recupere de herramientas que fallan y medir su tasa de éxito en 20 tareas.

## Proyecto o entregable

**Proyecto P5 · Agente desde cero.** agente sin frameworks para una tarea real tuya, con al menos 4 herramientas, planificación, memoria persistente, aprobación humana para acciones con efectos, límites de presupuesto, registro de trayectorias y evals. Puede usar P4 como herramienta de recuperación.

## Cómo se aprueba

P5 ≥ 80% en la rúbrica; *teach-back* del bucle completo; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 agencia excesiva y *sandboxing* · 📏 evals de trayectoria · 💰 costo por tarea · 🧭 workflow vs. agente.
