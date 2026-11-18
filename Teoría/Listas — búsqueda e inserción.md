---
tipo: apunte
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
tags:
  - AED
  - listas
  - punteros
  - teoria
---

# Listas — búsqueda e inserción (simple, doble y circular)

> [!abstract] Qué es esta nota
> Todo lo que hace falta para **buscar** e **insertar** en los cuatro tipos de lista que da la materia: **simple**, **doble**, **circular simple** y **circular doble**. Para cada uno: cómo es, el algoritmo, por qué funciona y las trampas.
> Sale del material de cátedra (filminas 2026, guía, campus y repositorio de la cátedra; ver [[#9. Fuentes|§ Fuentes]]). **Todos los algoritmos de esta nota se corrieron en la extensión**: 104 corridas con lista vacía, un nodo, repetidos, valores al principio, al medio y al final, y cargas al azar, sin una falla.

[[💻 Algoritmos — Índice|← Materia]] · [[plantillas]] §9 · [[8 — Listas (Inserción y Eliminación)]] · [[TEMA VI — Listas — Índice]]

---

## 0. El mapa en una tabla

| | Simple | Doble | Circular simple | Circular doble |
|---|---|---|---|---|
| **Cómo se ve** | `PRIM → [a] → [b] → [c] → NIL` | `NIL ← [a] ⇄ [b] ⇄ [c] → NIL` | `PRIM → [a] → [b] → [c] → (vuelve a a)` | como la doble, pero `c → a` y `a ← c` |
| **Punteros del nodo** | `prox` | `ant`, `prox` | `prox` | `ant`, `prox` |
| **Punteros externos** | `PRIM` (y `ULT` si se carga al final) | `PRIM`, `ULT` | `PRIM` (y `ULT` para insertar ordenado o al final) | `PRIM`, `ULT` |
| **El recorrido corta en…** | `P = NIL` | `P = NIL` | **el siguiente es el primero** (`*P.prox = PRIM`) | **llegué al último** (`P = ULT`) |
| **Al cortar, el último…** | ya se procesó | ya se procesó | **no se procesó**: se mira aparte | **no se procesó**: se mira aparte |
| **Para buscar el lugar uso** | `P` y `ANT` | solo `P` (el anterior es `*P.ant`) | `P` y `ANT` | solo `P` |
| **Insertar antes del primero obliga a tocar…** | `PRIM` | `PRIM` y `*P.ant` | `PRIM` **y el último** | `PRIM`, **el último** y `*P.ant` |
| **Un solo nodo** | `prox = NIL` | `ant = prox = NIL` | `prox` = **él mismo** | `ant = prox` = **él mismo** |

> [!tip] La regla que explica toda la tabla
> En la circular **el último apunta al primero**. Por eso:
> 1. No hay `NIL` donde cortar: se corta cuando "el siguiente es el primero".
> 2. Cada vez que cambia el primero hay que avisarle **al último**.

---

## 1. Lo que vale para las cuatro

### Notación

| Qué | Cómo se escribe |
|---|---|
| Pedir un nodo | `NUEVO(Q)` |
| Liberarlo | `DISPONER(Q)` |
| Puntero a ningún lado | `NIL` (en material de cátedra también `NILL`, `NULO`, `Nil`) |
| Campo del nodo apuntado | `*P.dato` (también `P^.dato`, `P*.dato`) |
| Campo del nodo apuntado por un campo | `*(*P.ant).prox` |

`P.dato` **sin** asterisco está mal: `P` es la dirección, no el nodo.

### Las dos preguntas antes de escribir

1. **¿Dónde corta el recorrido?** En una lineal, en `NIL`. En una circular, al volver al principio.
2. **¿Qué punteros cambian?** Contá cuántas flechas hay que redibujar: en la simple son **2**, en la doble **4**, y en la circular se suma **la del último**.

### El orden de los enganches importa

Antes de pisar un puntero, asegurate de que lo que apuntaba siga alcanzable por otro lado. Si no, **perdés el resto de la lista**. Por eso el nodo nuevo se engancha **primero hacia afuera** (`*Q.prox := P`) y recién después la lista **lo apunta a él**. En la doble esto decide si el algoritmo anda o no (ver [[#3.5 Inserción ordenada|§ 3.5]]).

### Tres formas de insertar

La guía les pone nombre a las tres "cargas":

| Carga | Dónde va el nuevo | ¿Busca el lugar? | Cómo queda la lista |
|---|---|---|---|
| **Apilada** | siempre adelante | no | al revés de como se leyó |
| **Encolada** | siempre al final | no (con `ULT`) | en el orden en que se leyó |
| **Ordenada** | donde le toca según un campo | **sí, cada vez** | ordenada |

> [!tip] Antes de ordenar, mirá si ya viene ordenado
> Si los datos llegan en el orden que te piden (por ejemplo, un archivo ordenado por código y una lista pedida por código), alcanza con la **encolada**, que no busca nada.

### Ascendente, descendente y empates

En el `MIENTRAS` que busca el lugar:

- `*P.dato < *Q.dato` deja la lista **de menor a mayor**, y `>` **de mayor a menor**.
- Con `<`, un valor repetido queda **antes** de sus iguales. Con `<=`, queda **después**.
- Para desempatar por otro campo se amplía la condición: `(*P.a < *Q.a) O ((*P.a = *Q.a) Y (*P.b < *Q.b))`.

**`P <> NIL` va primero** en la condición: si `P` es `NIL`, `*P.dato` no existe, y el `Y` corta antes de evaluarlo.

---

## 2. Lista simple

```
PRIM → [10|•] → [20|•] → [30|NIL]
```

Cada nodo sabe quién le sigue, **no quién lo precede**. Por eso, para insertar, hay que ir guardando el anterior en `ANT`.

### 2.1 Declaración

```
NODO = REGISTRO
    dato: entero;
    prox: Puntero a NODO;
FIN_REGISTRO
PRIM, ULT, P, Q, ANT: Puntero a NODO;
valor: entero;
```

`ULT` solo hace falta para cargar al final.

### 2.2 Recorrido

```
P := PRIM;
MIENTRAS P <> NIL HACER
    ESCRIBIR(*P.dato);
    P := *P.prox;              // avanzar: sin esto, ciclo infinito
FIN_MIENTRAS
```

### 2.3 Búsqueda

```
P := PRIM;
MIENTRAS (P <> NIL) Y (*P.dato <> valor) HACER
    P := *P.prox;
FIN_MIENTRAS
SI P = NIL ENTONCES
    ESCRIBIR(valor, " no está");
SINO
    ESCRIBIR("Encontré el ", *P.dato);
FIN_SI
```

**Cómo funciona.** Avanza mientras haya nodo **y** no sea el buscado. El ciclo termina por una de dos razones, y el `SI` de abajo distingue cuál:

| Al salir | Quiere decir |
|---|---|
| `P = NIL` | recorrí toda la lista y no estaba |
| `P <> NIL` | `P` está parado **en** el nodo buscado |

Traza buscando 20 en `10 → 20 → 30`:

```
P = 10   ¿10 <> 20? sí → avanzo
P = 20   ¿20 <> 20? no → corto       P <> NIL → lo encontré
```

**Si la lista está ordenada**, se puede cortar apenas se pasa del valor. Es la misma idea que la búsqueda secuencial con corte en un arreglo ordenado ([[5 — Búsqueda y Ordenamiento]]):

```
P := PRIM;
MIENTRAS (P <> NIL) Y (*P.dato < valor) HACER
    P := *P.prox;
FIN_MIENTRAS
SI (P <> NIL) Y (*P.dato = valor) ENTONCES
    ESCRIBIR("Encontré el ", *P.dato);
SINO
    ESCRIBIR(valor, " no está");
FIN_SI
```

Al salir, `P` está en el primer nodo que **no es menor**: o es el buscado, o ya se pasó, o es `NIL`.

### 2.4 Inserción al inicio (carga apilada)

```
NUEVO(Q);
*Q.dato := valor;
*Q.prox := PRIM;               // el nuevo apunta al que era primero (o a NIL)
PRIM := Q;                     // y pasa a ser el primero
```

Anda también con la lista vacía: `PRIM` es `NIL`, así que el nuevo queda apuntando a `NIL`.

### 2.5 Inserción al final (carga encolada)

```
NUEVO(Q);
*Q.dato := valor;
*Q.prox := NIL;                // va a ser el último
SI PRIM = NIL ENTONCES
    PRIM := Q;                 // lista vacía: también es el primero
SINO
    *ULT.prox := Q;            // el que era último lo apunta
FIN_SI
ULT := Q;
```

Sin `ULT` habría que recorrer toda la lista para encontrar el último. Es lo mismo que **ENCOLAR** en [[9 — Pilas y Colas con Listas]].

### 2.6 Inserción ordenada

Es la de [[8 — Listas (Inserción y Eliminación)]], con sus **4 casos**:

```
CASO 1 · lista vacía            PRIM → NIL                      →  PRIM → [Q|NIL]
CASO 2 · antes del primero      PRIM → [10] → [20] → NIL        →  PRIM → [Q] → [10] → [20] → NIL
CASO 3 · en el medio            [10] → [20] → [30]   (ANT=20, P=30)  →  [10] → [20] → [Q] → [30]
CASO 4 · después del último     [10] → [20] → NIL    (ANT=20, P=NIL) →  [10] → [20] → [Q] → NIL
```

```
NUEVO(Q);
*Q.dato := valor;
SI PRIM = NIL ENTONCES                          { CASO 1: lista vacía }
    PRIM := Q;
    *Q.prox := NIL;
SINO
    P := PRIM;
    ANT := NIL;
    MIENTRAS (P <> NIL) Y (*P.dato < *Q.dato) HACER
        ANT := P;
        P := *P.prox;
    FIN_MIENTRAS
    SI P = PRIM ENTONCES                        { CASO 2: antes del primero }
        PRIM := Q;
        *Q.prox := P;
    SINO
        SI P = NIL ENTONCES                     { CASO 4: después del último }
            *ANT.prox := Q;
            *Q.prox := NIL;
        SINO                                    { CASO 3: en el medio }
            *ANT.prox := Q;
            *Q.prox := P;
        FIN_SI
    FIN_SI
FIN_SI
```

**Cómo funciona.**

1. **Búsqueda del lugar.** Avanza mientras el nodo de la lista sea menor que el nuevo, guardando el anterior. Al salir, **el nuevo va entre `ANT` y `P`**.
2. **Enganche según dónde quedaron `ANT` y `P`:**

| Al salir | Caso | Se cambia |
|---|---|---|
| `PRIM = NIL` | 1 | `PRIM` |
| `P = PRIM` (no avanzó) | 2 | `PRIM` y `*Q.prox` |
| `P <> NIL` y `P <> PRIM` | 3 | `*ANT.prox` y `*Q.prox` |
| `P = NIL` (llegó al final) | 4 | `*ANT.prox` y `*Q.prox` |

Traza insertando 25 en `10 → 20 → 30`:

```
vuelta   ANT    P     ¿*P.dato < 25?
inicio   NIL    10    sí → avanzo
1        10     20    sí → avanzo
2        20     30    no → corto            → CASO 3 (P <> NIL, P <> PRIM)

*ANT.prox := Q     20 → 25
*Q.prox := P       25 → 30          resultado: 10 → 20 → 25 → 30
```

**Versión corta.** Mirando la tabla, en los 4 casos el nuevo termina apuntando a `P` (que es `NIL` justo en los casos 1 y 4), y lo apunta `PRIM` si `ANT = NIL` o `*ANT.prox` si no. Queda:

```
NUEVO(Q);
*Q.dato := valor;
P := PRIM;
ANT := NIL;
MIENTRAS (P <> NIL) Y (*P.dato < *Q.dato) HACER
    ANT := P;
    P := *P.prox;
FIN_MIENTRAS
SI ANT = NIL ENTONCES          { CASOS 1 y 2: va primero }
    PRIM := Q;
SINO                           { CASOS 3 y 4: va después de ANT }
    *ANT.prox := Q;
FIN_SI
*Q.prox := P;                  { P es NIL en los casos 1 y 4 }
```

Hace exactamente lo mismo (se probó con las mismas cargas). Para el parcial sirven las dos: la larga muestra los casos, la corta es más difícil de equivocar.

> [!warning] `ANT := NIL` va adentro del ciclo de carga
> Si insertás varios valores dentro de un `MIENTRAS`, `ANT` tiene que volver a `NIL` **antes de cada búsqueda**. Si no, arrastra el anterior de la vuelta pasada y el caso 2 se rompe.

---

## 3. Lista doble

```
NIL ← [•|10|•] ⇄ [•|20|•] ⇄ [•|30|•] → NIL
       PRIM                    ULT
```

Cada nodo sabe quién le sigue (`prox`) **y quién lo precede** (`ant`). Se recorre en los dos sentidos, y para insertar **no hace falta `ANT`**: el anterior de `P` es `*P.ant`. A cambio, cada inserción mueve **4 punteros** en lugar de 2.

- El `ant` del primero vale `NIL`.
- El `prox` del último vale `NIL`.
- Se mantienen **`PRIM` y `ULT`**.

### 3.1 Declaración

```
NODO = REGISTRO
    dato: entero;
    ant: Puntero a NODO;
    prox: Puntero a NODO;
FIN_REGISTRO
PRIM, ULT, P, Q: Puntero a NODO;
valor: entero;
```

### 3.2 Recorrido, en los dos sentidos

```
P := PRIM;                     // hacia adelante
MIENTRAS P <> NIL HACER
    ESCRIBIR(*P.dato);
    P := *P.prox;
FIN_MIENTRAS

P := ULT;                      // hacia atrás
MIENTRAS P <> NIL HACER
    ESCRIBIR(*P.dato);
    P := *P.ant;
FIN_MIENTRAS
```

### 3.3 Búsqueda

Igual que en la simple:

```
P := PRIM;
MIENTRAS (P <> NIL) Y (*P.dato <> valor) HACER
    P := *P.prox;
FIN_MIENTRAS
SI P = NIL ENTONCES
    ESCRIBIR(valor, " no está");
SINO
    ESCRIBIR("Encontré el ", *P.dato);
FIN_SI
```

Y como hay `ant`, también se puede buscar **desde atrás**:

```
P := ULT;
MIENTRAS (P <> NIL) Y (*P.dato <> valor) HACER
    P := *P.ant;
FIN_MIENTRAS
SI P = NIL ENTONCES
    ESCRIBIR(valor, " no está");
SINO
    ESCRIBIR("Encontré el ", *P.dato);
FIN_SI
```

Desde atrás conviene cuando lo buscado está más cerca del final, o cuando la lista está ordenada de menor a mayor y buscás valores grandes.

### 3.4 Inserción al final

Es la de `LISTA_DOBLE` de la guía (Complementos 2026):

```
NUEVO(Q);
*Q.dato := valor;
SI PRIM = NIL ENTONCES
    *Q.ant := NIL;
    *Q.prox := NIL;
    PRIM := Q;
    ULT := Q;
SINO
    *ULT.prox := Q;
    *Q.ant := ULT;
    ULT := Q;
    *Q.prox := NIL;
FIN_SI
```

### 3.5 Inserción ordenada

Es la de [[8 — Listas (Inserción y Eliminación)]]:

```
NUEVO(Q);
*Q.dato := valor;
SI PRIM = NIL ENTONCES                          { CASO 1: lista vacía }
    PRIM := Q;
    ULT := Q;
    *Q.prox := NIL;
    *Q.ant := NIL;
SINO
    P := PRIM;
    MIENTRAS (P <> NIL) Y (*P.dato < *Q.dato) HACER
        P := *P.prox;
    FIN_MIENTRAS
    SI P = PRIM ENTONCES                        { CASO 2: antes del primero }
        *Q.prox := P;
        *P.ant := Q;
        *Q.ant := NIL;
        PRIM := Q;
    SINO
        SI P = NIL ENTONCES                     { CASO 4: después del último }
            *Q.ant := ULT;
            *Q.prox := NIL;
            *ULT.prox := Q;
            ULT := Q;
        SINO                                    { CASO 3: en el medio, antes de P }
            *Q.ant := *P.ant;
            *Q.prox := P;
            *(*P.ant).prox := Q;
            *P.ant := Q;
        FIN_SI
    FIN_SI
FIN_SI
```

**Los 4 enganches del caso 3**, insertando 25 entre 20 y 30 (`P` = 30, y `*P.ant` = 20):

```
antes:    [20] ⇄ [30]                Q = [25]
                  P

1. *Q.ant := *P.ant        25 ──ant──→ 20
2. *Q.prox := P            25 ──prox─→ 30
3. *(*P.ant).prox := Q     20 ──prox─→ 25      (*P.ant todavía es el 20)
4. *P.ant := Q             30 ──ant──→ 25

después:  [20] ⇄ [25] ⇄ [30]
```

> [!warning] El paso 4 va último
> El paso 3 usa `*P.ant` para llegar al 20. Si hacés primero `*P.ant := Q`, en el paso 3 `*P.ant` ya es el nuevo, y `*(*P.ant).prox := Q` lo deja **apuntándose a sí mismo**. El 20 queda desenganchado.

**Qué cambia en cada caso:**

| Caso | Se cambia |
|---|---|
| 1 · vacía | `PRIM`, `ULT`, y los dos punteros del nuevo en `NIL` |
| 2 · antes del primero | `*Q.prox`, `*P.ant` (el viejo primero), `*Q.ant := NIL`, `PRIM` |
| 3 · en el medio | los 4 del dibujo |
| 4 · después del último | `*Q.ant := ULT`, `*Q.prox := NIL`, `*ULT.prox`, `ULT` |

> [!info] Por qué el caso 4 usa `ULT`
> Cuando la búsqueda llega al final, `P` es `NIL` y no hay `*P.ant` de donde sacar el anterior. Por eso se mantiene `ULT`: es el anterior del nuevo.

---

## 4. Lista circular simple

```
PRIM → [10] → [20] → [30] ─┐
        ↑__________________┘         (el último apunta al primero)
```

- El último **no** apunta a `NIL`: apunta al **primero**.
- Con un solo nodo, ese nodo **se apunta a sí mismo**.
- No hay `NIL` donde cortar un recorrido. Si escribís `MIENTRAS P <> NIL`, el ciclo **no termina nunca**.

La declaración es la misma que la de la simple ([[#2.1 Declaración|§ 2.1]]). Lo que dice que es circular son los enganches.

### 4.1 Recorrido

Es el de `LISTA_CIRCULAR` (guía):

```
SI PRIM = NIL ENTONCES
    ESCRIBIR("Lista vacía");
SINO
    P := PRIM;
    MIENTRAS *P.prox <> PRIM HACER         // corta parado en el último
        ESCRIBIR(*P.dato);
        P := *P.prox;
    FIN_MIENTRAS
    ESCRIBIR(*P.dato);                     // el último, que el ciclo no escribió
FIN_SI
```

**Por qué el último se escribe afuera.** El ciclo corta cuando `*P.prox = PRIM`, es decir, **cuando `P` está en el último**. Ese nodo todavía no se escribió, así que se escribe después del ciclo.

Por qué no se usa `MIENTRAS P <> PRIM`: `P` arranca valiendo `PRIM`, así que **el ciclo no entraría nunca**. Ese es justamente el error de la diapositiva 16 de [[3.02 — Listas Doblemente Enlazadas y Circulares]].

### 4.2 Búsqueda

Es la de la guía y la de la diapositiva 17 de la 3.02:

```
SI PRIM = NIL ENTONCES
    ESCRIBIR("Lista vacía");
SINO
    P := PRIM;
    MIENTRAS (*P.prox <> PRIM) Y (*P.dato <> valor) HACER
        P := *P.prox;
    FIN_MIENTRAS
    SI *P.dato = valor ENTONCES            // también mira el último
        ESCRIBIR("Encontré el ", *P.dato);
    SINO
        ESCRIBIR(valor, " no está");
    FIN_SI
FIN_SI
```

Corta parado en el buscado **o en el último**. Por eso el `SI` de afuera pregunta por el dato y no por el puntero: si corta en el último, puede ser porque era ese o porque no estaba.

### 4.3 Inserción sin orden

**En el 2º lugar** (`LISTA_CIRCULAR`, guía). Es la más corta, porque no toca al último:

```
NUEVO(Q);
*Q.dato := valor;
SI PRIM = NIL ENTONCES
    *Q.prox := Q;                  // único nodo: se apunta a sí mismo
    PRIM := Q;
SINO
    *Q.prox := *PRIM.prox;         // en el 2º lugar: no hay que tocar al último
    *PRIM.prox := Q;
FIN_SI
```

**Al final, con `ULT`** (es el caso 4 de la ordenada del repositorio):

```
NUEVO(Q);
*Q.dato := valor;
SI PRIM = NIL ENTONCES
    PRIM := Q;
    ULT := Q;
    *Q.prox := Q;                  // único nodo: se apunta a sí mismo
SINO
    *ULT.prox := Q;                // el viejo último apunta al nuevo
    *Q.prox := PRIM;               // el nuevo cierra el círculo
    ULT := Q;
FIN_SI
```

> [!bug] Ojo con la diapositiva 19 de la 3.02
> Sus etapas de "insertar en una circular" dicen que el nuevo apunta al primero y que `ULT` pasa al nuevo, pero **no enganchan el viejo último con el nuevo** (`*ULT.prox := Q`). Sin esa línea, el nodo queda fuera de la lista.

### 4.4 Inserción ordenada

Es la de `LISTAS_SIMPLE_CIRC_INS.c` del repositorio de la cátedra, traducida al pseudocódigo ([[Repo isi-aed — Listas (C, Python y pseudocódigo)]]):

```
NUEVO(Q);
*Q.dato := valor;
SI PRIM = NIL ENTONCES                                  { CASO 1: lista vacía }
    PRIM := Q;
    ULT := Q;
    *Q.prox := Q;
SINO
    P := PRIM;
    ANT := NIL;
    MIENTRAS (*P.prox <> PRIM) Y (*P.dato < *Q.dato) HACER
        ANT := P;
        P := *P.prox;
    FIN_MIENTRAS
    SI (P = PRIM) Y (*P.dato >= *Q.dato) ENTONCES      { CASO 2: antes del primero }
        *Q.prox := PRIM;
        PRIM := Q;
        *ULT.prox := Q;                                 // el último apunta al nuevo primero
    SINO
        SI (*P.prox = PRIM) Y (*P.dato < *Q.dato) ENTONCES { CASO 4: después del último }
            *P.prox := Q;
            *Q.prox := PRIM;                            // el nuevo último cierra el círculo
            ULT := Q;
        SINO                                            { CASO 3: en el medio, antes de P }
            *ANT.prox := Q;
            *Q.prox := P;
        FIN_SI
    FIN_SI
FIN_SI
```

**Cómo funciona.** La búsqueda es la de la simple, pero el corte "llegué al final" es `*P.prox <> PRIM` en vez de `P <> NIL`. Eso tiene una consecuencia: **el ciclo puede cortar en el último sin haberlo comparado**. Por eso, después del ciclo, cada caso **vuelve a preguntar por el dato**:

| Al salir | Caso | Qué se hace |
|---|---|---|
| `PRIM = NIL` | 1 · vacía | el nuevo se apunta a sí mismo; `PRIM` y `ULT` son él |
| `P = PRIM` y `*P.dato >= nuevo` | 2 · antes del primero | el nuevo apunta al viejo primero, pasa a ser `PRIM` y **el último lo apunta** (`*ULT.prox := Q`) |
| `P` es el último y `*P.dato < nuevo` | 4 · después del último | el último apunta al nuevo, **el nuevo apunta a `PRIM`**, `ULT` pasa al nuevo |
| cualquier otro | 3 · en el medio | igual que la simple: `*ANT.prox := Q`, `*Q.prox := P` |

El caso 3 cubre también **"antes del último"**: el ciclo se detuvo en el último, pero el último es mayor.

Caso 2 insertando 5 en `10 → 20 → 30 → (10)`:

```
antes:    PRIM → [10] → [20] → [30] → (10)            ULT = 30
                  P

*Q.prox := PRIM       5 → 10
PRIM := Q             PRIM → 5
*ULT.prox := Q        30 → 5                          (si te lo olvidás, el 5 no está en el círculo)

después:  PRIM → [5] → [10] → [20] → [30] → (5)
```

> [!tip] Por qué hace falta `ULT`
> Para insertar antes del primero hay que cambiar el puntero **del último**. Sin `ULT`, habría que recorrer toda la lista para encontrarlo. Es lo que hace la guía al **eliminar** el primero de una circular, y lo que intenta `INSERCION-PREVIA` en el ejemplo del campus.

> [!bug] El ejemplo del campus tiene justo estos dos errores
> [[Ejemplo — Carga ordenada de lista circular simple]] (el `.docx` de la carpeta del campus):
> - **No compara el último**: cargando 10, 30 y 20 queda 10 → 30 → 20.
> - **`INSERCION-PREVIA` busca el último pero no lo engancha** (`A*.PROX := P; PRIM := P` no están): el nodo se pierde.
>
> El algoritmo de arriba resuelve las dos cosas: el `(*P.dato < *Q.dato)` del caso 4 y el `*ULT.prox := Q` del caso 2.

---

## 5. Lista circular doble

```
        ┌────────────── prox del último ──────────────┐
        ↓                                             │
PRIM → [•|10|•]  ⇄  [•|20|•]  ⇄  [•|30|•] ← ULT ──────┘
        │                              ↑
        └─────── ant del primero ──────┘
```

- Es una doble donde **el último apunta al primero** (`prox`) y **el primero apunta al último** (`ant`).
- Con un solo nodo, `prox` y `ant` **apuntan a él mismo**.
- Se mantienen `PRIM` y `ULT`. Al tener `ULT`, el corte "llegué al último" se escribe directo: `P = ULT`.

La declaración es la misma que la de la doble ([[#3.1 Declaración|§ 3.1]]).

### 5.1 Recorrido, en los dos sentidos

```
SI PRIM = NIL ENTONCES
    ESCRIBIR("Lista vacía");
SINO
    P := PRIM;                     // hacia adelante: corta en ULT
    MIENTRAS P <> ULT HACER
        ESCRIBIR(*P.dato);
        P := *P.prox;
    FIN_MIENTRAS
    ESCRIBIR(*P.dato);

    P := ULT;                      // hacia atrás: corta en PRIM
    MIENTRAS P <> PRIM HACER
        ESCRIBIR(*P.dato);
        P := *P.ant;
    FIN_MIENTRAS
    ESCRIBIR(*P.dato);
FIN_SI
```

### 5.2 Búsqueda

```
SI PRIM = NIL ENTONCES
    ESCRIBIR("Lista vacía");
SINO
    P := PRIM;
    MIENTRAS (P <> ULT) Y (*P.dato <> valor) HACER
        P := *P.prox;
    FIN_MIENTRAS
    SI *P.dato = valor ENTONCES
        ESCRIBIR("Encontré el ", *P.dato);
    SINO
        ESCRIBIR(valor, " no está");
    FIN_SI
FIN_SI
```

> [!bug] No copies la búsqueda de la doble lineal
> `DOBLE_CIRC_DEL` del repositorio busca con `P <> NIL` (copiado de la doble lineal): **si el valor no está, no termina nunca**. En una circular se corta en `ULT` (o en `*P.prox = PRIM`).

### 5.3 Inserción ordenada

Es la de `LISTAS_DOBLE_CIRC_INS.c` del repositorio, traducida al pseudocódigo:

```
NUEVO(Q);
*Q.dato := valor;
SI PRIM = NIL ENTONCES                                  { CASO 1: lista vacía }
    PRIM := Q;
    ULT := Q;
    *Q.prox := Q;
    *Q.ant := Q;
SINO
    P := PRIM;
    MIENTRAS (P <> ULT) Y (*P.dato < *Q.dato) HACER
        P := *P.prox;
    FIN_MIENTRAS
    SI (P = PRIM) Y (*P.dato >= *Q.dato) ENTONCES      { CASO 2: antes del primero }
        *Q.prox := P;
        *P.ant := Q;
        *Q.ant := ULT;
        PRIM := Q;
        *ULT.prox := Q;                                 // cierre: ULT → nuevo PRIM
    SINO
        SI (P = ULT) Y (*P.dato < *Q.dato) ENTONCES    { CASO 4: después del último }
            *ULT.prox := Q;
            *Q.ant := ULT;
            *Q.prox := PRIM;
            ULT := Q;
            *PRIM.ant := Q;                             // cierre: PRIM ← nuevo ULT
        SINO                                            { CASO 3: en el medio, antes de P }
            *Q.ant := *P.ant;
            *Q.prox := P;
            *(*P.ant).prox := Q;
            *P.ant := Q;
        FIN_SI
    FIN_SI
FIN_SI
```

Son los 4 casos de la doble ([[#3.5 Inserción ordenada|§ 3.5]]) con **dos enganches más**, los que cierran el círculo:

| Caso | Lo mismo que la doble, más… |
|---|---|
| 1 · vacía | `prox` y `ant` del nuevo apuntan **a él mismo** (en vez de `NIL`) |
| 2 · antes del primero | `*Q.ant := ULT` (en vez de `NIL`) y **`*ULT.prox := Q`** |
| 3 · en el medio | nada: no toca ni al primero ni al último |
| 4 · después del último | `*Q.prox := PRIM` (en vez de `NIL`) y **`*PRIM.ant := Q`** |

Igual que en la circular simple, el ciclo puede cortar en `ULT` sin compararlo. Por eso el caso 4 pregunta `(P = ULT) Y (*P.dato < *Q.dato)`, y "antes del último" cae en el caso 3.

---

## 6. Todo junto: qué se toca en cada caso

| Caso | Simple | Doble | Circular simple | Circular doble |
|---|---|---|---|---|
| **1 · vacía** | `PRIM := Q`, `*Q.prox := NIL` | + `ULT := Q`, `*Q.ant := NIL` | `PRIM := Q`, `ULT := Q`, **`*Q.prox := Q`** | + **`*Q.ant := Q`** |
| **2 · antes del primero** | `PRIM := Q`, `*Q.prox := P` | + `*P.ant := Q`, `*Q.ant := NIL` | `*Q.prox := PRIM`, `PRIM := Q`, **`*ULT.prox := Q`** | + `*P.ant := Q`, **`*Q.ant := ULT`** |
| **3 · en el medio** | `*ANT.prox := Q`, `*Q.prox := P` | los 4 enganches | igual que la simple | igual que la doble |
| **4 · después del último** | `*ANT.prox := Q`, `*Q.prox := NIL` | `*Q.ant := ULT`, `*Q.prox := NIL`, `*ULT.prox := Q`, `ULT := Q` | `*P.prox := Q`, **`*Q.prox := PRIM`**, `ULT := Q` | + **`*PRIM.ant := Q`** |

En negrita, lo que cambia por ser circular: **donde la lineal pone `NIL`, la circular pone el primero (o el último)**.

---

## 7. Errores típicos

| Error | Qué pasa | Cómo se evita |
|---|---|---|
| `p.dato` sin `*` | `p` es una dirección, no tiene campos | `*p.dato` |
| Olvidar `P := *P.prox` en el ciclo | ciclo infinito | escribí el avance apenas abrís el `MIENTRAS` |
| `*P.dato <> x` antes que `P <> NIL` | se evalúa un nodo que no existe | `P <> NIL` siempre primero |
| `ANT := NIL` una sola vez, fuera del ciclo de carga | el caso 2 usa el `ANT` de la vuelta pasada | reiniciarlo antes de cada búsqueda |
| No inicializar `PRIM := NIL` (y `ULT := NIL`) | el primer `SI PRIM = NIL` no se cumple | inicializar antes de cargar |
| En la doble, solo 2 de los 4 enganches del caso 3 | `ant` o `prox` quedan viejos; recorrer hacia atrás da otra lista | contar: 2 del nuevo + 1 del anterior + 1 del siguiente |
| En la doble, `*P.ant := Q` antes que `*(*P.ant).prox := Q` | el nuevo se apunta a sí mismo | `*P.ant` va último |
| En la doble, no actualizar `ULT` en el caso 4 | `ULT` deja de ser el último | `ULT := Q` |
| En la circular, `MIENTRAS P <> NIL` | no termina nunca | cortar con `*P.prox <> PRIM` o `P <> ULT` |
| En la circular, `MIENTRAS P <> PRIM` arrancando con `P := PRIM` | el ciclo no entra | preguntar por el **siguiente** (`*P.prox <> PRIM`) |
| En la circular, no mirar el último después del ciclo | no encuentra el último, o lo deja fuera de orden | volver a preguntar por el dato después del ciclo |
| En la circular, insertar antes del primero sin tocar el último | el nuevo queda fuera del círculo | `*ULT.prox := Q` |
| En la circular, el nuevo último apuntando a `NIL` | se rompe el círculo | `*Q.prox := PRIM` |
| En la circular, el primer nodo con `prox := NIL` | no es circular | un nodo solo se apunta a sí mismo |

---

## 8. Cómo practicarlo

1. Dibujá la lista con 3 nodos, en papel, con flechas.
2. Elegí 4 valores: uno menor que todos, uno entre el 1º y el 2º, uno entre los dos últimos y uno mayor que todos. Más la lista vacía, son los 4 casos y el "antes del último" de las circulares.
3. Para cada uno, hacé la traza de la búsqueda (`ANT`, `P`, condición) y redibujá **solo las flechas que cambian**.
4. Al final, recorré la lista dibujada en todos los sentidos que tenga: si pasás por todos los nodos y volvés (o terminás en `NIL`) donde corresponde, está bien.
5. Si querés confirmarlo, corrélo en la extensión: un `ESCRIBIR` del recorrido hacia adelante (y hacia atrás si es doble) muestra enseguida un enganche mal hecho.

---

## 9. Fuentes

| Parte | De dónde sale |
|---|---|
| Notación, cargas apilada/encolada/ordenada, búsqueda simple | teoría de listas de la guía ([[plantillas]] §9, [[SINTAXIS]] §10) |
| Inserción ordenada simple y doble (4 casos) | [[8 — Listas (Inserción y Eliminación)]] (filmina 2026) |
| Inserción al final de la doble, búsqueda en doble | `LISTA_DOBLE`, Complementos Teóricos de la Guía 2026 |
| Recorrido hacia atrás | [[3.02 — Listas Doblemente Enlazadas y Circulares]] (campus) |
| Encolar con `ULT` | [[9 — Pilas y Colas con Listas]] |
| Recorrido, búsqueda e inserción en 2º lugar de la circular | `LISTA_CIRCULAR`, Complementos 2026 · 3.02 diap. 17 |
| Inserción ordenada en circular simple y doble, al final en circular | repositorio de la cátedra `UTN-FRRe/isi-aed` ([[Repo isi-aed — Listas (C, Python y pseudocódigo)]]), traducido al pseudocódigo |
| Búsqueda con corte en lista ordenada | la búsqueda secuencial con corte de [[5 — Búsqueda y Ordenamiento]], aplicada a una lista |
| Búsqueda en circular doble cortando en `ULT` | la búsqueda de la circular simple, con el corte que usa `DOBLE_CIRC_INS` para ubicar el lugar |

> [!info] Cómo se verificó
> Cada bloque de código de esta nota se armó como programa y se corrió en la extensión `aed-vscode`: 12 algoritmos, 104 corridas. Las cargas fueron 30, 10, 50, 20, 40, 10, 5 y 60, más lista vacía, un nodo, dos nodos y 8 cargas al azar para cada inserción ordenada. Se buscaron valores presentes (el primero, uno del medio, el último) y ausentes. En las circulares se comprobó además que quedara cerrado el círculo (`*ULT.prox = PRIM` y, en la doble, `*PRIM.ant = ULT`).
