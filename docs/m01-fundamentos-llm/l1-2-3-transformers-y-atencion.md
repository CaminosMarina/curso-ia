---
id: L1.2.3
titulo: "Transformers y atención"
modulo: M1
unidad: U1.2
tipo: C
horas_estimadas: 1
costo: gratis
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/l1-2-3.md
---

# Transformers y atención

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** explicar qué hace el mecanismo de atención, por qué los transformers permitieron modelos tan grandes y qué es la ventana de contexto.
> - **Necesitás:** [L1.2.2](l1-2-2-embeddings.md); Ollama con `llama3.2` ([L0.2.2](../m00-orientacion/l0-2-2-claves-y-modelo-local.md)).
> - **Tiempo:** 1 hora (35 min de lectura y 25 de práctica) · **Costo:** gratis.

> [!WARNING]
> 📝 **Borrador.** Esta lección todavía no pasó la revisión final.

## Teoría

### 1. El problema: relacionar palabras lejanas

Para predecir bien el próximo token, el modelo tiene que saber a qué se refiere cada palabra. Compará:

- "El trofeo no entraba en la valija porque **era** muy grande." (*era* = el trofeo)
- "El trofeo no entraba en la valija porque **era** muy chica." (*era* = la valija)

Una sola palabra al final cambia a qué se refiere *era*. El modelo necesita relacionar palabras que pueden estar lejos entre sí, incluso a páginas de distancia.

Los modelos anteriores leían el texto palabra por palabra, llevando un "resumen" de lo leído. Eran lentos, porque no podían procesar varias palabras a la vez, y la información de lo que estaba lejos se iba perdiendo.

### 2. La atención

En 2017, investigadores de Google presentaron el **transformer**, una arquitectura basada en un mecanismo llamado **atención**. Es la base de todos los modelos de lenguaje actuales.

La idea: para interpretar cada token, el modelo **mira los tokens anteriores y decide cuánto importa cada uno**. Solo mira hacia atrás, porque al generar no puede ver lo que todavía no se escribió. En la primera oración, al llegar a *grande*, la atención podría repartirse así (valores ilustrativos):

| Token | Atención |
|---|---:|
| trofeo | alta |
| era | alta |
| valija | media |
| entraba | media |
| el, la, en | muy baja |

Con esa información, el vector de *grande* (ver [L1.2.2](l1-2-2-embeddings.md)) se ajusta para representar "el trofeo es grande": la pista que llega al final se resuelve mirando hacia atrás.

Un transformer repite esta operación en muchas **capas** sucesivas, y en cada una mira varias relaciones a la vez, como a qué se refiere un pronombre o la concordancia gramatical. Nadie programa qué mira: lo aprende durante el entrenamiento.

### 3. Por qué cambió todo

- **Procesa en paralelo:** durante el entrenamiento, todos los tokens se procesan a la vez. Eso permitió aprovechar muchos procesadores gráficos (GPU) y entrenar con cantidades enormes de texto.
- **Conecta directamente cada token con todos los anteriores:** el último token de un texto largo puede mirar el primero en un solo paso, sin depender de un resumen que se va degradando.

### 4. La ventana de contexto

La **ventana de contexto** es la cantidad máxima de tokens que el modelo puede considerar en una llamada: lo que le enviás **más** lo que responde. Lo que queda afuera, para el modelo, no existe.

¿Por qué hay un límite? Porque la atención compara cada token con todos los anteriores: si el texto se duplica, las comparaciones se multiplican por cuatro. Más contexto requiere mucha más memoria y cálculo.

En un chat, la ventana incluye las instrucciones de la aplicación, el historial de la conversación, los archivos adjuntos y la respuesta. Por eso, en una conversación muy larga, la aplicación tiene que descartar o resumir partes viejas.

### 5. Qué significa para vos

- **Si no está en la ventana, el modelo no lo sabe.** No recuerda conversaciones anteriores salvo que la aplicación las vuelva a incluir.
- **Más contexto, más costo y más espera:** cada token de entrada se paga y se procesa.
- **Que entre no significa que lo use bien.** Con contextos muy largos, los modelos aprovechan peor la información del medio (L1.4.2).

> [!NOTE]
> **Específico de herramienta** · verificado el 2026-10-24 · fuente: [Ollama: context length](https://github.com/ollama/ollama/blob/main/docs/context-length.mdx)
>
> - El tamaño de la ventana varía mucho entre modelos y aumenta con cada generación: consultalo en la documentación de cada uno.
> - Ollama usa por defecto una ventana de 4k (4.096 tokens) en computadoras con menos de 24 GB de memoria de video, aunque el modelo admita más. Se puede ampliar en su configuración, a cambio de más memoria. `ollama ps` muestra la ventana asignada en la columna `CONTEXT`.

> [!TIP]
> **Errores frecuentes**
>
> - Olvidar que la respuesta también ocupa lugar en la ventana.

## Práctica

Esta lección es conceptual: la práctica aplica la teoría. Guardá tus respuestas donde quieras.

1. **Resolvé referencias.** Para cada oración, indicá a quién se refiere *ella* y qué palabra te lo indicó:

    - "Ana le prestó el libro a Laura porque **ella** lo necesitaba para un examen."
    - "Ana le prestó el libro a Laura porque **ella** ya lo había terminado."

    **Resultado esperado:** dos respuestas distintas. La palabra que te dio la pista es la que el modelo tendría que "atender" más.

2. **Calculá si entra en la ventana.** Un modelo ficticio tiene una ventana de 128.000 tokens. Querés enviarle instrucciones (2.000 tokens), tres documentos de 30.000 tokens cada uno y el historial de la conversación (10.000 tokens), y reservar 4.000 tokens para la respuesta.

    - ¿Entra todo?
    - ¿Y si agregás un cuarto documento de 30.000 tokens?

    **Resultado esperado:** dos respuestas con la cuenta.

3. **Mirá la ventana de tu modelo local.** Ejecutá una consulta para que el modelo quede cargado y, enseguida, `ollama ps`:

    ```bash
    ollama run llama3.2 "Hola"
    ollama ps
    ```

    **Resultado esperado:** una fila con `llama3.2` y, en la columna `CONTEXT`, la ventana asignada. Anotá el número y calculá cuántas páginas de texto entrarían, a unos 500 tokens por página.

Comprobá tus respuestas en las [soluciones de la práctica](soluciones/l1-2-3.md#práctica).

## Autoevaluación

Elegí una respuesta en cada pregunta. La página te corrige al instante y explica por qué. Para completar la lección necesitás 4 de 5 correctas.

```quiz
¿Qué hace el mecanismo de atención?
- [ ] Hace que el modelo lea más despacio para no equivocarse
- [x] Para interpretar cada token, pondera cuánto importa cada uno de los tokens anteriores
- [ ] Elimina las palabras poco importantes antes de procesar el texto
> La atención no descarta palabras: decide cuánto peso darle a cada una para interpretar cada token. Así, al llegar a *grande* o a *chica*, el modelo relaciona la oración con *trofeo* o con *valija*.
```

```quiz
¿Por qué el transformer permitió entrenar modelos mucho más grandes que los anteriores?
- [ ] Porque usa menos datos
- [x] Porque procesa todos los tokens en paralelo, lo que permite aprovechar muchas GPU
- [ ] Porque no necesita entrenamiento
> Los modelos anteriores procesaban palabra por palabra. El transformer procesa los tokens a la vez durante el entrenamiento, y eso permitió escalar a cantidades enormes de texto.
```

```quiz
¿Qué incluye la ventana de contexto en una llamada a un modelo?
- [ ] Solo la pregunta del usuario
- [ ] Todo lo que el modelo leyó durante el entrenamiento
- [x] Todo lo que se le envía (instrucciones, historial, archivos) más la respuesta que genera
> La ventana es el texto que el modelo considera en esa llamada, incluida su propia respuesta. Lo aprendido en el entrenamiento está en sus parámetros, no en la ventana.
```

```quiz
¿Por qué existe un límite de ventana de contexto?
- [ ] Por una decisión comercial de los proveedores
- [x] Porque la atención compara cada token con todos los anteriores, y el cálculo y la memoria crecen muy rápido con la longitud
- [ ] Porque los tokenizadores no admiten textos largos
> Si el texto se duplica, las comparaciones se multiplican por cuatro. Por eso ampliar la ventana requiere mucha más memoria, como se ve en la configuración de Ollama.
```

```quiz
Después de una conversación muy larga, el asistente "olvida" algo que le dijiste al principio. ¿Qué es lo más probable?
- [ ] El modelo se cansó
- [x] Esa parte quedó fuera de la ventana de contexto, o la aplicación la resumió para que entrara
- [ ] El modelo borró ese dato de sus parámetros
> El modelo solo considera lo que está en la ventana. Cuando la conversación no entra, la aplicación descarta o resume partes viejas. Sus parámetros no cambian al conversar.
```

## Resumen

- Para predecir bien, el modelo tiene que relacionar palabras que pueden estar lejos entre sí.
- La **atención** permite que cada token pondere cuánto importa cada uno de los anteriores; el **transformer** apila muchas capas de atención.
- El transformer procesa en paralelo: eso permitió entrenar modelos enormes.
- La **ventana de contexto** es el máximo de tokens por llamada, entrada más salida. Lo que queda afuera no existe para el modelo.
- El límite existe porque el costo de la atención crece muy rápido con la longitud.

## Para profundizar

- **L1.4.2:** la ventana de contexto en la práctica y el efecto "perdido en el medio".
- **Módulo 7:** cómo decidir qué entra en la ventana (Context Engineering).
- **Términos nuevos en el [glosario](../glosario.md):** transformer, atención.
