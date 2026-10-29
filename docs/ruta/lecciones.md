<!-- Generado por scripts/generar.py a partir de las portadas de los módulos. No editar a mano. -->

# Todas las lecciones

Las 233 lecciones del curso, etapa por etapa. **9 tienen material**: son las que llevan enlace. Las demás ya forman parte del programa y se están escribiendo.

**Tipo de lección:** *Conceptual* (se comprueba con preguntas), *Práctica* (con un ejercicio) o *Mixta* (las dos cosas). **Ruta:** las lecciones *esenciales* son el núcleo de cada módulo; las marcadas para *profundizar* amplían el tema y se pueden hacer después.

## Etapa 1 · Fundamentos y uso profesional

### [Módulo 0 · Orientación y entorno de trabajo](../m00-orientacion/index.md)

6 h · 4 lecciones · **Prerrequisitos:** ninguno.

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L0.1.1 | **[Cómo funciona este curso](../m00-orientacion/l0-1-1-mapa-del-curso.md)**<br>Etapas, módulos y lecciones; prerrequisitos; Nivel 1 y Nivel 2; estados de una lección y cómo llevar tu avance. | Conceptual | Esencial | 📝 Borrador |
| L0.1.2 | **[Aprender en un campo que cambia cada mes](../m00-orientacion/l0-1-2-aprender-en-un-campo-que-cambia.md)**<br>Cómo aprender en un campo que cambia cada mes: fuentes oficiales, *changelogs* y cómo verificar lo que dice un modelo (incluido un tutor de IA). | Conceptual | Esencial | 📝 Borrador |
| L0.2.1 | **[Repositorio y entorno de trabajo](../m00-orientacion/l0-2-1-repositorio-y-entorno.md)**<br>Repositorio Git del curso (registros, apuntes y proyectos), estructura de carpetas, entornos de Python y Java, Docker. | Práctica | Esencial | 📝 Borrador |
| L0.2.2 | **[Claves de API y primer modelo local](../m00-orientacion/l0-2-2-claves-y-modelo-local.md)**<br>Claves de API: creación, almacenamiento seguro (`.env`, gestor de secretos, nunca en Git), límites de gasto y alertas. Instalación de Ollama y primer modelo local. | Práctica | Esencial | 📝 Borrador |

### [Módulo 1 · Fundamentos de IA generativa y LLM](../m01-fundamentos-llm/index.md)

24 h · 16 lecciones · **Prerrequisitos:** [Módulo 0](../m00-orientacion/index.md) (indispensable).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L1.1.1 | **[IA, ML, deep learning e IA generativa](../m01-fundamentos-llm/l1-1-1-ia-ml-deep-learning.md)**<br>Definiciones precisas y qué problema resuelve cada uno. | Conceptual | Esencial | 📝 Borrador |
| L1.1.2 | **Redes neuronales en 90 minutos**<br>Parámetros, entrenamiento y generalización (lo justo para entender LLM, sin matemática innecesaria). | Conceptual | Profundizar | Próximamente |
| L1.1.3 | **[Qué es un modelo de lenguaje](../m01-fundamentos-llm/l1-1-3-que-es-un-modelo-de-lenguaje.md)**<br>Predecir el próximo token. Por qué algo tan simple produce comportamientos complejos. | Conceptual | Esencial | 📝 Borrador |
| L1.2.1 | **[Tokens y tokenización](../m01-fundamentos-llm/l1-2-1-tokens-y-tokenizacion.md)**<br>BPE, por qué el español "cuesta" más tokens, cómo se tokenizan imágenes y otros formatos, impacto en costo y límites. | Mixta | Esencial | 📝 Borrador |
| L1.2.2 | **[Embeddings](../m01-fundamentos-llm/l1-2-2-embeddings.md)**<br>El contenido como vectores, similitud semántica (intro práctica; se profundiza en M8). | Mixta | Esencial | 📝 Borrador |
| L1.2.3 | **[Transformers y atención](../m01-fundamentos-llm/l1-2-3-transformers-y-atencion.md)**<br>Intuición del mecanismo, por qué permite contexto largo y qué significa "ventana de contexto". | Conceptual | Esencial | 📝 Borrador |
| L1.3.1 | **Preentrenamiento**<br>Datos, escala y fecha de corte de conocimiento. | Conceptual | Profundizar | Próximamente |
| L1.3.2 | **Post-entrenamiento**<br>Ajuste por instrucciones, RLHF y técnicas afines, *system prompts*. Por qué un modelo "asistente" se comporta distinto que un modelo base. | Conceptual | Esencial | Próximamente |
| L1.3.3 | **Modelos de razonamiento**<br>Modelos de razonamiento (*thinking*): qué cambia, cuándo convienen y su costo. | Conceptual | Esencial | Próximamente |
| L1.4.1 | **Generación token a token y muestreo**<br>Temperatura, top-p, top-k, *stop sequences* y máximo de tokens. Determinismo y por qué no está garantizado. | Mixta | Esencial | Próximamente |
| L1.4.2 | **Ventana de contexto en la práctica**<br>Entrada, salida, efecto "perdido en el medio" y degradación con contextos largos. | Mixta | Esencial | Próximamente |
| L1.4.3 | **Latencia, throughput y costos**<br>Latencia, *throughput* y costos: tokens de entrada, salida y razonamiento; *streaming*. | Mixta | Esencial | Próximamente |
| L1.5.1 | **Alucinaciones**<br>Por qué ocurren (no es un bug, es la naturaleza del modelo) y estrategias de mitigación. | Mixta | Esencial | Próximamente |
| L1.5.2 | **Multimodalidad**<br>Visión, audio, generación de imágenes. Qué es nativo y qué es un sistema combinado. | Conceptual | Profundizar | Próximamente |
| L1.5.3 | **Panorama de modelos**<br>Cerrados (Claude, GPT, Gemini) y abiertos (Llama, Qwen, Mistral, DeepSeek, Gemma); niveles de tamaño; cómo leer (y desconfiar de) los *benchmarks*. Versiones vigentes verificadas al preparar la lección. | Conceptual | Esencial | Próximamente |
| L1.5.4 | **Modelo, producto y harness**<br>Modelo vs. producto vs. *harness*: la diferencia entre un modelo, la app que lo envuelve y el agente que lo usa. Clave para todo el curso. | Conceptual | Esencial | Próximamente |

### [Módulo 2 · Prompt Engineering](../m02-prompt-engineering/index.md)

20 h · 15 lecciones · **Prerrequisitos:** [Módulo 1](../m01-fundamentos-llm/index.md) (indispensable).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L2.1.1 | **Qué es un prompt para el modelo**<br>Todo es contexto (texto, archivos, imágenes). Roles y estructura de mensajes. | Conceptual | Esencial | Próximamente |
| L2.1.2 | **Claridad y especificidad**<br>Tarea, contexto, restricciones, formato y criterio de éxito. El "test del colega nuevo". | Mixta | Esencial | Próximamente |
| L2.1.3 | **System prompt y mensaje de usuario**<br>*System prompt* vs. mensaje de usuario: qué va en cada uno y por qué. | Conceptual | Esencial | Próximamente |
| L2.2.1 | **Ejemplos (few-shot)**<br>Ejemplos (*few-shot*): cuántos, cuáles, cómo evitar que el modelo copie de más. | Mixta | Esencial | Próximamente |
| L2.2.2 | **Estructura con delimitadores y XML**<br>Estructura con delimitadores y XML; documentos largos al principio y pregunta al final. | Mixta | Esencial | Próximamente |
| L2.2.3 | **Razonamiento paso a paso**<br>Razonamiento paso a paso y modelos con *thinking*: cuándo pedirlo, cuándo sobra. | Mixta | Esencial | Próximamente |
| L2.2.4 | **Prompt chaining**<br>Descomposición y encadenamiento de prompts (*prompt chaining*). | Mixta | Esencial | Próximamente |
| L2.2.5 | **Control del formato de salida**<br>JSON, Markdown y plantillas (preparación para salidas estructuradas en M6). | Práctica | Esencial | Próximamente |
| L2.3.1 | **Prompts para tareas de desarrollo**<br>Revisión de código, generación de tests, documentación, análisis de logs. | Práctica | Esencial | Próximamente |
| L2.3.2 | **Portabilidad de prompts entre modelos**<br>Diferencias entre modelos y portabilidad de prompts: qué es transferible y qué es específico. | Mixta | Profundizar | Próximamente |
| L2.3.3 | **Meta-prompting**<br>Usar un LLM para mejorar prompts, y sus límites. | Mixta | Profundizar | Próximamente |
| L2.4.1 | **Por qué probar una vez no alcanza**<br>Por qué "lo probé una vez y anduvo" no alcanza: variabilidad y casos de prueba. | Conceptual | Esencial | Próximamente |
| L2.4.2 | **Primer conjunto de evaluación**<br>Casos, salidas esperadas y criterios. Comparación A/B con promptfoo. | Práctica | Esencial | Próximamente |
| L2.4.3 | **Versionado de prompts como código** | Práctica | Profundizar | Próximamente |
| L2.4.4 | **Prompt injection: introducción**<br>*Prompt injection* (introducción): qué es, por qué no se resuelve solo con instrucciones y la regla de oro (todo contenido externo es dato no confiable). | Mixta | Esencial | Próximamente |

### [Módulo 3 · Asistentes de IA en la práctica](../m03-asistentes/index.md)

36 h · Nivel 1 · 25 lecciones · **Prerrequisitos:** [Módulo 2](../m02-prompt-engineering/index.md) (indispensable).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L3.1.1 | **Anatomía de un asistente moderno**<br>Modelo + *system prompt* + herramientas + memoria + interfaz. Qué es igual en todas y qué cambia. | Conceptual | Esencial | Próximamente |
| L3.1.2 | **Proyectos, conocimiento e instrucciones**<br>Proyectos, conocimiento adjunto e instrucciones personalizadas: qué entra realmente al contexto y cuándo. | Mixta | Esencial | Próximamente |
| L3.1.3 | **Memoria entre conversaciones**<br>Cómo funciona, cómo inspeccionarla, editarla y desactivarla. | Mixta | Esencial | Próximamente |
| L3.2.1 | **Claude: conversación, proyectos y research**<br>Claude: conversación, proyectos, artifacts, búsqueda y research. Cómo decide cuánto trabajo hacer. | Práctica | Esencial | Próximamente |
| L3.2.2 | **Claude: trabajo agéntico en la app**<br>Trabajo agéntico en la app: archivos locales, tareas largas, permisos, tareas programadas, Docs, Slides y Design `[Beta]`. | Práctica | Esencial | Próximamente |
| L3.2.3 | **Proyectos de Claude bien diseñados**<br>Instrucciones, documentos de conocimiento y su mantenimiento (aplicado a este mismo curso). | Práctica | Esencial | Próximamente |
| L3.3.1 | **ChatGPT: conversaciones y proyectos**<br>ChatGPT: conversaciones, instrucciones personalizadas, chats temporales y organización del trabajo (proyectos con memoria por defecto o solo del proyecto, proyectos compartidos, Space y Pages según disponibilidad). | Práctica | Esencial | Próximamente |
| L3.3.2 | **ChatGPT: archivos, datos y deep research**<br>ChatGPT: archivos, análisis de datos, búsqueda e investigación profunda (*deep research*): cuándo usar cada una, alcance, límites por plan y país, y cómo verificar las fuentes. | Práctica | Esencial | Próximamente |
| L3.3.3 | **ChatGPT Work: delegar tareas largas**<br>ChatGPT Work: delegar tareas largas que producen documentos, hojas de cálculo, presentaciones o sitios; tareas en sitios con sesión iniciada y confirmaciones antes de acciones con consecuencias `[Pago según plan]`. | Práctica | Esencial | Próximamente |
| L3.3.4 | **ChatGPT: plugins y tareas programadas**<br>ChatGPT: plugins (apps, skills y conectores en un mismo directorio), tareas programadas y disparadas por eventos de apps conectadas; permisos, Centro de privacidad y supervisión de lo que se ejecuta sin vos `[Disponibilidad según plan]`. | Práctica | Esencial | Próximamente |
| L3.3.5 | **Gemini y el ecosistema Google**<br>Gems, integración con Workspace y NotebookLM. | Práctica | Profundizar | Próximamente |
| L3.3.6 | **Asistente local y privado**<br>Ollama con una interfaz de chat. Cuándo vale la pena (privacidad, costo cero) y sus límites. | Práctica | Profundizar | Próximamente |
| L3.4.1 | **Diseñar instrucciones de proyecto**<br>Diseñar instrucciones y conocimiento de proyecto: qué escribir, qué evitar y cómo medir si mejora el resultado. | Mixta | Esencial | Próximamente |
| L3.4.2 | **Conversaciones largas**<br>Degradación del contexto, cuándo empezar de nuevo, resúmenes de traspaso y memoria explícita. | Mixta | Esencial | Próximamente |
| L3.5.1 | **Connectors y apps**<br>Connectors y apps en Claude y ChatGPT (y Gemini como referencia): qué son (frecuentemente MCP bajo el capó), permisos que otorgan, lectura vs. escritura y cómo revocarlos. | Práctica | Esencial | Próximamente |
| L3.5.2 | **Servidores MCP locales**<br>Servidores MCP locales existentes en la app de escritorio: instalar y configurar uno (por ejemplo, sistema de archivos con alcance limitado), probarlo y revisar qué puede hacer. | Práctica | Esencial | Próximamente |
| L3.5.3 | **Skills y plugins existentes**<br>Skills y plugins existentes en Claude y en ChatGPT: qué contiene un plugin en cada plataforma, cómo instalarlo, invocarlo y evaluar si realmente ayuda; revisar su contenido antes de instalarlo (scripts, connectors, permisos) y su costo de contexto. | Práctica | Esencial | Próximamente |
| L3.6.1 | **Visión, documentos y audio**<br>Análisis de capturas, PDF, diagramas y voz. Qué funciona bien y dónde falla. | Práctica | Profundizar | Próximamente |
| L3.6.2 | **Agentes de navegador y uso de computadora**<br>Qué resuelven, cuándo conviene una API o un connector en su lugar, y riesgos (sitios no confiables, credenciales, acciones irreversibles). | Mixta | Profundizar | Próximamente |
| L3.7.1 | **Especificar una tarea delegable**<br>Objetivo, contexto, criterios de aceptación, límites, permisos y entregable esperado. | Mixta | Esencial | Próximamente |
| L3.7.2 | **Supervisar la ejecución agéntica**<br>Planes, puntos de control, aprobaciones, tareas programadas y cuándo interrumpir. | Práctica | Esencial | Próximamente |
| L3.7.3 | **Verificar resultados**<br>Listas de control, contraste con fuentes, pruebas reproducibles y detección de errores plausibles. | Práctica | Esencial | Próximamente |
| L3.8.1 | **Privacidad**<br>Entrenamiento con tus datos, retención, planes personales vs. empresariales y qué nunca subir. | Conceptual | Esencial | Próximamente |
| L3.8.2 | **Propiedad intelectual y políticas de uso**<br>Propiedad intelectual, confidencialidad y políticas de uso de IA en empresas (fundamentos; profundización en E3). | Conceptual | Profundizar | Próximamente |
| L3.8.3 | **Matriz de decisión: Claude, ChatGPT y Gemini**<br>Matriz de decisión y diferencias prácticas entre Claude, ChatGPT y Gemini (contexto, memoria, agentes, extensiones, privacidad, planes); costos verificados al preparar la lección. | Mixta | Esencial | Próximamente |

### [Módulo 4 · Agentes de programación](../m04-agentes-programacion/index.md)

21 h · Nivel 1 · 14 lecciones · **Prerrequisitos:** [Módulo 2](../m02-prompt-engineering/index.md) (indispensable), [Módulo 3](../m03-asistentes/index.md) (recomendado).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L4.1.1 | **Qué es un agente de programación**<br>Qué es un agente de programación y en qué se diferencia del autocompletado y del chat. Qué es común a todos (bucle, herramientas de lectura/edición/terminal, permisos, archivo de instrucciones) y por qué actuar en tu máquina exige cuidado. | Conceptual | Esencial | Próximamente |
| L4.1.2 | **Claude Code: primeros pasos**<br>Claude Code: acceso, instalación, primera sesión y superficies (terminal, IDE, escritorio y web). | Práctica | Esencial | Próximamente |
| L4.1.3 | **Codex: primeros pasos**<br>Codex: acceso (cuenta de ChatGPT o clave de API), superficies (app de escritorio de ChatGPT, CLI, extensión para IDE, web y nube), instalación en Windows y primera sesión. | Práctica | Esencial | Próximamente |
| L4.2.1 | **Explorar, planificar, implementar y verificar**<br>Explorar, planificar, implementar y verificar con tests: el mismo flujo en Claude Code (modo plan) y en Codex. | Práctica | Esencial | Próximamente |
| L4.2.2 | **Pedidos concretos y verificables**<br>Cómo especificar una tarea de código (retoma L3.7.1). | Mixta | Esencial | Próximamente |
| L4.2.3 | **Instrucciones persistentes**<br>Un `AGENTS.md` inicial que sirva a ambos agentes (convenciones, comandos de build y test, qué no tocar); cómo lo lee cada uno (Codex: cadena global → raíz → carpeta actual; Claude Code: `CLAUDE.md` o `AGENTS.md`). | Práctica | Esencial | Próximamente |
| L4.2.4 | **Revisar y aceptar cambios**<br>Lectura de diffs, revisión asistida (`/review` en Codex, revisión en Claude Code), Git como red de seguridad, ramas y *commits* pequeños. | Práctica | Esencial | Próximamente |
| L4.3.1 | **Permisos y aislamiento**<br>Conceptos comunes (qué puede leer, escribir y ejecutar; acceso a red; aprobaciones) y su implementación en Claude Code (modos de permisos) y en Codex (modos de *sandbox* `read-only` / `workspace-write` / acceso total y políticas de aprobación). Qué permitir, qué preguntar siempre y qué nunca. | Mixta | Esencial | Próximamente |
| L4.3.2 | **MCP y skills en los agentes**<br>Usar servidores MCP y skills existentes desde ambos agentes (configuración de cada uno, invocación explícita e implícita). | Práctica | Esencial | Próximamente |
| L4.3.3 | **Contexto y sesiones**<br>Cuándo compactar, cuándo empezar de cero, cómo retomar una sesión anterior en cada herramienta. | Mixta | Esencial | Próximamente |
| L4.4.1 | **Configuración inicial de Codex**<br>Configuración inicial de Codex (`config.toml`: modelo y esfuerzo, permisos, configuración por proyecto) y trabajo con repositorios (proyectos locales, *worktrees* para tareas en paralelo). | Práctica | Profundizar | Próximamente |
| L4.4.2 | **Codex en la nube**<br>Entornos, acceso a internet desactivado por defecto y lista de dominios permitidos, tareas en paralelo, revisión del resultado y *pull requests*. | Práctica | Profundizar | Próximamente |
| L4.5.1 | **Qué delegar y qué no**<br>Tareas ideales, tareas riesgosas y señales de que el agente se está desviando. | Mixta | Esencial | Próximamente |
| L4.5.2 | **Claude Code vs. Codex**<br>Comparación práctica Claude Code vs. Codex: misma tarea, calidad, consumo, ergonomía, permisos y qué conviene para cada tipo de trabajo. | Mixta | Profundizar | Próximamente |

### [Módulo 5 · Automatización con n8n](../m05-n8n/index.md)

18 h · Nivel 1 · 11 lecciones · **Prerrequisitos:** [Módulo 0](../m00-orientacion/index.md) (indispensable), [Módulo 2](../m02-prompt-engineering/index.md) (recomendado, solo para L5.3.3).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L5.1.1 | **Qué es n8n y cuándo conviene**<br>Qué es n8n y cuándo conviene frente a código propio u otras plataformas. Workflow determinista vs. agente (anticipo). | Conceptual | Esencial | Próximamente |
| L5.1.2 | **Instalación con Docker y PostgreSQL**<br>Instalación con Docker y PostgreSQL; estructura de una instancia. | Práctica | Esencial | Próximamente |
| L5.1.3 | **Modelo de datos**<br>Ítems, JSON, expresiones y *mapping*. | Práctica | Esencial | Próximamente |
| L5.1.4 | **Triggers**<br>*Triggers*: manual, programado, webhook y eventos de aplicaciones. | Práctica | Esencial | Próximamente |
| L5.2.1 | **Webhooks y HTTP Request**<br>Webhooks entrantes y salientes; nodo HTTP Request contra API REST propias. | Práctica | Esencial | Próximamente |
| L5.2.2 | **Bases de datos, archivos y servicios**<br>Bases de datos, archivos y servicios (correo, calendario, GitHub, Slack o Telegram). | Práctica | Esencial | Próximamente |
| L5.2.3 | **Credenciales y seguridad en n8n**<br>Credenciales y seguridad de n8n 2.x: *task runners*, aislamiento del nodo de código, variables de entorno bloqueadas, nodos deshabilitados por defecto y gestión de secretos. | Mixta | Esencial | Próximamente |
| L5.2.4 | **Nodo de código y subworkflows**<br>Nodo de código (JavaScript/Python), subworkflows y reutilización. | Práctica | Profundizar | Próximamente |
| L5.3.1 | **Manejo de errores**<br>*error workflows*, reintentos, idempotencia y alertas. | Práctica | Esencial | Próximamente |
| L5.3.2 | **Guardar, publicar y versionar workflows**<br>Guardar vs. publicar, exportación y versionado de workflows en Git. | Práctica | Profundizar | Próximamente |
| L5.3.3 | **Primer nodo LLM en un workflow**<br>Primer nodo LLM dentro de un workflow determinista (clasificar o resumir), con control de costo y validación de la salida. | Mixta | Esencial | Próximamente |

## Etapa 2 · Construir con modelos

### [Módulo 6 · Desarrollo con APIs de modelos](../m06-apis-modelos/index.md)

30 h · 14 lecciones · **Prerrequisitos:** [Módulo 2](../m02-prompt-engineering/index.md) (indispensable), [Módulo 3](../m03-asistentes/index.md) (recomendado).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L6.1.1 | **Anatomía de una llamada**<br>Endpoint, autenticación, modelo, mensajes, parámetros y respuesta. Lo que hace el SDK por vos (con `curl` primero). | Práctica | Esencial | Próximamente |
| L6.1.2 | **Conversaciones sin estado**<br>Por qué el cliente reenvía el historial y qué implica en costo y diseño. Variantes con estado del lado del proveedor. | Conceptual | Esencial | Próximamente |
| L6.1.3 | **Streaming (SSE)**<br>*Streaming* (SSE): cuándo usarlo y cómo procesarlo. | Práctica | Profundizar | Próximamente |
| L6.1.4 | **Comparativa de API**<br>Anthropic Messages, OpenAI Responses y Gemini. Conceptos equivalentes y diferencias. | Mixta | Profundizar | Próximamente |
| L6.2.1 | **Salidas estructuradas**<br>JSON Schema, modo estricto, validación con Pydantic o Bean Validation. | Práctica | Esencial | Próximamente |
| L6.2.2 | **Manejo de errores**<br>Límites de tasa, *timeouts*, reintentos con *backoff*, errores de contenido y respuestas truncadas. | Práctica | Esencial | Próximamente |
| L6.2.3 | **Pruebas de código que llama a un LLM**<br>*mocks*, *fixtures* grabadas y tests de contrato vs. evals. | Práctica | Esencial | Próximamente |
| L6.3.1 | **Qué es tool calling**<br>El modelo no ejecuta tu función, propone una llamada y tu código la ejecuta. El ciclo completo. | Mixta | Esencial | Próximamente |
| L6.3.2 | **Diseño de herramientas**<br>Nombres, descripciones, esquemas y errores devueltos al modelo. | Práctica | Esencial | Próximamente |
| L6.3.3 | **Llamadas paralelas y herramientas del proveedor**<br>Llamadas paralelas, elección forzada de herramienta y herramientas ejecutadas por el proveedor (búsqueda web, ejecución de código): quién ejecuta qué y dónde. | Mixta | Esencial | Próximamente |
| L6.3.4 | **Riesgos de tool calling**<br>Validar argumentos, permisos mínimos y confirmación humana para acciones destructivas. | Mixta | Esencial | Próximamente |
| L6.4.1 | **Caché de prompts, batch y elección de modelo**<br>Caché de prompts, procesamiento por lotes (*batch*) y selección de modelo por tarea. | Práctica | Esencial | Próximamente |
| L6.4.2 | **Portabilidad entre proveedores**<br>Portabilidad: API compatibles con OpenAI, Ollama, routers (por ejemplo LiteLLM u OpenRouter) y el costo de la abstracción. | Mixta | Profundizar | Próximamente |
| L6.4.3 | **LLM en Java con Spring AI 2.0**<br>`ChatClient`, *advisors*, salidas estructuradas y herramientas. | Práctica | Profundizar | Próximamente |

### [Módulo 7 · Context Engineering](../m07-context-engineering/index.md)

20 h · Nivel 2 · 11 lecciones · **Prerrequisitos:** [Módulo 6](../m06-apis-modelos/index.md) (indispensable); [Módulo 3](../m03-asistentes/index.md) y [Módulo 4](../m04-agentes-programacion/index.md) (recomendados: aportan la experiencia de uso que aquí se formaliza).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L7.1.1 | **Qué es context engineering**<br>Qué es context engineering y por qué reemplazó al "prompt engineering" como habilidad central. | Conceptual | Esencial | Próximamente |
| L7.1.2 | **Componentes del contexto**<br>Instrucciones de sistema, definiciones de herramientas, conocimiento recuperado, memoria, historial y resultados de herramientas. Cuánto "pesa" cada uno. | Mixta | Esencial | Próximamente |
| L7.1.3 | **Degradación del contexto (context rot)**<br>Degradación del contexto (*context rot*): medirla y por qué más contexto no siempre es mejor. | Mixta | Esencial | Próximamente |
| L7.2.1 | **Seleccionar el contexto**<br>Seleccionar: qué incluir y qué dejar afuera; recuperación bajo demanda vs. carga anticipada. | Mixta | Esencial | Próximamente |
| L7.2.2 | **Comprimir el contexto**<br>Comprimir: resúmenes, compactación y edición de contexto (limpiar resultados viejos de herramientas). | Práctica | Esencial | Próximamente |
| L7.2.3 | **Aislar el contexto**<br>Aislar: dividir trabajo en subcontextos (anticipo de subagentes y multiagente). | Conceptual | Esencial | Próximamente |
| L7.2.4 | **Persistir el contexto**<br>Persistir: notas externas, archivos de estado y *memory tools*. | Práctica | Esencial | Próximamente |
| L7.2.5 | **Orden del contexto y caché**<br>Orden y caché: estructurar el contexto para aprovechar la caché de prompts. | Práctica | Profundizar | Próximamente |
| L7.3.1 | **Tipos de memoria**<br>De trabajo, episódica, semántica y procedimental. Cómo se implementa cada una. | Conceptual | Esencial | Próximamente |
| L7.3.2 | **Archivos de instrucciones a fondo**<br>Archivos de instrucciones a fondo (`CLAUDE.md`, `AGENTS.md`, instrucciones de proyecto): principios de diseño, alcance y medición de efecto (formaliza lo usado en M3 y M4). | Mixta | Esencial | Próximamente |
| L7.3.3 | **Divulgación progresiva**<br>El principio detrás de las Agent Skills y la búsqueda de herramientas. | Conceptual | Profundizar | Próximamente |

### [Módulo 8 · Embeddings y RAG](../m08-rag/index.md)

34 h · 14 lecciones · **Prerrequisitos:** [Módulo 6](../m06-apis-modelos/index.md) y [Módulo 7](../m07-context-engineering/index.md) (indispensables).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L8.1.1 | **Embeddings en profundidad**<br>Qué capturan, dimensiones, modelos, normalización y embeddings multimodales (texto e imagen en un mismo espacio). | Mixta | Esencial | Próximamente |
| L8.1.2 | **Similitud y búsqueda del vecino más cercano**<br>Similitud (coseno, producto punto, euclídea) y búsqueda del vecino más cercano: exacta vs. aproximada. | Mixta | Profundizar | Próximamente |
| L8.1.3 | **Bases vectoriales**<br>Pgvector, Chroma y servicios gestionados. Índices HNSW e IVF; filtros por metadatos. | Práctica | Esencial | Próximamente |
| L8.2.1 | **Arquitectura RAG**<br>Ingesta → indexación → recuperación → generación. Por qué funciona y dónde falla. | Conceptual | Esencial | Próximamente |
| L8.2.2 | **Ingesta de documentos**<br>Ingesta: extracción de PDF, HTML y código; limpieza; metadatos. | Práctica | Esencial | Próximamente |
| L8.2.3 | **Chunking**<br>*Chunking*: tamaño, solapamiento, por estructura y semántico. Efectos en la calidad. | Mixta | Esencial | Próximamente |
| L8.2.4 | **Generación con contexto recuperado**<br>Prompt de RAG, citas y "no sé" cuando no hay evidencia. | Práctica | Esencial | Próximamente |
| L8.3.1 | **Búsqueda híbrida y reranking**<br>Búsqueda híbrida y *reranking*. | Práctica | Esencial | Próximamente |
| L8.3.2 | **Reescritura de consultas y HyDE**<br>Reescritura y expansión de consultas, HyDE y consultas multi-paso. | Mixta | Profundizar | Próximamente |
| L8.3.3 | **RAG agéntico**<br>La recuperación como herramienta que decide el agente. | Mixta | Profundizar | Próximamente |
| L8.3.4 | **Alternativas a RAG**<br>Alternativas y complementos: contexto largo, búsqueda tipo `grep` en agentes de código, GraphRAG. Cuándo NO usar RAG y cuándo considerar *fine-tuning*. | Conceptual | Esencial | Próximamente |
| L8.4.1 | **Métricas de RAG**<br>Métricas: *recall* y precisión de recuperación, fidelidad (*faithfulness*) y relevancia de la respuesta. Construcción de un *dataset* de preguntas y respuestas. | Mixta | Esencial | Próximamente |
| L8.4.2 | **Herramientas de evaluación de RAG**<br>Herramientas de evaluación de RAG (por ejemplo Ragas, promptfoo o LLM como juez) y sus límites. | Práctica | Profundizar | Próximamente |
| L8.4.3 | **Operación de un sistema RAG**<br>Operación: actualización incremental, versionado del índice y control de acceso por documento. | Mixta | Profundizar | Próximamente |

## Etapa 3 · Agentes e interoperabilidad

### [Módulo 9 · Agentes desde cero](../m09-agentes-desde-cero/index.md)

30 h · 13 lecciones · **Prerrequisitos:** [Módulo 6](../m06-apis-modelos/index.md) y [Módulo 7](../m07-context-engineering/index.md) (indispensables), [Módulo 8](../m08-rag/index.md) (recomendado).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L9.1.1 | **Workflows vs. agentes**<br>Workflows vs. agentes: control determinístico vs. control del modelo. Niveles de autonomía (de sugerir a actuar sin supervisión). | Conceptual | Esencial | Próximamente |
| L9.1.2 | **Cuándo no construir un agente**<br>Cuándo NO construir un agente: el costo de la autonomía (latencia, gasto, impredecibilidad). | Conceptual | Esencial | Próximamente |
| L9.1.3 | **Patrones de workflows con LLM**<br>Encadenamiento, enrutamiento, paralelización, orquestador-trabajadores y evaluador-optimizador. | Mixta | Esencial | Próximamente |
| L9.2.1 | **El bucle agéntico mínimo en ~100 líneas**<br>Modelo, herramientas, observación y parada. | Práctica | Esencial | Próximamente |
| L9.2.2 | **ReAct y razonamiento intercalado**<br>ReAct y razonamiento intercalado; uso de *thinking* entre llamadas a herramientas. | Mixta | Profundizar | Próximamente |
| L9.2.3 | **Diseño de herramientas para agentes**<br>Granularidad, idempotencia y errores informativos. | Práctica | Esencial | Próximamente |
| L9.2.4 | **Condiciones de parada y presupuesto**<br>Condiciones de parada, límites de pasos y presupuesto, bucles infinitos y recuperación de errores. | Práctica | Esencial | Próximamente |
| L9.3.1 | **Planificación explícita**<br>Planes, listas de tareas y re-planificación. | Práctica | Esencial | Próximamente |
| L9.3.2 | **Memoria del agente**<br>*scratchpad*, archivos de estado y memoria a largo plazo con RAG. | Práctica | Esencial | Próximamente |
| L9.3.3 | **Tareas de larga duración**<br>Checkpoints y reanudación (concepto; se implementa en M14). | Conceptual | Profundizar | Próximamente |
| L9.4.1 | **Human-in-the-loop**<br>*Human-in-the-loop*: aprobaciones, puntos de control e interrupciones. | Práctica | Esencial | Próximamente |
| L9.4.2 | **Agencia excesiva**<br>Permisos mínimos, *sandboxing*, acciones reversibles vs. irreversibles. | Mixta | Esencial | Próximamente |
| L9.4.3 | **Evaluar agentes**<br>Éxito de la tarea, trayectoria, costo y pasos. | Práctica | Esencial | Próximamente |

### [Módulo 10 · Model Context Protocol (MCP)](../m10-mcp/index.md)

32 h · Nivel 2 · 16 lecciones · **Prerrequisitos:** [Módulo 9](../m09-agentes-desde-cero/index.md) (indispensable), [Módulo 3](../m03-asistentes/index.md) (recomendado: uso de connectors y MCP en Nivel 1).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L10.1.1 | **Qué problema resuelve MCP**<br>Repaso del Nivel 1 y qué problema resuelve MCP. Historia, gobernanza (Agentic AI Foundation) y adopción. | Conceptual | Esencial | Próximamente |
| L10.1.2 | **Host, cliente y servidor**<br>Quién hace qué. MCP como "tool calling estandarizado y descubrible". | Conceptual | Esencial | Próximamente |
| L10.1.3 | **Primitivas del servidor**<br>Herramientas, recursos y prompts. Cuándo usar cada una. | Mixta | Esencial | Próximamente |
| L10.1.4 | **Interacción con el cliente**<br>Elicitación mediante el patrón *multi round-trip requests* (MRTR). Roots, Sampling y Logging: qué eran, por qué se deprecan y con qué se reemplazan. | Conceptual | Esencial | Próximamente |
| L10.1.5 | **Transportes y especificación vigente**<br>Transportes: stdio vs. Streamable HTTP (HTTP+SSE deprecado). Núcleo sin estado de la especificación 2026-07-28 (`server/discover`, sin sesiones de protocolo) y qué cambia respecto de la 2025-11-25. | Mixta | Esencial | Próximamente |
| L10.2.1 | **Primer servidor en Python**<br>Herramientas y recursos, probado con MCP Inspector. | Práctica | Esencial | Próximamente |
| L10.2.2 | **Servidor en Java con Spring AI**<br>Servidor en Java con Spring AI (`@McpTool`, `@McpResource`) sobre una API REST o base de datos existente. | Práctica | Profundizar | Próximamente |
| L10.2.3 | **Diseño de servidores para agentes**<br>Pocas herramientas bien descritas vs. "envolver toda la API". Errores, paginación, orden determinista y caché de listas. | Mixta | Esencial | Próximamente |
| L10.2.4 | **Extensiones oficiales**<br>Tasks (operaciones largas), MCP Apps (interfaces interactivas) y Skills over MCP. Concepto y ejemplo según soporte de SDK y host `[Verificar]`. | Mixta | Profundizar | Próximamente |
| L10.3.1 | **Configuración avanzada en hosts**<br>Ámbitos, servidores remotos con OAuth, variables y depuración (amplía L3.5.2 y L4.3.2). | Práctica | Esencial | Próximamente |
| L10.3.2 | **Cliente MCP propio**<br>Construir un cliente MCP propio e integrarlo al agente de P5. | Práctica | Esencial | Próximamente |
| L10.3.3 | **Ecosistema y registros de servidores**<br>Ecosistema: registros de servidores y cómo evaluarlos antes de instalarlos. | Mixta | Profundizar | Próximamente |
| L10.4.1 | **Autorización en servidores remotos**<br>OAuth 2.1/OIDC, *scopes*, tokens y registro de clientes (Client ID Metadata Documents; Dynamic Client Registration deprecado). | Mixta | Esencial | Próximamente |
| L10.4.2 | **Amenazas y mitigaciones**<br>Amenazas: *tool poisoning*, *prompt injection* indirecta vía resultados, *confused deputy*, robo de credenciales y servidores maliciosos. Mitigaciones. | Mixta | Esencial | Próximamente |
| L10.4.3 | **Despliegue y observabilidad**<br>Despliegue remoto (contenedor, *serverless*), observabilidad con trazas (OpenTelemetry) y versionado. | Práctica | Profundizar | Próximamente |
| L10.4.4 | **MCP vs. API, skills y A2A**<br>MCP vs. API directa vs. skill vs. A2A: cuándo usar cada uno. | Conceptual | Esencial | Próximamente |

### [Módulo 11 · Agentes de programación avanzados](../m11-agentes-programacion-avanzado/index.md)

25 h · Nivel 2 · 14 lecciones · **Prerrequisitos:** [Módulo 4](../m04-agentes-programacion/index.md) y [Módulo 7](../m07-context-engineering/index.md) (indispensables), [Módulo 10](../m10-mcp/index.md) (recomendado, para L11.3.2).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L11.1.1 | **Anatomía del harness**<br>Anatomía del *harness*: bucle, herramientas (lectura, edición, terminal, búsqueda), contexto y permisos. Comparación entre Claude Code, Codex y tu agente de P5. | Conceptual | Esencial | Próximamente |
| L11.1.2 | **Gestión del contexto en el agente**<br>Cómo gestiona el contexto un agente de programación: compactación, memoria, carga de instrucciones y skills, búsqueda en el código vs. RAG. Diferencias entre ambas herramientas. | Conceptual | Esencial | Próximamente |
| L11.2.1 | **AGENTS.md y CLAUDE.md a fondo**<br>`AGENTS.md` y `CLAUDE.md` a fondo: jerarquía, alcance por carpeta, archivos de anulación y límites de tamaño en Codex, memoria en Claude Code; mantenimiento y medición de efecto. | Mixta | Esencial | Próximamente |
| L11.2.2 | **Portabilidad de la configuración**<br>Portabilidad de la configuración entre agentes: qué es estándar (`AGENTS.md`, Agent Skills, MCP) y qué es propio (`config.toml` de Codex, `settings.json` de Claude Code, hooks, extensiones de skills). | Mixta | Profundizar | Próximamente |
| L11.3.1 | **Permisos avanzados y aislamiento**<br>Políticas por proyecto y organización en Claude Code; en Codex, modos de *sandbox*, políticas de aprobación, revisión automática de aprobaciones, reglas de ejecución y el *sandbox* nativo de Windows. | Práctica | Esencial | Próximamente |
| L11.3.2 | **Tu servidor MCP en ambos agentes**<br>Tu servidor MCP (P6) en ambos agentes: configuración, autenticación OAuth, herramientas permitidas o bloqueadas y aprobación por herramienta. | Práctica | Esencial | Próximamente |
| L11.3.3 | **Hooks y automatismos del ciclo de vida**<br>Hooks de Claude Code (formateo, lint, tests, bloqueos de seguridad) y su equivalente en Codex, si existe en la versión vigente `[Verificar]`. | Práctica | Esencial | Próximamente |
| L11.3.4 | **Subagentes y trabajo en paralelo**<br>Subagentes de Claude Code; tareas en paralelo con *worktrees* y en la nube en Codex; cuándo aislar contexto. | Mixta | Esencial | Próximamente |
| L11.3.5 | **Primera skill propia**<br>Primera skill propia dentro del agente de programación: ubicaciones (`.claude/skills` y `.agents/skills`), invocación explícita e implícita, y una misma skill usada en Claude Code y en Codex (el desarrollo a fondo sigue en M12). | Práctica | Esencial | Próximamente |
| L11.4.1 | **Modo no interactivo y scripting**<br>`claude -p` y `codex exec` (salida JSON, salida con esquema, *sandbox* de solo lectura por defecto en Codex, reanudar sesiones). | Práctica | Esencial | Próximamente |
| L11.4.2 | **Agentes en CI**<br>Revisión de PR y corrección de fallas con la integración de GitHub Actions de Claude Code y con la acción oficial de Codex (separar el job que ejecuta al agente del job con permisos de escritura); revisión de código automática en GitHub. | Práctica | Esencial | Próximamente |
| L11.4.3 | **Tareas programadas y en la nube**<br>Routines y tareas de escritorio de Claude Code; tareas programadas de Codex (locales en *worktree* o en la nube para equipos). Límites y riesgos de la ejecución desatendida `[Pago]`. | Mixta | Profundizar | Próximamente |
| L11.5.1 | **Revisión de código generado a escala**<br>Calidad, seguridad y deuda técnica. | Mixta | Profundizar | Próximamente |
| L11.5.2 | **Medir la eficacia de los agentes**<br>Medir la eficacia de cada agente en tu repositorio: tareas de referencia, tasa de éxito, intervenciones y costo. | Práctica | Profundizar | Próximamente |

### [Módulo 12 · Desarrollo de skills y plugins](../m12-skills-plugins/index.md)

18 h · Nivel 2 · 10 lecciones · **Prerrequisitos:** [Módulo 3](../m03-asistentes/index.md) y [Módulo 11](../m11-agentes-programacion-avanzado/index.md) (indispensables).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L12.1.1 | **Repaso y divulgación progresiva**<br>Repaso del Nivel 1. Divulgación progresiva y cómo decide el agente activar una skill. | Conceptual | Esencial | Próximamente |
| L12.1.2 | **Anatomía de una skill**<br>Anatomía: `SKILL.md` (metadatos, descripción que dispara la activación, instrucciones), `scripts/`, `references/`, `assets/`. Campos del estándar vs. extensiones de cada cliente (por ejemplo, controles de invocación de Claude Code o `agents/openai.yaml` de Codex) y límites de carga de cada cliente. | Mixta | Esencial | Próximamente |
| L12.1.3 | **Escribir buenas skills**<br>Descripciones precisas, instrucciones concisas, scripts deterministas para lo que no debe "improvisar" el modelo. | Práctica | Esencial | Próximamente |
| L12.1.4 | **Probar y evaluar skills**<br>¿se activa cuando debe? ¿mejora el resultado? Iteración. | Práctica | Esencial | Próximamente |
| L12.2.1 | **Elegir el mecanismo de extensión**<br>Skill vs. servidor MCP vs. subagente vs. comando vs. hook vs. `AGENTS.md`: matriz de decisión. | Conceptual | Esencial | Próximamente |
| L12.2.2 | **Portabilidad de skills**<br>Portabilidad: la misma skill en Claude, Claude Code, Codex, Gemini CLI y Spring AI; skills distribuidas por MCP. Qué se rompe y por qué. | Práctica | Profundizar | Próximamente |
| L12.3.1 | **Plugins en dos ecosistemas**<br>Plugins de Claude (skills, comandos, agentes, hooks, servidores MCP; qué carga cada superficie) y plugins de ChatGPT/Codex (skills, servidores MCP y hooks del ciclo de vida, con un directorio compartido). Qué es común y qué no es portable. | Mixta | Esencial | Próximamente |
| L12.3.2 | **Marketplaces y distribución**<br>Públicos, privados y de equipo. Versionado y actualización. | Práctica | Profundizar | Próximamente |
| L12.3.3 | **Cadena de suministro**<br>Revisar skills y plugins de terceros (scripts, permisos, connectors) y procedencia. | Mixta | Esencial | Próximamente |
| L12.3.4 | **Costo de contexto y evals de plugins**<br>Medir costo de contexto y uso de un plugin; evals de plugins. | Práctica | Profundizar | Próximamente |

## Etapa 4 · Automatización y sistemas avanzados

### [Módulo 13 · n8n con IA y agentes](../m13-n8n-ia/index.md)

24 h · Nivel 2 · 10 lecciones · **Prerrequisitos:** [Módulo 5](../m05-n8n/index.md), [Módulo 6](../m06-apis-modelos/index.md) y [Módulo 9](../m09-agentes-desde-cero/index.md) (indispensables); [Módulo 8](../m08-rag/index.md) y [Módulo 10](../m10-mcp/index.md) (recomendados, para L13.3.1 y L13.3.2).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L13.1.1 | **Nodos LLM con salida estructurada**<br>Nodos de LLM con salida estructurada y validación: clasificación, extracción y resumen (amplía L5.3.3). | Práctica | Esencial | Próximamente |
| L13.1.2 | **Patrones de workflows con LLM en n8n**<br>Encadenamiento, enrutamiento, paralelización y evaluador-optimizador (mapeo con L9.1.3). | Mixta | Esencial | Próximamente |
| L13.2.1 | **Nodo AI Agent**<br>Modelo, memoria y herramientas. Mapeo con el bucle de M9. | Mixta | Esencial | Próximamente |
| L13.2.2 | **Herramientas del agente**<br>Nodos, HTTP y workflows como herramientas. | Práctica | Esencial | Próximamente |
| L13.2.3 | **Aprobación humana en workflows**<br>Aprobación humana dentro de workflows (esperar confirmación por correo o chat). | Práctica | Esencial | Próximamente |
| L13.3.1 | **RAG en n8n**<br>Ingesta a un vector store y agente con recuperación. | Práctica | Esencial | Próximamente |
| L13.3.2 | **MCP en n8n**<br>Consumir servidores MCP (MCP Client Tool) y exponer workflows como servidor MCP (MCP Server Trigger). | Práctica | Esencial | Próximamente |
| L13.4.1 | **Monitoreo, costos y límites**<br>Monitoreo de ejecuciones, costos de LLM y límites. | Práctica | Esencial | Próximamente |
| L13.4.2 | **Escalado y entornos**<br>Modo cola, réplicas y consideraciones para endpoints MCP `[Verificar]`. | Mixta | Profundizar | Próximamente |
| L13.4.3 | **Workflow con LLM vs. agente**<br>Workflow determinista + LLM puntual vs. agente autónomo; n8n vs. código propio. | Conceptual | Esencial | Próximamente |

### [Módulo 14 · Frameworks de agentes](../m14-frameworks-agentes/index.md)

36 h · 11 lecciones · **Prerrequisitos:** [Módulo 9](../m09-agentes-desde-cero/index.md) (indispensable), [Módulo 10](../m10-mcp/index.md) (recomendado).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L14.1.1 | **Qué aporta un framework**<br>Qué aporta un framework sobre tu agente de P5: estado, herramientas, memoria, trazas y despliegue. El costo de la abstracción. | Conceptual | Esencial | Próximamente |
| L14.1.2 | **Mapa de opciones y matriz de decisión**<br>Mapa de opciones vigente (Python, TypeScript y Java), su estado de mantenimiento y matriz de decisión. | Conceptual | Esencial | Próximamente |
| L14.2.1 | **Claude Agent SDK**<br>El *harness* de Claude Code como librería. Herramientas, permisos, subagentes y MCP. Referencia: el SDK de Codex como enfoque equivalente del otro proveedor `[Verificar alcance]`. | Práctica | Esencial | Próximamente |
| L14.2.2 | **OpenAI Agents SDK**<br>Agentes, *handoffs*, *guardrails* y sesiones. | Práctica | Esencial | Próximamente |
| L14.2.3 | **Runtimes gestionados**<br>Runtimes gestionados (por ejemplo Claude Managed Agents): cuándo delegar la infraestructura `[Pago]`. | Mixta | Profundizar | Próximamente |
| L14.3.1 | **LangGraph**<br>Grafos de estado, nodos, aristas condicionales, checkpoints e interrupciones para aprobación humana. | Práctica | Esencial | Próximamente |
| L14.3.2 | **Agentes en Java**<br>Spring AI 2.0 (bucle en la cadena de *advisors*, herramientas y MCP) y comparación con LangChain4j y Google ADK para Java. | Práctica | Profundizar | Próximamente |
| L14.4.1 | **Ejecución durable**<br>Persistencia del estado, reintentos y reanudación tras fallos. | Práctica | Esencial | Próximamente |
| L14.4.2 | **Memoria a largo plazo**<br>Estrategias y almacenamiento. | Mixta | Profundizar | Próximamente |
| L14.4.3 | **Guardrails**<br>*Guardrails* de entrada y salida, validación y límites. | Práctica | Esencial | Próximamente |
| L14.4.4 | **Exponer un agente como servicio**<br>API, *streaming* de eventos, autenticación y despliegue en contenedor. | Práctica | Esencial | Próximamente |

### [Módulo 15 · Sistemas multiagente](../m15-multiagente/index.md)

26 h · 11 lecciones · **Prerrequisitos:** [Módulo 14](../m14-frameworks-agentes/index.md) (indispensable).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L15.1.1 | **Cuándo usar varios agentes**<br>Cuándo varios agentes superan a uno (y cuándo no): evidencia, costos y la regla de "empezar con uno". | Conceptual | Esencial | Próximamente |
| L15.1.2 | **Topologías y patrones de coordinación** | Conceptual | Esencial | Próximamente |
| L15.1.3 | **Delegación efectiva entre agentes**<br>Qué contexto pasar, formato de resultados y criterios de terminación (versión programática de L3.7.1). | Mixta | Esencial | Próximamente |
| L15.2.1 | **Orquestador y trabajadores**<br>Orquestador-trabajadores con investigación en paralelo. | Práctica | Esencial | Próximamente |
| L15.2.2 | **Handoffs y estado compartido**<br>*Handoffs* entre agentes especializados y estado compartido. | Práctica | Esencial | Próximamente |
| L15.2.3 | **Evaluador-optimizador**<br>Evaluador-optimizador y revisión cruzada entre agentes. | Práctica | Profundizar | Próximamente |
| L15.3.1 | **El protocolo A2A**<br>El protocolo A2A 1.0: Agent Cards (incluidas las firmadas), tareas, mensajes y artefactos. | Conceptual | Profundizar | Próximamente |
| L15.3.2 | **A2A en la práctica**<br>Exponer y consumir un agente vía A2A; A2A + MCP en una misma arquitectura. | Práctica | Profundizar | Próximamente |
| L15.4.1 | **Evaluar sistemas multiagente**<br>Éxito global, contribución de cada agente y trazas. | Práctica | Esencial | Próximamente |
| L15.4.2 | **Fallos típicos**<br>Duplicación de trabajo, delegación vaga, bucles entre agentes y explosión de costos. Presupuestos por agente. | Mixta | Esencial | Próximamente |
| L15.4.3 | **Confianza entre agentes**<br>Propagación de *prompt injection*, identidad y permisos por agente. | Mixta | Esencial | Próximamente |

## Etapa 5 · Producción e integración

### [Módulo 16 · Seguridad, evaluación y operación](../m16-produccion/index.md)

36 h · 16 lecciones · **Prerrequisitos:** [Módulo 13](../m13-n8n-ia/index.md) y [Módulo 14](../m14-frameworks-agentes/index.md) (indispensables); [Módulo 12](../m12-skills-plugins/index.md) y [Módulo 15](../m15-multiagente/index.md) (recomendados).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L16.1.1 | **Modelado de amenazas**<br>Modelado de amenazas para aplicaciones y agentes con LLM: activos, fronteras de confianza y la "tríada letal" (datos privados + contenido no confiable + capacidad de comunicación externa). | Mixta | Esencial | Próximamente |
| L16.1.2 | **OWASP Top 10 para LLM y agentes**<br>OWASP Top 10 LLM 2026 y Top 10 de aplicaciones agénticas: recorrido con ejemplos sobre tus proyectos. | Mixta | Esencial | Próximamente |
| L16.1.3 | **Defensa contra prompt injection**<br>Defensa contra *prompt injection*: por qué no hay solución completa; aislamiento, permisos, confirmación humana y separación de privilegios. | Mixta | Esencial | Próximamente |
| L16.1.4 | **Identidad y credenciales de agentes**<br>Secretos, tokens de corta duración y permisos mínimos por herramienta. | Práctica | Esencial | Próximamente |
| L16.1.5 | **Privacidad**<br>Datos personales, minimización, anonimización y retención en proveedores. | Conceptual | Esencial | Próximamente |
| L16.2.1 | **Estrategia de evaluación**<br>Tipos (deterministas, basados en modelo, humanos) y qué medir en cada tipo de sistema. | Conceptual | Esencial | Próximamente |
| L16.2.2 | **LLM como juez**<br>Diseño de rúbricas, calibración con humanos y sesgos. | Práctica | Esencial | Próximamente |
| L16.2.3 | **Evals en integración continua**<br>Regresión al cambiar prompts, modelos o herramientas. | Práctica | Esencial | Próximamente |
| L16.2.4 | **Red teaming**<br>*Red teaming* y evaluación adversarial. | Práctica | Profundizar | Próximamente |
| L16.3.1 | **Trazas con OpenTelemetry**<br>Trazas de LLM y agentes con OpenTelemetry: spans, atributos y convenciones. | Práctica | Esencial | Próximamente |
| L16.3.2 | **Plataformas LLMOps**<br>Plataformas LLMOps (Langfuse o Phoenix): trazas, *datasets*, evaluaciones en línea y *feedback*. | Práctica | Profundizar | Próximamente |
| L16.3.3 | **Depurar agentes**<br>Leer trayectorias, reproducir fallos y análisis de errores sistemático. | Práctica | Esencial | Próximamente |
| L16.4.1 | **Optimización de costos**<br>Optimización: enrutamiento por modelo, caché, *batch*, compresión de contexto y presupuestos. | Práctica | Esencial | Próximamente |
| L16.4.2 | **Confiabilidad**<br>*fallbacks* entre proveedores, límites de tasa, *timeouts* y degradación controlada. | Práctica | Esencial | Próximamente |
| L16.4.3 | **Mantenimiento**<br>Deprecación de modelos, API y herramientas (casos reales: Assistants API, Agent Builder), migraciones y deriva. | Mixta | Esencial | Próximamente |
| L16.4.4 | **Gobernanza mínima**<br>Registro de decisiones, auditoría y documentación de sistemas de IA. | Conceptual | Profundizar | Próximamente |

### [Módulo 17 · Proyecto final integrador](../m17-proyecto-final/index.md)

50 h · 8 lecciones · **Prerrequisitos:** [Módulo 16](../m16-produccion/index.md) (indispensable).

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L17.1.1 | **Elegir el problema y los requisitos**<br>Elección del problema y definición de requisitos, métricas de éxito y restricciones (costo, privacidad). | Mixta | Esencial | Próximamente |
| L17.1.2 | **Arquitectura y decisiones (ADR)**<br>Arquitectura y decisiones técnicas documentadas (ADR): qué es determinista, qué es agente, qué es RAG, qué es MCP y qué es n8n. | Mixta | Esencial | Próximamente |
| L17.1.3 | **Amenazas y plan de evaluación**<br>Modelo de amenazas y plan de evaluación antes de construir. | Mixta | Esencial | Próximamente |
| L17.2.1 | **Hito 1: núcleo funcional**<br>Hito 1: núcleo funcional mínimo con evals. | Práctica | Esencial | Próximamente |
| L17.2.2 | **Hito 2: integraciones**<br>Hito 2: integraciones (MCP, n8n y datos). | Práctica | Esencial | Próximamente |
| L17.2.3 | **Hito 3: seguridad, observabilidad y costos**<br>Hito 3: seguridad, observabilidad y costos. | Práctica | Esencial | Próximamente |
| L17.3.1 | **Evaluación final y métricas**<br>Evaluación final, informe de métricas y análisis de costos. | Práctica | Esencial | Próximamente |
| L17.3.2 | **Documentación, demostración y retrospectiva** | Mixta | Esencial | Próximamente |

## Electivas

Especializaciones opcionales, sin lecciones numeradas: ver [Electivas](electivas.md).
