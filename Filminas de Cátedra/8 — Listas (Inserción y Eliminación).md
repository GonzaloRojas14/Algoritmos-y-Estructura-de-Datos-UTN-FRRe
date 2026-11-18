---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 8
titulo_original: Listas Generalizadas — Inserción y Eliminación
archivo_original: 02_Listas_Insercion_Eliminacion_3.1.pdf
diapositivas: 53
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - listas
  - punteros
---

# 8 — Listas (Inserción y Eliminación)

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 53 diapositivas de **Listas Generalizadas — Inserción y Eliminación** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[02_Listas_Insercion_Eliminacion_3.1.pdf]] (carpeta `PDF originales/`).
> El PDF tiene 53 páginas, pero el pie de página numera las diapositivas de 02 a 39 (más la de cierre): 12 páginas son **ampliaciones** del bloque de código de la diapositiva anterior (repiten el mismo número de pie) y la página 44 es un **duplicado** exacto de la 43. Se transcriben todas, en orden, marcando cuáles son ampliaciones.
> Los diagramas de nodos están pasados a texto. En la filmina, lo que se agrega o cambia está en **naranja** y el nodo que se elimina aparece sombreado, con borde punteado y una ✕ sobre el puntero que lo señala; acá se indica debajo de cada diagrama.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

Viene de [[7 — Listas (Introducción)]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

**Listas Generalizadas**
**Inserción y Eliminación**

Clase — Mantenimiento de listas simples y dobles ordenadas

Inserción ordenada · Eliminación · Simples y Dobles

---

## 2 · ¿Qué vamos a aprender hoy?

**OBJETIVOS DE LA CLASE**

1. **Los 4 casos de inserción ordenada**
   Lista vacía, antes del primero, en el medio, después del último.
2. **Cómo buscar el lugar**
   El recorrido con ANT y P que precede a toda inserción o eliminación.
3. **Los 4 casos de eliminación**
   El mismo esquema de casos, liberando memoria con DISPONER.
4. **Simples vs. dobles**
   Qué cambia (y qué no) al agregar el puntero ANT y el puntero externo ULT.

---

## 3 · Los 4 casos de inserción ordenada

**INSERCIÓN**

1. **Lista vacía**
   El nodo nuevo pasa a ser el primer (y único) nodo de la lista.
2. **Antes del primer elemento**
   El valor nuevo es menor a todos: cambia el puntero externo PRIM.
3. **En el medio — caso normal**
   Se recorre hasta encontrar el lugar y se enlaza entre ANT y P.
4. **Después del último elemento**
   El valor nuevo es mayor a todos: cambia el final de la lista.

---

## 4 · Recordando el nodo simple

**REPASO · LISTA SIMPLE**

```
      PRIM
        ↓
 ┌──────┬──────┐
 │  8   │      │
 └──────┴──────┘
   DATO   PROX
```

**Un solo puntero externo**

- La lista simple sólo conoce el frente: el puntero externo PRIM. Para llegar al anterior de un nodo hay que recorrer desde PRIM.

---

## 5 · Buscando el lugar de inserción

**INSERCIÓN · SIMPLE**

```
P := PRIM;
ANT := NIL;
MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
   ANT := P;
   P := *P.prox;
FIN MIENTRAS;
{ salgo: P es el lugar, ANT es el anterior }
```

- "Pregunto por qué salgo… y sigo trabajando": la condición de salida del MIENTRAS es la que distingue los 4 casos.

---

## 6 · Buscando el lugar de inserción *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 05). Mismo contenido:*

```
P := PRIM;
ANT := NIL;
MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
   ANT := P;
   P := *P.prox;
FIN MIENTRAS;
{ salgo: P es el lugar, ANT es el anterior }
```

- "Pregunto por qué salgo… y sigo trabajando": la condición de salida del MIENTRAS es la que distingue los 4 casos.

---

## 7 · Lista vacía — primer nodo

**INSERCIÓN · SIMPLE · CASO 1**

```
 PRIM, Q
    ↓
  [5|•]──→ NIL
```

*(En naranja: el nodo nuevo 5, apuntado por PRIM y Q.)*

**ACCIONES**

```
Condición: PRIM = NIL

PRIM := Q;
*Q.prox := NIL;
```

---

## 8 · Antes del primer elemento

**INSERCIÓN · SIMPLE · CASO 2**

```
 PRIM,Q       P
   ↓          ↓
 [3|•] ──→ [5|•] ──→ [6|•] ──→ [8|•] ──→ NIL
```

*(En naranja: el nodo nuevo 3, el puntero PRIM,Q y el enlace 3 → 5.)*

**ACCIONES**

```
Condición: PRIM = P  (equivale a ANT = NIL)

PRIM := Q;
*Q.prox := P;
```

*P sigue apuntando al viejo primer nodo (ahora 2º); PRIM pasa a apuntar a Q.*

---

## 9 · En el medio — caso normal

**INSERCIÓN · SIMPLE · CASO 3**

```
 PRIM        ANT                   P
   ↓          ↓                    ↓
 [3|•] ──→ [5|•] ──→ [6|•] ──→ [8|•] ──→ NIL
                       ↑
                       Q
```

*(En naranja: el nodo nuevo 6, el puntero Q y los enlaces 5 → 6 y 6 → 8.)*

**ACCIONES**

```
Condición: *P.DATO > *Q.DATO  (con ANT <> NIL)

*ANT.prox := Q;
*Q.prox := P;
```

*ANT y P son los nodos entre los que se abre lugar para Q.*

> [!note] Observación
> El MIENTRAS de la búsqueda sale cuando `*P.DATO < *Q.DATO` es falso, o sea cuando `*P.DATO >= *Q.DATO`. Si el valor nuevo es **igual** a uno que ya está, también cae en este caso (se inserta antes del igual), aunque la condición de la filmina diga sólo `>`.

---

## 10 · Después del último elemento

**INSERCIÓN · SIMPLE · CASO 4**

```
                       ANT        Q
                        ↓         ↓
 [3|•] ──→ [5|•] ──→ [6|•] ──→ [8|•] ──→ NIL ←── P = NIL
```

*(En naranja: el nodo nuevo 8, el puntero Q y los enlaces 6 → 8 y 8 → NIL.)*

**ACCIONES**

```
Condición: P = NIL

*ANT.prox := Q;
*Q.prox := NIL;
```

*P llegó a NIL: Q se enlaza después del que era el último nodo.*

---

## 11 · Algoritmo de inserción — declaración

**PSEUDOCÓDIGO · SIMPLE**

```
(COMIENZA LA ACCIÓN…)
ACCION INSERCION ES
  (PRIM: PUNTERO A NODO);

  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
  FIN REGISTRO;

  P, Q, ANT: PUNTERO A NODO;
```

**Lectura**

- PRIM es el único parámetro: el puntero externo de la lista.
- P, Q y ANT son punteros de trabajo: Q para el nodo nuevo, P y ANT para ubicar el lugar.

> [!bug] Errata de la filmina
> En esta versión falta la palabra **`AMBIENTE`** antes de la declaración del `NODO`. En la ampliación (diapositiva siguiente) sí está.

---

## 12 · Algoritmo de inserción — declaración *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 10). Acá la cabecera va en una sola línea y aparece `AMBIENTE`:*

```
(COMIENZA LA ACCIÓN…)
ACCION INSERCION ES (PRIM: PUNTERO A NODO);
  AMBIENTE
  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
  FIN REGISTRO;

  P, Q, ANT: PUNTERO A NODO;
```

---

## 13 · Algoritmo de inserción — proceso (1/2): búsqueda

**PSEUDOCÓDIGO · SIMPLE**

```
PROCESO
  NUEVO(Q); LEER(*Q.DATO);
  SI (PRIM = NIL) ENTONCES
     PRIM := Q;  *Q.prox := NIL;            { CASO 1 }
  SINO
     P := PRIM;  ANT := NIL;
     MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
        ANT := P;  P := *P.prox;
     FIN MIENTRAS;
     { P y ANT ya ubican el lugar → sigue en la parte 2 }
```

---

## 14 · Algoritmo de inserción — proceso (1/2) *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 11). Resalta en negrita la condición `(P <> NIL) Y (*P.DATO < *Q.DATO)`; el `}` del comentario final queda solo en la línea de abajo por el tamaño de letra:*

```
PROCESO
  NUEVO(Q); LEER(*Q.DATO);
  SI (PRIM = NIL) ENTONCES
     PRIM := Q;  *Q.prox := NIL;            { CASO 1 }
  SINO
     P := PRIM;  ANT := NIL;
     MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
        ANT := P;  P := *P.prox;
     FIN MIENTRAS;
     { P y ANT ya ubican el lugar → sigue en la parte 2
}
```

---

## 15 · Algoritmo de inserción — proceso (2/2): los 4 casos

**PSEUDOCÓDIGO · SIMPLE**

```
     { … viene de la parte 1: ya se ubicaron P y ANT }
     SI (P = PRIM) ENTONCES
        PRIM := Q;  *Q.prox := P;             { CASO 2 }
     SINO SI (P = NIL) ENTONCES
        *ANT.prox := Q;  *Q.prox := NIL;      { CASO 4 }
     SINO
        *ANT.prox := Q;  *Q.prox := P;        { CASO 3 }
     FIN SI;
  FIN SI;
FIN ACCION.
```

> [!note] Sobre el `SINO SI`
> `SINO SI (P = NIL) ENTONCES` se usa como una cadena (tipo "si no, si…") que cierra con **un solo** `FIN SI;`. El segundo `FIN SI;` cierra el `SI (PRIM = NIL)` de la parte 1. Si se lo leyera como un `SI` anidado dentro del `SINO`, faltaría un `FIN SI;`. La filmina usa la misma forma en todos los algoritmos de esta clase.

---

## 16 · Algoritmo de inserción — proceso (2/2) *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 12). Resalta en negrita `(P = PRIM)` y `SI (P = NIL)`:*

```
     { … viene de la parte 1: ya se ubicaron P y ANT }
     SI (P = PRIM) ENTONCES
        PRIM := Q;  *Q.prox := P;             { CASO 2 }
     SINO SI (P = NIL) ENTONCES
        *ANT.prox := Q;  *Q.prox := NIL;      { CASO 4 }
     SINO
        *ANT.prox := Q;  *Q.prox := P;        { CASO 3 }
     FIN SI;
  FIN SI;
FIN ACCION.
```

---

## 17 · Recordando el nodo doble

**REPASO · LISTA DOBLE**

```
       PRIM              ULT
         ↓                 ↓
 ┌───────┬───────┬───────┐
 │       │   8   │       │
 └───────┴───────┴───────┘
    ANT     DATO    PROX
```

*(PRIM apunta al nodo por el lado del campo ANT y ULT por el lado del campo PROX: es el único nodo.)*

**Dos punteros externos, y un campo más**

- La lista doble agrega el campo ant en cada nodo y un segundo puntero externo, ULT, al último nodo: se puede ir hacia atrás sin recorrer de nuevo.
- Por eso, en las dobles, insertar o eliminar en el medio no necesita el puntero ANT: alcanza con *P.ant.

---

## 18 · Buscando el lugar de inserción

**INSERCIÓN · DOBLE**

```
P := PRIM;
MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
   P := *P.prox;
FIN MIENTRAS;
{ no hace falta ANT: ya tengo *P.ant }
```

- En la doble, la búsqueda es más simple: no hace falta llevar un puntero ANT aparte, porque cada nodo ya sabe quién es su anterior.

---

## 19 · Buscando el lugar de inserción *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 14). Resalta en negrita la condición `(P <> NIL) Y (*P.DATO < *Q.DATO)`:*

```
P := PRIM;
MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
   P := *P.prox;
FIN MIENTRAS;
{ no hace falta ANT: ya tengo *P.ant }
```

- En la doble, la búsqueda es más simple: no hace falta llevar un puntero ANT aparte, porque cada nodo ya sabe quién es su anterior.

---

## 20 · Lista vacía — primer nodo

**INSERCIÓN · DOBLE · CASO 1**

```
     PRIM,ULT,Q
          ↓
 NIL ←── [ |5| ] ──→ NIL
```

*(En naranja: el nodo nuevo 5, apuntado por PRIM, ULT y Q; ant y prox en NIL.)*

**ACCIONES**

```
Condición: PRIM = NIL

PRIM := Q;  ULT := Q;
*Q.prox := NIL;
*Q.ant  := NIL;
```

---

## 21 · Antes del primer elemento

**INSERCIÓN · DOBLE · CASO 2**

```
         PRIM,Q          P
            ↓            ↓
 NIL ←── [ |3| ] ⇄ [ |5| ] ⇄ [ |6| ]
```

*(En naranja: el nodo nuevo 3, el puntero PRIM,Q, su ant → NIL y los enlaces 3 → 5 y 5 → 3.)*

**ACCIONES**

```
Condición: PRIM = P

*Q.prox := P;   *P.ant := Q;
*Q.ant  := NIL;
PRIM := Q;
```

*P sigue apuntando al viejo primer nodo (ahora 2º); PRIM pasa a apuntar a Q.*

---

## 22 · En el medio — caso normal

**INSERCIÓN · DOBLE · CASO 3**

```
                         P
                         ↓
 [ |5| ] ⇄ [ |6| ] ⇄ [ |8| ]
              ↑
              Q
```

*(En naranja: el nodo nuevo 6, el puntero Q y los cuatro enlaces 5 ⇄ 6 y 6 ⇄ 8.)*

**ACCIONES**

```
Condición: *P.DATO > *Q.DATO

*Q.ant := *P.ant;  *Q.prox := P;
*(*P.ant).prox := Q;
*(*Q.prox).ant := Q;
```

*ANT y P son los nodos entre los que se abre lugar para Q.*

> [!bug] Errata de la filmina
> La leyenda de abajo está copiada de la versión simple (diapositiva 9): en la doble **no hay puntero ANT** de trabajo (y el diagrama no lo muestra). El nodo anterior es `*P.ant`.
> Los enganches están bien: `*(*P.ant).prox := Q` se hace cuando `*P.ant` todavía es el nodo 5, y `*(*Q.prox).ant := Q` es lo mismo que `*P.ant := Q` (así se escribe en la diapositiva 28).

---

## 23 · Después del último elemento

**INSERCIÓN · DOBLE · CASO 4**

```
             Q, ULT
               ↓
 [ |6| ] ⇄ [ |8| ] ──→ NIL
```

*(En naranja: el nodo nuevo 8, el puntero Q, ULT y los enlaces 6 ⇄ 8 y 8 → NIL.)*

**ACCIONES**

```
Condición: P = NIL

*Q.ant := ULT;  *Q.prox := NIL;
*(*Q.ant).prox := Q;
ULT := Q;
```

*(La línea `*(*Q.ant).prox := Q;` está resaltada en negrita.)*

*P llegó a NIL: Q se enlaza después del que era el último nodo.*

---

## 24 · Algoritmo de inserción doble — declaración

**PSEUDOCÓDIGO · DOBLE**

```
(COMIENZA LA ACCIÓN…)
ACCION INSERCION_DOBLE ES
  (PRIM, ULT: PUNTERO A NODO);

  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
    ant:  PUNTERO A NODO;
  FIN REGISTRO;

  P, Q: PUNTERO A NODO;
```

**Lectura**

- PRIM y ULT son los dos punteros externos: ya no hace falta un ANT de trabajo para ubicar el anterior.
- El NODO suma el campo ant. P recorre buscando el lugar; Q es el nodo nuevo.

> [!bug] Errata de la filmina
> Igual que en la diapositiva 11, falta **`AMBIENTE`** antes del `NODO`; la ampliación siguiente sí lo tiene.

---

## 25 · Algoritmo de inserción doble — declaración *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 19). La cabecera se corta en dos renglones por el tamaño de letra:*

```
(COMIENZA LA ACCIÓN…)
ACCION INSERCION_DOBLE ES(PRIM, ULT: PUNTERO A
NODO);
  AMBIENTE
  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
    ant:  PUNTERO A NODO;
  FIN REGISTRO;

  P, Q: PUNTERO A NODO;
```

---

## 26 · Algoritmo de inserción doble — proceso (1/2): búsqueda

**PSEUDOCÓDIGO · DOBLE**

```
PROCESO
  NUEVO(Q); LEER(*Q.DATO);
  SI (PRIM = NIL) ENTONCES
     PRIM := Q;  ULT := Q;
     *Q.prox := NIL;  *Q.ant := NIL;        { CASO 1 }
  SINO
     P := PRIM;
     MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
        P := *P.prox;
     FIN MIENTRAS;
     { P ya ubica el lugar: no recorro ANT, leo *P.ant → parte 2 }
```

---

## 27 · Algoritmo de inserción doble — proceso (1/2) *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 20). El comentario final está en negrita y cursiva, cortado en dos renglones:*

```
PROCESO
  NUEVO(Q); LEER(*Q.DATO);
  SI (PRIM = NIL) ENTONCES
     PRIM := Q;  ULT := Q;
     *Q.prox := NIL;  *Q.ant := NIL;        { CASO 1 }
  SINO
     P := PRIM;
     MIENTRAS (P <> NIL) Y (*P.DATO < *Q.DATO) HACER
        P := *P.prox;
     FIN MIENTRAS;
     { P ya ubica el lugar: no recorro ANT, leo *P.ant
    → parte 2 }
```

---

## 28 · Algoritmo de inserción doble — proceso (2/2): los 4 casos

**PSEUDOCÓDIGO · DOBLE**

**CASOS 2 Y 4 — los extremos**

```
SI (P = PRIM) ENTONCES    {2}
   *Q.prox := P;  *P.ant := Q;
   *Q.ant := NIL;  PRIM := Q;
SINO SI (P = NIL) ENTONCES {4}
   *Q.ant := ULT;  *Q.prox := NIL;
   *ULT.prox := Q;  ULT := Q;
```

**CASO 3 — en el medio**

```
SINO                       {3}
   *Q.ant := *P.ant;
   *Q.prox := P;
   *(*P.ant).prox := Q;
   *P.ant := Q;
FIN SI;
```

```
FIN SI;      { cierra el SI (PRIM = NIL) de la parte 1 }
FIN ACCION.
```

*Son 3 casos, no 2: a diferencia de la simple, acá no hay forma de fusionar CASO 2 con CASO 4 en una sola rama.*

> [!bug] Errata de la filmina
> La comparación con la simple no cierra: en la simple (diapositiva 15) los casos 2 y 4 **también** van en ramas separadas, así que no es una diferencia. Lo que sí se podría fusionar en la simple es el CASO 3 con el CASO 4 (con P = NIL, `*Q.prox := P` deja NIL), aunque la filmina tampoco lo hace.
> Los enganches de las tres ramas están bien. El CASO 4 escribe `*ULT.prox := Q` donde la diapositiva 23 escribía `*(*Q.ant).prox := Q` (es lo mismo porque `*Q.ant` ya vale ULT), y el CASO 3 escribe `*P.ant := Q` donde la 22 escribía `*(*Q.prox).ant := Q`.

---

## 29 · Algoritmo de inserción doble — proceso (2/2) *(ampliación)*

*Ampliación de los tres bloques de la diapositiva anterior (pie: 21). Mismo contenido:*

```
SI (P = PRIM) ENTONCES    {2}
   *Q.prox := P;  *P.ant := Q;
   *Q.ant := NIL;  PRIM := Q;
SINO SI (P = NIL) ENTONCES {4}
   *Q.ant := ULT;  *Q.prox := NIL;
   *ULT.prox := Q;  ULT := Q;
```

```
SINO                       {3}
   *Q.ant := *P.ant;
   *Q.prox := P;
   *(*P.ant).prox := Q;
   *P.ant := Q;
FIN SI;
```

```
FIN SI;      { cierra el SI (PRIM = NIL) de la parte 1 }
FIN ACCION.
```

*Son 3 casos, no 2: a diferencia de la simple, acá no hay forma de fusionar CASO 2 con CASO 4 en una sola rama.*

---

## 30 · Los 4 casos de eliminación

**ELIMINACIÓN**

1. **Único nodo de la lista**
   La lista vuelve a quedar vacía: PRIM (y ULT) vuelven a NIL.
2. **Eliminar el primer nodo**
   Cambia el puntero externo PRIM, que pasa al segundo nodo.
3. **Eliminar en el medio — caso normal**
   ANT.prox se reconecta directamente con el nodo siguiente al eliminado.
4. **Eliminar el último nodo**
   Cambia el final de la lista: el nuevo último pasa a apuntar a NIL.

---

## 31 · Buscando el valor a eliminar

**ELIMINACIÓN · SIMPLE**

```
LEER(VALOR);
P := PRIM;  ANT := NIL;
MIENTRAS (P <> NIL) Y (*P.DATO <> VALOR) HACER
   ANT := P;
   P := *P.prox;
FIN MIENTRAS;
{ P=NIL: no está.  P<>NIL: lo encontré }
```

- Antes de DISPONER(P), siempre hay que decidir en cuál de los 4 casos cayó la búsqueda.

---

## 32 · Buscando el valor a eliminar *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 23). Resalta `(P <> NIL) Y` en negrita y `(*P.DATO <> VALOR)` en amarillo:*

```
LEER(VALOR);
P := PRIM;  ANT := NIL;
MIENTRAS (P <> NIL) Y (*P.DATO <> VALOR) HACER
   ANT := P;
   P := *P.prox;
FIN MIENTRAS;
{ P=NIL: no está.  P<>NIL: lo encontré }
```

- Antes de DISPONER(P), siempre hay que decidir en cuál de los 4 casos cayó la búsqueda.

---

## 33 · Único nodo — vuelve a vacía

**ELIMINACIÓN · SIMPLE · CASO 1**

```
 PRIM, P
    ✕
  [5|•] ┄┄→ NIL
```

*(El nodo 5 aparece sombreado y con borde punteado: es el que se libera.)*

**ACCIONES**

```
Condición: P = PRIM  (y *P.prox = NIL)

PRIM := NIL;
DISPONER(P);
```

*Se libera el único nodo y el puntero externo vuelve a NIL.*

---

## 34 · Eliminar el primer nodo

**ELIMINACIÓN · SIMPLE · CASO 2**

```
   P        PRIM
   ✕          ↓
 [3|•] ┄┄→ [5|•] ──→ [6|•] ──→ [8|•] ──→ NIL
```

*(El nodo 3 se libera; en naranja, PRIM apuntando ahora al nodo 5.)*

**ACCIONES**

```
Condición: P = PRIM  (hay más de un nodo)

PRIM := *P.prox;
DISPONER(P);
```

*PRIM se corre un lugar; el resto de la lista queda intacta.*

---

## 35 · Eliminar en el medio — caso normal

**ELIMINACIÓN · SIMPLE · CASO 3**

```
              ANT        P
               ↓         ✕
               ╭───────────────────╮   (nuevo enlace 5 → 8)
 [3|•] ──→ [5|•] ┄┄→ [6|•] ┄┄→ [8|•] ──→ NIL
```

*(El nodo 6 se libera; en naranja, el enlace nuevo de 5 a 8 que pasa por encima del 6.)*

**ACCIONES**

```
Condición: *P.DATO = VALOR  (con ANT<>NIL, P<>último)

*ANT.prox := *P.prox;
DISPONER(P);
```

*ANT.prox salta directamente al nodo siguiente al eliminado.*

---

## 36 · Eliminar el último nodo

**ELIMINACIÓN · SIMPLE · CASO 4**

```
                         ANT        P
                          ↓         ✕
                          ╭────────────────→ NIL   (nuevo enlace 6 → NIL)
 [3|•] ──→ [5|•] ──→ [6|•] ┄┄→ [8|•]
```

*(El nodo 8 se libera; en naranja, el enlace nuevo de 6 a NIL.)*

**ACCIONES**

```
Condición: *P.prox = NIL

*ANT.prox := NIL;
DISPONER(P);
```

*El nuevo último (ANT) pasa a apuntar a NIL.*

---

## 37 · Algoritmo de eliminación — declaración

**PSEUDOCÓDIGO · SIMPLE**

```
(COMIENZA LA ACCIÓN…)
ACCION ELIM ES
  (VALOR: ENTERO;
   PRIM: PUNTERO A NODO);

  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
  FIN REGISTRO;

  P, ANT: PUNTERO A NODO;
```

**Lectura**

- Ahora la acción recibe también VALOR: el dato que se busca para eliminar.
- P y ANT vuelven a ser los punteros de trabajo de la búsqueda.
- Al final siempre hay un DISPONER(P): eliminar sin liberar memoria dejaría un nodo colgado.

> [!bug] Errata de la filmina
> Falta **`AMBIENTE`** antes del `NODO` (la ampliación siguiente lo tiene). Además, los parámetros se separan con **`;`** (`VALOR: ENTERO; PRIM: …`) y en la ampliación con **`,`** (`VALOR: ENTERO, PRIM: …`).

---

## 38 · Algoritmo de eliminación — declaración *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 28). Resalta en negrita `VALOR: ENTERO`:*

```
(COMIENZA LA ACCIÓN…)
ACCION ELIM ES(VALOR: ENTERO, PRIM: PUNTERO A NODO);
  AMBIENTE
  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
  FIN REGISTRO;

  P, ANT: PUNTERO A NODO;
```

---

## 39 · Algoritmo de eliminación — proceso (1/2): búsqueda

**PSEUDOCÓDIGO · SIMPLE**

```
PROCESO
  SI (PRIM = NIL) ENTONCES
     ESCRIBIR("LISTA VACÍA... NADA PARA BORRAR");
  SINO
     P := PRIM;  ANT := NIL;
     MIENTRAS (P <> NIL) Y (*P.DATO <> VALOR) HACER
        ANT := P;  P := *P.prox;
     FIN MIENTRAS;
     SI (P = NIL) ENTONCES
        ESCRIBIR("NO SE ENCUENTRA...");
     { si lo encontré (P<>NIL) → sigue en la parte 2 }
```

---

## 40 · Algoritmo de eliminación — proceso (1/2) *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 29). Resalta en negrita la condición `(P <> NIL) Y (*P.DATO <> VALOR)`:*

```
PROCESO
  SI (PRIM = NIL) ENTONCES
     ESCRIBIR("LISTA VACÍA... NADA PARA BORRAR");
  SINO
     P := PRIM;  ANT := NIL;
     MIENTRAS (P <> NIL) Y (*P.DATO <> VALOR) HACER
        ANT := P;  P := *P.prox;
     FIN MIENTRAS;
     SI (P = NIL) ENTONCES
        ESCRIBIR("NO SE ENCUENTRA...");
     { si lo encontré (P<>NIL) → sigue en la parte 2 }
```

---

## 41 · Algoritmo de eliminación — proceso (2/2): borrar el nodo

**PSEUDOCÓDIGO · SIMPLE**

```
     { … viene de la parte 1: P apunta al nodo a eliminar }
     SINO
        SI (P = PRIM) ENTONCES
           PRIM := *P.prox;               { CASO 1 o 2 }
        SINO
           *ANT.prox := *P.prox;          { CASO 3 o 4 }
        FIN SI;
        DISPONER(P);      { hay que liberar memoria }
     FIN SI;
  FIN SI;
FIN ACCION.
```

---

## 42 · Algoritmo de eliminación — proceso (2/2) *(ampliación)*

*Ampliación del código de la diapositiva anterior (pie: 30). Resalta `DISPONER(P);` en amarillo:*

```
     { … viene de la parte 1: P apunta al nodo a eliminar }
     SINO
        SI (P = PRIM) ENTONCES
           PRIM := *P.prox;               { CASO 1 o 2 }
        SINO
           *ANT.prox := *P.prox;          { CASO 3 o 4 }
        FIN SI;
        DISPONER(P);      { hay que liberar memoria }
     FIN SI;
  FIN SI;
FIN ACCION.
```

---

## 43 · Buscando el valor a eliminar

**ELIMINACIÓN · DOBLE**

```
LEER(VALOR);
P := PRIM;
MIENTRAS (P <> NIL) Y (*P.DATO <> VALOR) HACER
   P := *P.prox;
FIN MIENTRAS;
{ tampoco hace falta ANT: ya tengo *P.ant }
```

- Antes de DISPONER(P), siempre hay que decidir en cuál de los 4 casos cayó la búsqueda.

---

## 44 · Buscando el valor a eliminar *(duplicada)*

> [!info] Diapositiva repetida
> Esta página es idéntica a la anterior (mismo pie: 31), con el mismo tamaño de letra. No es una ampliación.

**ELIMINACIÓN · DOBLE**

```
LEER(VALOR);
P := PRIM;
MIENTRAS (P <> NIL) Y (*P.DATO <> VALOR) HACER
   P := *P.prox;
FIN MIENTRAS;
{ tampoco hace falta ANT: ya tengo *P.ant }
```

- Antes de DISPONER(P), siempre hay que decidir en cuál de los 4 casos cayó la búsqueda.

---

## 45 · Único nodo — vuelve a vacía

**ELIMINACIÓN · DOBLE · CASO 1**

```
  PRIM,ULT,P
       ✕
   [ |5| ]
```

*(El nodo 5 aparece sombreado y con borde punteado: es el que se libera.)*

**ACCIONES**

```
Condición: PRIM = ULT

PRIM := NIL;  ULT := NIL;
DISPONER(P);
```

*Se libera el único nodo y ambos punteros externos vuelven a NIL.*

---

## 46 · Eliminar el primer nodo

**ELIMINACIÓN · DOBLE · CASO 2**

```
     P          PRIM
     ✕            ↓
 [ |3| ] ┄┄→ [ |5| ] ──→ [ |6| ]
                 ↓
                NIL
```

*(El nodo 3 se libera; en naranja, PRIM apuntando al nodo 5 y el ant del 5 apuntando a NIL.)*

**ACCIONES**

```
Condición: P = PRIM

PRIM := *P.prox;
*PRIM.ant := NIL;
DISPONER(P);
```

*PRIM se corre un lugar y el nuevo primero pasa a tener ant = NIL.*

---

## 47 · Eliminar en el medio — caso normal

**ELIMINACIÓN · DOBLE · CASO 3**

```
                  P
                  ✕
         ╭────────────────────→      (nuevo prox: 5 → 8)
 [ |5| ] ┄┄→ [ |6| ] ┄┄→ [ |8| ]
         ←────────────────────╯      (nuevo ant: 8 → 5)
```

*(El nodo 6 se libera; en naranja, los dos enlaces nuevos entre 5 y 8.)*

**ACCIONES**

```
Condición: *P.DATO = VALOR

*(*P.prox).ant := *P.ant;
*(*P.ant).prox := *P.prox;
DISPONER(P);
```

*Cada eliminación toca dos enlaces: el de antes y el de después.*

---

## 48 · Eliminar el último nodo

**ELIMINACIÓN · DOBLE · CASO 4**

```
    ULT          P
     ↓           ✕
     ╭────────────────────→ NIL   (nuevo prox: 6 → NIL)
 [ |6| ] ┄┄→ [ |8| ]
```

*(El nodo 8 se libera; en naranja, el enlace nuevo de 6 a NIL. ULT ya apunta al 6.)*

**ACCIONES**

```
Condición: P = ULT

ULT := *P.ant;
*ULT.prox := NIL;
DISPONER(P);
```

*El nuevo último pasa a ser ULT.*

---

## 49 · Algoritmo de eliminación doble — declaración

**PSEUDOCÓDIGO · DOBLE**

```
(COMIENZA LA ACCIÓN…)
ACCION ELIM_DOBLE ES
  (VALOR: ENTERO;
   PRIM, ULT: PUNTERO A NODO);

  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
    ant:  PUNTERO A NODO;
  FIN REGISTRO;

  P: PUNTERO A NODO;
```

**Lectura**

- Alcanza con un único puntero de trabajo, P: el anterior se lee con *P.ant, no hace falta recorrerlo con ANT.
- PRIM y ULT pueden cambiar los dos, y nunca en la misma rama: por eso van los 4 casos por separado.

> [!bug] Errata de la filmina
> - Falta **`AMBIENTE`** antes del `NODO` (esta declaración no tiene ampliación con la que comparar).
> - "nunca en la misma rama" no es cierto: en el CASO 1 (diapositivas 45 y 51) PRIM y ULT cambian **los dos en la misma rama** (`PRIM := NIL;  ULT := NIL;`).

---

## 50 · Algoritmo de eliminación doble — proceso (1/2): búsqueda

**PSEUDOCÓDIGO · DOBLE**

```
PROCESO
  SI (PRIM = NIL) ENTONCES
     ESCRIBIR("LISTA VACÍA... NADA PARA BORRAR");
  SINO
     P := PRIM;
     MIENTRAS (P <> NIL) Y (*P.DATO <> VALOR) HACER
        P := *P.prox;
     FIN MIENTRAS;
     SI (P = NIL) ENTONCES
        ESCRIBIR("NO SE ENCUENTRA...");
     { si lo encontré (P<>NIL): ya tengo *P.ant → parte 2 }
```

---

## 51 · Algoritmo de eliminación doble — proceso (2/2): los 4 casos

**PSEUDOCÓDIGO · DOBLE**

**CASOS 1 Y 2**

```
SI (PRIM = ULT) ENTONCES   {1}
   PRIM := NIL;  ULT := NIL;
SINO SI (P = PRIM) ENTONCES {2}
   PRIM := *P.prox;
   *PRIM.ant := NIL;
```

**CASOS 4 Y 3**

```
SINO SI (P = ULT) ENTONCES {4}
   ULT := *P.ant;
   *ULT.prox := NIL;
SINO                       {3}
   *(*P.prox).ant := *P.ant;
   *(*P.ant).prox := *P.prox;
FIN SI;
```

```
DISPONER(P);
FIN SI;   { cierra el SI (P = NIL) de la parte 1 }
FIN SI;   { cierra el SI (PRIM = NIL) de la parte 1 }
FIN ACCION.
```

*4 casos, no 2: en la doble no se puede fusionar CASOS 1/2 ni CASOS 3/4 como en la simple — cada uno toca punteros distintos.*

> [!bug] Errata de la filmina
> Falta el **`SINO`** del `SI (P = NIL) ENTONCES ESCRIBIR("NO SE ENCUENTRA...");` de la parte 1. En la versión simple (diapositiva 41) la parte 2 empieza con ese `SINO`; acá arranca directo con `SI (PRIM = ULT)`, pero después se cierra con `FIN SI;   { cierra el SI (P = NIL) de la parte 1 }`. Tal como está, si P = NIL se ejecutarían los casos (y `DISPONER(P)`) con P en NIL.
> Los enganches de los 4 casos están bien.

---

## 52 · Lo esencial de hoy

**SÍNTESIS**

1. **4 casos, misma lógica siempre**
   Vacía, antes del primero, en el medio, después del último: en inserción y en eliminación.
2. **Buscar antes de actuar**
   Toda inserción y eliminación empieza con un recorrido que ubica P (y ANT si hace falta).
3. **La doble cambia el cómo, no el qué**
   El puntero ant reemplaza el recorrido con ANT; ULT evita recorrer para llegar al final.
4. **Nunca hay que olvidar DISPONER**
   Eliminar un nodo sin liberar su memoria deja un nodo colgado e inaccesible.

---

## 53 · Cierre

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

**¡Eso es Inserción y Eliminación!**

Vimos los 4 casos de cada operación, cómo se buscan y cómo cambia la solución entre listas simples y dobles.

*Próxima clase: Recorridos y Listas Circulares*

---

Sigue en [[9 — Pilas y Colas con Listas]]
