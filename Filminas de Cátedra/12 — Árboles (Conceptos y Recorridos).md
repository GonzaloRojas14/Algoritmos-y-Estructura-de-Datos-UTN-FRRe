---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 12
titulo_original: Árboles — Clase 1 · Conceptos, árbol binario y recorridos
archivo_original: 06_Arboles_Clase1_Conceptos_y_Recorridos_1.pdf
diapositivas: 32
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - arboles
  - punteros
  - recursividad
---

# 12 — Árboles (Conceptos y Recorridos)

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 32 páginas de **Árboles — Clase 1 · Conceptos, árbol binario y recorridos** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[06_Arboles_Clase1_Conceptos_y_Recorridos_1.pdf]] (carpeta `PDF originales/`).
> El PDF tiene 27 diapositivas numeradas más 5 páginas que repiten el código ampliado (pie de página 14, 18, 19, 20 y 23). Acá cada página del PDF es una sección, así que la numeración de las secciones no coincide con el número del pie a partir de la página 15.
> La cátedra escribe `NILL` (con doble L) y accede a los campos con `*p.campo`. Se respetó tal cual.

Sigue en [[13 — Árboles (ABB, AVL y B)]].

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

# Árboles

Clase 1 · Conceptos, árbol binario y recorridos

*Terminología · Representación con punteros · Pre-orden, En-orden, Post-orden*

---

## 2 · Objetivos de la clase

**OBJETIVOS DE LA CLASE**

### ¿Qué vamos a aprender hoy?

1. **Qué es un árbol**
   Una estructura homogénea, dinámica y no lineal, con definición recursiva.
2. **Su vocabulario**
   Raíz, padre, hijo, hoja, grado, nivel, altura, camino, rama…
3. **El árbol binario**
   Cómo se declara con punteros y cómo queda en memoria.
4. **Cómo se recorre**
   Pre-orden, En-orden y Post-orden: tres subacciones recursivas.

---

## 3 · De las listas a los árboles

**PUNTO DE PARTIDA**

### De las listas a los árboles

**LISTA · lineal**

```
 [5] ──→ [8] ──→ [3] ──→ [9]
```

Cada nodo tiene un solo sucesor.

**ÁRBOL · no lineal**

```
          5
        /   \
       8     3
      / \     \
     1   4     9
```

Cada nodo puede tener más de un sucesor.

> [!question] Pregunta
> ¿cómo representamos una jerarquía, como carpetas dentro de carpetas?

---

## 4 · ¿Qué es un árbol?

**CONCEPTO CENTRAL**

### ¿Qué es un árbol?

> [!important] Definición
> Un árbol es una estructura de datos **homogénea, dinámica y no lineal**.

| **Homogénea** | **Dinámica** | **No lineal** |
|---|---|---|
| Todos sus elementos (nodos) son del mismo tipo de dato. | Puede cambiar su forma y su cantidad de nodos en tiempo de ejecución. | Cada elemento puede tener más de un sucesor. |

*Lo nuevo respecto de las listas es la tercera: la estructura deja de ser una fila.*

---

## 5 · Una definición recursiva

**UNA DEFINICIÓN RECURSIVA**

### Un árbol está hecho de árboles

> [!important] Definición
> Un árbol de tipo T es la concatenación de un elemento de tipo T, llamado **raíz**, con un número finito de árboles disjuntos, llamados **subárboles**.

> [!info] Caso base
> El árbol vacío también es un árbol.

> [!info] Caso recursivo
> Raíz + subárboles, que a su vez son árboles.

```
            raíz
          /  |  \
         /   |   \
       /\   /\   /\
      /T1\ /T2\ /T3\
      ‾‾‾‾ ‾‾‾‾ ‾‾‾‾
```

*Cada Tᵢ es, a su vez, un árbol.*

---

## 6 · ¿Dónde aparecen los árboles?

**APLICACIONES**

### ¿Dónde aparecen los árboles?

| | |
|---|---|
| **Sistema de archivos** — Carpetas que contienen carpetas y archivos. | **Organigramas** — Jerarquías de una empresa o un árbol genealógico. |
| **Expresiones** — Los compiladores arman un árbol para evaluar (a + b) * c. | **Índices** — Bases de datos y archivos indexados usan árboles B y B+. |

**Ejemplo: un sistema de archivos**

```
              /
           /  |  \
       home  etc  usr
       /  \         \
     ana  luis      bin
```

---

## 7 · Vocabulario I

**VOCABULARIO I**

### Raíz, padre, hijo, hermanos, hoja e interior

```
                  A   ← raíz
              /   |   \
             B    C    D
            / \       / | \
           E   F     G  H  I
               |
               J

   B: interior · C: hoja · E: hoja
```

*(En el dibujo, A —la raíz— está resaltada en naranja y las hojas C y E en verde; B lleva la etiqueta "interior".)*

- **Raíz:** El único nodo que no tiene padre. Todo árbol no vacío tiene una sola.
- **Padre / hijo:** X es hijo de Y si Y apunta a X. Ej.: B es padre de E; E es hijo de B.
- **Hermanos:** Nodos con el mismo padre. Ej.: G, H e I.
- **Hoja (terminal):** Nodo sin hijos. Ej.: E, J, C, G, H, I.
- **Interior:** Nodo que no es raíz ni hoja. Ej.: B, F, D.

---

## 8 · Vocabulario II

**VOCABULARIO II**

### Grado, nivel y altura

![[arbol1-grado-nivel-altura.png]]

*El mismo árbol de la diapositiva anterior, con las franjas de nivel y el grado anotado en A, B, D y F.*

```
Nivel 1                 A            ← grado 3
                     /  |  \
Nivel 2             B   C   D        ← B: grado 2 · D: grado 3
                   / \     / | \
Nivel 3           E   F   G  H  I    ← F: grado 1
                      |
Nivel 4               J
```

| | |
|---|---|
| **Grado de un nodo** | Cantidad de hijos (descendientes directos). |
| **Grado del árbol** | El mayor grado entre todos sus nodos → 3. |
| **Nivel** | Raíz = nivel 1; cada hijo, uno más. |
| **Altura** | El máximo nivel de todos los nodos → 4. |

---

## 9 · Vocabulario III

**VOCABULARIO III**

### Camino, rama, longitud de camino y bosque

![[arbol1-camino-rama.png]]

*Árbol de 50 con la rama 50 – 17 – 12 – 9 resaltada en naranja.*

```
              50
            /    \
          17      72
         /  \    /  \
       12    23 54   76
      /  \
     9    14

   Rama: 50 – 17 – 12 – 9
```

- **Camino:** Secuencia de nodos donde dos consecutivos son padre e hijo. Ej.: 17 – 12 – 14.
- **Rama:** Camino desde la raíz hasta una hoja.
- **Longitud de camino de X:** Nodos que se recorren desde la raíz hasta X: raíz 1, sus hijos 2… El 9 tiene longitud 4.
- **Bosque:** Conjunto (normalmente ordenado) de uno o más árboles.

---

## 10 · Ejercicio en clase

**EJERCICIO EN CLASE**

### Lo identificamos sobre el árbol

```
            M
          /   \
         R     K
         |   / | \
         T  P  Q  S
              / \
             W   X
```

1. ¿Cuál es la raíz?
2. ¿Cuáles son las hojas?
3. ¿Cuáles son nodos interiores?
4. ¿Quiénes son hermanos de Q?
5. ¿Cuál es el grado de K? ¿Y el del árbol?
6. ¿Cuál es la altura del árbol?
7. ¿Cuál es la rama que llega a X?

---

## 11 · Ejercicio en clase — Solución

**EJERCICIO EN CLASE**

### Solución

```
            M
          /   \
         R     K
         |   / | \
         T  P  Q  S
              / \
             W   X
```

1. **Raíz:** `M`
2. **Hojas:** `T, P, W, X, S`
3. **Interiores:** `R, K, Q`
4. **Hermanos de Q:** `P y S`
5. **Grado de K / del árbol:** `3 / 3`
6. **Altura:** `4`
7. **Rama hasta X:** `M – K – Q – X`

---

## 12 · Dos cálculos útiles

**DOS CÁLCULOS ÚTILES**

### Amplitud y cantidad total de nodos

| **Amplitud (anchura)** | **Total de nodos** |
|---|---|
| Cantidad de nodos del nivel más poblado (el último, si está completo). | Cantidad total de nodos de un árbol completo de n niveles. |
| `A(n) = g^(n − 1)` | `T(n) = (g^n − 1) / (g − 1)` |
| Ejemplo: grado 3 y 3 niveles | Ejemplo: grado 3 y 4 niveles |
| `A(3) = 3² = 9` | `T(4) = (81 − 1) / 2 = 40` |

*Ambas suponen que el árbol está completo: todos los nodos con el máximo de hijos.*

---

## 13 · Tipos de árboles

**TIPOS DE ÁRBOLES**

### Según la cantidad máxima de hijos

| **BINARIO** | **TERNARIO** | **N-ARIO** |
|---|---|---|
| Cada nodo tiene, a lo sumo, un hijo izquierdo y un hijo derecho. | Cada nodo tiene, como máximo, tres hijos: izquierdo, medio y derecho. | Cada nodo puede tener cualquier cantidad de hijos. |

```
  BINARIO        TERNARIO        N-ARIO

     ●              ●               ●
    / \           / | \         / / | \ \
   ●   ●         ●  ●  ●       ● ●  ●  ● ●
```

---

## 14 · Árbol binario — Definición y declaración en pseudocódigo

**ÁRBOL BINARIO**

### Definición y declaración en pseudocódigo

> [!important] Definición
> Un árbol binario es una raíz más **dos árboles binarios disjuntos**: el subárbol izquierdo y el subárbol derecho. El árbol vacío también es un árbol binario.

```
Ambiente
    nodo = registro
        dato: entero;
        izq, der: puntero a nodo;
    fin_reg;

    RAIZ: puntero a nodo;
```

| | |
|---|---|
| **dato** | Simple (entero, caracter…) o registro. |
| **izq, der** | Apuntan a los subárboles izq. y der. |
| **RAIZ** | Árbol vacío: RAIZ = NILL. |

---

## 15 · *(ampliación del código de la diapositiva 14)*

*Página con el código de la diapositiva 14 a pantalla completa (pie de página: 14).*

```
Ambiente
    nodo = registro
        dato: entero;
        izq, der: puntero a nodo;
    fin_reg;

    RAIZ: puntero a nodo;
```

---

## 16 · Comparación — ¿Se parece a un nodo de lista doble?

**COMPARACIÓN**

### ¿Se parece a un nodo de lista doble?

![[arbol1-lista-doble-vs-binario.png]]

*A la izquierda, dos nodos de lista doble (8 y 3) enlazados en ambos sentidos; a la derecha, un nodo de árbol (5) cuyos dos punteros bajan a los nodos 2 y 7.*

```
LISTA DOBLE

  ant  dato  prox      ant  dato  prox
 [    |  8  |  •──]──→[    |  3  |    ]
 [    |     |     ]←──[──• |     |    ]


ÁRBOL BINARIO

          izq  dato  der
         [ •  |  5  |  • ]
          /             \
         ▼               ▼
 [NILL| 2 |NILL]   [NILL| 7 |NILL]
```

| **LISTA DOBLE** | **ÁRBOL BINARIO** |
|---|---|
| Apuntan al anterior y al siguiente: una fila de ida y vuelta. | Los dos punteros bajan hacia los hijos. |

> [!tip] Misma forma, distinto significado
> el registro es igual, pero en el árbol los punteros van a los hijos y nunca vuelven hacia el padre.

---

## 17 · Representación en memoria

**REPRESENTACIÓN EN MEMORIA**

### Así queda un árbol binario con punteros

![[arbol1-memoria-punteros.png]]

```
 RAIZ ──→ [ • | A | • ]
           /         \
          ▼           ▼
   [ • | B | • ]     [NILL| C | • ]
     /       \                  \
    ▼         ▼                  ▼
[NILL|D|NILL] [NILL|E|NILL]   [NILL|F|NILL]
```

> [!info] Hojas
> sus dos punteros valen NILL. Un nodo con un solo hijo tiene un puntero en NILL.

---

## 18 · Recorridos

**RECORRIDOS**

### Visitar cada nodo una sola vez

**Todo recorrido combina tres actividades:**

- **R** — Tratar (visitar) la raíz
- **I** — Recorrer el subárbol izquierdo
- **D** — Recorrer el subárbol derecho

| | | |
|---|---|---|
| **Pre-orden** | `R I D` | La raíz va primero |
| **En-orden** | `I R D` | La raíz va en el medio |
| **Post-orden** | `I D R` | La raíz va al final |

---

## 19 · Recorridos · Pre-orden

**RECORRIDOS · PRE-ORDEN**

### Pre-orden: raíz, izquierdo, derecho (RID)

```
Procedimiento PreOrden(p: puntero a nodo);
Proceso
    SI p <> NILL ENTONCES
        Escribir(*p.dato);
        PreOrden(*p.izq);
        PreOrden(*p.der);
    FIN_SI;
Fin;
```

```
          A
        /   \
       B     C
      / \     \
     D   E     F
```

**Salida sobre este árbol**

`A  B  D  E  C  F`

> [!tip] Sólo cambia el lugar de Escribir
> naranja = tratar la raíz; verde = recorrer los subárboles.
>
> *(En la filmina, `Escribir(*p.dato);` está en naranja y las dos llamadas recursivas en verde.)*

---

## 20 · *(ampliación del código de la diapositiva 18)*

*Página con el código de PreOrden a pantalla completa (pie de página: 18).*

```
Procedimiento PreOrden(p: puntero a nodo);
Proceso
    SI p <> NILL ENTONCES
        Escribir(*p.dato);
        PreOrden(*p.izq);
        PreOrden(*p.der);
    FIN_SI;
Fin;
```

---

## 21 · Recorridos · En-orden

**RECORRIDOS · EN-ORDEN**

### En-orden: izquierdo, raíz, derecho (IRD)

```
Procedimiento EnOrden(p: puntero a nodo);
Proceso
    SI p <> NILL ENTONCES
        EnOrden(*p.izq);
        Escribir(*p.dato);
        EnOrden(*p.der);
    FIN_SI;
Fin;
```

```
          A
        /   \
       B     C
      / \     \
     D   E     F
```

**Salida sobre este árbol**

`D  B  E  A  C  F`

> [!tip] Sólo cambia el lugar de Escribir
> naranja = tratar la raíz; verde = recorrer los subárboles.

---

## 22 · *(ampliación del código de la diapositiva 19)*

*Página con el código de EnOrden a pantalla completa (pie de página: 19).*

```
Procedimiento EnOrden(p: puntero a nodo);
Proceso
    SI p <> NILL ENTONCES
        EnOrden(*p.izq);
        Escribir(*p.dato);
        EnOrden(*p.der);
    FIN_SI;
Fin;
```

---

## 23 · Recorridos · Post-orden

**RECORRIDOS · POST-ORDEN**

### Post-orden: izquierdo, derecho, raíz (IDR)

```
Procedimiento PostOrden(p: puntero a nodo);
Proceso
    SI p <> NILL ENTONCES
        PostOrden(*p.izq);
        PostOrden(*p.der);
        Escribir(*p.dato);
    FIN_SI;
Fin;
```

```
          A
        /   \
       B     C
      / \     \
     D   E     F
```

**Salida sobre este árbol**

`D  E  B  F  C  A`

> [!tip] Sólo cambia el lugar de Escribir
> naranja = tratar la raíz; verde = recorrer los subárboles.

---

## 24 · *(ampliación del código de la diapositiva 20)*

*Página con el código de PostOrden a pantalla completa (pie de página: 20).*

```
Procedimiento PostOrden(p: puntero a nodo);
Proceso
    SI p <> NILL ENTONCES
        PostOrden(*p.izq);
        PostOrden(*p.der);
        Escribir(*p.dato);
    FIN_SI;
Fin;
```

---

## 25 · Recursividad en acción — ¿Dónde está el caso base?

**RECURSIVIDAD EN ACCIÓN**

### ¿Dónde está el caso base?

```
Procedimiento EnOrden(p: puntero a nodo);
Proceso
    SI p <> NILL ENTONCES
        EnOrden(*p.izq);
        Escribir(*p.dato);
        EnOrden(*p.der);
    FIN_SI;
Fin;
```

*(En la filmina, la línea `SI p <> NILL ENTONCES` está resaltada en naranja con la etiqueta **◀ si p = NILL, no hace nada**, y las dos llamadas `EnOrden(*p.izq);` / `EnOrden(*p.der);` en verde con la etiqueta **◀ llamadas con subárboles**.)*

| **Caso base** | **Caso recursivo** | **Más pequeño** |
|---|---|---|
| Árbol vacío (p = NILL): no hay nada para recorrer. | Se recorre cada subárbol con la misma subacción. | Cada subárbol tiene menos nodos que el árbol. |

---

## 26 · Recursividad en acción — Traza de EnOrden sobre el subárbol de B

**RECURSIVIDAD EN ACCIÓN**

### Traza de EnOrden sobre el subárbol de B

![[arbol1-traza-enorden.png]]

```
      B
     / \
    D   E
```

| Paso (con la sangría de la filmina) | |
|---|---|
| `EnOrden(B)` | baja a la izquierda |
| `  EnOrden(D)` | baja a la izquierda |
| `    EnOrden(NILL)` | caso base: vuelve |
| `  Escribir D` | baja a la derecha → NILL, vuelve |
| `Escribir B` | baja a la derecha |
| `  EnOrden(E)` | NILL · Escribir E · NILL |

**Salida**

`D  B  E`

---

## 27 · Otro ejemplo recursivo — Contar los nodos de un árbol

**OTRO EJEMPLO RECURSIVO**

### Contar los nodos de un árbol

```
Funcion Contar(p: puntero a nodo): entero;
Proceso
    SI p = NILL ENTONCES
        Contar := 0;
    CONTRARIO
        Contar := 1 + Contar(*p.izq) + Contar(*p.der);
    FIN_SI;
Fin;
```

*(En la filmina, `Contar := 0;` está en naranja con la etiqueta **◀ CASO BASE** y la línea recursiva en verde con la etiqueta **◀ RECURSIVO**.)*

> [!tip] La idea
> Nodos del árbol = 1 (la raíz) + nodos del izquierdo + nodos del derecho.

**Contar(RAIZ) sobre el árbol A…F**

`6`

---

## 28 · *(ampliación del código de la diapositiva 23)*

*Página con el código de Contar a pantalla completa (pie de página: 23). La línea recursiva aparece partida en dos.*

```
Funcion Contar(p: puntero a nodo): entero;
Proceso
    SI p = NILL ENTONCES
        Contar := 0;
    CONTRARIO
        Contar := 1 + Contar(*p.izq) +
                      Contar(*p.der);
    FIN_SI;
Fin;
```

---

## 29 · Ejercicio en clase — Escribí los tres recorridos

**EJERCICIO EN CLASE**

### Escribí los tres recorridos

```
              8
           /     \
          3       10
         / \        \
        1   6        14
           / \      /
          4   7    13
```

- **Pre-orden:** \_\_\_\_\_\_\_\_\_\_
- **En-orden:** \_\_\_\_\_\_\_\_\_\_
- **Post-orden:** \_\_\_\_\_\_\_\_\_\_

---

## 30 · Ejercicio en clase — Solución

**EJERCICIO EN CLASE**

### Solución

![[arbol1-ejercicio-recorridos-solucion.png]]

```
              8
           /     \
          3       10
         / \        \
        1   6        14
           / \      /
          4   7    13
```

- **Pre-orden:** `8 3 1 6 4 7 10 14 13`
- **En-orden:** `1 3 4 6 7 8 10 13 14`
- **Post-orden:** `1 4 7 6 3 13 14 10 8`

> [!tip] ¿Notaron algo?
> el en-orden quedó ordenado. Es la pista para la próxima clase.

---

## 31 · Resumen de la clase

**RESUMEN DE LA CLASE**

### Lo que tenemos que llevarnos

1. Un árbol es una estructura homogénea, dinámica y no lineal, con definición recursiva.
2. Vocabulario: raíz, padre, hijo, hermanos, hoja, interior, grado, nivel, altura, rama.
3. Árbol binario: nodo = registro con dato y dos punteros (izq, der); vacío = NILL.
4. Recorridos: Pre (RID), En (IRD) y Post (IDR); el nombre dice cuándo va la raíz.
5. Todos son recursivos: caso base p = NILL, caso recursivo sobre cada subárbol.

---

## 32 · Para practicar — Ejercicios para la próxima clase

**PARA PRACTICAR**

### Ejercicios para la próxima clase

| | |
|---|---|
| **1. Contar hojas** — Función que devuelva cuántas hojas tiene un árbol binario. | **2. Sumar los datos** — Función que devuelva la suma de todos los datos de un árbol de enteros. |
| **3. Altura** — Función que calcule la altura (árbol vacío: 0; raíz sola: 1). | **4. Recorridos a mano** — Dibujar un árbol de 8 nodos y escribir sus tres recorridos. |

> [!tip] Pista
> copiá la estructura de Contar y cambiá sólo lo que hace en cada caso.

---

Sigue en [[13 — Árboles (ABB, AVL y B)]].
