---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 13
titulo_original: Árboles — Clase 2 · Reconstrucción, tipos de árboles binarios, ABB, AVL y árboles B
archivo_original: 06_Arboles_Clase2_ABB_AVL_y_B_Rev_1.pdf
diapositivas: 30
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - arboles
  - punteros
  - recursividad
  - abb
  - avl
  - arbol-b
---

# 13 — Árboles (ABB, AVL y B)

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 30 páginas de **Árboles — Clase 2 · Reconstrucción, tipos de árboles binarios, ABB, AVL y árboles B** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[06_Arboles_Clase2_ABB_AVL_y_B_Rev_1.pdf]] (carpeta `PDF originales/`).
> El PDF tiene 27 diapositivas numeradas más 3 páginas que repiten el código ampliado (pie de página 14, 16 y 17). Acá cada página del PDF es una sección, así que la numeración de las secciones no coincide con el número del pie a partir de la página 15.
> Se usa la misma notación que en la clase 1: `NILL` (con doble L), `*p.campo`, `NUEVO(Q)`, `:=`, `FIN_SI;`, `FIN_MIENTRAS;`.

Viene de [[12 — Árboles (Conceptos y Recorridos)]].

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

# Árboles

Clase 2 · Reconstrucción, tipos de árboles binarios, ABB, AVL y árboles B

*Pre + En / Post + En · Expresión · ABB: buscar e insertar · Factor de equilibrio · B y B+*

---

## 2 · Repaso de la clase anterior

**REPASO DE LA CLASE ANTERIOR**

### Lo que ya sabemos

| **Pre-orden · RID** | **En-orden · IRD** | **Post-orden · IDR** |
|---|---|---|
| La raíz va primero. | La raíz va en el medio. | La raíz va al final. |

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

> [!info] Siempre recursivo
> Caso base: p = NILL (árbol vacío).
> Caso recursivo: cada subárbol.

---

## 3 · Reconstruir un árbol — Del recorrido al dibujo

**RECONSTRUIR UN ÁRBOL**

### Del recorrido al dibujo

> [!important] Con un solo recorrido no alcanza:
> necesitamos el EN-ORDEN y además el PRE-ORDEN o el POST-ORDEN.

1. **Buscar la raíz**
   En el PRE-ORDEN es el primero. En el POST-ORDEN es el último.
2. **Partir el EN-ORDEN**
   Lo que está a la izquierda de la raíz es el subárbol izquierdo; lo de la derecha, el derecho.
3. **Repetir en cada mitad**
   Cada subárbol se reconstruye igual. ¡Es recursivo!

*Referencia de colores usada en las diapositivas siguientes:* **raíz** (naranja) · **subárbol izquierdo** (celeste) · **subárbol derecho** (verde).

---

## 4 · Reconstruir · Pre-orden + En-orden

**RECONSTRUIR · PRE-ORDEN + EN-ORDEN**

### Ejemplo: Pre = 5 3 1 7 6 9 · En = 1 3 5 6 7 9

| | | | | | | |
|---|---|---|---|---|---|---|
| **Pre-orden** | **5** | 3 | 1 | 7 | 6 | 9 |
| **En-orden** | 1 | 3 | **5** | 6 | 7 | 9 |

*(En la filmina: el 5 en naranja; 3 y 1 en celeste —subárbol izquierdo—; 7, 6 y 9 en verde —subárbol derecho—.)*

1. La raíz es el 5 (primero del pre-orden).
2. En-orden: {1, 3} izquierda · {6, 7, 9} derecha.
3. Izquierdo: pre 3 1 → raíz 3, y el 1 queda a su izquierda.
4. Derecho: pre 7 6 9 → raíz 7, con hijos 6 y 9.

```
          5
        /   \
       3     7
      /     / \
     1     6   9
```

---

## 5 · Reconstruir · Post-orden + En-orden

**RECONSTRUIR · POST-ORDEN + EN-ORDEN**

### Ejemplo: Post = 4 5 2 6 7 3 1 · En = 4 2 5 1 6 3 7

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| **Post-orden** | 4 | 5 | 2 | 6 | 7 | 3 | **1** |
| **En-orden** | 4 | 2 | 5 | **1** | 6 | 3 | 7 |

*(En la filmina: el 1 en naranja; 4, 5 y 2 en celeste; 6, 7 y 3 en verde.)*

1. La raíz es el 1 (último del post-orden).
2. En-orden: {4, 2, 5} izquierda · {6, 3, 7} derecha.
3. Izquierdo: post 4 5 2 → raíz 2, con 4 y 5 como hijos.
4. Derecho: post 6 7 3 → raíz 3, con 6 y 7 como hijos.

```
            1
         /     \
        2       3
       / \     / \
      4   5   6   7
```

---

## 6 · Ejercicio en clase — Reconstruí estos dos árboles

**EJERCICIO EN CLASE**

### Reconstruí estos dos árboles

| **Ejercicio 1** | **Ejercicio 2** |
|---|---|
| **Pre-orden** | **Post-orden** |
| `G E A I B M C L D F K J H` | `C D A F I H G E B` |
| **En-orden** | **En-orden** |
| `I A B E G L D C F M K H J` | `C A D B F E I H G` |
| **a** Dibujar el árbol. | **a** Dibujar el árbol. |
| **b** Dar su recorrido post-orden. | **b** Dar su recorrido pre-orden. |

---

## 7 · Ejercicio en clase — Solución del ejercicio 1

**EJERCICIO EN CLASE**

### Solución del ejercicio 1

![[arbol2-reconstruccion-ej1-solucion.png]]

```
                 G
              /     \
             E       M
            /      /   \
           A      C     K
          / \    / \     \
         I   B  L   F     J
                 \       /
                  D     H
```

**Post-orden**

`I B A E D L F C H J K M G`

> [!info] Cómo se arrancó
> Pre: G primero → raíz.
> En: I A B E | G | L D C F M K H J.
> Izq.: raíz E. Der.: raíz M.

---

## 8 · Ejercicio en clase — Solución del ejercicio 2

**EJERCICIO EN CLASE**

### Solución del ejercicio 2

![[arbol2-reconstruccion-ej2-solucion.png]]

```
              B
           /     \
          A       E
         / \     / \
        C   D   F   G
                   /
                  H
                 /
                I
```

**Pre-orden**

`B A C D E F G H I`

> [!info] Cómo se arrancó
> Post: B último → raíz.
> En: C A D | B | F E I H G.
> Izq.: raíz A. Der.: raíz E.

---

## 9 · Tipos de árboles binarios — Árbol de expresión

**TIPOS DE ÁRBOLES BINARIOS**

### Árbol de expresión

> [!important] Definición
> Las **hojas** son operandos (constantes o variables) y los **nodos interiores** son operadores.

**`(a + b) * (c − d)`**

```
            *
         /     \
        +       −
       / \     / \
      a   b   c   d
```

| | | |
|---|---|---|
| **Infija · en-orden** | `a + b * c − d` | *Sin paréntesis: pierde la prioridad* |
| **Prefija · pre-orden** | `* + a b − c d` | *El operador va antes que los operandos* |
| **Posfija · post-orden** | `a b + c d − *` | *El operador va después de los operandos* |

---

## 10 · Tipos de árboles binarios — Equilibrado y completo

**TIPOS DE ÁRBOLES BINARIOS**

### Equilibrado y completo

| **Equilibrado** | **Completo** |
|---|---|
| En todos los nodos: \| altura(izq) − altura(der) \| ≤ 1 | Todo nodo interior tiene dos hijos y todas las hojas están en el mismo nivel. |

```
   Equilibrado              Completo

        8                      4
      /   \                  /   \
     4     12               2     6
    / \   /                / \   / \
   2   6 10               1   3 5   7
```

---

## 11 · Comparar dos árboles binarios — Distintos, similares y equivalentes

**COMPARAR DOS ÁRBOLES BINARIOS**

### Distintos, similares y equivalentes

![[arbol2-distintos-similares-equivalentes.png]]

| **DISTINTOS** | **SIMILARES** | **EQUIVALENTES** |
|---|---|---|
| Estructuras diferentes. | Misma forma, distinta información. | Misma forma y misma información. |

```
 DISTINTOS                SIMILARES             EQUIVALENTES

   A          A            A        X            A        A
  / \        / \          / \      / \          / \      / \
 B   C      B   C        B   C    Y   Z        B   C    B   C
    /        \
   D          D
```

---

## 12 · Árbol binario de búsqueda (ABB)

**ÁRBOL BINARIO DE BÚSQUEDA (ABB)**

### Un árbol que mantiene el orden

> [!important] Definición
> En todo nodo: a la izquierda, **valores menores**; a la derecha, **valores mayores**.

![[arbol2-abb-ejemplo.png]]

```
                   120
                /       \
             87          140
           /    \        /
         43      99    130
        /  \    /         \
      22   65  93         135
           /
          56
```

> [!info] Requisito
> Los valores deben poder ordenarse: enteros, caracteres, claves…

**En-orden**

`22 43 56 65 87 93 99 120 130 135 140`

> [!tip] ¡Sale ordenado!

---

## 13 · ABB · Búsqueda — Buscar el 65

**ABB · BÚSQUEDA**

### Buscar el 65: en cada nodo, izquierda o derecha

![[arbol2-abb-buscar-65.png]]

*El mismo ABB, con el camino 120 → 87 → 43 → 65 resaltado en naranja.*

| | |
|---|---|
| `65 < 120` | → izquierda |
| `65 < 87` | → izquierda |
| `65 > 43` | → derecha |
| `65 = 65` | → ¡encontrado! |

> [!tip] 4 comparaciones
> en lugar de recorrer los 11 nodos.

---

## 14 · ABB · Búsqueda — Función recursiva Buscar

**ABB · BÚSQUEDA**

### Función recursiva Buscar

```
Funcion Buscar(p: puntero a nodo; x: entero): logico;
Proceso
    SI p = NILL ENTONCES
        Buscar := falso;
    CONTRARIO
        SI x = *p.dato ENTONCES
            Buscar := verdadero;
        CONTRARIO
            SI x < *p.dato ENTONCES
                Buscar := Buscar(*p.izq, x);
            CONTRARIO
                Buscar := Buscar(*p.der, x);
            FIN_SI;
        FIN_SI;
    FIN_SI;
Fin;
```

*(En la filmina, los dos casos que terminan —`SI p = NILL … Buscar := falso;` y `SI x = *p.dato … Buscar := verdadero;`— están en naranja, y las dos llamadas recursivas en verde.)*

| | |
|---|---|
| **No está** | p = NILL: se llegó a un árbol vacío. |
| **Encontrado** | x = *p.dato |
| **Sigue buscando** | Menor: izquierda. Mayor: derecha. |

---

## 15 · *(ampliación del código de la diapositiva 14)*

*Página con el código de Buscar a pantalla completa (pie de página: 14).*

```
Funcion Buscar(p: puntero a nodo; x: entero): logico;
Proceso
    SI p = NILL ENTONCES
        Buscar := falso;
    CONTRARIO
        SI x = *p.dato ENTONCES
            Buscar := verdadero;
        CONTRARIO
            SI x < *p.dato ENTONCES
                Buscar := Buscar(*p.izq, x);
            CONTRARIO
                Buscar := Buscar(*p.der, x);
            FIN_SI;
        FIN_SI;
    FIN_SI;
Fin;
```

---

## 16 · ABB · Construcción — Insertar { 10, 5, 14, 7, 12 } uno por uno

**ABB · CONSTRUCCIÓN**

### Insertar { 10, 5, 14, 7, 12 } uno por uno

![[arbol2-abb-insertar-secuencia.png]]

*Cinco cuadros; en cada uno, el nodo recién insertado está en naranja.*

```
  +10       +5        +14         +7            +12

  10        10        10          10            10
           /         /  \        /  \          /  \
          5         5    14     5    14       5    14
                                 \             \   /
                                  7             7 12
```

| **Regla** | **El nuevo nodo** |
|---|---|
| Menor: izq. · Mayor: der. · En NILL: se cuelga. | Siempre entra como hoja. |

---

## 17 · ABB · Insertar (parte 1/2) — Crear el nodo y el caso del árbol vacío

**ABB · INSERTAR (PARTE 1/2)**

### Crear el nodo y el caso del árbol vacío

```
Procedimiento Insertar(x: entero);
Proceso
    NUEVO(Q);
    *Q.dato := x;
    *Q.izq := NILL;
    *Q.der := NILL;
    SI RAIZ = NILL ENTONCES
        RAIZ := Q;
    CONTRARIO
        // buscar el lugar (Parte 2)
    FIN_SI;
Fin;
```

*(En la filmina, `NUEVO(Q);` y las tres asignaciones a `*Q` están en naranja; `RAIZ := Q;` en verde.)*

**Proceso principal**

```
RAIZ := NILL;
Leer(x);
MIENTRAS x <> 0 HACER
    Insertar(x);
    Leer(x);
FIN_MIENTRAS;
```

> [!info] Árbol vacío:
> el primer valor ingresado se convierte en la raíz.

---

## 18 · *(ampliación del código de la diapositiva 16)*

*Página con los dos bloques de código de la diapositiva 16 ampliados (pie de página: 16).*

```
Procedimiento Insertar(x: entero);
Proceso
    NUEVO(Q);
    *Q.dato := x;
    *Q.izq := NILL;
    *Q.der := NILL;
    SI RAIZ = NILL ENTONCES
        RAIZ := Q;
    CONTRARIO
        // buscar el lugar (Parte 2)
    FIN_SI;
Fin;
```

```
RAIZ := NILL;
Leer(x);
MIENTRAS x <> 0 HACER
    Insertar(x);
    Leer(x);
FIN_MIENTRAS;
```

---

## 19 · ABB · Insertar (parte 2/2) — Buscar el lugar y colgar el nodo

**ABB · INSERTAR (PARTE 2/2)**

### Buscar el lugar y colgar el nodo

*(Este fragmento reemplaza el comentario `// buscar el lugar (Parte 2)`: empieza en el `CONTRARIO` del `SI RAIZ = NILL` y cierra con su `FIN_SI;`.)*

```
    CONTRARIO
        P := RAIZ;
        MIENTRAS P <> NILL HACER
            ANT := P;
            SI x < *P.dato ENTONCES
                P := *P.izq;
            CONTRARIO
                P := *P.der;
            FIN_SI;
        FIN_MIENTRAS;
        SI x < *ANT.dato ENTONCES
            *ANT.izq := Q;
        CONTRARIO
            *ANT.der := Q;
        FIN_SI;
    FIN_SI;
```

*(En la filmina, `MIENTRAS P <> NILL HACER`, `ANT := P;` y `FIN_MIENTRAS;` están en naranja; el `SI x < *ANT.dato … FIN_SI;` que cuelga el nodo, en verde.)*

> [!info] 1. Bajar hasta NILL
> P avanza a izquierda o derecha. ANT guarda el nodo anterior: el futuro padre.

> [!info] 2. Colgar el nodo
> Se compara con ANT para saber de qué lado va Q.
> ¿Te acordás de ANT en listas?

> [!bug] Errata de la filmina
> - El procedimiento `Insertar` no tiene `Ambiente`: `Q`, `P` y `ANT` no se declaran en ningún lado (deberían ser `puntero a nodo`), y tampoco se declara `x` en el proceso principal. Tal como está escrito, `Q`, `P`, `ANT` y `RAIZ` funcionan como variables globales.
> - `RAIZ` no se pasa como parámetro: `Insertar(x: entero)` lee y modifica directamente la `RAIZ` global (`RAIZ := Q;`). No hay pasaje por referencia de la raíz.

> [!note] Observación (no es un error)
> Si `x` es igual a `*P.dato`, el `CONTRARIO` lo manda a la derecha: el procedimiento no controla claves repetidas, las inserta en el subárbol derecho.

---

## 20 · *(ampliación del código de la diapositiva 17)*

*Página con el código de la parte 2 a pantalla completa (pie de página: 17).*

```
    CONTRARIO
        P := RAIZ;
        MIENTRAS P <> NILL HACER
            ANT := P;
            SI x < *P.dato ENTONCES
                P := *P.izq;
            CONTRARIO
                P := *P.der;
            FIN_SI;
        FIN_MIENTRAS;
        SI x < *ANT.dato ENTONCES
            *ANT.izq := Q;
        CONTRARIO
            *ANT.der := Q;
        FIN_SI;
    FIN_SI;
```

---

## 21 · Ejercicio en clase — Construir e interpretar ABB

**EJERCICIO EN CLASE**

### Construir e interpretar ABB

**a) Construir el ABB**

Insertar en este orden:

`D F E B A C G`

Después, escribir su recorrido en-orden. ¿Qué se observa?

**b) ¿En qué orden se ingresaron las claves?**

```
     Árbol 1                   Árbol 2

        50                  10
      /    \                  \
    30      70                 20
   /  \    /  \                  \
  20  40  60  80                  30
                                    \
                                     40
```

---

## 22 · Ejercicio en clase — Solución

**EJERCICIO EN CLASE**

### Solución

```
          D
        /   \
       B     F
      / \   / \
     A   C E   G
```

**En-orden**

`A B C D E F G`

> [!info] Árbol 1
> Por ejemplo 50 30 70 20 40 60 80, o 50 30 20 40 70 60 80.
> Cualquier orden con cada padre antes que sus hijos (el pre-orden siempre sirve).

> [!warning] Árbol 2
> Sólo 10 20 30 40: las claves llegaron ordenadas. El árbol quedó degenerado (como una lista) y buscar vuelve a ser secuencial.
> ¿Cómo lo evitamos? → árboles balanceados.

---

## 23 · Árbol balanceado (AVL) — Un ABB que no se deforma

**ÁRBOL BALANCEADO (AVL)**

### Un ABB que no se deforma

> [!important] Definición
> Un AVL es un **ABB** en el que, para todo nodo, las alturas de sus dos subárboles **difieren a lo sumo en 1**.

**Definición formal (recursiva)**

> [!info] Caso base
> El árbol vacío es AVL.

> [!info] Caso recursivo
> T no vacío, con subárboles T_i y T_d, es AVL si y sólo si:
>
> - `T_i es AVL`
> - `T_d es AVL`
> - `| H(T_i) − H(T_d) | ≤ 1`

*H(n) = altura del árbol n*

---

## 24 · Árbol balanceado (AVL) — Factor de equilibrio (FE)

**ÁRBOL BALANCEADO (AVL)**

### Factor de equilibrio (FE)

> [!important] Definición
> `FE = altura(der) − altura(izq)`

| | |
|---|---|
| `0` | Equilibrado: ambos subárboles tienen la misma altura. |
| `+1` | El subárbol derecho es un nivel más alto. |
| `−1` | El subárbol izquierdo es un nivel más alto. |

![[arbol2-avl-factor-equilibrio.png]]

```
                30
              FE +1
            /       \
          20          40
        FE −1       FE +1
        /           /    \
      10          35      50
       0           0    FE +1
                             \
                              60
                               0
```

> [!warning] Si | FE | ≥ 2
> el árbol dejó de ser AVL y hay que reequilibrarlo.

---

## 25 · Árbol balanceado (AVL) — ¿Es un árbol AVL?

**ÁRBOL BALANCEADO (AVL)**

### ¿Es un árbol AVL?

![[arbol2-es-avl.png]]

```
   Árbol 1               Árbol 2               Árbol 3

     30                    20                    20
    /  \                  /  \                  /  \
   20   40              10    30              10    40
  / \     \            /  \                  /        \
 10  25    50         5    15               5          50
                     /                                   \
                    3                                     60
```

*(En la filmina están resaltados en naranja el 20 del árbol 2 y el 40 del árbol 3: los nodos donde se rompe la condición.)*

| **Árbol 1** | **Árbol 2** | **Árbol 3** |
|---|---|---|
| **Sí: en todos los nodos la diferencia es ≤ 1.** | **No: en 20, izquierdo altura 3 y derecho altura 1.** | **No: el 20 está bien, pero en 40 la diferencia es 2.** |

---

## 26 · Árboles multicamino — Árbol B

**ÁRBOLES MULTICAMINO**

### Árbol B: pensado para memoria externa

**Árbol B de orden D**

- Cada página (salvo la raíz) tiene entre D y 2D claves.
- La raíz tiene entre 1 y 2D claves.
- Las páginas interiores tienen entre D + 1 y 2D + 1 hijos.
- La raíz, si no es hoja, tiene al menos 2 hijos.
- Todas las hojas están en el mismo nivel.

**Ejemplo · orden D = 2**

![[arbol2-arbol-b-orden2.png]]

```
                 [ 30 | 60 ]
               /      |      \
              ▼       ▼       ▼
       [10 | 20]  [40 | 50]  [70 | 80 | 90]
```

*Las claves de cada página quedan entre las claves de su padre: < 30, entre 30 y 60, > 60.*

> [!info] Página:
> un grupo de claves que se lee de una vez desde el disco.

---

## 27 · Árboles multicamino — Árbol B+

**ÁRBOLES MULTICAMINO**

### Árbol B+: toda la información en las hojas

- Raíz e interiores: sólo claves que sirven de índice.
- Toda la información (con su clave) está en las hojas.
- Todas las hojas están al mismo nivel: igual longitud de camino.
- Mismos límites que el B: entre D y 2D claves por página.

![[arbol2-arbol-bmas.png]]

```
                    [ 40 | 70 ]   índice
                  /      |      \
                 ▼       ▼       ▼
     [10 | 20 | 30] → [40 | 50 | 60] → [70 | 80]

            hojas con los datos, enlazadas →
```

*40 y 70 aparecen dos veces: en el índice y en la hoja.*

> [!info] Archivos indexados:
> el índice (raíz e interiores) permite acceso directo y las hojas encadenadas, acceso secuencial y mixto.

---

## 28 · Árboles multicamino — Árbol B vs árbol B+

**ÁRBOLES MULTICAMINO**

### Árbol B vs árbol B+

| | **Árbol B** | **Árbol B+** |
|---|---|---|
| **Dónde está la información** | En cualquier página | Sólo en las hojas |
| **Raíz e interiores** | Claves con su información | Sólo claves (índice) |
| **Claves repetidas** | No | Sí: en el índice y en la hoja |
| **Espacio** | Menor | Mayor (por la duplicación) |
| **Modificaciones frecuentes** | Reorganizar es costoso | Evita la reorganización |

---

## 29 · Resumen de la clase

**RESUMEN DE LA CLASE**

### Lo que tenemos que llevarnos

1. Con el en-orden + el pre-orden (o el post-orden) se reconstruye el árbol.
2. Árbol de expresión: hojas = operandos; cada recorrido da una notación.
3. ABB: menores a la izquierda, mayores a la derecha; el en-orden sale ordenado.
4. Buscar e insertar en un ABB: bajar por un solo lado hasta encontrar o llegar a NILL.
5. AVL: ABB con | FE | ≤ 1 en todos los nodos. B y B+: páginas para memoria externa.

---

## 30 · Para practicar — Ejercicios

**PARA PRACTICAR**

### Ejercicios

| | |
|---|---|
| **1. Construir y recorrer** — Insertar 45 20 70 10 30 60 90 25 en un ABB y dar sus tres recorridos. | **2. Reconstruir** — Pre = A B D E C F G, En = D B E A F C G. Dibujar el árbol y dar el post-orden. |
| **3. Buscar iterativo** — Reescribir Buscar con un MIENTRAS en lugar de recursión. | **4. Mínimo y máximo** — Funciones que devuelvan el menor y el mayor valor de un ABB. |
| **5. ¿Es AVL?** — Calcular el FE de cada nodo del ABB del ejercicio 1. | **6. Expresión** — Dibujar el árbol de (a − b) − c y de a − (b − c). Dar sus tres notaciones. |

---

Viene de [[12 — Árboles (Conceptos y Recorridos)]].
