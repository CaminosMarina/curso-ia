---
modulo: M3
titulo: "Asistentes de IA: uso profesional, contexto y delegación"
bloque: I
nivel: N1
horas_teoria: 11
horas_practica: 25
---

# M3 · Asistentes de IA: uso profesional, contexto y delegación

**Bloque I** · **Nivel 1 (usar y configurar)** · 36 h (11 h de teoría y 25 h de práctica) · 25 lecciones

## Objetivo

Usar con eficacia, seguridad y criterio las principales plataformas de asistentes —**Claude** (con sus capacidades agénticas) y **ChatGPT** (con Work) como herramientas principales, Gemini y una opción local como complemento—, incluidos proyectos, memoria, connectors, servidores MCP, skills y plugins existentes, y delegarles tareas complejas con supervisión y verificación.

## Qué vas a aprender

Anatomía de un asistente; gestión del contexto como persona usuaria (proyectos, instrucciones, conocimiento, memoria, conversaciones largas); connectors y servidores MCP existentes; skills y plugins existentes; multimodalidad y agentes de computadora o navegador como persona usuaria; especificación, supervisión y verificación de tareas delegadas; privacidad, propiedad intelectual y selección de herramientas.

## Antes de empezar

- **Prerrequisitos:** [M2](../m02-prompt-engineering/index.md) (duro).
- **Herramientas:** planes gratuitos de Claude, ChatGPT y Gemini; Ollama con una interfaz local. Recomendado `[Pago]`: un plan pago de Claude **o** de ChatGPT (habilitan las funciones agénticas completas: tareas largas, ChatGPT Work, más tareas programadas). No hace falta pagar ambos: las prácticas que requieren un plan pago tienen alternativa en la otra plataforma o en el plan gratuito. Disponibilidad por plan y región verificada al preparar cada lección (ver la nota de herramientas de cada lección).

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U3.1 · Conceptos comunes a todas las plataformas

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.1.1 | Anatomía de un asistente moderno: modelo + *system prompt* + herramientas + memoria + interfaz. Qué es igual en todas y qué cambia. | C | — |
| L3.1.2 | Proyectos, conocimiento adjunto e instrucciones personalizadas: qué entra realmente al contexto y cuándo. | M | — |
| L3.1.3 | Memoria entre conversaciones: cómo funciona, cómo inspeccionarla, editarla y desactivarla. | M | — |

### U3.2 · Claude y sus capacidades agénticas (antes "Cowork")

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.2.1 | Claude: conversación, proyectos, artifacts, búsqueda y research. Cómo decide cuánto trabajo hacer. | P | — |
| L3.2.2 | Trabajo agéntico en la app: archivos locales, tareas largas, permisos, tareas programadas, Docs, Slides y Design `[Beta]`. | P | — |
| L3.2.3 | Proyectos de Claude bien diseñados: instrucciones, documentos de conocimiento y su mantenimiento (aplicado a este mismo curso). | P | — |

### U3.3 · ChatGPT en profundidad, Gemini y alternativas

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.3.1 | ChatGPT: conversaciones, instrucciones personalizadas, chats temporales y organización del trabajo (proyectos con memoria por defecto o solo del proyecto, proyectos compartidos, Space y Pages según disponibilidad). | P | — |
| L3.3.2 | ChatGPT: archivos, análisis de datos, búsqueda e investigación profunda (*deep research*): cuándo usar cada una, alcance, límites por plan y país, y cómo verificar las fuentes. | P | — |
| L3.3.3 | ChatGPT Work: delegar tareas largas que producen documentos, hojas de cálculo, presentaciones o sitios; tareas en sitios con sesión iniciada y confirmaciones antes de acciones con consecuencias `[Pago según plan]`. | P | — |
| L3.3.4 | ChatGPT: plugins (apps, skills y conectores en un mismo directorio), tareas programadas y disparadas por eventos de apps conectadas; permisos, Centro de privacidad y supervisión de lo que se ejecuta sin vos `[Disponibilidad según plan]`. | P | — |
| L3.3.5 | Gemini y el ecosistema Google: Gems, integración con Workspace y NotebookLM. | P | — |
| L3.3.6 | Asistente local y privado: Ollama con una interfaz de chat. Cuándo vale la pena (privacidad, costo cero) y sus límites. | P | — |

### U3.4 · Gestión del contexto como persona usuaria

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.4.1 | Diseñar instrucciones y conocimiento de proyecto: qué escribir, qué evitar y cómo medir si mejora el resultado. | M | — |
| L3.4.2 | Conversaciones largas: degradación del contexto, cuándo empezar de nuevo, resúmenes de traspaso y memoria explícita. | M | — |

### U3.5 · Connectors, MCP, skills y plugins: Nivel 1

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.5.1 | Connectors y apps en Claude y ChatGPT (y Gemini como referencia): qué son (frecuentemente MCP bajo el capó), permisos que otorgan, lectura vs. escritura y cómo revocarlos. | P | — |
| L3.5.2 | Servidores MCP locales existentes en la app de escritorio: instalar y configurar uno (por ejemplo, sistema de archivos con alcance limitado), probarlo y revisar qué puede hacer. | P | — |
| L3.5.3 | Skills y plugins existentes en Claude y en ChatGPT: qué contiene un plugin en cada plataforma, cómo instalarlo, invocarlo y evaluar si realmente ayuda; revisar su contenido antes de instalarlo (scripts, connectors, permisos) y su costo de contexto. | P | — |

### U3.6 · Multimodalidad y agentes de computadora/navegador: uso

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.6.1 | Visión, documentos y audio: análisis de capturas, PDF, diagramas y voz. Qué funciona bien y dónde falla. | P | — |
| L3.6.2 | Agentes de navegador y uso de computadora: qué resuelven, cuándo conviene una API o un connector en su lugar, y 🔒 riesgos (sitios no confiables, credenciales, acciones irreversibles). | M | — |

### U3.7 · Delegación de tareas complejas

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.7.1 | Especificar una tarea delegable: objetivo, contexto, criterios de aceptación, límites, permisos y entregable esperado. | M | — |
| L3.7.2 | Supervisar la ejecución agéntica: planes, puntos de control, aprobaciones, tareas programadas y cuándo interrumpir. | P | — |
| L3.7.3 | Verificar resultados: listas de control, contraste con fuentes, pruebas reproducibles y detección de errores plausibles. | P | — |

### U3.8 · Criterio y uso responsable

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L3.8.1 | 🔒 Privacidad: entrenamiento con tus datos, retención, planes personales vs. empresariales y qué nunca subir. | C | — |
| L3.8.2 | Propiedad intelectual, confidencialidad y políticas de uso de IA en empresas (fundamentos; profundización en E3). | C | — |
| L3.8.3 | 🧭 Matriz de decisión y diferencias prácticas entre Claude, ChatGPT y Gemini (contexto, memoria, agentes, extensiones, privacidad, planes); costos verificados al preparar la lección. | M | — |

## Práctica del módulo

- Guiado: la misma tarea de investigación técnica en Claude, ChatGPT y Gemini; comparar calidad, fuentes, tiempo y costo (comparación justificada: es la base de la matriz de decisión).
- Guiado (ChatGPT): proyecto con memoria solo del proyecto, archivos de referencia y una tarea programada que monitorea un cambio; documentar qué entra al contexto y qué se ejecuta sin supervisión.
- Guiado (Claude): configurar un servidor MCP local en la app de escritorio y documentar los permisos otorgados.
- Independiente: evaluar un plugin o skill en Claude y otro en ChatGPT con casos de prueba propios.
- Desafío: delegar una tarea de varios pasos a ChatGPT Work o a Claude (la que no hayas usado en el ejercicio anterior), con especificación, supervisión y verificación documentadas.

## Proyecto o entregable

**Proyecto P2 · Sistema personal de trabajo con IA (parte A).** proyecto configurado en **Claude y en ChatGPT** para una tarea recurrente real, con instrucciones y conocimiento evaluados, al menos un connector o servidor MCP configurado con permisos mínimos, un plugin o skill evaluado, una tarea programada o delegada con su verificación, un *playbook* de delegación (plantilla de especificación + lista de verificación) y tu matriz de decisión.

## Cómo se aprueba

P2-A ≥ 80% en la rúbrica; configuración de privacidad revisada en cada plataforma usada; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 permisos de connectors, MCP y plugins; datos sensibles · 📏 comparación sistemática y verificación de resultados · 💰 planes y límites de uso · 🧭 matriz de herramientas.
