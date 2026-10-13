---
modulo: M10
titulo: "Model Context Protocol: desarrollo"
bloque: III
nivel: N2
horas_teoria: 11
horas_practica: 21
---

# M10 · Model Context Protocol: desarrollo

**Bloque III** · **Nivel 2 (construir y profundizar)** · 32 h (11 h de teoría y 21 h de práctica) · 16 lecciones

## Objetivo

Comprender la arquitectura de MCP y construir, asegurar, probar y desplegar servidores y clientes propios, usándolos desde varios hosts.

## Qué vas a aprender

El problema N×M; arquitectura host-cliente-servidor; primitivas (herramientas, recursos, prompts); interacción con el usuario (elicitación mediante *multi round-trip requests*); características deprecadas (Roots, Sampling, Logging); transportes (stdio y Streamable HTTP); especificación 2026-07-28 (núcleo sin estado, `server/discover`) y diferencias con la 2025-11-25; extensiones oficiales (Tasks, MCP Apps, Skills over MCP); autorización OAuth; seguridad; pruebas con MCP Inspector; despliegue remoto; MCP vs. A2A.

## Antes de empezar

- **Prerrequisitos:** [M9](../m09-agentes-desde-cero/index.md) (duro), [M3](../m03-asistentes/index.md) (recomendado: uso de connectors y MCP en Nivel 1).
- **Herramientas:** SDK oficial de MCP para Python o TypeScript, MCP Java SDK / Spring AI 2.0, MCP Inspector; hosts: app Claude, Claude Code, Codex, ChatGPT (según plan), VS Code o Copilot, Gemini CLI y n8n. **Versión de especificación por SDK:** se verifica al iniciar el módulo (ver la nota de herramientas de cada lección).

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U10.1 · Arquitectura y conceptos

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L10.1.1 | Repaso del Nivel 1 y qué problema resuelve MCP. Historia, gobernanza (Agentic AI Foundation) y adopción. | C | — |
| L10.1.2 | Host, cliente y servidor: quién hace qué. MCP como "tool calling estandarizado y descubrible". | C | — |
| L10.1.3 | Primitivas del servidor: herramientas, recursos y prompts. Cuándo usar cada una. | M | — |
| L10.1.4 | Interacción con el cliente: elicitación mediante el patrón *multi round-trip requests* (MRTR). Roots, Sampling y Logging: qué eran, por qué se deprecan y con qué se reemplazan. | C | — |
| L10.1.5 | Transportes: stdio vs. Streamable HTTP (HTTP+SSE deprecado). Núcleo sin estado de la especificación 2026-07-28 (`server/discover`, sin sesiones de protocolo) y qué cambia respecto de la 2025-11-25. | M | — |

### U10.2 · Construir servidores

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L10.2.1 | Primer servidor en Python: herramientas y recursos, probado con MCP Inspector. | P | — |
| L10.2.2 | Servidor en Java con Spring AI (`@McpTool`, `@McpResource`) sobre una API REST o base de datos existente. | P | — |
| L10.2.3 | Diseño de servidores para agentes: pocas herramientas bien descritas vs. "envolver toda la API". Errores, paginación, orden determinista y caché de listas. | M | — |
| L10.2.4 | Extensiones oficiales: Tasks (operaciones largas), MCP Apps (interfaces interactivas) y Skills over MCP. Concepto y ejemplo según soporte de SDK y host `[Verificar]`. | M | — |

### U10.3 · Clientes e integración

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L10.3.1 | Configuración avanzada en hosts: ámbitos, servidores remotos con OAuth, variables y depuración (amplía L3.5.2 y L4.3.2). | P | — |
| L10.3.2 | Construir un cliente MCP propio e integrarlo al agente de P5. | P | — |
| L10.3.3 | Ecosistema: registros de servidores y cómo evaluarlos antes de instalarlos. | M | — |

### U10.4 · Seguridad y despliegue

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L10.4.1 | 🔒 Autorización en servidores remotos: OAuth 2.1/OIDC, *scopes*, tokens y registro de clientes (Client ID Metadata Documents; Dynamic Client Registration deprecado). | M | — |
| L10.4.2 | 🔒 Amenazas: *tool poisoning*, *prompt injection* indirecta vía resultados, *confused deputy*, robo de credenciales y servidores maliciosos. Mitigaciones. | M | — |
| L10.4.3 | Despliegue remoto (contenedor, *serverless*), observabilidad con trazas (OpenTelemetry) y versionado. | P | — |
| L10.4.4 | 🧭 MCP vs. API directa vs. skill vs. A2A: cuándo usar cada uno. | C | — |

## Práctica del módulo

- Guiado: servidor MCP de solo lectura sobre una base de datos de ejemplo.
- Guiado: el mismo servidor usado desde tres hosts de proveedores distintos (por ejemplo Claude Code, Codex y VS Code), comparando configuración, autenticación y aprobación de herramientas.
- Independiente: servidor en Java (Spring AI) sobre una API REST propia.
- Desafío: auditar un servidor MCP de terceros; escribir un servidor "malicioso" de laboratorio para entender el *tool poisoning*.

## Proyecto o entregable

**Proyecto P6 · Servidor MCP propio.** servidor que exponga un sistema tuyo con herramientas, recursos y prompts; versiones stdio y HTTP remota con autenticación; tests; documentación; probado en al menos dos hosts de proveedores distintos e integrado en el agente de P5.

## Cómo se aprueba

P6 ≥ 80% en la rúbrica con análisis de seguridad; *teach-back* de la arquitectura; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).

## Hilos transversales

🔒 OAuth, *tool poisoning*, permisos · 📏 tests de contrato · 💰 costo de contexto de las definiciones de herramientas · 🧭 MCP vs. alternativas.
