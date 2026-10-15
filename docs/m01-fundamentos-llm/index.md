---
modulo: M1
titulo: "Fundamentos de IA generativa y LLM"
bloque: I
nivel: general
horas_teoria: 12
horas_practica: 12
---

# Módulo 1 · Fundamentos de IA generativa y LLM

**Etapa 1** · 24 h (12 h de teoría y 12 h de práctica) · 16 lecciones

## Objetivo

Construir un modelo mental correcto de qué es y cómo funciona un LLM, para explicar sus capacidades, limitaciones y comportamientos.

## Qué vas a aprender

Diferencias entre IA, ML, deep learning e IA generativa; tokens y tokenización (texto e imágenes); embeddings (intro); arquitectura *transformer* y atención a nivel conceptual; entrenamiento (preentrenamiento, ajuste por instrucciones, RLHF); inferencia y parámetros de muestreo; modelos de razonamiento; ventana de contexto; alucinaciones; multimodalidad; panorama de modelos; costos y latencia.

## Antes de empezar

- **Prerrequisitos:** [Módulo 0](../m00-orientacion/index.md) (indispensable).
- **Herramientas:** Ollama, tokenizadores (por ejemplo `tiktoken` y el conteo de tokens de las API), *playgrounds* de proveedores, Python con notebooks.

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 1.1 · Del aprendizaje automático a la IA generativa

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L1.1.1 | **IA, ML, deep learning e IA generativa**<br>Definiciones precisas y qué problema resuelve cada uno. | Conceptual | Esencial | Próximamente |
| L1.1.2 | **Redes neuronales en 90 minutos**<br>Parámetros, entrenamiento y generalización (lo justo para entender LLM, sin matemática innecesaria). | Conceptual | Profundizar | Próximamente |
| L1.1.3 | **Qué es un modelo de lenguaje**<br>Predecir el próximo token. Por qué algo tan simple produce comportamientos complejos. | Conceptual | Esencial | Próximamente |

### 1.2 · Cómo "ve" la información un modelo

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L1.2.1 | **Tokens y tokenización**<br>BPE, por qué el español "cuesta" más tokens, cómo se tokenizan imágenes y otros formatos, impacto en costo y límites. | Mixta | Esencial | Próximamente |
| L1.2.2 | **Embeddings**<br>El contenido como vectores, similitud semántica (intro práctica; se profundiza en M8). | Mixta | Esencial | Próximamente |
| L1.2.3 | **Transformers y atención**<br>Intuición del mecanismo, por qué permite contexto largo y qué significa "ventana de contexto". | Conceptual | Esencial | Próximamente |

### 1.3 · Cómo se construye un LLM

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L1.3.1 | **Preentrenamiento**<br>Datos, escala y fecha de corte de conocimiento. | Conceptual | Profundizar | Próximamente |
| L1.3.2 | **Post-entrenamiento**<br>Ajuste por instrucciones, RLHF y técnicas afines, *system prompts*. Por qué un modelo "asistente" se comporta distinto que un modelo base. | Conceptual | Esencial | Próximamente |
| L1.3.3 | **Modelos de razonamiento**<br>Modelos de razonamiento (*thinking*): qué cambia, cuándo convienen y su costo. | Conceptual | Esencial | Próximamente |

### 1.4 · Inferencia: qué pasa cuando le pedís algo

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L1.4.1 | **Generación token a token y muestreo**<br>Temperatura, top-p, top-k, *stop sequences* y máximo de tokens. Determinismo y por qué no está garantizado. | Mixta | Esencial | Próximamente |
| L1.4.2 | **Ventana de contexto en la práctica**<br>Entrada, salida, efecto "perdido en el medio" y degradación con contextos largos. | Mixta | Esencial | Próximamente |
| L1.4.3 | **Latencia, throughput y costos**<br>Latencia, *throughput* y costos: tokens de entrada, salida y razonamiento; *streaming*. | Mixta | Esencial | Próximamente |

### 1.5 · Capacidades, limitaciones y panorama

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L1.5.1 | **Alucinaciones**<br>Por qué ocurren (no es un bug, es la naturaleza del modelo) y estrategias de mitigación. | Mixta | Esencial | Próximamente |
| L1.5.2 | **Multimodalidad**<br>Visión, audio, generación de imágenes. Qué es nativo y qué es un sistema combinado. | Conceptual | Profundizar | Próximamente |
| L1.5.3 | **Panorama de modelos**<br>Cerrados (Claude, GPT, Gemini) y abiertos (Llama, Qwen, Mistral, DeepSeek, Gemma); niveles de tamaño; cómo leer (y desconfiar de) los *benchmarks*. Versiones vigentes verificadas al preparar la lección. | Conceptual | Esencial | Próximamente |
| L1.5.4 | **Modelo, producto y harness**<br>Modelo vs. producto vs. *harness*: la diferencia entre un modelo, la app que lo envuelve y el agente que lo usa. Clave para todo el curso. | Conceptual | Esencial | Próximamente |

## Práctica del módulo

- Guiado: contar tokens del mismo texto en español e inglés con distintos tokenizadores y calcular el costo.
- Guiado: correr un modelo local con Ollama variando temperatura y top-p, y documentar el efecto.
- Independiente: provocar y analizar alucinaciones en tres modelos distintos; proponer mitigaciones.
- Desafío: medir la degradación de recuperación en un contexto largo (prueba de "aguja en un pajar") con un modelo local.

## Proyecto o entregable

**Entregable (no es proyecto numerado).** mini-informe técnico "Cómo funciona un LLM, explicado a un colega backend".

## Cómo se aprueba

Evaluación de módulo ≥ 80%; *teach-back* aprobado de token, ventana de contexto, temperatura y alucinación; entregable revisado.

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 qué pasa con los datos que enviás (retención y entrenamiento según el proveedor y el plan) · 💰 cálculo de costo por token · 🧭 modelo grande vs. chico vs. local.
