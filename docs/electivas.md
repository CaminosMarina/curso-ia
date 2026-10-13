# Electivas

Las electivas son especializaciones opcionales. Se pueden intercalar cuando se cumplen sus prerrequisitos duros. No tienen lecciones numeradas: su desglose se define al elegirlas.

## Qué es obligatorio y qué es electivo

**Criterio de clasificación:** es **obligatorio** lo que necesitás para usar la IA moderna profesionalmente o para construir con seguridad. Es **electivo** lo que constituye una especialización.

| Capacidad | Obligatorio (dónde) | Electivo |
|---|---|---|
| Entender la multimodalidad | [M1](m01-fundamentos-llm/index.md) (L1.5.2), [M3](m03-asistentes/index.md) (L3.6.1), [M8](m08-rag/index.md) (L8.1.1) | — |
| Usar visión, documentos y voz | [M3](m03-asistentes/index.md) (L3.6.1) | — |
| Usar agentes de navegador y de computadora con criterio y seguridad | [M3](m03-asistentes/index.md) (L3.6.2) | — |
| Desarrollar agentes de navegador/computadora, voz en tiempo real, generación de imágenes | — | E1 |
| Panorama de modelos abiertos y ejecución local básica | [M0](m00-orientacion/index.md), [M1](m01-fundamentos-llm/index.md) (L1.5.3), [M3](m03-asistentes/index.md) (L3.3.6) | — |
| Cuantización, servidores de inferencia y *fine-tuning* | Criterio de cuándo usarlo: [M2](m02-prompt-engineering/index.md), [M8](m08-rag/index.md) (L8.3.4) | E2 |
| Privacidad, propiedad intelectual y políticas de uso | [M3](m03-asistentes/index.md) (L3.8.1, L3.8.2), [M16](m16-produccion/index.md) (L16.1.5, L16.4.4) | — |
| Marco regulatorio en profundidad y evaluación de impacto | — | E3 |

## E1 · Multimodalidad avanzada y agentes de computadora/navegador

**12 h** (4 h de teoría y 8 h de práctica)

- **Prerrequisitos:** [M3](m03-asistentes/index.md) y [M9](m09-agentes-desde-cero/index.md) (duros).
- **Contenido:** cómo funcionan por dentro los agentes de navegador y de uso de computadora; construir uno en un entorno aislado; agentes de voz en tiempo real; generación de imágenes por API; extracción robusta desde documentos escaneados; riesgos específicos y mitigaciones.
- **Práctica:** agente que completa una tarea en un navegador aislado; pipeline de extracción desde PDF escaneados con visión.
- **Aprobación:** proyecto corto con análisis de riesgos.

## E2 · Modelos abiertos, ejecución local y fine-tuning

**22 h** (8 h de teoría y 14 h de práctica)

- **Prerrequisitos:** [M1](m01-fundamentos-llm/index.md) (duro), [M8](m08-rag/index.md) (recomendado).
- **Contenido:** ecosistema de modelos abiertos y licencias; cuantización y requisitos de hardware; servidores de inferencia (Ollama, llama.cpp, vLLM); cuándo hacer *fine-tuning* (y cuándo no); LoRA/QLoRA; preparación de *datasets*; evaluación antes y después; destilación.
- **Práctica:** *fine-tuning* LoRA de un modelo pequeño en un entorno gratuito o de bajo costo y comparación con *prompting* y RAG.
- **Aprobación:** informe comparativo con métricas. `[Puede requerir GPU en la nube de bajo costo]`

## E3 · Ética, marco legal y gobernanza de IA

**6 h** (5 h de teoría y 1 h de práctica)

- **Prerrequisitos:** [M3](m03-asistentes/index.md) (duro).
- **Contenido:** sesgos, transparencia y responsabilidad; propiedad intelectual y licencias de código generado (profundización de L3.8.2); protección de datos personales (la normativa del país de cada estudiante; por ejemplo, la Ley 25.326 de Argentina y su eventual actualización, con el GDPR como referencia); EU AI Act y clasificación de riesgo; políticas corporativas.
- **Práctica:** evaluación de impacto de uno de tus proyectos.
- **Aprobación:** documento de evaluación. `[Verificar el estado normativo vigente al preparar el módulo]`
