---
tipo: indice
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
tema: "TEMA VI: Listas"
tags:
  - AED
  - campus
  - listas
  - moc
---

# TEMA VI — Listas — Índice

> [!abstract] Qué hay acá
> Todo el material de la sección **TEMA VI: Listas** del campus (frre.cvg.utn.edu.ar, curso ISI_Aed), bajado el 17/11/2026 y pasado a Markdown: 4 presentaciones (114 diapositivas), el ejemplo de lista circular ordenada y el código de listas del repositorio de la cátedra.
> Complementa las filminas 2026 ([[7 — Listas (Introducción)]], [[8 — Listas (Inserción y Eliminación)]], [[9 — Pilas y Colas con Listas]]). Lo que **solo** está acá es lo de **listas circulares**.

[[💻 Algoritmos — Índice|← Volver a la materia]] · [[📽️ Filminas de Cátedra — Índice|Filminas 2026]]

---

## 📘 Lo que dice la sección del campus

> **Subunidad C: Listas Lineales**
> En esta parte del recorrido vamos a adentrarnos en una de las estructuras dinámicas más importantes en programación: las listas.
> Aprenderemos cómo se organizan y acceden los datos en una lista, cuáles son sus tipos (particularizadas y generalizadas) y qué ventajas ofrecen frente a otras estructuras como los arreglos.
> También incorporaremos un nuevo concepto clave: el puntero, que nos permitirá trabajar con listas de manera flexible y dinámica, gestionando la memoria de forma eficiente.
> En esta subunidad veremos:
> - Clasificación de las Listas Lineales
> - Organización y acceso a los elementos
> - Listas Particularizadas y Generalizadas
> - Concepto de restricción y noción de puntero
> - Operaciones básicas: recorrido, inserción y eliminación
>
> Te invitamos a explorar los materiales, analizar los ejemplos de código y practicar las operaciones para dominar el manejo de listas.

La sección también tiene la **Actividad Formativa 4 — Listas** (cuestionario, abre el viernes 20/11/2026). No se abrió ni se bajó.

---

## 📑 Las notas

| Nota | En el campus | Qué tiene |
|---|---|---|
| **[[3.01 — Listas Simplemente Enlazadas]]** · 76 diap. | "Presentación a LISTAS SIMPLEMENTE ENLAZADAS" | Estructuras dinámicas, ordenadas vs. desordenadas, punteros internos y externos, clasificación, los 4 casos de inserción y de eliminación, un programa en C, búsqueda y recorrido. Las diapositivas 37 a 76 son restos de la plantilla, sin contenido |
| **[[3.02 — Listas Doblemente Enlazadas y Circulares]]** · 20 diap. | "Presentación a LISTAS DOBLEMENTE ENLAZADAS Y CIRCULARES" | Ambiente simple vs. doble, recorridos hacia adelante y hacia atrás, borrado en doble; circulares: definición, **búsqueda** y etapas de la inserción |
| **[[3.03 — Pilas y Colas]]** · 6 diap. | "Presentación a LISTAS PARTICULARIZADAS" | Pila (LIFO) con PUSH/POP y cola (FIFO) con InsertaCola/EliminaCola |
| **[[12 — Listas Parte II (Cómo borrar en listas simples)]]** · 12 diap. | "Cómo Borrar en Listas Simples" | Los 4 casos de eliminación en simples, la búsqueda con ANT/P y la acción ELIM |
| **[[Ejemplo — Carga ordenada de lista circular simple]]** | carpeta "Ejemplo de carga ordenada de una lista circular simple" | El único pseudocódigo de cátedra que **inserta ordenado en una circular**. Tiene dos errores de lógica, probados con ejemplos |
| **[[Repo isi-aed — Listas (C, Python y pseudocódigo)]]** | "Repo de código de AED" (GitHub `UTN-FRRe/isi-aed`) | Las 10 operaciones en C y Python: simple, doble, **simple circular y doble circular** (inserción ordenada y eliminación), pila y cola. Cada una con su traducción al pseudocódigo, probada en la extensión |

Los originales están en `originales/`: las 4 presentaciones como PDF (generadas desde la versión publicada) y el `.docx`. El código del repo, tal cual, está en `repo isi-aed/`.

---

## 🔁 Listas circulares: qué hay y dónde

Es el tema con menos material de cátedra: la presentación 2026 de circulares (la `03`) no está en la carpeta del profesor.

| Operación | Simple circular | Doble circular |
|---|---|---|
| **Recorrer / listar** | guía (`LISTA_CIRCULAR`, en [[SINTAXIS]] §10) · repo `Pseudocodigo/LISTA_CIRC` | repo (`DOBLE_CIRC_*`) |
| **Buscar** | guía · [[3.02 — Listas Doblemente Enlazadas y Circulares]] diap. 17 (la 16 tiene un error) | repo |
| **Insertar ordenado** | repo `SIMPLE_CIRC_INS` (✅ correcto) · [[Ejemplo — Carga ordenada de lista circular simple]] (❌ con errores) | repo `DOBLE_CIRC_INS` (✅ correcto) |
| **Insertar sin orden** | guía: en el 2º lugar · 3.02 diap. 19: al final (le falta un enganche) | — |
| **Eliminar** | guía (3 casos) · repo `SIMPLE_CIRC_DEL` | repo `DOBLE_CIRC_DEL` (❌ no termina si el valor no está) |

La idea que se repite en todos: **el recorrido corta cuando el siguiente es el primero** (`*P.prox <> PRIM`), no en `NIL`. Al terminar, el puntero queda **parado en el último nodo, que no se comparó**: hay que mirarlo aparte. Y cualquier cambio del primero obliga a tocar **el último**, que es el que lo apunta.

---

## ⚠️ Erratas detectadas

| Dónde | Qué está mal |
|---|---|
| [[3.01 — Listas Simplemente Enlazadas]] · 24 | Usa `*Q.DATO` sin `NUEVO(Q)`; `Q` y `ANT` sin declarar; el registro no tiene campo `DATO` |
| [[3.01 — Listas Simplemente Enlazadas]] · 30–31 | Eliminar del medio y del final: dice `ANT:=*P.prox` en vez de `*ANT.prox := *P.prox` (la filmina 8 de 2026 lo tiene bien) |
| [[3.02 — Listas Doblemente Enlazadas y Circulares]] · 9 | Borrado en doble: 5 `Si` y 4 `Fsi`; con un único nodo no ejecuta `DISPONER` |
| [[3.02 — Listas Doblemente Enlazadas y Circulares]] · 16 | Búsqueda en circular: `T := PRIM` y `Mientras (T <> PRIM)` → el ciclo no entra nunca. La 17 es la corregida |
| [[3.02 — Listas Doblemente Enlazadas y Circulares]] · 19 | Etapas de inserción en circular: falta enganchar el viejo último al nuevo |
| [[3.03 — Pilas y Colas]] · 5 | `Q` sin declarar en InsertaCola |
| [[12 — Listas Parte II (Cómo borrar en listas simples)]] · 12 | `NUEVO(Q); LEER(*Q.DATO)` dentro de la eliminación, sin sentido y con `Q` sin declarar |
| [[Ejemplo — Carga ordenada de lista circular simple]] | `M` sin declarar; llama a `CARGAR-NODO` pero se llama `CARGA-NODO`; **`INSERCION-PREVIA` pierde el nodo**; **el último no se compara** (10, 30, 20 queda 10 → 30 → 20) |
| [[Repo isi-aed — Listas (C, Python y pseudocódigo)]] | `libera_lista` de las circulares simples en C se cae con lista vacía; **`DOBLE_CIRC_DEL` no termina si el valor no está** y borra mal el último (en C); `SIMPLE_DEL.py` no arranca (`try` sin `except`); `LISTA_CIRC` no controla `PRIM = NIL` |

---

## 🛠️ Notación nueva para la extensión

- **`^` como "Y"** (el ∧ de la lógica): `MIENTRAS (P <> NIL) ^ (*P.DATO < *Q.DATO) HACER` (3.01 y Parte II). ❌ **La extensión hoy lo toma como potencia** (avisa "la potencia se escribe `**`") y la condición falla. Pendiente.
- **`Q^.dato`** (Pascal) en pilas (3.03): ya está documentado como `p^.dato` en [[SINTAXIS]] §10.
- **`P*.DATO`** (asterisco después del puntero) en el ejemplo de la circular: es la forma de los Complementos 2026. ✅ La extensión ya lo acepta.
- **Subacciones con `ACCION X ES … FIN ACCION`** dentro de otra acción, y `MIENTRAS` sin `HACER`, en el ejemplo de la circular.
