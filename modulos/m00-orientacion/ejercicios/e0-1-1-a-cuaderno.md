---
id: E0.1.1-a
leccion: L0.1.1
titulo: "Armar tu cuaderno y probar el protocolo de sesión"
nivel: inicial
tiempo_estimado: 45 min
costo: gratis
estado: borrador
ultima_revision: 2026-10-12
probado_desde_cero: 2026-10-12
soluciones: ../../../soluciones/m00/l0-1-1.md
---

# E0.1.1-a · Armar tu cuaderno y probar el protocolo de sesión

## Objetivo

Demostrar que sabés crear tu registro privado, separado del curso, y aplicar el protocolo de sesión completo (inicio, trabajo y cierre) con estados respaldados por evidencia.

## Requisitos

| Requisito | Detalle |
|---|---|
| Software | Un editor de texto. Opcional: una terminal (Bash, Git Bash o PowerShell) para los comandos de verificación |
| Cuentas | Ninguna |
| Sistema operativo | Cualquiera |
| Costo | Gratis |
| Conocimientos | Haber estudiado L0.1.1 |

## Preparación

1. Tené una copia del curso en tu computadora, por ejemplo en `estudio-ia/curso-ia/` ([`COMO-EMPEZAR.md`](../../../COMO-EMPEZAR.md), paso 2). Si solo lo leés en GitHub, descargá el ZIP.
2. Ubicá la carpeta `curso-ia/plantillas/cuaderno-estudiante/`.

## Consigna

1. **Creá tu cuaderno fuera del curso.** Copiá `plantillas/cuaderno-estudiante/` a `estudio-ia/mi-cuaderno/` ([`COMO-EMPEZAR.md`](../../../COMO-EMPEZAR.md), paso 3).
2. **Completá `PUNTO-DE-PARTIDA.md`,** sin datos sensibles.
3. **Completá el encabezado de `PROGRESO.md`:** versión académica del programa, modalidad, dedicación semanal y fecha de inicio.
4. **Abrí la sesión:** en "Sesión en curso", escribí `Abierta · <fecha> · L0.1.1`.
5. **Escribí tu ruta para el Bloque I** (la pregunta de aplicación de la lección) en un archivo nuevo `mi-cuaderno/evidencias/L0.1.1-ruta.md`. Incluí el orden de los módulos, lo que vas a hacer en paralelo, las semanas estimadas (con el cálculo) y la justificación según los prerrequisitos.
6. **Registrá la lección:** agregá en `PROGRESO.md` › Lecciones la fila de L0.1.1 con el estado que corresponde **a lo que hiciste hasta ahora** y el enlace a la evidencia.
7. **Cerrá la sesión:**
   - agregá una fila en la bitácora (fecha, qué hiciste, horas reales, cambio de estado y próxima actividad);
   - dejá "Sesión en curso: Ninguna";
   - completá "Próxima actividad".
8. **Opcional:** si ya hiciste la autoevaluación y la corregiste, actualizá el estado y la evidencia en la fila de L0.1.1 y en la bitácora.

## Criterios de aceptación

El ejercicio está aprobado si se cumplen **todos** estos criterios:

- [ ] `mi-cuaderno/` está **fuera** de la carpeta del curso: `curso-ia/` no contiene ningún archivo tuyo.
- [ ] `mi-cuaderno/` contiene `PROGRESO.md`, `REFUERZO.md`, `PUNTO-DE-PARTIDA.md` y `evidencias/L0.1.1-ruta.md`.
- [ ] El encabezado de `PROGRESO.md` indica la versión académica (la misma que figura arriba de todo en `PROGRAMA.md`), la modalidad y la dedicación semanal.
- [ ] `L0.1.1-ruta.md` respeta los prerrequisitos duros de la sección 3 del programa y el cálculo de semanas usa las horas de la sección 4.
- [ ] La fila de L0.1.1 tiene un estado coherente con la evidencia: 🛠️ si hiciste solo la pregunta de aplicación, o ✅ si además tenés la autoevaluación corregida con 4 o más de 5. Nunca ✅ sin autoevaluación.
- [ ] La columna "Evidencia" apunta a un archivo que existe.
- [ ] La bitácora tiene una fila de esta sesión, con horas reales y la próxima actividad.
- [ ] "Sesión en curso" dice `Ninguna`.
- [ ] Ningún archivo contiene credenciales ni datos sensibles.

## Cómo verificar

**Con una terminal** (Bash o Git Bash), desde `estudio-ia/`:

```bash
ls mi-cuaderno mi-cuaderno/evidencias
grep -n "Versión académica" mi-cuaderno/PROGRESO.md
grep -n "^| L0.1.1" mi-cuaderno/PROGRESO.md
grep -n "Sesión en curso" mi-cuaderno/PROGRESO.md
ls curso-ia | grep -i cuaderno || echo "OK: no hay ningún cuaderno dentro del curso"
```

**Con PowerShell,** desde `estudio-ia\`:

```powershell
Get-ChildItem mi-cuaderno, mi-cuaderno\evidencias
Select-String -Path mi-cuaderno\PROGRESO.md -Pattern "Versión académica", "^\| L0.1.1", "Sesión en curso"
if (-not (Get-ChildItem curso-ia -Filter "*cuaderno*")) { "OK: no hay ningún cuaderno dentro del curso" }
```

**Resultado esperado:** se listan los archivos del cuaderno; aparecen la línea de la versión académica, la fila de L0.1.1 y `Sesión en curso | Ninguna`; y se imprime el mensaje "OK".

**Sin terminal:** abrí cada archivo y recorré los criterios de aceptación uno por uno.

**Con un tutor de IA:** compartile tu `PROGRESO.md` y tu `L0.1.1-ruta.md` y pedile que los revise contra los criterios de aceptación de este ejercicio.

## Qué guardar en tu cuaderno

Todo el ejercicio vive en tu cuaderno; nada se agrega al repositorio del curso. Si después de verificarlo se cumplen todos los criterios, la pregunta de aplicación queda hecha y L0.1.1 queda, como mínimo, en 🛠️.

## Pistas

<details>
<summary>Pista 1 · ¿Qué estado pongo si todavía no hice la autoevaluación?</summary>

Mirá la tabla "Registrar en tu cuaderno" al final de la lección: la pregunta de aplicación es la actividad mínima de una lección `[C]`.

</details>

<details>
<summary>Pista 2 · ¿Cómo calculo las semanas?</summary>

Sumá las horas de los módulos de tu ruta (tabla de la sección 4 del programa), dividilas por tus horas semanales y agregá un 10% de margen.

</details>

<details>
<summary>Pista 3 · ¿Puedo poner M5 antes que M1?</summary>

Mirá cuáles son los prerrequisitos duros de M5 en la sección 3 del programa.

</details>

## Solución

La guía de corrección y un ejemplo resuelto están en [soluciones](../../../soluciones/m00/l0-1-1.md#ejercicio-e011-a). Consultalos después de intentar.
