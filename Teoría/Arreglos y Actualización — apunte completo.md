# Cómo usar este apunte

Este apunte cubre dos temas que en los parciales aparecen solos y también mezclados: **arreglos**
(vectores y matrices, con búsqueda y ordenamiento) y **actualización de archivos** (unitaria, por
lotes e indexada). La parte IV es la combinación de los dos, que es la forma en que más suele
venir en los parciales.

Todo el pseudocódigo de este apunte **está probado ejecutándolo**. Los ejemplos largos existen
como archivos `.frre` en la carpeta `Práctica/`, con sus datos de prueba, así que podés abrirlos
y darles ▶ mientras leés.

## Las tres cosas que hay que tener claras antes de empezar

> **1. `FDA` no significa "el cursor llegó al final".** Significa **"el último LEER no trajo
> nada"**. De ahí sale toda la estructura de lectura anticipada: hay que leer *antes* de
> preguntar, y volver a leer *al final* del ciclo.

> **2. Los registros se comparan campo por campo, en el orden en que están declarados.** Por eso
> una fecha se declara `anio, mes, dia` y no al revés, y por eso el registro clave se declara en
> el mismo orden que dice el "ordenado por" del enunciado.

> **3. Los arreglos de la cátedra arrancan en 1**, no en 0. El tamaño es `ls - li + 1`.

## Notación

La cátedra acepta dos formas y las dos valen: la moderna (`FIN_SI`, `Proceso`, `SINO`) y la vieja
(`FinSi`, `Algoritmo`, `Contrario`). Este apunte usa la moderna en mayúsculas. Mezclarlas no es
error — los propios materiales de la cátedra las mezclan.

---

# Parte I · Arreglos

## Qué es un arreglo

> **Definición de la cátedra.** El arreglo es una estructura de datos **estática** que almacena,
> en memoria interna, una **colección de datos del mismo tipo**. Es un conjunto **homogéneo,
> finito y ordenado** de elementos.

Las tres palabras importan:

- **homogéneo** — todos los elementos son del mismo tipo
- **finito** — el tamaño se fija al declararlo y **no cambia en ejecución**
- **ordenado** — cada elemento tiene una posición, y se llega a él por su índice

| Concepto | Definición |
|---|---|
| **Tamaño** | El número de elementos que lo conforman: `ls - li + 1` |
| **Dimensión** | Cuántos índices necesito para llegar a un elemento |
| **Índice** | El número de orden de cada elemento dentro del arreglo |

Por dimensión se clasifican en **unidimensional** (vector), **bidimensional** (matriz) y
multidimensional.

## Para qué sirven

Un arreglo resuelve un problema puntual: **necesito tener varios datos disponibles a la vez, en
memoria, para poder volver sobre ellos**. Con variables sueltas no podés, y recorriendo un archivo
tampoco, porque cuando leés el registro 50 ya perdiste el 1.

Eso aparece en tres situaciones típicas:

1. **Totalizar por una categoría que no está en el orden del archivo.** No podés cortar, así que
   acumulás en memoria. (Parte II.)
2. **Necesitar dos pasadas sobre los mismos datos.** Por ejemplo calcular un promedio y después
   comparar cada elemento contra el promedio.
3. **Tener una tabla de referencia.** Nombres de meses, descripciones de códigos de error, costo
   por hora de cada circuito. El índice es el código.

## Vectores

### Declaración

```
V : ARREGLO[1..10] de entero
nombres : ARREGLO[1..5] de AN(30)
costo_hora : ARREGLO[1..6] de real
```

El `1..10` son el límite inferior y el superior. Tiene que ser **constante**: no podés declarar
`ARREGLO[1..n]` con `n` leído por teclado, porque el tamaño se reserva al declarar.

### Acceso y recorrido

El acceso es `V[i]`. El recorrido es siempre con `PARA`, porque la cantidad de vueltas se sabe:

```
PARA i := 1 HASTA 10 HACER
    LEER(V[i])
FIN_PARA
```

### Ejemplo completo: cargar un vector y sumarlo

Este es el ejemplo de la filmina 19 de la cátedra, escrito para que corra:

```
ACCION suma_vector ES
    Ambiente
        V : ARREGLO[1..10] de entero
        i, suma : entero
    Proceso
        suma := 0
        PARA i := 1 HASTA 10 HACER
            ESCRIBIR("Ingrese el elemento ", i, ": ")
            LEER(V[i])
            suma := suma + V[i]
        FIN_PARA
        ESCRIBIR("La suma total es: ", suma)
FIN_ACCION
```

> Fijate que la suma se acumula **dentro del mismo ciclo** de la carga. No hace falta un segundo
> recorrido. Si el ejercicio pidiera además comparar cada elemento contra el promedio, ahí sí
> necesitarías dos ciclos: uno para cargar y sumar, y otro para comparar. Ese es el caso donde el
> arreglo se vuelve imprescindible.

### Vectores paralelos

Dos o más vectores del mismo tamaño donde **la posición `i` de todos se refiere a la misma cosa**.
Es la forma de la cátedra de tener "varios campos" sin usar un arreglo de registros.

```
nombres : ARREGLO[1..5] de AN(30)
sexos   : ARREGLO[1..5] de caracter
```

`nombres[3]` y `sexos[3]` son el nombre y el sexo de la **misma** persona. Se recorren con un solo
índice:

```
PARA i := 1 HASTA 5 HACER
    SI (sexos[i] = 'm') ENTONCES
        ESCRIBIR(nombres[i], " es varon")
    FIN_SI
FIN_PARA
```

La trampa de los vectores paralelos es que **si ordenás uno tenés que ordenar el otro igual**, o
la correspondencia se rompe.

## Matrices

### Declaración y acceso

> Una matriz es un arreglo **bidimensional**: sus componentes se definen con **dos subíndices**,
> el primero referido a la **fila** y el segundo a la **columna**.

```
M : ARREGLO[1..3, 1..4] de entero
```

Tres filas, cuatro columnas, doce elementos. El acceso es `M[i,j]` = `M[fila, columna]`. El orden
no es negociable: **primero fila, después columna**.

### Recorrido: dos PARA anidados

```
PARA i := 1 HASTA 3 HACER
    PARA j := 1 HASTA 4 HACER
        LEER(M[i,j])
    FIN_PARA
FIN_PARA
```

El de afuera maneja las filas, el de adentro las columnas. Si los das vuelta, recorrés la matriz
por columnas en lugar de por filas — a veces es lo que querés, pero tiene que ser a propósito.

### Los tres errores clásicos con matrices

La cátedra los lista explícitamente en la filmina 30:

1. **Acceder a un índice fuera de rango.** `M[3,4]` en una matriz de 3×4 está bien;
   `M[4,4]` no existe. Acordate de que arrancan en 1.
2. **Confundir filas con columnas.** Siempre `[fila, columna]`.
3. **No inicializar la matriz.** Un acumulador que no arranca en 0 acumula basura. Esto es el
   paso 1 de todo proceso estadístico.

```
PARA i := 1 HASTA 7 HACER
    PARA j := 1 HASTA 5 HACER
        T[i,j] := 0
    FIN_PARA
FIN_PARA
```

---

# Parte I (cont.) · Búsqueda en arreglos

Hay tres métodos y la pregunta que los separa es siempre la misma: **¿el arreglo está ordenado?**

| Método | Requiere orden | Encuentra repetidos | Cuándo usarlo |
|---|---|---|---|
| Lineal | no | **sí** | hay que ver todos los elementos (máximo, mínimo, contar) |
| Lineal con centinela | no (mejor si sí) | no | buscar **un** elemento |
| Binaria | **sí, obligatorio** | no | buscar en arreglos grandes y ordenados |

## Búsqueda lineal

Recorre todo el arreglo de punta a punta, sin cortar. Por eso es el único que sirve para encontrar
elementos repetidos, y el único que sirve para máximos y mínimos, porque para saber cuál es el
mayor tenés que haber visto todos.

```
// El menor elemento de un vector de 10 posiciones
menor := A[1]
PARA i := 2 HASTA 10 HACER
    SI (A[i] < menor) ENTONCES
        menor := A[i]
    FIN_SI
FIN_PARA
ESCRIBIR("El menor elemento es: ", menor)
```

> Dos cosas de este código que valen para cualquier máximo o mínimo:
>
> **`menor` arranca en `A[1]`, no en 0 ni en un número inventado.** Si inicializás en 0 buscando
> un mínimo, nunca vas a encontrar nada mayor que 0. Inicializar con el primer elemento real es
> siempre seguro.
>
> **El `PARA` arranca en 2**, porque el 1 ya lo usaste como valor inicial.

Si hay varios elementos iguales al mínimo, este código se queda con el primero. Si el enunciado
pide *cuáles* son, hay que guardar la posición y volver a recorrer, o acumular las posiciones.

## Búsqueda lineal con centinela

> El método recorre el arreglo y **en el momento de hallar lo buscado, termina el recorrido**. Usa
> un **ciclo indefinido** controlado por una variable centinela.

Ciclo indefinido significa `MIENTRAS`, no `PARA`: no sabés cuántas vueltas va a dar.

```
ACCION busqueda_centinela ES
    Ambiente
        A : ARREGLO[1..5] de entero
        i, buscado : entero
        encontrado : logico
    Proceso
        // ... A ya está cargado ...
        ESCRIBIR("Que numero busco? ")
        LEER(buscado)

        i := 1
        encontrado := falso
        MIENTRAS (i <= 5) Y (NO encontrado) HACER
            SI (A[i] = buscado) ENTONCES
                encontrado := verdadero
            SINO
                i := i + 1
            FIN_SI
        FIN_MIENTRAS

        SI encontrado ENTONCES
            ESCRIBIR("Esta en la posicion ", i)
        SINO
            ESCRIBIR("No esta en el arreglo")
        FIN_SI
FIN_ACCION
```

> Los dos ejemplos de búsqueda de esta sección son **extractos**: dan por cargado el arreglo `A`.
> Si los pegás tal cual, la extensión te va a avisar que `A` nunca recibe valor — tiene razón,
> agregale un `PARA` de carga antes.

> **El orden de la condición no es decorativo.** `(i <= 5) Y (NO encontrado)`: primero se controla
> el rango. Si lo pusieras al revés y el elemento no estuviera, `i` llegaría a 6 y `A[6]`
> reventaría antes de que el ciclo corte.
>
> Y fijate que el `i := i + 1` va en la rama del `SINO`. Si lo pusieras afuera del `SI`, al
> encontrarlo incrementarías `i` una vez más y la posición que informás quedaría corrida en uno.

### Sobre arreglos ordenados: la variante que corta antes

Si el arreglo está ordenado, se puede cortar también cuando pasaste de largo:

> El método termina al hallar lo buscado **o, en su defecto, el inmediato mayor** (orden
> creciente). Si buscás 17 en `12 · 13 · 18 · 39 · 45`, el algoritmo termina en la posición 3,
> porque 18 ya es mayor que 17: si estuviera, habría aparecido antes.

Solo cambia la condición: se agrega `Y (A[i] <= buscado)`. Sigue sin encontrar repetidos.

## Búsqueda binaria (dicotómica)

> Se aplica **únicamente sobre arreglos ordenados**. Compara si el valor buscado está en la mitad
> superior o inferior; en la que esté, subdivide de nuevo, y así hasta encontrarlo.

Los tres pasos según la cátedra: definir los límites como variables independientes, calcular el
medio como promedio de los límites, y verificar si está en el medio o sobre qué subvector seguir.

```
ACCION busqueda_binaria ES
    Ambiente
        A : ARREGLO[1..100] de entero
        izq, der, medio, buscado : entero
        encontrado : logico
    Proceso
        // ... A ya está cargado Y ORDENADO ...
        ESCRIBIR("Que numero busco? ")
        LEER(buscado)

        izq := 1
        der := 100
        encontrado := falso

        MIENTRAS (izq <= der) Y (NO encontrado) HACER
            medio := (izq + der) DIV 2
            SI (A[medio] = buscado) ENTONCES
                encontrado := verdadero
            SINO
                SI (buscado < A[medio]) ENTONCES
                    der := medio - 1        // sigo por la mitad izquierda
                SINO
                    izq := medio + 1        // sigo por la mitad derecha
                FIN_SI
            FIN_SI
        FIN_MIENTRAS

        SI encontrado ENTONCES
            ESCRIBIR("Esta en la posicion ", medio)
        SINO
            ESCRIBIR("No esta en el arreglo")
        FIN_SI
FIN_ACCION
```

> **`DIV`, no `/`.** La división real te daría 50.5 y un índice no puede ser real. `DIV` es
> división entera.
>
> **Los `± 1` son obligatorios.** Si escribís `der := medio` en lugar de `medio - 1`, cuando la
> búsqueda se reduzca a un solo elemento el ciclo no avanza más y se cuelga.

El rendimiento es la razón de ser del método: en 100 elementos, la lineal puede necesitar 100
comparaciones y la binaria 7. Pero **pierde todo su sentido si el arreglo no está ordenado**, y
ordenar cuesta más que una búsqueda lineal. La binaria se justifica cuando el arreglo ya viene
ordenado, o cuando vas a buscar muchas veces sobre el mismo arreglo.

---

# Parte I (cont.) · Ordenamiento

Tres métodos. En un parcial lo que se pide es escribir uno y saber qué lo diferencia de los otros.

## Selección

> Selecciona el elemento menor del arreglo no ordenado y lo ubica en el arreglo ordenado.

```
PARA i := 1 HASTA (N-1) HACER
    x := A[i]
    MIN := i
    PARA j := (i+1) HASTA N HACER
        SI (A[j] < x) ENTONCES
            MIN := j
            x := A[j]
        FIN_SI
    FIN_PARA
    A[MIN] := A[i]
    A[i] := x
FIN_PARA
```

La idea: para cada posición `i`, buscar el menor de lo que queda y traerlo. El ciclo interno es una
búsqueda lineal de mínimo, igual a la que vimos.

> **Nota de la cátedra:** si los elementos ya quedan ordenados, el método **igualmente sigue
> procesando** hasta el último elemento. No se da cuenta de que terminó.

Traza sobre `44 · 55 · 12 · 94 · 42`:

| Paso | Arreglo | Qué se intercambia |
|---|---|---|
| inicial | 44 · 55 · 12 · 94 · 42 | |
| 1 | **12** · 55 · 44 · 94 · 42 | 44 ↔ 12 |
| 2 | 12 · **42** · 44 · 94 · 55 | 55 ↔ 42 |
| 3 | 12 · 42 · **44** · 94 · 55 | 44 ya está en su lugar |
| 4 | 12 · 42 · 44 · **55** · 94 | 94 ↔ 55 |

## Inserción

> Toma uno por uno los elementos y lo recorre hacia su posición respecto de los anteriormente
> ordenados. Empieza con el **segundo** y lo ordena respecto del primero, después el tercero
> respecto de los dos anteriores, y así.

Es el método de ordenar cartas en la mano.

```
PARA i := 2 HASTA N HACER
    x := A[i]
    j := i - 1
    MIENTRAS (x < A[j]) Y (j > 0) HACER
        A[j+1] := A[j]
        j := j - 1
    FIN_MIENTRAS
    A[j+1] := x
FIN_PARA
```

> **Arranca en 2**, porque un solo elemento ya está ordenado por definición.
>
> El `MIENTRAS` va corriendo elementos hacia la derecha para hacerle lugar a `x`. Ojo con el orden
> de la condición: tal como está en la filmina, `(x < A[j])` se evalúa antes de `(j > 0)`, lo que
> en la vuelta final accede a `A[0]`. En papel se entiende; si lo vas a ejecutar, poné
> `(j > 0) Y (x < A[j])`.

Traza con la mano `5 · 3 · 4 · 2`: `3·5·4·2` → `3·4·5·2` → `2·3·4·5`.

## Intercambio (burbujeo)

> La característica es el **intercambio entre pares de ítems adyacentes** hasta que todos estén
> ordenados.

```
Bandera := falso
MIENTRAS (NO Bandera) HACER
    Bandera := verdadero
    PARA j := 1 HASTA (N-1) HACER
        SI (A[j] > A[j+1]) ENTONCES
            X := A[j]
            A[j] := A[j+1]
            A[j+1] := X
            Bandera := falso
        FIN_SI
    FIN_PARA
FIN_MIENTRAS
```

> **Esto es lo que lo diferencia de los otros dos, y es lo que suelen preguntar.** La `Bandera`
> hace que el método haga **solo la cantidad de pasadas necesarias más una** para verificar que
> quedó ordenado. Si una pasada completa no intercambia nada, `Bandera` queda en verdadero y el
> ciclo corta. Selección e inserción no tienen esta salida temprana.
>
> El intercambio de dos elementos **necesita una variable auxiliar**. `A[j] := A[j+1]` seguido de
> `A[j+1] := A[j]` no intercambia nada: deja los dos con el mismo valor.

## Resumen comparativo

| Método | Ciclo externo | Corta si ya está ordenado | Idea |
|---|---|---|---|
| Selección | `PARA i := 1 HASTA N-1` | no | buscar el mínimo y traerlo |
| Inserción | `PARA i := 2 HASTA N` | no (pero el interno sí) | insertar en la parte ya ordenada |
| Intercambio | `MIENTRAS NO Bandera` | **sí** | intercambiar adyacentes |

---

# Parte II · Procesos estadísticos (arreglos + archivos)

Acá se juntan los dos temas por primera vez: un **archivo** que se recorre y una **matriz** en
memoria donde se acumula.

## Cuándo aplicarlo

La cátedra da cuatro señales:

1. Necesito organizar información de **manera tabular**
2. Los **datos vienen desordenados** desde un archivo u otra fuente
3. Necesito **información cuantitativa clasificando por categorías**
4. Necesito **totales generales**

La señal decisiva es la 2. **Si el archivo no está ordenado por lo que hay que totalizar, no hay
corte de control posible**, y entonces no queda otra que acumular en memoria.

> **Corte de control vs. proceso estadístico — el criterio.**
>
> **Corte de control:** el archivo está ordenado por los mismos criterios que hay que totalizar, y
> se totaliza en ese orden jerárquico. Alcanzan acumuladores sueltos, se informa a medida que se
> avanza, y no importa cuántos grupos hay.
>
> **Proceso estadístico:** hay que totalizar por criterios que **no están en el orden**, o cruzar
> **dos criterios a la vez**. No se puede informar nada hasta terminar de recorrer, así que se
> acumula en una estructura. Exige que los grupos sean **conocidos y finitos**.

## La metodología: los 7 pasos

Esta es la receta textual de la cátedra, y conviene aprenderla en este orden:

1. **Poner a 0** la matriz estadística
2. Iniciar **procesamiento** del archivo
3. **Recuperar datos** desde el registro
4. De acuerdo al valor, **actualizar la matriz** → `A[Reg.Fila, Reg.Col] := A[Reg.Fila, Reg.Col] + 1`
5. **Verificar** si se requiere actualizar filas/columnas totalizadoras
6. Continuar procesando el archivo **hasta el final**
7. **Mostrar la matriz** e informar los datos específicos que se pidan

## La matriz con márgenes

Este es el corazón del tema, y es textual de la cátedra:

> La matriz es de **51 × 31**: 50 filas de bases de datos **+ una fila más** de totales, y 30
> columnas de problemas **+ una columna más** de totales. La intersección final es el **total
> general**.
>
> **Una fila más** acumula el total por columna. **Una columna más** acumula el total por fila. La
> celda `M[51,31]` es el total general.

O sea que si el enunciado te dice "6 circuitos y 4 lugares de origen", la matriz **no** es de 6×4:

```
T : ARREGLO[1..7, 1..5] de real

        columnas 1..4 = lugares      columna 5 = total de la fila
      +----+----+----+----+-------+
  f 1 |    |    |    |    | tot 1 |   filas 1..6 = circuitos
  i 2 |    |    |    |    | tot 2 |
  l 3 |    |    |    |    | tot 3 |
  a 4 |    |    |    |    | tot 4 |
  s 5 |    |    |    |    | tot 5 |
    6 |    |    |    |    | tot 6 |
      +----+----+----+----+-------+
    7 | t1 | t2 | t3 | t4 | TOTAL |   fila 7 = total de la columna
      +----+----+----+----+-------+
```

## Los cuatro incrementos

Del paso 4 y 5 juntos sale la parte que hay que escribir sin pensar. **Por cada registro que
cuenta, cuatro acumulaciones:**

```
T[fila, col] := T[fila, col] + valor        // la celda
T[fila, 5]   := T[fila, 5]   + valor        // total de esa fila
T[7, col]    := T[7, col]    + valor        // total de esa columna
T[7, 5]      := T[7, 5]      + valor        // total general
```

> Es tentador ahorrarse tres de esos incrementos y calcular los márgenes al final con dos ciclos
> anidados. Funciona, pero **la cátedra enseña los cuatro incrementos** (paso 5 de la metodología),
> así que escribir otra cosa es pelearse con el corrector para ahorrar tres líneas.
>
> El error frecuente es **olvidarse uno**. Si la última fila no cierra con la última columna,
> buscá ahí.

## De dónde sale el índice

Esta es la parte que más cuesta. La fila y la columna casi nunca vienen como número en el registro:

| Cómo viene el dato | Cómo se convierte en índice |
|---|---|
| Ya es un número chico (mes 1..12, circuito 1..6) | se usa directo |
| Es un **código** y hay un vector con los códigos | hay que **buscarlo** en el vector: la posición es el índice |
| Está en **otro archivo**, indexado | hay que **consultarlo** por clave (ver Parte IV) |

El caso del medio es el del ejercicio de los errores: *"el código del problema se corresponde a la
posición del mismo en el arreglo"*. Ahí la búsqueda es parte del algoritmo.

## Ejemplo completo y ejecutable

Archivo de ventas con `mes` (1..12) y `rubro` (1..4), desordenado. Se quiere la recaudación
cruzada, los totales por mes, por rubro, el general, y el mes que más recaudó.

```
ACCION estadistica_ventas ES
    Ambiente
        venta = REGISTRO
            mes     : 1..12
            rubro   : 1..4
            importe : real
        FIN_REGISTRO

        ventas : ARCHIVO de venta        // sin "ordenado por": viene desordenado
        r : venta

        // 12 meses + fila de totales  x  4 rubros + columna de totales
        T : ARREGLO[1..13, 1..5] de real
        i, j, mes_max : entero
        maximo : real
    Proceso
        // PASO 1: poner a 0
        PARA i := 1 HASTA 13 HACER
            PARA j := 1 HASTA 5 HACER
                T[i,j] := 0
            FIN_PARA
        FIN_PARA

        // PASOS 2, 3, 4, 5 y 6
        ABRIR E/(ventas)
        LEER(ventas, r)
        MIENTRAS NFDA(ventas) HACER
            i := r.mes
            j := r.rubro
            T[i,j]  := T[i,j]  + r.importe
            T[i,5]  := T[i,5]  + r.importe
            T[13,j] := T[13,j] + r.importe
            T[13,5] := T[13,5] + r.importe
            LEER(ventas, r)
        FIN_MIENTRAS
        CERRAR(ventas)

        // PASO 7: mostrar
        ESCRIBIR("mes | rubro1 | rubro2 | rubro3 | rubro4 | TOTAL")
        PARA i := 1 HASTA 12 HACER
            ESCRIBIR(i, " | ", T[i,1], " | ", T[i,2], " | ", T[i,3], " | ",
                     T[i,4], " | ", T[i,5])
        FIN_PARA

        ESCRIBIR("")
        PARA j := 1 HASTA 4 HACER
            ESCRIBIR("Total del rubro ", j, ": ", T[13,j])
        FIN_PARA
        ESCRIBIR("TOTAL GENERAL: ", T[13,5])

        // el mes que más recaudó: búsqueda lineal de máximo sobre la columna 5
        maximo := T[1,5]
        mes_max := 1
        PARA i := 2 HASTA 12 HACER
            SI (T[i,5] > maximo) ENTONCES
                maximo := T[i,5]
                mes_max := i
            FIN_SI
        FIN_PARA
        ESCRIBIR("El mes que mas recaudo fue el ", mes_max, " con ", maximo)
FIN_ACCION
```

> **`maximo` y `mes_max` se inicializan ANTES del ciclo, no adentro.** Es el error más común de
> todo el tema: si los ponés dentro del `PARA`, en cada vuelta se reinicia el máximo y terminás
> informando el último elemento en lugar del mayor.
>
> Y fijate que el máximo se busca **sobre la columna de totales** `T[i,5]`, que ya está calculada.
> No hace falta volver a sumar nada: para eso existen los márgenes.

### Los datos para correrlo

En una carpeta `<nombre>.datos/` al lado del `.frre`, un archivo `ventas.tsv` separado por
tabulaciones, con los nombres de los campos en la primera fila:

```
mes	rubro	importe
3	1	1500
3	2	800
7	1	2200
1	4	450
7	3	1900
12	2	3000
7	1	1100
```

Podés generar la plantilla sola: clic derecho en el editor → **AED: Generar plantilla de datos**.

---

# Parte III · Actualización de archivos

## Los conceptos

Tenés un **maestro**: la información permanente, la fuente de verdad. Y tenés **movimientos**: lo
que pasó en el período. Actualizar es aplicar los movimientos al maestro.

| Concepto | Qué es | Ejemplos |
|---|---|---|
| **Archivo maestro** | información permanente y actualizada | clientes, productos, equipos |
| **Archivo de movimientos** | las novedades del período | altas, bajas, modificaciones |
| **Tipos de movimiento** | Alta, Baja, Modificación | siempre esos tres |

La cátedra además clasifica:

- **Tipos de actualización:** **por lotes** (varios registros de movimiento para un registro
  maestro) y **unitaria** (un movimiento por registro maestro).
- **Ficheros de entrada:** por lo menos dos, maestro y movimientos. **De salida:** como mínimo uno.
- **Tipos de maestro:** histórico y común o normal.

## Mezcla vs. actualización

El código se parece mucho y se confunden. Los dos recorren dos archivos en paralelo comparando
claves. La diferencia está en qué hacés cuando las claves coinciden:

| Situación | Qué se usa |
|---|---|
| Combinar o listar, los dos archivos deben agotarse | Mezcla **inclusiva** con `HV` |
| Combinar o listar, solo mientras haya en ambos | Mezcla **exclusiva** + 2 ciclos de vaciado |
| Maestro + movimientos, **1 movimiento por clave** | Actualización **unitaria** |
| Maestro + movimientos, **varios por clave** | Actualización **por lotes** |

## Secuencial o indexada: por qué importa

Esta es la primera decisión, y cambia todo el algoritmo.

| | Secuencial | Indexada |
|---|---|---|
| Archivos para el maestro | **dos**: uno `E/` y uno `/S` | **uno**: `E/S` |
| Se genera un maestro nuevo | **sí, siempre** | no, se modifica en el lugar |
| El maestro viejo | queda como respaldo | se pisa |
| La baja | **no copiar** al nuevo | marcar `'*'` o `ELIMINAR` |
| Recorrido | en paralelo, comparando claves | no hay: acceso puntual por clave |
| `HV` | sí | no |

En un archivo secuencial **no se puede actualizar en el lugar**. Se abre o para leer o para
escribir, nunca las dos cosas. Y aunque pudieras pisar un registro, un **alta** no tendría dónde
meterse y una **baja** dejaría un agujero. Por eso el maestro nuevo se construye entero, de cero.

> **Regla práctica para contar archivos en el parcial: en secuencial, el maestro cuenta doble.** Si
> el enunciado nombra tres archivos, vas a declarar cuatro variables.

## El esqueleto invariante

De las cinco piezas de una actualización secuencial, **cuatro son genéricas**. Cambian de nombre,
no de contenido:

```
PROCEDIMIENTO leer_mae ES
    Proceso
        LEER(arch_mae, reg_mae)
        SI FDA(arch_mae) ENTONCES
            reg_mae.cla := HV           // un := HV por cada campo de la clave
        FIN_SI
FIN_PROCEDIMIENTO

PROCEDIMIENTO leer_mov ES               // idéntico, sobre el otro archivo
```

Y el `Proceso` entero también:

```
ABRIR E/(arch_mae) ; ABRIR E/(arch_mov)
ABRIR /S(arch_mae_act)

leer_mae                                 // LECTURAS ANTICIPADAS
leer_mov

MIENTRAS (reg_mae.cla.<1er campo> <> HV) O (reg_mov.cla.<1er campo> <> HV) HACER

    SI (reg_mae.cla < reg_mov.cla) ENTONCES
        ESCRIBIR(arch_mae_act, reg_mae)      // paso directo
        leer_mae                             // avanza UNO
    SINO
        SI (reg_mae.cla = reg_mov.cla) ENTONCES
            iguales
            leer_mae                         // avanzan LOS DOS
            leer_mov
        SINO
            distintos
            leer_mov                         // avanza UNO
        FIN_SI
    FIN_SI

FIN_MIENTRAS

CERRAR los archivos
```

**Eso es el 80% del código y es siempre igual.** Lo único que cambia de ejercicio a ejercicio es
qué hay adentro de `iguales` y `distintos`.

> **Qué leer en cada rama es lo que más se equivoca.** La regla: **avanza el que se consumió**. Si
> el maestro pasó directo, se consumió el maestro. Si las claves coincidieron, se consumieron los
> dos. Si el movimiento no tenía maestro, se consumió solo el movimiento.

## HV y el ciclo incluyente

`HV` (High Value) es un valor centinela altísimo, típicamente `99999999`. Cuando un archivo se
termina, se le clava `HV` a su clave. Como ningún dato real llega a ese número, ese archivo pierde
todas las comparaciones y el otro **se sigue vaciando solo**, sin código extra.

Por eso el ciclo va con **`O`, no con `Y`**:

```
MIENTRAS (reg_mae.clave <> HV) O (reg_mov.clave <> HV) HACER
```

La alternativa sin `HV` es `MIENTRAS NFDA(a1) Y NFDA(a2)` **más dos ciclos de vaciado** al final.
Las dos son válidas pero **no se cruzan**: o `O` + HV, o `Y` + vaciados.

> **Si la clave es compuesta, `HV` va en TODOS los campos.** Si la clave tiene tres campos y le
> clavás `HV` a uno solo, la comparación de registros mira los otros dos y hace cualquier cosa.

## La tabla de seis celdas

Todo el ejercicio se reduce a esto: dos preguntas cruzadas, *¿el registro existe en el maestro?* y
*¿qué tipo de movimiento es?*

| | **Alta** | **Baja** | **Modificación** |
|---|---|---|---|
| **Existe** (`mae = mov`) → `iguales` | ERROR: alta de existente | marcar baja o mudar, y grabar | pisar los campos que vengan, y grabar |
| **No existe** (`mae > mov`) → `distintos` | crear el registro y grabar | ERROR: baja de inexistente | ERROR: modificación de inexistente |

**Tres celdas válidas en diagonal, tres errores.** Si tu tabla no tiene tres errores, leíste mal el
enunciado. Cuando la consigna dice *"controlar cualquier tipo de error en los datos o referencias
inexistentes"*, te está pidiendo exactamente esas tres celdas rojas.

Dos detalles que se repiten en casi todos los ejercicios:

- En la **modificación** solo se pisan los campos que vienen con dato: `SI (reg_mov.campo1 <> "")`.
  El registro de movimiento deja en blanco lo que no hay que tocar.
- En el **alta** se copia campo por campo, **no** con `reg_mae := reg_mov`, porque maestro y
  movimientos son tipos distintos. Los nombres de los campos muchas veces ni coinciden.

---

# Parte III (cont.) · Actualización unitaria completa

Este es el ejercicio **2.2.19 de la guía de cátedra**, resuelto y ejecutado. Es unitaria porque el
enunciado dice *"solo existe un registro de movimiento para cada registro del maestro"*.

## El enunciado, resumido

`MAE_REMEDIOS` (ordenado por Farmacia + Medicamento) se actualiza con `MOVIMIENTOS` (ordenado por
Farmacia + Medicamento + Cod_Mov). Si las claves son iguales: `Cod_Mov` 1 es error, 2 manda el
registro al archivo `REM_VENC`, 3 modifica la cantidad. Si la del maestro es mayor: 1 incorpora el
remedio con vencimiento a 30 días, 2 y 3 son error.

| Archivo | Campos |
|---|---|
| MAE_REMEDIOS | Farmacia, Medicamento, Cant_Actual, Fecha_Vencimiento |
| MOVIMIENTOS | Farmacia, Medicamento, Cod_Mov, Cant_Recibida |
| REM_VENC | Medicamento, Cant_Vencida |

## Las dos deducciones que hay que hacer

**Qué es cada `Cod_Mov`.** El enunciado no lo dice. Se deduce: el que da error si ya existe es el
**alta** (1); el que saca el remedio es la **baja** (2); el que cambia la cantidad es la
**modificación** (3).

**Que hay tres diseños de registro y cuatro archivos.** El maestro y los movimientos **no tienen la
misma estructura** — solo comparten la clave. Y `REM_VENC` es un tercer diseño, con un campo que
encima se llama distinto (`Cant_Vencida`, no `Cant_Actual`).

| Tipo | Lo usan |
|---|---|
| `mae` | MAE_REMEDIOS **y** el maestro actualizado |
| `mov` | MOVIMIENTOS |
| `venc` | REM_VENC |

## El algoritmo

```
ACCION act_remedios ES
    Ambiente
        HV = 99999

        fecha = REGISTRO
            anio : 1..9999          // este orden importa: los registros se
            mes  : 1..12            // comparan campo por campo en el orden
            dia  : 1..31            // en que están declarados
        FIN_REGISTRO

        clave = REGISTRO            // clave COMPUESTA en un registro aparte:
            Farmacia    : entero    // así se compara de una sola vez.
            Medicamento : entero    // Farmacia primero, como el "ordenado por".
        FIN_REGISTRO

        mae = REGISTRO
            cla               : clave
            Cant_Actual       : entero
            Fecha_Vencimiento : fecha
        FIN_REGISTRO

        mov = REGISTRO
            cla           : clave
            Cod_Mov       : 1..3
            Cant_Recibida : entero
        FIN_REGISTRO

        venc = REGISTRO
            Medicamento  : entero
            Cant_Vencida : entero
        FIN_REGISTRO

        arch_mae, arch_mae_act : ARCHIVO de mae ordenado por cla
        arch_mov  : ARCHIVO de mov ordenado por cla y Cod_Mov
        arch_venc : ARCHIVO de venc

        reg_mae  : mae
        reg_mov  : mov
        reg_venc : venc
        reg_mae_act : mae          // un registro por archivo

        hoy, venc30 : fecha

        PROCEDIMIENTO leer_mae ES
            Proceso
                LEER(arch_mae, reg_mae)
                SI FDA(arch_mae) ENTONCES
                    reg_mae.cla.Farmacia    := HV
                    reg_mae.cla.Medicamento := HV
                FIN_SI
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO leer_mov ES
            Proceso
                LEER(arch_mov, reg_mov)
                SI FDA(arch_mov) ENTONCES
                    reg_mov.cla.Farmacia    := HV
                    reg_mov.cla.Medicamento := HV
                FIN_SI
        FIN_PROCEDIMIENTO

        // FILA DE ARRIBA DE LA TABLA: el remedio EXISTE
        PROCEDIMIENTO iguales ES
            Proceso
                SEGUN reg_mov.Cod_Mov HACER

                    1 : ESCRIBIR("ERROR - ALTA de un remedio que ya existe: ",
                                 reg_mae.cla.Farmacia, "-", reg_mae.cla.Medicamento)
                        ESCRIBIR(arch_mae_act, reg_mae)

                    2 : reg_venc.Medicamento  := reg_mae.cla.Medicamento
                        reg_venc.Cant_Vencida := reg_mae.Cant_Actual
                        ESCRIBIR(arch_venc, reg_venc)

                    3 : reg_mae.Cant_Actual := reg_mae.Cant_Actual + reg_mov.Cant_Recibida
                        ESCRIBIR(arch_mae_act, reg_mae)

                FIN_SEGUN
        FIN_PROCEDIMIENTO

        // FILA DE ABAJO: el remedio NO existe en el maestro
        PROCEDIMIENTO distintos ES
            Proceso
                SEGUN reg_mov.Cod_Mov HACER

                    1 : reg_mae_act.cla               := reg_mov.cla
                        reg_mae_act.Cant_Actual       := reg_mov.Cant_Recibida
                        reg_mae_act.Fecha_Vencimiento := venc30
                        ESCRIBIR(arch_mae_act, reg_mae_act)

                    2 : ESCRIBIR("ERROR - BAJA de un remedio inexistente: ",
                                 reg_mov.cla.Farmacia, "-", reg_mov.cla.Medicamento)

                    3 : ESCRIBIR("ERROR - MODIFICACION de inexistente: ",
                                 reg_mov.cla.Farmacia, "-", reg_mov.cla.Medicamento)

                FIN_SEGUN
        FIN_PROCEDIMIENTO

    Proceso
        ESCRIBIR("Fecha actual (anio mes dia): ")
        LEER(hoy.anio)
        LEER(hoy.mes)
        LEER(hoy.dia)

        // "30 dias despues". En el parcial esto se asume dado.
        venc30 := hoy                   // copia de registro completo: mismo tipo
        SI (hoy.mes = 12) ENTONCES
            venc30.mes  := 1
            venc30.anio := hoy.anio + 1
        SINO
            venc30.mes := hoy.mes + 1
        FIN_SI

        ABRIR E/(arch_mae)
        ABRIR E/(arch_mov)
        ABRIR /S(arch_mae_act)
        ABRIR /S(arch_venc)

        leer_mae
        leer_mov

        MIENTRAS (reg_mae.cla.Farmacia <> HV) O (reg_mov.cla.Farmacia <> HV) HACER
            SI (reg_mae.cla < reg_mov.cla) ENTONCES
                ESCRIBIR(arch_mae_act, reg_mae)
                leer_mae
            SINO
                SI (reg_mae.cla = reg_mov.cla) ENTONCES
                    iguales
                    leer_mae
                    leer_mov
                SINO
                    distintos
                    leer_mov
                FIN_SI
            FIN_SI
        FIN_MIENTRAS

        CERRAR(arch_mae)
        CERRAR(arch_mov)
        CERRAR(arch_mae_act)
        CERRAR(arch_venc)
FIN_ACCION
```

## Las tres decisiones que el enunciado no aclara

1. **La baja no marca, muda.** Y como `venc` y `mae` son tipos distintos, hay que armar `reg_venc`
   campo por campo. **No se graba en el maestro nuevo**: así se borra un registro en una
   actualización secuencial, no copiándolo.
2. **La modificación suma** al stock en lugar de reemplazar. Es una farmacia recibiendo mercadería.
   Si el profesor dice que reemplaza, se cambia una línea.
3. **El error de alta sobre existente graba el maestro igual.** Si no lo grabaras, perderías un
   remedio que existe solo porque alguien cargó mal un movimiento. El dato malo es el movimiento.

Cuando una decisión es ambigua de verdad, **elegí una y dejá el comentario** diciendo qué asumiste.

## Los datos y la salida verificada

`arch_mae.tsv` (6 registros) y `arch_mov.tsv` (6 movimientos, uno por cada celda de la tabla):

```
cla.Farmacia  cla.Medicamento  Cant_Actual  ...Vencimiento.anio  .mes  .dia
1             100              50           2026                 11    10
1             200              30           2026                 12    1
1             300              15           2027                 1     20
2             100              80           2026                 10    5
2             400              5            2026                 9     30
3             100              60           2027                 3     15

cla.Farmacia  cla.Medicamento  Cod_Mov  Cant_Recibida
1             200              2        0       <- baja de existente    (valida)
1             300              3        25      <- modif de existente   (valida)
1             500              1        120     <- alta de inexistente  (valida)
2             100              1        10      <- alta de existente    ERROR
2             250              2        0       <- baja de inexistente  ERROR
3             700              3        40      <- modif de inexistente ERROR
```

Ejecutado con fecha 2026-09-24, la salida por pantalla son los tres errores, y los archivos quedan:

```
maestro actualizado                      REM_VENC
1  100   50  2026-11-10                  200   30
1  300   40  2027-01-20   <- 15+25
1  500  120  2026-10-24   <- el alta
2  100   80  2026-10-05   <- conservado, pese al error
2  400    5  2026-09-30
3  100   60  2027-03-15
```

Seis registros entran, seis salen: uno se fue a `REM_VENC` y el alta ocupó su lugar.

---

# Parte III (cont.) · Por lotes e indexada

## Actualización por lotes

Cuando **puede haber varios movimientos para la misma clave**. El armazón es idéntico; cambian tres
cosas:

**1. Un registro auxiliar.** Se copia el maestro al auxiliar, se le aplican **todos** los
movimientos de esa clave encima, y se graba **una sola vez** al final.

```
aux_mae : mae
```

**2. Un ciclo interno**, e `iguales` deja de grabar:

```
PROCEDIMIENTO lote ES
    Proceso
        MIENTRAS (aux_mae.cla = reg_mov.cla) HACER
            iguales                          // modifica aux, NO graba
            leer_mov
        FIN_MIENTRAS
        ESCRIBIR(arch_mae_act, aux_mae)      // graba una sola vez
FIN_PROCEDIMIENTO
```

**3. El Proceso llama a `lote`** en lugar de a `iguales`:

```
SI (reg_mae.cla = reg_mov.cla) ENTONCES
    aux_mae := reg_mae                   // copio el maestro al auxiliar
    lote
    leer_mae
SINO
    // ALTA: cargo aux desde el movimiento
    aux_mae.cla         := reg_mov.cla
    aux_mae.Cant_Actual := reg_mov.Cant_Recibida
    leer_mov                             // <-- IMPRESCINDIBLE, ver abajo
    lote
FIN_SI
```

> **La trampa del lote.** En la rama de alta hay que hacer `leer_mov` **antes** de entrar al lote.
> La plantilla oficial de la cátedra lo omite, y como `lote` arranca comparando
> `aux_mae.cla = reg_mov.cla`, la primera vuelta reprocesa **el mismo movimiento de alta** a través
> de `iguales`, que imprime "ERROR - ALTA de registro existente".

## Actualización indexada (ABM)

Desaparece el recorrido, el `HV` y el maestro nuevo. Es acceso puntual, en tiempo real, sobre el
mismo archivo. **Pero la tabla de seis celdas es exactamente la misma**: lo que era `mae = mov`
ahora es `SI EXISTE`, y lo que era `mae > mov` es el `SINO`.

> **La secuencia de toda operación indexada es de cuatro pasos y es obligatoria:**
>
> `asignar la clave` → `LEER` → `SI EXISTE` → `operar`

| Operación | Instrucción | Requiere |
|---|---|---|
| Alta | `ESCRIBIR(arch, reg)` | que **no** exista |
| Modificación | `RE-ESCRIBIR(arch, reg)` | que exista, y haber hecho el `LEER` |
| Baja lógica | marcar un campo + `RE-ESCRIBIR` | que exista |
| Baja física | `ELIMINAR(arch, reg)` | que exista |

La baja lógica marca y el registro sigue ocupando lugar; la física borra de verdad pero deja
"huecos" en el área de datos.

```
ACCION abm_indexado ES
    Ambiente
        mae = REGISTRO
            clave  : entero
            campo1 : AN(50)
            campo4 : real
            Baja   : caracter
        FIN_REGISTRO

        reg_mae : mae
        arch_mae : ARCHIVO de mae INDEXADO por clave
        campo1 : AN(50)
        campo4 : real
        op, acc : caracter

        PROCEDIMIENTO alta ES
            Proceso
                ESCRIBIR("Ingrese clave")
                LEER(reg_mae.clave)
                LEER(arch_mae, reg_mae)
                SI EXISTE ENTONCES
                    ESCRIBIR("ERROR, EL REGISTRO YA EXISTE")
                SINO
                    ESCRIBIR("Ingrese campo1: "); LEER(reg_mae.campo1)
                    ESCRIBIR("Ingrese campo4: "); LEER(reg_mae.campo4)
                    reg_mae.Baja := '-'
                    ESCRIBIR(arch_mae, reg_mae)
                FIN_SI
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO modif_baja(TipoMov : caracter) ES
            Proceso
                ESCRIBIR("Ingrese clave")
                LEER(reg_mae.clave)
                LEER(arch_mae, reg_mae)
                SI EXISTE ENTONCES
                    SI (TipoMov = 'B') ENTONCES
                        reg_mae.Baja := '*'
                    SINO
                        ESCRIBIR("Ingrese campo1: "); LEER(campo1)
                        SI (campo1 <> "") ENTONCES
                            reg_mae.campo1 := campo1
                        FIN_SI
                        ESCRIBIR("Ingrese campo4: "); LEER(campo4)
                        SI (campo4 <> 0) ENTONCES
                            reg_mae.campo4 := campo4
                        FIN_SI
                    FIN_SI
                    RE-ESCRIBIR(arch_mae, reg_mae)
                SINO
                    ESCRIBIR("ERROR, EL REGISTRO NO EXISTE")
                FIN_SI
        FIN_PROCEDIMIENTO

    Proceso
        ABRIR E/S(arch_mae)
        ESCRIBIR("Desea continuar? S/N"); LEER(op)
        MIENTRAS (op = 'S') HACER
            ESCRIBIR("Ingrese accion A/B/M"); LEER(acc)
            SEGUN acc HACER
                'A'      : alta
                'B', 'M' : modif_baja(acc)
                otros    : ESCRIBIR("Accion INCORRECTA")
            FIN_SEGUN
            ESCRIBIR("Desea continuar? S/N"); LEER(op)
        FIN_MIENTRAS
        CERRAR(arch_mae)
FIN_ACCION
```

> **`ABRIR E/S`**, un solo archivo. Y la **modificación solo pisa los campos que vengan con dato**:
> si el usuario aprieta Enter sin escribir nada, ese campo queda como estaba.

---

# Parte III (cont.) · Errores y trampas

Estos dos están **probados ejecutando**, y los dos vienen de plantillas de la cátedra.

## El alta pisa el registro del maestro

La rama de alta de la plantilla de actualización unitaria armaba el registro nuevo **encima de
`reg_mae`**:

```
SINO
    reg_mae.clave  := reg_mov.clave        // ✗ MAL
    reg_mae.campo1 := reg_mov.campo1
    ESCRIBIR(arch_mae_act, reg_mae)
```

A la rama de alta se llega cuando `reg_mae.clave > reg_mov.clave`. O sea: **`reg_mae` tiene un
registro del maestro, válido y sin procesar** — perdió la comparación justamente por eso. Pisarlo lo
destruye. Y como en esa rama solo avanza `leer_mov`, el `reg_mae` corrupto sobrevive a la vuelta
siguiente y se compara como si fuera real.

Ejecutado con 6 registros de maestro y 6 movimientos, el maestro salió así:

```
1  500  120     <- grabado dos veces
1  500  120
2  100   10     <- tenia 80, quedo con la cantidad del movimiento
2  100   10
(2, 400)        <- perdido, nunca se grabo
```

**La solución es un registro por archivo:** `reg_mae_act` para armar las altas, y `reg_mae` que solo
se lee. La plantilla de **lotes no tiene el problema**, porque ya usa `aux_mae` para armar todo.

## El índice equivocado en una matriz

En el ejercicio de la Parte IV, el costo por hora está en un vector indexado **por circuito**.
Escribir `costo[lugar]` en lugar de `costo[circuito]`:

| | Bien | Con el bug |
|---|--:|--:|
| Circuito 1 | 40800 | 43900 |
| Circuito 3 | 19800 | 27900 |
| Circuito 4 | 42000 | 28500 |
| **Total general** | **168100** | **170400** |

**No se cae.** El lugar de origen vale 1..4 y el vector va de 1..6, así que el índice es válido y el
algoritmo termina perfecto con números equivocados. Es el peor tipo de error: silencioso.

## Los cinco que matan en actualización

1. **Qué leer en cada rama.** Avanza el que se consumió; en la rama del medio, los dos.
2. **`O`, no `Y`**, en el ciclo incluyente. Con `Y` quedan registros sin procesar.
3. **`HV` en todos los campos de la clave**, no solo en el primero.
4. **No escribir en `reg_mae`** en la rama de alta. Un registro por archivo.
5. **El orden de los campos del registro clave** tiene que ser el del "ordenado por".

## Los cinco que matan en arreglos

1. **No inicializar la matriz en 0.** Es el paso 1 de la metodología.
2. **Inicializar el máximo adentro del ciclo.** Va antes, y con el primer elemento real.
3. **Olvidarse uno de los cuatro incrementos.** Si los márgenes no cierran, es eso.
4. **Índice fuera de rango.** Arrancan en 1, y `ARREGLO[1..7,1..5]` no tiene `[8,1]`.
5. **Confundir fila con columna.** Siempre `[fila, columna]`.

---

# Parte IV · Los dos temas combinados

Así es como más suele venir en los parciales: **una matriz estadística alimentada recorriendo un
archivo secuencial, donde uno de los índices sale de consultar un archivo indexado**.

## El enunciado

Archivo `NOVEDADES` (ordenado por tipo_equipo, nro_equipo, tipo_novedad, fecha) con
`nro_circuito` e `id_usuario`, entre otros campos. `tipo_novedad` 2 es un préstamo.

Archivo `USUARIOS`, **indexado por id_usuario**, con el `lugar_de_origen` (1..4) de cada usuario.

Hay un **vector de 6 posiciones con el costo por hora de cada circuito**, y una función
`diff(hora_inicio, hora_fin)` que devuelve la diferencia de horas.

Se pide la recaudación por préstamos **discriminada por circuito y por lugar de origen**, los
totales por circuito y por lugar, y los lugares de origen que superan un monto ingresado.

## El razonamiento, en tres pasos

**1. ¿Corte o estadístico?** `NOVEDADES` viene ordenado por `tipo_equipo, nro_equipo`. Hay que
totalizar por **circuito** y por **lugar de origen**. Ninguno está en el orden → **estadístico**.

Y hay un argumento más fuerte: **el lugar de origen no está en `NOVEDADES`**. Se obtiene consultando
el indexado. Un dato que conseguís por búsqueda **jamás puede ser criterio de corte**, porque el
archivo no puede estar ordenado por algo que no contiene.

**2. La matriz.** Seis circuitos y cuatro lugares, los dos con dominio fijo y chico. Con los
márgenes: `ARREGLO[1..7, 1..5]`.

**3. De dónde sale la columna.** Por cada préstamo: sacar el `id_usuario` de la novedad, buscarlo
por clave en `USUARIOS`, y de ahí sale el `lugar_de_origen`. **El indexado no se recorre, se
consulta.**

## El algoritmo

```
ACCION estadistica_circuitos(costo_hora : ARREGLO[1..6] de real) ES
    Ambiente
        fecha = REGISTRO
            anio : 1..9999
            mes  : 1..12
            dia  : 1..31
        FIN_REGISTRO

        novedad = REGISTRO
            tipo_equipo   : entero
            nro_equipo    : entero
            tipo_novedad  : 1..3
            fecha_novedad : fecha
            hora_inicio   : entero
            hora_fin      : entero
            nro_circuito  : 1..6
            id_usuario    : entero
        FIN_REGISTRO

        usuario = REGISTRO
            id_usuario        : entero
            dni               : entero
            sexo              : caracter
            apellido_y_nombre : AN(40)
            lugar_de_origen   : 1..4
            edad              : entero
        FIN_REGISTRO

        novedades : ARCHIVO de novedad ordenado por tipo_equipo, nro_equipo, tipo_novedad y fecha_novedad
        usuarios  : ARCHIVO de usuario INDEXADO por id_usuario

        reg_nov : novedad
        reg_usu : usuario

        // filas 1..6 circuitos, fila 7 totales por lugar
        // columnas 1..4 lugares, columna 5 totales por circuito
        T : ARREGLO[1..7, 1..5] de real

        desc_lugar : ARREGLO[1..4] de AN(30)
        importe, monto : real
        circ, lugar, i, j : entero
        hubo : logico
    Proceso
        // PASO 1: la matriz en 0
        PARA i := 1 HASTA 7 HACER
            PARA j := 1 HASTA 5 HACER
                T[i,j] := 0
            FIN_PARA
        FIN_PARA

        desc_lugar[1] := "Chaco"
        desc_lugar[2] := "Otra provincia argentina"
        desc_lugar[3] := "Pais limitrofe"
        desc_lugar[4] := "Otro pais"

        ABRIR E/(novedades)
        ABRIR E/(usuarios)

        LEER(novedades, reg_nov)
        MIENTRAS NFDA(novedades) HACER

            SI (reg_nov.tipo_novedad = 2) ENTONCES      // solo los prestamos

                // el indexado se CONSULTA: clave -> LEER -> SI EXISTE
                reg_usu.id_usuario := reg_nov.id_usuario
                LEER(usuarios, reg_usu)

                SI EXISTE ENTONCES
                    circ    := reg_nov.nro_circuito
                    lugar   := reg_usu.lugar_de_origen
                    importe := diff(reg_nov.hora_inicio, reg_nov.hora_fin) * costo_hora[circ]

                    T[circ, lugar] := T[circ, lugar] + importe   // la celda
                    T[circ, 5]     := T[circ, 5]     + importe   // total del circuito
                    T[7, lugar]    := T[7, lugar]    + importe   // total del lugar
                    T[7, 5]        := T[7, 5]        + importe   // total general
                SINO
                    ESCRIBIR("ERROR: el usuario ", reg_nov.id_usuario, " no existe")
                FIN_SI

            FIN_SI

            LEER(novedades, reg_nov)
        FIN_MIENTRAS

        CERRAR(novedades)
        CERRAR(usuarios)

        // PASO 7: mostrar la matriz
        ESCRIBIR("Circuito | Chaco | Otra prov. | Limitrofe | Otro pais | TOTAL")
        PARA i := 1 HASTA 6 HACER
            ESCRIBIR("    ", i, "    | ", T[i,1], " | ", T[i,2], " | ", T[i,3],
                     " | ", T[i,4], " | ", T[i,5])
        FIN_PARA

        ESCRIBIR("")
        PARA i := 1 HASTA 6 HACER
            ESCRIBIR("Total del circuito ", i, ": ", T[i,5])
        FIN_PARA
        ESCRIBIR("TOTAL GENERAL: ", T[7,5])

        // los lugares que superan el monto: se recorre la fila de totales
        ESCRIBIR("")
        ESCRIBIR("Ingrese el monto a superar: ")
        LEER(monto)
        hubo := falso
        PARA j := 1 HASTA 4 HACER
            SI (T[7,j] > monto) ENTONCES
                ESCRIBIR(desc_lugar[j], " supero el monto, con ", T[7,j])
                hubo := verdadero
            FIN_SI
        FIN_PARA
        SI (NO hubo) ENTONCES
            ESCRIBIR("Ningun lugar de origen supero ese monto")
        FIN_SI
FIN_ACCION
```

> **El vector de costos va como parámetro de la `ACCION`, y así se ejecuta.** Los enunciados dicen
> "reciba como parámetro" o "se cuenta con un vector de 6 posiciones": son **datos externos**, no
> los produce el algoritmo. La extensión los carga desde la carpeta de datos, igual que los
> archivos — un `costo_hora.txt` con un valor por línea. Escribilo como lo pide la consigna.
>
> Lo único que sí hay que agregar para correrlo es la **función `diff`**, que la consigna da por
> dada: `FUNCION diff(hi : entero, hf : entero) : real ES` con `diff := hf - hi`.

## Las cuatro cosas que este ejercicio enseña

**El vector de costos entra por parámetro.** El enunciado dice "se cuenta con un vector de 6
posiciones": eso significa que viene dado. Declararlo como parámetro de la `ACCION` es la lectura
fiel, y además evita cargarlo a mano.

**`costo_hora[circ]`, no `costo_hora[lugar]`.** El vector tiene el costo **por circuito**. Es el
error silencioso de la Parte III: como el lugar vale 1..4 y el vector va de 1..6, el índice es
válido y no se cae.

**El `SI EXISTE` no es opcional.** Si el `id_usuario` no está en `USUARIOS`, `reg_usu.lugar_de_origen`
queda con el valor del usuario **anterior** y acumulás la plata en la columna equivocada, sin que
nada avise.

**El inciso final sale de los márgenes.** Los lugares que superan el monto se recorren sobre
`T[7, 1..4]`, que ya está calculada. Para eso están las filas y columnas totalizadoras: los incisos
"informar cuál fue el mayor / cuáles superan tal valor" son búsquedas sobre los márgenes, no
recorridos nuevos del archivo.

## Variantes que hay que reconocer

| Si el enunciado dice… | Entonces |
|---|---|
| "el archivo no tiene ningún orden lógico" | estadístico, seguro |
| "el código se corresponde con la posición en el arreglo" | la columna sale de una **búsqueda** en el vector |
| "indexado por X" y el dato que necesitás está ahí | **consulta** por clave, con `SI EXISTE` |
| "pueden existir múltiples novedades para un mismo X" | actualización **por lotes** |
| "informar el mayor / el menor / cuáles superan" | búsqueda lineal sobre los márgenes |

---

# Parte V · Para sentarse a ejecutar

## Cómo correr los ejemplos

Los archivos van con extensión **`.frre`**. Con la extensión de VS Code instalada:

- **F5** o el botón ▶ arriba a la derecha, o el CodeLens "▶ Ejecutar" sobre la línea `ACCION`
- **Cmd+Alt+N** también
- Los errores aparecen subrayados en el editor y en el panel Problems mientras escribís

## Cómo se guardan los datos

Al lado del `.frre`, una carpeta que se llama **igual que el archivo pero con `.datos`**:

```
Actualizacion 2.2.19 — Remedios.frre
Actualizacion 2.2.19 — Remedios.datos/
    arch_mae.tsv
    arch_mov.tsv
```

Cada archivo de datos se llama como la **variable** declarada en el `Ambiente`, no como el tipo.

**Para un `ARCHIVO de registro`**: un `.tsv` separado por **tabulaciones**, con la primera fila de
encabezado. Los campos anidados se escriben con punto:

```
cla.Farmacia	cla.Medicamento	Cant_Actual	Fecha_Vencimiento.anio
1	100	50	2026
```

**Para una `SECUENCIA`**: un `.txt` con el contenido crudo, leído carácter a carácter.

**Para un parámetro de la `ACCION`** (los datos que la consigna te da por recibidos): un arreglo de
registros va en `.tsv` con encabezado, igual que un archivo; un arreglo de escalares o un valor
suelto van en `.txt`, un valor por línea. El archivo se llama como el parámetro.

**Atajo:** clic derecho en el editor → **AED: Generar plantilla de datos**. Inspecciona el
`Ambiente` y crea los archivos con los encabezados correctos.

## Dos cosas que te van a morder al ejecutar

**Si declarás `ordenado por`, la extensión lo verifica.** Si el TSV no está ordenado por esas
claves, te corta con un error explicando qué fila está fuera de lugar. Es a propósito: es la
precondición del algoritmo.

**Un archivo indexado persiste entre corridas.** Lo que das de alta hoy sigue estando mañana, porque
el maestro indexado se modifica en el lugar. Si querés empezar de cero, borrá el `.tsv`.

## Los archivos que ya están resueltos y corriendo

| Archivo en `Práctica/` | Qué tema |
|---|---|
| `Actualizacion 2.2.19 — Remedios.frre` | actualización unitaria, clave compuesta, 3 archivos |
| `Parcial — Circuitos y equipos.frre` | matriz estadística + consulta a indexado |
| `Actualizacion Parcial.frre` | corte de control de dos niveles |
| `Eco-Rutas — revision de mi solucion.frre` | los tres bugs típicos, explicados |

En `aed-vscode/ejemplos/` además están `corte_1000.frre` (corte de tres niveles sobre 1000
registros), `abm_indexado.frre` y `palabras.frre` (secuencias).

## Checklist antes de entregar un parcial

**Del Ambiente:**

- ¿Están declarados **todos** los registros que uso como tipo?
- ¿La clave está declarada **igual** en los dos archivos?
- ¿El orden de los campos del registro clave es el del "ordenado por"?
- ¿Los códigos numéricos están declarados numéricos, y no como `AN`?
- ¿Conté el maestro **dos veces** si es actualización secuencial?
- ¿`HV` está declarado?

**Del Proceso:**

- ¿Hay una lectura anticipada por cada archivo que recorro?
- ¿El `LEER` está **al final** del ciclo?
- ¿El ciclo incluyente va con `O`?
- ¿Avanzo el archivo correcto en cada rama?
- ¿La matriz arranca en 0?
- ¿Los máximos y mínimos se inicializan **antes** del ciclo?
- ¿Cerré todos los archivos?

**De la lógica:**

- ¿La tabla de seis celdas tiene **tres errores**?
- ¿Están los **cuatro incrementos** de la matriz?
- ¿Cada `LEER` sobre un indexado tiene su `SI EXISTE`?
- ¿Emití lo que quedó pendiente después del `FIN_MIENTRAS`?

> **Lo último, y es lo que más puntos recupera:** si una consigna es ambigua de verdad, **elegí una
> interpretación y escribí un comentario diciendo qué asumiste**. Eso no se descuenta. Dejarlo en
> blanco o adivinar en silencio, sí.
