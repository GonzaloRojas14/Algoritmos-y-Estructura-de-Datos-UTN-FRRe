---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 4
titulo_original: Arreglos — Clase 1 — Fundamentos teóricos
archivo_original: Arreglos_Clase1_Fundamentos_2.pdf
diapositivas: 34
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - arreglos
  - vectores
  - matrices
---

# 4 — Arreglos

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 34 diapositivas de **Arreglos — Clase 1 — Fundamentos teóricos** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[Arreglos_Clase1_Fundamentos_2.pdf]] (carpeta `PDF originales/`).
> Las secciones siguen el número de **página del PDF** (1 a 34). El pie de cada diapositiva trae su propia numeración (01 a 25): varias diapositivas se repiten como **ampliación del código** de la anterior, y eso se indica en cada caso.

> [!info] Cambios respecto de la versión anterior
> La versión anterior era otra presentación (Google Slides, 35 diapositivas): [[4 — Arreglos (versión anterior)]].
> - **Temas nuevos:** tipos simples vs. estructurados, motivación con 50 notas, arreglo como colección *finita, homogénea y ordenada* (F-H-O), memoria interna vs. externa, **Número Total de Componentes (NTC)** para vector, matriz y n dimensiones, arreglos de 3 dimensiones, tabla vector vs. matriz, operaciones válidas (sin inserción ni eliminación), acciones completas de **carga y recorrido** de vector y matriz, **recorrido con MIENTRAS y centinela**, recorrido de matriz **por filas vs. por columnas**, errores comunes y síntesis.
> - **Se sacó:** estructuras estáticas vs. dinámicas, tipos de índice válidos, el ejemplo de suma de un vector y su **versión en C**, compiladores online, **vectores paralelos**, recorrido normal (Argentina/Brasil…), el quiz, las aplicaciones con imagen y batalla naval, la declaración de matrices en C y el ejercicio del menú sobre una matriz 4×4.
> - **Notación:** cambió. Antes `vectorA: arreglo de [1...10] de entero`, `Para i:=1 hasta 10 hacer … Fin_Para`, `Esc(...)`, comentarios con `#` y sin punto y coma. Ahora `v: arreglo [1..50] de entero;` (sin el `de` antes del rango), `PARA i:=1 HASTA 50 HACER … FIN_PARA;` en mayúsculas, `Escribir(...)`, `Accion X ES; Ambiente … Proceso … FinAccion.` y punto y coma al final de cada sentencia.
> - **Erratas de la versión anterior:** ninguna sigue. La de los índices 0..7 vs. 1..8 ya no aparece (toda la presentación numera desde 1), y el pseudocódigo de la matriz 4×4 sin `suma` declarada y con 3 de las 5 opciones resueltas ya no está en la presentación. Esta versión trae erratas propias (páginas 6, 21 y 25).

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE

**Arreglos**

**Clase 1 — Fundamentos teóricos**

*Definición · Vectores y matrices · Carga, lectura y recorrido*

---

## 2 · ¿Qué vamos a aprender hoy?

*OBJETIVOS DE LA CLASE*

1. **Por qué existen los arreglos**
   El problema de manejar muchos datos del mismo tipo sin una estructura que los agrupe.
2. **Vectores y matrices**
   Arreglos unidimensionales y bidimensionales: definición, declaración y diferencias.
3. **Componentes e índices**
   Cómo se nombra y se accede a cada elemento de un arreglo.
4. **Operaciones fundamentales**
   Carga, lectura y recorrido de arreglos, en pseudocódigo completo.

---

## 3 · Tipos de datos: simples vs. estructurados

*REPASO RÁPIDO*

| **Tipos simples**<br>*Guardan UN solo valor por variable.* | **Tipos estructurados**<br>*Agrupan varios valores bajo un mismo nombre.* |
|---|---|
| `entero` | `registro` |
| `real` | `archivo` |
| `caracter` | `secuencia` |
| `logico` | **`arreglo  ← hoy`** |
| `alfanumerico / AN(longitud)` | |

---

## 4 · El problema: 50 notas de un curso

*MOTIVACIÓN*

**Sin arreglos**

```
nota1: real;
nota2: real;
nota3: real;
...
nota50: real;
```

**Con un arreglo**

```
notas: arreglo [1..50] de real;

PARA i:=1 HASTA 50 HACER
    Leer(notas[i]);
FIN_PARA;
```

*50 variables sueltas no escalan: código repetitivo, propenso a errores y difícil de generalizar. Un arreglo agrupa todo bajo un nombre y un índice.*

---

## 5 · ¿Qué es un arreglo?

*CONCEPTO CENTRAL*

> [!important] Definición
> Colección **FINITA**, **HOMOGÉNEA** y **ORDENADA** de elementos.

| **F** — Finita | **H** — Homogénea | **O** — Ordenada |
|---|---|---|
| Tiene un límite: se define de antemano la cantidad máxima de elementos. | Todos sus componentes son del mismo tipo de dato (todos enteros, todos reales, etc.). | Se puede identificar el primero, el segundo, ..., el enésimo elemento. |

---

## 6 · Memoria interna y memoria externa

*DÓNDE VIVE UN ARREGLO*

| Memoria interna (RAM) | Memoria externa (archivos) |
|---|---|
| • **Temporal:** los datos se pierden al finalizar el programa. | • **Persistente:** los datos sobreviven al fin del programa. |
| • Acceso directo y rápido a cada posición. | • Acceso secuencial o indexado, más lento que la RAM. |
| • Acá viven las variables, los arreglos y los registros mientras el programa se ejecuta. | • La usan las `SECUENCIA` y el `ARCHIVO`. |

> [!important] El arreglo es una estructura ESTÁTICA
> Vive en memoria interna y se usa como soporte mientras el programa corre. Su tamaño y el tipo de sus elementos se definen a priori, en la declaración, y no cambian durante la ejecución. Por eso no existen operaciones de inserción ni eliminación: solo lectura, escritura y asignación sobre posiciones ya definidas.

> [!bug] Errata de la filmina
> "La usan **las** SECUENCIA y el ARCHIVO": falta de concordancia (sería "la SECUENCIA" o "las SECUENCIAS"). Es sólo de redacción.

---

## 7 · Componentes e índices

*ANATOMÍA DE UN ARREGLO*

```
                                   Componente
Nombre del arreglo: notas               │
┌──────┬──────┬──────┬──────┬──────┬──────┐
│  12  │  45  │   7  │ [88] │   3  │  60  │
└──────┴──────┴──────┴──────┴──────┴──────┘
   1      2      3      4      5      6
   ┆
 Índice
```

(La celda 4, valor **88**, está resaltada como "Componente"; los números de abajo son los índices.)

Para referenciar un elemento se necesitan dos cosas: **el nombre del arreglo** y **el índice**. Ejemplo: `notas[4]` → accede al elemento en la posición 4 (valor 88).

---

## 8 · PARTE 1 — Vectores

**PARTE 1**

**Vectores**

Arreglos unidimensionales

---

## 9 · Declaración de un vector

*VECTORES*

```
┌─────┬─────┬─────┬─────┬─────┬─────┐
│ V1  │ V2  │ V3  │     │     │ V50 │
└─────┴─────┴─────┴─────┴─────┴─────┘
   1     2     3     …     …    50
```

> [!info] Número Total de Componentes
> **NTC = límsup − líminf + 1**
>
> Para V[1..50]:
> NTC = 50 − 1 + 1 = 50 elementos

**Sintaxis general**

```
v: arreglo [li..ls] de tipo;
```

*Ejemplo: V, un vector de 50 enteros*

```
v: arreglo [1..50] de entero;
```

---

## 10 · ¿Para qué se usan los vectores?

*VECTORES EN LA PRÁCTICA*

| # | Uso | Descripción |
|---|---|---|
| 1 | **Notas de un curso** | 35 alumnos → un vector de 35 posiciones, una por alumno. |
| 2 | **Temperaturas diarias** | Registro de 365 mediciones a lo largo de un año. |
| 3 | **Stock de productos** | Cantidad disponible de cada artículo en un depósito. |
| 4 | **Nombres de meses** | Doce posiciones fijas y ordenadas, una por mes. |

---

## 11 · PARTE 2 — Matrices

**PARTE 2**

**Matrices**

Arreglos bidimensionales y multi dimensionales

---

## 12 · Declaración de una matriz

*MATRICES*

*columnas →* · *filas (renglones)*

| | | | | | |
|---|---|---|---|---|---|
| 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6 |
| 2,1 | 2,2 | 2,3 | 2,4 | **[2,5]** | 2,6 |
| 3,1 | 3,2 | 3,3 | 3,4 | 3,5 | 3,6 |
| 4,1 | 4,2 | 4,3 | 4,4 | 4,5 | 4,6 |
| 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6 |

(La celda **2,5** está resaltada.)

> [!info] NTC de una matriz
> `NTC = (filSup−filInf+1) × (colSup−colInf+1)`
>
> Ejemplo: matriz [1..10, 1..5]
> NTC = 10 × 5 = 50 elementos

**Sintaxis general**

```
m: arreglo [1..f, 1..c] de tipo;
```

*Se referencia con dos índices: primero fila, luego columna.*

```
m[2,5]  ← fila 2, columna 5
```

---

## 13 · ¿Para qué se usan las matrices?

*MATRICES EN LA PRÁCTICA*

| # | Uso | Descripción |
|---|---|---|
| 1 | **Planilla de notas** | Filas = alumnos, columnas = parciales. m[alumno, parcial]. |
| 2 | **Tablero de juego** | Ajedrez, buscaminas: cada celda es una posición (fila, columna). |
| 3 | **Imagen digital** | Cada píxel es un componente ubicado por (fila, columna). |
| 4 | **Distancias entre ciudades** | Tabla cruzada: d[origen, destino]. |

---

## 14 · Vector vs. Matriz

*COMPARACIÓN*

| Aspecto | Vector (1D) | Matriz (2D) |
|---|---|---|
| Dimensiones | Una | Dos (filas y columnas) |
| Índices por elemento | `Uno: v[i]` | `Dos: m[i, j]` |
| Declaración | `arreglo [1..n] de tipo` | `arreglo [1..f, 1..c] de tipo` |
| Recorrido típico | Un ciclo PARA | Dos ciclos PARA anidados |
| Ejemplo de uso | Notas de un curso | Planilla alumno × parcial |

---

## 15 · Arreglos de más de dos dimensiones (ejemplo)

*UN PASO MÁS ALLÁ*

Se generaliza el concepto: N dimensiones → N índices para referenciar cada componente.

**Ejemplo**

Producción de una empresa: 5 departamentos × 12 meses × 4 años.

```
a: arreglo [1..5,1..12,1..4] de real;
a[dpto, mes, anio]
```

---

## 16 · Arreglos de más de dos dimensiones (NTC generalizado)

*UN PASO MÁS ALLÁ* — misma diapositiva que la anterior (pie 15), con el recuadro inferior cambiado.

Se generaliza el concepto: N dimensiones → N índices para referenciar cada componente.

> [!info] NTC generalizado
> **NTC = (LS₁−LI₁+1) × (LS₂−LI₂+1) × … × (LSₙ−LIₙ+1)**

Para el ejemplo: 5 × 12 × 4 = 240 elementos.

---

## 17 · PARTE 3 — Operaciones sobre arreglos

**PARTE 3**

**Operaciones sobre arreglos**

Carga, lectura y recorrido

---

## 18 · Operaciones válidas sobre un arreglo

*PANORAMA*

| Operación | Descripción |
|---|---|
| **Lectura / Carga** | Asignar un valor a cada componente, típicamente con un ciclo PARA. |
| **Escritura / Recorrido** | Recuperar y mostrar el valor de cada componente. |
| **Asignación** | Modificar el valor de una posición puntual ya existente del arreglo. |
| **Recorrido condicional** | Recorrer con MIENTRAS hasta que se cumpla una condición (p. ej. un centinela). |
| *Búsqueda* | *Encontrar la posición de un valor dentro del arreglo.* |
| *Ordenamiento* | *Reorganizar los componentes según un criterio de orden.* |

(En la filmina, Búsqueda y Ordenamiento aparecen en gris: no son tema de esta clase.)

*El arreglo es estático: no hay inserción ni eliminación de posiciones. Hoy vemos lectura, carga y recorrido. Búsqueda y Ordenamiento → Clase 2.*

---

## 19 · Carga de un vector

*OPERACIÓN: CARGA*

```
Accion CARGAR_VECTOR ES;
Ambiente
    v: arreglo [1..50] de entero;
    i: entero;
Proceso
    PARA i:=1 HASTA 50 HACER
        Leer(v[i]);
    FIN_PARA;
FinAccion.
```

**Lectura del algoritmo**

- `i` recorre cada índice, de 1 a 50.
- `v[i]` es la posición que se está cargando.
- `Leer(v[i])` ingresa un valor directamente en esa posición.
- Al terminar el ciclo, las 50 posiciones tienen un valor asignado.

---

## 20 · Carga de un vector (ampliación del código)

Ampliación a pantalla completa del código de la página 19 (pie 18):

```
Accion CARGAR_VECTOR ES;
Ambiente
    v: arreglo [1..50] de entero;
    i: entero;
Proceso
    PARA i:=1 HASTA 50 HACER
        Leer(v[i]);
    FIN_PARA;
FinAccion.
```

---

## 21 · Recorrido (lectura) de un vector

*OPERACIÓN: RECORRIDO*

```
Accion MOSTRAR_VECTOR (arreglo [1..50] de entero) ES;
Ambiente
    i: entero;
Proceso
    PARA i:=1 HASTA 50 HACER
        Escribir(v[i]);
    FIN_PARA;
FinAccion.
```

> [!info] Recorrer = visitar cada elemento
> Recorrer un arreglo significa pasar por cada una de sus posiciones, en orden, para leer, mostrar o procesar su contenido.
>
> *La estructura del ciclo es idéntica a la de carga: cambia solo la acción interna (Leer → Escribir).*

> [!bug] Errata de la filmina
> El parámetro `(arreglo [1..50] de entero)` **no tiene nombre**, pero el cuerpo usa `v[i]`. Para que `v` exista dentro de la acción, el parámetro tendría que declararse con nombre (por ejemplo `v: arreglo [1..50] de entero`). Lo mismo pasa en `MOSTRAR_HASTA_CENTINELA` (página 25).

---

## 22 · Recorrido (lectura) de un vector (ampliación del código)

Ampliación a pantalla completa del código de la página 21 (pie 19):

```
Accion MOSTRAR_VECTOR (arreglo [1..50] de entero) ES;
Ambiente
    i: entero;
Proceso
    PARA i:=1 HASTA 50 HACER
        Escribir(v[i]);
    FIN_PARA;
FinAccion.
```

---

## 23 · Recorrido (lectura) de un vector (repetida)

Repetición idéntica de la página 21 (mismo pie, 19). No agrega contenido.

---

## 24 · Recorrido (lectura) de un vector (ampliación, repetida)

Repetición idéntica de la página 22 (mismo pie, 19). No agrega contenido.

---

## 25 · Recorrido con condición: MIENTRAS

*VARIANTE*

Cuando el corte del recorrido depende de una condición —no de un número fijo de vueltas— se usa MIENTRAS. Es la misma lógica que usa la Búsqueda por Centinela.

```
Accion MOSTRAR_HASTA_CENTINELA (arreglo [1..50] de entero) ES;
Ambiente
    i: entero;
Proceso
    i := 1;
    MIENTRAS (i<=50) Y (v[i]<>-1) HACER
        Escribir(v[i]);
        i := i+1;
    FIN_MIENTRAS;
FinAccion.
```

Diagrama del vector:

```
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ 12 │ 45 │  7 │ 88 │  3 │ -1 │    │    │
└────┴────┴────┴────┴────┴────┴────┴────┘
 └───── datos válidos ────┘ centinela sin usar
```

- `i` se inicializa en 1 antes del ciclo (MIENTRAS es pre-test).
- La condición combina dos chequeos: no pasarse del arreglo (`i<=50`) y no haber llegado al centinela (`v[i]<>-1`).
- `-1` marca el fin de los datos válidos cuando no se sabe de antemano cuántos elementos hay cargados.

> [!bug] Errata de la filmina
> - Igual que en la página 21: el parámetro no tiene nombre y el cuerpo usa `v`.
> - Punto dudoso: si las 50 posiciones tienen datos válidos (ningún `-1`), `i` llega a 51 y la condición evalúa `v[51]`, que es justo el error "Índice fuera de rango" de la página 31. Sólo se salva si `Y` corta la evaluación cuando `i<=50` ya es falso; la filmina no lo aclara.

---

## 26 · Recorrido con condición: MIENTRAS (ampliación del código)

Ampliación a pantalla completa del código de la página 25 (pie 20):

```
Accion MOSTRAR_HASTA_CENTINELA (arreglo [1..50] de entero) ES;
Ambiente
    i: entero;
Proceso
    i := 1;
    MIENTRAS (i<=50) Y (v[i]<>-1) HACER
        Escribir(v[i]);
        i := i+1;
    FIN_MIENTRAS;
FinAccion.
```

---

## 27 · Carga de una matriz

*OPERACIÓN: CARGA (2D)*

```
Accion CARGAR_MATRIZ ES;
Ambiente
    m: arreglo [1..10, 1..5] de real;
    i, j: entero;
Proceso
    PARA i:=1 HASTA 10 HACER
        PARA j:=1 HASTA 5 HACER
            Leer(m[i,j]);
        FIN_PARA;
    FIN_PARA;
FinAccion.
```

**Dos índices, dos ciclos**

- `i` (ciclo externo) recorre las filas.
- `j` (ciclo interno) recorre las columnas de esa fila.
- Por cada valor de `i`, `j` se completa por entero (1 a 5) antes de avanzar a la fila siguiente.

---

## 28 · Carga de una matriz (ampliación del código)

Ampliación a pantalla completa del código de la página 27 (pie 21):

```
Accion CARGAR_MATRIZ ES;
Ambiente
    m: arreglo [1..10, 1..5] de real;
    i, j: entero;
Proceso
    PARA i:=1 HASTA 10 HACER
        PARA j:=1 HASTA 5 HACER
            Leer(m[i,j]);
        FIN_PARA;
    FIN_PARA;
FinAccion.
```

---

## 29 · Recorrer una matriz: filas vs. columnas

*OPERACIÓN: RECORRIDO (2D)*

**Por filas (recorrido natural)**

```
PARA i:=1 HASTA 10 HACER
    PARA j:=1 HASTA 5 HACER
        Escribir(m[i,j]);
    FIN_PARA;
FIN_PARA;
```

*i externo (fila), j interno (columna): se completa cada fila antes de pasar a la siguiente.*

**Por columnas**

```
PARA j:=1 HASTA 5 HACER
    PARA i:=1 HASTA 10 HACER
        Escribir(m[i,j]);
    FIN_PARA;
FIN_PARA;
```

*j externo (columna), i interno (fila): simplemente se invierte cuál índice es el ciclo exterior.*

---

## 30 · Recorrer una matriz (ampliación del código)

Ampliación a pantalla completa de los dos bloques de la página 29 (pie 22):

```
PARA i:=1 HASTA 10 HACER
    PARA j:=1 HASTA 5 HACER
        Escribir(m[i,j]);
    FIN_PARA;
FIN_PARA;
```

```
PARA j:=1 HASTA 5 HACER
    PARA i:=1 HASTA 10 HACER
        Escribir(m[i,j]);
    FIN_PARA;
FIN_PARA;
```

---

## 31 · Errores comunes al trabajar con arreglos

*ANTES DE TERMINAR*

> [!warning] ! Índice fuera de rango
> Acceder a v[51] en un vector [1..50] es un error: no existe esa posición.

> [!warning] ! Confundir NTC con el último índice
> El NTC es la cantidad de elementos, no necesariamente el valor del último índice (si líminf ≠ 1).

> [!warning] ! No inicializar antes de leer
> Recorrer para mostrar un arreglo que nunca se cargó da valores indefinidos.

> [!warning] ! Invertir filas y columnas
> m[i,j] ≠ m[j,i]: el orden de los índices importa y no es intercambiable.

---

## 32 · Lo esencial de hoy (1 a 3)

*SÍNTESIS*

1. Un arreglo es una colección finita, homogénea y ordenada de elementos, en memoria interna.
2. Es estático: tamaño y tipo se fijan a priori y no cambian. No hay inserción ni eliminación.
3. Vector = 1 índice (arreglo unidimensional). Matriz = 2 índices (bidimensional).

---

## 33 · Lo esencial de hoy (4 y 5)

*SÍNTESIS* — continuación (mismo pie, 24).

4. Se declara con arreglo [límites] de tipo; el NTC se calcula a partir de esos límites.
5. Carga y recorrido usan PARA (vueltas fijas) o MIENTRAS (corte por condición, p. ej. centinela).

---

## 34 · Próxima clase: Búsqueda y Ordenamiento

*PRÓXIMA CLASE*

**Búsqueda y Ordenamiento**

Clase 2 tomará el recorrido que vimos hoy y lo convertirá en algoritmos de búsqueda secuencial y métodos de ordenamiento.

> *¿Preguntas sobre arreglos, vectores, matrices o las operaciones vistas hoy?*

---

## 🔗 Notas relacionadas

- [[4 — Arreglos (versión anterior)]] — la presentación anterior (Google Slides, 35 diapositivas)
- [[5 — Búsqueda y Ordenamiento]] — la Clase 2 que anuncia la página 34
- [[6 — Procesos Estadísticos]] — matrices aplicadas a informes estadísticos
- [[3 — Arreglos]] — los ejercicios de la Guía de Cátedra sobre este tema
- [[Arreglos]] — la página de teoría del sitio de la cátedra
- [[sintaxis-completa]] · [[plantillas]] — la notación oficial de pseudocódigo
- [[errores-y-trampas]]
