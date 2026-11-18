---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 7
titulo_original: Listas Introducción
archivo_original: 01_Listas_Introduccion_2.pdf
diapositivas: 16
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - listas
  - punteros
---

# 7 — Listas (Introducción)

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 16 diapositivas de **Listas — Introducción** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[01_Listas_Introduccion_2.pdf]] (carpeta `PDF originales/`).
> El número del pie de cada filmina no coincide con el número de página del PDF desde la 7 (la 7 es una portada de sección sin pie); acá se numera por página del PDF y se indica el pie entre paréntesis cuando difiere.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

**Listas**
**Introducción**

Clase — Estructuras de datos lineales y dinámicas

Nodo · Puntero · Enlace · Clasificación

---

## 2 · Objetivos de la clase

**OBJETIVOS DE LA CLASE**

### ¿Qué vamos a aprender hoy?

1. **Qué es una lista**
   Una estructura de datos lineal y dinámica: una colección de elementos que no están necesariamente consecutivos en memoria.
2. **Cómo se clasifican**
   Particularizadas (pilas y colas) y generalizadas (simples, dobles y circulares).
3. **El nodo y el puntero**
   Cómo se logra el enlace entre elementos sin posiciones consecutivas en memoria.
4. **NUEVO y DISPONER**
   Los verbos para pedir y liberar la memoria de cada nodo de la lista.

---

## 3 · ¿Qué es una lista?

**¿QUÉ ES UNA LISTA?**

### Una estructura lineal y dinámica

> [!important] Definición
> Es una colección de elementos del mismo tipo, originalmente vacía, cuyo tamaño puede crecer o decrecer durante la ejecución del programa según las necesidades del problema.

| **A** — Arreglo (repaso) | **L** — Lista |
|---|---|
| Tamaño fijo, definido de antemano. Los elementos ocupan posiciones consecutivas en memoria: se accede por índice. | Tamaño dinámico: crece y decrece en ejecución. Los elementos (nodos) no están necesariamente consecutivos: se accede siguiendo enlaces. |

---

## 4 · Clasificación

**CLASIFICACIÓN**

### ¿Cómo se clasifican las listas?

```
                         LISTAS
                ┌──────────┴───────────┐
         Particularizadas         Generalizadas
          ┌──────┴─────┐       ┌───────┼────────┐
     Pilas (LIFO) Colas (FIFO) Simples Dobles Circulares
```

*En esta serie de clases nos enfocamos en las Generalizadas: simples, dobles y circulares.*

---

## 5 · Particularizadas · Pilas

**PARTICULARIZADAS · PILAS**

### Pilas: acceso LIFO

**Last In, First Out**

- Una pila (stack) es una lista en la que sólo se accede por un extremo, llamado TOPE.
- Apilar (push) coloca un elemento en el tope; desapilar (pop) retira el último elemento apilado.
- El último en entrar es el primero en salir: por eso LIFO.
- Ejemplos: la pila de llamadas de un programa (call stack), deshacer/rehacer en un editor.

```
      TOPE
       │            APILAR
       ▼          ↙
   ┌────────┐
   │   3    │
   └────────┘     ↗
   ┌────────┐   DESAPILAR
   │   7    │
   └────────┘
   ┌────────┐
   │   10   │
   └────────┘
```

---

## 6 · Particularizadas · Colas

**PARTICULARIZADAS · COLAS**

### Colas: acceso FIFO

**First In, First Out**

- Una cola es una lista en la que se inserta por un extremo (FINAL) y se retira por el otro (FRENTE): el primer dato en entrar es el primero en salir.

```
                  FRENTE               FINAL
                    │                    │
                    ▼                    ▼
  DESENCOLAR ←   [ A ] ──→ [ B ] ──→ [ C ]   ← ENCOLAR
```

*Ejemplos: la cola de impresión, la fila de un banco, un buffer de mensajes.*

---

## 7 · Una pregunta clave

**UNA PREGUNTA CLAVE**

### Si los elementos no están consecutivos en memoria…

¿cómo pasamos de un elemento al siguiente cuando recorremos la lista?

---

## 8 · El nodo *(pie: 07)*

**EL NODO**

### La clave está en el nodo

```
   DATO   PROX
  ┌─────┬─────┐
  │  A  │  •──┼──────→   al siguiente nodo
  └─────┴─────┘
```

| **D** — Campo DATO | **P** — Campo PROX |
|---|---|
| Guarda la información del nodo: un número, un registro, lo que el problema necesite. | Guarda un puntero: la dirección del siguiente nodo de la lista (o NIL si es el último). |

---

## 9 · El puntero *(pie: 08)*

**EL PUNTERO**

### ¿Qué es un puntero?

> [!important] Definición
> Un puntero es un tipo de dato cuyo valor es una dirección de memoria: no guarda el dato en sí, sino dónde encontrarlo.

```
   ( P ) ───→ ┌─────┬─────┐
              │  5  │     │
              └─────┴─────┘
```

**DECLARACIÓN**

```
P: puntero a Nodo;
Nodo = registro
  dato: [tipo de dato];
  prox: puntero a Nodo;
fin registro;
```

**IDEA**

```
P no contiene el dato:
contiene la DIRECCIÓN
de memoria donde vive
el nodo.
Un puntero siempre está
asociado a un tipo.
```

---

## 10 · Pseudocódigo: declarando el nodo y sus punteros *(pie: 09)*

**PSEUDOCÓDIGO**

### Declarando el nodo y sus punteros

**AMBIENTE**

```
P: puntero a Nodo;
Nodo = registro
  dato: [tipo de dato];
  prox: puntero a Nodo;
fin registro;

p, q, PRIM: puntero a Nodo;
```

**LECTURA**

```
Nodo es el registro que
viaja por la lista: guarda
dato y prox.

p y q son punteros de
trabajo (auxiliares).

PRIM es el puntero
externo: apunta siempre
al primer nodo de la lista.
```

> [!bug] Errata de la filmina
> En el mismo AMBIENTE se declara `P: puntero a Nodo;` y después `p, q, PRIM: puntero a Nodo;`. Como el pseudocódigo no distingue mayúsculas, `P` y `p` son la misma variable declarada dos veces. La primera línea parece arrastrada de la filmina anterior (la de "Declaración"); con la segunda alcanza.

---

## 11 · Pseudocódigo: operando con punteros *(pie: 10)*

**PSEUDOCÓDIGO**

### Operando con punteros

**DOS NOTACIONES EQUIVALENTES**

```
*p.dato := [dato];
p^.dato := [dato];

Escribir(*p.dato);
Escribir(p^.dato);

Leer(*p.dato);
Leer(p^.dato);
```

**QUÉ SIGNIFICA**

```
*p  y  p^  significan lo
mismo: "el nodo al que
apunta p".

De estas formas accedo
al registro que contiene
los datos del nodo, para
leerlo o para escribirlo.
```

---

## 12 · Cuidado con los alias *(pie: 11)*

**CUIDADO CON LOS ALIAS**

### ¿Qué sucede si hago  p := q ?

```
        p      q
        │      │
        ▼      ▼
      ┌─────┬─────┐
      │  3  │     │
      └─────┴─────┘
```

- La asignación p := q hace que ambos punteros queden apuntando a la misma dirección de memoria: al mismo nodo.
- No se copia el nodo, sólo la dirección. Cambiar el dato desde p también se ve reflejado si accedo desde q.

---

## 13 · Mapa de la materia *(pie: 12)*

**MAPA DE LA MATERIA**

### Los procesos sobre una lista

1. **Crear un nodo — NUEVO**
   Pedir memoria para un nodo nuevo. Lo vemos en esta clase.
2. **Insertar**
   Enlazar el nodo nuevo en el lugar correcto. Próxima clase: los 4 casos, en simples y dobles.
3. **Buscar / Recorrer**
   Avanzar nodo a nodo siguiendo los punteros. Clase de Recorridos: simples, dobles y circulares.
4. **Eliminar un nodo — DISPONER**
   Desenlazar el nodo y liberar su memoria. Próxima clase: los 4 casos, en simples y dobles.

---

## 14 · NUEVO y DISPONER *(pie: 13)*

**NUEVO Y DISPONER**

### Crear y eliminar un nodo

**CREAR — NUEVO(Q)**

```
Nuevo(Q);
*Q.dato := algo;

{ o bien }

Nuevo(Q);
Leer(*Q.dato);
```

**ELIMINAR — DISPONER(Q)**

```
Disponer(Q);

{ libera la memoria de la }
{ posición apuntada por Q }
```

- NUEVO pide una posición de memoria libre y hace que el puntero quede apuntando a ella. DISPONER hace exactamente lo inverso: libera esa memoria.

---

## 15 · Síntesis *(pie: 14)*

**SÍNTESIS**

### Lo esencial de hoy

1. **Una lista es lineal y dinámica**
   Sus elementos no están necesariamente consecutivos en memoria; el tamaño cambia en ejecución.
2. **Particularizadas vs. generalizadas**
   Pilas (LIFO) y colas (FIFO) restringen el acceso; las generalizadas (simples, dobles, circulares) no.
3. **El nodo enlaza vía punteros**
   Cada nodo guarda su dato y un puntero (prox) que indica dónde está el siguiente.
4. **NUEVO y DISPONER manejan la memoria**
   Piden y liberan la memoria de cada nodo; el resto de los procesos se arma sobre estos dos verbos.

---

## 16 · Cierre

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

### ¡Eso es introducción a Listas!

Vimos qué es una lista, cómo se clasifica, y cómo el nodo y el puntero resuelven el problema de no tener posiciones consecutivas en memoria.

*Próxima clase: Listas Generalizadas — Inserción y Eliminación*

---

Sigue en [[8 — Listas (Inserción y Eliminación)]]
