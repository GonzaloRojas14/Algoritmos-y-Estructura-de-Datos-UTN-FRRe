---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 5
titulo_original: Búsqueda y Ordenamiento — Clase 2 — Algoritmos sobre arreglos
archivo_original: Arreglos_Clase2_BusquedaYOrdenamiento_2.1.pdf
diapositivas: 43
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - arreglos
  - busqueda
  - ordenamiento
---

# 5 — Búsqueda y Ordenamiento

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 43 diapositivas de **Búsqueda y Ordenamiento — Clase 2 — Algoritmos sobre arreglos** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[Arreglos_Clase2_BusquedaYOrdenamiento_2.1.pdf]] (carpeta `PDF originales/`).
> Todas las diapositivas llevan el pie `AED · UTN FRRe · Búsqueda y Ordenamiento — Clase 2` y el número; no se repite en cada sección. Los rótulos chicos en naranja que encabezan cada diapositiva van en *cursiva mayúscula* debajo del título. Las diapositivas 9, 11, 15, 20, 28, 30, 33, 35 y 39 son el bloque de código de la anterior, ampliado a pantalla completa.

> [!info] Cambios respecto de la versión anterior
> Comparada con [[5 — Búsqueda y Ordenamiento (versión anterior)]] (33 diapositivas de Google Slides):
> - **Orden**: ahora primero se ve **Ordenamiento** (Parte 1) y después **Búsqueda** (Parte 2).
> - **Métodos nuevos o renombrados**: aparece la **Burbuja** (ordenamiento por intercambio directo, con `PARA` fijo) y su **variante con bandera** `hubo_cambio`, que reemplaza al viejo "Intercambio" con `Bandera` / `Mientras NO Bandera`. La búsqueda "lineal" ahora se llama **Secuencial**, y se agrega la **Secuencial con corte anticipado** para arreglos ordenados. Se mencionan (sin pseudocódigo) Selección de máximo, Selección bidireccional, Inserción binaria, **Shell** y **Quicksort**.
> - **Nuevo**: tablas comparativas (Burbuja/Selección/Inserción, Secuencial/Centinela, comparación final), casos de uso de cada método, complejidad en O(n²), O(n), O(log n).
> - **Se sacó**: las 7 diapositivas de relleno de la plantilla, las FAQ, las pruebas de escritorio en tabla de variables (`dato | J | i | A[i]`), el ejemplo de búsqueda del menor, el análisis mejor/peor/promedio de la lineal y la analogía de las cartas con imágenes. Las trazas ahora son tablas de pasadas sobre el arreglo `8 3 5 1 9 2`.
> - **Notación**: toda en mayúsculas y uniforme (`PARA i:=1 HASTA n-1 HACER`, `FIN_PARA;`, `SI ... ENTONCES` / `SI_NO` / `FIN_SI;`, `MIENTRAS ... HACER` / `FIN_MIENTRAS;`, conector `Y`), dentro de `Accion NOMBRE (v: arreglo [1..n] de entero) ES; Ambiente ... Proceso ... FinAccion.`. Cambian los nombres: `A` → `v`, `x` (auxiliar) → `aux`, `ESC` → `Escribir`, `Leer` → `LEER`, `izq`/`der` → `inicio`/`fin`, `MIN` → `pos_min`. Desaparecen `Contrario`, `^` y la mezcla de mayúsculas/minúsculas.
> - **Erratas viejas**: el `DIV 2 DIV 2` de la binaria **ya no está** (ahora `medio := (inicio + fin) DIV 2;`). Pero la binaria nueva tiene un error propio (`SI encontrado` sin variable `encontrado`), y aparecen erratas nuevas en la Secuencial ordenada y en las tablas de Centinela: ver los callouts `[!bug]` de las diapositivas 26, 29–31, 34, 36, 38–39 y 41.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

**Búsqueda y Ordenamiento**

Clase 2 — Algoritmos sobre arreglos

*Burbuja · Selección · Inserción · Secuencial · Centinela · Binaria*

(Decoración: una fila de celdas `8 · 3 · 5 · 1 · 9 · 2` con el 5 resaltado, seguida del número de diapositiva `01`.)

---

## 2 · ¿Qué vamos a aprender hoy?

*OBJETIVOS DE LA CLASE*

1. **Por qué ordenar y por qué buscar**
   La relación costo/beneficio entre ambos procesos sobre un arreglo.
2. **Métodos de ordenamiento**
   Burbuja, Selección e Inserción, con sus variantes más comunes.
3. **Métodos de búsqueda**
   Secuencial, Centinela y Binaria, en arreglos ordenados y desordenados.
4. **Cuándo usar cada uno**
   Casos de uso, ventajas y el costo de cada algoritmo.

---

## 3 · ¿Por qué ordenar y por qué buscar?

*ANTES DE EMPEZAR*

| Ordenar | Buscar |
|---|---|
| Reorganizar los componentes de un arreglo según un criterio de orden (creciente o decreciente). | Encontrar la posición de un valor dentro del arreglo (o determinar que no está). |

> [!tip] Ordenar tiene un costo, pero se amortiza
> En un arreglo ordenado se puede buscar mucho más rápido (Búsqueda Binaria). Si el arreglo se va a recorrer o consultar muchas veces, ordenar primero conviene. Si se busca una sola vez, puede no valer la pena pagar el costo de ordenar.

---

## 4 · Parte 1 — Ordenamiento

*PARTE 1*

**Ordenamiento**

Burbuja, Selección e Inserción

---

## 5 · ¿Qué es ordenar un arreglo?

*ORDENAMIENTO*

> [!important] Definición
> Reorganizar los componentes de un arreglo según un **criterio de orden** (creciente o decreciente).

| C — **Criterio** | I — **In-place** | C — **Costo** |
|---|---|---|
| Se define de antemano si el orden es creciente (v[i] ≤ v[i+1]) o decreciente. | Los 3 métodos de hoy reordenan el mismo arreglo, sin usar uno auxiliar completo. | Se mide en comparaciones e intercambios/movimientos de elementos. |

---

## 6 · Burbuja: ¿cómo funciona?

*ORDENAMIENTO POR INTERCAMBIO DIRECTO*

Compara pares de elementos adyacentes; si están en el orden incorrecto, los intercambia. En cada pasada, el elemento más grande "burbujea" hasta su posición final.

*Antes de la pasada 1*

| 8 | 3 | 5 | 1 | 9 | 2 |
|---|---|---|---|---|---|

*se comparan pares adyacentes y se intercambian si están desordenados*

*Después de la pasada 1*

| 3 | 5 | 1 | 8 | 2 | **9** |
|---|---|---|---|---|---|

El 9 (resaltado en naranja): *en su posición final*

---

## 7 · Burbuja: recorrido completo

*ORDENAMIENTO POR INTERCAMBIO DIRECTO*

Aplicando el algoritmo completo: en cada pasada se fija un elemento más por la derecha, hasta la pasada sin intercambios.

En **negrita**, las celdas resaltadas en naranja (ya en su posición final).

| Posición | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Inicial | 8 | 3 | 5 | 1 | 9 | 2 |
| Pasada 1 | 3 | 5 | 1 | 8 | 2 | **9** |
| Pasada 2 | 3 | 1 | 5 | 2 | **8** | **9** |
| Pasada 3 | 1 | 3 | 2 | **5** | **8** | **9** |
| Pasada 4 | 1 | 2 | **3** | **5** | **8** | **9** |
| Pasada 5 | **1** | **2** | **3** | **5** | **8** | **9** |

> [!note] Verificación de la traza
> Se rehízo la traza con el pseudocódigo de la diapositiva 8 (`n = 6`, 5 pasadas): todas las filas coinciden. La pasada 5 (`j` de 1 a 1) no hace intercambios.

---

## 8 · Pseudocódigo de la Burbuja

*BURBUJA*

```
Accion BURBUJA (v: arreglo [1..n] de entero) ES;
Ambiente
    i, j, aux: entero;
Proceso
    PARA i:=1 HASTA n-1 HACER
        PARA j:=1 HASTA n-i HACER
            SI v[j] > v[j+1] ENTONCES
                aux := v[j];
                v[j] := v[j+1];
                v[j+1] := aux;
            FIN_SI;
        FIN_PARA;
    FIN_PARA;
FinAccion.
```

**Lectura del algoritmo**

- `i` cuenta las pasadas: se necesitan n-1 como máximo.
- `j` recorre los pares adyacentes; el rango se achica (`n-i`) porque el final ya está ordenado.
- Si `v[j] > v[j+1]`, se intercambian con una variable auxiliar.
- **Complejidad:** ≈ n²/2 comparaciones en el peor caso.

---

## 9 · *(código ampliado)* Burbuja

```
Accion BURBUJA (v: arreglo [1..n] de entero) ES;
Ambiente
    i, j, aux: entero;
Proceso
    PARA i:=1 HASTA n-1 HACER
        PARA j:=1 HASTA n-i HACER
            SI v[j] > v[j+1] ENTONCES
                aux := v[j];
                v[j] := v[j+1];
                v[j+1] := aux;
            FIN_SI;
        FIN_PARA;
    FIN_PARA;
FinAccion.
```

---

## 10 · Casos de uso y variante con bandera

*BURBUJA*

**Casos de uso**

- Fines didácticos: es el método más simple de entender e implementar.
- Arreglos muy pequeños, donde la eficiencia no es crítica.
- Detectar si un arreglo ya está ordenado (con la variante de bandera).

> [!tip] Variante: corte anticipado (bandera)
> Si en una pasada no hubo intercambios, el arreglo ya está ordenado: se corta el ciclo antes. Mejor caso: O(n) en vez de O(n²).

```
i := 1;
hubo_cambio := VERDADERO;
MIENTRAS (i<=n-1) Y (hubo_cambio) HACER
    hubo_cambio := FALSO;
    PARA j:=1 HASTA n-i HACER
        SI v[j] > v[j+1] ENTONCES
            aux := v[j];
            v[j] := v[j+1];
            v[j+1] := aux;
            hubo_cambio := VERDADERO;
        FIN_SI;
    FIN_PARA;
    i := i+1;
FIN_MIENTRAS;
```

---

## 11 · *(código ampliado)* Burbuja con bandera

```
i := 1;
hubo_cambio := VERDADERO;
MIENTRAS (i<=n-1) Y (hubo_cambio) HACER
    hubo_cambio := FALSO;
    PARA j:=1 HASTA n-i HACER
        SI v[j] > v[j+1] ENTONCES
            aux := v[j];
            v[j] := v[j+1];
            v[j+1] := aux;
            hubo_cambio := VERDADERO;
        FIN_SI;
    FIN_PARA;
    i := i+1;
FIN_MIENTRAS;
```

---

## 12 · Selección: ¿cómo funciona?

*ORDENAMIENTO POR SELECCIÓN DIRECTA*

En cada pasada busca el mínimo del resto del arreglo y lo coloca en su posición final con un único intercambio. A diferencia de la Burbuja, minimiza la cantidad de intercambios.

*Antes de la pasada 1 (se busca el mínimo)*

| 8 | 3 | 5 | **1** | 9 | 2 |
|---|---|---|---|---|---|

El 1 (resaltado en rojo): *mínimo encontrado*

*Después de la pasada 1 (se intercambia con la posición 1)*

| **1** | 3 | 5 | 8 | 9 | 2 |
|---|---|---|---|---|---|

El 1 (resaltado en naranja): *en su posición final*

---

## 13 · Selección: recorrido completo

*ORDENAMIENTO POR SELECCIÓN DIRECTA*

Aplicando el algoritmo completo: en cada pasada se fija un elemento más por la izquierda, con un único intercambio por pasada.

En **negrita**, las celdas resaltadas en naranja (ya en su posición final).

| Posición | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Inicial | 8 | 3 | 5 | 1 | 9 | 2 |
| Pasada 1 | **1** | 3 | 5 | 8 | 9 | 2 |
| Pasada 2 | **1** | **2** | 5 | 8 | 9 | 3 |
| Pasada 3 | **1** | **2** | **3** | 8 | 9 | 5 |
| Pasada 4 | **1** | **2** | **3** | **5** | 9 | 8 |
| Pasada 5 | **1** | **2** | **3** | **5** | **8** | **9** |

> [!note] Verificación de la traza
> Se rehízo con el pseudocódigo de la diapositiva 14: todas las filas coinciden (en cada pasada el mínimo está en la posición 4, 6, 6, 6 y 6 respectivamente).

---

## 14 · Pseudocódigo de la Selección

*SELECCIÓN*

```
Accion SELECCION (v: arreglo [1..n] de entero) ES;
Ambiente
    i, j, pos_min, aux: entero;
Proceso
    PARA i:=1 HASTA n-1 HACER
        pos_min := i;
        PARA j:=i+1 HASTA n HACER
            SI v[j] < v[pos_min] ENTONCES
                pos_min := j;
            FIN_SI;
        FIN_PARA;
        SI pos_min <> i ENTONCES
            aux := v[i];
            v[i] := v[pos_min];
            v[pos_min] := aux;
        FIN_SI;
    FIN_PARA;
FinAccion.
```

**Lectura del algoritmo**

- `pos_min` guarda la posición del menor valor visto hasta ahora en esta pasada.
- `j` recorre desde i+1 buscando algo menor que `v[pos_min]`.
- El intercambio se hace **una sola vez por pasada**, al final.
- **Complejidad:** ≈ n²/2 comparaciones, pero máximo n-1 intercambios.

---

## 15 · *(código ampliado)* Selección

```
Accion SELECCION (v: arreglo [1..n] de entero) ES;
Ambiente
    i, j, pos_min, aux: entero;
Proceso
    PARA i:=1 HASTA n-1 HACER
        pos_min := i;
        PARA j:=i+1 HASTA n HACER
            SI v[j] < v[pos_min] ENTONCES
                pos_min := j;
            FIN_SI;
        FIN_PARA;
        SI pos_min <> i ENTONCES
            aux := v[i];
            v[i] := v[pos_min];
            v[pos_min] := aux;
        FIN_SI;
    FIN_PARA;
FinAccion.
```

---

## 16 · Casos de uso y variantes

*SELECCIÓN*

| Casos de uso | Variantes |
|---|---|
| • Cuando el costo de **escribir/intercambiar** es alto (por ejemplo, memoria externa costosa).<br>• Se necesita un número acotado y predecible de intercambios: máximo n-1.<br>• Arreglos pequeños o medianos, sin requerir estabilidad. | • **Selección de máximo:** igual lógica, pero se busca el mayor y se coloca al final del rango.<br>• **Selección bidireccional:** en la misma pasada se buscan el mínimo y el máximo, reduciendo a la mitad el número de pasadas.<br>• *Se mencionan como variantes conceptuales; no se desarrolla su pseudocódigo completo hoy.* |

---

## 17 · Inserción: ¿cómo funciona?

*ORDENAMIENTO POR INSERCIÓN DIRECTA*

Construye el arreglo ordenado de a poco: toma cada elemento y lo inserta en su posición correcta dentro de la porción ya ordenada, desplazando los mayores a la derecha. Es análogo a ordenar cartas en la mano.

*Antes de insertar v[3]=5 (ordenado: 3, 8 | por insertar: 5, 1)*

| 3 | 8 | **5** | 1 |
|---|---|---|---|

El 5 (resaltado en rojo): *aux (a insertar)*. El 3 y el 8 están en verde (porción ordenada).

*Después de insertar (8 se desplazó una posición a la derecha)*

| 3 | **5** | 8 | 1 |
|---|---|---|---|

El 5 (resaltado en naranja): *insertado en su lugar*

---

## 18 · Inserción: recorrido completo

*ORDENAMIENTO POR INSERCIÓN DIRECTA*

Aplicando el algoritmo completo: en cada paso crece por la izquierda la porción ya ordenada, insertando un elemento nuevo por vez.

En **negrita**, las celdas resaltadas en naranja (porción ya ordenada).

| Posición | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| i=1 | **8** | 3 | 5 | 1 | 9 | 2 |
| i=2 | **3** | **8** | 5 | 1 | 9 | 2 |
| i=3 | **3** | **5** | **8** | 1 | 9 | 2 |
| i=4 | **1** | **3** | **5** | **8** | 9 | 2 |
| i=5 | **1** | **3** | **5** | **8** | **9** | 2 |
| i=6 | **1** | **2** | **3** | **5** | **8** | **9** |

> [!note] Verificación de la traza
> Coincide con el pseudocódigo de la diapositiva 19. La fila `i=1` es el arreglo inicial (el `PARA` empieza en `i:=2`; con un solo elemento, la porción ya está ordenada).

---

## 19 · Pseudocódigo de la Inserción

*INSERCIÓN*

```
Accion INSERCION (v: arreglo [1..n] de entero) ES;
Ambiente
    i, j, aux: entero;
Proceso
    PARA i:=2 HASTA n HACER
        aux := v[i];
        j := i-1;
        MIENTRAS (j>=1) Y (v[j]>aux) HACER
            v[j+1] := v[j];
            j := j-1;
        FIN_MIENTRAS;
        v[j+1] := aux;
    FIN_PARA;
FinAccion.
```

**Lectura del algoritmo**

- `aux` guarda el elemento a insertar antes de sobrescribir su posición.
- El `MIENTRAS` desplaza a la derecha mientras haya elementos mayores que `aux`.
- Al cortar el `MIENTRAS`, `j+1` es la posición correcta para `aux`.
- **Complejidad:** ≈ n²/2 en el peor caso; O(n) si ya está casi ordenado.

---

## 20 · *(código ampliado)* Inserción

```
Accion INSERCION (v: arreglo [1..n] de entero) ES;
Ambiente
    i, j, aux: entero;
Proceso
    PARA i:=2 HASTA n HACER
        aux := v[i];
        j := i-1;
        MIENTRAS (j>=1) Y (v[j]>aux) HACER
            v[j+1] := v[j];
            j := j-1;
        FIN_MIENTRAS;
        v[j+1] := aux;
    FIN_PARA;
FinAccion.
```

---

## 21 · Casos de uso y variante

*INSERCIÓN*

**Casos de uso**

- Datos que llegan de a poco (inserción incremental / streaming).
- Arreglos **casi ordenados**: se acerca a O(n), el mejor caso de los tres métodos.
- Arreglos pequeños, donde su simplicidad compensa su costo cuadrático.

> [!info] Variante: inserción binaria
> En vez de comparar de a uno con el MIENTRAS, se usa Búsqueda Binaria (la vemos más adelante) para encontrar la posición de inserción con menos comparaciones.
>
> *Ojo: reduce las comparaciones, pero los desplazamientos de elementos siguen siendo O(n) por inserción. El costo total no mejora tanto como parece.*

---

## 22 · Burbuja vs. Selección vs. Inserción

*COMPARACIÓN*

| Aspecto | Burbuja | Selección | Inserción |
|---|---|---|---|
| Comparaciones | ≈ n²/2 | ≈ n²/2 | ≈ n²/2 (peor caso) |
| Intercambios / movimientos | Muchos (hasta n²/2) | Pocos: máx. n-1 | Muchos en peor caso; pocos si ya está ordenado |
| Mejor caso | O(n) con bandera | O(n²) siempre | O(n) si ya está ordenado |
| Ventaja principal | Simplicidad; detecta orden | Minimiza escrituras | Eficiente con datos casi ordenados |

---

## 23 · Métodos más eficientes (mención)

*UN PASO MÁS ALLÁ*

Los métodos de hoy son O(n²). Existen métodos más eficientes que no se desarrollan en detalle en esta clase, pero es útil conocer su idea general.

| Shell | Quicksort |
|---|---|
| Generaliza la Inserción: en vez de comparar elementos adyacentes, compara elementos separados por un "salto" (gap) que se va reduciendo. Mueve elementos lejanos más rápido antes de refinar con saltos chicos (el último paso es una Inserción normal, gap=1). | Divide y vencerás: elige un pivote, particiona el arreglo en "menores" y "mayores" que el pivote, y ordena recursivamente cada partición. En promedio es mucho más rápido: O(n log n) vs. O(n²). |
| *Uso: mejora notable sobre Inserción con poco cambio de código.* | *Uso: el más usado en bibliotecas y lenguajes de programación reales.* |

---

## 24 · Parte 2 — Búsqueda

*PARTE 2*

**Búsqueda**

Secuencial, Centinela y Binaria

---

## 25 · ¿Qué es buscar? tres formas de hacerlo

*BÚSQUEDA*

Ya vimos en Clase 1 el recorrido con MIENTRAS y la idea de centinela. Ahora los formalizamos como algoritmos de búsqueda completos.

| Método | Idea | Requiere orden |
|---|---|---|
| **Secuencial** | Recorre y compara uno a uno, en orden. Funciona en cualquier arreglo. | *Requiere orden: No* |
| **Centinela** | Igual idea, pero evita chequear el límite del arreglo en cada vuelta. | *Requiere orden: No* |
| **Binaria** | Divide el rango a la mitad en cada paso, comparando contra el medio. | *Requiere orden: Sí, obligatorio* |

---

## 26 · Secuencial: recorrer y comparar

*BÚSQUEDA SECUENCIAL*

Recorre el arreglo desde el principio, comparando cada elemento con el valor buscado, hasta encontrarlo o llegar al final. No requiere que el arreglo esté ordenado.

*Buscando x = 8*

| 5 | 3 | 9 | **8** | 1 | 2 |
|---|---|---|---|---|---|
| i=1 | i=2 | i=3 | ¡encontrado! | | |

(5, 3 y 9 en gris; 8 en naranja; 1 y 2 sin visitar.)

> Se descartan las posiciones ya visitadas (gris) hasta encontrar el valor en la posición 4. Si el valor no estuviera, se recorrerían las 6 posiciones sin éxito.
> *Peor caso: n comparaciones (recorrer todo el arreglo sin encontrarlo).*

> [!bug] Errata de la filmina
> Esta diapositiva describe una búsqueda que **corta** al encontrar ("hasta encontrarlo o llegar al final"), pero el pseudocódigo de la diapositiva 27 usa un `PARA` que **no corta** (lo dice su propia lectura: "El PARA no corta el recorrido, lo hace total"): con x = 8 sigue comparando 1 y 2. Es un recorrido total que informa todas las ocurrencias.

---

## 27 · Secuencial en un arreglo desordenado

*BÚSQUEDA SECUENCIAL*

```
Accion BUSCAR_SECUENCIAL (v: arreglo [1..n] de entero) ES;
Ambiente
    buscado, i: entero;
Proceso
    LEER(buscado);
    PARA i := 1 HASTA n HACER
      SI v[i] = buscado ENTONCES
        Escribir("Encontrado en la posición: ", i);
      FIN_SI;
    FIN_PARA;
FinAccion.
```

**Lectura y casos de uso**

- La condición (`v[i] = buscado`) no corta la busqueda, solo indica que encontro el valor solicitado.
- El **PARA** no corta el recorrido, lo hace total.
- **Uso:** arreglos pequeños, desordenados, o que se buscan pocas veces (no justifica ordenar antes).

---

## 28 · *(código ampliado)* Secuencial

```
Accion BUSCAR_SECUENCIAL (v: arreglo [1..n] de entero) ES;
Ambiente
    buscado, i: entero;
Proceso
    LEER(buscado);
    PARA i := 1 HASTA n HACER
      SI v[i] = buscado ENTONCES
        Escribir("Encontrado en la posición: ", i);
      FIN_SI;
    FIN_PARA;
FinAccion.
```

---

## 29 · Secuencial con corte anticipado

*VARIANTE EN ARREGLO ORDENADO*

Si el arreglo está ordenado, no hace falta llegar al final: en cuanto v[i] es mayor o igual que x, ya se puede cortar (si no estaba antes, no está).

```
Accion BUSCAR_SECUENCIAL_ORDENADO (v: arreglo [1..n] de entero)
ES;
Ambiente
    buscado, i: entero;
Proceso
    i := 1;
    LEER(buscado);
    MIENTRAS (i<=n) Y (v[i]<buscado) HACER
     SI (v[i]=buscado) ENTONCES
        Escribir("Encontrado en la posición: ", i);
     FIN_SI;
      i := i+1;
    FIN_MIENTRAS;
FinAccion.
```

**Qué cambió**

- La condición pasa de `v[i]<>x` a `v[i]<x`: corta apenas se pasa del valor buscado.
- Se agrega un chequeo final (`v[i]=x`) porque el corte pudo ser por `v[i]>x`.
- Ahorra comparaciones en promedio cuando el valor no está.

> [!bug] Errata de la filmina
> El algoritmo **nunca encuentra nada**: el `SI (v[i]=buscado)` está **dentro** del `MIENTRAS`, y adentro del ciclo siempre vale `v[i]<buscado`, así que esa condición es siempre falsa. Cuando `v[i]=buscado` el ciclo ya terminó y no se escribe nada (ni "encontrado" ni "no se encontró").
> La propia lectura dice que se agrega un **chequeo final** — es decir, el `SI` debería ir **después** del `FIN_MIENTRAS` (como en la Centinela ordenada de la diapositiva 34). Además: la lectura habla de `x` y el código de `buscado`; y con `(i<=n)`, si el valor es mayor que todos, `i` llega a `n+1` y se evalúa `v[n+1]` fuera de rango (salvo evaluación en cortocircuito).

---

## 30 · *(código ampliado)* Secuencial con corte anticipado

```
Accion BUSCAR_SECUENCIAL_ORDENADO (v: arreglo [1..n] de entero)
ES;
Ambiente
    buscado, i: entero;
Proceso
    i := 1;
    LEER(buscado);
    MIENTRAS (i<=n) Y (v[i]<buscado) HACER
     SI (v[i]=buscado) ENTONCES
        Escribir("Encontrado en la posición: ", i);
     FIN_SI;
      i := i+1;
    FIN_MIENTRAS;
FinAccion.
```

> [!bug] Errata de la filmina
> Mismo código y mismo error que la diapositiva 29: el `SI` dentro del ciclo nunca se cumple.

---

## 31 · Centinela: evitar el chequeo de límite

*BÚSQUEDA POR CENTINELA*

En la Secuencial, cada vuelta del MIENTRAS chequea dos condiciones: el límite del arreglo y el valor.

> *Centinela: LEER(**buscado**) -> esa variable será el corte, o el final del arreglo.*

| 5 | 3 | 9 | 1 | 2 | 8 |
|---|---|---|---|---|---|

*posiciones 1..n (datos reales)*

> [!info]
> Si el MIENTRAS termina en una posición ≤ n, el valor estaba realmente en el arreglo. Si termina justo en la posición del centinela (n+1), es porque no se encontró antes: no estaba.

> [!bug] Errata de la filmina
> La diapositiva mezcla dos ideas incompatibles con el resto de la clase:
> - Dice que la **Secuencial** usa un MIENTRAS con dos condiciones, pero la Secuencial de la diapositiva 27 usa un `PARA` y una sola condición.
> - Habla de un centinela en la **posición n+1**, pero el dibujo solo tiene las posiciones 1..n y el algoritmo de la diapositiva 32 no guarda nada en `v[n+1]` (el arreglo es `[1..n]`): corta con `(i<n)`, así que nunca llega a n+1. Con ese algoritmo, "no estaba" se decide con el `SI v[i]=buscado` final, no por la posición en que termina.

---

## 32 · Centinela en un arreglo desordenado

*CENTINELA*

```
Accion BUSCAR_CENTINELA (v: arreglo [1..n] de entero) ES;
Ambiente
    buscado, i: entero;
Proceso
    LEER(buscado);
    i := 1;
    MIENTRAS (i<n) y (v[i]<>buscado) HACER
        i := i+1;
    FIN_MIENTRAS;
    SI v[i]=buscado  ENTONCES
        Escribir("Encontrado en la posición: ", i);
    SI_NO
        Escribir("No se encontró.");
    FIN_SI;
FinAccion.
```

**Lectura del algoritmo**

- El **MIENTRAS** tiene doble condición: `control de tope del arreglo` y `v[i]<>buscado`.
- Al cortar, si `i<tope` fue un dato encontrado; o se encuentra en la posicion final. Se chequea en el condicional
- Menos comparaciones por vuelta que la Secuencial: en la práctica, más rápida.

> [!bug] Errata de la filmina
> La lectura contradice al resto: acá el MIENTRAS de la Centinela tiene **doble** condición (`i<n` y el valor), mientras que la diapositiva 25 dice que la Centinela "evita chequear el límite del arreglo en cada vuelta". Y no tiene "menos comparaciones por vuelta que la Secuencial": la Secuencial (diap. 27) hace una sola comparación de valor por vuelta. El algoritmo en sí es correcto (con `i<n` nunca se sale del arreglo y el `SI` final decide).
> El conector aparece en minúscula (`y`) en este código, a diferencia del `Y` del resto de la presentación.

---

## 33 · *(código ampliado)* Centinela

```
Accion BUSCAR_CENTINELA (v: arreglo [1..n] de entero) ES;
Ambiente
    buscado, i: entero;
Proceso
    LEER(buscado);
    i := 1;
    MIENTRAS (i<n) y (v[i]<>buscado) HACER
         i := i+1;
    FIN_MIENTRAS;
    SI v[i]=buscado ENTONCES
         Escribir("Encontrado en la posición: ", i);
    SI_NO
         Escribir("No se encontró.");
    FIN_SI;
FinAccion.
```

---

## 34 · Variante en ordenado y casos de uso

*CENTINELA*

```
Accion BUSCAR_CENTINELA (v: arreglo [1..n] de entero) ES;
Ambiente
    buscado, i: entero;
Proceso
    LEER(buscado);
    i := 1;
    MIENTRAS (i<n) y (v[i]<buscado) HACER
        i := i+1;
    FIN_MIENTRAS;
    SI v[i]=buscado ENTONCES
      Escribir("Encontrado en la posición: ", i);
    SI_NO
      Escribir(“No se encontró");
    FIN_SI;
FinAccion.
```

**Casos de uso**

- Arreglos grandes ordenados.
- Combinado con orden: se gana el corte anticipado además del chequeo simplificado.

> [!bug] Errata de la filmina
> En el `SI_NO` el texto abre con comilla tipográfica `“` y cierra con `"`, y le falta el punto final; la versión ampliada (diapositiva 35) dice `Escribir("No se encontró.");`. Además la Acción se llama igual que la de desordenados (`BUSCAR_CENTINELA`); solo cambia `<>` por `<` en el MIENTRAS.

---

## 35 · *(código ampliado)* Centinela en ordenado

```
Accion BUSCAR_CENTINELA (v: arreglo [1..n] de entero) ES;
Ambiente
    buscado, i: entero;
Proceso
    LEER(buscado);
    i := 1;
    MIENTRAS (i<n) y (v[i]<buscado) HACER
        i := i+1;
    FIN_MIENTRAS;
    SI v[i]=buscado ENTONCES
      Escribir("Encontrado en la posición: ", i);
    SI_NO
      Escribir("No se encontró.");
    FIN_SI;
FinAccion.
```

---

## 36 · Secuencial vs. Centinela

*COMPARACIÓN*

| Aspecto | Secuencial | Centinela |
|---|---|---|
| Condición por vuelta | Una sola: valor | Dos: límite Y valor |
| Comparaciones | n | n-1 (peor caso) |
| Cuándo conviene | Muchas búsquedas sobre el mismo arreglo | Búsquedas ocasionales |

> [!bug] Errata de la filmina
> - **Condición por vuelta**: contradice la diapositiva 25 ("[Centinela] evita chequear el límite del arreglo en cada vuelta") y la 31 ("Centinela: evitar el chequeo de límite"). En la idea clásica es al revés: la Secuencial con MIENTRAS chequea límite y valor, y la Centinela solo el valor. Los pseudocódigos de esta clase tampoco ayudan: la Secuencial usa `PARA` (el límite lo controla el PARA) y la Centinela tiene `(i<n) y (...)`.
> - **Cuándo conviene**: "Muchas búsquedas sobre el mismo arreglo" para la Secuencial contradice la diapositiva 27 ("Uso: ... que se buscan pocas veces") y la 40 (si se va a buscar muchas veces, conviene ordenar y usar Binaria).

---

## 37 · Binaria: dividir el rango a la mitad

*BÚSQUEDA BINARIA*

Solo funciona en arreglos ordenados. Compara el valor buscado contra el elemento del medio del rango: si es igual, lo encontró; si es menor, descarta la mitad derecha; si es mayor, descarta la mitad izquierda. Repite sobre la mitad restante.

En **negrita**, el elemento del medio (naranja); ~~tachado~~, las posiciones descartadas (gris).

*Buscando x = 23 — inicio=1, fin=9, medio=5 (17<23 → descarta la izquierda)*

| ~~2~~ | ~~5~~ | ~~9~~ | ~~12~~ | **17** | 23 | 38 | 45 | 60 |
|---|---|---|---|---|---|---|---|---|

*inicio=6, fin=9, medio=7 (38>23 → descarta la derecha)*

| ~~2~~ | ~~5~~ | ~~9~~ | ~~12~~ | ~~17~~ | 23 | **38** | ~~45~~ | ~~60~~ |
|---|---|---|---|---|---|---|---|---|

*inicio=6, fin=6, medio=6 (23=23 → ¡encontrado!)*

| ~~2~~ | ~~5~~ | ~~9~~ | ~~12~~ | ~~17~~ | **23** | ~~38~~ | ~~45~~ | ~~60~~ |
|---|---|---|---|---|---|---|---|---|

***Encontrado en solo 3 pasos, sobre 9 elementos.***

> [!note] Verificación de la traza
> Los valores de inicio, fin y medio son correctos: (1+9) DIV 2 = 5, (6+9) DIV 2 = 7, (6+6) DIV 2 = 6. Con el pseudocódigo literal de la diapositiva 38 el ciclo hace una vuelta más de las que muestra (la primera recalcula medio = 5) y al encontrar el 23 ejecuta `fin := medio-1` (queda fin = 5) antes de salir, pero `medio` termina en 6, que es la posición correcta.

---

## 38 · Pseudocódigo de la Búsqueda Binaria

*BINARIA*

```
Accion BUSCAR_BINARIA (v: arreglo [1..n] de entero, x: entero) ES;
Ambiente
    inicio, fin, medio: entero;
Proceso
    inicio := 1;  fin := n; medio := (inicio + fin) DIV 2;
    MIENTRAS (inicio<=fin) Y v[medio]<>x HACER
        medio := (inicio + fin) DIV 2;
        SI v[medio] < x ENTONCES
            inicio := medio+1;
        SI_NO
            fin := medio-1;
        FIN_SI;
    FIN_MIENTRAS;
    SI encontrado ENTONCES
        Escribir("Encontrado en la posición: ", medio);
    SI_NO
        Escribir("No se encontró.");
    FIN_SI;
FinAccion.
```

**Lectura del algoritmo**

- `inicio` y `fin` delimitan el rango donde puede estar x.
- `medio` parte el rango al medio con `DIV` (división entera).
- Cada paso descarta la mitad donde x no puede estar.
- **Complejidad:** O(log₂ n): con 1000 elementos, ~10 comparaciones como máximo.

> [!bug] Errata de la filmina
> `SI encontrado ENTONCES` usa una variable **`encontrado` que no está declarada en el Ambiente ni se asigna** en ningún lado. Por cómo sale el ciclo, la condición que corresponde es `SI v[medio]=x ENTONCES` (es la que usaba la versión anterior: `SI dato = A[medio]`).
> Otros detalles: el `medio` se calcula dos veces seguidas (antes del ciclo y al principio de cada vuelta), y la condición del MIENTRAS evalúa `v[medio]` con el medio de la vuelta anterior; cuando `v[medio]=x` dentro de la vuelta, igual se ejecuta `fin := medio-1`. No cambia el resultado, pero no sigue exactamente los pasos de la diapositiva 37.

---

## 39 · *(código ampliado)* Binaria

```
Accion BUSCAR_BINARIA (v: arreglo [1..n] de entero, x: entero) ES;
Ambiente
    inicio, fin, medio: entero;
Proceso
    inicio := 1;  fin := n; medio := (inicio+fin) DIV 2;
    MIENTRAS (inicio<=fin) Y v[medio]<>x HACER
        medio := (inicio + fin) DIV 2;
        SI v[medio] < x ENTONCES
            inicio := medio+1;
        SI_NO
            fin := medio-1;
        FIN_SI;
    FIN_MIENTRAS;
    SI encontrado ENTONCES
        Escribir("Encontrado en la posición: ", medio);
    SI_NO
        Escribir("No se encontró.");
    FIN_SI;
FinAccion.
```

> [!bug] Errata de la filmina
> Mismo error que la diapositiva 38: `encontrado` no existe; debería ser `v[medio]=x`.

---

## 40 · Casos de uso y su requisito clave

*BINARIA*

**Casos de uso**

- Arreglos **grandes** y ya ordenados, con muchas consultas: índices, diccionarios, tablas de precios.
- Cuando la velocidad de búsqueda importa más que el costo de mantener el orden.
- Base de otras técnicas: por ejemplo, la inserción binaria que vimos antes.

> [!warning] Requisito clave: orden
> Si el arreglo no está ordenado, descartar una mitad puede descartar el valor buscado: el algoritmo da resultados incorrectos.
>
> *Por eso: si se va a buscar muchas veces en un arreglo desordenado, primero puede convenir ordenarlo (Burbuja/Selección/Inserción) y después usar Binaria.*

---

## 41 · Secuencial, Centinela y Binaria

*COMPARACIÓN FINAL*

| Aspecto | Secuencial | Centinela | Binaria |
|---|---|---|---|
| Requiere orden | No | No | Sí, obligatorio |
| Comparaciones (peor caso) | n | 1 a n-1 | log₂ n |
| Idea clave | Recorrer y comparar | Chequeo de límite | Dividir el rango a la mitad |
| Uso típico | Muchas búsquedas | Arreglos chicos / Corte en primer caso encontrado | Arreglos grandes y ordenados |

> [!bug] Errata de la filmina
> Arrastra las contradicciones de la diapositiva 36: "Uso típico: Muchas búsquedas" para la Secuencial choca con la diapositiva 27 ("que se buscan pocas veces") y la 40. Y la "Idea clave" de la Centinela según la diapositiva 25 es justamente **evitar** el chequeo de límite. En la diapositiva 34 la Centinela ordenada se recomendaba para "Arreglos grandes ordenados", y acá para "Arreglos chicos".

---

## 42 · Lo esencial de hoy

*SÍNTESIS*

1. Ordenar y buscar están relacionados: ordenar tiene un costo que se amortiza con búsquedas más rápidas (Binaria).
2. Burbuja, Selección e Inserción son O(n²); cada una tiene su ventaja: simplicidad, pocos intercambios, o casi-ordenado.
3. Secuencial funciona en cualquier arreglo; Centinela realiza el chequeo de límite; ambas mejoran si el arreglo está ordenado.
4. Binaria requiere orden pero es mucho más rápida: O(log n) contra O(n) de las anteriores.

---

## 43 · ¡Eso es Arreglos!

*FIN DE LA UNIDAD DE ARREGLOS*

Entre las dos clases vimos definición, vectores y matrices, sus operaciones de carga y recorrido, y los algoritmos clásicos de ordenamiento y búsqueda sobre ellos.

> *¿Preguntas sobre algún algoritmo, su pseudocódigo o cuándo usar cada uno?*

---

## 🔗 Notas relacionadas

- [[5 — Búsqueda y Ordenamiento (versión anterior)]] — la presentación vieja, para comparar
- [[4 — Arreglos]] — la Clase 1 de Arreglos
- [[6 — Procesos Estadísticos]] — la siguiente
