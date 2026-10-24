---
id: L0.2.1
titulo: "Repositorio y entorno de trabajo"
modulo: M0
unidad: U0.2
tipo: P
horas_estimadas: 2
costo: gratis
estado: borrador
ultima_revision: 2026-10-24
version_academica: "1.3"
soluciones: soluciones/l0-2-1.md
---

# Repositorio y entorno de trabajo

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** armar tu repositorio de trabajo del curso, crear proyectos de Python aislados con `uv` y comprobar que Docker funciona.
> - **Necesitás:** [L0.1.1](l0-1-1-mapa-del-curso.md); una computadora con Windows 10/11, macOS o Linux donde puedas instalar programas; saber abrir una terminal.
> - **Tiempo:** 2 horas (20 min de lectura y 1 h 40 de práctica) · **Costo:** gratis.

> [!WARNING]
> 📝 **Borrador.** Esta lección todavía no pasó la revisión final.

## Teoría

### 1. Entorno reproducible

Tu **entorno de trabajo** es todo lo que tu código necesita: el lenguaje y su versión, las librerías y las herramientas. Es **reproducible** cuando podés recrearlo igual en otra computadora siguiendo instrucciones escritas.

En IA las librerías cambian cada pocas semanas (ver [L0.1.2](l0-1-2-aprender-en-un-campo-que-cambia.md)). Si cada práctica declara sus versiones, cuando algo deja de andar sabés qué cambió.

### 2. Tu repositorio de trabajo

Todo lo que produzcas en el curso va en una carpeta con Git, **fuera** de la carpeta del curso. Si la subís a GitHub, que sea **privada**: va a tener tus respuestas.

```text
curso-ia-trabajo/
├── README.md        ← qué hay y cómo recrear el entorno
├── .gitignore       ← lo que Git no tiene que versionar
├── apuntes/
├── practicas/       ← una carpeta por práctica
└── proyectos/
```

El archivo **`.gitignore`** le indica a Git qué archivos ignorar. Hay tres cosas que nunca se versionan:

| Qué | Ejemplos | Por qué |
|---|---|---|
| **Secretos** | `.env`, claves de API | Quien vea el repositorio puede usarlos a tu nombre |
| **Archivos generados** | `.venv/`, `__pycache__/` | Se recrean con un comando |
| **Archivos grandes** | modelos descargados | Git no está pensado para archivos de varios GB |

### 3. Entornos de Python con `uv`

Si instalás librerías de Python en el sistema, todas tus prácticas comparten las mismas versiones, y actualizar una puede romper otra. Un **entorno virtual** lo evita: es una carpeta (`.venv/`) con su propio Python y sus propias librerías, solo para ese proyecto.

El curso usa **`uv`**, una herramienta que crea el entorno, instala Python si hace falta y registra las dependencias:

| Archivo | Qué contiene | ¿Va a Git? |
|---|---|---|
| `pyproject.toml` | Nombre del proyecto, versión de Python y dependencias | Sí |
| `uv.lock` | Versiones exactas de todas las dependencias (un *lockfile*) | Sí |
| `.python-version` | Versión de Python del proyecto | Sí |
| `.venv/` | El entorno instalado | **No**: se recrea con `uv sync` |

Si ya usás `venv` con `pip`, o Poetry, los conceptos son los mismos.

### 4. Docker

Un **contenedor** es un programa que corre aislado, con sus propios archivos y configuración, creado a partir de una **imagen** (la plantilla). En el curso, Docker sirve para correr servicios como n8n (Módulo 5) o una base de datos (Módulo 8) sin instalarlos en tu sistema: si algo sale mal, borrás el contenedor y empezás de nuevo.

### 5. Java (opcional)

Solo hace falta para las lecciones de Java *para profundizar* (L6.4.3, L10.2.2 y L14.3.2): un JDK en versión LTS (con soporte extendido), 21 o superior.

> [!NOTE]
> **Específico de herramienta** · verificado el 2026-10-24 · fuentes: [uv](https://docs.astral.sh/uv/getting-started/installation/) · [Git para Windows](https://git-scm.com/install/windows) · [Docker Desktop para Windows](https://docs.docker.com/desktop/setup/install/windows-install/) · [Eclipse Temurin](https://adoptium.net/installation)
>
> - **Python:** la última versión estable es la 3.15; el curso funciona con 3.12 o superior.
> - **Java:** la LTS más reciente de Temurin es la 25; también sirve la 21.
> - **Docker Desktop en Windows:** requiere Windows 10 22H2 o Windows 11 23H2, edición Pro, Enterprise o Education, con WSL 2 y al menos 8 GB de RAM. Es gratis para uso personal, educativo y empresas de menos de 250 empleados **y** menos de 10 millones de dólares anuales.

> [!TIP]
> **Errores frecuentes**
>
> - Después de instalar algo, la terminal dice que el comando no existe: abrí una terminal nueva.
> - Hacer un *commit* sin mirar antes `git status`.
> - Usar tu correo personal en Git y después publicar un repositorio: queda visible en cada *commit*.

## Práctica

En Windows usá **PowerShell**; en macOS, la app *Terminal*. También necesitás un editor de texto: si no tenés uno, [VS Code](https://code.visualstudio.com/) es gratuito. Si ya tenés una herramienta instalada, verificá la versión y seguí.

### Práctica guiada

1. **Instalá y configurá Git.**

    === "PowerShell (Windows)"

        ```powershell
        winget install --id Git.Git -e --source winget
        ```

    === "Bash (macOS, Linux)"

        En macOS, `git --version` ofrece instalarlo. En Debian o Ubuntu: `sudo apt install git`.

    En una terminal nueva, configurá tu identidad. Si alguna vez vas a publicar repositorios, usá el correo privado de GitHub (*Settings › Emails*) en lugar del personal.

    ```bash
    git --version
    git config --global user.name "Tu nombre"
    git config --global user.email "<tu correo>"
    git config --global init.defaultBranch main
    ```

    **Resultado esperado:** `git version 2.…` y, con `git config --global --list`, los tres valores.

2. **Creá el repositorio con su `.gitignore`.** El `.gitignore` se descarga del curso: ya incluye secretos, entornos y archivos de editores.

    === "PowerShell (Windows)"

        ```powershell
        cd $HOME\Documents
        mkdir curso-ia-trabajo; cd curso-ia-trabajo
        git init
        mkdir apuntes, practicas, proyectos
        Invoke-WebRequest https://raw.githubusercontent.com/CaminosMarina/curso-ia/main/plantillas/cuaderno-estudiante/.gitignore -OutFile .gitignore -UseBasicParsing
        ```

    === "Bash (macOS, Linux)"

        ```bash
        cd ~/Documents
        mkdir curso-ia-trabajo && cd curso-ia-trabajo
        git init
        mkdir apuntes practicas proyectos
        curl -fsSL -o .gitignore https://raw.githubusercontent.com/CaminosMarina/curso-ia/main/plantillas/cuaderno-estudiante/.gitignore
        ```

    Abrí el `.gitignore` en tu editor y leelo: tenés que poder explicar para qué está cada grupo de líneas.

    **Resultado esperado:** `git status` dice `On branch main` y `No commits yet`.

3. **Escribí el `README.md` y hacé el primer *commit*.** Con tu editor, creá `README.md` con un título y una línea que explique qué guarda el repositorio. Después:

    ```bash
    git add .
    git status
    ```

    Revisá la lista: solo tienen que aparecer `.gitignore` y `README.md` (Git no guarda carpetas vacías; las otras aparecen cuando tengan archivos). Si está bien:

    ```bash
    git commit -m "Inicio del repositorio de trabajo"
    ```

    **Resultado esperado:** `git log --oneline` muestra un *commit*.

4. **Instalá `uv`.**

    === "PowerShell (Windows)"

        ```powershell
        winget install --id=astral-sh.uv -e
        ```

    === "Bash (macOS, Linux)"

        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```

    **Resultado esperado:** en una terminal nueva, `uv --version` muestra un número de versión.

5. **Creá tu primer proyecto de Python.** Desde la carpeta del repositorio:

    ```bash
    uv init --vcs none practicas/m00-hola
    cd practicas/m00-hola
    uv run main.py
    uv add rich
    ```

    `--vcs none` evita que `uv` cree otro repositorio Git dentro del tuyo. `uv run` crea `.venv/` la primera vez y ejecuta el programa; `uv add` instala `rich` (una librería para mostrar texto con formato, que usamos como ejemplo) solo en este proyecto.

    **Resultado esperado:** `Hello from m00-hola!`. En `pyproject.toml` aparece `rich` en `dependencies`, y se creó `uv.lock`.

6. **Instalá Docker y probalo.** En Windows y macOS, instalá [Docker Desktop](https://docs.docker.com/desktop/) (en Windows, aceptá activar WSL 2 si te lo pide). En Linux, [Docker Engine](https://docs.docker.com/engine/install/). Con Docker abierto:

    ```bash
    docker run hello-world
    ```

    **Resultado esperado:** el mensaje `Hello from Docker!`.

    Si tu computadora no cumple los requisitos, anotalo y seguí: Docker se usa recién desde el Módulo 5.

7. **(Opcional) Instalá Java.** En Windows: `winget install EclipseAdoptium.Temurin.25.JDK`. En macOS o Linux, seguí [adoptium.net/installation](https://adoptium.net/installation).

    **Resultado esperado:** `java -version` muestra `25` y `Temurin`.

### Ejercicio

**Objetivo:** registrar tu entorno y comprobar que el repositorio ignora lo que corresponde.

1. Creá `apuntes/entorno.md` con la fecha, tu sistema operativo y la salida de `git --version`, `uv --version`, `uv run python --version` (desde `practicas/m00-hola`), `docker --version` y, si lo instalaste, `java -version`.
2. Hacé un *commit* que incluya `apuntes/entorno.md` y `practicas/m00-hola`.

**Criterios de aceptación:**

- [ ] `apuntes/entorno.md` tiene la fecha y las versiones, incluida la de Python.
- [ ] El *commit* incluye `pyproject.toml`, `uv.lock` y `.python-version` de `m00-hola`.
- [ ] Nada de `.venv/` está versionado.
- [ ] `git status` dice `nothing to commit, working tree clean`.

**Cómo verificar:** desde la raíz del repositorio, `git ls-files` no tiene que mostrar nada dentro de `.venv/`, y `git check-ignore -v practicas/m00-hola/.venv` tiene que mostrar la línea del `.gitignore` que lo ignora.

> [!TIP]
> **Respaldo en GitHub (opcional):** creá un repositorio nuevo marcado como **Private**, sin README ni `.gitignore`, y seguí las instrucciones de GitHub para subir un repositorio existente.

Comprobá tu trabajo y los problemas frecuentes en las [soluciones de la práctica](soluciones/l0-2-1.md#práctica).

## Autoevaluación

Elegí una respuesta en cada pregunta. Esta lección se completa con el ejercicio; las preguntas sirven para comprobar que entendiste el porqué.

```quiz
¿Por qué conviene un entorno virtual por proyecto?
- [ ] Porque las librerías instaladas en el sistema son más lentas
- [x] Porque cada proyecto puede necesitar versiones distintas, y así actualizar uno no rompe otro
- [ ] Porque Python no permite instalar librerías en el sistema
> Un entorno virtual tiene su propio Python y sus propias librerías: cada práctica usa sus versiones sin afectar a las demás.
```

```quiz
Tu práctica tiene `pyproject.toml`, `uv.lock`, `.python-version` y `.venv/`. ¿Qué subís al repositorio?
- [ ] Todo, para que sea reproducible
- [x] Todo menos `.venv/`
- [ ] Solo `pyproject.toml`
> `.venv/` se recrea con `uv sync` a partir de los otros tres archivos. `uv.lock` es el que garantiza las mismas versiones exactas.
```

```quiz
Instalaste `uv`, pero la terminal dice que el comando no existe. ¿Qué probás primero?
- [ ] Reinstalar `uv` con otro método
- [x] Abrir una terminal nueva
- [ ] Instalar Python primero
> El instalador agrega `uv` a la lista de carpetas donde se buscan comandos (la variable PATH), pero una terminal ya abierta conserva la lista anterior.
```

## Resumen

- Tu repositorio de trabajo es privado, vive fuera del curso y nunca versiona secretos, archivos generados ni archivos grandes.
- Mirá `git status` antes de cada *commit*.
- Cada práctica de Python es un proyecto aislado: `uv init`, `uv add`, `uv run`. Se versiona todo menos `.venv/`.
- Docker corre servicios aislados; lo vas a usar desde el Módulo 5.
- Java es opcional.

## Para profundizar

- **L0.2.2:** claves de API seguras y primer modelo local.
- [uv: trabajar con proyectos](https://docs.astral.sh/uv/guides/projects/) · [Pro Git, el libro oficial de Git](https://git-scm.com/book/es/v2) · [Docker: primeros pasos](https://docs.docker.com/get-started/).
- **Términos nuevos en el [glosario](../glosario.md):** entorno virtual, *lockfile* y contenedor.
