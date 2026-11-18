---
tipo: apuntes
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
clase: 1
origen: Clase_Uno_despues_de_organizacion.txt
tags:
  - AED
  - practica
  - arreglos
  - InProgress
---

# Clase 1 — apuntes de arreglos

> [!abstract] Qué es esta nota
> Tus apuntes propios de la primera clase después de la reorganización, tomados en `Clase_Uno_despues_de_organizacion.txt`. Estaban en un `.txt`, que Obsidian **no indexa** (`showUnsupportedFiles: false`), así que no aparecían en la búsqueda ni en el grafo. Acá está el contenido íntegro, ya contrastado contra las filminas de la cátedra.
>
> El `.txt` original se conserva en la misma carpeta.

[[💻 Algoritmos — Índice|← Materia]] · [[4 — Arreglos|Filminas de la cátedra sobre este tema]]

---

## 🎯 Alcance del segundo parcial

> [!danger] Lo que anotaste en clase
> **Corte de control, actualización y arreglos entran en el segundo parcial.**
> (Tener en cuenta para realizar research y estudio)

Material del vault para cada uno de los tres temas:

| Tema | Teoría de cátedra | Filminas | Plantilla | Ejercicios |
|---|---|---|---|---|
| **Corte de control** | [[Corte de Control]] | — | [[plantillas]] | [[2.2 — Archivos Secuenciales]] |
| **Actualización** | [[Actualización]] | — | [[plantillas]] | [[2.3 — Archivos Indexados]] |
| **Arreglos** | [[Arreglos]] | [[4 — Arreglos]] · [[5 — Búsqueda y Ordenamiento]] · [[6 — Procesos Estadísticos]] | [[sintaxis-completa]] | [[3 — Arreglos]] |

---

## La arquitectura de los Arreglos

> [!bug] Corrección — acá el apunte dice lo contrario de la cátedra
> Tu apunte dice: *"Arreglo es una estructura **dinámica**, vive en la RAM durante la ejecución, homogéneo, finito y ordenado"*.
>
> El arreglo es una estructura **ESTÁTICA**. La filmina 6 de [[4 — Arreglos]] lo define así:
> > *son aquellas en las que el tamaño ocupado en memoria se define **antes** de que cualquier acción se ejecute y **no puede modificarse** dicho tamaño durante la ejecución del proceso.*
>
> Es una pregunta de parcial clásica, y el propio apunte se contradice más abajo: *"El tamaño de un array es fijo, no se puede cambiar durante la ejecución"*. Lo que sí es correcto de tu frase: **vive en memoria interna durante la ejecución**, y es **homogéneo, finito y ordenado**.

**Definición corregida:** el arreglo es una estructura de datos **estática**, capaz de almacenar en **memoria interna** una colección de datos **del mismo tipo**. Es un conjunto **homogéneo, finito y ordenado** de elementos.

### Dimensión

Dependiendo de la dimensión, los arreglos pueden ser:

- **unidimensional** (vector)
- **bidimensional** (matrices)
- **multidimensional**

### Acciones que podemos hacer en un arreglo

1. Lectura y escritura
2. Recorrido
3. Actualización
4. Búsqueda
5. Ordenamiento

> Las dos últimas son el tema completo de [[5 — Búsqueda y Ordenamiento]].

### Definición en el ambiente

```
mi_vector: ARREGLO de [1..7] de ENTEROS
```

---

## Proceso básico de carga para un arreglo

Lo que anotaste:

```
PARA i:= 1 a 30 HACER 
    LEER(notas[1])
FIN_PARA
```

> [!bug] Errata del apunte
> Dice `notas[1]` — con **uno**, no con la variable del ciclo. Así carga 30 veces la **misma** posición. Va con `i`:

```
PARA i := 1 A 30, 1 HACER
    LEER(notas[i])
FIN_PARA
```

## Proceso básico de escritura para un arreglo

Lo que anotaste:

```
PARA i:= 1 a 30 HACER
    ESCRIBIR(notas[1])
FIN_PARA
```

Con la misma corrección:

```
PARA i := 1 A 30, 1 HACER
    ESCRIBIR(notas[i])
FIN_PARA
```

> [!tip] Notación del parcial
> Las plantillas oficiales escriben el `PARA` con **coma y paso**: `PARA i := 1 HASTA 10, 1 HACER`. Ver [[sintaxis-completa]] y [[plantillas]] — es uno de los seis puntos donde el libro y las plantillas no coinciden, y en el parcial se corrige con las plantillas.

---

## Otras notas de la clase

- **El primer índice siempre es la fila y el segundo la columna.** ✅ Coincide con la filmina 28 de [[4 — Arreglos]].
- **El tamaño de un array es fijo**, no se puede cambiar durante la ejecución. ✅
- Se puede **acceder a cada elemento directamente** sabiendo los índices del mismo. ✅

---

## Ejercicio de ejemplo — `ej_3.2`

**Consigna** ([[3 — Arreglos|Guía de Cátedra, Ejercicio 3.2]]):

> Genere un **único algoritmo** que resuelva las 3 consignas del ejercicio anterior.

Y las tres consignas del **Ejercicio 3.1**, usando un arreglo de 100 números enteros:

> 1. Almacenar 100 números.
> 2. Localizar el número de mayor valor y el de menor valor, informar sus valores y sus posiciones.
> 3. Contar y sumar todos los números pares.

Por eso el algoritmo hace todo **en un solo recorrido**: esa es justamente la gracia del 3.2.

**Lo que escribiste en clase:**

```
ACCION ej_3.2 ES
    AMBIENTE
        num: ARREGLO de [1..100] de ENTERO
        i, posicion_min, posicion_max, contpar, acumpar: ENTERO

    PROCESO
        contpar:= 0; acumpar:= 0
        posicion_min := 1; posicion_max := 1

        PARA i := 1 a 100 HACAER
            ESCRIBIR('Ingrese la piscion ', i, 'del arreglo')
            LEER(num[i])
            SI num[1] > num[posicion_max] ENTONCES
                posicion_max := i 
            SINO
                SI num[i] < num[posicion_min] ENTONCES
                    posicion_min := i
                FIN_SI
            FIN_SI

            SI num[i] MOD 2 = 0
                contpar := contpar +1
                acumpar := acumpar + num[num[i]]
            FIN_SI
        FIN_PARA

        ESCRIBIR("El valor del mayor numero es: ", num[posicion_max], "y su posiciion es: ", posicion_max)
        ESCRIBIR("El valor del menor numero es: ", num[posicion_min], "y su posiciion es: ", posicion_min)
        ESCRIBIR("La cantidad de pares son: ", contpar, "Y la suma de los pares son: ", acumpar)
    FIN_PROCESO
FIN_ACCION
```

> [!bug] Cinco errores a corregir
> 1. `HACAER` → **`HACER`** (tipeo).
> 2. `SI num[1] > num[posicion_max]` → **`num[i]`**. Con `num[1]` compara siempre el primer elemento y el máximo queda mal.
> 3. `SI num[i] MOD 2 = 0` **sin `ENTONCES`**. Falta la palabra clave.
> 4. `acumpar := acumpar + num[num[i]]` → **`acumpar + num[i]`**. `num[num[i]]` usa el *valor* como índice: se va de rango apenas cargues un número mayor a 100 o negativo.
> 5. `FIN_PROCESO` no existe en la notación de la cátedra: el bloque `PROCESO` cierra con `FIN_ACCION`.
>
> Además, el `SINO` anidado es correcto pero innecesario: en el mismo recorrido podés chequear máximo y mínimo con dos `SI` independientes. Ver [[errores-y-trampas]].

**Versión corregida:**

```
ACCION ej_3.2 ES
    AMBIENTE
        num: ARREGLO de [1..100] de ENTERO
        i, posicion_min, posicion_max, contpar, acumpar: ENTERO

    PROCESO
        contpar := 0
        acumpar := 0
        posicion_min := 1
        posicion_max := 1

        PARA i := 1 A 100, 1 HACER
            ESCRIBIR('Ingrese la posición ', i, ' del arreglo')
            LEER(num[i])

            SI num[i] > num[posicion_max] ENTONCES
                posicion_max := i
            FIN_SI

            SI num[i] < num[posicion_min] ENTONCES
                posicion_min := i
            FIN_SI

            SI num[i] MOD 2 = 0 ENTONCES
                contpar := contpar + 1
                acumpar := acumpar + num[i]
            FIN_SI
        FIN_PARA

        ESCRIBIR('El valor del mayor número es: ', num[posicion_max], ' y su posición es: ', posicion_max)
        ESCRIBIR('El valor del menor número es: ', num[posicion_min], ' y su posición es: ', posicion_min)
        ESCRIBIR('La cantidad de pares es: ', contpar, ' y la suma de los pares es: ', acumpar)
FIN_ACCION
```

> [!info] Por qué inicializar en 1 y no en 0
> `posicion_min` y `posicion_max` arrancan en **1**, no en 0: son *posiciones*, y la posición 1 es la única que existe con seguridad antes de leer nada. Es la misma idea que el `menor:= A[1]` de la filmina 15 de [[5 — Búsqueda y Ordenamiento]] y el `menor:=HV` de la filmina 10 de [[6 — Procesos Estadísticos]].

---

## Ejercicio de práctica — `ej_3.4`

**Consigna** ([[3 — Arreglos|Guía de Cátedra, Ejercicio 3.4]] — está copiada textual en tu apunte):

> Considerando un arreglo de 50 números enteros, confeccione un algoritmo para resolver las siguientes consignas:
>
> 1. Modificar el arreglo dado, de modo que todos sus elementos sean múltiplos de 3.
> 2. Crear otro arreglo que contenga los números que no cumplieron la condición.
> 3. Informar cuántos números cumplieron la condición.

**Lo que llegaste a escribir** — el apunte se corta acá:

```
ACCION ej_3.4 (nums: arreglo[1..50] de ENTERO)ES
    AMBIENTE
        numsno3: ARREGLOS de [1..50] de ENTEROS
        i, j, contnum: ENTERO

    PROCESO
        contnum := 0, j :=1

        PARA i := 1 a 50 HACER
```

> [!todo] Pendiente — está sin terminar
> Quedó cortado en el `PARA`. Abajo está una resolución completa para comparar, pero **rehacelo vos primero**: es exactamente el tipo de ejercicio del segundo parcial.

**Una resolución completa, para contrastar después:**

```
ACCION ej_3.4 (nums: ARREGLO de [1..50] de ENTERO) ES
    AMBIENTE
        numsno3: ARREGLO de [1..50] de ENTERO
        i, j, contnum: ENTERO

    PROCESO
        contnum := 0
        j := 1

        PARA i := 1 A 50, 1 HACER
            SI nums[i] MOD 3 = 0 ENTONCES
                # ya es múltiplo de 3: cumple la condición
                contnum := contnum + 1
            SINO
                # no cumple: lo guardo aparte y después lo llevo al múltiplo de 3 más cercano hacia arriba
                numsno3[j] := nums[i]
                j := j + 1
                nums[i] := nums[i] + (3 - (nums[i] MOD 3))
            FIN_SI
        FIN_PARA

        ESCRIBIR('Cantidad de números que ya eran múltiplos de 3: ', contnum)

        ESCRIBIR('Números que no cumplían la condición:')
        PARA i := 1 A (j - 1), 1 HACER
            ESCRIBIR(numsno3[i])
        FIN_PARA
FIN_ACCION
```

> [!warning] Dos decisiones que la consigna deja abiertas
> 1. **Cómo "modificar" para que sea múltiplo de 3.** Acá se redondea hacia arriba (`+ (3 - resto)`). Otras opciones válidas: truncar hacia abajo (`- resto`) o multiplicar por 3. Elegí una y **dejala escrita como comentario** — en el parcial se valora que expliques el criterio.
> 2. **`j` se usa como contador propio de `numsno3`**, independiente de `i`. Es el patrón de "arreglo de salida más corto que el de entrada": nunca reutilices `i` para indexar el segundo arreglo.
>
> Notá que `contnum` cuenta los que **sí** cumplían, y `j - 1` es la cantidad de los que **no**. Deben sumar 50.

---

## 🔗 Notas relacionadas

- [[4 — Arreglos]] — la teoría de cátedra de este mismo tema, completa
- [[5 — Búsqueda y Ordenamiento]] — las acciones 4 y 5 de la lista de arriba
- [[6 — Procesos Estadísticos]] — arreglos + archivos, el tema que cierra la unidad
- [[3 — Arreglos]] — los ejercicios `3.x` de la Guía de Cátedra (de ahí salen `ej_3.2` y `ej_3.4`)
- [[Ejercicios Rojas]] — tus otros ejercicios resueltos
- [[errores-y-trampas]] · [[sintaxis-completa]] · [[plantillas]]
