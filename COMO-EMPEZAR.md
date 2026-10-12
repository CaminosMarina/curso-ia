# Cómo empezar

Esta guía te lleva de cero hasta la primera lección. Tarda unos 20 minutos y no requiere pagar nada ni crear cuentas.

## 1. Qué vas a tener al final

Dos carpetas separadas:

```
estudio-ia/
├── curso-ia/        ← copia del curso. Solo lectura: no escribas tus datos acá
└── mi-cuaderno/     ← tu cuaderno privado: progreso, respuestas, dificultades y entregables
```

**Por qué dos carpetas:** el curso se actualiza; tu cuaderno es tuyo. Si los mezclás, actualizar el curso puede pisar tus registros o, peor, tus datos personales pueden terminar publicados.

> [!WARNING]
> No guardes tu progreso en un *fork* del curso en GitHub. En GitHub, un fork de un repositorio público también es público. Tu cuaderno va en una carpeta local o en un repositorio **privado** propio.

## 2. Conseguir el curso

Elegí una opción:

| Opción | Cuándo conviene | Cómo |
|---|---|---|
| Leer en GitHub | Solo querés mirar | Abrí [`PROGRAMA.md`](PROGRAMA.md) en el navegador |
| Descargar ZIP | No usás Git todavía | En GitHub: **Code → Download ZIP**, y descomprimilo en `estudio-ia/curso-ia/` |
| Clonar con Git | Ya usás Git (o lo instalás en la lección L0.2.1) | `git clone <URL-del-repositorio> curso-ia` dentro de `estudio-ia/` |

Con Git, para actualizar el curso más adelante alcanza con ejecutar `git pull` dentro de `curso-ia/` (ver el paso 7).

## 3. Crear tu cuaderno privado

Copiá la carpeta `plantillas/cuaderno-estudiante/` **fuera** del curso, con el nombre `mi-cuaderno`.

- **Explorador de archivos:** copiá la carpeta y pegala dentro de `estudio-ia/`; después renombrala a `mi-cuaderno`.
- **Terminal (Linux, macOS o Git Bash),** desde `estudio-ia/`:
  ```bash
  cp -r curso-ia/plantillas/cuaderno-estudiante mi-cuaderno
  ```
- **PowerShell (Windows),** desde `estudio-ia\`:
  ```powershell
  Copy-Item -Recurse curso-ia\plantillas\cuaderno-estudiante mi-cuaderno
  ```

El cuaderno contiene:

| Archivo | Para qué sirve |
|---|---|
| `PROGRESO.md` | Estado de cada lección, módulo, proyecto y evaluación; bitácora de sesiones |
| `REFUERZO.md` | Dificultades detectadas, actividades de refuerzo y repasos espaciados |
| `PUNTO-DE-PARTIDA.md` | Tu situación inicial: experiencia, objetivos, tiempo y presupuesto |
| `README.md` | Cómo usar y proteger el cuaderno |
| `.gitignore` | Evita subir credenciales si convertís el cuaderno en un repositorio |

## 4. Completar los datos iniciales

1. Abrí `mi-cuaderno/PUNTO-DE-PARTIDA.md` y completalo. No anotes datos sensibles (documentos, direcciones, contraseñas, información confidencial de tu trabajo).
2. Abrí `mi-cuaderno/PROGRESO.md` y completá el encabezado: versión académica del programa (figura arriba de todo en `PROGRAMA.md`; hoy es **1.2**), modalidad y dedicación semanal.

## 5. Elegir modalidad

### Modalidad autónoma

Por cada lección:

1. **Inicio de sesión.** Abrí tu `PROGRESO.md`, revisá la "Próxima actividad" y los repasos pendientes en `REFUERZO.md`.
2. **Estudio.** Leé la lección completa en orden: conceptos, propósito, explicación, ejemplos y aplicación con herramientas.
3. **Práctica.** Hacé la práctica guiada y el ejercicio independiente. Guardá la evidencia en tu cuaderno.
4. **Autoevaluación.** Respondé por escrito, **sin mirar las soluciones**. Después corregí con la carpeta [`soluciones/`](soluciones/).
5. **Cierre.** Actualizá el estado de la lección **solo con evidencia**, registrá las horas reales y la próxima actividad.

La lección L0.1.1 explica este protocolo en detalle y lo practica.

### Modalidad con tutor de IA

Seguí [`TUTOR.md`](TUTOR.md). En resumen: le das al asistente las instrucciones de tutor, el programa, la lección actual y tu cuaderno. El tutor explica, pregunta, corrige y propone cambios al cuaderno, pero **las fuentes de verdad son el material del curso y tu cuaderno**, no la memoria del asistente.

Las dos modalidades se pueden combinar: por ejemplo, estudiar solo y usar el tutor para corregir la autoevaluación o destrabar una duda.

## 6. Empezar

Abrí la primera lección: [L0.1.1 · Mapa del curso, niveles 1 y 2, estados de aprendizaje y protocolo de sesión](modulos/m00-orientacion/l0-1-1-mapa-del-curso.md).

Después seguí el orden de [`PROGRAMA.md`](PROGRAMA.md), respetando los prerrequisitos de la sección 3. Si una lección todavía no tiene material (no tiene enlace en el programa), podés estudiarla con fuentes oficiales o con un tutor, sabiendo que ese contenido no fue revisado por el curso.

## 7. Mantener el curso actualizado

1. Actualizá tu copia: `git pull` dentro de `curso-ia/` o descargá un ZIP nuevo. Tu cuaderno no se toca, porque está en otra carpeta.
2. Leé [`CHANGELOG.md`](CHANGELOG.md):
   - Si solo cambió la **versión de publicación** (lecciones nuevas, correcciones, notas de herramientas actualizadas), no tenés que hacer nada en tu cuaderno.
   - Si cambió la **versión académica** con una versión mayor o menor, aplicá la tabla de equivalencias de la sección 10.3 de `PROGRAMA.md` en tu cuaderno y anotá la migración en tu `PROGRESO.md`.

## Costos

M0 está diseñado para hacerse con herramientas y cuentas gratuitas; cada lección indica sus requisitos verificados. Cuando una lección necesita un plan pago, una API paga o infraestructura adicional, lo indica en "Antes de empezar" y en `PROGRAMA.md` (marcas `[Pago]`), con alternativas gratuitas cuando existen.
