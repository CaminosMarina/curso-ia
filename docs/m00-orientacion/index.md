---
modulo: M0
titulo: "Orientación, entorno y método"
bloque: I
nivel: general
horas_teoria: 2
horas_practica: 4
---

# M0 · Orientación, entorno y método

**Bloque I** · 6 h (2 h de teoría y 4 h de práctica) · 4 lecciones

## Objetivo

Dejar listo el entorno de trabajo, el sistema de registro y las reglas de seguridad y costos del curso.

## Qué vas a aprender

Mapa del curso; entorno reproducible para IA; repositorio Git del curso; manejo seguro de claves de API; control de gastos.

## Antes de empezar

- **Prerrequisitos:** ninguno.
- **Herramientas:** Git, Python 3.12+ con `uv` o `venv`, JDK 21+, Docker, VS Code o IntelliJ, Ollama, cuentas gratuitas de Claude, ChatGPT y Gemini.

## Lecciones

Las lecciones con material tienen enlace. Las demás forman parte del programa, pero su material todavía se está escribiendo.

### U0.1 · Cómo funciona este curso

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L0.1.1 | [Mapa del curso, niveles 1 y 2, estados de aprendizaje y protocolo de sesión (inicio, cierre y sincronización de registros).](l0-1-1-mapa-del-curso.md) | C | 📝 Borrador |
| L0.1.2 | Cómo aprender en un campo que cambia cada mes: fuentes oficiales, *changelogs* y cómo verificar lo que dice un modelo (incluido un tutor de IA). | C | — |

### U0.2 · Entorno de trabajo

| ID | Lección | Tipo | Material |
|---|---|:-:|---|
| L0.2.1 | Repositorio Git del curso (registros, apuntes y proyectos), estructura de carpetas, entornos de Python y Java, Docker. | P | — |
| L0.2.2 | Claves de API: creación, almacenamiento seguro (`.env`, gestor de secretos, nunca en Git), límites de gasto y alertas. Instalación de Ollama y primer modelo local. | P | — |

## Práctica del módulo

Repositorio creado con `.gitignore` correcto y primer *commit* de los registros; una llamada "hola mundo" a un modelo local y a una API con nivel gratuito; límite de gasto configurado.

## Cómo se aprueba

Entorno funcionando; ninguna clave en el repositorio (verificado con un escáner de secretos como `gitleaks`); protocolo de sesión probado de punta a punta.

Las reglas generales están en [Evaluación y estados](../programa/evaluacion.md).
