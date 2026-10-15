---
modulo: M12
titulo: "Desarrollo de skills y plugins"
bloque: III
nivel: N2
horas_teoria: 5
horas_practica: 13
---

# Módulo 12 · Desarrollo de skills y plugins

**Etapa 3** · **Nivel 2 (construir y profundizar)** · 18 h (5 h de teoría y 13 h de práctica) · 10 lecciones

## Objetivo

Diseñar, construir, probar, empaquetar y distribuir capacidades reutilizables para agentes, con foco en el estándar abierto Agent Skills y en el sistema de plugins de Claude.

## Qué vas a aprender

Agent Skills por dentro (estructura, `SKILL.md`, divulgación progresiva, scripts y recursos); extensiones propias de cada cliente vs. formato portable; diferencia entre skill, herramienta, servidor MCP, subagente, comando y hook; plugins (componentes y soporte por superficie); marketplaces; evaluación de skills y plugins; cadena de suministro.

## Antes de empezar

- **Prerrequisitos:** [Módulo 3](../m03-asistentes/index.md) y [Módulo 11](../m11-agentes-programacion-avanzado/index.md) (indispensables).
- **Herramientas:** Claude Code y app Claude `[Pago]`; Codex y ChatGPT; Gemini CLI (opcional) para probar portabilidad; Agent Skills por API (opcional `[Pago]`); Spring AI Agent Skills (opcional).

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 12.1 · Agent Skills por dentro

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L12.1.1 | **Repaso y divulgación progresiva**<br>Repaso del Nivel 1. Divulgación progresiva y cómo decide el agente activar una skill. | Conceptual | Esencial | Próximamente |
| L12.1.2 | **Anatomía de una skill**<br>Anatomía: `SKILL.md` (metadatos, descripción que dispara la activación, instrucciones), `scripts/`, `references/`, `assets/`. Campos del estándar vs. extensiones de cada cliente (por ejemplo, controles de invocación de Claude Code o `agents/openai.yaml` de Codex) y límites de carga de cada cliente. | Mixta | Esencial | Próximamente |
| L12.1.3 | **Escribir buenas skills**<br>Descripciones precisas, instrucciones concisas, scripts deterministas para lo que no debe "improvisar" el modelo. | Práctica | Esencial | Próximamente |
| L12.1.4 | **Probar y evaluar skills**<br>¿se activa cuando debe? ¿mejora el resultado? Iteración. | Práctica | Esencial | Próximamente |

### 12.2 · Elegir el mecanismo correcto

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L12.2.1 | **Elegir el mecanismo de extensión**<br>Skill vs. servidor MCP vs. subagente vs. comando vs. hook vs. `AGENTS.md`: matriz de decisión. | Conceptual | Esencial | Próximamente |
| L12.2.2 | **Portabilidad de skills**<br>Portabilidad: la misma skill en Claude, Claude Code, Codex, Gemini CLI y Spring AI; skills distribuidas por MCP. Qué se rompe y por qué. | Práctica | Profundizar | Próximamente |

### 12.3 · Plugins

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L12.3.1 | **Plugins en dos ecosistemas**<br>Plugins de Claude (skills, comandos, agentes, hooks, servidores MCP; qué carga cada superficie) y plugins de ChatGPT/Codex (skills, servidores MCP y hooks del ciclo de vida, con un directorio compartido). Qué es común y qué no es portable. | Mixta | Esencial | Próximamente |
| L12.3.2 | **Marketplaces y distribución**<br>Públicos, privados y de equipo. Versionado y actualización. | Práctica | Profundizar | Próximamente |
| L12.3.3 | **Cadena de suministro**<br>Revisar skills y plugins de terceros (scripts, permisos, connectors) y procedencia. | Mixta | Esencial | Próximamente |
| L12.3.4 | **Costo de contexto y evals de plugins**<br>Medir costo de contexto y uso de un plugin; evals de plugins. | Práctica | Profundizar | Próximamente |

## Práctica del módulo

- Guiado: skill de "revisión de código según tus estándares Java" con script de verificación.
- Guiado: la misma skill en dos clientes distintos.
- Independiente: skill con referencias y plantillas para una tarea recurrente tuya.
- Desafío: auditar una skill pública e identificar riesgos.

## Proyecto o entregable

**Proyecto P7 · Kit de productividad para desarrollo (plugin).** plugin con al menos 3 skills, 2 comandos, 1 hook y tu servidor MCP de P6, con evaluación de cada skill, documentación, tabla de soporte por superficie y distribución vía un marketplace privado (repositorio Git). Las skills y el servidor MCP deben funcionar también en Codex; empaquetarlos además como plugin de Codex es opcional.

## Cómo se aprueba

P7 ≥ 80% en la rúbrica, instalable desde el marketplace; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 cadena de suministro · 📏 evals de skills · 💰 costo de contexto · 🧭 elegir el mecanismo de extensión.
