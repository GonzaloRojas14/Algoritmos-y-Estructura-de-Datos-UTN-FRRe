---
tipo: campus
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
tema: "TEMA VI: Listas"
titulo_original: 12-LISTAS Parte II.pptx
diapositivas: 12
fuente: Presentación de Google publicada, enlazada en el campus (TEMA VI — Listas)
tags:
  - AED
  - campus
  - listas
---

# 12 — Listas Parte II (Cómo borrar en listas simples)

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 12 diapositivas de **12-LISTAS Parte II.pptx**, la presentación que enlaza el campus como "Cómo Borrar en Listas Simples". PDF: [[12-LISTAS Parte II.pdf]] (carpeta `originales/`).
> Los diagramas de nodos están pasados a texto. En la filmina, lo nuevo (el enlace que se crea) está en **rojo** y el enlace que se corta tiene una **✕**; acá se indica con `─╳→` y con una línea debajo de cada diagrama.

> [!info] Comparación con las filminas 2026
> Es la versión anterior del bloque de eliminación simple de [[8 — Listas (Inserción y Eliminación)]] (diapositivas 30–48): mismos 4 casos, mismos diagramas (3, 5, 6, 8), mismo "Buscando el valor a eliminar… (PREGUNTO POR QUE SALGO… SIGO TRABAJANDO)" y misma notación `*P.prox`, `PRIM`, `ANT`, `DISPONER`. Diferencias: el MIENTRAS usa **`^`** como Y lógico (`(P <> NIL) ^ (*P.DATO <> VALOR)`, en 2026 es `Y`), y el algoritmo final deja los casos como marcadores, `(CASO 1 o 2)` / `(CASO 3 o 4)`, sin escribir las acciones.

[[TEMA VI — Listas — Índice|← Volver al TEMA VI]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**LISTAS**

**UTN FRRe**

**INGENIERÍA EN SISTEMAS DE INFORMACIÓN**
Algoritmos y Estructuras de Datos

---

## 2 · PROCESOS con LISTAS

**PROCESOS con LISTAS**

| | | |
|---|---|---|
| Crear un Nodo | Insertar un elemento | Buscar un elemento |
| Borrar un elemento | Recorrer la lista | Borrar toda la lista |

---

## 3 · Borrar un Elemento

**Borrar un Elemento** — ***Eliminar Nodos*** **en Listas con elementos cargados**

- **CASO 1: UNICO NODO DE LA LISTA.**
    - VUELVE A LISTA VACÍA.
- **CASO 2: ELIMINAR PRIMER NODO.**
    - CAMBIA EL PRIMER NODO.
- **CASO 3: ELIMINACIÓN EN EL MEDIO.**
    - CASO NORMAL.
- **CASO 4: ELIMINACIÓN DEL ULTIMO NODO**
    - CAMBIA EL FINAL DE LA LISTA

---

## 4 · CASO 1: LISTA VACÍA.

> [!example] CASO 1: LISTA VACÍA.
> VUELVE A LISTA VACÍA

```
            P
            ↓
PRIM ─╳→ [ 5 | • ] → NIL        Ant → NIL
PRIM ──→ NIL
```

*Un único nodo (5), apuntado por P. El enlace de PRIM al nodo está tachado y PRIM pasa a NIL (en rojo). Ant está en NIL.*

| CONDICIÓN: | ACCIONES: |
|---|---|
| P = PRIM | PRIM := NIL; |
| (o **ANT = NIL**) | (o **PRIM := \*P.prox;**) |

*Lo que va entre paréntesis está en rojo en la filmina.*

---

## 5 · CASO 2: ELIMINAR PRIMER NODO

> [!example] CASO 2: ELIMINAR PRIMER NODO
> CAMBIA PRIMER ELEMENTO

```
PRIM ─╳→ [ 3 | • ] ──→ [ 5 | • ] → NIL      Ant → NIL
  │         ↑            ↑
  │         P            │
  └──────────────────────┘
```

*El enlace de PRIM al 3 está tachado; la flecha nueva (en rojo) va de PRIM al 5. P apunta al 3; Ant está en NIL.*

**ACCIONES:**

```
PRIM := *P.prox;
```

**CONDICIÓN:**

```
P = PRIM
(o ANT = NIL)
```

*`(o ANT = NIL)` está en rojo en la filmina.*

---

## 6 · CASO 3: ELIMINACIÓN DEL MEDIO

> [!example] CASO 3: ELIMINACIÓN DEL MEDIO
> CASO NORMAL

```
                  Ant
                   ↓
PRIM → [ 3 | • ] → [ 5 | • ] ─────────────→ [ 8 | • ] → NIL
                         ╲╳                   ↑
                           ↘ [ 6 | • ] ───────┘
                                ↑
                                P
```

*El enlace del 5 al 6 está tachado; la flecha nueva (en rojo) va del 5 al 8. Ant apunta al 5 y P al 6.*

**CONDICIÓN:**

```
*P.DATO = VALOR
(o ANT <> NIL)
```

**ACCIONES:**

```
*ANT.prox := *P.prox;
```

*`(o ANT <> NIL)` está en rojo en la filmina.*

---

## 7 · CASO 4: ÚLTIMO ELEMENTO

> [!example] CASO 4: ÚLTIMO ELEMENTO
> CAMBIA EL FINAL DE LA LISTA

```
                  Ant           P
                   ↓            ↓
PRIM → [ 3 | • ] → [ 6 | • ] ─╳→ [ 8 | • ] → NIL
                         │
                         └→ NIL
```

*El enlace del 6 al 8 está tachado; la flecha nueva (en rojo) va del 6 a NIL. Ant apunta al 6 y P al 8.*

**CONDICIÓN:**

```
*P.DATO = VALOR
(o ANT <> NIL)
```

**ACCIONES:**

```
*ANT.prox := NIL;
(o *ANT.prox := *P.prox;)
```

*Lo que va entre paréntesis está en rojo en la filmina.*

---

## 8 · PROCESOS con LISTAS

**PROCESOS con LISTAS**

*(Repite la diapositiva 2.)*

| | | |
|---|---|---|
| Crear un Nodo | Insertar un elemento | Buscar un elemento |
| Borrar un elemento | Recorrer la lista | Borrar toda la lista |

---

## 9 · Antes de eliminar…

*La diapositiva tiene dos estados animados superpuestos:*

1. *Señal de PARE:* "Antes de **eliminar el nodo** tengo otra cosa…"
2. *Lupa sobre la señal de PARE:* "Pues si…debo **buscar el elemento** a eliminar"

*Lo que está en negrita va resaltado en amarillo en la filmina.*

---

## 10 · Buscando el valor a eliminar…

**Buscando el valor a eliminar…**

```
LEER(VALOR);
P := PRIM;
ANT := NIL;
MIENTRAS (P <> NIL) ^ (*P.DATO <> VALOR) HACER
        ANT := P;
        P := *P.prox;
FIN  MIENTRAS
```

> [!question] A QUE SE PARECE?
> *(Una flecha señala la condición del MIENTRAS.)*

> [!tip]
> **(PREGUNTO POR QUE SALGO…  SIGO TRABAJANDO)**

---

## 11 · RESUMIENDO

**RESUMIENDO**

---

## 12 · (COMIENZA LA ACCION…) / (SIGUE…)

**(COMIENZA LA ACCION…)**

```
ACCION ELIM ES (VALOR: ENTERO; PRIM: PUNTERO A NODO);
        NODO = REGISTRO
                DATO: Entero;
                prox: PUNTERO A NODO;
        FIN REGISTRO;

        P, ANT: PUNTERO A NODO;
```

**(SIGUE…)**

```
ALGORITMO
        NUEVO(Q); LEER(*Q.DATO);
        SI (PRIM = NIL) ENTONCES
                ESCRIBIR("LISTA VACÍA... NADA PARA BORRAR")
        SINO
                P := PRIM;
                ANT := NIL;

                MIENTRAS (P <> NIL) ^ (*P.DATO <> VALOR) HACER
                                ANT := P;
                                P := *P.prox;
                FIN  MIENTRAS
               SI (P = NIL) ENTONCES
                        ESCRIBIR("SORRY... NOTHING HERE.")
                SINO
                        SI P = PRIM ENTONCES
                                (CASO 1 o 2)
                        SINO
                                (CASO 3 o 4)
                        FIN SI;

                        DISPONER(P);    HAY QUE LIBERAR MEMORIA

                FIN SI;
        FIN SI;
FIN ACCION;
```

*"HAY QUE LIBERAR MEMORIA" está en amarillo, como comentario al lado de `DISPONER(P);`.*

> [!bug] Errata de la filmina
> `NUEVO(Q); LEER(*Q.DATO);` no corresponde a una eliminación: `Q` **no está declarada** (el ambiente sólo tiene `P, ANT`), el valor a borrar ya llega como parámetro `VALOR` (que es lo que compara el MIENTRAS), y el nodo que se pide con `NUEVO(Q)` nunca se usa ni se libera. Parece copiado del algoritmo de inserción.
