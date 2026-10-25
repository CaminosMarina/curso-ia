---
id: EVAL-M0
modulo: M0
tipo: evaluacion
titulo: "Evaluación del Módulo 0 · Orientación y entorno de trabajo"
umbral_aprobacion: 80
tiempo_estimado: 45 min
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/evaluacion.md
---

# Evaluación del Módulo 0

> [!NOTE]
> **Antes de empezar**
>
> - **Cuándo hacerla:** después de completar las cuatro lecciones del módulo.
> - **Tiempo:** unos 45 minutos (20 de preguntas y 25 para comprobar la práctica).
> - **Cómo se aprueba:** 8 de las 10 preguntas correctas **y** todos los puntos de la Parte D cumplidos.

> [!WARNING]
> 📝 **Borrador.** Esta evaluación todavía no pasó la revisión final.

Respondé sin mirar las lecciones. Las preguntas se corrigen al instante y explican cada respuesta. Si no llegás a 8, repasá las lecciones indicadas al final y volvé a intentarlo otro día.

## Parte A · Conceptos

```quiz
¿Cuál de estos datos es conocimiento volátil, que conviene verificar con fecha y fuente?
- [ ] Un modelo de lenguaje puede generar datos falsos con tono seguro
- [x] La cantidad de llamadas por minuto que permite el nivel gratuito de una API
- [ ] Una clave de API no se guarda en un repositorio
> Los límites de un plan cambian según decisiones comerciales: son volátiles. Las otras dos opciones describen cómo funcionan las cosas, y eso dura años.
```

```quiz
Completaste los Módulos 0 a 7. Un módulo tiene al Módulo 6 como prerrequisito indispensable y al Módulo 8 como recomendado. ¿Podés empezarlo?
- [x] Sí: tenés el indispensable, y el recomendado se puede retomar después
- [ ] No: falta el Módulo 8
- [ ] Solo si hacés el Módulo 8 al mismo tiempo
> Para empezar un módulo alcanza con sus prerrequisitos indispensables. Los recomendados mejoran la experiencia, pero no son obligatorios.
```

```quiz
Le preguntás a un asistente, sin búsqueda web, por una versión de una herramienta publicada después de su fecha de corte. ¿Qué es lo más probable?
- [ ] Que responda correctamente, porque los modelos se actualizan solos
- [x] Que responda con información vieja o invente datos con tono seguro
- [ ] Que siempre diga que no sabe
> El modelo no conoce lo posterior a su fecha de corte. Como genera la respuesta más probable, puede dar información desactualizada o inventada sin avisar.
```

```quiz
¿Qué archivos alcanzan para que otra persona recree exactamente el entorno de tu práctica de Python con `uv`?
- [ ] La carpeta `.venv/`
- [ ] Solo `pyproject.toml`
- [x] `pyproject.toml`, `uv.lock` y `.python-version`
> `uv sync` recrea `.venv/` a partir de esos tres archivos. `uv.lock` fija las versiones exactas; sin él, se instalarían las versiones más nuevas disponibles.
```

## Parte B · Criterio

```quiz
Tenés que armar un prototipo rápido que procesa datos de clientes reales. ¿Qué opción del Módulo 0 usás?
- [ ] El nivel gratuito de la API de Gemini, porque es más capaz
- [x] Un modelo local con Ollama
- [ ] Pegar los datos en el chat de un asistente gratuito
> Con un modelo local los datos no salen de tu computadora. Lo que se envía al nivel gratuito de Gemini puede usarse para mejorar productos y ser revisado por personas.
```

```quiz
Un video tutorial dice que uses un parámetro de una API. El changelog oficial de este mes dice que ese parámetro está en deprecación. ¿Qué hacés?
- [ ] Lo uso: si sigue funcionando, no hay problema
- [x] Uso la alternativa que indica el changelog, porque el parámetro se va a retirar
- [ ] Espero a que el video se actualice
> Una deprecación avisa que algo va a dejar de funcionar en una fecha. La fuente oficial y reciente decide; el video quedó desactualizado.
```

```quiz
Vas a compartir un proyecto con un compañero. Necesita la misma clave de API, pero la suya. ¿Cómo lo organizás?
- [ ] Pongo la clave en `config.py`, porque el repositorio es privado
- [ ] Le mando la clave por chat y la escribo en el README
- [x] Versiono un `.env.example` sin valores; cada uno crea su `.env`, que Git ignora
> Una clave nunca va al repositorio, aunque sea privado, ni a un chat. El `.env.example` documenta qué variables hacen falta, y cada persona usa su propia clave.
```

## Parte C · Diagnóstico de casos

```quiz
Gitleaks encuentra una clave de API en un commit de hace dos meses. El repositorio es privado. ¿Qué hacés primero?
- [x] Revoco la clave en la consola del proveedor y creo una nueva
- [ ] Nada, porque el repositorio es privado
- [ ] Borro ese commit del historial
> Un repositorio privado puede compartirse o volverse público, y la clave pudo haberse copiado. Revocarla es lo único que la inutiliza; limpiar el historial viene después.
```

```quiz
Al ejecutar `uv run --env-file .env api.py` aparece `stream did not contain valid UTF-8`. Creaste el `.env` en PowerShell con `>`. ¿Cuál es la causa?
- [ ] La clave de API es inválida
- [x] El archivo quedó guardado en una codificación que `uv` no lee
- [ ] Falta instalar la librería `google-genai`
> En Windows PowerShell, `>` puede guardar el archivo en UTF-16. Hay que crearlo con un editor, en UTF-8.
```

```quiz
Creaste una práctica nueva y, después de `git add .`, `git status` lista archivos dentro de `practicas/m01-prueba/.venv/`. ¿Qué es lo más probable?
- [ ] `uv` falló al crear el entorno
- [x] El `.gitignore` de la raíz falta o tiene otro nombre
- [ ] Git siempre muestra `.venv/` la primera vez
> El `.gitignore` del curso ignora `.venv/` en cualquier carpeta. Si aparece, la regla no se está aplicando. Para sacarlo de lo que vas a confirmar: `git restore --staged practicas/m01-prueba/.venv`.
```

## Parte D · Práctica

Comprobá tu repositorio de trabajo y tildá cada punto (las marcas se guardan en este navegador):

- [ ] Tu repositorio tiene *commits* con `practicas/m00-hola`, `practicas/m00-modelos` y `apuntes/entorno.md`.
- [ ] `git ls-files` no muestra ningún `.env` ni nada dentro de `.venv/`.
- [ ] `gitleaks git`, desde la raíz, termina con `no leaks found`.
- [ ] `uv run local.py` responde con el modelo local (Ollama abierto).
- [ ] `uv run --env-file .env api.py` responde con la API de Gemini.
- [ ] Tu proyecto de AI Studio está en el nivel gratuito, o tiene un límite de gasto configurado.

Si un punto no se cumple, la [guía de comprobación](soluciones/evaluacion.md) dice qué revisar.

## Si no aprobaste

| Preguntas o puntos que fallaste | Lección para repasar |
|---|---|
| Preguntas 1, 3 y 6 | [L0.1.2 · Aprender en un campo que cambia cada mes](l0-1-2-aprender-en-un-campo-que-cambia.md) |
| Pregunta 2 | [L0.1.1 · Cómo funciona este curso](l0-1-1-mapa-del-curso.md) |
| Preguntas 4 y 10, y los dos primeros puntos de la Parte D | [L0.2.1 · Repositorio y entorno de trabajo](l0-2-1-repositorio-y-entorno.md) |
| Preguntas 5, 7, 8 y 9, y los últimos cuatro puntos de la Parte D | [L0.2.2 · Claves de API y primer modelo local](l0-2-2-claves-y-modelo-local.md) |

Cuando apruebes, el Módulo 0 queda completo. Si llevás un cuaderno de estudio, anotá la fecha y el resultado.
