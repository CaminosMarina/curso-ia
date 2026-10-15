# Proyectos

Los proyectos son incrementales: cada uno reutiliza piezas de los anteriores.

| ID | Proyecto | Módulos | Qué construís | Reutiliza | Complejidad |
|---|---|---|---|---|---|
| P1 | Biblioteca de prompts evaluada | [Módulo 2](../m02-prompt-engineering/index.md) | Prompts versionados con casos de prueba en varios modelos | — | ★ |
| P2 | Sistema personal de trabajo con IA (partes A, B y C, en cualquier orden) | [Módulo 3](../m03-asistentes/index.md), [Módulo 4](../m04-agentes-programacion/index.md), [Módulo 5](../m05-n8n/index.md) | Claude y ChatGPT configurados, MCP/plugins evaluados, *playbook* de delegación, repositorio listo para Claude Code y Codex, primer workflow n8n | P1 | ★★ |
| P3 | DevAssist CLI | [Módulo 6](../m06-apis-modelos/index.md), [Módulo 7](../m07-context-engineering/index.md) | CLI multiproveedor con salidas estructuradas, herramienta, costos, contexto y memoria | P1 | ★★ |
| P4 | RAG sobre documentación técnica | [Módulo 8](../m08-rag/index.md) | Ingesta, búsqueda híbrida, citas y evaluación con métricas | P3 | ★★★ |
| P5 | Agente desde cero | [Módulo 9](../m09-agentes-desde-cero/index.md) | Agente sin frameworks con planificación, memoria, HITL y evals | P3, P4 | ★★★ |
| P6 | Servidor MCP propio | [Módulo 10](../m10-mcp/index.md) | Servidor stdio + HTTP con OAuth, usado en varios hosts y en P5 | P5 | ★★★ |
| P7 | Kit de productividad para desarrollo (plugin) | [Módulo 11](../m11-agentes-programacion-avanzado/index.md), [Módulo 12](../m12-skills-plugins/index.md) | Skills, comandos, hooks y MCP empaquetados y distribuidos; skills y MCP probados también en Codex | P2-B, P6 | ★★★ |
| P8 | Automatización inteligente con n8n | [Módulo 13](../m13-n8n-ia/index.md) | Workflow de producción con LLM, agente, RAG, MCP y aprobación humana | P2-C, P4, P6 | ★★★★ |
| P9 | Sistema multiagente | [Módulo 14](../m14-frameworks-agentes/index.md), [Módulo 15](../m15-multiagente/index.md) | Orquestación, A2A opcional, trazas, presupuestos y comparación | P5, P6 | ★★★★ |
| P10 | Proyecto final integrador | [Módulo 17](../m17-proyecto-final/index.md) | Solución integral a elección | Todos | ★★★★★ |

**No numerados (entregables o actividades):** informe de [Módulo 1](../m01-fundamentos-llm/index.md); P3 extendido en [Módulo 7](../m07-context-engineering/index.md); base de P7 en [Módulo 11](../m11-agentes-programacion-avanzado/index.md); base de P9 en [Módulo 14](../m14-frameworks-agentes/index.md); actividad integradora de producción en [Módulo 16](../m16-produccion/index.md).

**Ubicación de entregables:** cada proyecto vive en tu cuaderno o en un repositorio propio enlazado desde tu `PROGRESO.md`, nunca dentro del repositorio del curso.

**P2 en partes:** P2-A, P2-B y P2-C se registran y aprueban por separado y pueden completarse en cualquier orden (por ejemplo, P2-C antes que P2-A si cursás [Módulo 5](../m05-n8n/index.md) primero). P2 se considera aprobado cuando las tres partes están aprobadas.
