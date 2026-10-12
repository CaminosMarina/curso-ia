# Mi cuaderno del curso de IA

Este es tu cuaderno **privado**: tu progreso, tus respuestas, tus dificultades y tus entregables.

## Reglas

1. **Vive fuera de la carpeta del curso.** Si lo guardás dentro, una actualización del curso puede mezclarse con tus datos o publicarlos por error.
2. **No lo subas a un fork del curso.** En GitHub, un fork de un repositorio público es público. Si querés respaldo en GitHub, creá un repositorio **privado** aparte.
3. **No guardes credenciales.** Ninguna clave de API, contraseña ni archivo `.env` va en los archivos `.md`. El `.gitignore` de esta carpeta ayuda, pero no reemplaza el cuidado.
4. **Cada cambio de estado necesita evidencia** (una respuesta escrita, un archivo, un *commit*, una salida de comando). Guardá la evidencia en `evidencias/`, `proyectos/` o donde prefieras, y enlazala desde `PROGRESO.md`.
5. **Vos controlás el registro.** Si usás un tutor de IA, él solo propone cambios; verificá cada cambio abriendo el archivo.

## Archivos

| Archivo | Contenido |
|---|---|
| `PROGRESO.md` | Encabezado, estado de lecciones, módulos, proyectos y evaluaciones; bitácora de sesiones; migraciones |
| `REFUERZO.md` | Dificultades, actividades de refuerzo y repasos espaciados |
| `PUNTO-DE-PARTIDA.md` | Tu situación inicial y tus objetivos |
| `.gitignore` | Evita versionar credenciales y archivos generados |

Podés crear las carpetas que necesites (por ejemplo `evidencias/`, `apuntes/`, `proyectos/`).

## Si querés versionarlo con Git (opcional)

Se explica en la lección L0.2.1. En resumen, dentro de esta carpeta:

```bash
git init
git add .
git status        # revisá la lista ANTES de confirmar: no debe aparecer ningún secreto
git commit -m "Inicio del cuaderno"
```
