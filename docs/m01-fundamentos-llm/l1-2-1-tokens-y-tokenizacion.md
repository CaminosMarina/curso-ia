---
id: L1.2.1
titulo: "Tokens y tokenización"
modulo: M1
unidad: U1.2
tipo: M
horas_estimadas: 1.5
costo: gratis
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/l1-2-1.md
---

# Tokens y tokenización

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** explicar qué es un token, contar tokens con código y estimar cómo afectan el idioma y las imágenes al costo.
> - **Necesitás:** [L1.1.3](l1-1-3-que-es-un-modelo-de-lenguaje.md); tu repositorio de trabajo con `uv` y la clave de Gemini del [Módulo 0](../m00-orientacion/l0-2-2-claves-y-modelo-local.md).
> - **Tiempo:** 1 hora y media (30 min de lectura y 1 h de práctica) · **Costo:** gratis.

> [!WARNING]
> 📝 **Borrador.** Esta lección todavía no pasó la revisión final.

## Teoría

### 1. Por qué tokens

Un modelo no procesa letras ni palabras: procesa **tokens**, fragmentos de texto que tienen un número dentro de un vocabulario fijo. El texto se convierte en una lista de números, el modelo trabaja con ellos y su respuesta se vuelve a convertir en texto. El programa que hace esa conversión es el **tokenizador**.

¿Por qué no usar letras o palabras?

- **Letras:** el vocabulario sería mínimo, pero cada texto sería una secuencia larguísima, más lenta y cara de procesar.
- **Palabras:** las secuencias serían cortas, pero el vocabulario no tendría fin: nombres propios, palabras nuevas, errores de tipeo.

Los tokens son el punto medio: un vocabulario de decenas o cientos de miles de fragmentos con los que se puede escribir cualquier texto.

### 2. Cómo se arma el vocabulario: BPE

La técnica más usada se llama **BPE** (*Byte Pair Encoding*). Funciona así:

1. Se empieza con los caracteres (en realidad, los bytes) como vocabulario.
2. En un gran conjunto de textos, se busca el par de símbolos vecinos más frecuente (por ejemplo, `e` + `n`) y se agrega al vocabulario como un símbolo nuevo (`en`).
3. Se repite, uniendo pares cada vez más largos (`en` + `tre` → `entre`), hasta llegar al tamaño de vocabulario buscado.

El resultado: las palabras frecuentes quedan como un solo token, y las raras se arman con varios. Como el punto de partida son los bytes, cualquier texto se puede representar, aunque tenga palabras que el tokenizador nunca vio.

### 3. Idiomas, números y código

El vocabulario depende de los textos con los que se armó, y en esos textos suele predominar el inglés. Por eso:

- **El mismo contenido en español suele ocupar más tokens que en inglés:** más palabras se parten en varios fragmentos. Más tokens es más costo y menos espacio libre en lo que el modelo puede recibir.
- **Los números y las palabras poco comunes se cortan en pedazos arbitrarios.** Por eso un modelo puede fallar en tareas que a una persona le parecen triviales, como contar las letras de una palabra: no ve letras, ve tokens.

### 4. Cada modelo tiene su tokenizador

Cada proveedor arma su propio vocabulario, así que el mismo texto da cantidades distintas de tokens en GPT, Claude o Gemini. Como referencia, en inglés un token equivale a unos 4 caracteres. Para un número exacto, usá el contador del proveedor.

### 5. Imágenes y otros formatos

Las imágenes también se convierten en tokens: el modelo las divide en cuadrados pequeños, y cuanto más resolución, más tokens. Con el audio, el video y los PDF pasa algo parecido. Si no necesitás detalle fino, reducir la resolución de una imagen antes de enviarla baja el costo.

### 6. Por qué importa

| Aspecto | Qué tienen que ver los tokens |
|---|---|
| **Costo** | Las API cobran por millón de tokens, con un precio para los de entrada y otro, en general más alto, para los de salida |
| **Límites** | La ventana de contexto y el máximo de respuesta se miden en tokens (L1.4.2) |
| **Velocidad** | La respuesta se genera token a token: más tokens de salida, más espera |

> [!NOTE]
> **Específico de herramienta** · verificado el 2026-10-24 · fuentes: [tiktoken](https://github.com/openai/tiktoken) · [Claude: visión](https://platform.claude.com/docs/en/build-with-claude/vision) · [Gemini: contar tokens](https://ai.google.dev/gemini-api/docs/interactions/tokens)
>
> - **OpenAI:** `tiktoken` es su tokenizador de código abierto. La codificación `o200k_base` es la de GPT-4o y los modelos posteriores.
> - **Claude:** divide las imágenes en cuadrados de 28 × 28 píxeles. Una imagen cuesta ⌈ancho / 28⌉ × ⌈alto / 28⌉ tokens: 1000 × 1000 píxeles son 1.296 tokens. Las imágenes muy grandes se reducen antes de procesarse.
> - **Gemini:** una imagen de hasta 384 píxeles por lado cuesta 258 tokens; las más grandes, 258 por cada bloque de 768 × 768. Su API incluye una función para contar tokens.

> [!TIP]
> **Errores frecuentes**
>
> - Calcular costos con palabras en lugar de tokens.
> - Usar el contador de un proveedor para estimar el costo de otro.

## Práctica

### Práctica guiada

1. **Creá el proyecto.** Desde la raíz de tu repositorio de trabajo:

    ```bash
    uv init --vcs none practicas/m01-tokens
    cd practicas/m01-tokens
    uv add tiktoken google-genai
    ```

2. **Mirá cómo se parte un texto.** Creá `tokens.py`:

    ```python
    import tiktoken

    enc = tiktoken.get_encoding("o200k_base")

    textos = {
        "inglés": "The weather is nice today, so we will go for a walk in the park.",
        "español": "Hoy hace buen tiempo, así que vamos a salir a caminar por el parque.",
        "palabra rara": "electroencefalografista",
        "número": "3.141592653589793",
    }

    for nombre, texto in textos.items():
        tokens = enc.encode(texto)
        partes = [enc.decode([t]) for t in tokens]
        print(f"{nombre}: {len(texto)} caracteres, {len(tokens)} tokens")
        print("   ", partes)
    ```

    Ejecutalo con `uv run tokens.py`. La primera vez, `tiktoken` descarga su vocabulario: necesitás conexión a internet.

    **Resultado esperado:** para cada texto, la cantidad de tokens y cómo se partió. Anotá cuántos tokens tuvo cada uno.

3. **Compará con el tokenizador de Gemini.** Creá `gemini_tokens.py`:

    ```python
    from google import genai

    client = genai.Client()

    for texto in [
        "The weather is nice today, so we will go for a walk in the park.",
        "Hoy hace buen tiempo, así que vamos a salir a caminar por el parque.",
    ]:
        respuesta = client.models.count_tokens(model="gemini-3.8-flash", contents=texto)
        print(respuesta.total_tokens, "tokens:", texto)
    ```

    Ejecutalo con la clave del Módulo 0, sin copiarla:

    ```bash
    uv run --env-file ../m00-modelos/.env gemini_tokens.py
    ```

    **Resultado esperado:** dos cantidades, probablemente distintas de las de `tiktoken` para los mismos textos.

4. **Calculá el costo de dos imágenes.** Con la fórmula de Claude del recuadro *Específico de herramienta*, calculá cuántos tokens cuesta una imagen de 200 × 200 píxeles y una de 1000 × 1000.

    **Resultado esperado:** dos números. ¿Cuántas veces más cuesta la grande?

### Ejercicio

**Objetivo:** medir el efecto del idioma con tus propios textos.

1. Elegí un párrafo de unas 50 palabras de un texto tuyo (un correo, una documentación) que no tenga datos personales, y escribí su traducción al inglés o al español.
2. Agregalo a `tokens.py` en los dos idiomas y ejecutalo.
3. Calculá cuántos tokens más (o menos) ocupa la versión en español, en porcentaje.

**Criterios de aceptación:**

- [ ] `tokens.py` muestra los dos textos con su cantidad de tokens.
- [ ] Anotaste el porcentaje de diferencia y una explicación de por qué.
- [ ] El proyecto `practicas/m01-tokens` está en un *commit*.

Comprobá tus resultados en las [soluciones de la práctica](soluciones/l1-2-1.md#práctica).

## Autoevaluación

Elegí una respuesta en cada pregunta. La página te corrige al instante y explica por qué. Para completar la lección necesitás 4 de 5 correctas, además del ejercicio.

```quiz
¿Por qué los modelos usan tokens en lugar de palabras completas?
- [ ] Porque las palabras ocupan más memoria en la computadora
- [x] Porque un vocabulario de palabras no tendría fin, y con fragmentos se puede escribir cualquier texto
- [ ] Porque así lo exige el idioma inglés
> Con palabras, cada nombre propio o palabra nueva necesitaría su propio lugar. Los tokens son un vocabulario fijo de fragmentos que alcanza para cualquier texto.
```

```quiz
En BPE, ¿qué pasa con una palabra muy frecuente en los textos de entrenamiento del tokenizador?
- [x] Suele quedar como un solo token
- [ ] Se divide en letras
- [ ] Se elimina del vocabulario
> BPE une los pares más frecuentes una y otra vez, así que las palabras comunes terminan siendo un solo token. Las raras se arman con varios.
```

```quiz
El mismo texto, traducido al español, ocupa más tokens que en inglés. ¿Cuál es la causa más probable?
- [ ] El español tiene más letras en su alfabeto
- [x] El vocabulario del tokenizador se armó con más texto en inglés, y más palabras en español se parten en varios fragmentos
- [ ] Los modelos cobran más por los idiomas que no son el inglés
> El tokenizador refleja los textos con los que se construyó. El precio por token es el mismo; lo que cambia es la cantidad de tokens.
```

```quiz
Un modelo se equivoca al contar cuántas letras "r" tiene una palabra. ¿Qué lo explica mejor?
- [ ] El modelo no sabe leer
- [x] El modelo procesa tokens, no letras: la palabra puede ser uno o dos fragmentos que no muestran sus letras por separado
- [ ] Es un problema de la conexión a internet
> Si una palabra es un solo token, el modelo no "ve" sus letras una por una. Por eso tareas de deletreo o conteo de caracteres pueden fallar.
```

```quiz
Tenés que analizar 10.000 fotos de productos y alcanza con reconocer de qué tipo es cada uno. ¿Qué hacés para bajar el costo?
- [ ] Nada: las imágenes cuestan lo mismo sin importar el tamaño
- [x] Reducir su resolución antes de enviarlas, porque menos píxeles son menos tokens
- [ ] Convertirlas a blanco y negro
> El costo de una imagen depende de cuántos cuadrados ocupa. Si no necesitás detalle fino, una imagen más chica cuesta menos tokens.
```

## Resumen

- Un **token** es un fragmento de texto con un número en un vocabulario fijo; el **tokenizador** convierte texto en tokens y al revés.
- **BPE** arma el vocabulario uniendo los pares más frecuentes: las palabras comunes son un token, las raras varios.
- El español suele ocupar más tokens que el inglés; los números y las palabras raras se parten en pedazos arbitrarios.
- Cada modelo tiene su propio tokenizador: usá el contador de cada proveedor.
- Las imágenes también son tokens, y más resolución cuesta más.
- Costo, límites y velocidad se miden en tokens.

## Para profundizar

- **L1.2.2:** embeddings, lo que el modelo hace con cada token.
- **L1.4.2:** la ventana de contexto en la práctica.
- **Términos nuevos en el [glosario](../glosario.md):** tokenizador, BPE.
