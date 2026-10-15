---
modulo: M10
titulo: "Model Context Protocol (MCP)"
bloque: III
nivel: N2
horas_teoria: 11
horas_practica: 21
---

# Módulo 10 · Model Context Protocol (MCP)

**Etapa 3** · **Nivel 2 (construir y profundizar)** · 32 h (11 h de teoría y 21 h de práctica) · 16 lecciones

## Objetivo

Comprender la arquitectura de MCP y construir, asegurar, probar y desplegar servidores y clientes propios, usándolos desde varios hosts.

## Qué vas a aprender

El problema N×M; arquitectura host-cliente-servidor; primitivas (herramientas, recursos, prompts); interacción con el usuario (elicitación mediante *multi round-trip requests*); características deprecadas (Roots, Sampling, Logging); transportes (stdio y Streamable HTTP); especificación 2026-07-28 (núcleo sin estado, `server/discover`) y diferencias con la 2025-11-25; extensiones oficiales (Tasks, MCP Apps, Skills over MCP); autorización OAuth; seguridad; pruebas con MCP Inspector; despliegue remoto; MCP vs. A2A.

## Antes de empezar

- **Prerrequisitos:** [Módulo 9](../m09-agentes-desde-cero/index.md) (indispensable), [Módulo 3](../m03-asistentes/index.md) (recomendado: uso de connectors y MCP en Nivel 1).
- **Herramientas:** SDK oficial de MCP para Python o TypeScript, MCP Java SDK / Spring AI 2.0, MCP Inspector; hosts: app Claude, Claude Code, Codex, ChatGPT (según plan), VS Code o Copilot, Gemini CLI y n8n. **Versión de especificación por SDK:** se verifica al iniciar el módulo (ver la nota de herramientas de cada lección).

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 10.1 · Arquitectura y conceptos

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L10.1.1 | **Qué problema resuelve MCP**<br>Repaso del Nivel 1 y qué problema resuelve MCP. Historia, gobernanza (Agentic AI Foundation) y adopción. | Conceptual | Esencial | Próximamente |
| L10.1.2 | **Host, cliente y servidor**<br>Quién hace qué. MCP como "tool calling estandarizado y descubrible". | Conceptual | Esencial | Próximamente |
| L10.1.3 | **Primitivas del servidor**<br>Herramientas, recursos y prompts. Cuándo usar cada una. | Mixta | Esencial | Próximamente |
| L10.1.4 | **Interacción con el cliente**<br>Elicitación mediante el patrón *multi round-trip requests* (MRTR). Roots, Sampling y Logging: qué eran, por qué se deprecan y con qué se reemplazan. | Conceptual | Esencial | Próximamente |
| L10.1.5 | **Transportes y especificación vigente**<br>Transportes: stdio vs. Streamable HTTP (HTTP+SSE deprecado). Núcleo sin estado de la especificación 2026-07-28 (`server/discover`, sin sesiones de protocolo) y qué cambia respecto de la 2025-11-25. | Mixta | Esencial | Próximamente |

### 10.2 · Construir servidores

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L10.2.1 | **Primer servidor en Python**<br>Herramientas y recursos, probado con MCP Inspector. | Práctica | Esencial | Próximamente |
| L10.2.2 | **Servidor en Java con Spring AI**<br>Servidor en Java con Spring AI (`@McpTool`, `@McpResource`) sobre una API REST o base de datos existente. | Práctica | Profundizar | Próximamente |
| L10.2.3 | **Diseño de servidores para agentes**<br>Pocas herramientas bien descritas vs. "envolver toda la API". Errores, paginación, orden determinista y caché de listas. | Mixta | Esencial | Próximamente |
| L10.2.4 | **Extensiones oficiales**<br>Tasks (operaciones largas), MCP Apps (interfaces interactivas) y Skills over MCP. Concepto y ejemplo según soporte de SDK y host `[Verificar]`. | Mixta | Profundizar | Próximamente |

### 10.3 · Clientes e integración

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L10.3.1 | **Configuración avanzada en hosts**<br>Ámbitos, servidores remotos con OAuth, variables y depuración (amplía L3.5.2 y L4.3.2). | Práctica | Esencial | Próximamente |
| L10.3.2 | **Cliente MCP propio**<br>Construir un cliente MCP propio e integrarlo al agente de P5. | Práctica | Esencial | Próximamente |
| L10.3.3 | **Ecosistema y registros de servidores**<br>Ecosistema: registros de servidores y cómo evaluarlos antes de instalarlos. | Mixta | Profundizar | Próximamente |

### 10.4 · Seguridad y despliegue

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L10.4.1 | **Autorización en servidores remotos**<br>OAuth 2.1/OIDC, *scopes*, tokens y registro de clientes (Client ID Metadata Documents; Dynamic Client Registration deprecado). | Mixta | Esencial | Próximamente |
| L10.4.2 | **Amenazas y mitigaciones**<br>Amenazas: *tool poisoning*, *prompt injection* indirecta vía resultados, *confused deputy*, robo de credenciales y servidores maliciosos. Mitigaciones. | Mixta | Esencial | Próximamente |
| L10.4.3 | **Despliegue y observabilidad**<br>Despliegue remoto (contenedor, *serverless*), observabilidad con trazas (OpenTelemetry) y versionado. | Práctica | Profundizar | Próximamente |
| L10.4.4 | **MCP vs. API, skills y A2A**<br>MCP vs. API directa vs. skill vs. A2A: cuándo usar cada uno. | Conceptual | Esencial | Próximamente |

## Práctica del módulo

- Guiado: servidor MCP de solo lectura sobre una base de datos de ejemplo.
- Guiado: el mismo servidor usado desde tres hosts de proveedores distintos (por ejemplo Claude Code, Codex y VS Code), comparando configuración, autenticación y aprobación de herramientas.
- Independiente: servidor en Java (Spring AI) sobre una API REST propia.
- Desafío: auditar un servidor MCP de terceros; escribir un servidor "malicioso" de laboratorio para entender el *tool poisoning*.

## Proyecto o entregable

**Proyecto P6 · Servidor MCP propio.** servidor que exponga un sistema tuyo con herramientas, recursos y prompts; versiones stdio y HTTP remota con autenticación; tests; documentación; probado en al menos dos hosts de proveedores distintos e integrado en el agente de P5.

## Cómo se aprueba

P6 ≥ 80% en la rúbrica con análisis de seguridad; *teach-back* de la arquitectura; evaluación de módulo ≥ 80%.

Las reglas generales están en [Evaluación y estados](../sobre/evaluacion.md).

## Hilos transversales

🔒 OAuth, *tool poisoning*, permisos · 📏 tests de contrato · 💰 costo de contexto de las definiciones de herramientas · 🧭 MCP vs. alternativas.
