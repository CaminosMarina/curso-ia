---
modulo: M11
titulo: "Agentes de programación: arquitectura y configuración avanzada"
bloque: III
nivel: N2
horas_teoria: 7
horas_practica: 18
---

# M11 · Agentes de programación: arquitectura y configuración avanzada

**Bloque III** · **Nivel 2 (construir y profundizar)** · 25 h (7 h de teoría y 18 h de práctica) · 14 lecciones

## Objetivo

Entender cómo están construidos los agentes de programación y configurar a nivel avanzado **Claude Code y Codex** (instrucciones, permisos y aislamiento, MCP propio, skills propias, hooks, subagentes, automatización y CI), midiendo su eficacia y distinguiendo lo común de lo específico de cada uno.

## Qué vas a aprender

Arquitectura del *harness*; gestión interna del contexto; instrucciones y memoria a fondo; portabilidad de configuración; permisos avanzados, *sandbox* y revisión automática de aprobaciones; MCP propio; skills propias en el agente; hooks; subagentes y tareas en paralelo; modo no interactivo, CI y tareas programadas; revisión de código a escala; métricas de eficacia.

## Antes de empezar

- **Prerrequisitos:** [M4](../m04-agentes-programacion/index.md) y [M7](../m07-context-engineering/index.md) (duros), [M10](../m10-mcp/index.md) (recomendado, para L11.3.2).
- **Herramientas:** Claude Code `[Pago]`; Codex (CLI, app y GitHub Action); Git; GitHub Actions. Las funciones marcadas `[Verificar]` se comprueban en la documentación de cada herramienta al preparar la lección.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U11.1 · Arquitectura

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L11.1.1 | Anatomía del *harness*: bucle, herramientas (lectura, edición, terminal, búsqueda), contexto y permisos. Comparación entre Claude Code, Codex y tu agente de P5. | C | — |
| L11.1.2 | Cómo gestiona el contexto un agente de programación: compactación, memoria, carga de instrucciones y skills, búsqueda en el código vs. RAG. Diferencias entre ambas herramientas. | C | — |

### U11.2 · Instrucciones y memoria a fondo

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L11.2.1 | `AGENTS.md` y `CLAUDE.md` a fondo: jerarquía, alcance por carpeta, archivos de anulación y límites de tamaño en Codex, memoria en Claude Code; mantenimiento y medición de efecto. | M | — |
| L11.2.2 | Portabilidad de la configuración entre agentes: qué es estándar (`AGENTS.md`, Agent Skills, MCP) y qué es propio (`config.toml` de Codex, `settings.json` de Claude Code, hooks, extensiones de skills). | M | — |

### U11.3 · Configuración avanzada

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L11.3.1 | 🔒 Permisos avanzados y aislamiento: políticas por proyecto y organización en Claude Code; en Codex, modos de *sandbox*, políticas de aprobación, revisión automática de aprobaciones, reglas de ejecución y el *sandbox* nativo de Windows. | P | — |
| L11.3.2 | Tu servidor MCP (P6) en ambos agentes: configuración, autenticación OAuth, herramientas permitidas o bloqueadas y aprobación por herramienta. | P | — |
| L11.3.3 | Hooks y automatismos del ciclo de vida: hooks de Claude Code (formateo, lint, tests, bloqueos de seguridad) y su equivalente en Codex, si existe en la versión vigente `[Verificar]`. | P | — |
| L11.3.4 | Subagentes y trabajo en paralelo: subagentes de Claude Code; tareas en paralelo con *worktrees* y en la nube en Codex; cuándo aislar contexto. | M | — |
| L11.3.5 | Primera skill propia dentro del agente de programación: ubicaciones (`.claude/skills` y `.agents/skills`), invocación explícita e implícita, y una misma skill usada en Claude Code y en Codex (el desarrollo a fondo sigue en M12). | P | — |

### U11.4 · Automatización

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L11.4.1 | Modo no interactivo y scripting: `claude -p` y `codex exec` (salida JSON, salida con esquema, *sandbox* de solo lectura por defecto en Codex, reanudar sesiones). | P | — |
| L11.4.2 | Agentes en CI: revisión de PR y corrección de fallas con la integración de GitHub Actions de Claude Code y con la acción oficial de Codex (separar el job que ejecuta al agente del job con permisos de escritura); revisión de código automática en GitHub. | P | — |
| L11.4.3 | Tareas programadas y en la nube: Routines y tareas de escritorio de Claude Code; tareas programadas de Codex (locales en *worktree* o en la nube para equipos). Límites y riesgos de la ejecución desatendida `[Pago]`. | M | — |

### U11.5 · Calidad

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L11.5.1 | Revisión de código generado a escala: calidad, seguridad y deuda técnica. | M | — |
| L11.5.2 | 📏 Medir la eficacia de cada agente en tu repositorio: tareas de referencia, tasa de éxito, intervenciones y costo. | P | — |

## Práctica del módulo

- Guiado: hooks de calidad y seguridad en Claude Code; política de *sandbox* y aprobaciones equivalente en Codex.
- Guiado: una skill de proyecto usada desde ambos agentes.
- Independiente: pipeline de revisión automática de PR en GitHub Actions con uno de los agentes (el otro, opcional).
- Desafío: conjunto de 10 tareas de referencia y comparación cuantitativa entre Claude Code y Codex (o entre dos configuraciones del mismo agente).

## Proyecto o entregable

**Proyecto.** base de P7 (configuración avanzada que después se empaqueta como plugin en M12).

## Cómo se aprueba

Repositorio con configuración avanzada justificada para ambos agentes y métricas de eficacia; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 permisos, *sandbox*, secretos en CI y código inseguro · 📏 métricas de eficacia · 💰 consumo por tarea · 🧭 qué automatizar y con qué agente.
