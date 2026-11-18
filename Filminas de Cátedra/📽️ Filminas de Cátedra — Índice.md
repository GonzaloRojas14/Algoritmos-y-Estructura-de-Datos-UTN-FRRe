---
tipo: indice
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
tags:
  - AED
  - filminas
  - moc
---

# 📽️ Filminas de Cátedra — Índice

> [!abstract] Qué hay acá
> Las **presentaciones de teoría** que el profesor subió a la carpeta *Presentaciones* (OneDrive de la cátedra, AED 2026), transcriptas **íntegras** a Markdown: 13 presentaciones, 435 páginas, sin resumir. Hay una sección por página del PDF.
> Son la fuente más cercana a lo que se toma en el parcial, después de las plantillas de pseudocódigo. Lo que dicen las filminas **no se corrige**: los errores se marcan aparte en callouts `[!bug]`.

[[💻 Algoritmos — Índice|← Volver a la materia]]

---

## 📑 Las presentaciones

| # | Nota | Págs. | Tema |
|---|---|---|---|
| 1-2 | **[[1-2 — Introducción]]** | 71 | TEMA I: qué es un algoritmo, características, sistemas, pseudocódigo (nombre/ambiente/proceso), tipos de datos, variables y constantes. TEMA II: acciones, asignación, Escribir/Leer, operadores aritméticos, relacionales y lógicos |
| 3 | **[[3 — Secuenciales y Condicionales]]** | 35 | Estructuras de control: secuencial, condicional simple, alternativa (SI/SINO), múltiple (SEGÚN) y anidadas, con equivalentes en Python |
| 4 | **[[4 — Arreglos]]** | 34 | Definición F-H-O, memoria interna/externa, vectores, matrices y arreglos de n dimensiones, carga y recorrido con PARA y con MIENTRAS/centinela, recorrido por filas y por columnas, errores comunes |
| 5 | **[[5 — Búsqueda y Ordenamiento]]** | 43 | Burbuja (y con bandera), Selección, Inserción; búsqueda Secuencial (y con corte), Centinela (desordenado/ordenado) y Binaria; comparativas |
| 6 | **[[6 — Procesos Estadísticos]]** | 16 | Cuadro estadístico: ventas sucursal × rubro en una matriz 6×8 con totalizadores, acción ESTAD, del pseudocódigo a C. Anexos: [[estadistico.c]] y [[ventas.csv]] |
| 7 | **[[7 — Listas (Introducción)]]** | 16 | Qué es una lista, clasificación (particularizadas y generalizadas), nodo y puntero, `*p` / `p^`, alias con `p := q`, NUEVO y DISPONER |
| 8 | **[[8 — Listas (Inserción y Eliminación)]]** | 53 | Inserción ordenada y eliminación en listas simples y dobles: búsqueda con ANT/P, los 4 casos de cada operación, DISPONER |
| 9 | **[[9 — Pilas y Colas con Listas]]** | 17 | Pila y cola sobre una lista simple (TOPE, FRENTE, FINAL): apilar, desapilar, encolar, desencolar, todas O(1) |
| 10 | **[[10 — Recursividad (Concepto)]]** | 27 | Caso base y caso recursivo, 3 pasos de diseño, Factorial iterativo y recursivo, pila de llamadas, las tres preguntas, recursión infinita, Potencia |
| 11 | **[[11 — Recursividad (Tipos y Ejemplos)]]** | 33 | Directa e indirecta (EsPar/EsImpar), de cola, de cabeza, múltiple (Fibonacci), anidada (Ackermann); ContarDig, SumarDig, SumarVec, BusBin; recursión vs iteración |
| 12 | **[[12 — Árboles (Conceptos y Recorridos)]]** | 32 | Definición recursiva, vocabulario (raíz, hoja, grado, nivel, altura, rama), árbol binario con punteros, PreOrden/EnOrden/PostOrden, Contar |
| 13 | **[[13 — Árboles (ABB, AVL y B)]]** | 30 | Reconstruir un árbol con pre+en o post+en, árbol de expresión, equilibrado y completo, ABB (Buscar recursivo, Insertar iterativo), AVL y factor de equilibrio, árboles B y B+ |
| 14 | **[[14 — Complejidad Algorítmica]]** | 28 | Complejidad espacial y temporal, operaciones elementales, mejor/peor/caso medio, notación O, órdenes, sumatorias y bucles anidados |

> [!warning] Falta una presentación
> En la carpeta del profesor los archivos de listas van `01`, `02` y `04`: **no hay `03`**. El cierre de [[8 — Listas (Inserción y Eliminación)]] anuncia "Próxima clase: Recorridos y Listas Circulares", así que probablemente es esa. Si aparece, va como nota nueva entre la 8 y la 9.

> [!info] Numeración de páginas
> Muchas filminas repiten una diapositiva con el código ampliado. Las notas van **por página del PDF**, así que a partir de cierto punto el número de sección no coincide con el pie de la filmina. Cada nota lo aclara.

---

## 🧭 Cómo leerlas — el hilo

```
1-2 INTRODUCCIÓN ──► 3 ESTRUCTURAS DE CONTROL
                              │
                              ▼
                        4 ARREGLOS ──► 5 BÚSQUEDA Y ORDENAMIENTO
                              │
                              └──► 6 PROCESOS ESTADÍSTICOS (arreglos + archivos)

7 LISTAS ──► 8 INSERCIÓN/ELIMINACIÓN ──► (03 circulares, falta) ──► 9 PILAS Y COLAS
                                                                        │
10 RECURSIVIDAD ──► 11 TIPOS Y EJEMPLOS ─────────────────────────────────┤
                                                                        ▼
                                  12 ÁRBOLES ──► 13 ABB, AVL y B
                                  (recorridos recursivos + nodos con punteros)

14 COMPLEJIDAD ── sirve para comparar todo lo anterior
```

---

## ✅ De dónde salió cada nota

Todas salen de los PDF de la carpeta `PDF originales/` (bajados el 17/11/2026). Se transcribieron página por página, mirando cada una renderizada para respetar tablas, tarjetas y diagramas. Los diagramas que se pueden escribir en texto (nodos y punteros, pilas de llamadas, árboles chicos, trazas) están en ASCII o en tablas. Los que no, están recortados en `img/` con el prefijo de su nota.

| Nota | PDF original |
|---|---|
| 1-2 | `TEMA 1_2 - INTRODUCCIÓN.pdf` (en realidad son dos presentaciones: TEMA I y TEMA II) |
| 3 | `TEMA 3-Secuenciales_Condicionales.pdf` |
| 4 | `Arreglos_Clase1_Fundamentos_2.pdf` |
| 5 | `Arreglos_Clase2_BusquedaYOrdenamiento_2.1.pdf` |
| 6 | `Procesos_Estadisticos_2026_2.pdf` + `estadistico.c` + `ventas.csv` (el `.c` compila y da las cifras de la filmina) |
| 7 · 8 · 9 | `01_Listas_Introduccion_2.pdf` · `02_Listas_Insercion_Eliminacion_3.1.pdf` · `04_Pilas_Colas_Listas_Simples_2.pdf` |
| 10 · 11 | `05_Recursividad_Clase1_Concepto_Rev1.pdf` · `05_Recursividad_Clase2_Tipos_y_Ejemplos_Rev_1.pdf` |
| 12 · 13 | `06_Arboles_Clase1_Conceptos_y_Recorridos_1.pdf` · `06_Arboles_Clase2_ABB_AVL_y_B_Rev_1.pdf` |
| 14 | `07_Complejidad_Algoritmica.pdf` |

> [!info] Versiones anteriores
> Las notas 4, 5 y 6 reemplazan a las transcripciones de las presentaciones viejas (Google Slides y el PDF de 13 páginas), que quedaron en `versión anterior/`: [[4 — Arreglos (versión anterior)]], [[5 — Búsqueda y Ordenamiento (versión anterior)]], [[6 — Procesos Estadísticos (versión anterior)]]. Cada nota nueva tiene un callout con lo que cambió. Las erratas viejas (índices 0..7, `suma` sin declarar, `DIV 2 DIV 2`, `M[51,J]`) ya no están en las versiones nuevas.

---

## ⚠️ Erratas detectadas en las filminas

Están verificadas a mano (trazas, recorridos, enganches de punteros). En cada nota aparecen como `[!bug]` en la diapositiva correspondiente.

| Dónde | Qué está mal |
|---|---|
| [[1-2 — Introducción]] · 24 | `cantcar` sin declarar; compara con `""` en vez del blanco `" "`; el ciclo que saltea blancos no controla `NFDS` |
| [[1-2 — Introducción]] · 18, 37, 38, 64 | Detalles: título repetido, "pedios"/"constates", portada del TEMA II dice 2025, salida "Suma> >> 29" |
| [[3 — Secuenciales y Condicionales]] · 25 | Con empate muestra "Instagram es más usada" |
| [[3 — Secuenciales y Condicionales]] · 30 | Casos `<18` y `<50` superpuestos; con 50 años el pseudocódigo y el Python dan resultados distintos |
| [[3 — Secuenciales y Condicionales]] · 32 | `num` sin declarar; declara `user`/`followers` que no usa |
| [[4 — Arreglos]] · 21, 25 | Parámetro **sin nombre** `(arreglo [1..50] de entero)` y el cuerpo usa `v` |
| [[5 — Búsqueda y Ordenamiento]] · 29–30 | **Secuencial ordenada nunca encuentra nada**: el `SI v[i]=buscado` está dentro del `MIENTRAS … v[i]<buscado`. Va después del `FIN_MIENTRAS` |
| [[5 — Búsqueda y Ordenamiento]] · 38–39 | Binaria: `SI encontrado` usa una variable que no existe; va `SI v[medio]=x` |
| [[5 — Búsqueda y Ordenamiento]] · 26, 31, 32, 36, 41 | Las lecturas de Secuencial vs. Centinela se contradicen entre diapositivas |
| [[7 — Listas (Introducción)]] · 10 | `P` y `p` declaradas en el mismo Ambiente (son la misma variable) |
| [[8 — Listas (Inserción y Eliminación)]] · 11, 24, 37, 49 | Falta `AMBIENTE` antes del `NODO` |
| [[8 — Listas (Inserción y Eliminación)]] · 51 | Eliminación doble: falta el `SINO` después de "NO SE ENCUENTRA" → `DISPONER` con P en NIL |
| [[8 — Listas (Inserción y Eliminación)]] · 22, 28, 49 | Leyendas: nombra ANT en la doble; comparaciones con la simple que no cierran |
| [[9 — Pilas y Colas con Listas]] · 6 | `NODO` declarado solo dentro de APILAR |
| [[9 — Pilas y Colas con Listas]] · 14 | DESENCOLAR: al `SI (FRENTE=NIL)` interno le falta su `FIN SI` |
| [[13 — Árboles (ABB, AVL y B)]] · 19 | `Insertar` usa `Q`, `P`, `ANT` (y el proceso `x`) sin declararlos |
| [[14 — Complejidad Algorítmica]] · 12, 14 | `n` sin declarar; "no está (o está al final)" mezcla dos casos con distinto costo |

> [!tip] Lo que **no** es errata (y por eso no está marcado)
> - Mezclar mayúsculas en un nombre (`a`/`A`, `Dinero`/`dinero`): el pseudocódigo no distingue mayúsculas.
> - Que cada filmina cierre distinto (`FIN_SI`, `Fin Si`, `FinSi`, `FIN SI;`; `Fin;`, `FinAccion.`, `FIN ACCION.`): todas aparecen en material de cátedra y se pueden mezclar. Ver [[SINTAXIS]].
> - Que no aparezca `var`: **ninguna** filmina de listas, recursividad o árboles lo usa, aunque modifican `PRIM`, `TOPE` o `RAIZ`. La guía sí lo usa. En [[9 — Pilas y Colas con Listas]] quedó como aviso.
> - Recursividad (10 y 11) y los recorridos, reconstrucciones, AVL y árboles B (12 y 13) se verificaron enteros y no tienen errores.

---

## 🛠️ Notación de las filminas y la extensión `aed-vscode`

Se pasaron por el verificador de la extensión los 84 bloques de código que son programas o subprogramas completos, y además un programa de árboles armado con el código exacto de las filminas 12 y 13.

**Ya funciona** (sin cambios): `Funcion F(...): tipo;` … `Fin;` (con o sin `Ambiente` propio) · `Procedimiento P(...);` · `CONTRARIO` · `FinSi`, `FIN SI;`, `FinMientras`, `FIN MIENTRAS;` · `FIN REGISTRO;`, `Fin_Reg;`, registro anidado · `FIN ACCION.`, `Fin_Accion.` · parámetros escritos después de `ES` · `{ comentarios }` y `//` · recursión indirecta · `*(*P.ant).prox` · `archivo de … ordenado por`, `Abrir E`, `No FDA`. El árbol de las filminas corre bien: PreOrden, EnOrden, PostOrden, Contar y Buscar dan lo que dicen las diapositivas.

**Todavía no lo acepta**:

| Forma | Dónde aparece | Qué hace hoy la extensión |
|---|---|---|
| `Accion X ES;` (punto y coma después de `ES`) | 4, 5, 6, 10, 11, 12, 13 — es **la forma habitual** de las filminas nuevas | Error: no reconoce el `Ambiente` que sigue |
| `NILL` | 10, 11, 12, 13 (siempre con doble L) | Error: "NILL no está declarada" |
| `SI_NO` | 5 | Error: lo toma como un procedimiento |
| `SINO SI … FIN SI` con un solo cierre | 8 | Error: falta un `FIN_SI` |
| tipos `numérico` / `alfanumérico` | 1-2, 3 | Error: tipo no declarado |
| `Subaccion X Es … FinSubaccion` sin `Proceso` | 1-2 | Error |
| arreglo como parámetro con límite `n` sin declarar: `(v: arreglo [1..n] de entero)` | 5 (todos los algoritmos) | Error: el límite tiene que ser constante |

Ver también [[errores-y-trampas]] · [[sintaxis-completa]] · [[plantillas]].

---

## 🔗 A dónde seguir

- [[3 — Arreglos]] — los ejercicios de la Guía de Cátedra sobre arreglos
- [[Arreglos]] — la página de teoría del sitio de la cátedra
- [[Clase 1 — apuntes de arreglos]] — tus apuntes de clase sobre arreglos
- [[sintaxis-completa]] · [[plantillas]] · [[SINTAXIS]] — la notación de referencia

---

## 📂 Todo lo de esta carpeta

```dataview
TABLE WITHOUT ID file.link AS "Nota", unidad AS "#", diapositivas AS "Páginas"
FROM #filminas
SORT unidad ASC
```
