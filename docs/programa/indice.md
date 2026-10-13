<!-- Generado por scripts/generar.py a partir de las portadas de los módulos. No editar a mano. -->

# Índice de lecciones

Las 233 lecciones del núcleo, módulo por módulo. **1 tiene material**: es la que lleva enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

**Tipo de lección:** `C` conceptual (se verifica con preguntas) · `P` práctica (se verifica con un ejercicio) · `M` mixta (las dos cosas). Detalle en [Evaluación y estados](evaluacion.md).

## Bloque I · Fundamentos y uso profesional

### [M0 · Orientación, entorno y método](../m00-orientacion/index.md)

6 h · 4 lecciones · **Prerrequisitos:** ninguno.

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L0.1.1 | [Mapa del curso, niveles 1 y 2, estados de aprendizaje y protocolo de sesión (inicio, cierre y sincronización de registros).](../m00-orientacion/l0-1-1-mapa-del-curso.md) | C | 📝 Borrador |
| L0.1.2 | Cómo aprender en un campo que cambia cada mes: fuentes oficiales, *changelogs* y cómo verificar lo que dice un modelo (incluido un tutor de IA). | C | — |
| L0.2.1 | Repositorio Git del curso (registros, apuntes y proyectos), estructura de carpetas, entornos de Python y Java, Docker. | P | — |
| L0.2.2 | Claves de API: creación, almacenamiento seguro (`.env`, gestor de secretos, nunca en Git), límites de gasto y alertas. Instalación de Ollama y primer modelo local. | P | — |

### [M1 · Fundamentos de IA generativa y LLM](../m01-fundamentos-llm/index.md)

24 h · 16 lecciones · **Prerrequisitos:** [M0](../m00-orientacion/index.md) (duro).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L1.1.1 | IA, ML, deep learning e IA generativa: definiciones precisas y qué problema resuelve cada uno. | C | — |
| L1.1.2 | Redes neuronales en 90 minutos: parámetros, entrenamiento y generalización (lo justo para entender LLM, sin matemática innecesaria). | C | — |
| L1.1.3 | Qué es un modelo de lenguaje: predecir el próximo token. Por qué algo tan simple produce comportamientos complejos. | C | — |
| L1.2.1 | Tokens y tokenización: BPE, por qué el español "cuesta" más tokens, cómo se tokenizan imágenes y otros formatos, impacto en costo y límites. | M | — |
| L1.2.2 | Embeddings: el contenido como vectores, similitud semántica (intro práctica; se profundiza en M8). | M | — |
| L1.2.3 | Transformers y atención: intuición del mecanismo, por qué permite contexto largo y qué significa "ventana de contexto". | C | — |
| L1.3.1 | Preentrenamiento: datos, escala y fecha de corte de conocimiento. | C | — |
| L1.3.2 | Post-entrenamiento: ajuste por instrucciones, RLHF y técnicas afines, *system prompts*. Por qué un modelo "asistente" se comporta distinto que un modelo base. | C | — |
| L1.3.3 | Modelos de razonamiento (*thinking*): qué cambia, cuándo convienen y su costo. | C | — |
| L1.4.1 | Generación token a token y muestreo: temperatura, top-p, top-k, *stop sequences* y máximo de tokens. Determinismo y por qué no está garantizado. | M | — |
| L1.4.2 | Ventana de contexto en la práctica: entrada, salida, efecto "perdido en el medio" y degradación con contextos largos. | M | — |
| L1.4.3 | Latencia, *throughput* y costos: tokens de entrada, salida y razonamiento; *streaming*. | M | — |
| L1.5.1 | Alucinaciones: por qué ocurren (no es un bug, es la naturaleza del modelo) y estrategias de mitigación. | M | — |
| L1.5.2 | Multimodalidad: visión, audio, generación de imágenes. Qué es nativo y qué es un sistema combinado. | C | — |
| L1.5.3 | Panorama de modelos: cerrados (Claude, GPT, Gemini) y abiertos (Llama, Qwen, Mistral, DeepSeek, Gemma); niveles de tamaño; cómo leer (y desconfiar de) los *benchmarks*. Versiones vigentes verificadas al preparar la lección. | C | — |
| L1.5.4 | Modelo vs. producto vs. *harness*: la diferencia entre un modelo, la app que lo envuelve y el agente que lo usa. Clave para todo el curso. | C | — |

### [M2 · Prompt Engineering](../m02-prompt-engineering/index.md)

20 h · 15 lecciones · **Prerrequisitos:** [M1](../m01-fundamentos-llm/index.md) (duro).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L2.1.1 | Qué es un prompt para el modelo: todo es contexto (texto, archivos, imágenes). Roles y estructura de mensajes. | C | — |
| L2.1.2 | Claridad y especificidad: tarea, contexto, restricciones, formato y criterio de éxito. El "test del colega nuevo". | M | — |
| L2.1.3 | *System prompt* vs. mensaje de usuario: qué va en cada uno y por qué. | C | — |
| L2.2.1 | Ejemplos (*few-shot*): cuántos, cuáles, cómo evitar que el modelo copie de más. | M | — |
| L2.2.2 | Estructura con delimitadores y XML; documentos largos al principio y pregunta al final. | M | — |
| L2.2.3 | Razonamiento paso a paso y modelos con *thinking*: cuándo pedirlo, cuándo sobra. | M | — |
| L2.2.4 | Descomposición y encadenamiento de prompts (*prompt chaining*). | M | — |
| L2.2.5 | Control del formato de salida: JSON, Markdown y plantillas (preparación para salidas estructuradas en M6). | P | — |
| L2.3.1 | Prompts para tareas de desarrollo: revisión de código, generación de tests, documentación, análisis de logs. | P | — |
| L2.3.2 | Diferencias entre modelos y portabilidad de prompts: qué es transferible y qué es específico. | M | — |
| L2.3.3 | Meta-prompting: usar un LLM para mejorar prompts, y sus límites. | M | — |
| L2.4.1 | Por qué "lo probé una vez y anduvo" no alcanza: variabilidad y casos de prueba. | C | — |
| L2.4.2 | Primer conjunto de evaluación: casos, salidas esperadas y criterios. Comparación A/B con promptfoo. | P | — |
| L2.4.3 | Versionado de prompts como código. | P | — |
| L2.4.4 | 🔒 *Prompt injection* (introducción): qué es, por qué no se resuelve solo con instrucciones y la regla de oro (todo contenido externo es dato no confiable). | M | — |

### [M3 · Asistentes de IA: uso profesional, contexto y delegación](../m03-asistentes/index.md)

36 h · Nivel 1 · 25 lecciones · **Prerrequisitos:** [M2](../m02-prompt-engineering/index.md) (duro).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.1.1 | Anatomía de un asistente moderno: modelo + *system prompt* + herramientas + memoria + interfaz. Qué es igual en todas y qué cambia. | C | — |
| L3.1.2 | Proyectos, conocimiento adjunto e instrucciones personalizadas: qué entra realmente al contexto y cuándo. | M | — |
| L3.1.3 | Memoria entre conversaciones: cómo funciona, cómo inspeccionarla, editarla y desactivarla. | M | — |
| L3.2.1 | Claude: conversación, proyectos, artifacts, búsqueda y research. Cómo decide cuánto trabajo hacer. | P | — |
| L3.2.2 | Trabajo agéntico en la app: archivos locales, tareas largas, permisos, tareas programadas, Docs, Slides y Design `[Beta]`. | P | — |
| L3.2.3 | Proyectos de Claude bien diseñados: instrucciones, documentos de conocimiento y su mantenimiento (aplicado a este mismo curso). | P | — |
| L3.3.1 | ChatGPT: conversaciones, instrucciones personalizadas, chats temporales y organización del trabajo (proyectos con memoria por defecto o solo del proyecto, proyectos compartidos, Space y Pages según disponibilidad). | P | — |
| L3.3.2 | ChatGPT: archivos, análisis de datos, búsqueda e investigación profunda (*deep research*): cuándo usar cada una, alcance, límites por plan y país, y cómo verificar las fuentes. | P | — |
| L3.3.3 | ChatGPT Work: delegar tareas largas que producen documentos, hojas de cálculo, presentaciones o sitios; tareas en sitios con sesión iniciada y confirmaciones antes de acciones con consecuencias `[Pago según plan]`. | P | — |
| L3.3.4 | ChatGPT: plugins (apps, skills y conectores en un mismo directorio), tareas programadas y disparadas por eventos de apps conectadas; permisos, Centro de privacidad y supervisión de lo que se ejecuta sin vos `[Disponibilidad según plan]`. | P | — |
| L3.3.5 | Gemini y el ecosistema Google: Gems, integración con Workspace y NotebookLM. | P | — |
| L3.3.6 | Asistente local y privado: Ollama con una interfaz de chat. Cuándo vale la pena (privacidad, costo cero) y sus límites. | P | — |
| L3.4.1 | Diseñar instrucciones y conocimiento de proyecto: qué escribir, qué evitar y cómo medir si mejora el resultado. | M | — |
| L3.4.2 | Conversaciones largas: degradación del contexto, cuándo empezar de nuevo, resúmenes de traspaso y memoria explícita. | M | — |
| L3.5.1 | Connectors y apps en Claude y ChatGPT (y Gemini como referencia): qué son (frecuentemente MCP bajo el capó), permisos que otorgan, lectura vs. escritura y cómo revocarlos. | P | — |
| L3.5.2 | Servidores MCP locales existentes en la app de escritorio: instalar y configurar uno (por ejemplo, sistema de archivos con alcance limitado), probarlo y revisar qué puede hacer. | P | — |
| L3.5.3 | Skills y plugins existentes en Claude y en ChatGPT: qué contiene un plugin en cada plataforma, cómo instalarlo, invocarlo y evaluar si realmente ayuda; revisar su contenido antes de instalarlo (scripts, connectors, permisos) y su costo de contexto. | P | — |
| L3.6.1 | Visión, documentos y audio: análisis de capturas, PDF, diagramas y voz. Qué funciona bien y dónde falla. | P | — |
| L3.6.2 | Agentes de navegador y uso de computadora: qué resuelven, cuándo conviene una API o un connector en su lugar, y 🔒 riesgos (sitios no confiables, credenciales, acciones irreversibles). | M | — |
| L3.7.1 | Especificar una tarea delegable: objetivo, contexto, criterios de aceptación, límites, permisos y entregable esperado. | M | — |
| L3.7.2 | Supervisar la ejecución agéntica: planes, puntos de control, aprobaciones, tareas programadas y cuándo interrumpir. | P | — |
| L3.7.3 | Verificar resultados: listas de control, contraste con fuentes, pruebas reproducibles y detección de errores plausibles. | P | — |
| L3.8.1 | 🔒 Privacidad: entrenamiento con tus datos, retención, planes personales vs. empresariales y qué nunca subir. | C | — |
| L3.8.2 | Propiedad intelectual, confidencialidad y políticas de uso de IA en empresas (fundamentos; profundización en E3). | C | — |
| L3.8.3 | 🧭 Matriz de decisión y diferencias prácticas entre Claude, ChatGPT y Gemini (contexto, memoria, agentes, extensiones, privacidad, planes); costos verificados al preparar la lección. | M | — |

### [M4 · Agentes de programación: uso guiado](../m04-agentes-programacion/index.md)

21 h · Nivel 1 · 14 lecciones · **Prerrequisitos:** [M2](../m02-prompt-engineering/index.md) (duro), [M3](../m03-asistentes/index.md) (recomendado).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L4.1.1 | Qué es un agente de programación y en qué se diferencia del autocompletado y del chat. Qué es común a todos (bucle, herramientas de lectura/edición/terminal, permisos, archivo de instrucciones) y por qué actuar en tu máquina exige cuidado. | C | — |
| L4.1.2 | Claude Code: acceso, instalación, primera sesión y superficies (terminal, IDE, escritorio y web). | P | — |
| L4.1.3 | Codex: acceso (cuenta de ChatGPT o clave de API), superficies (app de escritorio de ChatGPT, CLI, extensión para IDE, web y nube), instalación en Windows y primera sesión. | P | — |
| L4.2.1 | Explorar, planificar, implementar y verificar con tests: el mismo flujo en Claude Code (modo plan) y en Codex. | P | — |
| L4.2.2 | Pedidos concretos y verificables: cómo especificar una tarea de código (retoma L3.7.1). | M | — |
| L4.2.3 | Instrucciones persistentes: un `AGENTS.md` inicial que sirva a ambos agentes (convenciones, comandos de build y test, qué no tocar); cómo lo lee cada uno (Codex: cadena global → raíz → carpeta actual; Claude Code: `CLAUDE.md` o `AGENTS.md`). | P | — |
| L4.2.4 | Revisar y aceptar cambios: lectura de diffs, revisión asistida (`/review` en Codex, revisión en Claude Code), Git como red de seguridad, ramas y *commits* pequeños. | P | — |
| L4.3.1 | 🔒 Permisos y aislamiento: conceptos comunes (qué puede leer, escribir y ejecutar; acceso a red; aprobaciones) y su implementación en Claude Code (modos de permisos) y en Codex (modos de *sandbox* `read-only` / `workspace-write` / acceso total y políticas de aprobación). Qué permitir, qué preguntar siempre y qué nunca. | M | — |
| L4.3.2 | Usar servidores MCP y skills existentes desde ambos agentes (configuración de cada uno, invocación explícita e implícita). | P | — |
| L4.3.3 | Contexto y sesiones: cuándo compactar, cuándo empezar de cero, cómo retomar una sesión anterior en cada herramienta. | M | — |
| L4.4.1 | Configuración inicial de Codex (`config.toml`: modelo y esfuerzo, permisos, configuración por proyecto) y trabajo con repositorios (proyectos locales, *worktrees* para tareas en paralelo). | P | — |
| L4.4.2 | Codex en la nube: entornos, acceso a internet desactivado por defecto y lista de dominios permitidos, tareas en paralelo, revisión del resultado y *pull requests*. | P | — |
| L4.5.1 | 🧭 Qué delegar y qué no: tareas ideales, tareas riesgosas y señales de que el agente se está desviando. | M | — |
| L4.5.2 | Comparación práctica Claude Code vs. Codex: misma tarea, calidad, consumo, ergonomía, permisos y qué conviene para cada tipo de trabajo. | M | — |

### [M5 · Automatización con n8n: workflows deterministas](../m05-n8n/index.md)

18 h · Nivel 1 · 11 lecciones · **Prerrequisitos:** [M0](../m00-orientacion/index.md) (duro), [M2](../m02-prompt-engineering/index.md) (recomendado, solo para L5.3.3).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L5.1.1 | Qué es n8n y cuándo conviene frente a código propio u otras plataformas. Workflow determinista vs. agente (anticipo). | C | — |
| L5.1.2 | Instalación con Docker y PostgreSQL; estructura de una instancia. | P | — |
| L5.1.3 | Modelo de datos: ítems, JSON, expresiones y *mapping*. | P | — |
| L5.1.4 | *Triggers*: manual, programado, webhook y eventos de aplicaciones. | P | — |
| L5.2.1 | Webhooks entrantes y salientes; nodo HTTP Request contra API REST propias. | P | — |
| L5.2.2 | Bases de datos, archivos y servicios (correo, calendario, GitHub, Slack o Telegram). | P | — |
| L5.2.3 | Credenciales y 🔒 seguridad de n8n 2.x: *task runners*, aislamiento del nodo de código, variables de entorno bloqueadas, nodos deshabilitados por defecto y gestión de secretos. | M | — |
| L5.2.4 | Nodo de código (JavaScript/Python), subworkflows y reutilización. | P | — |
| L5.3.1 | Manejo de errores: *error workflows*, reintentos, idempotencia y alertas. | P | — |
| L5.3.2 | Guardar vs. publicar, exportación y versionado de workflows en Git. | P | — |
| L5.3.3 | Primer nodo LLM dentro de un workflow determinista (clasificar o resumir), con 💰 control de costo y validación de la salida. | M | — |

## Bloque II · Construir con modelos

### [M6 · Desarrollo con APIs de modelos](../m06-apis-modelos/index.md)

30 h · 14 lecciones · **Prerrequisitos:** [M2](../m02-prompt-engineering/index.md) (duro), [M3](../m03-asistentes/index.md) (recomendado).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L6.1.1 | Anatomía de una llamada: endpoint, autenticación, modelo, mensajes, parámetros y respuesta. Lo que hace el SDK por vos (con `curl` primero). | P | — |
| L6.1.2 | Conversaciones sin estado: por qué el cliente reenvía el historial y qué implica en costo y diseño. Variantes con estado del lado del proveedor. | C | — |
| L6.1.3 | *Streaming* (SSE): cuándo usarlo y cómo procesarlo. | P | — |
| L6.1.4 | Comparativa de API: Anthropic Messages, OpenAI Responses y Gemini. Conceptos equivalentes y diferencias. | M | — |
| L6.2.1 | Salidas estructuradas: JSON Schema, modo estricto, validación con Pydantic o Bean Validation. | P | — |
| L6.2.2 | Manejo de errores: límites de tasa, *timeouts*, reintentos con *backoff*, errores de contenido y respuestas truncadas. | P | — |
| L6.2.3 | Pruebas de código que llama a un LLM: *mocks*, *fixtures* grabadas y tests de contrato vs. evals. | P | — |
| L6.3.1 | Qué es tool calling: el modelo no ejecuta tu función, propone una llamada y tu código la ejecuta. El ciclo completo. | M | — |
| L6.3.2 | Diseño de herramientas: nombres, descripciones, esquemas y errores devueltos al modelo. | P | — |
| L6.3.3 | Llamadas paralelas, elección forzada de herramienta y herramientas ejecutadas por el proveedor (búsqueda web, ejecución de código): quién ejecuta qué y dónde. | M | — |
| L6.3.4 | 🔒 Riesgos de tool calling: validar argumentos, permisos mínimos y confirmación humana para acciones destructivas. | M | — |
| L6.4.1 | 💰 Caché de prompts, procesamiento por lotes (*batch*) y selección de modelo por tarea. | P | — |
| L6.4.2 | Portabilidad: API compatibles con OpenAI, Ollama, routers (por ejemplo LiteLLM u OpenRouter) y el costo de la abstracción. | M | — |
| L6.4.3 | LLM en Java con Spring AI 2.0: `ChatClient`, *advisors*, salidas estructuradas y herramientas. | P | — |

### [M7 · Context Engineering](../m07-context-engineering/index.md)

20 h · Nivel 2 · 11 lecciones · **Prerrequisitos:** [M6](../m06-apis-modelos/index.md) (duro); [M3](../m03-asistentes/index.md) y [M4](../m04-agentes-programacion/index.md) (recomendados: aportan la experiencia de uso que aquí se formaliza).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L7.1.1 | Qué es context engineering y por qué reemplazó al "prompt engineering" como habilidad central. | C | — |
| L7.1.2 | Componentes del contexto: instrucciones de sistema, definiciones de herramientas, conocimiento recuperado, memoria, historial y resultados de herramientas. Cuánto "pesa" cada uno. | M | — |
| L7.1.3 | Degradación del contexto (*context rot*): medirla y por qué más contexto no siempre es mejor. | M | — |
| L7.2.1 | Seleccionar: qué incluir y qué dejar afuera; recuperación bajo demanda vs. carga anticipada. | M | — |
| L7.2.2 | Comprimir: resúmenes, compactación y edición de contexto (limpiar resultados viejos de herramientas). | P | — |
| L7.2.3 | Aislar: dividir trabajo en subcontextos (anticipo de subagentes y multiagente). | C | — |
| L7.2.4 | Persistir: notas externas, archivos de estado y *memory tools*. | P | — |
| L7.2.5 | Orden y caché: estructurar el contexto para aprovechar la caché de prompts. | P | — |
| L7.3.1 | Tipos de memoria: de trabajo, episódica, semántica y procedimental. Cómo se implementa cada una. | C | — |
| L7.3.2 | Archivos de instrucciones a fondo (`CLAUDE.md`, `AGENTS.md`, instrucciones de proyecto): principios de diseño, alcance y medición de efecto (formaliza lo usado en M3 y M4). | M | — |
| L7.3.3 | Divulgación progresiva: el principio detrás de las Agent Skills y la búsqueda de herramientas. | C | — |

### [M8 · Embeddings, búsqueda semántica y RAG](../m08-rag/index.md)

34 h · 14 lecciones · **Prerrequisitos:** [M6](../m06-apis-modelos/index.md) y [M7](../m07-context-engineering/index.md) (duros).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L8.1.1 | Embeddings en profundidad: qué capturan, dimensiones, modelos, normalización y embeddings multimodales (texto e imagen en un mismo espacio). | M | — |
| L8.1.2 | Similitud (coseno, producto punto, euclídea) y búsqueda del vecino más cercano: exacta vs. aproximada. | M | — |
| L8.1.3 | Bases vectoriales: pgvector, Chroma y servicios gestionados. Índices HNSW e IVF; filtros por metadatos. | P | — |
| L8.2.1 | Arquitectura RAG: ingesta → indexación → recuperación → generación. Por qué funciona y dónde falla. | C | — |
| L8.2.2 | Ingesta: extracción de PDF, HTML y código; limpieza; metadatos. | P | — |
| L8.2.3 | *Chunking*: tamaño, solapamiento, por estructura y semántico. Efectos en la calidad. | M | — |
| L8.2.4 | Generación con contexto recuperado: prompt de RAG, citas y "no sé" cuando no hay evidencia. | P | — |
| L8.3.1 | Búsqueda híbrida y *reranking*. | P | — |
| L8.3.2 | Reescritura y expansión de consultas, HyDE y consultas multi-paso. | M | — |
| L8.3.3 | RAG agéntico: la recuperación como herramienta que decide el agente. | M | — |
| L8.3.4 | Alternativas y complementos: contexto largo, búsqueda tipo `grep` en agentes de código, GraphRAG. 🧭 Cuándo NO usar RAG y cuándo considerar *fine-tuning*. | C | — |
| L8.4.1 | 📏 Métricas: *recall* y precisión de recuperación, fidelidad (*faithfulness*) y relevancia de la respuesta. Construcción de un *dataset* de preguntas y respuestas. | M | — |
| L8.4.2 | Herramientas de evaluación de RAG (por ejemplo Ragas, promptfoo o LLM como juez) y sus límites. | P | — |
| L8.4.3 | Operación: actualización incremental, versionado del índice y 🔒 control de acceso por documento. | M | — |

## Bloque III · Agentes e interoperabilidad

### [M9 · Agentes desde cero](../m09-agentes-desde-cero/index.md)

30 h · 13 lecciones · **Prerrequisitos:** [M6](../m06-apis-modelos/index.md) y [M7](../m07-context-engineering/index.md) (duros), [M8](../m08-rag/index.md) (recomendado).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L9.1.1 | Workflows vs. agentes: control determinístico vs. control del modelo. Niveles de autonomía (de sugerir a actuar sin supervisión). | C | — |
| L9.1.2 | 🧭 Cuándo NO construir un agente: el costo de la autonomía (latencia, gasto, impredecibilidad). | C | — |
| L9.1.3 | Patrones de workflows con LLM: encadenamiento, enrutamiento, paralelización, orquestador-trabajadores y evaluador-optimizador. | M | — |
| L9.2.1 | El bucle agéntico mínimo en ~100 líneas: modelo, herramientas, observación y parada. | P | — |
| L9.2.2 | ReAct y razonamiento intercalado; uso de *thinking* entre llamadas a herramientas. | M | — |
| L9.2.3 | Diseño de herramientas para agentes: granularidad, idempotencia y errores informativos. | P | — |
| L9.2.4 | Condiciones de parada, límites de pasos y presupuesto, bucles infinitos y recuperación de errores. | P | — |
| L9.3.1 | Planificación explícita: planes, listas de tareas y re-planificación. | P | — |
| L9.3.2 | Memoria del agente: *scratchpad*, archivos de estado y memoria a largo plazo con RAG. | P | — |
| L9.3.3 | Tareas de larga duración: checkpoints y reanudación (concepto; se implementa en M14). | C | — |
| L9.4.1 | *Human-in-the-loop*: aprobaciones, puntos de control e interrupciones. | P | — |
| L9.4.2 | 🔒 Agencia excesiva: permisos mínimos, *sandboxing*, acciones reversibles vs. irreversibles. | M | — |
| L9.4.3 | 📏 Evaluar agentes: éxito de la tarea, trayectoria, costo y pasos. | P | — |

### [M10 · Model Context Protocol: desarrollo](../m10-mcp/index.md)

32 h · Nivel 2 · 16 lecciones · **Prerrequisitos:** [M9](../m09-agentes-desde-cero/index.md) (duro), [M3](../m03-asistentes/index.md) (recomendado: uso de connectors y MCP en Nivel 1).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L10.1.1 | Repaso del Nivel 1 y qué problema resuelve MCP. Historia, gobernanza (Agentic AI Foundation) y adopción. | C | — |
| L10.1.2 | Host, cliente y servidor: quién hace qué. MCP como "tool calling estandarizado y descubrible". | C | — |
| L10.1.3 | Primitivas del servidor: herramientas, recursos y prompts. Cuándo usar cada una. | M | — |
| L10.1.4 | Interacción con el cliente: elicitación mediante el patrón *multi round-trip requests* (MRTR). Roots, Sampling y Logging: qué eran, por qué se deprecan y con qué se reemplazan. | C | — |
| L10.1.5 | Transportes: stdio vs. Streamable HTTP (HTTP+SSE deprecado). Núcleo sin estado de la especificación 2026-07-28 (`server/discover`, sin sesiones de protocolo) y qué cambia respecto de la 2025-11-25. | M | — |
| L10.2.1 | Primer servidor en Python: herramientas y recursos, probado con MCP Inspector. | P | — |
| L10.2.2 | Servidor en Java con Spring AI (`@McpTool`, `@McpResource`) sobre una API REST o base de datos existente. | P | — |
| L10.2.3 | Diseño de servidores para agentes: pocas herramientas bien descritas vs. "envolver toda la API". Errores, paginación, orden determinista y caché de listas. | M | — |
| L10.2.4 | Extensiones oficiales: Tasks (operaciones largas), MCP Apps (interfaces interactivas) y Skills over MCP. Concepto y ejemplo según soporte de SDK y host `[Verificar]`. | M | — |
| L10.3.1 | Configuración avanzada en hosts: ámbitos, servidores remotos con OAuth, variables y depuración (amplía L3.5.2 y L4.3.2). | P | — |
| L10.3.2 | Construir un cliente MCP propio e integrarlo al agente de P5. | P | — |
| L10.3.3 | Ecosistema: registros de servidores y cómo evaluarlos antes de instalarlos. | M | — |
| L10.4.1 | 🔒 Autorización en servidores remotos: OAuth 2.1/OIDC, *scopes*, tokens y registro de clientes (Client ID Metadata Documents; Dynamic Client Registration deprecado). | M | — |
| L10.4.2 | 🔒 Amenazas: *tool poisoning*, *prompt injection* indirecta vía resultados, *confused deputy*, robo de credenciales y servidores maliciosos. Mitigaciones. | M | — |
| L10.4.3 | Despliegue remoto (contenedor, *serverless*), observabilidad con trazas (OpenTelemetry) y versionado. | P | — |
| L10.4.4 | 🧭 MCP vs. API directa vs. skill vs. A2A: cuándo usar cada uno. | C | — |

### [M11 · Agentes de programación: arquitectura y configuración avanzada](../m11-agentes-programacion-avanzado/index.md)

25 h · Nivel 2 · 14 lecciones · **Prerrequisitos:** [M4](../m04-agentes-programacion/index.md) y [M7](../m07-context-engineering/index.md) (duros), [M10](../m10-mcp/index.md) (recomendado, para L11.3.2).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L11.1.1 | Anatomía del *harness*: bucle, herramientas (lectura, edición, terminal, búsqueda), contexto y permisos. Comparación entre Claude Code, Codex y tu agente de P5. | C | — |
| L11.1.2 | Cómo gestiona el contexto un agente de programación: compactación, memoria, carga de instrucciones y skills, búsqueda en el código vs. RAG. Diferencias entre ambas herramientas. | C | — |
| L11.2.1 | `AGENTS.md` y `CLAUDE.md` a fondo: jerarquía, alcance por carpeta, archivos de anulación y límites de tamaño en Codex, memoria en Claude Code; mantenimiento y medición de efecto. | M | — |
| L11.2.2 | Portabilidad de la configuración entre agentes: qué es estándar (`AGENTS.md`, Agent Skills, MCP) y qué es propio (`config.toml` de Codex, `settings.json` de Claude Code, hooks, extensiones de skills). | M | — |
| L11.3.1 | 🔒 Permisos avanzados y aislamiento: políticas por proyecto y organización en Claude Code; en Codex, modos de *sandbox*, políticas de aprobación, revisión automática de aprobaciones, reglas de ejecución y el *sandbox* nativo de Windows. | P | — |
| L11.3.2 | Tu servidor MCP (P6) en ambos agentes: configuración, autenticación OAuth, herramientas permitidas o bloqueadas y aprobación por herramienta. | P | — |
| L11.3.3 | Hooks y automatismos del ciclo de vida: hooks de Claude Code (formateo, lint, tests, bloqueos de seguridad) y su equivalente en Codex, si existe en la versión vigente `[Verificar]`. | P | — |
| L11.3.4 | Subagentes y trabajo en paralelo: subagentes de Claude Code; tareas en paralelo con *worktrees* y en la nube en Codex; cuándo aislar contexto. | M | — |
| L11.3.5 | Primera skill propia dentro del agente de programación: ubicaciones (`.claude/skills` y `.agents/skills`), invocación explícita e implícita, y una misma skill usada en Claude Code y en Codex (el desarrollo a fondo sigue en M12). | P | — |
| L11.4.1 | Modo no interactivo y scripting: `claude -p` y `codex exec` (salida JSON, salida con esquema, *sandbox* de solo lectura por defecto en Codex, reanudar sesiones). | P | — |
| L11.4.2 | Agentes en CI: revisión de PR y corrección de fallas con la integración de GitHub Actions de Claude Code y con la acción oficial de Codex (separar el job que ejecuta al agente del job con permisos de escritura); revisión de código automática en GitHub. | P | — |
| L11.4.3 | Tareas programadas y en la nube: Routines y tareas de escritorio de Claude Code; tareas programadas de Codex (locales en *worktree* o en la nube para equipos). Límites y riesgos de la ejecución desatendida `[Pago]`. | M | — |
| L11.5.1 | Revisión de código generado a escala: calidad, seguridad y deuda técnica. | M | — |
| L11.5.2 | 📏 Medir la eficacia de cada agente en tu repositorio: tareas de referencia, tasa de éxito, intervenciones y costo. | P | — |

### [M12 · Skills y plugins: desarrollo](../m12-skills-plugins/index.md)

18 h · Nivel 2 · 10 lecciones · **Prerrequisitos:** [M3](../m03-asistentes/index.md) y [M11](../m11-agentes-programacion-avanzado/index.md) (duros).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L12.1.1 | Repaso del Nivel 1. Divulgación progresiva y cómo decide el agente activar una skill. | C | — |
| L12.1.2 | Anatomía: `SKILL.md` (metadatos, descripción que dispara la activación, instrucciones), `scripts/`, `references/`, `assets/`. Campos del estándar vs. extensiones de cada cliente (por ejemplo, controles de invocación de Claude Code o `agents/openai.yaml` de Codex) y límites de carga de cada cliente. | M | — |
| L12.1.3 | Escribir buenas skills: descripciones precisas, instrucciones concisas, scripts deterministas para lo que no debe "improvisar" el modelo. | P | — |
| L12.1.4 | 📏 Probar y evaluar skills: ¿se activa cuando debe? ¿mejora el resultado? Iteración. | P | — |
| L12.2.1 | 🧭 Skill vs. servidor MCP vs. subagente vs. comando vs. hook vs. `AGENTS.md`: matriz de decisión. | C | — |
| L12.2.2 | Portabilidad: la misma skill en Claude, Claude Code, Codex, Gemini CLI y Spring AI; skills distribuidas por MCP. Qué se rompe y por qué. | P | — |
| L12.3.1 | Plugins en dos ecosistemas: plugins de Claude (skills, comandos, agentes, hooks, servidores MCP; qué carga cada superficie) y plugins de ChatGPT/Codex (skills, servidores MCP y hooks del ciclo de vida, con un directorio compartido). Qué es común y qué no es portable. | M | — |
| L12.3.2 | Marketplaces y distribución: públicos, privados y de equipo. Versionado y actualización. | P | — |
| L12.3.3 | 🔒 Cadena de suministro: revisar skills y plugins de terceros (scripts, permisos, connectors) y procedencia. | M | — |
| L12.3.4 | 💰 Medir costo de contexto y uso de un plugin; evals de plugins. | P | — |

## Bloque IV · Automatización y sistemas avanzados

### [M13 · n8n con IA y agentes](../m13-n8n-ia/index.md)

24 h · Nivel 2 · 10 lecciones · **Prerrequisitos:** [M5](../m05-n8n/index.md), [M6](../m06-apis-modelos/index.md) y [M9](../m09-agentes-desde-cero/index.md) (duros); [M8](../m08-rag/index.md) y [M10](../m10-mcp/index.md) (recomendados, para L13.3.1 y L13.3.2).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L13.1.1 | Nodos de LLM con salida estructurada y validación: clasificación, extracción y resumen (amplía L5.3.3). | P | — |
| L13.1.2 | Patrones de workflows con LLM en n8n: encadenamiento, enrutamiento, paralelización y evaluador-optimizador (mapeo con L9.1.3). | M | — |
| L13.2.1 | Nodo AI Agent: modelo, memoria y herramientas. Mapeo con el bucle de M9. | M | — |
| L13.2.2 | Herramientas del agente: nodos, HTTP y workflows como herramientas. | P | — |
| L13.2.3 | Aprobación humana dentro de workflows (esperar confirmación por correo o chat). | P | — |
| L13.3.1 | RAG en n8n: ingesta a un vector store y agente con recuperación. | P | — |
| L13.3.2 | MCP en n8n: consumir servidores MCP (MCP Client Tool) y exponer workflows como servidor MCP (MCP Server Trigger). | P | — |
| L13.4.1 | Monitoreo de ejecuciones, 💰 costos de LLM y límites. | P | — |
| L13.4.2 | Escalado y entornos: modo cola, réplicas y consideraciones para endpoints MCP `[Verificar]`. | M | — |
| L13.4.3 | 🧭 Workflow determinista + LLM puntual vs. agente autónomo; n8n vs. código propio. | C | — |

### [M14 · Frameworks y SDK de agentes para producción](../m14-frameworks-agentes/index.md)

36 h · 11 lecciones · **Prerrequisitos:** [M9](../m09-agentes-desde-cero/index.md) (duro), [M10](../m10-mcp/index.md) (recomendado).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L14.1.1 | Qué aporta un framework sobre tu agente de P5: estado, herramientas, memoria, trazas y despliegue. El costo de la abstracción. | C | — |
| L14.1.2 | 🧭 Mapa de opciones vigente (Python, TypeScript y Java), su estado de mantenimiento y matriz de decisión. | C | — |
| L14.2.1 | Claude Agent SDK: el *harness* de Claude Code como librería. Herramientas, permisos, subagentes y MCP. Referencia: el SDK de Codex como enfoque equivalente del otro proveedor `[Verificar alcance]`. | P | — |
| L14.2.2 | OpenAI Agents SDK: agentes, *handoffs*, *guardrails* y sesiones. | P | — |
| L14.2.3 | Runtimes gestionados (por ejemplo Claude Managed Agents): cuándo delegar la infraestructura `[Pago]`. | M | — |
| L14.3.1 | LangGraph: grafos de estado, nodos, aristas condicionales, checkpoints e interrupciones para aprobación humana. | P | — |
| L14.3.2 | Agentes en Java: Spring AI 2.0 (bucle en la cadena de *advisors*, herramientas y MCP) y comparación con LangChain4j y Google ADK para Java. | P | — |
| L14.4.1 | Ejecución durable: persistencia del estado, reintentos y reanudación tras fallos. | P | — |
| L14.4.2 | Memoria a largo plazo: estrategias y almacenamiento. | M | — |
| L14.4.3 | *Guardrails* de entrada y salida, validación y límites. | P | — |
| L14.4.4 | Exponer un agente como servicio: API, *streaming* de eventos, autenticación y despliegue en contenedor. | P | — |

### [M15 · Sistemas multiagente](../m15-multiagente/index.md)

26 h · 11 lecciones · **Prerrequisitos:** [M14](../m14-frameworks-agentes/index.md) (duro).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L15.1.1 | 🧭 Cuándo varios agentes superan a uno (y cuándo no): evidencia, costos y la regla de "empezar con uno". | C | — |
| L15.1.2 | Topologías y patrones de coordinación. | C | — |
| L15.1.3 | Delegación efectiva entre agentes: qué contexto pasar, formato de resultados y criterios de terminación (versión programática de L3.7.1). | M | — |
| L15.2.1 | Orquestador-trabajadores con investigación en paralelo. | P | — |
| L15.2.2 | *Handoffs* entre agentes especializados y estado compartido. | P | — |
| L15.2.3 | Evaluador-optimizador y revisión cruzada entre agentes. | P | — |
| L15.3.1 | El protocolo A2A 1.0: Agent Cards (incluidas las firmadas), tareas, mensajes y artefactos. | C | — |
| L15.3.2 | Exponer y consumir un agente vía A2A; A2A + MCP en una misma arquitectura. | P | — |
| L15.4.1 | 📏 Evaluar sistemas multiagente: éxito global, contribución de cada agente y trazas. | P | — |
| L15.4.2 | Fallos típicos: duplicación de trabajo, delegación vaga, bucles entre agentes y explosión de costos. 💰 Presupuestos por agente. | M | — |
| L15.4.3 | 🔒 Confianza entre agentes: propagación de *prompt injection*, identidad y permisos por agente. | M | — |

## Bloque V · Producción e integración

### [M16 · Seguridad, evaluación, observabilidad y operación](../m16-produccion/index.md)

36 h · 16 lecciones · **Prerrequisitos:** [M13](../m13-n8n-ia/index.md) y [M14](../m14-frameworks-agentes/index.md) (duros); [M12](../m12-skills-plugins/index.md) y [M15](../m15-multiagente/index.md) (recomendados).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L16.1.1 | Modelado de amenazas para aplicaciones y agentes con LLM: activos, fronteras de confianza y la "tríada letal" (datos privados + contenido no confiable + capacidad de comunicación externa). | M | — |
| L16.1.2 | OWASP Top 10 LLM 2026 y Top 10 de aplicaciones agénticas: recorrido con ejemplos sobre tus proyectos. | M | — |
| L16.1.3 | Defensa contra *prompt injection*: por qué no hay solución completa; aislamiento, permisos, confirmación humana y separación de privilegios. | M | — |
| L16.1.4 | Identidad y credenciales de agentes: secretos, tokens de corta duración y permisos mínimos por herramienta. | P | — |
| L16.1.5 | Privacidad: datos personales, minimización, anonimización y retención en proveedores. | C | — |
| L16.2.1 | Estrategia de evaluación: tipos (deterministas, basados en modelo, humanos) y qué medir en cada tipo de sistema. | C | — |
| L16.2.2 | LLM como juez: diseño de rúbricas, calibración con humanos y sesgos. | P | — |
| L16.2.3 | Evals en integración continua: regresión al cambiar prompts, modelos o herramientas. | P | — |
| L16.2.4 | *Red teaming* y evaluación adversarial. | P | — |
| L16.3.1 | Trazas de LLM y agentes con OpenTelemetry: spans, atributos y convenciones. | P | — |
| L16.3.2 | Plataformas LLMOps (Langfuse o Phoenix): trazas, *datasets*, evaluaciones en línea y *feedback*. | P | — |
| L16.3.3 | Depurar agentes: leer trayectorias, reproducir fallos y análisis de errores sistemático. | P | — |
| L16.4.1 | 💰 Optimización: enrutamiento por modelo, caché, *batch*, compresión de contexto y presupuestos. | P | — |
| L16.4.2 | Confiabilidad: *fallbacks* entre proveedores, límites de tasa, *timeouts* y degradación controlada. | P | — |
| L16.4.3 | Mantenimiento: deprecación de modelos, API y herramientas (casos reales: Assistants API, Agent Builder), migraciones y deriva. | M | — |
| L16.4.4 | Gobernanza mínima: registro de decisiones, auditoría y documentación de sistemas de IA. | C | — |

### [M17 · Proyecto final integrador](../m17-proyecto-final/index.md)

50 h · 8 lecciones · **Prerrequisitos:** [M16](../m16-produccion/index.md) (duro).

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L17.1.1 | Elección del problema y definición de requisitos, métricas de éxito y restricciones (costo, privacidad). | M | — |
| L17.1.2 | Arquitectura y decisiones técnicas documentadas (ADR): qué es determinista, qué es agente, qué es RAG, qué es MCP y qué es n8n. | M | — |
| L17.1.3 | Modelo de amenazas y plan de evaluación antes de construir. | M | — |
| L17.2.1 | Hito 1: núcleo funcional mínimo con evals. | P | — |
| L17.2.2 | Hito 2: integraciones (MCP, n8n y datos). | P | — |
| L17.2.3 | Hito 3: seguridad, observabilidad y costos. | P | — |
| L17.3.1 | Evaluación final, informe de métricas y análisis de costos. | P | — |
| L17.3.2 | Documentación, demostración y retrospectiva. | M | — |

## Electivas

Especializaciones opcionales, sin lecciones numeradas: ver [Electivas](../electivas.md).
