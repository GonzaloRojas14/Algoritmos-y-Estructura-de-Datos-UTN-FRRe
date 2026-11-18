# Algoritmos y Estructuras de Datos — UTN FRRe

Todo el material de la materia **Algoritmos y Estructuras de Datos** (Ingeniería en Sistemas de Información, UTN Facultad Regional Resistencia, 2026), ordenado en un solo lugar: teoría, presentaciones de cátedra, guía de trabajos prácticos, clases, ejercicios resueltos, parciales y trabajos prácticos.

Casi todo está en **Markdown**, pensado para leerse en [Obsidian](https://obsidian.md) (los enlaces `[[...]]` y los callouts `> [!info]` funcionan ahí), aunque GitHub también lo muestra bien. Los ejercicios en pseudocódigo son archivos `.frre`.

## Por dónde empezar

- **[💻 Algoritmos — Índice](💻%20Algoritmos%20—%20Índice.md)**: el mapa de la materia, tema por tema.
- **[CONTEXTO COMPLETO](CONTEXTO%20COMPLETO.md)**: qué hay en cada carpeta, de dónde salió y qué queda pendiente.

## Qué hay en cada carpeta

| Carpeta | Qué tiene |
|---|---|
| [`Teoría/`](Teoría) | La referencia de pseudocódigo de la cátedra: sintaxis, plantillas, errores y trampas, búsqueda e inserción en listas, y el Libro de Cátedra |
| [`Filminas de Cátedra/`](Filminas%20de%20Cátedra) | Las 13 presentaciones de teoría 2026, transcriptas íntegras (una sección por diapositiva), con los PDF originales y las erratas marcadas |
| [`Guía de Cátedra/`](Guía%20de%20Cátedra) | La guía de trabajos prácticos completa (275 ejercicios) y la teoría del sitio de la cátedra |
| [`Campus/`](Campus) | Material del aula virtual: apuntes de cátedra y el TEMA VI (Listas): presentaciones, ejemplos y el código del repositorio de la cátedra |
| [`Clases/`](Clases) | Transcripciones de las clases |
| [`Práctica/`](Práctica) | Ejercicios resueltos (`.frre`, con sus datos en `.datos/`), parciales, apuntes de clase y los ejercicios de Brisa, Peralta y Rojas |
| [`Trabajo Práctico/`](Trabajo%20Práctico) | Actividad Formativa 3 (Estación de Monitoreo) y el TP de C: el **Simulador Artemis** es un submódulo (repo de [Peralta-Luciano](https://github.com/Peralta-Luciano/Simulador-Artemis-Grupo-D9)) |
| [`Actividad N2 E-Comerce/`](Actividad%20N2%20E-Comerce) | Actividad Formativa 2: consigna, documentación y el código de Hextech Bazaar y RetroVerse |
| [`.claude/skills/`](.claude/skills) | El skill `pseudocodigo-utn` para Claude Code: la misma referencia de `Teoría/`, para escribir y revisar pseudocódigo con la notación de la cátedra |

## Clonar

El TP de C es un submódulo, así que para traerlo también:

```bash
git clone --recursive https://github.com/GonzaloRojas14/Algoritmos-y-Estructura-de-Datos-UTN-FRRe.git
```

(Si ya lo clonaste sin `--recursive`: `git submodule update --init`.)

## Correr el pseudocódigo

Los `.frre` se pueden ejecutar, con prueba de escritorio paso a paso, con la extensión de VS Code de la materia, que vive en su propio repo: [pseudocodigo_exe](https://github.com/GonzaloRojas14/pseudocodigo_exe). Los datos de cada ejercicio (archivos, secuencias, listas) están en la carpeta `<ejercicio>.datos/` que tiene al lado.

## Sobre el material

Las presentaciones, la guía, el libro y los apuntes son de la cátedra de Algoritmos y Estructuras de Datos de la UTN FRRe; acá están transcriptos y ordenados para estudiar. Donde el material original tiene un error, la transcripción lo deja tal cual y lo marca aparte (`[!bug] Errata`), sin corregirlo.
