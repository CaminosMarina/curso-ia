---
id: L0.2.2
titulo: "Claves de API y primer modelo local"
modulo: M0
unidad: U0.2
tipo: P
horas_estimadas: 2
costo: gratis
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/l0-2-2.md
---

# Claves de API y primer modelo local

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** guardar una clave de API sin exponerla, controlar el gasto de un proveedor, correr un modelo en tu computadora con Ollama y comprobar que tu repositorio no tiene secretos.
> - **Necesitás:** [L0.2.1](l0-2-1-repositorio-y-entorno.md) (tu repositorio de trabajo y `uv`); una cuenta de Google; unos 5 GB libres en disco.
> - **Tiempo:** 2 horas (20 min de lectura y 1 h 40 de práctica) · **Costo:** gratis (nivel gratuito de la API de Gemini).

> [!WARNING]
> 📝 **Borrador.** Esta lección todavía no pasó la revisión final.

## Teoría

### 1. Qué es una clave de API

Una **API** de un modelo es un servicio web al que tu programa le envía texto y recibe la respuesta del modelo. Para saber quién la usa y a quién cobrarle, el proveedor te da una **clave de API**: una cadena larga que tu programa envía en cada llamada.

Una clave funciona como una contraseña: **quien la tenga puede usar la API a tu nombre y gastar tu saldo**. Hay programas que recorren GitHub buscando claves publicadas por error, y pueden usarlas en minutos.

### 2. Dónde guardarla

La clave nunca va en el código ni en el repositorio. Se guarda en una **variable de entorno**, un valor que el sistema operativo le pasa a tu programa al ejecutarlo.

En lugar de definir la variable en la terminal cada vez, se escribe en un archivo **`.env`** en la carpeta del proyecto:

```text
GEMINI_API_KEY=tu-clave
```

- El `.gitignore` del curso ya ignora `.env`.
- Al lado se versiona un **`.env.example`** con los nombres de las variables y sin valores, para que quien clone el proyecto sepa qué necesita.
- `uv run --env-file .env programa.py` carga las variables del archivo al ejecutar.

Otras opciones, para más adelante: un gestor de contraseñas para guardar la clave original, y los gestores de secretos de cada nube (Módulo 16).

**Si una clave se filtra** (la subiste a GitHub, la pegaste en un chat, aparece en una captura): revocala en la consola del proveedor y creá otra. Borrarla del repositorio no alcanza, porque queda en el historial de Git.

### 3. Controlar el gasto

Los proveedores cobran por uso: por cantidad de texto procesado (lo vas a ver en el Módulo 1 como *tokens*). Un error en un bucle puede hacer miles de llamadas. Antes de cargar saldo en cualquier proveedor:

- **Configurá un límite de gasto**: al alcanzarlo, la API deja de responder en lugar de seguir cobrando.
- **Preferí saldo prepago** cuando el proveedor lo ofrezca: no podés gastar más de lo que cargaste.

En este curso empezás con el **nivel gratuito de la API de Gemini**, que no requiere vincular un medio de pago. Tiene una condición importante: lo que enviás puede usarse para mejorar los productos de Google, y personas pueden revisarlo. **No le envíes datos personales ni confidenciales.**

### 4. Modelos locales

Un **modelo local** corre en tu computadora: no necesita internet ni clave, no tiene costo por uso y tus datos no salen de tu equipo. A cambio, los modelos que entran en una computadora personal son menos capaces que los de las API, y más lentos sin una buena placa de video.

**Ollama** es una aplicación que descarga modelos abiertos (que cualquiera puede descargar y ejecutar) y los corre en tu computadora. Además de un chat en la terminal, levanta un servidor en tu computadora (en `http://localhost:11434`) al que tus programas le hablan como si fuera una API.

El tamaño de un modelo se mide en **parámetros**, los valores numéricos que aprendió (se explica en el Módulo 1). Un modelo de 3.000 millones de parámetros pesa unos 2 GB y corre en una computadora común; uno de 30.000 millones necesita una placa de video potente.

> [!NOTE]
> **Específico de herramienta** · verificado el 2026-10-24 · fuentes: [Gemini API: quickstart](https://ai.google.dev/gemini-api/docs/quickstart) · [Gemini API: facturación](https://ai.google.dev/gemini-api/docs/billing) · [Gemini API: términos](https://ai.google.dev/gemini-api/terms) · [Ollama](https://github.com/ollama/ollama) · [Gitleaks](https://github.com/gitleaks/gitleaks)
>
> - **Gemini:** el nivel gratuito no requiere vincular facturación. El modelo del ejemplo es `gemini-3.8-flash`, el que usa la guía oficial. Si activás la facturación, AI Studio permite fijar un límite de gasto por proyecto en la página *Spend*.
> - **Ollama:** en Windows requiere Windows 10 22H2 o posterior (Home o Pro) y al menos 4 GB libres para la instalación, más el espacio de los modelos. El modelo del ejemplo, `llama3.2`, es el que usa la documentación oficial y pesa unos 2 GB. Los modelos disponibles están en [ollama.com/library](https://ollama.com/library).
> - **Gitleaks:** el proyecto se considera completo y solo recibe parches de seguridad. Sigue siendo válido para esta comprobación.

> [!TIP]
> **Errores frecuentes**
>
> - Pegar la clave en el código "solo para probar" y después hacer un *commit*.
> - Compartir una captura de pantalla o un mensaje de error que muestra la clave.
> - Borrar una clave filtrada del repositorio sin revocarla.

## Práctica

Abrí una terminal en la raíz de tu repositorio de trabajo (`curso-ia-trabajo`).

### Práctica guiada

1. **Instalá Ollama.**

    === "PowerShell (Windows)"

        ```powershell
        irm https://ollama.com/install.ps1 | iex
        ```

        También podés usar el [instalador](https://ollama.com/download).

    === "Bash (macOS, Linux)"

        ```bash
        curl -fsSL https://ollama.com/install.sh | sh
        ```

    **Resultado esperado:** en una terminal nueva, `ollama --version` muestra un número de versión.

2. **Conversá con un modelo local.**

    ```bash
    ollama run llama3.2
    ```

    La primera vez descarga el modelo. Cuando aparezca `>>>`, escribí una pregunta corta, por ejemplo "¿Qué es una API?". Para salir, escribí `/bye`.

    **Resultado esperado:** una respuesta en la terminal. Una vez descargado, el modelo funciona sin internet. Puede equivocarse: es un modelo chico.

3. **Llamá al modelo local desde Python.** Creá el proyecto e instalá las dos librerías que vas a usar:

    ```bash
    uv init --vcs none practicas/m00-modelos
    cd practicas/m00-modelos
    uv add ollama google-genai
    ```

    Creá `local.py`:

    ```python
    from ollama import chat

    respuesta = chat(model="llama3.2", messages=[
        {"role": "user", "content": "Decí hola en una oración."},
    ])
    print(respuesta.message.content)
    ```

    Ejecutalo con `uv run local.py`. El `main.py` que crea `uv init` no se usa en esta práctica: podés borrarlo.

    **Resultado esperado:** un saludo generado por el modelo. Ollama tiene que estar abierto (en Windows y macOS queda corriendo en segundo plano).

4. **Creá tu clave de Gemini y guardala en `.env`.** Entrá a [Google AI Studio › API keys](https://aistudio.google.com/apikey) con tu cuenta de Google, creá una clave y copiala. En `practicas/m00-modelos`, creá dos archivos con tu editor (en Windows, no uses `>` en PowerShell: puede guardarlos en una codificación que `uv` no lee):

    - `.env`, con tu clave: `GEMINI_API_KEY=` seguido de la clave.
    - `.env.example`, sin la clave: `GEMINI_API_KEY=`

    Comprobá que Git ignora el primero:

    ```bash
    git status
    git check-ignore -v .env
    ```

    **Resultado esperado:** entre los archivos nuevos, `git status` muestra `.env.example`, pero no `.env`; `git check-ignore` muestra la regla `.env` del `.gitignore`.

5. **Llamá a la API de Gemini.** Creá `api.py` con el ejemplo de la guía oficial:

    ```python
    from google import genai

    client = genai.Client()  # lee la clave de la variable GEMINI_API_KEY

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input="Decí hola en una oración.",
    )
    print(interaction.output_text)
    ```

    Ejecutalo cargando el `.env`:

    ```bash
    uv run --env-file .env api.py
    ```

    **Resultado esperado:** un saludo generado por Gemini. Si aparece un error de autenticación, revisá que el `.env` no tenga espacios ni comillas alrededor de la clave.

6. **Revisá el gasto.** En AI Studio, en la sección de facturación, comprobá que tu proyecto está en el **nivel gratuito**, sin facturación vinculada: así no puede generar cargos. Si alguna vez la activás, fijá ahí un límite de gasto antes de usarla.

7. **Buscá secretos en tu repositorio con Gitleaks.** Instalalo:

    === "PowerShell (Windows)"

        ```powershell
        winget install --id=Gitleaks.Gitleaks -e
        ```

    === "Bash (macOS, Linux)"

        En macOS: `brew install gitleaks`. En Linux, descargá el binario de la [página de versiones](https://github.com/gitleaks/gitleaks/releases).

    Después, desde la raíz de tu repositorio:

    ```bash
    gitleaks git
    ```

    **Resultado esperado:** la última línea dice `no leaks found`. Gitleaks revisa todos los *commits*: tu `.env` no aparece porque nunca entró a Git.

### Ejercicio

**Objetivo:** versionar la práctica sin exponer la clave, y demostrarlo.

1. Hacé un *commit* con `practicas/m00-modelos`.
2. Ejecutá `gitleaks git` desde la raíz del repositorio.

**Criterios de aceptación:**

- [ ] El *commit* incluye `local.py`, `api.py`, `pyproject.toml`, `uv.lock` y `.env.example`.
- [ ] `.env` no está versionado: `git ls-files` no lo muestra.
- [ ] `gitleaks git` termina con `no leaks found`.
- [ ] Tu proyecto de AI Studio está en el nivel gratuito, o tiene un límite de gasto configurado.

Comprobá tu trabajo y los problemas frecuentes en las [soluciones de la práctica](soluciones/l0-2-2.md#práctica).

## Autoevaluación

Elegí una respuesta en cada pregunta. Esta lección se completa con el ejercicio; las preguntas sirven para comprobar que entendiste el porqué.

```quiz
Subiste por error tu clave de API a un repositorio público. ¿Qué hacés primero?
- [ ] Borro el archivo y hago un nuevo commit
- [x] Revoco la clave en la consola del proveedor y creo una nueva
- [ ] Hago el repositorio privado
> La clave pudo haber sido copiada apenas se publicó, y sigue en el historial de Git aunque borres el archivo. Lo único que la inutiliza es revocarla.
```

```quiz
¿Para qué sirve versionar un `.env.example` sin valores?
- [ ] Para que el programa funcione sin clave
- [x] Para que quien clone el proyecto sepa qué variables tiene que configurar
- [ ] Para que Gitleaks no dé error
> El `.env.example` documenta los nombres de las variables. Cada persona crea su propio `.env` con sus valores, que nunca se versiona.
```

```quiz
Tenés que resumir documentos internos de tu trabajo. ¿Qué opción del Módulo 0 es la adecuada?
- [ ] El nivel gratuito de la API de Gemini, porque es más capaz
- [x] Un modelo local con Ollama, porque los datos no salen de tu computadora
- [ ] Cualquiera de las dos: el resultado es el mismo
> Lo que enviás al nivel gratuito de Gemini puede usarse para mejorar productos y ser revisado por personas. Con un modelo local los datos quedan en tu equipo, aunque el modelo sea menos capaz.
```

## Resumen

- Una clave de API es como una contraseña: quien la tenga gasta a tu nombre.
- Va en un `.env` ignorado por Git; se versiona un `.env.example` sin valores.
- Si se filtra, se revoca. Borrarla del repositorio no alcanza.
- Antes de cargar saldo en un proveedor, configurá un límite de gasto.
- El nivel gratuito de Gemini no cobra, pero no es privado: no envíes datos sensibles.
- Un modelo local es privado y gratuito, pero menos capaz.
- `gitleaks git` comprueba que ningún *commit* tenga secretos.

## Para profundizar

- **Módulo 1:** qué son los tokens y por qué determinan el costo.
- **Módulo 6:** las API de modelos en detalle.
- **Términos nuevos en el [glosario](../glosario.md):** clave de API, variable de entorno, modelo local.
