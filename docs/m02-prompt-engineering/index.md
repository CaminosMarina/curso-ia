---
modulo: M2
titulo: "Prompt Engineering"
bloque: I
nivel: general
horas_teoria: 8
horas_practica: 12
---

# Módulo 2 · Prompt Engineering

**Etapa 1** · 20 h (8 h de teoría y 12 h de práctica) · 15 lecciones

## Objetivo

Diseñar instrucciones efectivas, reproducibles y evaluables, entendiendo por qué funcionan.

## Qué vas a aprender

Anatomía de un prompt (texto, archivos e imágenes); roles (system, user, assistant); técnicas (instrucciones explícitas, ejemplos *few-shot*, descomposición, razonamiento paso a paso, delimitadores y XML, formato de salida); prompts para modelos de razonamiento; versionado y evaluación de prompts; *prompt injection* (introducción).

## Antes de empezar

- **Prerrequisitos:** [Módulo 1](../m01-fundamentos-llm/index.md) (indispensable).
- **Herramientas:** *playgrounds* (Claude Console, OpenAI Playground, Google AI Studio), Ollama, promptfoo (introducción).

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 2.1 · Fundamentos

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L2.1.1 | **Qué es un prompt para el modelo**<br>Todo es contexto (texto, archivos, imágenes). Roles y estructura de mensajes. | Conceptual | Esencial | Próximamente |
| L2.1.2 | **Claridad y especificidad**<br>Tarea, contexto, restricciones, formato y criterio de éxito. El "test del colega nuevo". | Mixta | Esencial | Próximamente |
| L2.1.3 | **System prompt y mensaje de usuario**<br>*System prompt* vs. mensaje de usuario: qué va en cada uno y por qué. | Conceptual | Esencial | Próximamente |

### 2.2 · Técnicas principales

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L2.2.1 | **Ejemplos (few-shot)**<br>Ejemplos (*few-shot*): cuántos, cuáles, cómo evitar que el modelo copie de más. | Mixta | Esencial | Próximamente |
| L2.2.2 | **Estructura con delimitadores y XML**<br>Estructura con delimitadores y XML; documentos largos al principio y pregunta al final. | Mixta | Esencial | Próximamente |
| L2.2.3 | **Razonamiento paso a paso**<br>Razonamiento paso a paso y modelos con *thinking*: cuándo pedirlo, cuándo sobra. | Mixta | Esencial | Próximamente |
| L2.2.4 | **Prompt chaining**<br>Descomposición y encadenamiento de prompts (*prompt chaining*). | Mixta | Esencial | Próximamente |
| L2.2.5 | **Control del formato de salida**<br>JSON, Markdown y plantillas (preparación para salidas estructuradas en M6). | Práctica | Esencial | Próximamente |

### 2.3 · Prompts de calidad profesional

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L2.3.1 | **Prompts para tareas de desarrollo**<br>Revisión de código, generación de tests, documentación, análisis de logs. | Práctica | Esencial | Próximamente |
| L2.3.2 | **Portabilidad de prompts entre modelos**<br>Diferencias entre modelos y portabilidad de prompts: qué es transferible y qué es específico. | Mixta | Profundizar | Próximamente |
| L2.3.3 | **Meta-prompting**<br>Usar un LLM para mejorar prompts, y sus límites. | Mixta | Profundizar | Próximamente |

### 2.4 · Evaluar y mantener prompts

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L2.4.1 | **Por qué probar una vez no alcanza**<br>Por qué "lo probé una vez y anduvo" no alcanza: variabilidad y casos de prueba. | Conceptual | Esencial | Próximamente |
| L2.4.2 | **Primer conjunto de evaluación**<br>Casos, salidas esperadas y criterios. Comparación A/B con promptfoo. | Práctica | Esencial | Próximamente |
| L2.4.3 | **Versionado de prompts como código** | Práctica | Profundizar | Próximamente |
| L2.4.4 | **Prompt injection: introducción**<br>*Prompt injection* (introducción): qué es, por qué no se resuelve solo con instrucciones y la regla de oro (todo contenido externo es dato no confiable). | Mixta | Esencial | Próximamente |

## Práctica del módulo

- Guiado: refactorizar 5 prompts malos aplicando las técnicas y medir la mejora.
- Independiente: diseñar un prompt de revisión de código Java con salida en JSON y probarlo en 3 modelos.
- Desafío: romper con *prompt injection* un prompt propio y después endurecerlo (y documentar por qué el endurecimiento es parcial).

## Proyecto o entregable

**Proyecto P1 · Biblioteca de prompts evaluada.** repositorio con 8 a 10 prompts para tu trabajo diario, cada uno con propósito, versión, casos de prueba y resultados en al menos dos modelos.

## Cómo se aprueba

P1 ≥ 80% en la rúbrica, con evaluaciones reproducibles; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 *prompt injection* · 📏 primer set de evals · 💰 costo del *few-shot* y de los prompts largos · 🧭 prompt vs. *fine-tuning* vs. RAG (primera aproximación).
