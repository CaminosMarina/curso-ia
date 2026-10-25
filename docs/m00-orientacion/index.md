---
modulo: M0
titulo: "Orientación y entorno de trabajo"
bloque: I
nivel: general
horas_teoria: 2
horas_practica: 4
---

# Módulo 0 · Orientación y entorno de trabajo

**Etapa 1** · 6 h (2 h de teoría y 4 h de práctica) · 4 lecciones

## Objetivo

Dejar listo el entorno de trabajo, el sistema de registro y las reglas de seguridad y costos del curso.

## Qué vas a aprender

Mapa del curso; entorno reproducible para IA; repositorio Git del curso; manejo seguro de claves de API; control de gastos.

## Antes de empezar

- **Prerrequisitos:** ninguno.
- **Herramientas:** Git, Python 3.12+ con `uv` o `venv`, JDK 21+, Docker, VS Code o IntelliJ, Ollama, cuentas gratuitas de Claude, ChatGPT y Gemini.

## Lecciones

Las lecciones con material tienen enlace. Las marcadas como *Próximamente* ya forman parte del programa y se están escribiendo. Las de la **ruta esencial** son el núcleo del módulo; las marcadas para **profundizar** amplían el tema y se pueden hacer después.

### 0.1 · Cómo funciona este curso

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L0.1.1 | **[Cómo funciona este curso](l0-1-1-mapa-del-curso.md)**<br>Etapas, módulos y lecciones; prerrequisitos; Nivel 1 y Nivel 2; estados de una lección y cómo llevar tu avance. | Conceptual | Esencial | 📝 Borrador |
| L0.1.2 | **[Aprender en un campo que cambia cada mes](l0-1-2-aprender-en-un-campo-que-cambia.md)**<br>Cómo aprender en un campo que cambia cada mes: fuentes oficiales, *changelogs* y cómo verificar lo que dice un modelo (incluido un tutor de IA). | Conceptual | Esencial | 📝 Borrador |

### 0.2 · Entorno de trabajo

| ID | Lección | Tipo | Ruta | Material |
|---|---|---|---|---|
| L0.2.1 | **[Repositorio y entorno de trabajo](l0-2-1-repositorio-y-entorno.md)**<br>Repositorio Git del curso (registros, apuntes y proyectos), estructura de carpetas, entornos de Python y Java, Docker. | Práctica | Esencial | 📝 Borrador |
| L0.2.2 | **[Claves de API y primer modelo local](l0-2-2-claves-y-modelo-local.md)**<br>Claves de API: creación, almacenamiento seguro (`.env`, gestor de secretos, nunca en Git), límites de gasto y alertas. Instalación de Ollama y primer modelo local. | Práctica | Esencial | 📝 Borrador |

## Práctica del módulo

Repositorio creado con `.gitignore` correcto y primer *commit* de los registros; una llamada "hola mundo" a un modelo local y a una API con nivel gratuito; límite de gasto configurado.

## Cómo se aprueba

Entorno funcionando y ninguna clave en el repositorio (verificado con un escáner de secretos como `gitleaks`).

Comprobalo con la [evaluación del módulo](evaluacion.md). Las reglas generales están en [Cómo se aprueba](../sobre/evaluacion.md).
