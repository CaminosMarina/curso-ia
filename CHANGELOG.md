# Registro de cambios

Este repositorio maneja dos versiones independientes ([`PROGRAMA.md`](PROGRAMA.md), sección 10):

- **Versión académica** (por ejemplo, 1.2): cambios del programa. Solo las versiones mayores y menores pueden requerir migrar el progreso, y siempre con una tabla de equivalencias.
- **Versión de publicación** (`vX.Y.Z`, versionado semántico): qué material está terminado y publicado. **Nunca obliga a migrar el progreso.**

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

## [Sin publicar]

**Versión académica:** 1.2 (sin cambios académicos)

### Agregado

- Estructura inicial (etapa 0): `README.md`, `PROGRAMA.md`, `COMO-EMPEZAR.md`, `TUTOR.md`, `GLOSARIO.md`, `LICENSE` (CC BY-SA 4.0, contenido), `LICENSE-CODE` (MIT, código), `.gitignore`.
- `PROGRAMA.md`: versión pública del programa académico 1.2 (18 módulos, 233 lecciones, 10 proyectos, núcleo de 486 h), con su procedencia y adaptaciones en la sección 10.2.
- Plantillas de lección, ejercicio y evaluación, y el cuaderno del estudiante (`plantillas/`).
- `scripts/verificar.py`: verificaciones de consistencia del programa, formato de lecciones y ejercicios, enlaces internos, separación de soluciones y privacidad.
- L0.1.1 en estado 📝 borrador, con el ejercicio E0.1.1-a y las soluciones separadas.

## Plan de publicación

| Versión | Contenido | Condición |
|---|---|---|
| `v0.1.0` | M0 completo (4 lecciones, ejercicios, evaluación) | Todas las lecciones de M0 en 📗 publicada y verificaciones superadas; recién ahí el repositorio pasa a público |
| `v0.x.0` | Un módulo nuevo por versión menor | Módulo completo y verificado |
| `v1.0.0` | Núcleo M0 a M17 completo | — |
