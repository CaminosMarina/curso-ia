# Cómo empezar

Esta guía te lleva de cero hasta la primera lección. Tarda unos 20 minutos y no requiere pagar nada ni crear cuentas.

Podés leer todo el curso en este sitio. Lo que necesitás descargar es solo la **plantilla de tu cuaderno**, donde vas a registrar tu progreso.

## 1. Qué vas a tener al final

Dos carpetas separadas:

```
estudio-ia/
├── curso-ia/        ← copia del curso (opcional). Solo lectura: no escribas tus datos acá
└── mi-cuaderno/     ← tu cuaderno privado: progreso, respuestas, dificultades y entregables
```

**Por qué dos carpetas:** el curso se actualiza; tu cuaderno es tuyo. Si los mezclás, actualizar el curso puede pisar tus registros o, peor, tus datos personales pueden terminar publicados.

> [!WARNING]
> No guardes tu progreso en un *fork* del curso en GitHub. En GitHub, un fork de un repositorio público también es público. Tu cuaderno va en una carpeta local o en un repositorio **privado** propio.

## 2. Conseguir el curso

Elegí una opción:

| Opción | Cuándo conviene | Cómo |
|---|---|---|
| Leer en este sitio | Querés estudiar sin instalar nada | Seguí leyendo acá. Para el cuaderno, descargá el ZIP de la opción siguiente |
| Descargar ZIP | No usás Git todavía | En el [repositorio](https://github.com/CaminosMarina/curso-ia): **Code → Download ZIP**, y descomprimilo en `estudio-ia/curso-ia/` |
| Clonar con Git | Ya usás Git (o lo instalás en la lección L0.2.1) | `git clone https://github.com/CaminosMarina/curso-ia.git curso-ia` dentro de `estudio-ia/` |

Con Git, para actualizar el curso más adelante alcanza con ejecutar `git pull` dentro de `curso-ia/` (ver el paso 7).

## 3. Crear tu cuaderno privado

Copiá la carpeta [`plantillas/cuaderno-estudiante/`](https://github.com/CaminosMarina/curso-ia/tree/main/plantillas/cuaderno-estudiante) **fuera** del curso, con el nombre `mi-cuaderno`.

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
2. Abrí `mi-cuaderno/PROGRESO.md` y completá el encabezado: versión académica del programa (figura arriba de todo en [El programa](../programa/index.md); hoy es **1.2**), modalidad y dedicación semanal.

## 5. Elegir modalidad

### Modalidad autónoma

Por cada lección:

1. **Inicio de sesión.** Abrí tu `PROGRESO.md`, revisá la "Próxima actividad" y los repasos pendientes en `REFUERZO.md`.
2. **Estudio.** Leé la lección completa en orden: conceptos, propósito, explicación, ejemplos y aplicación con herramientas.
3. **Práctica.** Hacé la práctica guiada y el ejercicio independiente. Guardá la evidencia en tu cuaderno.
4. **Autoevaluación.** Respondé por escrito, **sin mirar las soluciones**. Después corregí con la página de soluciones que enlaza cada lección.
5. **Cierre.** Actualizá el estado de la lección **solo con evidencia**, registrá las horas reales y la próxima actividad.

La lección L0.1.1 explica este protocolo en detalle y lo practica.

### Modalidad con tutor de IA

Seguí [Estudiar con un tutor de IA](tutor.md). En resumen: le das al asistente las instrucciones de tutor, el programa, la lección actual y tu cuaderno. El tutor explica, pregunta, corrige y propone cambios al cuaderno, pero **las fuentes de verdad son el material del curso y tu cuaderno**, no la memoria del asistente.

Las dos modalidades se pueden combinar: por ejemplo, estudiar solo y usar el tutor para corregir la autoevaluación o destrabar una duda.

## 6. Empezar

Abrí la primera lección: [L0.1.1 · Mapa del curso y protocolo de sesión](../m00-orientacion/l0-1-1-mapa-del-curso.md).

Después seguí el [índice de lecciones](../programa/indice.md), respetando los prerrequisitos de cada módulo. Si una lección todavía no tiene material (no tiene enlace en el índice), podés estudiarla con fuentes oficiales o con un tutor, sabiendo que ese contenido no fue revisado por el curso.

## 7. Mantener el curso actualizado

1. Si tenés una copia local, actualizala: `git pull` dentro de `curso-ia/` o descargá un ZIP nuevo. Si leés en el sitio, siempre ves la última versión. Tu cuaderno no se toca, porque está en otra carpeta.
2. Leé el [registro de cambios](https://github.com/CaminosMarina/curso-ia/blob/main/CHANGELOG.md):
    - Si solo cambió la **versión de publicación** (lecciones nuevas, correcciones, notas de herramientas actualizadas), no tenés que hacer nada en tu cuaderno.
    - Si cambió la **versión académica** con una versión mayor o menor, aplicá la tabla de equivalencias de [Versiones y cambios](../programa/versiones.md) en tu cuaderno y anotá la migración en tu `PROGRESO.md`.

## Costos

M0 está diseñado para hacerse con herramientas y cuentas gratuitas; cada lección indica sus requisitos verificados. Cuando una lección necesita un plan pago, una API paga o infraestructura adicional, lo indica en "Antes de empezar" y en la portada del módulo (marcas `[Pago]`), con alternativas gratuitas cuando existen.
