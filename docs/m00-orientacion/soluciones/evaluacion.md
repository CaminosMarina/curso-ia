# Guía de comprobación · Evaluación del Módulo 0

> [!WARNING]
> **Spoilers.** Consultá esta página **después** de intentar.
>
> Evaluación: [Evaluación del Módulo 0](../evaluacion.md) · Estado: 📝 borrador · Última revisión: 2026-10-24

Las preguntas de las Partes A a C se corrigen en la misma página. Acá está qué revisar si un punto de la Parte D no se cumple.

## Parte D

| Punto | Cómo comprobarlo | Si no se cumple |
|---|---|---|
| *Commits* con las prácticas y `apuntes/entorno.md` | `git log --stat` muestra qué archivos entraron en cada *commit* | Agregá lo que falte con `git add` y hacé un nuevo *commit* ([L0.2.1](../l0-2-1-repositorio-y-entorno.md), ejercicio) |
| Sin `.env` ni `.venv/` versionados | `git ls-files` | Sacalos del repositorio sin borrarlos del disco con `git rm -r --cached <ruta>`. Si era un `.env` con una clave, revocala |
| Gitleaks sin hallazgos | `gitleaks git` desde la raíz | Revocá la clave encontrada y creá otra ([L0.2.2](../l0-2-2-claves-y-modelo-local.md), soluciones) |
| Modelo local | `ollama list` muestra `llama3.2` | Abrí Ollama o descargá el modelo con `ollama pull llama3.2` |
| API de Gemini | El programa imprime un saludo | Revisá el `.env` y los problemas frecuentes de las [soluciones de L0.2.2](l0-2-2.md#problemas-frecuentes) |
| Gasto controlado | En AI Studio, sección de facturación | Si vinculaste facturación, fijá un límite de gasto en la página *Spend* |
