# Versiones y cambios del programa

## Dos versiones independientes

| | Versión académica | Versión de publicación |
|---|---|---|
| Qué identifica | El programa: módulos, unidades, lecciones, IDs, tipos, prerrequisitos, horas, proyectos y sistema de evaluación | Qué material está desarrollado y publicado en el repositorio |
| Dónde figura | Página [Sobre el curso](index.md) | `CHANGELOG.md` y etiquetas de Git (`vX.Y.Z`) |
| ¿Obliga a migrar el progreso de un estudiante? | Solo en cambios mayores o menores, y siempre con tabla de equivalencias | Nunca |

**Versión académica:**
- **Mayor (2.0):** cambia la estructura de módulos o la secuencia de etapas. Requiere tabla de equivalencias.
- **Menor (1.3):** se agregan, quitan, reordenan o renumeran lecciones o unidades. Requiere tabla de equivalencias.
- **Corrección (1.2.1):** se corrigen datos, redacción o referencias del programa sin cambiar lecciones. No requiere migrar el progreso.

**Versión de publicación** (versionado semántico del repositorio):
- **0.x** mientras el núcleo no esté completo; **1.0.0** cuando M0 a M17 estén publicados.
- **Menor:** se publica un módulo completo.
- **Parche:** correcciones editoriales, enlaces, actualización de notas de herramientas o mejoras de lecciones ya publicadas.

**No cambian la versión académica:** los enlaces de disponibilidad de las lecciones, la redacción de las lecciones, las notas de herramientas ni las correcciones de enlaces.

**Regla de IDs:** un ID de lección, unidad, módulo o proyecto nunca se reutiliza. Toda renumeración se publica con una tabla de equivalencias en el [registro de cambios académicos](#registro-de-cambios-académicos) para que cada estudiante migre su cuaderno sin perder progreso.

## Registro de cambios académicos

| Versión | Fecha | Cambio | ¿Requiere migración? |
|---|---|---|---|
| 1.3.1 | 24/10/2026 | Correcciones de redacción: se quitan nombres de productos no verificados de la tabla Nivel 1 / Nivel 2, se resumen los principios de diseño y se quita del Módulo 0 un criterio que quedó de la versión 1.2 (protocolo de sesión) | No |
| 1.3 | 15/10/2026 | Nombres más claros para etapas, módulos y lecciones; seguimiento simplificado a tres estados; ruta esencial | Solo si registraste estados con el sistema anterior (ver abajo) |
| 1.2 | 12/10/2026 | Primera versión pública del programa (18 módulos, 233 lecciones, 10 proyectos, núcleo de 486 h). Las versiones de diseño 1.0 y 1.1 no tuvieron estudiantes | No (versión inicial) |

### Cambios de la versión 1.3

**No cambiaron** los contenidos, los IDs de lecciones (`L0.1.1`, `L3.5.2`…), los tipos, las horas, los prerrequisitos ni los proyectos.

**Nombres.** Los bloques pasan a llamarse *etapas* (Bloque I → Etapa 1, y así sucesivamente). Varios módulos tienen nombres más cortos; por ejemplo, "Asistentes de IA: uso profesional, contexto y delegación" pasa a "Asistentes de IA en la práctica". Cada lección tiene un título corto y su descripción completa debajo. "Prerrequisito duro" pasa a "prerrequisito indispensable".

**Ruta esencial.** Cada lección se marca como *Esencial* (183) o *Para profundizar* (50). Todas siguen en el programa; la marca solo indica qué hacer primero.

**Estados de una lección.** Si llevabas tu progreso con los cinco estados anteriores, convertilos así:

| Estado anterior | Estado nuevo |
|---|---|
| ⬜ Pendiente | Por hacer |
| 📖 Estudiada, 🛠️ Practicada o 🔁 Necesita refuerzo | En curso |
| ✅ Aprobada | Completada |
