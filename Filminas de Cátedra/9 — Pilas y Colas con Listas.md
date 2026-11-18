---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 9
titulo_original: Pilas y Colas con Listas Enlazadas
archivo_original: 04_Pilas_Colas_Listas_Simples_2.pdf
diapositivas: 17
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - listas
  - punteros
  - pilas
  - colas
---

# 9 — Pilas y Colas con Listas

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 17 diapositivas de **Pilas y Colas con Listas Enlazadas** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[04_Pilas_Colas_Listas_Simples_2.pdf]] (carpeta `PDF originales/`).
> En los diagramas, `[8|•]` es un nodo con DATO = 8 y el puntero PROX al siguiente. Los "CASO 2", "CASO 3" y "CASO 4" remiten a los casos de inserción y eliminación de [[8 — Listas (Inserción y Eliminación)]].

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

**Pilas y Colas**
**con Listas Enlazadas**

Clase — De la lista simple a pilas y colas

Apilar · Desapilar · Encolar · Desencolar

---

## 2 · Objetivos de la clase

**OBJETIVOS DE LA CLASE**

### ¿Qué vamos a aprender hoy?

1. **De la idea a la implementación**
   Ya vimos qué son las pilas (LIFO) y las colas (FIFO); hoy vemos cómo construirlas con nodos y punteros.
2. **Apilar y desapilar**
   Insertar y eliminar siempre en un único extremo: el TOPE.
3. **Encolar y desencolar**
   Insertar por un extremo (FINAL) y eliminar por el otro (FRENTE).
4. **Por qué son casos particulares de la lista simple**
   Cada operación es, en el fondo, uno de los 4 casos de inserción o eliminación que ya conocemos.

---

## 3 · Repaso

**REPASO**

### Pila y cola: LIFO y FIFO

| **P** — Pila — LIFO | **C** — Cola — FIFO |
|---|---|
| Un solo extremo, el TOPE: por ahí se apila y se desapila. El último elemento en entrar es el primero en salir. | Dos extremos: FINAL para encolar, FRENTE para desencolar. El primer elemento en entrar es el primero en salir. |

---

## 4 · Pila

**PILA**

### La pila es una lista simple, con una sola regla

> [!important] Definición
> Por dentro, una pila es una lista enlazada simple: el puntero externo TOPE cumple exactamente el papel de PRIM.

```
  TOPE
   │
   ▼
 [8|•] ──→ [5|•] ──→ [3|•] ──→ NIL
```

*Apilar y desapilar siempre tocan el primer nodo: nunca hace falta recorrer la lista para encontrar dónde.*

---

## 5 · Pila · Apilar (push)

**PILA · APILAR (PUSH)**

### Cómo se arma el nuevo TOPE

```
 TOPE, P
   │
   ▼
 [8|•] ──→ [5|•] ──→ [3|•] ──→ NIL
 (nuevo)
```

*(En la filmina, el nodo 8 y su enlace al 5 están resaltados: es el nodo recién creado, apuntado por TOPE y por P.)*

**ACCIONES**

```
NUEVO(P);
*P.DATO := VALOR;
*P.prox := TOPE;
TOPE := P;
```

> [!warning] El orden importa
> *El nuevo nodo apunta al viejo TOPE antes de que TOPE pase a apuntar a él: si se invierte el orden, se pierde la lista.*

---

## 6 · Pseudocódigo · Pila: algoritmo de apilar (push)

**PSEUDOCÓDIGO · PILA**

### Algoritmo de apilar (push)

**DECLARACIÓN**

```
ACCION APILAR ES
   (TOPE: PUNTERO A NODO;
    VALOR: ENTERO);

  NODO = REGISTRO
    DATO: Entero;
    prox: PUNTERO A NODO;
  FIN REGISTRO;

  P: PUNTERO A NODO;
```

**PROCESO**

```
PROCESO
  NUEVO(P);
  *P.DATO := VALOR;
  *P.prox := TOPE;
  TOPE := P;
FIN ACCION.
```

*TOPE hace exactamente el papel de PRIM: apilar es insertar antes del primero (CASO 2) en una lista simple.*

> [!bug] Errata de la filmina
> - El tipo `NODO` se usa en la lista de parámetros (`TOPE: PUNTERO A NODO`) antes de declararse, y se declara como local de APILAR; DESAPILAR, ENCOLAR y DESENCOLAR no lo declaran. Se entiende que es un tipo global compartido.

> [!warning] Ojo con el pasaje de parámetros
> `TOPE` se modifica dentro de la acción (`TOPE := P;`) y ese cambio tiene que verse afuera. La guía de la cátedra marca el pasaje por referencia con el prefijo `var` (ver [[sintaxis-completa]]), pero **ninguna de las presentaciones de listas lo usa** (tampoco [[8 — Listas (Inserción y Eliminación)]]). Pasa lo mismo con `FRENTE` y `FINAL` en las acciones de cola. En un parcial conviene poner el `var`.

> [!info] Forma de la cabecera
> Acá la cabecera es `ACCION APILAR ES (parámetros);`, con los parámetros **después** de `ES`. Es la misma forma que usa [[8 — Listas (Inserción y Eliminación)]]; en la guía y en las otras presentaciones va `ACCION nombre (parámetros) ES`. Las dos aparecen en material de cátedra.

---

## 7 · Pila · Desapilar (pop)

**PILA · DESAPILAR (POP)**

### Qué pasa con el viejo TOPE

```
   P         TOPE
   ✕          │
   ┊          ▼
 [8|•] ┄┄→ [5|•] ──→ [3|•] ──→ NIL
 (se libera)
```

*(En la filmina, el nodo 8 aparece punteado/sombreado y el enlace de P tachado: es el nodo que se libera con DISPONER. TOPE ya apunta al 5.)*

**ACCIONES**

```
P := TOPE;
VALOR := *P.DATO;
TOPE := *P.prox;
DISPONER(P);
```

> [!tip]
> *Guardar el dato antes de mover TOPE: una vez que TOPE avanza, sólo P conserva el camino al nodo viejo.*

---

## 8 · Pseudocódigo · Pila: algoritmo de desapilar (pop)

**PSEUDOCÓDIGO · PILA**

### Algoritmo de desapilar (pop)

**DECLARACIÓN**

```
ACCION DESAPILAR ES
   (TOPE: PUNTERO A NODO;
    VALOR: ENTERO);

  P: PUNTERO A NODO;
```

**PROCESO**

```
PROCESO
  SI (TOPE = NIL) ENTONCES
     ESCRIBIR("PILA VACÍA");
  SINO
     P := TOPE;
     VALOR := *P.DATO;
     TOPE := *P.prox;
     DISPONER(P);
  FIN SI;
FIN ACCION.
```

> [!important]
> *Antes de tocar nada hay que preguntar si la pila está vacía: desapilar es eliminar el primer nodo (CASO 2).*

---

## 9 · Síntesis · Pila

**SÍNTESIS · PILA**

### Por qué apilar y desapilar son instantáneos

1. **Siempre tocan la cabeza**
   TOPE = PRIM: nunca hace falta recorrer nada para encontrar dónde insertar o eliminar.
2. **Por eso son O(1)**
   El tiempo que toman no depende de cuántos elementos tenga la pila.
3. **Comparado con una lista general**
   Insertar o eliminar en el medio (CASO 3) sí exige recorrer con ANT y P: la pila evita ese costo restringiendo dónde se puede tocar.

---

## 10 · Cola

**COLA**

### La cola necesita dos extremos

> [!important] Definición
> También es una lista simple, pero para insertar por el FINAL sin recorrer toda la lista hace falta un segundo puntero externo.

```
 FRENTE              FINAL
   │                   │
   ▼                   ▼
 [8|•] ──→ [5|•] ──→ [3|•] ──→ NIL
```

*Si sólo hubiera FRENTE, encolar obligaría a recorrer toda la lista cada vez para encontrar el último nodo.*

---

## 11 · Cola · Encolar (enqueue)

**COLA · ENCOLAR (ENQUEUE)**

### Cómo se arma el nuevo FINAL

```
 FRENTE              FINAL
   │                   │
   ▼                   ▼
 [8|•] ──→ [5|•] ──→ [3|•] ──→ NIL
                     (nuevo)
```

*(En la filmina, el nodo 3, el enlace 5 → 3 y el enlace 3 → NIL están resaltados: es el nodo recién encolado, apuntado por FINAL.)*

**ACCIONES**

```
NUEVO(P); *P.DATO := VALOR; *P.prox := NIL;
SI (FRENTE = NIL) ENTONCES FRENTE := P;
SINO *FINAL.prox := P;
FINAL := P;
```

*Si la cola estaba vacía, el nuevo nodo pasa a ser también el FRENTE.*

---

## 12 · Pseudocódigo · Cola: algoritmo de encolar (enqueue)

**PSEUDOCÓDIGO · COLA**

### Algoritmo de encolar (enqueue)

**DECLARACIÓN**

```
ACCION ENCOLAR ES
   (FRENTE, FINAL:
      PUNTERO A NODO;
    VALOR: ENTERO);

  P: PUNTERO A NODO;
```

**PROCESO**

```
PROCESO
  NUEVO(P);
  *P.DATO := VALOR;
  *P.prox := NIL;
  SI (FRENTE = NIL) ENTONCES
     FRENTE := P;
  SINO
     *FINAL.prox := P;
  FIN SI;
  FINAL := P;
FIN ACCION.
```

*FRENTE y FINAL viajan juntos: encolar es insertar después del último (CASO 4) en una lista simple.*

---

## 13 · Cola · Desencolar (dequeue)

**COLA · DESENCOLAR (DEQUEUE)**

### Qué pasa con el viejo FRENTE

```
   P        FRENTE      FINAL
   ✕          │           │
   ┊          ▼           ▼
 [8|•] ┄┄→ [5|•] ──→ [3|•] ──→ NIL
 (se libera)
```

*(En la filmina, el nodo 8 aparece punteado/sombreado y el enlace de P tachado: es el nodo que se libera. FRENTE ya apunta al 5.)*

**ACCIONES**

```
P := FRENTE;
VALOR := *P.DATO;
FRENTE := *P.prox;
SI (FRENTE = NIL) ENTONCES FINAL := NIL;
DISPONER(P);
```

> [!warning]
> *Si la cola queda vacía después de desencolar, hay que acordarse de poner FINAL en NIL también.*

---

## 14 · Pseudocódigo · Cola: algoritmo de desencolar (dequeue)

**PSEUDOCÓDIGO · COLA**

### Algoritmo de desencolar (dequeue)

**DECLARACIÓN**

```
ACCION DESENCOLAR ES
   (FRENTE, FINAL:
      PUNTERO A NODO;
    VALOR: ENTERO);

  P: PUNTERO A NODO;
```

**PROCESO**

```
PROCESO
  SI (FRENTE = NIL) ENTONCES
     ESCRIBIR("COLA VACÍA");
  SINO
     P := FRENTE;
     VALOR := *P.DATO;
     FRENTE := *P.prox;
     SI (FRENTE=NIL) ENTONCES
        FINAL:=NIL;
     DISPONER(P);
  FIN SI;
FIN ACCION.
```

*Desencolar es eliminar el primer nodo (CASO 2), igual que desapilar — pero acá también hay que cuidar FINAL.*

> [!bug] Errata de la filmina
> El `SI (FRENTE=NIL) ENTONCES` interno no tiene su `FIN SI`. Por la sangría, `DISPONER(P);` va **fuera** de ese SI (se ejecuta siempre en la rama SINO), pero tal como está escrito el único `FIN SI` cierra un solo SI y queda uno abierto. Debería ser:
> ```
>      SI (FRENTE=NIL) ENTONCES
>         FINAL:=NIL;
>      FIN SI;
>      DISPONER(P);
> ```
> Las versiones resumidas de las filminas 11 y 13 ("ACCIONES") también escriben los SI en una línea sin `FIN SI`; en la 12 (ENCOLAR) sí está.

---

## 15 · Pila vs. cola

**PILA VS. COLA**

### Dos reglas distintas sobre la misma lista

1. **Dónde se inserta**
   Pila: siempre en el TOPE (la cabeza). Cola: siempre en el FINAL (la cola de la lista).
2. **Dónde se elimina**
   Pila: siempre en el TOPE (la cabeza). Cola: siempre en el FRENTE (también la cabeza) — igual que la pila.
3. **Punteros externos**
   Pila: uno solo, TOPE. Cola: dos, FRENTE y FINAL, porque inserta y elimina en extremos distintos.
4. **Complejidad**
   Ambas son O(1): ningún caso necesita recorrer la lista, gracias a mantener los punteros justos.

---

## 16 · Síntesis

**SÍNTESIS**

### Lo esencial de hoy

1. **Pila y cola son listas simples con reglas**
   No son estructuras nuevas: son una lista simple a la que sólo se le permite tocar ciertos extremos.
2. **TOPE cumple el rol de PRIM**
   Apilar es insertar antes del primero; desapilar es eliminar el primero.
3. **FRENTE y FINAL dividen el trabajo**
   FRENTE elimina, FINAL inserta: por eso la cola necesita dos punteros externos.
4. **Todo es O(1)**
   Ninguna operación recorre la lista: por eso pilas y colas son tan baratas de usar.

---

## 17 · Cierre

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

### ¡Eso es Pilas y Colas!

Vimos cómo apilar, desapilar, encolar y desencolar son, en el fondo, los mismos casos de inserción y eliminación que ya conocíamos, aplicados sobre una lista simple.

*Próxima clase: nuevas estructuras de datos*
