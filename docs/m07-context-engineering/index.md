---
modulo: M7
titulo: "Context Engineering"
bloque: II
nivel: N2
horas_teoria: 8
horas_practica: 12
---

# M7 · Context Engineering

**Bloque II** · **Nivel 2 (construir y profundizar)** · 20 h (8 h de teoría y 12 h de práctica) · 11 lecciones

## Objetivo

Diseñar y gestionar sistemáticamente, desde el código, todo lo que entra a la ventana de contexto (instrucciones, conocimiento, memoria, herramientas e historial) para obtener resultados confiables y eficientes.

## Qué vas a aprender

El contexto como recurso finito; componentes del contexto; estrategias (seleccionar, comprimir, aislar, persistir); memoria de corto y largo plazo; archivos de instrucciones a fondo; divulgación progresiva; compactación y edición de contexto; caché y orden del contexto.

## Antes de empezar

- **Prerrequisitos:** [M6](../m06-apis-modelos/index.md) (duro); [M3](../m03-asistentes/index.md) y [M4](../m04-agentes-programacion/index.md) (recomendados: aportan la experiencia de uso que aquí se formaliza).
- **Herramientas:** API de Claude, OpenAI y Gemini; Ollama; conteo de tokens.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U7.1 · Del prompt al contexto

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L7.1.1 | Qué es context engineering y por qué reemplazó al "prompt engineering" como habilidad central. | C | — |
| L7.1.2 | Componentes del contexto: instrucciones de sistema, definiciones de herramientas, conocimiento recuperado, memoria, historial y resultados de herramientas. Cuánto "pesa" cada uno. | M | — |
| L7.1.3 | Degradación del contexto (*context rot*): medirla y por qué más contexto no siempre es mejor. | M | — |

### U7.2 · Estrategias

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L7.2.1 | Seleccionar: qué incluir y qué dejar afuera; recuperación bajo demanda vs. carga anticipada. | M | — |
| L7.2.2 | Comprimir: resúmenes, compactación y edición de contexto (limpiar resultados viejos de herramientas). | P | — |
| L7.2.3 | Aislar: dividir trabajo en subcontextos (anticipo de subagentes y multiagente). | C | — |
| L7.2.4 | Persistir: notas externas, archivos de estado y *memory tools*. | P | — |
| L7.2.5 | Orden y caché: estructurar el contexto para aprovechar la caché de prompts. | P | — |

### U7.3 · Memoria y conocimiento

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L7.3.1 | Tipos de memoria: de trabajo, episódica, semántica y procedimental. Cómo se implementa cada una. | C | — |
| L7.3.2 | Archivos de instrucciones a fondo (`CLAUDE.md`, `AGENTS.md`, instrucciones de proyecto): principios de diseño, alcance y medición de efecto (formaliza lo usado en M3 y M4). | M | — |
| L7.3.3 | Divulgación progresiva: el principio detrás de las Agent Skills y la búsqueda de herramientas. | C | — |

## Práctica del módulo

- Guiado: medir cómo cambia la calidad de una tarea al variar tamaño y orden del contexto.
- Guiado: implementar compactación automática de historial en el DevAssist CLI.
- Independiente: diseñar un sistema de memoria persistente simple (archivo o base de datos) para un asistente.
- Desafío: evaluar con datos el efecto del `AGENTS.md` de tu repositorio (de P2-B) en un agente de programación y mejorarlo.

## Proyecto o entregable

**Proyecto.** P3 extendido con gestión de contexto y memoria.

## Cómo se aprueba

P3 extendido revisado; *teach-back* de las cuatro estrategias con ejemplos; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 fuga de datos por contexto y memoria · 📏 calidad vs. tamaño de contexto · 💰 tokens por turno · 🧭 cargar vs. recuperar.
