---
modulo: M4
titulo: "Agentes de programación"
bloque: I
nivel: N1
horas_teoria: 5
horas_practica: 16
---

# Módulo 4 · Agentes de programación

**Etapa 1** · **Nivel 1 (usar y configurar)** · 21 h (5 h de teoría y 16 h de práctica) · 14 lecciones

## Objetivo

Incorporar agentes de programación a tu trabajo diario de forma productiva y segura, con un flujo profesional y configuración básica, trabajando con **Claude Code y Codex** como herramientas principales y separando lo común a todos los agentes de lo propio de cada uno, antes de estudiar su arquitectura.

## Qué vas a aprender

Diferencia entre autocompletado, chat y agente; acceso, instalación y superficies de Claude Code y de Codex; flujo explorar → planificar → implementar → verificar; pedidos verificables; `AGENTS.md` (y `CLAUDE.md`) inicial compartido; Git como red de seguridad; permisos, aislamiento (*sandbox*) y aprobaciones en cada herramienta; uso de servidores MCP y skills existentes; configuración inicial de Codex y trabajo en la nube; gestión del contexto y de las sesiones; revisión del código generado; comparación práctica.

## Antes de empezar

- **Prerrequisitos:** [Módulo 2](../m02-prompt-engineering/index.md) (indispensable), [Módulo 3](../m03-asistentes/index.md) (recomendado).
- **Herramientas:** Claude Code `[Pago: suscripción o API]`; Codex (incluido en los planes de ChatGPT, también Free con uso limitado, o con clave de API con pago por uso; las funciones en la nube requieren cuenta de ChatGPT); opcionales: Gemini CLI u OpenCode con modelo local; Git; un repositorio Java o Python real tuyo (o uno de práctica). En Windows se usa el *sandbox* nativo de cada herramienta o WSL (ver la nota de herramientas de cada lección).

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 4.1 · Primeros pasos

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L4.1.1 | **Qué es un agente de programación**<br>Qué es un agente de programación y en qué se diferencia del autocompletado y del chat. Qué es común a todos (bucle, herramientas de lectura/edición/terminal, permisos, archivo de instrucciones) y por qué actuar en tu máquina exige cuidado. | Conceptual | Esencial | Próximamente |
| L4.1.2 | **Claude Code: primeros pasos**<br>Claude Code: acceso, instalación, primera sesión y superficies (terminal, IDE, escritorio y web). | Práctica | Esencial | Próximamente |
| L4.1.3 | **Codex: primeros pasos**<br>Codex: acceso (cuenta de ChatGPT o clave de API), superficies (app de escritorio de ChatGPT, CLI, extensión para IDE, web y nube), instalación en Windows y primera sesión. | Práctica | Esencial | Próximamente |

### 4.2 · Flujo de trabajo profesional (en ambos agentes)

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L4.2.1 | **Explorar, planificar, implementar y verificar**<br>Explorar, planificar, implementar y verificar con tests: el mismo flujo en Claude Code (modo plan) y en Codex. | Práctica | Esencial | Próximamente |
| L4.2.2 | **Pedidos concretos y verificables**<br>Cómo especificar una tarea de código (retoma L3.7.1). | Mixta | Esencial | Próximamente |
| L4.2.3 | **Instrucciones persistentes**<br>Un `AGENTS.md` inicial que sirva a ambos agentes (convenciones, comandos de build y test, qué no tocar); cómo lo lee cada uno (Codex: cadena global → raíz → carpeta actual; Claude Code: `CLAUDE.md` o `AGENTS.md`). | Práctica | Esencial | Próximamente |
| L4.2.4 | **Revisar y aceptar cambios**<br>Lectura de diffs, revisión asistida (`/review` en Codex, revisión en Claude Code), Git como red de seguridad, ramas y *commits* pequeños. | Práctica | Esencial | Próximamente |

### 4.3 · Configuración básica y seguridad

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L4.3.1 | **Permisos y aislamiento**<br>Conceptos comunes (qué puede leer, escribir y ejecutar; acceso a red; aprobaciones) y su implementación en Claude Code (modos de permisos) y en Codex (modos de *sandbox* `read-only` / `workspace-write` / acceso total y políticas de aprobación). Qué permitir, qué preguntar siempre y qué nunca. | Mixta | Esencial | Próximamente |
| L4.3.2 | **MCP y skills en los agentes**<br>Usar servidores MCP y skills existentes desde ambos agentes (configuración de cada uno, invocación explícita e implícita). | Práctica | Esencial | Próximamente |
| L4.3.3 | **Contexto y sesiones**<br>Cuándo compactar, cuándo empezar de cero, cómo retomar una sesión anterior en cada herramienta. | Mixta | Esencial | Próximamente |

### 4.4 · Codex en la práctica

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L4.4.1 | **Configuración inicial de Codex**<br>Configuración inicial de Codex (`config.toml`: modelo y esfuerzo, permisos, configuración por proyecto) y trabajo con repositorios (proyectos locales, *worktrees* para tareas en paralelo). | Práctica | Profundizar | Próximamente |
| L4.4.2 | **Codex en la nube**<br>Entornos, acceso a internet desactivado por defecto y lista de dominios permitidos, tareas en paralelo, revisión del resultado y *pull requests*. | Práctica | Profundizar | Próximamente |

### 4.5 · Criterio

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L4.5.1 | **Qué delegar y qué no**<br>Tareas ideales, tareas riesgosas y señales de que el agente se está desviando. | Mixta | Esencial | Próximamente |
| L4.5.2 | **Claude Code vs. Codex**<br>Comparación práctica Claude Code vs. Codex: misma tarea, calidad, consumo, ergonomía, permisos y qué conviene para cada tipo de trabajo. | Mixta | Profundizar | Próximamente |

## Práctica del módulo

- Guiado: implementar una funcionalidad pequeña con el flujo completo en Claude Code.
- Guiado: implementar otra funcionalidad en el mismo repositorio con Codex (CLI o app), con *sandbox* `workspace-write` y revisión con `/review`.
- Independiente: escribir el `AGENTS.md` compartido y comprobar que ambos agentes lo respetan.
- Independiente: una tarea en Codex en la nube que termine en un *pull request* revisado por vos.
- Desafío: refactorización mediana resuelta por ambos agentes; informe comparativo con datos (resultado, tests, consumo, intervenciones necesarias).

## Proyecto o entregable

**Proyecto P2 · Sistema personal de trabajo con IA (parte B).** repositorio real configurado para trabajar con Claude Code y Codex (`AGENTS.md` compartido, permisos justificados en cada herramienta, al menos un MCP o skill útil) y un registro de 4 tareas reales delegadas (al menos una en cada agente) con resultado y verificación.

## Cómo se aprueba

P2-B ≥ 80% en la rúbrica; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 permisos, *sandbox* y secretos en el repositorio · 📏 verificación con tests · 💰 consumo por sesión y límites del plan · 🧭 qué delegar y a qué agente.
