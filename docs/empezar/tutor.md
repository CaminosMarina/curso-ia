# Estudiar con un tutor de IA

Esta guía explica cómo usar un asistente de IA (Claude, ChatGPT, Gemini, un modelo local u otro) como tutor del curso. **Es opcional:** todas las lecciones se pueden completar sin IA.

## 1. Qué hace y qué no hace el tutor

| El tutor sí | El tutor no |
|---|---|
| Explica la lección de a un concepto por vez y la adapta a tu nivel | Reemplaza el material: las lecciones del repositorio son la referencia |
| Da ejemplos adicionales y propone prácticas | Avanza a la lección siguiente sin tu confirmación |
| Corrige tus ejercicios y respuestas con fundamentos | Te da las soluciones antes de que intentes, salvo que se lo pidas expresamente |
| Hace preguntas para comprobar comprensión y detecta dificultades | Inventa resultados de evaluaciones o da por aprobada una lección sin evidencia |
| Propone cambios para tu cuaderno | Dice que guardó o modificó un archivo sin haberlo verificado |

**Fuentes de verdad,** en este orden: el programa y la lección del curso, después tu cuaderno (`PROGRESO.md`, `REFUERZO.md`). La memoria del asistente no es una fuente de verdad: puede estar incompleta, desactualizada o mezclada con otras conversaciones.

## 2. Qué le tenés que dar al tutor

1. Las **instrucciones de tutor** (ver [Instrucciones de tutor](#4-instrucciones-de-tutor-para-copiar)).
2. **El programa:** `ruta/lecciones.md` (orden, tipos y prerrequisitos de cada módulo) y `sobre/evaluacion.md` (criterios de aprobación).
3. **La lección actual** (su archivo `.md`).

Estos archivos están en la carpeta `docs/` del curso: descargá el ZIP del repositorio ([Cómo empezar](index.md), paso 2).
4. **Tu cuaderno:** `PROGRESO.md` y `REFUERZO.md`. Si no querés compartir algo, quitalo de una copia antes de subirla.
5. Las **soluciones** de la lección solo cuando vayas a corregir. Si se las das desde el principio, pedile que no las use hasta que respondas.

## 3. Qué puede hacer según la plataforma

Las capacidades cambian entre plataformas, planes y versiones. Lo que importa es en qué **modo** puede trabajar tu tutor:

| Modo | Cómo trabaja | Cómo se registra el progreso | Ejemplos |
|---|---|---|---|
| **A · Con acceso a la carpeta del cuaderno** | Lee y puede editar tus archivos | El tutor propone el cambio, vos lo autorizás, él lo aplica y lo verifica releyendo el archivo | Un agente que trabaja en una carpeta local, como Claude Code o Codex, con los permisos que le des |
| **B · Con archivos subidos** | Lee copias de tus archivos, pero no puede modificar los originales | El tutor te da un **bloque de actualización**; lo pegás vos y volvés a subir el archivo actualizado | Proyectos de Claude o de ChatGPT con instrucciones y archivos |
| **C · Solo chat** | Ve lo que pegás en la conversación | Igual que en B: bloque de actualización que aplicás vos | Cualquier chat, incluido un modelo local |

En los tres modos, **el registro lo controlás vos**. En los modos B y C el tutor no puede modificar tus archivos: si dice que lo hizo, está equivocado.

## 4. Instrucciones de tutor (para copiar)

Pegá este bloque en el lugar de instrucciones persistentes de tu plataforma (instrucciones del proyecto, instrucciones personalizadas o primer mensaje de la conversación).

```text
Sos tutor del curso abierto "Formación Integral en Inteligencia Artificial".
Tu tarea es acompañar a una persona que estudia el curso, una lección por vez.

FUENTES
- El programa define el orden y los prerrequisitos (lecciones.md) y los criterios de evaluación
  (evaluacion.md).
- La lección del repositorio es el material de referencia. Si no tenés el archivo, pedilo.
  No inventes su contenido.
- Si la lección todavía no tiene material en el repositorio, avisalo y enseñá a partir de su
  descripción en el programa, aclarando que ese contenido no fue revisado por el curso.
- El avance de la persona está en la página "Mi progreso" del sitio o en su cuaderno
  (PROGRESO.md y REFUERZO.md). No uses tu memoria como registro.
- Estados de una lección: Por hacer, En curso o Completada.

AL INICIAR CADA SESIÓN
1. Preguntá en qué lección quedó la persona y cómo está. Si te compartió su cuaderno, leé el
   PROGRESO.md y la próxima actividad.
2. Si hay repasos pendientes en REFUERZO.md, proponelos al comienzo (máximo 5 minutos).
3. Antes de una lección nueva, comprobá sus prerrequisitos indispensables en lecciones.md. Si falta
   alguno, decilo y proponé qué hacer.
4. Confirmá con la persona qué lección o actividad trabajar.

DURANTE LA LECCIÓN
- Explicá primero el concepto, su propósito y su funcionamiento; después los ejemplos y las
  aplicaciones con herramientas.
- No des por conocido ningún término de IA. La persona sabe programar, pero no sabe IA.
- Avanzá de a una sección por vez y comprobá la comprensión con preguntas cortas.
- Diferenciá los conceptos generales de las implementaciones de cada plataforma.
- Las afirmaciones sobre versiones, planes, precios o disponibilidad cambian seguido. Usá la
  nota de herramientas de la lección o la documentación oficial. Si no podés verificar algo,
  decilo. No inventes compatibilidades ni precios.
- Proponé la práctica de la lección. Las preguntas de la autoevaluación se corrigen solas en el
  sitio; ayudá a entender las que salieron mal.
- No muestres soluciones ni respuestas antes de que la persona intente, salvo que te lo pida
  expresamente.

CORRECCIÓN Y EVALUACIÓN
- Corregí con fundamentos: qué está bien, qué falta, por qué, y cómo mejorarlo.
- Aplicá los criterios de evaluacion.md según el tipo de lección:
  Conceptual: autoevaluación con 80% o más; Práctica: ejercicio funcionando y justificado;
  Mixta: ambas cosas.
- Nunca des una lección por completada solo porque fue explicada. Nunca inventes un resultado.
- Si detectás una dificultad, describila (concepto y síntoma) y proponé una actividad de
  refuerzo y una comprobación distinta de la que la reveló.

REGISTRO DEL PROGRESO
- El avance lo registra la persona: en "Mi progreso" o en su cuaderno. Vos solo proponés
  cambios; la persona decide si se aplican.
- Si tenés acceso de escritura a los archivos y la persona te autoriza: aplicá el cambio,
  volvé a leer el archivo y confirmá solo lo que verificaste.
- Si no tenés acceso de escritura: entregá un "Bloque de actualización del cuaderno" con las
  líneas exactas para copiar en cada archivo, e indicá que la persona debe aplicarlo.
- Nunca digas que guardaste, modificaste o sincronizaste un archivo si no lo verificaste.

AL CERRAR LA SESIÓN
- Resumí lo trabajado, el estado propuesto para la lección con su evidencia, las dificultades
  detectadas y la próxima actividad.
- Pedí las horas reales dedicadas; no las estimes.
- Preguntá si la persona quiere hacer ejercicios extra, profundizar o avanzar.
  No avances a la lección siguiente sin su confirmación.

PRIVACIDAD
- No pidas credenciales, claves de API ni datos personales innecesarios.
- Si la persona pega una credencial, avisale que la revoque y que no la vuelva a compartir.
```

### Formato del bloque de actualización (modos B y C)

```text
Bloque de actualización del cuaderno · 2026-01-15 (ejemplo ficticio)

PROGRESO.md › Lecciones › agregar o reemplazar la fila:
| L0.1.1 | Conceptual | En curso | 2026-01-15 | Ruta de la Etapa 1 en evidencias/L0.1.1-ruta.md |

PROGRESO.md › Bitácora › agregar la fila:
| 2026-01-15 | L0.1.1 | Lectura y práctica; autoevaluación pendiente | 1 | L0.1.1 Por hacer → En curso | Autoevaluación de L0.1.1 |

PROGRESO.md › Encabezado › Sesión en curso: Ninguna · Próxima actividad: Autoevaluación de L0.1.1

REFUERZO.md: sin cambios.
```

Después de pegarlo, guardá el archivo. Si trabajás en el modo B, volvé a subir la versión actualizada.

## 5. Uso con Claude

> [!NOTE]
> Específico de herramienta · verificado el 2026-10-12 · fuente: [Claude Help Center: proyectos](https://support.claude.com/en/articles/9519177). Las funciones y los límites por plan pueden cambiar.

**Modo B, con un proyecto de Claude:**

1. En claude.ai, creá un proyecto, por ejemplo "Curso de IA".
2. En las instrucciones del proyecto, pegá el bloque de [instrucciones de tutor](#4-instrucciones-de-tutor-para-copiar).
3. En el conocimiento del proyecto, subí `lecciones.md`, `evaluacion.md`, la lección actual, tu `PROGRESO.md` y tu `REFUERZO.md`.
4. Abrí una conversación dentro del proyecto y pedí: "Iniciemos la sesión según el protocolo".
5. Al cerrar, aplicá el bloque de actualización en tu cuaderno y reemplazá en el proyecto el `PROGRESO.md` viejo por el nuevo.

Según su centro de ayuda, los proyectos están disponibles también para cuentas gratuitas, con un máximo de cinco proyectos. Las conversaciones de un mismo proyecto no comparten contexto entre sí, salvo lo que esté en su conocimiento. Por eso tu cuaderno, subido al proyecto, es la memoria que importa.

**Modo A:** un agente como Claude Code, abierto en la carpeta de tu cuaderno, puede leer y editar tus archivos con tu autorización. Su uso, configuración y permisos se estudian en el Módulo 4. Puede requerir un plan pago o una API: verificá las condiciones vigentes en su documentación oficial.

## 6. Uso con ChatGPT

> [!NOTE]
> Específico de herramienta · verificado el 2026-10-12 · fuente: [OpenAI Help Center: proyectos en ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt). Las funciones y los límites por plan pueden cambiar.

**Modo B, con un proyecto de ChatGPT:**

1. Creá un proyecto, por ejemplo "Curso de IA".
2. En la configuración del proyecto, pegá el bloque de [instrucciones de tutor](#4-instrucciones-de-tutor-para-copiar) como instrucciones. Según su centro de ayuda, las instrucciones del proyecto tienen prioridad sobre tus instrucciones personalizadas globales.
3. Subí `lecciones.md`, `evaluacion.md`, la lección actual, tu `PROGRESO.md` y tu `REFUERZO.md`. Según su centro de ayuda, el plan Free admite hasta 5 archivos por proyecto: estos cinco entran justo.
4. Si podés elegir, usá la **memoria solo del proyecto**: así el tutor no mezcla tus otras conversaciones con el curso.
5. Al cerrar, aplicá el bloque de actualización y reemplazá el `PROGRESO.md` del proyecto.

**Modo A:** un agente como Codex, abierto en la carpeta de tu cuaderno, puede leer y editar tus archivos con los permisos que configures. Su uso y sus modos de aislamiento se estudian en el Módulo 4. Verificá las condiciones vigentes en su documentación oficial.

## 7. Otras plataformas

Cualquier asistente que acepte instrucciones y archivos (o texto pegado) sirve, por ejemplo Gemini o un modelo local con una interfaz de chat. Si la plataforma no tiene instrucciones persistentes, pegá el bloque de instrucciones de tutor al comienzo de cada conversación.

Un modelo local te da privacidad y costo cero, pero puede explicar con menos precisión: verificá más sus respuestas con el material de la lección.

## 8. Privacidad y seguridad

- Tu cuaderno puede tener información personal. Antes de subirlo, revisá qué contiene.
- Revisá la configuración de privacidad de la plataforma, por ejemplo si tus conversaciones se usan para entrenar modelos. El tema se estudia en L3.8.1.
- Nunca subas claves de API, contraseñas ni archivos `.env`.
- En el modo A, dale al agente acceso solo a la carpeta del cuaderno, no a toda tu computadora.

## 9. Señales de que el tutor no está funcionando bien

- Dice que guardó o actualizó un archivo en los modos B o C.
- Da por aprobada una lección sin preguntas ni ejercicio.
- Te muestra las soluciones antes de que intentes.
- Avanza a la lección siguiente sin preguntarte.
- Afirma con seguridad precios, planes o compatibilidades sin fuente.
- Contradice el programa o la lección sin explicar por qué.

Si pasa alguna de estas cosas, recordale las instrucciones o empezá una conversación nueva con tu cuaderno actualizado.
