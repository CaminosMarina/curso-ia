---
id: Lm.u.n
titulo: "<título corto, igual que en la portada del módulo>"
modulo: Mm
unidad: Um.u
tipo: C            # C conceptual · P práctica · M mixta (igual que en la portada del módulo)
horas_estimadas: 1.5
costo: gratis      # gratis · opcional-pago · requiere-pago
estado: borrador   # borrador · revisada · publicada
ultima_revision: AAAA-MM-DD
version_academica: "1.3"
soluciones: soluciones/lm-u-n.md
---

<!--
CÓMO USAR ESTA PLANTILLA
- Copiala a docs/mNN-<slug>/lm-u-n-<slug>.md, completá el front matter y ejecutá
  python scripts/generar.py: la lección aparece en el menú, en el índice y en la portada del módulo.
  El selector de estado (Por hacer / En curso / Completada) se agrega solo al final de la página.
- Mantené los seis encabezados de nivel 2 (los verifica scripts/verificar.py). Los de nivel 3 son libres.
- Autodidacta: la lección se tiene que entender sola, sin conversaciones ni tutor. No uses frases
  como "como vimos" sin citar la lección ("ver L1.2.1").
- Teoría clara y concisa: cada término se define antes de usarse; un ejemplo por idea importante;
  diagramas mermaid cuando ayuden. Lo que cambia seguido (versiones, planes, precios, pantallas)
  va en un aviso "Específico de herramienta" con fecha y fuente oficial.
- Práctica paso a paso: un paso = una acción + el resultado esperado. Comandos para Bash y
  PowerShell cuando difieran (pestañas). Capturas solo donde hay que tocar una interfaz.
- Capturas: en docs/mNN-<slug>/img/, nombre lm-u-n-paso-N.png, texto alternativo descriptivo,
  clase "captura" y sin datos personales (correos, nombres de cuenta, rutas).
    ![Botón "New project" en la barra lateral](img/l3-2-3-paso-1.png){ .captura }
- Ninguna respuesta va en este archivo: van en soluciones/.
- Borrá este comentario al terminar.
-->

# Título corto de la lección

> [!NOTE]
> **Antes de empezar**
>
> - **Vas a aprender a:** <2 a 5 objetivos con verbos observables: explicar, distinguir, configurar, decidir…>
> - **Necesitás:** <lecciones previas, software y versión mínima, cuentas>
> - **Tiempo:** <lectura + práctica> · **Costo:** <gratis / opcional pago / requiere pago, con alternativa gratuita>

## Teoría

### 1. <Primer concepto>

<Qué es, para qué sirve y cómo funciona. Corto. Un ejemplo concreto.>

### 2. <Segundo concepto>

<…>

> [!TIP]
> **Errores frecuentes:** <errores típicos y cómo detectarlos>

## Práctica

<Si la lección es conceptual [C], la práctica es la pregunta de aplicación. Si no hace falta práctica, escribí "Esta lección no tiene práctica" y el motivo.>

### Práctica guiada

1. **<Acción>.** <Detalle.>

    **Resultado esperado:** <qué tenés que ver.>
2. …

=== "Bash (Linux, macOS, Git Bash)"

    ```bash
    comando
    ```

=== "PowerShell (Windows)"

    ```powershell
    comando
    ```

### Ejercicio

**Objetivo:** <qué demostrás.>

1. …

**Criterios de aceptación:**

- [ ] <condición observable>

**Cómo verificar:** <comandos y salida esperada, o lista de comprobación.>

<details markdown>
<summary>Pista 1</summary>

…

</details>

## Autoevaluación

Elegí una respuesta en cada pregunta. La página te corrige al instante. Para completar la lección necesitás 80% o más.

<!-- 3 a 5 preguntas, al menos una de diagnóstico ("¿por qué pasa X?"). Una sola opción correcta,
     marcada con [x]. La línea con ">" es la explicación que se muestra al responder. -->

```quiz
¿Pregunta?
- [ ] Opción incorrecta, pero creíble
- [x] Opción correcta
- [ ] Otra opción incorrecta
> Por qué la correcta es correcta y por qué las otras no.
```

## Resumen

- <4 a 7 viñetas con lo esencial.>

## Para profundizar

- <Lecciones relacionadas y fuentes oficiales.>
- **Términos nuevos en el [glosario](../glosario.md):** <lista.>
