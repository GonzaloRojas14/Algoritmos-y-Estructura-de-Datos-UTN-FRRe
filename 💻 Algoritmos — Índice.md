---
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
tags:
  - materia
  - AED
---

# 💻 Algoritmos y Estructura de Datos

> [!abstract] Qué es esta carpeta
> Todo el material de **AyED (UTN FRRe)**. Es la materia con más volumen del vault: teoría de cátedra, 7 clases grabadas con sus transcripciones, 60 ejercicios resueltos y un trabajo práctico de e-commerce.
> Lo que estaba en formatos que Obsidian no lee (`.txt`, `.py`, `.wav`) ahora tiene además una **versión Markdown legible**, con los originales intactos.

[[🏠 Inicio|← Volver al HQ]]

---

## 🧭 Cómo está organizado

| Carpeta | Qué contiene |
|---|---|
| 📂 **Filminas de Cátedra/** | 🆕 Las 13 presentaciones de teoría de 2026: **435 páginas** transcriptas, con los PDF originales |
| 📂 **Campus/TEMA VI — Listas/** | 🆕 Todo lo de la sección de Listas del campus: 4 presentaciones (114 diap.), el ejemplo de circular ordenada y el código de listas del repo de la cátedra → [[TEMA VI — Listas — Índice]] |
| 📂 **Guía de Cátedra/** | El sitio oficial completo: **275 ejercicios** + 5 páginas de teoría |
| 📂 **Teoría/** | La referencia de pseudocódigo de la cátedra — 6 notas (incluye listas y recursividad) |
| 📂 **Clases/** | 7 clases transcriptas completas + el PDF |
| 📂 **Práctica/** | 60 ejercicios resueltos + la guía de cátedra |
| 📂 **Trabajo Práctico/** | Actividad Formativa N.º 2 (los 2 e-commerce) y N.º 3 (Estación de Monitoreo) |

---

## 🎯 Qué entra en el segundo parcial

> [!danger] Anotado en clase
> **Corte de control, actualización y arreglos.**

| Tema | Teoría de cátedra | Filminas | Ejercicios |
|---|---|---|---|
| Corte de control | [[Corte de Control]] | — | [[2.2 — Archivos Secuenciales]] |
| Actualización | [[Actualización]] | — | [[2.3 — Archivos Indexados]] |
| Arreglos | [[Arreglos]] | [[4 — Arreglos]] · [[5 — Búsqueda y Ordenamiento]] · [[6 — Procesos Estadísticos]] | [[3 — Arreglos]] |

Las plantillas de los tres temas están en [[plantillas]].

---

## 🔗 Listas, recursividad y árboles

| Tema | Estado | Teoría y notación | Plantillas | Ejercicios |
|---|---|---|---|---|
| **Listas con punteros** | ✅ visto | ⭐ [[Listas — búsqueda e inserción]] (simple, doble y circulares, todo probado) · [[SINTAXIS]] §10 · [[Listas]] (teoría de la guía) · filminas [[7 — Listas (Introducción)]], [[8 — Listas (Inserción y Eliminación)]], [[9 — Pilas y Colas con Listas]] · campus [[TEMA VI — Listas — Índice]] (circulares) | [[plantillas]] §9 | [[4 — Listas]] · [[4 — Tratamiento de Listas]] · `Práctica/Clase 5 Listas.frre` |
| **Recursividad** | ✅ visto | [[SINTAXIS]] §11 (planteo formal de clase, prueba de escritorio) · filminas [[10 — Recursividad (Concepto)]], [[11 — Recursividad (Tipos y Ejemplos)]] | [[plantillas]] §10 | [[5 — Recursividad]] · `Práctica/Recursividad.frre` y sus dos archivos hermanos · [[Parcial 3 — el patrón de los ejercicios de listas]] |
| **Árboles** | ⏳ **pendiente** en la documentación — ya están las filminas | [[12 — Árboles (Conceptos y Recorridos)]] · [[13 — Árboles (ABB, AVL y B)]] · [[SINTAXIS]] "Árboles — pendiente" | — | [[5 — Recursividad]] §5.3 |

Lo que más se equivoca en estos temas está en [[errores-y-trampas]] (§A "Listas" y "Recursividad", §B.8).

---

## 📽️ Filminas de la cátedra — 13 presentaciones, 435 páginas

> [!success] Actualizado el 17/11/2026
> Las **presentaciones de teoría 2026** que el profesor subió a la carpeta *Presentaciones*, transcriptas íntegras página por página. Incluye lo que en el original eran imágenes: pseudocódigo, tablas, trazas, nodos y árboles. Las erratas están marcadas aparte, sin corregir el original.
>
> **→ [[📽️ Filminas de Cátedra — Índice]]** (ahí está la tabla de erratas y lo que la extensión todavía no acepta)

| # | Presentación | Págs. | Tema |
|---|---|---|---|
| 1-2 | [[1-2 — Introducción]] | 71 | Algoritmos, pseudocódigo, tipos de datos; acciones, asignación, operadores |
| 3 | [[3 — Secuenciales y Condicionales]] | 35 | Secuencial, SI, SI/SINO, SEGÚN, anidados |
| 4 | [[4 — Arreglos]] | 34 | Vectores, matrices, n dimensiones, carga y recorrido |
| 5 | [[5 — Búsqueda y Ordenamiento]] | 43 | Burbuja, selección, inserción; secuencial, centinela, binaria |
| 6 | [[6 — Procesos Estadísticos]] | 16 | Matriz con totalizadores, pseudocódigo y C |
| 7 | [[7 — Listas (Introducción)]] | 16 | Nodo, puntero, NUEVO, DISPONER |
| 8 | [[8 — Listas (Inserción y Eliminación)]] | 53 | Los 4 casos de inserción y eliminación, simples y dobles |
| 9 | [[9 — Pilas y Colas con Listas]] | 17 | Apilar, desapilar, encolar, desencolar |
| 10 | [[10 — Recursividad (Concepto)]] | 27 | Caso base, caso recursivo, pila de llamadas |
| 11 | [[11 — Recursividad (Tipos y Ejemplos)]] | 33 | Directa/indirecta, cola/cabeza, múltiple, anidada; recursión vs iteración |
| 12 | [[12 — Árboles (Conceptos y Recorridos)]] | 32 | Vocabulario, árbol binario con punteros, Pre/En/PostOrden |
| 13 | [[13 — Árboles (ABB, AVL y B)]] | 30 | Reconstrucción, ABB, AVL, árboles B y B+ |
| 14 | [[14 — Complejidad Algorítmica]] | 28 | Operaciones elementales, mejor/peor/medio, notación O |

---

## 📘 Guía de Trabajos Prácticos de la cátedra

> [!success] Nuevo — bajado el 24/08/2026
> Está transcripto íntegro el sitio **[aed-frre.github.io](https://aed-frre.github.io/)**: los enunciados de los **275 ejercicios** de la guía y las **5 páginas de teoría** que cubren corte de control, mezcla, actualización, arreglos y listas.
>
> **→ [[📘 Guía de Cátedra — Índice]]**
>
> Ahí están las consignas originales de los ejercicios que resolviste en [[Ejercicios Rojas]], con la misma numeración.

---

## 📖 Teoría y sintaxis del pseudocódigo

Esta es **la parte más importante para aprobar**: la cátedra tiene una notación propia y estricta.

Todo en 📂 **Teoría/**.

| Nota | Qué es | Estado |
|---|---|---|
| [[SINTAXIS]] | Referencia de teoría **y** notación, 15 secciones (fundamentos → complejidad), con listas (§10), recursividad (§11) y árboles marcados como pendientes. Teoría del libro Pinto & Bolatti 2026; notación verificada contra las plantillas oficiales | ✅ **Corregido y alineado** |
| [[sintaxis-completa]] | Sintaxis oficial derivada de las plantillas de cátedra (`isi-aed/Pseudocodigo/`), más punteros (§13) y recursividad (§14) | ✅ **Esta es la buena** |
| [[plantillas]] | 10 plantillas canónicas: secuencial, corte de control, mezcla inclusiva/exclusiva, actualización unitaria y por lotes, ABM indexado, secuencias, listas, recursividad | ✅ Se copian y adaptan, no se reinventan |
| [[errores-y-trampas]] | Catálogo de errores frecuentes, propios y de las fuentes de referencia | ✅ |
| [[SKILL — pseudocodigo-utn]] | Definición del skill `pseudocodigo-utn` que usa las tres referencias de arriba | — |

> [!success] SINTAXIS.md ya está corregido
> Tenía la notación deducida **del libro**, que en seis puntos contradice a las **plantillas
> oficiales** — y el parcial se corrige con las plantillas. Ya está alineado: `ESCRIBIR` (no
> `GRABAR`), `RE-ESCRIBIR` (no `REGRABAR`), `ABRIR /S(arch)`, `SI EXISTE ENTONCES`,
> `ELIMINAR(arch, reg)` y `PARA i := 1 HASTA 10, 1 HACER` con coma.
> La teoría quedó intacta; solo se corrigió notación y se agregaron referencias cruzadas.

> [!tip] Orden de autoridad — si dos fuentes se contradicen, gana la de arriba
> 1. **Plantillas oficiales** `isi-aed/Pseudocodigo/` → notación. Es lo que se pide en el parcial
> 2. **Libro** Pinto & Bolatti 2026 → teoría, conceptos, clasificaciones
> 3. **Resoluciones de alumnos** `AED26_Guia_Ejercicios` → solo como ejemplo, **tienen bugs**

---

## 🎙️ Clases grabadas — 7 clases

Grabadas en video, pasadas a audio y transcriptas con Whisper. **Las transcripciones están completas, sin resumir.**

| Clase | Transcripción | Palabras | Video original |
|---|---|---|---|
| 1 | [[Clase 1 — transcripción]] | 5.090 | `temp_videos/clase1.mp4` |
| 2 | [[Clase 2 — transcripción]] | 3.244 | `temp_videos/clase2.mp4` |
| 3 | [[Clase 3 — transcripción]] | 5.961 | `temp_videos/clase3.mp4` |
| 4 | [[Clase 4 — transcripción]] | 5.609 | `temp_videos/clase4.mp4` |
| 5 | [[Clase 5 — transcripción]] | 6.582 | `temp_videos/clase5.mp4` |
| 6 | [[Clase 6 — transcripción]] | 4.678 | `temp_videos/clase6.mp4` |
| 7 | [[Clase 7 — transcripción]] | 5.410 | `clase7.mp4` |

En la misma carpeta está [[Transcripciones-Clases.pdf]] — las mismas transcripciones exportadas a PDF.

> [!info] Por qué hay varias versiones de cada transcripción
> Los videos, audios y las pasadas intermedias están en `.material-crudo/Videos de clase (pipeline Whisper)/`, fuera de la vista de Obsidian. El pipeline de Whisper se corrió varias veces:
> - `claseN.txt` → primera pasada, transcripción cruda
> - `claseN_vad.txt` → con **VAD** (detección de voz) para cortar silencios
> - `claseN_strict.txt` → parámetros más estrictos contra alucinaciones
> - `final/claseN.txt` → **la versión buena**: pasada por `dedup.py`, que colapsa oraciones repetidas consecutivas (bucles de alucinación del modelo, no habla real)
>
> Las notas Markdown de la tabla salen de `final/`. Todo el material crudo se conserva. Ver [[🗺️ Mapa del Vault]].

---

## ✍️ Ejercicios resueltos — 60 archivos

Transcriptos íntegros a Markdown. Los originales `.txt` y `.py` se conservan en `.material-crudo/Repo AyED (git)/Practica/`.

Todo en 📂 **Práctica/**, junto con [[guia-aed-frre.pdf]] (guía de ejercicios de cátedra).

| Nota | Autor | Archivos | Qué tiene |
|---|---|---|---|
| [[Ejercicios Rojas]] | **Vos** | 26 | Los 3 enunciados de parcial, arreglos, registros, corte de control, indexados |
| [[Ejercicios Peralta]] | Peralta | 30 | El set más completo: cada ejercicio en `.txt` (pseudocódigo) **y** `.py` (Python ejecutable) |
| [[Ejercicios Brisaa]] | Brisa | 4 | Unidad 1.1, secuencias |
| [[Clase 1 — apuntes de arreglos]] | **Vos** | 1 | 🆕 Apuntes de la clase de arreglos: teoría, `ej_3.2` y `ej_3.4`, con las erratas corregidas |
| [[Clase 2 — apuntes de procesos estadísticos]] | **Vos** | 1 | 🆕 Apuntes de la clase de procesos estadísticos: el algoritmo `ESTAD` (ventas × sucursales × rubros), reconstruido y corregido |
| `Clase 5 Listas.frre` | **Vos** | 1 | Apuntes de la clase de listas: nodo, punteros, cargas apilada y encolada |
| `Recursividad.frre` + `— prueba de escritorio` + `— dígitos impares` | **Vos** | 3 | 🆕 Recursividad: teoría, ejercicios de clase pasados en limpio, prueba de escritorio paso a paso y dígitos impares |
| `Parcial 3 …` (5 `.frre`) + [[Parcial 3 — el patrón de los ejercicios de listas]] | **Vos** | 6 | 🆕 Los ejercicios de listas de los modelos de tercer parcial 2025 (Tema A, Tema B, Empresa) resueltos, y **el patrón común** para encararlos |

> [!tip] Los parciales
> Dentro de [[Ejercicios Rojas]] están `Parcial.1.txt`, `Parcial.2.txt` y `Parcial.3.txt`. El primero es el de la cadena de hoteles: dos secuencias de entrada (caracteres y enteros), generar secuencia de salida filtrada e informar máximo por hotel. Es el formato típico de parcial de la materia.

---

## 🛒 Actividad Formativa N.º 2 — e-Commerce con IA

Trabajo práctico: diseñar un e-commerce usando IA. Hay **dos proyectos completos** hechos en Next.js.

En 📂 **Trabajo Práctico/**:

| Documento | Qué es |
|---|---|
| [[Actividad Formativa N.º 2 – Diseñando un e-Commerce con Inteligencia Artificial.pdf]] | La consigna |
| [[Hextech Bazaar - Documentacion Actividad N2.pdf]] | Documentación del proyecto 1 |
| [[RetroVerse - Documentacion Actividad N2.pdf]] | Documentación del proyecto 2 |

> [!note] El código está fuera del vault
> Los dos proyectos Next.js (33 subcarpetas, 160 imágenes de assets) viven en
> `.material-crudo/Repo AyED (git)/Actividad N2 E-Comerce/`. El repo quedó **entero e intacto**,
> con su historial de git. Se abre normal con VS Code.

---

## 🌡️ Actividad Formativa N.º 3 — Estación de Monitoreo

En 📂 **Trabajo Práctico/AF3 - Estación de Monitoreo/**: la consigna, el generador de datos en
Python, los CSV, el pseudocódigo y el PDF de entrega (`AF3 - Estación de Monitoreo - Rojas Gonzalo.pdf`).

---

## 📕 Guías en PDF

- [[guia-aed-frre.pdf]] — guía de ejercicios de la cátedra (en `Ejercicios Git.Io/`)
- [[Transcripciones-Clases.pdf]] — las 7 clases en un solo PDF

---

## 🧰 Otros skills que hay en el repo

En `.claude/skills/` hay dos skills que **no son de esta materia**, quedaron guardados ahí:
- `snowflake-data-modeling` — modelado de datos en Snowflake
- `synthwave-ecommerce-design` — diseño visual synthwave (se usó para el e-commerce)

---

## 🔎 Todo lo de AED

```dataview
TABLE WITHOUT ID file.link AS "Nota", file.folder AS "Carpeta"
FROM #AED
SORT file.name ASC
```
