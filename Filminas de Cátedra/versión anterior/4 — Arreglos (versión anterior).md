---
tipo: filminas-anterior
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 4
titulo_original: 4-ARREGLOS
diapositivas: 35
fuente: Presentación de Google publicada por la cátedra
tags:
  - AED
  - filminas-anterior
  - teoria
  - arreglos
---

# 4 — Arreglos

> [!warning] Versión anterior — reemplazada
> Esta es la transcripción de la presentación **vieja** (la que había antes de la revisión 2026 que subió el profesor a la carpeta Presentaciones). La vigente es [[4 — Arreglos]]. Se conserva para comparar.


> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 35 diapositivas de la presentación **4-ARREGLOS** de la cátedra (Algoritmos y Estructuras de Datos 2026, UTN FRRe, Ingeniería en Sistemas de Información).
> Se conserva el orden y el contenido original de cada diapositiva. Las imágenes con contenido (diagramas, pseudocódigo) están recuperadas en `img/`.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**ARREGLOS**

ALGORITMOS Y ESTRUCTURAS DE DATOS 2026
UTN FRRe — Ingeniería en Sistemas de Información

---

## 2 · Disparador

> Si se contaran con datos de N estudiantes, y debieran mostrar por pantalla el nombre y el puntaje de cada caso en el examen de AED, junto con el promedio de puntaje al final.

**¿Qué herramientas de las aprendidas hasta ahora usarías?**

---

## 3 · Estructuras de Datos Estáticas

**Estructuras de Datos Estáticas**

¿Qué son? y ¿para qué sirven?

---

## 4 · Clasificación de Estructuras de Datos

**ESTRUCTURAS DE DATOS**

| | Definición |
|---|---|
| **ESTÁTICAS** | Aquellas a las que se le asigna una cantidad fija de memoria de acuerdo a lo definido en la declaración de la variable. |
| **DINÁMICAS** | Aquellas cuyo tamaño en memoria aumenta o disminuye en tiempo de ejecución de acuerdo a las necesidades del programa. |

---

## 5 · Clasificación de Estructuras de Datos | Ejemplo

**ESTRUCTURAS DE DATOS**

| | Ejemplo |
|---|---|
| **ESTÁTICAS** | Por ejemplo: los días de la semana son 7, tamaño fijo |
| **DINÁMICAS** | Por ejemplo, cantidad de personas que usan Instagram el primer día del mes, no conocemos el espacio que deberíamos reservar para almacenar datos |

---

## 6 · Estructuras de datos estáticas — definición

> [!info] ESTRUCTURAS DE DATOS ESTÁTICAS
> son aquellas en las que el tamaño ocupado en memoria se define antes de que cualquier acción se ejecute y no puede modificarse dicho tamaño durante la ejecución del proceso.

---

## 7 · Arreglos

**Arreglos**

¿Qué son? y ¿para qué sirven?

---

## 8 · Definición de Arreglos

> [!important] Definición
> El **arreglo** es una estructura de datos estática, que es capaz de almacenar, en memoria interna, una **colección de datos del mismo tipo**.
>
> Es un conjunto **homogéneo, finito y ordenado** de elementos.

Diagrama de la diapositiva — celdas numeradas 1 a 8:

```
   1     2     3     4     5     6     7     8
+-----+-----+-----+-----+-----+-----+-----+-----+
|     |     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+-----+
```

![[arreglos-vector-elemento-indice.png]]

> [!warning] Ojo con el índice inicial
> La imagen de la diapositiva rotula los índices de **0 a 7** (convención de C), mientras que el texto de la misma diapositiva los numera de **1 a 8**. En el pseudocódigo de la cátedra los arreglos arrancan en **1** — ver diapositiva 30, punto 1.

---

## 9 · Más datos importantes

| Concepto | Definición |
|---|---|
| **Tamaño** | Es el número de elementos que lo conforman |
| **Dimensión** | Indica la cantidad de índices que necesitamos para acceder a un elemento del arreglo |
| **Índice** | Representa el número de orden de cada elemento dentro del arreglo |

---

## 10 · Clasificación de arreglos por su dimensión

- **UNIDIMENSIONAL** (Vector)
- **BIDIMENSIONAL** → Matriz
- **MULTIDIMENSIONAL**

---

## 11 · Clasificación por dimensión — ejemplos

### Monto de horas extras (Ejemplo Vector)

| | |
|---|---|
| 1 | 25000 |
| 2 | 35420 |
| 3 | 22300 |
| 4 | 46210 |
| 5 | 25610 |

### Cantidad de personas inscriptas (Ejemplo Matriz)

| Carrera | Inscriptos |
|---|---|
| ISI | 1520 |
| IEM | 850 |
| IQ | 724 |
| LAR | 521 |
| TUP | 568 |

### Cantidad de personas inscriptas en 3 Regionales

La diapositiva muestra **tres tablas apiladas** (una por regional), con la misma estructura de carreras:

| Carrera | Regional 1 | Regional 2 | Regional 3 |
|---|---|---|---|
| ISI | 1520 | 750 | 512 |
| IEM | 850 | 652 | 850 |
| IQ | 724 | 724 | 724 |
| LAR | 521 | 521 | 521 |
| TUP | 568 | 568 | 568 |

> Al agregar la tercera dimensión (la regional), el mismo dato pasa de vector → matriz → arreglo multidimensional.

---

## 12 · ¿Qué tamaño y dimensión tienen estos arreglos de ejemplo?

| Ejemplo | Tamaño | Dimensión |
|---|---|---|
| Un arreglo de 100 DNIS | 100 elementos | 1 |
| Ventas por semana de un ecommerce | 7 elementos | 1 |
| El promedio de 10 estudiantes en 10 materias | 10 filas, 10 columnas | 2 |
| Cantidad de clientes que ingresaron en 2 sucursales en 3 turnos | 2 filas, 3 columnas | 2 |

---

## 13 · Qué puedo hacer utilizando Arreglos

| # | Operación | Descripción |
|---|---|---|
| **01** | **LECTURA/ESCRITURA** | Puedo acceder a un elemento o asignar un valor a un elemento del arreglo |
| **02** | **RECORRIDO** | Puedo acceder a cada uno de los elementos del arreglo ya sea para mostrar su valor o para operar con él |
| **03** | **ACTUALIZACIÓN** | Si fuera necesario puedo modificar el contenido de algún elemento o borrarlo |
| **04** | **BÚSQUEDA** | Puedo buscar en el arreglo algún elemento en particular de acuerdo a su contenido |
| **05** | **ORDENAMIENTO** | Puedo ordenar los elementos de un arreglo teniendo en cuenta algún criterio (ascendente, descendente, etc) |

> [!tip] Las operaciones 04 y 05 son el tema de la presentación siguiente
> → [[5 — Búsqueda y Ordenamiento]]

---

## 14 · Qué puedo hacer utilizando Arreglos (por qué)

> Los arreglos permiten almacenar múltiples valores en una sola variable, en lugar de declarar variables separadas para cada valor.
>
> Piensa qué pasaría si tuvieras que cargar los nombres de personas invitadas a un evento, y fueran 300…. ¿usarías 300 variables?

---

## 15 · VECTORES

**VECTORES — Empecemos a trabajar**

---

## 16 · Definición en el ambiente

```
Mi_vector : arreglo de [1..7] de entero
```

---

## 17 · Acceso a cada elemento

```
Acceso al elemento
Escribir ( a[1])

Asignación de valores
a[1] := 23
```

> [!info] Tipos de índice válidos
> Los índices de un arreglo pueden ser: **entero, lógico, caracter, enumerado o rango**.

---

## 18 · Vamos con un ejemplo

> Cargar 10 elementos en un vector, sumarlos y mostrar el resultado por pantalla.

**Pasos para resolver este problema:**

1. Leer un vector de 10 elementos
2. Sumar los elementos
3. Mostrar el resultado de la suma por pantalla

---

## 19 · Resuelto en pseudocódigo

En la diapositiva sólo figura, como texto suelto:

```
Leer(valor)
vectorA[i]:=valor
```

El pseudocódigo completo está en la imagen de la diapositiva, transcripto acá:

```
#Cargar un vector de 10 elementos, y obtener la suma total para mostrar por pantalla

ACCION ejemploarreglo ES
AMBIENTE
   vectorA: arreglo de [1...10] de entero
   i: entero
   suma:entero
PROCESO
   Esc('Arranquemos cargando el vector')
   suma:=0

   Para i:=1 hasta 10 hacer
     #cargamos
     Esc('Ingrese un valor entero')
     Leer(vectorA[i])

     #aprovechamos y sumamos
     suma:=suma+vectorA[i]
   Fin_Para

   Esc('El resultado de la suma final es: ', suma)

FIN_ACCION
```

![[arreglos-pseudocodigo-suma-vector.png]]

---

## 20 · Versión en C

```c
#include <stdio.h> //Versión en C
int main() {
    // Declaramos un arreglo (vector) de 10 elementos
    int vector[10];
    // Variable para almacenar la suma de los elementos del vector
    int suma = 0;
    // Bucle para leer los 10 elementos del vector
    printf("Ingrese 10 elementos:\n");
    for (int i = 0; i < 10; i++) {
        // Leemos cada elemento del vector y lo almacenamos en la posición i
        scanf("%d", &vector[i]);
    }
    // Bucle para sumar los elementos del vector
    for (int i = 0; i < 10; i++) {
        // Sumamos cada elemento del vector a la variable suma
        suma += vector[i];
    }
        // Mostramos el resultado de la suma por pantalla
    printf("La suma de los elementos del vector es: %d\n", suma);

    return 0; // Indicamos que el programa terminó exitosamente
}
```

Las tres llamadas de atención de la diapositiva:

- **Declaración del tipo del arreglo** → `int vector[10];`
- **Asignación de los elementos del arreglo** → el primer `for` con `scanf`
- **Suma de los elementos del arreglo** → el segundo `for` con `suma += vector[i]`

---

## 21 · Algunos compiladores online

- https://www.onlinegdb.com/online_c_compiler
- https://www.programiz.com/c-programming/online-compiler/
- https://onecompiler.com/c

---

## 22 · Otra herramienta que debes conocer

> [!important] VECTORES PARALELOS
> Dos o más arreglos que utilizan el **mismo subíndice** para acceder a elementos de distintos arreglos, se denominan **arreglos paralelos**.
> Estos arreglos pueden procesarse **simultáneamente**.

---

## 23 · Ejemplo

**Escenario**

> Se tienen dos vectores, uno conteniendo DNI y otro Edades de 5 personas. La posición de uno se corresponde con el otro. Se necesita informar el DNI y la edad por persona.

---

## 24 · Ejemplo de Vectores Paralelos

> Se tienen dos arreglos de 5 elementos.
> El primero contiene nombres de personas y el segundo contiene los sexos de las personas del primer arreglo, codificados como ´f´ y ´m´.
> Obtener a partir de estos, dos arreglos nuevos, el primero de los cuales debe contener todos los nombres de las personas de sexo 'm' y el segundo, el nombre de las personas de sexo 'f'.

---

## 25 · Cómo recorrer un arreglo

> [!info] Recorrido Normal
> Aquél que permite posicionarse en cada elemento de la estructura respetando su orden y definición.

Vector de ejemplo de la diapositiva:

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Argentina | Brasil | Chile | Suiza | Egipto |

---

## 26 · Hora de repasar

**HORA DE REPASAR**

Quiz de la cátedra: https://bit.ly/QUIZARRAYS_AED

---

## 27 · MATRICES

**MATRICES — Más power a la materia**

---

## 28 · Definición de Matriz

> [!important] Una matriz es un arreglo bidimensional
> Espacio de memoria interna que almacena elementos del mismo tipo en el que sus componentes vienen definidos por **dos subíndices**, el primero referido a la **fila** y el segundo a la **columna**.

---

## 29 · Matriz bidimensional

Esquema de la diapositiva — **FILAS** en vertical, **COLUMNAS** en horizontal:

| | 1 | 2 | 3 | 4 | … |
|---|---|---|---|---|---|
| **1** | 10 | 12 | 32 | ... | M |
| **2** | 24 | 34 | **33** | ... | ... |
| **3** | 3 | 4 | | | …. |
| **4** | ,,, | | | | N |
| **….** | ... | | | | |

La diapositiva señala `Matriz[2,3]` → el elemento **33** (fila 2, columna 3).

---

## 30 · Características de las matrices

- Todos los elementos son del mismo tipo.
- Se accede mediante dos índices: `matriz[fila][columna]`.
- Se clasifican por sus dimensiones: 2D (matriz), 3D (cubos), nD (hipermatrices).

### Consideraciones al implementar matrices

**1. Uso de índices**
- Una matriz se accede con dos índices: `matriz[fila][columna]`
- Los índices comienzan en **1**

**2. Recorridos con ciclos anidados**
- Lo más común es recorrer filas y columnas con dos bucles manejados por contador
- Recomendado inicializar en el momento de la declaración o recorrer con un ciclo para asignar valores.

**3. Errores comunes a evitar**
- Acceder a un índice fuera de rango (`m[3][4]` en una matriz 3x4).
- Confundir filas con columnas.
- No inicializar la matriz.

---

## 31 · Aplicaciones de matrices en software

La diapositiva es sólo el título con dos imágenes. Las dos aplicaciones que ilustra:

**Imagen digital como matriz de píxeles** — una foto de 59 × 65 píxeles donde cada posición guarda el valor de intensidad: `Pixel[1,1] = 124`, `Pixel[1,59] = 125`, `Pixel[65,1] = 125`, `Pixel[65,59] = 125`, `Pixel[20,20] = 44`, `Pixel[32,29] = 245`, `Pixel[40,25] = 88`, `Pixel[45,40] = 60`.

![[matrices-aplicacion-imagen-digital.png]]

**Tablero de Batalla Naval** — grilla de 10 × 10 indexada por letra (A–J) para las filas y número (1–10) para las columnas.

![[matrices-aplicacion-batalla-naval.png]]

---

## 32 · Definición en el ambiente

```
Mi_matriz : arreglo [1..3,1...7] de entero
```

- El primer rango son las **filas**
- El segundo rango son las **col**(umnas)

Ejemplo señalado en la diapositiva:

```
Posición: 3,1
Contenido:  Mi_matriz[3,1] = 9
```

---

## 33 · Definición en el ambiente en C

```c
tipo nombre[filas][columnas];
```

**Matriz de enteros 3x4**

```c
int matriz[3][4];
```

**Matriz de caracteres** (por ejemplo, para guardar letras en una sopa de letras 5x5)

```c
char letras[5][5];
```

> *Te toca a vos ver más ejemplos en C*

---

## 34 · Ejemplo

> Nos piden crear una matriz de 4×4 de números enteros que inicialmente está vacía, nos piden hacer un menú con estas opciones:
> - Rellenar TODA la matriz de números, se debe pedir que ingrese.
> - Suma de una fila seleccionada (controlar que elija 1 correcta)
> - Suma de una columna seleccionada (controlar que elija 1 correcta)
> - Sumar la diagonal principal
> - La media de todos los valores de la matriz

**Solución en C:** https://www.programiz.com/online-compiler/9c2C9lUTAgfgn

---

## 35 · Resolución en pseudocódigo

```
#Trabajar sobre una matriz 4x4
ACCION matrices ES
AMBIENTE
	mimatriz: arreglo de [1..4, 1..4] de entero
	i,j,fila: entero
PROCESO
	Esc('Cargar la matriz')
	Para i:=1 hasta 4 hacer
		Para j:= 1 hasta 4 hacer
			Leer(mimatriz[i,j])
		Fin_Para
	Fin_Para

	#Obtengo la suma de los elementos de una fila que se ingresa
Esc('Ingrese la fila que desea sumar, entre 1 y 4')
	Leer(fila)
	Si fila >= 1 y fila <= 4 entonces
		Para j:=1 hasta 4 hacer
			suma:=suma+mimatriz[fila, j]
		Fin_Para
		Esc('Suma de la fila', fila, 'es:', suma)
	contrario
		Esc('Ud ha ingresado un valor fuera de rango. Por pillo se cierra')
	Fin_SI

	#Obtener la suma de los elementos de la columna 4
	suma:=0
	Para j:= 1 hasta 4 hacer
		suma:=suma+mimatriz[j,4]
	Fin_Para
	Esc('Suma de los elementos de la columna4 es:', suma)
Fin_Accion
```

> [!bug] Dos cosas que la filmina trae mal
> 1. `suma` **no está declarada** en el AMBIENTE (sólo `i, j, fila`) y **no se inicializa en 0** antes del primer `Para`. En el segundo bloque sí se hace `suma:=0`.
> 2. La consigna de la diapositiva 34 pide **cinco** opciones de menú (incluida la diagonal principal y la media); el pseudocódigo resuelve sólo la carga, la suma de una fila y la suma de la columna 4 — y sin menú.
>
> Si esto sale en el parcial, completá lo que falta y declará `suma`. Ver [[errores-y-trampas]].

---

## 🔗 Notas relacionadas

- [[5 — Búsqueda y Ordenamiento]] — las operaciones 04 y 05 de la diapositiva 13
- [[6 — Procesos Estadísticos]] — arreglos combinados con archivos
- [[3 — Arreglos]] — los ejercicios de la Guía de Cátedra sobre este tema
- [[Arreglos]] — la página de teoría del sitio de la cátedra
- [[sintaxis-completa]] · [[plantillas]] — la notación oficial de pseudocódigo
