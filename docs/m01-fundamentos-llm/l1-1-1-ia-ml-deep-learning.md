---
id: L1.1.1
titulo: "IA, ML, deep learning e IA generativa"
modulo: M1
unidad: U1.1
tipo: C
horas_estimadas: 1
costo: gratis
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/l1-1-1.md
---

# IA, ML, deep learning e IA generativa

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** definir inteligencia artificial, aprendizaje automático, deep learning e IA generativa; explicar cómo se relacionan; y elegir el enfoque adecuado para un problema.
> - **Necesitás:** el [Módulo 0](../m00-orientacion/index.md).
> - **Tiempo:** 1 hora (30 min de lectura y 30 de práctica) · **Costo:** gratis.

> [!WARNING]
> 📝 **Borrador.** Esta lección todavía no pasó la revisión final.

## Teoría

Estos cuatro términos se usan como sinónimos, pero no lo son: cada uno está contenido en el anterior.

```text
Inteligencia artificial
└── Aprendizaje automático (machine learning)
    └── Deep learning
        └── IA generativa actual (por ejemplo, los modelos de lenguaje)
```

Hubo modelos generativos antes del deep learning, pero los actuales se construyen con él.

### 1. Inteligencia artificial

La **inteligencia artificial (IA)** es el campo que busca que una computadora haga tareas que, en una persona, requieren inteligencia: razonar, reconocer, decidir, comunicarse.

No todo sistema de IA aprende. Un programa de ajedrez que evalúa jugadas con reglas escritas por personas, o un sistema que diagnostica fallas con cientos de reglas *si… entonces*, también son IA. El problema de este enfoque es que hay tareas cuyas reglas nadie sabe escribir: ¿qué regla distingue una foto de un gato de una de un perro?

### 2. Aprendizaje automático

El **aprendizaje automático** (*machine learning*, ML) es la parte de la IA en la que el sistema **aprende patrones a partir de ejemplos**, en lugar de seguir reglas escritas a mano.

Como persona que programa, pensalo así: en lugar de escribir la función, le das pares de entrada y salida, y el algoritmo ajusta una función que los reproduce y que funciona también con casos nuevos. Al resultado se lo llama **modelo**.

Tres formas principales de aprender:

| Tipo | Con qué aprende | Ejemplo |
|---|---|---|
| **Supervisado** | Ejemplos con la respuesta correcta | Correos marcados como *spam* o no, para clasificar los nuevos |
| **No supervisado** | Ejemplos sin respuesta: busca estructura | Agrupar clientes con hábitos de compra parecidos |
| **Por refuerzo** | Premios y castigos según sus acciones | Un programa que aprende a jugar probando y recibiendo puntos |

**Qué resuelve:** problemas donde las reglas son demasiadas o desconocidas, pero hay datos.

### 3. Deep learning

El **deep learning** (aprendizaje profundo) es la parte del ML que usa **redes neuronales con muchas capas**. Una red neuronal es una función con millones o miles de millones de valores ajustables (sus **parámetros**); "profunda" significa que procesa la información en muchas etapas sucesivas.

Su ventaja es que aprende directamente de datos crudos, como píxeles, audio o texto. En el **ML clásico** (el aprendizaje automático sin redes profundas, como los árboles de decisión o las regresiones), una persona tenía que decidir qué características medir (por ejemplo, "cantidad de palabras en mayúscula" para detectar *spam*); una red profunda descubre sola qué características importan.

**Qué resuelve:** percepción y lenguaje (imágenes, voz, texto), donde las características son difíciles de definir a mano. **Qué cuesta:** necesita muchos datos y mucha capacidad de cómputo.

### 4. IA generativa

La **IA generativa** son los modelos que **generan contenido nuevo** (texto, imágenes, audio, código) en lugar de devolver una etiqueta o un número.

| Un modelo que… | Responde | Ejemplo |
|---|---|---|
| **Clasifica o predice** | Una categoría o un valor | "Este correo es *spam*"; "esta casa vale tanto" |
| **Genera** | Contenido nuevo | Redactar la respuesta a un correo; crear una imagen desde una descripción |

Los **modelos de lenguaje** (LLM, por *Large Language Model*), que están detrás de ChatGPT, Claude o Gemini, son IA generativa de texto construida con deep learning. Por dentro también predicen: la palabra siguiente, una y otra vez (lo vas a ver en L1.1.3).

### 5. Elegir el enfoque

Que la IA generativa sea la más nueva no la hace la mejor para todo. Muchas veces la solución correcta es más simple:

| Si el problema… | Conviene | Por qué |
|---|---|---|
| Tiene reglas claras y estables | Código normal | Es predecible, barato y fácil de probar |
| Es predecir un valor o una categoría con datos en tablas | ML clásico | Suele ser más barato, rápido y explicable que un LLM |
| Es reconocer imágenes, voz o patrones complejos | Deep learning | Aprende características que no se pueden escribir a mano |
| Es redactar, resumir, traducir o conversar | IA generativa | Produce lenguaje nuevo y se adapta a pedidos distintos |

> [!TIP]
> **Errores frecuentes**
>
> - Usar "IA" como sinónimo de ChatGPT: la IA es un campo mucho más amplio.
> - Resolver con un LLM lo que resuelve una regla o un modelo de ML clásico: más caro, más lento y menos predecible.
> - Creer que un modelo "entiende" como una persona: aprende patrones estadísticos de sus datos.

## Práctica

Esta lección es conceptual: la práctica aplica la teoría a casos reales. Para cada caso, decidí qué enfoque usarías (código normal, ML clásico, deep learning o IA generativa) y justificalo en una línea.

1. Calcular el descuento de un pedido según reglas de la empresa (10% desde 100 dólares, 15% desde 500).
2. Estimar cuánto va a vender una sucursal el mes que viene, con el historial de ventas de los últimos tres años.
3. Detectar productos defectuosos en fotos de una línea de producción.
4. Responder consultas de clientes por chat, en lenguaje natural, a partir de la documentación de la empresa.
5. Agrupar a los usuarios de una aplicación según cómo la usan, sin categorías definidas de antemano.
6. Validar que un correo electrónico ingresado en un formulario tenga un formato correcto.

**Resultado esperado:** seis decisiones, cada una con su justificación. Comprobalas en las [soluciones de la práctica](soluciones/l1-1-1.md#práctica).

## Autoevaluación

Elegí una respuesta en cada pregunta. La página te corrige al instante y explica por qué. Para completar la lección necesitás 4 de 5 correctas.

```quiz
¿Cuál es la relación correcta entre estos términos?
- [ ] Son cuatro nombres para lo mismo
- [x] La IA generativa actual se construye con deep learning, que es parte del aprendizaje automático, que es parte de la IA
- [ ] El deep learning y la IA generativa son campos separados de la IA
> Cada término está contenido en el anterior: la IA es el campo más amplio y la IA generativa actual, construida con deep learning, el más específico.
```

```quiz
Un sistema de diagnóstico de fallas funciona con 300 reglas *si… entonces* escritas por expertos. ¿Es inteligencia artificial?
- [x] Sí: es IA, aunque no use aprendizaje automático
- [ ] No: si no aprende de datos, no es IA
- [ ] Solo si usa redes neuronales
> La IA incluye sistemas basados en reglas. El aprendizaje automático es solo una de sus formas.
```

```quiz
¿Qué diferencia al aprendizaje automático de la programación tradicional?
- [ ] Que no necesita computadoras potentes
- [x] Que el sistema aprende la relación entre entradas y salidas a partir de ejemplos, en lugar de que alguien escriba las reglas
- [ ] Que siempre da resultados exactos
> En ML no escribís la función: le das ejemplos y el algoritmo ajusta un modelo que los reproduce y generaliza a casos nuevos. Sus resultados son probables, no garantizados.
```

```quiz
¿Cuál es la principal ventaja del deep learning frente al ML clásico?
- [ ] Necesita menos datos
- [x] Aprende solo qué características importan, a partir de datos crudos como imágenes o texto
- [ ] Es más fácil de explicar
> En el ML clásico una persona define qué medir. Una red profunda descubre las características por sí misma, a cambio de necesitar más datos y cómputo, y de ser más difícil de explicar.
```

```quiz
Tenés que predecir si un cliente va a dejar de pagar su suscripción, con datos de uso y pagos en una tabla. ¿Qué conviene probar primero?
- [ ] Un LLM, porque es la tecnología más avanzada
- [x] Un modelo de ML clásico, porque es predecir una categoría con datos en tablas
- [ ] Reglas escritas a mano, porque son más baratas
> Es un problema de clasificación con datos estructurados: el ML clásico suele resolverlo mejor, más barato y de forma más explicable que un LLM. Las reglas a mano no captarían patrones que nadie conoce.
```

## Resumen

- **IA:** el campo amplio; incluye sistemas basados en reglas.
- **Aprendizaje automático:** aprende patrones de ejemplos en lugar de seguir reglas escritas (supervisado, no supervisado, por refuerzo).
- **Deep learning:** ML con redes neuronales de muchas capas; aprende de datos crudos, pero necesita muchos datos y cómputo.
- **IA generativa:** genera contenido nuevo; los LLM son IA generativa de texto.
- Elegí el enfoque más simple que resuelva el problema: no todo necesita un LLM.

## Para profundizar

- **L1.1.2** (para profundizar): redes neuronales, parámetros y entrenamiento.
- **L1.1.3:** qué es un modelo de lenguaje.
- **Términos nuevos en el [glosario](../glosario.md):** inteligencia artificial, aprendizaje automático, deep learning, IA generativa.
