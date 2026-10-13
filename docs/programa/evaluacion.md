# Evaluación y estados de aprendizaje

## Estados de una lección

| Estado | Significado | Condición para alcanzarlo |
|---|---|---|
| ⬜ **Pendiente** | No empezada | — |
| 📖 **Estudiada** | Recorriste la lección completa, por tu cuenta o con un tutor | Lección leída o explicada de punta a punta (no implica comprensión) |
| 🛠️ **Practicada** | Hiciste la actividad práctica mínima | Actividad entregada y revisada, con evidencia (archivo, *commit*, captura o salida) |
| ✅ **Aprobada** | La comprensión fue verificada | Verificación superada según el tipo de lección (ver [Verificación según el tipo de lección](#verificación-según-el-tipo-de-lección)) |
| 🔁 **Necesita refuerzo** | La verificación de una lección **todavía no aprobada** no se superó | Se registra una dificultad en `REFUERZO.md` de tu cuaderno con su ID |

Una lección **nunca** pasa a "Aprobada" solo porque fue explicada.

**Dificultades posteriores a la aprobación.** Si aparece una dificultad relacionada con una lección ya aprobada, la lección **conserva** su estado ✅, su fecha y su evidencia original; solo se agrega el ID de la dificultad en la columna "Dificultad" (por ejemplo, "D-004"). El refuerzo se gestiona en `REFUERZO.md` de tu cuaderno sin borrar el progreso demostrado. La lección vuelve a 🔁 únicamente si la dificultad muestra que la verificación original no era válida (por ejemplo, se aprobó con un error conceptual de fondo); en ese caso se mantiene la evidencia anterior y se agrega la nueva.

## Reglas de coherencia entre estados

1. **Lección ✅** ⇒ tiene fecha y evidencia de verificación.
2. **Módulo ✅** ⇒ todas sus lecciones ✅, evaluación de módulo ≥ 80% y su proyecto o parte de proyecto aprobados. Una dificultad posterior no le quita el estado, salvo que una lección vuelva a 🔁.
3. **Módulo ⛔ Bloqueado** ⇒ existe una dificultad 🔴 abierta cuyo campo "Bloquea a" incluye ese módulo; solo puede marcarse en módulos no iniciados o en curso.
4. **Proyecto ✅** ⇒ rúbrica ≥ 80% registrada. P2 ✅ ⇒ P2-A, P2-B y P2-C ✅.
5. **Dificultad consolidada o descartada** ⇒ sale de la tabla de activas y se mueve al historial de `REFUERZO.md` de tu cuaderno.

## Verificación según el tipo de lección

| Tipo | Actividad mínima (→ Practicada) | Verificación (→ Aprobada) |
|---|---|---|
| `[C]` Conceptual | Una pregunta de aplicación respondida por escrito (aplicar el concepto a un caso tuyo) | 3 a 5 preguntas de comprensión con ≥ 80% correctas, incluida al menos una de diagnóstico ("¿por qué pasa X?"), o *teach-back* aprobado |
| `[P]` Práctica o de herramienta | Ejercicio de la lección hecho, con evidencia | Ejercicio funcionando y correctamente justificado: explicar qué hiciste y por qué, y responder 1 o 2 preguntas sobre alternativas o riesgos |
| `[M]` Mixta | Ejercicio o pregunta de aplicación | Ambas verificaciones anteriores (preguntas ≥ 80% y ejercicio justificado) |

## Evaluación de módulos y proyectos

| Instrumento | Cuándo | Criterio |
|---|---|---|
| **Evaluación de módulo** | Al cerrar cada módulo | ≥ 80%: preguntas conceptuales, de criterio y de diagnóstico de casos |
| **Proyecto** | Al cierre de los módulos indicados | Rúbrica (abajo) ≥ 80% |
| ***Teach-back*** | Módulos clave (M1, M7, M9, M10) | Explicar el concepto con tus palabras; correcto y completo |
| **Repaso espaciado** | Para dificultades registradas | Ver `REFUERZO.md` de tu cuaderno |

**Un módulo está aprobado cuando:** todas sus lecciones están en ✅; la evaluación de módulo es ≥ 80%; el proyecto o entregable (si tiene) es ≥ 80%; y no quedan dificultades **bloqueantes** abiertas que afecten a ese módulo.

## Cuándo una dificultad bloquea el avance

- Una dificultad es **bloqueante** solo si afecta un conocimiento que es **prerrequisito duro** de la próxima lección o de un módulo siguiente (ver el [mapa de aprendizaje](index.md#mapa-de-aprendizaje)).
- Bloquea **únicamente** las lecciones y módulos que dependen de ese conocimiento. Podés seguir con módulos independientes (por ejemplo, una dificultad en RAG no impide avanzar con n8n Nivel 1).
- Las dificultades no bloqueantes se trabajan en paralelo mediante repasos espaciados.

## Rúbrica de proyectos (100 puntos)

| Criterio | Puntos |
|---|---:|
| Funcionalidad: cumple los requisitos | 25 |
| Diseño y criterio: decisiones justificadas, alternativas consideradas | 20 |
| Evaluación: evals o tests reproducibles con resultados | 20 |
| Seguridad y privacidad: riesgos identificados y mitigados | 15 |
| Costos y rendimiento: medidos y razonables | 10 |
| Documentación: otra persona puede entenderlo y ejecutarlo | 10 |

En los proyectos de Nivel 1 (P2), "Evaluación" se interpreta como verificación documentada de resultados y "Costos" como consumo y plan utilizado.
