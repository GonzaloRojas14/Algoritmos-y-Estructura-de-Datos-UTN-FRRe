---
tipo: filminas-anterior
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 5
titulo_original: 5-BUSQUEDA Y ORDENAMIENTO
diapositivas: 33
fuente: Presentación de Google publicada por la cátedra
tags:
  - AED
  - filminas-anterior
  - teoria
  - arreglos
  - busqueda
  - ordenamiento
---

# 5 — Búsqueda y Ordenamiento en Arreglos

> [!warning] Versión anterior — reemplazada
> Esta es la transcripción de la presentación **vieja** (la que había antes de la revisión 2026 que subió el profesor a la carpeta Presentaciones). La vigente es [[5 — Búsqueda y Ordenamiento]]. Se conserva para comparar.


> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 33 diapositivas de la presentación **5-BUSQUEDA Y ORDENAMIENTO** de la cátedra. Se conserva el orden original.
> Las pruebas de escritorio se reconstruyeron respetando la disposición de filas y columnas de cada tabla, y las trazas que eran imágenes están recuperadas en `img/`.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

> [!warning] Esta presentación arrastra diapositivas de la plantilla
> Las diapositivas **3, 4, 6, 7, 8, 9 y 10** son el relleno de ejemplo de la plantilla de Google Slides (la historia del Traductor de Google, "Alberto", "Marcos" y los "Consejo:"). **No son contenido de la materia.** Están transcriptas igual, marcadas, para que la numeración coincida con la presentación real.

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS**

Búsqueda y Ordenamiento en Arreglos

---

## 2 · Disparadores

**Pregunta 1**

> ¿Cómo podemos hacer para acceder directamente a un elemento de un arreglo que nos interesa en forma particular?

**Pregunta 2**

> ¿Puedo beneficiarme al usar arreglos? ¿Cómo?
> ¿Generando rankings por ejemplo? ¿Qué técnica puedo usar?

---

## 3 · *(diapositiva de plantilla)*

> [!warning] Relleno de la plantilla — no es contenido de la materia
> **¿Cuántos idiomas tendríamos que saber para comunicarnos con el resto del mundo?**
>
> *Consejo:* En este ejemplo, iniciamos la presentación con algo inesperado. Mientras que la audiencia piensa en un número, les sorprendemos con la siguiente diapositiva.

---

## 4 · *(diapositiva de plantilla)*

> [!warning] Relleno de la plantilla — no es contenido de la materia
> **¡Solo uno! El tuyo.** (Con un poco de ayuda de tu smartphone, claro)
>
> *Consejo:* Recuerda: si algo suena a sentido común, la gente lo ignora. Destaca lo inesperado de tu tema.

---

## 5 · Búsqueda en Arreglos. ¿Cómo?

> [!important] Definición
> Los procesos de búsqueda en arreglos involucran **recorrer un arreglo completo** con el fin de encontrar algo que necesitamos encontrar.

Los tres métodos que se ven en la materia:

1. **LINEAL**
2. **LINEAL con CENTINELA**
3. **BINARIA o DICOTÓMICA**

---

## 6 · *(diapositiva de plantilla)*

> [!warning] Relleno de la plantilla — no es contenido de la materia
> La aplicación Traductor de Google puede traducir lo que quieras en hasta un máximo de NOVENTA IDIOMAS, ya sea alemán, japonés, checo o zulú.
>
> *Consejo:* No esperes hasta el final de la presentación para revelar el mensaje principal. Menciona antes tu producto o idea (en este caso, una aplicación de traducción).

---

## 7 · *(diapositiva de plantilla)*

> [!warning] Relleno de la plantilla — no es contenido de la materia
> **2. Ejemplos**
>
> Al final de este apartado, la audiencia debe ser capaz de responder a estas dos preguntas:
> ¿Qué? ¿Qué problema solucionas con tu propuesta?
> ¿Quién? Expón el caso de una persona concreta que pueda beneficiarse de tu solución.

---

## 8 · *(diapositiva de plantilla)*

> [!warning] Relleno de la plantilla — no es contenido de la materia
> Este es Alberto. Hace poco se marchó de España a un pueblo pequeño de Irlanda del norte. Le encanta el fútbol, pero no podía comunicarse con el entrenador ni con los jugadores de un equipo.
>
> *Consejo:* Si es posible, cuéntale el problema a la audiencia a través de la historia de una persona.

---

## 9 · *(diapositiva de plantilla)*

> [!warning] Relleno de la plantilla — no es contenido de la materia
> Este es Marcos. Hace poco abrió una tienda de cámaras de fotos cerca del Museo del Louvre en París. Las personas que visitan su tienda (turistas en su mayoría) hablan varios idiomas, por lo que atenderlas supone todo un reto para él.
>
> *Consejo:* Si un ejemplo no es suficiente para que la audiencia entienda la magnitud del problema, pon alguno más.
>
> Esta historia es solo para fines ilustrativos.

---

## 10 · *(diapositiva de plantilla)*

> [!warning] Relleno de la plantilla — no es contenido de la materia
> Debido a la barrera del idioma, Alberto se sentía solo y el negocio de Marcos se vio resentido.
>
> *Consejo:* Lo ideal es que hables de personas en situaciones diferentes, pero que todas ellas puedan beneficiarse de tu solución.

---

## 11 · BÚSQUEDA LINEAL

> [!important] BÚSQUEDA LINEAL
> Consiste en ir comparando el elemento que se busca con **cada** elemento del arreglo.
> En cada paso, se compara el elemento ingresado con el contenido en la posición `i`; si son iguales se realiza la acción que determine la consigna y **se continúa con el recorrido** hasta alcanzar la posición N del arreglo.

---

## 12 · FAQ > BÚSQUEDA LINEAL — elementos repetidos

**¿Qué ocurre si el ELEMENTO BUSCADO está repetido en el arreglo?**

> El proceso los encuentra a **TODOS** y en cada ocurrencia del elemento buscado con los valores del arreglo, el proceso me permite actuar.

Arreglo `A` del ejemplo:

| 1 | 2 | 3 |
|---|---|---|
| 123 | 234 | 123 |

```
Leer(dato) //supongamos el 123
J:= 0
PARA i:= 1 a 3 HACER
SI (dato = A[i]) ENTONCES    
	ESC('Encontrado en posición',i)
  		J := J +1
FIN SI
FIN_PARA
SI J = 0 ENTONCES
  ESC('No se encontró el elemento')
FIN_SI
```

**Prueba de escritorio**

| dato | J | i | A[i] | |
|---|---|---|---|---|
| 123 | - | - | - | |
| 123 | 0 | - | - | |
| 123 | 0 | 1 | - | |
| 123 | 0 | 1 | 123 | Encontrado en Posición 1 |
| 123 | 1 | 2 | 234 | |
| 123 | 1 | 3 | 123 | Encontrado en Posición 3 |

---

## 13 · FAQ > BÚSQUEDA LINEAL

**¿Hasta cuándo recorro el arreglo?**

---

## 14 · FAQ > BÚSQUEDA LINEAL — respuesta

1. Cómo debemos recorrer todo el arreglo es más conveniente hacer uso de un **recorrido natural**.
2. Este es el **único método para búsquedas múltiples**.
3. Considerando la **Cantidad de Comparaciones**:
   - **a. Mejor Caso** — El elemento buscado está en la primera posición. Es decir, se hace una sola comparación.
   - **b. Peor Caso** — El elemento buscado está en la última posición. Necesitándose realizar igual cantidad de comparaciones que de elementos el arreglo.
   - **c. En Promedio** — El elemento buscado está en las proximidades de la mitad del arreglo. Necesitando en promedio, la mitad de comparaciones que de elementos.

---

## 15 · BÚSQUEDA LINEAL — Ejemplos

```
//BÚSQUEDA DEL MENOR ELEMENTO EN UN VECTOR DE 10 POSICIONES
menor:= A[1]
PARA i:= 2 a 10 HACER
  SI (A[i] < menor) ENTONCES   
     menor:=A[i]
  FIN SI
FIN PARA
ESC('El menor elemento es: ', menor)
```

**¿Qué pasará si hay varios elementos iguales?**

---

## 16 · BÚSQUEDA LINEAL con CENTINELA

> [!important] BÚSQUEDA LINEAL con CENTINELA
> El método se basa en efectuar un recorrido del arreglo y **en el momento de hallar lo buscado, terminar con el recorrido**.
> El procedimiento utiliza un **ciclo indefinido** teniendo en cuenta el valor de una variable denominada **centinela**, que controla si el elemento buscado se ha encontrado.

---

## 17 · FAQ > BÚSQUEDA LINEAL CON CENTINELA — arreglos desordenados

**¿Cuándo se recomienda usar?** Se usa sobre **arreglos desordenados**.

**¿Cómo funciona en arreglos desordenados?**

1. El método recorre desde el principio el arreglo, y si no encuentra el elemento buscado llega al final del arreglo.
2. Además, como finaliza al encontrar lo buscado, **NO permite hallar elementos repetidos**.
3. En caso de éxito, dado que no necesita recorrer totalmente el arreglo es **más veloz que el Lineal**, pues finaliza la búsqueda.

---

## 18 · FAQ > BÚSQUEDA LINEAL CON CENTINELA — ejemplo desordenado

Arreglo `A` del ejemplo:

| 1 | 2 | 3 |
|---|---|---|
| 123 | 234 | 124 |

```
Leer (dato) //supongamos el 123
x:= 1   
Mientras (x<3) y (dato<>A[x]) hacer
 x := x +1
Fin Mientras
SI dato = A[x] Entonces 
	ESC("Elemento encontrado en",x)
Contrario 
	ESC("La búsqueda fracasó")
Fin Si
```

**PRUEBA DE ESCRITORIO**

| dato | x | A[i] | |
|---|---|---|---|
| 123 | - | - | |
| 123 | 1 | - | |
| 123 | 1 | 123 | Elemento encontrado en 1 |

---

## 19 · FAQ > BÚSQUEDA LINEAL CON CENTINELA — arreglos ordenados

> [!important] ARREGLOS ORDENADOS
> El método se basa en efectuar un recorrido del arreglo y en el momento de hallar lo buscado, **o en su defecto el inmediato mayor** (orden creciente) **/ inmediato menor** (orden decreciente), terminar con el recorrido.

> Por ejemplo, si se busca en el siguiente arreglo el elemento **17**, el algoritmo termina al acceder al elemento de la **posición 3** pues es mayor al buscado.

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 12 | 13 | 18 | 39 | 45 |

---

## 20 · FAQ > BÚSQUEDA LINEAL CON CENTINELA — cómo funciona en ordenados

**¿Cómo funciona en arreglos ordenados?**

1. Este método a diferencia del anterior **cambia el símbolo de comparación** por `<` o `>` según el orden del arreglo.
2. Igual que para desordenados, como finaliza al encontrar lo buscado, **NO permite hallar elementos repetidos**.
3. Al estar el arreglo ordenado es **aún más rápido** que si estuviera desordenado.

---

## 21 · FAQ > BÚSQUEDA LINEAL CON CENTINELA — ejemplo ordenado

Arreglo `A` del ejemplo:

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| 12 | 13 | 17 | 22 |

```
Leer (dato) //supongamos el 17
x:= 1  
Mientras (x<4) y (dato>A[x]) hacer
 x := x +1
Fin Mientras
SI dato = A[x] Entonces
  ESC("Elemento encontrado en",x)
Contrario
  ESC("La búsqueda fracasó")
Fin Si
```

**PRUEBA DE ESCRITORIO**

| dato | x | A[i] | |
|---|---|---|---|
| 17 | - | - | |
| 17 | 1 | - | |
| 17 | 1 | 12 | |
| 17 | 2 | 13 | |
| 17 | 3 | 17 | Elemento encontrado en 3 |

---

## 22 · BÚSQUEDA BINARIA

> [!important] BÚSQUEDA BINARIA
> El método se aplica sobre **arreglos ordenados únicamente**.
> La Búsqueda Binaria o dicotómica compara si el valor buscado está en la **mitad superior o inferior**. En la que esté, subdivido nuevamente, y así sucesivamente hasta encontrar el valor.

---

## 23 · FAQ > BÚSQUEDA BINARIA o dicotómica — cómo funciona

1. Se definen los valores del rango del arreglo como **variables independientes** (límite inferior o izquierdo y límite superior o derecho).
2. Se calcula el valor posicional **Medio** del arreglo como el promedio de los límites.
3. Se verifica si el elemento buscado se encuentra en el medio del arreglo (**Éxito**) o caso contrario se determina sobre qué **subvector** se continúa la búsqueda (subvector de la derecha o de la izquierda).

---

## 24 · FAQ > BÚSQUEDA BINARIA o dicotómica — ejemplo

Arreglo `A` del ejemplo:

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 12 | 13 | 17 | 22 | 32 |

```
Leer (dato) //supongamos el 22
izq:= 1 ; der:= 5
Medio:=(izq + der) DIV 2 DIV 2
Mientras (izq < der) y (dato <> A[medio] ) hacer
 SI dato < A[medio] Entonces
  Der := medio -1
 Contrario
  Izq := medio + 1
 Fin Si
 Medio := (izq + Der) DIV 2
Fin Mientras
SI dato = A[medio] Entonces
  ESC("Elemento encontrado en", medio)
 Contrario
  ESC("No está el elemento")
Fin Si
```

> [!bug] Errata de la filmina
> La tercera línea dice `Medio:=(izq + der) DIV 2 DIV 2` — el `DIV 2` está **repetido**. Lo correcto es `Medio:=(izq + der) DIV 2`, que es además lo que usa la propia prueba de escritorio de la diapositiva: `(1+5) DIV 2 = 3`. Con el `DIV 2` duplicado daría 1.

**PRUEBA DE ESCRITORIO**

| dato | Izq | der | medio | A[i] | |
|---|---|---|---|---|---|
| 22 | - | | | - | |
| 22 | 1 | 5 | - | - | |
| 22 | 1 | 5 | 3 | 17 | |
| 22 | 4 | 5 | 3 | 17 | |
| 22 | 4 | 5 | 4 | 22 | Elemento encontrado en 4 |

---

## 25 · FAQ > BÚSQUEDA BINARIA o dicotómica — rendimiento

1. Este método es **rápido en forma proporcional al tamaño del vector**. Más grande el vector mejor será la perfomance del método.
2. Si el vector es pequeño, es más conveniente por la poca cantidad de acciones a ejecutar, el **método lineal con centinela para ordenados**.
3. En el **mejor de los casos** el elemento buscado estará en el centro, por lo que solo ejecutará una sola comparación.
4. Si el elemento buscado está sobre uno de los **extremos** será el **peor caso**, y el algoritmo ejecutará **log₂(n)** cantidad de comparaciones.

---

## 26 · Ordenamiento en Arreglos. ¿Cómo?

> [!important] Por qué ordenar
> Debido a que las estructuras de datos son utilizadas para almacenar información, para poder **recuperar esa información de manera eficiente** es deseable que esté ordenada.
>
> **Ordenar datos** significa moverlos para que queden en una secuencia tal que represente un orden, el cual puede ser numérico, alfabético o incluso alfanumérico, ascendente o descendente.

Los tres métodos que se ven en la materia:

1. **SELECCIÓN**
2. **INSERCIÓN**
3. **INTERCAMBIO**

---

## 27 · SELECCIÓN

> [!important] SELECCIÓN
> El método de ordenamiento por selección consiste en encontrar el **menor de todos** los elementos del arreglo e **intercambiarlo con el que está en la primera posición**.
> Luego el segundo más pequeño, y así sucesivamente hasta ordenar todo el arreglo.

---

## 28 · ORDENAMIENTO POR SELECCIÓN

> El método selecciona el elemento menor del arreglo no ordenado y se lo ubica en el arreglo ordenado.

```
Para i:=1 a (N-1) hacer
 x:=A[i]
 MIN:=i;
 Para j:=(i+1) a N hacer
   Si A[j] < x entonces
      MIN:=j;
      x:=A[j]
   Fin si
 Fin para
 A[MIN]:=A[i]
 A[i]:=x
Fin para
```

> [!info] Nota de la diapositiva
> En el caso que los elementos queden ordenados en el arreglo, el método **igualmente seguirá procesando** hasta llegar al último elemento.

**Traza de la diapositiva** — arreglo inicial `44 55 12 94 42`:

| Paso | Arreglo | Qué se intercambia |
|---|---|---|
| inicial | 44 · 55 · 12 · 94 · 42 | |
| 1 | **12** · 55 · 44 · 94 · 42 | 44 ↔ 12 |
| 2 | 12 · **42** · 44 · 94 · 55 | 55 ↔ 42 |
| 3 | 12 · 42 · **44** · 94 · 55 | 44 ya está en su lugar |
| 4 | 12 · 42 · 44 · **55** · 94 | 94 ↔ 55 |

![[orden-seleccion-traza.png]]

---

## 29 · INSERCIÓN

> [!important] INSERCIÓN
> Consta de tomar uno por uno los elementos de un arreglo y recorrerlo hacia su posición con respecto a los anteriormente ordenados.
> Así empieza con el **segundo** elemento y lo ordena con respecto al primero. Luego sigue con el tercero y lo coloca en su posición ordenada con respecto a los dos anteriores, así sucesivamente hasta recorrer todas las posiciones del arreglo.

---

## 30 · ORDENAMIENTO POR INSERCIÓN

> El método realiza comparaciones y ubica el elemento en la posición correcta de acuerdo al orden deseado.

```
Para i:= 2 a N hacer
 x:= A[i];
 j:=i-1;
 Mientras(x < A[j]) ^ (j > 0) hacer
 	A[j+1]:= A[j]
 	j:= j -1
 Fin Mientras
 A[j+1]:=x
Fin para
```

**Traza de la diapositiva** — la analogía de las cartas, mano inicial `5 · 3 · 4 · 2`:

| Paso | Mano |
|---|---|
| inicial | 5 · 3 · 4 · 2 |
| 1 | **3** · 5 · 4 · 2 |
| 2 | 3 · **4** · 5 · 2 |
| 3 | **2** · 3 · 4 · 5 |

![[orden-insercion-cartas-1.png]]
![[orden-insercion-cartas-2.png]]
![[orden-insercion-cartas-3.png]]
![[orden-insercion-cartas-4.png]]

---

## 31 · INTERCAMBIO

> [!important] INTERCAMBIO
> La principal característica de este método es el **intercambio entre pares de ítems**.
> Se basa en el principio de **comparar e intercambiar pares de ítems adyacentes** hasta que todos estén ordenados.

---

## 32 · ORDENAMIENTO POR INTERCAMBIO

> El método realiza solo la **cantidad de pasadas necesarias + una extra** para verificar que el arreglo quede efectivamente ordenado. Esto lo diferencia de los otros métodos.

```
Bandera:= Falso; 
Mientras NO Bandera hacer 	
	Bandera:= Verdadero; 	
	Para j:=1 hasta (N-1) hacer 
		Si A[j] > A[j+1] entonces 
			X:=A [j]; 
			A[j] := A[j+1]; 
			A[j+1]:=X; 
			Bandera:= Falso; 
		Fin si 
	Fin para 
Fin mientras
```

---

## 33 · ORDENAMIENTO POR INTERCAMBIO — traza completa

La diapositiva es sólo el título con dos imágenes, que contienen las **cuatro pasadas** del método sobre el arreglo `44 · 55 · 12 · 94 · 42`.

### Pasada 1

| j | Arreglo | Comparación |
|---|---|---|
| 1 | 44 · 55 · 12 · 94 · 42 | 44 vs 55 → no cambia |
| 2 | 44 · 55 · 12 · 94 · 42 | 55 vs 12 → **intercambia** |
| 3 | 44 · 12 · 55 · 94 · 42 | 55 vs 94 → no cambia |
| 4 | 44 · 12 · 55 · 94 · 42 | 94 vs 42 → **intercambia** |
| fin | 44 · 12 · 55 · 42 · 94 | |

### Pasada 2

| j | Arreglo | Comparación |
|---|---|---|
| 1 | 44 · 12 · 55 · 42 · 94 | 44 vs 12 → **intercambia** |
| 2 | 12 · 44 · 55 · 42 · 94 | 44 vs 55 → no cambia |
| 3 | 12 · 44 · 55 · 42 · 94 | 55 vs 42 → **intercambia** |
| 4 | 12 · 44 · 42 · 55 · 94 | 55 vs 94 → no cambia |
| fin | 12 · 44 · 42 · 55 · 94 | |

![[orden-intercambio-pasadas-1-2.png]]

### Pasada 3

| j | Arreglo | Comparación |
|---|---|---|
| 1 | 12 · 44 · 42 · 55 · 94 | 12 vs 44 → no cambia |
| 2 | 12 · 44 · 42 · 55 · 94 | 44 vs 42 → **intercambia** |
| 3 | 12 · 42 · 44 · 55 · 94 | 44 vs 55 → no cambia |
| 4 | 12 · 42 · 44 · 55 · 94 | 55 vs 94 → no cambia |
| fin | 12 · 42 · 44 · 55 · 94 | |

### Pasada 4 — la pasada extra de verificación

| j | Arreglo | Comparación |
|---|---|---|
| 1 | 12 · 42 · 44 · 55 · 94 | 12 vs 42 → no cambia |
| 2 | 12 · 42 · 44 · 55 · 94 | 42 vs 44 → no cambia |
| 3 | 12 · 42 · 44 · 55 · 94 | 44 vs 55 → no cambia |
| 4 | 12 · 42 · 44 · 55 · 94 | 55 vs 94 → no cambia |
| fin | 12 · 42 · 44 · 55 · 94 | `Bandera` queda en Verdadero → corta |

![[orden-intercambio-pasadas-3-4.png]]

---

## 📌 Resumen de los métodos (armado a partir de las diapositivas)

### Búsqueda

| Método | Requiere ordenado | Encuentra repetidos | Comparaciones (peor caso) | Diapositivas |
|---|---|---|---|---|
| **Lineal** | No | **Sí — es el único** | N | 11–15 |
| **Lineal con centinela** (desordenado) | No | No | N | 16–18 |
| **Lineal con centinela** (ordenado) | Sí | No | N, corta antes | 19–21 |
| **Binaria / dicotómica** | **Sí, obligatorio** | No | log₂(n) | 22–25 |

### Ordenamiento

| Método | Idea | Diapositivas |
|---|---|---|
| **Selección** | Busca el menor y lo lleva a la primera posición; repite con el resto | 27–28 |
| **Inserción** | Toma cada elemento y lo inserta en su lugar entre los ya ordenados | 29–30 |
| **Intercambio** | Compara e intercambia pares adyacentes; usa `Bandera` y hace una pasada extra de verificación | 31–33 |

---

## 🔗 Notas relacionadas

- [[4 — Arreglos]] — la presentación anterior; búsqueda y ordenamiento son las operaciones 04 y 05 de su diapositiva 13
- [[6 — Procesos Estadísticos]] — la siguiente
- [[3 — Arreglos]] — los ejercicios de la Guía de Cátedra sobre este tema
- [[sintaxis-completa]] · [[plantillas]] — la notación oficial de pseudocódigo
