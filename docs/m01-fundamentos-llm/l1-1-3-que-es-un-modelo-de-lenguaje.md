---
id: L1.1.3
titulo: "Qué es un modelo de lenguaje"
modulo: M1
unidad: U1.1
tipo: C
horas_estimadas: 1
costo: gratis
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/l1-1-3.md
---

# Qué es un modelo de lenguaje

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** explicar qué hace un modelo de lenguaje, cómo genera una respuesta y por qué una tarea tan simple produce comportamientos complejos; y deducir de eso consecuencias prácticas.
> - **Necesitás:** [L1.1.1](l1-1-1-ia-ml-deep-learning.md); Ollama con `llama3.2` ([L0.2.2](../m00-orientacion/l0-2-2-claves-y-modelo-local.md)) o cualquier asistente de IA.
> - **Tiempo:** 1 hora (30 min de lectura y 30 de práctica) · **Costo:** gratis.

> [!WARNING]
> 📝 **Borrador.** Esta lección todavía no pasó la revisión final.

## Teoría

### 1. Predecir lo que sigue

Un **modelo de lenguaje** hace una sola cosa: recibe un texto y calcula qué tan probable es cada posible continuación. Esas continuaciones son **tokens**: fragmentos de texto que pueden ser una palabra, una parte de una palabra o un signo (los vas a ver en detalle en L1.2.1).

Por ejemplo, para el texto *"El cielo de hoy está"*, un modelo podría calcular algo así (valores ilustrativos):

| Próximo token | Probabilidad |
|---|---:|
| nublado | 31% |
| despejado | 24% |
| gris | 12% |
| … (miles de opciones más) | … |

El modelo no busca la respuesta en ningún lado: produce estas probabilidades con sus **parámetros**, los miles de millones de valores que ajustó durante el entrenamiento.

### 2. Generar es repetir la predicción

Para escribir una respuesta, el modelo repite un ciclo:

1. Calcula las probabilidades del próximo token.
2. Elige uno.
3. Lo agrega al texto y vuelve al paso 1.

Así, token a token, hasta que elige un token especial de "fin" o llega a un límite. Por eso los asistentes muestran la respuesta de a poco: se está generando en ese momento.

En el paso 2 no siempre elige el más probable: suele elegir al azar, respetando las probabilidades. Por eso la misma pregunta puede dar respuestas distintas. Cómo se controla esa elección es el tema de L1.4.1.

### 3. Cómo aprende

El entrenamiento usa la misma tarea, a una escala enorme: con billones de tokens de libros, sitios web y código, se oculta el token siguiente y el modelo intenta predecirlo. Cada vez que se equivoca, sus parámetros se ajustan un poco para acertar mejor la próxima vez.

Una consecuencia importante: el modelo **no guarda los textos**, sino patrones de ellos, comprimidos en sus parámetros. Por eso puede producir datos falsos con total seguridad (las alucinaciones de [L0.1.2](../m00-orientacion/l0-1-2-aprender-en-un-campo-que-cambia.md)): genera lo que *suena* probable, no lo que verificó.

### 4. Por qué algo tan simple produce comportamientos complejos

Para predecir bien el próximo token en cualquier texto, el modelo tiene que captar mucho más que vocabulario:

| Para completar… | Necesita captar |
|---|---|
| "La capital de Francia es…" | Datos del mundo |
| "Si llueve, el piso se moja. Llovió toda la noche, entonces el piso…" | Patrones de razonamiento |
| `for (int i = 0; i <` | La estructura de un programa |
| "Estimado cliente: lamentamos informarle…" | Tono y propósito del texto |

Con suficientes parámetros y datos, aprender a predecir texto obliga a aprender todo eso. Por eso un modelo entrenado "solo" para completar texto puede traducir, resumir, programar o explicar. Si eso es *entender* como una persona es un debate abierto; en la práctica, sus capacidades son reales y sus errores también.

### 5. Modelo base y asistente

Un modelo recién entrenado así (un **modelo base**) solo continúa texto. Si le escribís *"¿Cuál es la capital de Francia?"*, puede continuar con otra pregunta, como si fuera parte de una lista de preguntas.

Los asistentes como ChatGPT, Claude o Gemini usan modelos con un **entrenamiento adicional** para seguir instrucciones y conversar (L1.3.2). Por dentro, siguen prediciendo el próximo token: la conversación es un texto que el modelo continúa.

### 6. Qué significa para vos

- **Lo que escribís cambia las probabilidades.** Un pedido claro y con contexto lleva a mejores continuaciones: es la base del Módulo 2.
- **Solo "sabe" lo que está en sus parámetros o en el texto que recibe.** Lo que no esté ahí, lo completa con lo que suena probable.
- **No hay una única respuesta.** La misma pregunta puede dar resultados distintos.

> [!TIP]
> **Errores frecuentes**
>
> - Pensar que el modelo busca las respuestas en una base de datos o en internet: las genera (salvo que la aplicación le agregue una búsqueda).
> - Concluir que, como "solo predice palabras", no puede hacer tareas complejas; o al revés, que como hace tareas complejas, nunca se equivoca.

## Práctica

Esta lección es conceptual: la práctica muestra en acción lo que leíste. Guardá tus respuestas donde quieras.

1. **Predecí vos.** Para cada texto, escribí tres continuaciones probables y cuál te parece la más probable:

    - "Me olvidé el paraguas y…"
    - "def sumar(a, b):"
    - "Según la RAE, la palabra…"

    **Resultado esperado:** tres listas. Fijate qué conocimiento usaste para cada una.

2. **Observá la variación.** Ejecutá tres veces la misma consulta y compará las respuestas:

    ```bash
    ollama run llama3.2 "Escribí una sola oración sobre el mar."
    ```

    **Resultado esperado:** tres oraciones distintas. Si usás un asistente, abrí una conversación nueva cada vez.

3. **Provocá una invención.** Preguntá por algo que no existe:

    ```bash
    ollama run llama3.2 "Resumí la novela 'El reloj de los navegantes', de Lisandra Quettier."
    ```

    **Resultado esperado:** muy probablemente, un resumen con argumento y personajes. La novela y la autora son inventadas para este ejercicio. Si el modelo responde que no la conoce, también es un buen resultado: anotalo.

Compará tus observaciones con las [soluciones de la práctica](soluciones/l1-1-3.md#práctica).

## Autoevaluación

Elegí una respuesta en cada pregunta. La página te corrige al instante y explica por qué. Para completar la lección necesitás 4 de 5 correctas.

```quiz
¿Qué hace, en esencia, un modelo de lenguaje?
- [ ] Busca en una base de datos la respuesta más parecida a la pregunta
- [x] Calcula qué tan probable es cada posible continuación de un texto
- [ ] Ejecuta reglas gramaticales escritas por lingüistas
> Todo lo que hace se apoya en predecir el próximo token. Las respuestas no se buscan: se generan a partir de los patrones guardados en sus parámetros.
```

```quiz
¿Por qué la misma pregunta puede dar respuestas distintas?
- [ ] Porque el modelo aprende de cada conversación y cambia
- [x] Porque al generar, el modelo suele elegir el próximo token al azar, respetando las probabilidades
- [ ] Porque los servidores tienen versiones distintas del modelo
> Elegir con algo de azar hace que el texto varíe entre ejecuciones. El modelo no se modifica al conversar: sus parámetros quedan fijos después del entrenamiento.
```

```quiz
Un modelo describe con detalle una novela que no existe. ¿Qué explica mejor ese comportamiento?
- [ ] El modelo encontró información falsa en internet
- [x] El modelo genera lo que suena probable según sus patrones, no lo que verificó
- [ ] Es un error de programación que se va a corregir en la próxima versión
> El modelo no guarda los textos sino patrones. Ante un título desconocido, completa con lo que sería una respuesta probable. Es una consecuencia de cómo funciona, no un error puntual.
```

```quiz
Si un modelo "solo predice el próximo token", ¿cómo puede escribir un programa que funciona?
- [ ] No puede: solo copia programas que vio durante el entrenamiento
- [x] Para predecir bien código, tuvo que captar la estructura y los patrones de los programas
- [ ] Porque tiene un compilador interno que prueba el código
> Predecir bien en textos tan variados obliga a aprender patrones profundos: gramática, datos, razonamiento y estructura de código. Igual puede equivocarse, por eso el código generado se prueba.
```

```quiz
Le escribís a un modelo base (sin entrenamiento de asistente) "¿Cuál es la capital de Francia?". ¿Qué puede pasar?
- [ ] Siempre responde "París", igual que un asistente
- [x] Puede continuar con otra pregunta, como si fuera parte de una lista
- [ ] Se niega a responder
> Un modelo base solo continúa texto. Seguir instrucciones requiere el entrenamiento adicional que tienen los asistentes.
```

## Resumen

- Un modelo de lenguaje calcula la probabilidad de cada posible próximo token.
- Genera repitiendo el ciclo: predecir, elegir, agregar. Elegir con algo de azar hace que las respuestas varíen.
- Aprende prediciendo el token siguiente en enormes cantidades de texto; guarda patrones, no textos. De ahí vienen las alucinaciones.
- Predecir bien obliga a captar datos, razonamiento y estructura: por eso puede hacer tareas complejas, y también equivocarse.
- Un modelo base continúa texto; un asistente tiene entrenamiento adicional para seguir instrucciones.

## Para profundizar

- **L1.2.1:** tokens y tokenización.
- **L1.3.2:** el entrenamiento que convierte un modelo base en asistente.
- **L1.4.1:** cómo se elige el próximo token (temperatura y muestreo).
- **Términos nuevos en el [glosario](../glosario.md):** modelo base.
