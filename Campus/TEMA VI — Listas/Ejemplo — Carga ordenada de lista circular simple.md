---
tipo: campus
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
tema: "TEMA VI: Listas"
titulo_original: LISTA-CIRCULAR-SIMPLE-ORDENADA.docx
fuente: Carpeta "Ejemplo de carga ordenada de una lista circular simple" del campus (TEMA VI — Listas)
tags:
  - AED
  - campus
  - listas
  - circular
---

# Ejemplo — Carga ordenada de lista circular simple

> [!abstract] Qué es esta nota
> Transcripción **íntegra** del documento `LISTA-CIRCULAR-SIMPLE-ORDENADA.docx`, el único archivo de la carpeta "Ejemplo de carga ordenada de una lista circular simple" del campus. El original está en [[LISTA-CIRCULAR-SIMPLE-ORDENADA.docx]] (carpeta `originales/`).
> Es el **único material de cátedra que inserta ordenado en una lista circular**. La guía (`LISTA_CIRCULAR`, Complementos 2026) inserta siempre en el 2º lugar, sin orden.

[[TEMA VI — Listas — Índice|← Volver al TEMA VI]] · [[💻 Algoritmos — Índice|← Materia]]

> [!warning] Tiene dos errores de lógica y está incompleto
> Seguido al pie de la letra, **pierde nodos** y **deja algunos fuera de orden**. Abajo está transcripto sin tocar; los problemas están marcados con `[!bug]` y probados con ejemplos en [§ Prueba](#prueba-a-mano).

---

## El documento, tal cual

En el original, `CARGA-NODO` está dentro de un recuadro. Las otras subacciones van sin recuadro.

```
ACCION CARGA LISTA-CIRCULAR- SIMPLE-ORDENADA
AMBIENTE
PRIM, P,Q,A: PUNTERO A NODO
NODO: REGISTRO
	DATO: 
              PROX: PUNTERO A NODO
             FIN
VALOR:
```

```
┌──────────────────────────────┐
│ ACCION   CARGA-NODO ES       │
│    NUEVO (P)                 │
│    P*.DATO:= VALOR           │
│    P*.PROX:=P                │
│ FIN ACCION                   │
└──────────────────────────────┘
```

```
ACCION   LISTA-UNITARIA ES
 M*.PROX:= P
 P*.PROX:= M
SI   M*.DATO > VALOR
ENTONCES  PRIM := P
FINSI
FIN ACCION
```

```
ACCION   BUSQUEDA-POSICION ES
M:= PRIM
MIENTRAS (PRIM <> M*.PROX)  Y  (M*.DATO < VALOR)
A:= M
M:= M*.PROX
FIN
FINACCION
```

```
ACCION   INSERCION-PREVIA ES
P*.PROX := M
Q:= M*.PROX
MIENTRAS (PRIM <> Q)  
A:= Q
Q:= Q*.PROX
FIN
FINACCION
```

Proceso principal:

```
PRIM:= NIL
INGRESAR (VALOR)
MIENTRAS (VALOR <>0) HACER
CARGAR-NODO
M:= PRIM
SI  PRIM = NIL
ENTONCES  PRIM := P
CONTRARIO   SI M = M*.PROX
ENTONCES  LISTA-UNITARIA
CONTRARIO   BUSQUEDA-POSICION
SI PRIM = M
ENTONCES INSERCION-PREVIA
CONTRARIO  SI PRIM = M*.PROX
                        ENTONCES {INSERCION POSTERIOR}
                                              M*.PROX := P
                                               P*.PROX := PRIM
CONTRARIO {INSERCION INTERMEDIA}
                                              a*.PROX := P
                                               P*.PROX := M
FINSI
FINSI
FINSI
FINSI
INGRESAR (VALOR)
FINMIENTRAS
FINACCION
```

> [!bug] Errata del documento — declaraciones
> - `M` se usa en todas las subacciones y en el proceso, pero **no está declarada** (el Ambiente declara `PRIM, P, Q, A`).
> - El proceso llama a `CARGAR-NODO`, pero la subacción se llama **`CARGA-NODO`**.
> - `DATO:` y `VALOR:` no tienen tipo.
> - `NODO: REGISTRO` va con `:`. En el resto del material el tipo se define con `=` (`NODO = REGISTRO`).

> [!info] Notación que no es error
> `P*.DATO` (asterisco después del puntero) es la forma de los Complementos 2026; en las filminas es `*P.DATO`. `INGRESAR` es `LEER`. `FIN`, `FINSI`, `FINACCION` y `FIN ACCION` son cierres; el `MIENTRAS` de las subacciones va sin `HACER`. Todo eso es notación de cátedra (ver [[SINTAXIS]] §10, "Las formas que aparecen en el material").

---

## Cómo está pensado

Cada valor leído se carga en un nodo `P` que, mientras está suelto, **se apunta a sí mismo** (`P*.PROX := P`). Esa es la marca de la circular: con un solo nodo, ese nodo es el primero y el último. Después hay cinco situaciones:

| Situación | Cómo la reconoce | Qué hace |
|---|---|---|
| **Lista vacía** | `PRIM = NIL` | `PRIM := P`. Como `P` ya se apunta a sí mismo, es una circular de un nodo |
| **Un solo nodo** | `M = M*.PROX`: el primero se apunta a sí mismo | `LISTA-UNITARIA`: los dos nodos se apuntan entre sí. Si el viejo es mayor, el nuevo pasa a ser `PRIM` |
| **Va antes del primero** | después de `BUSQUEDA-POSICION`, `M` sigue en `PRIM` | `INSERCION-PREVIA` |
| **Va al final** | `M` quedó en el último (`M*.PROX = PRIM`) | el último apunta al nuevo y el nuevo a `PRIM` |
| **Va en el medio** | ninguna de las anteriores | `A*.PROX := P`, `P*.PROX := M`: igual que en la simple |

**`BUSQUEDA-POSICION`** es la búsqueda de la simple adaptada a la circular. Avanza con `M`, guardando el anterior en `A`, mientras `M` no sea el último (`PRIM <> M*.PROX`) y su dato sea menor que el valor. En la circular no se puede cortar con `M <> NIL`, porque nunca llega a `NIL`. El corte es "el siguiente es el primero", la misma idea que la guía (`*T.SIG <> PRIMERO`).

**`INSERCION-PREVIA`** es el caso que diferencia la circular de la simple. Si el nuevo va antes del primero, además de `P*.PROX := M` hay que conseguir que **el último** apunte al nuevo, porque el último es el que apunta al primero. Para eso recorre con `Q` hasta dar la vuelta, y al terminar `A` queda en el último.

> [!bug] Errata del documento — `INSERCION-PREVIA` no termina
> El ciclo deja a `A` parado en el último nodo, pero **nunca hace `A*.PROX := P` ni `PRIM := P`**. El nuevo nodo apunta al primero, pero nadie apunta a él y `PRIM` no cambia: **el nodo queda fuera de la lista**. Para completarlo, faltan esas dos asignaciones después del `FIN` del `MIENTRAS`. Es lo mismo que hace la guía al eliminar el primero de una circular: busca el último y lo engancha al nuevo primero.

> [!bug] Errata del documento — el último nodo no se compara
> `BUSQUEDA-POSICION` se detiene en el último nodo **sin mirar su dato** (la primera condición ya es falsa). Después, el proceso toma "`M` es el último" como "va al final" (`INSERCION POSTERIOR`), pero puede ser que el valor vaya **antes** del último. Falta preguntar si `M*.DATO < VALOR`: si se cumple va después, y si no va en el medio, entre `A` y `M`.
> Con 2 nodos no pasa, porque ese caso lo resuelve `LISTA-UNITARIA`, que sí compara. Falla desde 3 nodos.

---

## Prueba a mano

Se siguió el algoritmo **tal cual**, sin corregir nada. La lista se muestra desde `PRIM` dando una vuelta.

| Se cargan | Resultado | ¿Bien? | Por qué |
|---|---|---|---|
| 30, 10 | 10 → 30 → (vuelve a 10) | ✅ | el segundo valor lo resuelve `LISTA-UNITARIA`, que sí compara |
| 10, 30, 20 | 10 → 30 → **20** | ❌ | el 20 va antes del último (30), pero cae en `INSERCION POSTERIOR` |
| 10, 20, 40, 30 | 10 → 20 → 40 → **30** | ❌ | lo mismo con el 30 y el 40 |
| 20, 30, 5 | 20 → 30 (**el 5 se perdió**) | ❌ | `INSERCION-PREVIA` no engancha el último ni mueve `PRIM` |

Traza del caso 10, 30, 20, al cargar el 20:

```
PRIM → [10] → [30] → (vuelve a [10])

BUSQUEDA-POSICION:  M = 10   ¿PRIM <> M*.PROX? (30) sí   ¿10 < 20? sí  → A = 10, M = 30
                    M = 30   ¿PRIM <> M*.PROX? (10 = PRIM) NO → corta, sin comparar 30 con 20
¿PRIM = M?        no
¿PRIM = M*.PROX?  sí → INSERCION POSTERIOR: 30 → 20 → PRIM
Queda: 10 → 30 → 20   (debería ser 10 → 20 → 30)
```

---

## Lo que deja este ejemplo

Aunque tiene errores, muestra los **casos de la inserción ordenada en una circular simple**, que no aparecen en ningún otro material de cátedra:

1. Vacía → el nodo se apunta a sí mismo.
2. Un solo nodo → los dos se apuntan entre sí; según el orden, cambia o no `PRIM`.
3. Antes del primero → hay que **encontrar el último** para que apunte al nuevo, y mover `PRIM`.
4. Al final → el último apunta al nuevo y **el nuevo apunta a `PRIM`** (no a `NIL`).
5. En el medio → igual que la simple: `A*.PROX := P`, `P*.PROX := M`.

La condición de corte del recorrido es **"el siguiente es el primero"**, no `NIL`. Ver también [[3.02 — Listas Doblemente Enlazadas y Circulares]] y el código del repo en [[Repo isi-aed — Listas (C, Python y pseudocódigo)]].
