# Registro de cambios

Este repositorio maneja dos versiones independientes (ver [Versiones y cambios](docs/sobre/versiones.md)):

- **Versión académica** (por ejemplo, 1.2): cambios del programa. Solo las versiones mayores y menores pueden requerir migrar el progreso, y siempre con una tabla de equivalencias.
- **Versión de publicación** (`vX.Y.Z`, versionado semántico): qué material está terminado y publicado. **Nunca obliga a migrar el progreso.**

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

## [Sin publicar]

**Versión académica:** 1.3

### Agregado (15/10/2026): modo de lectura "Lofi"

- Cuarto modo de lectura, después de Espresso: *café de medianoche*, inspirado en la estética lofi para estudiar. Fondo índigo, títulos durazno, luz de lámpara en los granos de café, cielo con estrellas en el encabezado y grano de cinta muy suave. Contraste del texto 13:1.

### Cambiado (15/10/2026): curso más amigable e interactivo · versión académica 1.3

- **Nombres más claros:** los bloques pasan a ser *etapas*; varios módulos tienen nombres más cortos (por ejemplo, "Asistentes de IA en la práctica"); cada lección tiene un título corto con su descripción completa debajo; "prerrequisito duro" pasa a "indispensable". Los IDs, contenidos, horas y prerrequisitos no cambian.
- **Sitio reorganizado:** pestañas Inicio, Empezar, Ruta, Módulos, Mi progreso, Glosario y Sobre el curso. `docs/programa/` se repartió en `docs/ruta/` (ruta, lecciones, proyectos, electivas) y `docs/sobre/` (principios, cómo se aprueba, versiones).
- **Seguimiento en tres estados** (Por hacer, En curso, Completada). El cuaderno, las sesiones y los repasos pasan a la guía opcional *Cómo estudiar* (`docs/empezar/metodo.md`). Plantillas del cuaderno simplificadas.
- **Ruta esencial:** cada lección se marca como *Esencial* (183) o *Profundizar* (50); la ruta esencial suma unas 390 h.
- **Interactividad** (`docs/assets/curso.js`, `curso.css` y `hooks/curso.py`): autoevaluaciones que se corrigen al instante (bloques ```` ```quiz ````), selector de estado en cada lección, avance por módulo, página *Mi progreso* con copia de seguridad, mapa interactivo de la ruta, glosario al pasar el mouse y listas tildables que se recuerdan. El progreso se guarda solo en el navegador.
- L0.1.1 reescrita como *Cómo funciona este curso*, con autoevaluación interactiva.
- Plantilla de lección actualizada (título corto y autoevaluación con ```` ```quiz ````).

### Cambiado (13/10/2026): identidad visual "Latte"

- Estilo propio con temática café (`docs/assets/estilo-latte.css`), en lugar de los colores por defecto de Material.
- Tres modos de lectura que se alternan con el botón de la taza: Latte (claro), Cortado (ámbar, menos brillo) y Espresso (oscuro). Contraste del texto entre 10:1 y 14:1 en todos.
- Tipografías: Lexend (texto), Fraunces (títulos) y JetBrains Mono (código).
- Logo propio (taza con tres nodos conectados) y favicon.
- Autoría pública: Marina Caminos. La sección Procedencia del programa se simplificó.

### Cambiado (13/10/2026): el curso pasa a ser un sitio web

- Todo el contenido se movió a `docs/` y se publica como sitio con Material for MkDocs en GitHub Pages (`mkdocs.yml`, `requirements.txt`, `.github/workflows/sitio.yml`).
- `PROGRAMA.md` se dividió en páginas, sin cambiar contenidos, IDs, tipos, prerrequisitos ni horas:
    - `docs/programa/`: el programa (principios, niveles, mapa, horas, hilos y perfil de egreso), el índice de lecciones, los proyectos, la evaluación y las versiones;
    - `docs/mNN-*/index.md`: la portada de cada módulo, con su objetivo, prerrequisitos, lecciones, práctica, proyecto y criterios;
    - `docs/electivas.md`.
- **Una página por lección,** con teoría, práctica paso a paso y autoevaluación. Las soluciones viven en la carpeta `soluciones/` de cada módulo.
- **Plantilla de lección nueva** (`plantillas/leccion.md`): 5 secciones (Teoría, Práctica, Autoevaluación, Resumen, Para profundizar) en lugar de 13. Los ejercicios forman parte de la sección Práctica; se eliminó `plantillas/ejercicio.md`.
- L0.1.1 adaptada al formato nuevo; el ejercicio E0.1.1-a quedó dentro de la lección.
- `COMO-EMPEZAR.md` → `docs/empezar/index.md`; `TUTOR.md` → `docs/empezar/tutor.md`; `GLOSARIO.md` → `docs/glosario.md`.
- `README.md` más corto, con la tabla de módulos y el enlace al sitio.
- `scripts/generar.py` (nuevo): genera el índice de lecciones, el menú del sitio y las tablas de módulos a partir de las portadas y las lecciones.
- `scripts/verificar.py` adaptado a la estructura nueva.
- `hooks/callouts.py` (nuevo): los avisos con sintaxis de GitHub (`> [!NOTE]`) se ven como recuadros en el sitio.

### Agregado (12/10/2026): etapa 0

- Estructura inicial: README, programa académico 1.2 (18 módulos, 233 lecciones, 10 proyectos, núcleo de 486 h), guías para empezar y para estudiar con un tutor de IA, glosario, licencias (CC BY-SA 4.0 para el contenido y MIT para el código) y `.gitignore`.
- Plantillas de lección, ejercicio y evaluación, y el cuaderno del estudiante (`plantillas/`).
- `scripts/verificar.py`: verificaciones de consistencia del programa, formato, enlaces internos, separación de soluciones y privacidad.
- L0.1.1 en estado 📝 borrador, con su ejercicio y sus soluciones.

## Plan de publicación

| Versión | Contenido | Condición |
|---|---|---|
| `v0.1.0` | M0 completo (4 lecciones y evaluación) | Todas las lecciones de M0 en 📗 publicada y verificaciones superadas |
| `v0.x.0` | Un módulo nuevo por versión menor | Módulo completo y verificado |
| `v1.0.0` | Núcleo M0 a M17 completo | — |
