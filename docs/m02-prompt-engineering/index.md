---
modulo: M2
titulo: "Prompt Engineering"
bloque: I
nivel: general
horas_teoria: 8
horas_practica: 12
---

# M2 · Prompt Engineering

**Bloque I** · 20 h (8 h de teoría y 12 h de práctica) · 15 lecciones

## Objetivo

Diseñar instrucciones efectivas, reproducibles y evaluables, entendiendo por qué funcionan.

## Qué vas a aprender

Anatomía de un prompt (texto, archivos e imágenes); roles (system, user, assistant); técnicas (instrucciones explícitas, ejemplos *few-shot*, descomposición, razonamiento paso a paso, delimitadores y XML, formato de salida); prompts para modelos de razonamiento; versionado y evaluación de prompts; *prompt injection* (introducción).

## Antes de empezar

- **Prerrequisitos:** [M1](../m01-fundamentos-llm/index.md) (duro).
- **Herramientas:** *playgrounds* (Claude Console, OpenAI Playground, Google AI Studio), Ollama, promptfoo (introducción).

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U2.1 · Fundamentos

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L2.1.1 | Qué es un prompt para el modelo: todo es contexto (texto, archivos, imágenes). Roles y estructura de mensajes. | C | — |
| L2.1.2 | Claridad y especificidad: tarea, contexto, restricciones, formato y criterio de éxito. El "test del colega nuevo". | M | — |
| L2.1.3 | *System prompt* vs. mensaje de usuario: qué va en cada uno y por qué. | C | — |

### U2.2 · Técnicas principales

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L2.2.1 | Ejemplos (*few-shot*): cuántos, cuáles, cómo evitar que el modelo copie de más. | M | — |
| L2.2.2 | Estructura con delimitadores y XML; documentos largos al principio y pregunta al final. | M | — |
| L2.2.3 | Razonamiento paso a paso y modelos con *thinking*: cuándo pedirlo, cuándo sobra. | M | — |
| L2.2.4 | Descomposición y encadenamiento de prompts (*prompt chaining*). | M | — |
| L2.2.5 | Control del formato de salida: JSON, Markdown y plantillas (preparación para salidas estructuradas en M6). | P | — |

### U2.3 · Prompts de calidad profesional

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L2.3.1 | Prompts para tareas de desarrollo: revisión de código, generación de tests, documentación, análisis de logs. | P | — |
| L2.3.2 | Diferencias entre modelos y portabilidad de prompts: qué es transferible y qué es específico. | M | — |
| L2.3.3 | Meta-prompting: usar un LLM para mejorar prompts, y sus límites. | M | — |

### U2.4 · Evaluar y mantener prompts

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L2.4.1 | Por qué "lo probé una vez y anduvo" no alcanza: variabilidad y casos de prueba. | C | — |
| L2.4.2 | Primer conjunto de evaluación: casos, salidas esperadas y criterios. Comparación A/B con promptfoo. | P | — |
| L2.4.3 | Versionado de prompts como código. | P | — |
| L2.4.4 | 🔒 *Prompt injection* (introducción): qué es, por qué no se resuelve solo con instrucciones y la regla de oro (todo contenido externo es dato no confiable). | M | — |

## Práctica del módulo

- Guiado: refactorizar 5 prompts malos aplicando las técnicas y medir la mejora.
- Independiente: diseñar un prompt de revisión de código Java con salida en JSON y probarlo en 3 modelos.
- Desafío: romper con *prompt injection* un prompt propio y después endurecerlo (y documentar por qué el endurecimiento es parcial).

## Proyecto o entregable

**Proyecto P1 · Biblioteca de prompts evaluada.** repositorio con 8 a 10 prompts para tu trabajo diario, cada uno con propósito, versión, casos de prueba y resultados en al menos dos modelos.

## Cómo se aprueba

P1 ≥ 80% en la rúbrica, con evaluaciones reproducibles; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 *prompt injection* · 📏 primer set de evals · 💰 costo del *few-shot* y de los prompts largos · 🧭 prompt vs. *fine-tuning* vs. RAG (primera aproximación).
