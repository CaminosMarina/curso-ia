---
id: L1.2.2
titulo: "Embeddings"
modulo: M1
unidad: U1.2
tipo: M
horas_estimadas: 1.5
costo: gratis
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/l1-2-2.md
---

# Embeddings

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** explicar qué es un embedding, medir qué tan parecidos son dos textos y usar embeddings para buscar por significado.
> - **Necesitás:** [L1.2.1](l1-2-1-tokens-y-tokenizacion.md); Ollama ([L0.2.2](../m00-orientacion/l0-2-2-claves-y-modelo-local.md)) y tu repositorio de trabajo con `uv`.
> - **Tiempo:** 1 hora y media (30 min de lectura y 1 h de práctica) · **Costo:** gratis.

> [!WARNING]
> 📝 **Borrador.** Esta lección todavía no pasó la revisión final.

## Teoría

### 1. Qué es un embedding

Un **embedding** es una lista de números (un **vector**) que representa el significado de un contenido. Lo produce un **modelo de embeddings**: le das un texto y te devuelve un vector, siempre del mismo largo.

La propiedad clave: **textos de significado parecido dan vectores cercanos**, aunque usen palabras distintas. "¿Cómo cambio mi clave?" y "Quiero restablecer la contraseña" quedan cerca; "Los envíos tardan tres días" queda lejos de los dos.

Pensalo como un mapa. En un mapa, dos números (latitud y longitud) ubican una ciudad, y las ciudades cercanas tienen números parecidos. Un embedding hace lo mismo con el significado, pero con cientos de números en lugar de dos.

### 2. Cómo se mide el parecido

La medida más usada es la **similitud coseno**: compara hacia dónde apuntan dos vectores.

- Cerca de **1**: significado muy parecido.
- Cerca de **0**: sin relación.

Se calcula con una fórmula corta sobre los números de los dos vectores; el código está en la práctica.

No hay un valor universal que separe "parecido" de "distinto": depende del modelo. Lo útil es **comparar**: qué texto está más cerca de otro.

### 3. Para qué sirven

| Uso | Ejemplo |
|---|---|
| **Búsqueda semántica** | Encontrar el artículo de ayuda que responde una pregunta, aunque no comparta palabras con ella |
| **Agrupar** | Juntar comentarios de clientes que hablan del mismo problema |
| **Detectar duplicados** | Encontrar consultas repetidas escritas de forma distinta |
| **Recomendar** | Sugerir contenidos parecidos a los que alguien leyó |

La búsqueda semántica es la base de **RAG**, la técnica para que un modelo responda con tus propios documentos: se verá a fondo en el Módulo 8.

### 4. Embeddings y modelos de lenguaje

Por dentro, un modelo de lenguaje también convierte cada token en un vector. Pero son herramientas distintas:

| | Modelo de lenguaje | Modelo de embeddings |
|---|---|---|
| **Recibe** | Texto | Texto |
| **Devuelve** | Texto nuevo, token a token | Un vector por texto |
| **Sirve para** | Responder, redactar, resumir | Comparar, buscar, agrupar |

Los modelos de embeddings son más chicos, rápidos y baratos que un modelo de lenguaje.

### 5. Dos reglas

- **Usá el mismo modelo para todo.** Los vectores de modelos distintos no se pueden comparar entre sí: si guardás tus documentos con un modelo, las preguntas también tienen que pasar por ese modelo.
- **Probá con tus datos.** La calidad depende del modelo, del idioma y del tema. Antes de elegir uno, medí cómo ordena ejemplos reales.

> [!NOTE]
> **Específico de herramienta** · verificado el 2026-10-24 · fuente: [Ollama: embeddings](https://github.com/ollama/ollama/blob/main/docs/capabilities/embeddings.mdx)
>
> - La documentación de Ollama usa el modelo `embeddinggemma` y la función `ollama.embed`. El largo del vector depende del modelo; según esa documentación, suele estar entre 384 y 1024 números.

> [!TIP]
> **Errores frecuentes**
>
> - Fijar un umbral de similitud (por ejemplo, "más de 0,8 es igual") sin probarlo con el modelo que usás.
> - Usar un modelo de lenguaje para buscar en muchos documentos, cuando un modelo de embeddings lo hace más rápido y barato.

## Práctica

### Práctica guiada

1. **Descargá el modelo de embeddings y creá el proyecto.** Desde la raíz de tu repositorio de trabajo:

    ```bash
    ollama pull embeddinggemma
    uv init --vcs none practicas/m01-embeddings
    cd practicas/m01-embeddings
    uv add ollama
    ```

2. **Generá un embedding.** Creá `vector.py`:

    ```python
    import ollama

    respuesta = ollama.embed(model="embeddinggemma", input="¿Cómo cambio mi clave?")
    vector = respuesta["embeddings"][0]
    print("Largo del vector:", len(vector))
    print("Primeros 5 números:", vector[:5])
    ```

    Ejecutalo con `uv run vector.py`.

    **Resultado esperado:** el largo del vector (cientos de números) y los primeros cinco, que por sí solos no significan nada para una persona.

3. **Buscá por significado.** Creá `buscar.py`:

    ```python
    import math
    import ollama

    def similitud_coseno(a, b):
        producto = sum(x * y for x, y in zip(a, b))
        largo_a = math.sqrt(sum(x * x for x in a))
        largo_b = math.sqrt(sum(y * y for y in b))
        return producto / (largo_a * largo_b)

    documentos = [
        "Para restablecer tu contraseña, entrá a Configuración y elegí 'Olvidé mi contraseña'.",
        "Nuestro horario de atención es de lunes a viernes, de 9 a 18.",
        "Los envíos tardan entre 3 y 5 días hábiles.",
        "Podés pagar con tarjeta de crédito, débito o transferencia.",
    ]
    pregunta = "¿Cómo cambio mi clave?"

    vectores = ollama.embed(model="embeddinggemma", input=documentos)["embeddings"]
    vector_pregunta = ollama.embed(model="embeddinggemma", input=pregunta)["embeddings"][0]

    resultados = [(similitud_coseno(vector_pregunta, v), d) for v, d in zip(vectores, documentos)]
    for puntaje, documento in sorted(resultados, reverse=True):
        print(f"{puntaje:.3f}  {documento}")
    ```

    Ejecutalo con `uv run buscar.py`.

    **Resultado esperado:** los cuatro documentos ordenados por similitud. El primero tendría que ser el de la contraseña, aunque la pregunta dice "clave" y no "contraseña".

### Ejercicio

**Objetivo:** comprobar qué capta y qué no capta la búsqueda por significado.

1. En `buscar.py`, probá tres preguntas nuevas, una por vez: una que corresponda claramente a uno de los documentos, una que no corresponda a ninguno (por ejemplo, "¿Venden bicicletas?") y una en inglés que signifique lo mismo que la pregunta original.
2. Para cada una, anotá qué documento quedó primero y con qué puntaje.

**Criterios de aceptación:**

- [ ] Anotaste el documento ganador y el puntaje de las tres preguntas.
- [ ] Explicaste qué pasó con la pregunta que no corresponde a ningún documento.
- [ ] El proyecto `practicas/m01-embeddings` está en un *commit*.

Comprobá tus resultados en las [soluciones de la práctica](soluciones/l1-2-2.md#práctica).

## Autoevaluación

Elegí una respuesta en cada pregunta. La página te corrige al instante y explica por qué. Para completar la lección necesitás 4 de 5 correctas, además del ejercicio.

```quiz
¿Qué es un embedding?
- [ ] Un resumen corto de un texto
- [x] Un vector de números que representa el significado de un contenido
- [ ] La lista de tokens de un texto
> Un modelo de embeddings convierte un texto en un vector. Los textos de significado parecido dan vectores cercanos.
```

```quiz
"¿Cómo cambio mi clave?" y "Quiero restablecer la contraseña" no comparten casi ninguna palabra. ¿Qué pasa con sus embeddings?
- [x] Quedan cerca, porque significan algo parecido
- [ ] Quedan lejos, porque usan palabras distintas
- [ ] No se pueden comparar porque tienen largos distintos
> Los embeddings representan significado, no palabras. Además, un mismo modelo devuelve siempre vectores del mismo largo.
```

```quiz
La similitud coseno entre dos textos da 0,92 y entre otros dos da 0,15. ¿Qué podés concluir?
- [ ] Que el primer par es igual y el segundo, opuesto
- [x] Que el primer par es mucho más parecido en significado que el segundo
- [ ] Nada, porque la similitud coseno solo sirve para números
> Cuanto más cerca de 1, más parecido. Lo valioso es la comparación entre pares; el límite exacto entre "parecido" y "distinto" depende del modelo.
```

```quiz
Guardaste los embeddings de tus documentos con un modelo y ahora querés buscar con otro modelo más nuevo. ¿Qué hacés?
- [ ] Busco directamente: los vectores son compatibles
- [x] Genero de nuevo los embeddings de todos los documentos con el modelo nuevo
- [ ] Uso el modelo nuevo solo para las preguntas
> Cada modelo ubica los significados de forma distinta: sus vectores no se pueden comparar con los de otro modelo. Documentos y preguntas tienen que usar el mismo.
```

```quiz
Tenés que encontrar, entre 50.000 artículos de ayuda, los cinco más relacionados con una pregunta. ¿Qué conviene?
- [ ] Pasarle los 50.000 artículos a un modelo de lenguaje y pedirle que elija
- [x] Comparar el embedding de la pregunta con los embeddings de los artículos
- [ ] Buscar las palabras exactas de la pregunta
> Los embeddings se calculan una vez por artículo y comparar vectores es rápido y barato. La búsqueda por palabras exactas pierde los sinónimos.
```

## Resumen

- Un **embedding** es un vector que representa el significado de un contenido; textos parecidos dan vectores cercanos.
- La **similitud coseno** mide el parecido: cerca de 1, muy parecido; cerca de 0, sin relación. Lo útil es comparar.
- Sirven para búsqueda semántica, agrupar, detectar duplicados y recomendar; la búsqueda semántica es la base de RAG (Módulo 8).
- Un modelo de embeddings devuelve vectores, no texto, y es más chico y barato que un modelo de lenguaje.
- Usá el mismo modelo para documentos y preguntas, y probalo con tus datos.

## Para profundizar

- **L1.2.3:** transformers y atención.
- **Módulo 8:** embeddings, búsqueda semántica y RAG en profundidad.
- **Términos nuevos en el [glosario](../glosario.md):** similitud coseno, búsqueda semántica.
