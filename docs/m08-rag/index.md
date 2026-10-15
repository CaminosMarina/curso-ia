---
modulo: M8
titulo: "Embeddings y RAG"
bloque: II
nivel: general
horas_teoria: 12
horas_practica: 22
---

# Módulo 8 · Embeddings y RAG

**Etapa 2** · 34 h (12 h de teoría y 22 h de práctica) · 14 lecciones

## Objetivo

Conectar modelos con conocimiento propio mediante búsqueda semántica y *Retrieval-Augmented Generation*, y saber evaluarlo y decidir cuándo conviene.

## Qué vas a aprender

Embeddings (texto y multimodales) y métricas de similitud; bases vectoriales e índices (HNSW); *chunking*; pipeline de ingesta; búsqueda híbrida (BM25 + vectores); *reranking*; reescritura de consultas; citas; RAG agéntico; evaluación de RAG; alternativas (contexto largo, búsqueda por herramientas, grafos).

## Antes de empezar

- **Prerrequisitos:** [Módulo 6](../m06-apis-modelos/index.md) y [Módulo 7](../m07-context-engineering/index.md) (indispensables).
- **Herramientas:** PostgreSQL + pgvector (Docker), Chroma, modelos de embeddings (locales con Ollama o vía API), Python; Spring AI `VectorStore` (Java, opcional).

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 8.1 · Embeddings y búsqueda semántica

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L8.1.1 | **Embeddings en profundidad**<br>Qué capturan, dimensiones, modelos, normalización y embeddings multimodales (texto e imagen en un mismo espacio). | Mixta | Esencial | Próximamente |
| L8.1.2 | **Similitud y búsqueda del vecino más cercano**<br>Similitud (coseno, producto punto, euclídea) y búsqueda del vecino más cercano: exacta vs. aproximada. | Mixta | Profundizar | Próximamente |
| L8.1.3 | **Bases vectoriales**<br>Pgvector, Chroma y servicios gestionados. Índices HNSW e IVF; filtros por metadatos. | Práctica | Esencial | Próximamente |

### 8.2 · Construcción de un pipeline RAG

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L8.2.1 | **Arquitectura RAG**<br>Ingesta → indexación → recuperación → generación. Por qué funciona y dónde falla. | Conceptual | Esencial | Próximamente |
| L8.2.2 | **Ingesta de documentos**<br>Ingesta: extracción de PDF, HTML y código; limpieza; metadatos. | Práctica | Esencial | Próximamente |
| L8.2.3 | **Chunking**<br>*Chunking*: tamaño, solapamiento, por estructura y semántico. Efectos en la calidad. | Mixta | Esencial | Próximamente |
| L8.2.4 | **Generación con contexto recuperado**<br>Prompt de RAG, citas y "no sé" cuando no hay evidencia. | Práctica | Esencial | Próximamente |

### 8.3 · RAG avanzado

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L8.3.1 | **Búsqueda híbrida y reranking**<br>Búsqueda híbrida y *reranking*. | Práctica | Esencial | Próximamente |
| L8.3.2 | **Reescritura de consultas y HyDE**<br>Reescritura y expansión de consultas, HyDE y consultas multi-paso. | Mixta | Profundizar | Próximamente |
| L8.3.3 | **RAG agéntico**<br>La recuperación como herramienta que decide el agente. | Mixta | Profundizar | Próximamente |
| L8.3.4 | **Alternativas a RAG**<br>Alternativas y complementos: contexto largo, búsqueda tipo `grep` en agentes de código, GraphRAG. Cuándo NO usar RAG y cuándo considerar *fine-tuning*. | Conceptual | Esencial | Próximamente |

### 8.4 · Evaluación y operación

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L8.4.1 | **Métricas de RAG**<br>Métricas: *recall* y precisión de recuperación, fidelidad (*faithfulness*) y relevancia de la respuesta. Construcción de un *dataset* de preguntas y respuestas. | Mixta | Esencial | Próximamente |
| L8.4.2 | **Herramientas de evaluación de RAG**<br>Herramientas de evaluación de RAG (por ejemplo Ragas, promptfoo o LLM como juez) y sus límites. | Práctica | Profundizar | Próximamente |
| L8.4.3 | **Operación de un sistema RAG**<br>Operación: actualización incremental, versionado del índice y control de acceso por documento. | Mixta | Profundizar | Próximamente |

## Práctica del módulo

- Guiado: búsqueda semántica sobre un conjunto de documentos con pgvector.
- Guiado: comparar tres estrategias de *chunking* con métricas.
- Independiente: agregar búsqueda híbrida y *reranking* y medir la mejora.
- Desafío: RAG con permisos por documento y prueba de que no filtra información.

## Proyecto o entregable

**Proyecto P4 · RAG sobre documentación técnica.** sistema de preguntas y respuestas sobre documentación real, con ingesta, búsqueda híbrida, citas, *dataset* de evaluación de al menos 30 preguntas e informe de métricas. Versión Python obligatoria; versión Spring AI opcional. Reutiliza el cliente de P3.

## Cómo se aprueba

P4 ≥ 80% en la rúbrica, con mejora demostrada respecto de la línea base; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 permisos y datos sensibles en índices · 📏 métricas de RAG · 💰 costo de embeddings y almacenamiento · 🧭 RAG vs. contexto largo vs. *fine-tuning*.
