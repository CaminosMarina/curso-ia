# Versiones y cambios del programa

## Dos versiones independientes

| | Versión académica | Versión de publicación |
|---|---|---|
| Qué identifica | El programa: módulos, unidades, lecciones, IDs, tipos, prerrequisitos, horas, proyectos y sistema de evaluación | Qué material está desarrollado y publicado en el repositorio |
| Dónde figura | Página [El programa](index.md) | `CHANGELOG.md` y etiquetas de Git (`vX.Y.Z`) |
| ¿Obliga a migrar el progreso de un estudiante? | Solo en cambios mayores o menores, y siempre con tabla de equivalencias | Nunca |

**Versión académica:**
- **Mayor (2.0):** cambia la estructura de módulos o la secuencia de bloques. Requiere tabla de equivalencias.
- **Menor (1.3):** se agregan, quitan, reordenan o renumeran lecciones o unidades. Requiere tabla de equivalencias.
- **Corrección (1.2.1):** se corrigen datos, redacción o referencias del programa sin cambiar lecciones. No requiere migrar el progreso.

**Versión de publicación** (versionado semántico del repositorio):
- **0.x** mientras el núcleo no esté completo; **1.0.0** cuando M0 a M17 estén publicados.
- **Menor:** se publica un módulo completo.
- **Parche:** correcciones editoriales, enlaces, actualización de notas de herramientas o mejoras de lecciones ya publicadas.

**No cambian la versión académica:** los enlaces de disponibilidad de las lecciones, la redacción de las lecciones, las notas de herramientas ni las correcciones de enlaces.

**Regla de IDs:** un ID de lección, unidad, módulo o proyecto nunca se reutiliza. Toda renumeración se publica con una tabla de equivalencias en el [registro de cambios académicos](#registro-de-cambios-académicos) para que cada estudiante migre su cuaderno sin perder progreso.

## Procedencia

Este programa es la versión pública de la versión académica 1.2 (12/10/2026) del curso de origen. Las únicas adaptaciones fueron:

1. **Encabezado:** se quitaron el perfil de la persona para la que se diseñó originalmente, la fecha de aprobación individual y las referencias a sus documentos privados; se agregaron público destinatario, procedencia y disponibilidad.
2. **Principio 5:** "el profesor" de la instancia original pasa a "un tutor de IA opcional".
3. **Principio 7:** la justificación de Java ya no se refiere al trabajo de una persona concreta.
4. **Redacción inclusiva:** "como usuaria" pasa a "como persona usuaria" y "experiencia de usuaria" a "experiencia de uso".
5. **Referencias a documentos privados:** las menciones a `DIAGNOSTICO.md` pasan a la nota de herramientas de cada lección; `PROGRESO.md` y `REFUERZO.md` pasan a ser los del cuaderno de cada estudiante. "Al dictar" pasa a "al preparar".
6. **L0.1.2 y U17.2:** "tu profesor" y "revisión del profesor" pasan a tutor, par o autoevaluación con rúbrica.
7. **Estado 📖:** "Explicada (el profesor desarrolló la lección)" pasa a "Estudiada (por tu cuenta o con un tutor)", con el mismo símbolo y el mismo lugar en la secuencia de estados.
8. **E3 y P10-C:** la normativa de datos personales se generaliza al país de cada estudiante (con Argentina como ejemplo), y "tu stack Java" pasa a "Java".
9. **Entregables (proyectos):** viven en el cuaderno de cada estudiante, no en el repositorio del curso.
10. **Resumen de horas:** se quitó el párrafo sobre la evolución de horas entre versiones de diseño. **Sección de versiones:** se reemplazó por esta página.
11. **Organización en páginas (13/10/2026):** el programa, que era un único archivo, se dividió en estas páginas del sitio y en la portada de cada módulo. Los contenidos, IDs, tipos, prerrequisitos, horas y proyectos no cambiaron.

Las versiones de diseño 1.0 (200 lecciones) y 1.1 (227 lecciones) no tuvieron estudiantes con progreso en este repositorio; por eso no se incluyen sus tablas de equivalencias.

## Registro de cambios académicos

| Versión | Fecha | Cambio | ¿Requiere migración? |
|---|---|---|---|
| 1.2 | 12/10/2026 | Primera versión pública del programa (18 módulos, 233 lecciones, 10 proyectos, núcleo de 486 h) | No (versión inicial) |
