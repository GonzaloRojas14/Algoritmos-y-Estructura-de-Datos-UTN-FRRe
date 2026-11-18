---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 14
titulo_original: Complejidad algorítmica
archivo_original: 07_Complejidad_Algoritmica.pdf
diapositivas: 28
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - complejidad
---

# 14 — Complejidad Algorítmica

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 28 diapositivas de **Complejidad algorítmica** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[07_Complejidad_Algoritmica.pdf]] (carpeta `PDF originales/`).
> Las tablas y fórmulas se reconstruyeron en texto; el único gráfico recortado es el de crecimiento de los órdenes (diapositiva 20).

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

**Complejidad algorítmica**

¿Cómo medimos la eficiencia de un algoritmo?

*Recursos · Operaciones elementales · Mejor, peor y caso medio · Notación O*

---

## 2 · Objetivos de la clase

**OBJETIVOS DE LA CLASE**

### ¿Qué vamos a aprender hoy?

1. **Por qué medir un algoritmo**
   Un mismo problema admite varias soluciones: necesitamos un criterio objetivo para compararlas.
2. **Qué recursos consume**
   Memoria (complejidad espacial) y tiempo (complejidad temporal).
3. **Cómo contar el tiempo**
   Operaciones elementales (OE) y la función T(n), en el mejor, peor y caso medio.
4. **Cómo clasificarlo**
   Comportamiento asintótico, notación O y los órdenes de complejidad más comunes.

---

## 3 · Punto de partida

**PUNTO DE PARTIDA**

### Un problema, varias soluciones

**Buscar un valor en un arreglo ordenado de n elementos:**

| Búsqueda secuencial | Búsqueda binaria |
|---|---|
| Recorre el arreglo desde la posición 1, de a un elemento, hasta encontrarlo o llegar al final. | Compara con el elemento del medio y descarta la mitad que no puede contenerlo; repite sobre la otra mitad. |

> [!question]
> Las dos son correctas. **¿Cuál es más eficiente?** Para responder hay que poder medirlas.

---

## 4 · Concepto central

**CONCEPTO CENTRAL**

### ¿Qué es un algoritmo eficiente?

> [!important] Definición
> Un algoritmo es más **eficiente** que otro cuando **consume menos recursos**: tiempo y espacio de memoria necesarios para ejecutarlo.

**Criterios para evaluar su comportamiento**

| Simplicidad | Uso eficiente de los recursos |
|---|---|
| La sencillez facilita su verificación, el estudio de su eficiencia y su mantenimiento. Se valora el código legible frente a alternativas más crípticas. | Memoria → complejidad espacial.<br>Tiempo → complejidad temporal.<br>Es lo que vamos a medir hoy. |

---

## 5 · Recurso 1 · Memoria

**RECURSO 1 · MEMORIA**

### Complejidad espacial

Es la cantidad de espacio requerido para ejecutar el algoritmo.

| MEMORIA ESTÁTICA | MEMORIA DINÁMICA |
|---|---|
| • Se suma lo que ocupan las variables declaradas en el Ambiente.<br>• Se conoce antes de ejecutar.<br>• Ejemplo: arreglos, registros, simples. | • Depende de cada ejecución del algoritmo.<br>• Se pide y libera durante el proceso: NUEVO(p) / DISPONER(p).<br>• Ejemplo: listas y árboles. |

```
Ambiente
   V: ARREGLO[1..100] de entero;  i, suma: entero;
```

**100 + 2 = 102 enteros**

---

## 6 · Recurso 2 · Tiempo

**RECURSO 2 · TIEMPO**

### Complejidad temporal

> [!important] Tiempo de ejecución para una entrada de tamaño n
> **`T(n)`**

*n = tamaño de la entrada (ej.: la dimensión del arreglo a ordenar).*

**¿De qué depende el tiempo?**

1. **Los datos de entrada**
2. La calidad del código que genera el compilador
3. La arquitectura y rapidez del procesador (CISC, RISC)
4. **La complejidad intrínseca del algoritmo**

> [!tip]
> **Nos interesan el 1 y el 4:** los otros dos dependen de la máquina, no del algoritmo.

---

## 7 · Dos formas de estudiarlo

**DOS FORMAS DE ESTUDIARLO**

### Estudio a priori y a posteriori

| A PRIORI — *Teórico* | A POSTERIORI — *Empírico* |
|---|---|
| • Obtiene una función que acota el tiempo de ejecución.<br>• No hace falta ejecutar el algoritmo.<br>• Independiente de la computadora. | • Mide el tiempo real de ejecución.<br>• Para un conjunto de datos concreto.<br>• En una computadora concreta. |

> [!important]
> No existe una computadora estándar: **la unidad de tiempo no puede ser concreta** (segundos). Medimos en operaciones.

---

## 8 · Principio de invarianza

**PRINCIPIO DE INVARIANZA**

### Cambiar de máquina no cambia la forma

Dado un algoritmo y dos implementaciones I1 e I2, que tardan T1(n) y T2(n):

> [!important] Principio de invarianza
> existen c > 0 y n0 tales que, para todo n ≥ n0
>
> **`T1(n) ≤ c · T2(n)`**

| En palabras | Consecuencia |
|---|---|
| El tiempo de dos implementaciones distintas de un mismo algoritmo no difiere más que en una constante multiplicativa. | Una máquina el doble de rápida divide el tiempo por 2, pero no cambia cómo crece T(n) cuando crece n. |

---

## 9 · Estudio de la complejidad temporal

**ESTUDIO DE LA COMPLEJIDAD TEMPORAL**

### Mejor caso, peor caso y caso medio

| CASO MEJOR | CASO PEOR | CASO MEDIO |
|---|---|---|
| La traza que ejecuta el menor número posible de instrucciones. | La traza que ejecuta el mayor número posible de instrucciones. | El número esperado de instrucciones: promedio de todas las trazas posibles, según la probabilidad de cada una. |

*Traza = secuencia de sentencias que efectivamente se ejecutan para una entrada.*

> [!warning] Error común
> el mejor caso no es "cuando n = 1". Los tres casos se calculan para un mismo tamaño de entrada n.

---

## 10 · La unidad de medida

**LA UNIDAD DE MEDIDA**

### Operaciones elementales (OE)

> [!important] Definición
> Una OE es una operación que se realiza en un tiempo **acotado por una constante**. Cada una cuenta **1 OE**.

| Grupo | Operaciones |
|---|---|
| Aritméticas básicas | `+`  `−`  `*`  `/`  `DIV`  `MOD` |
| Asignación | `:=` |
| Comparaciones y lógicas | `<`  `>`  `=`  `<>`  `Y`  `O`  `NO` |
| Acceso a arreglos | `V[i]`  `M[i, j]` |
| Llamada y retorno | invocar una función o procedimiento |

> **`T(n) = cantidad de OE`**

---

## 11 · Práctica rápida

**PRÁCTICA RÁPIDA**

### Contando operaciones elementales

| Sentencia | OE | ¿Cuáles? |
|---|:-:|---|
| `A := A + 1` | **2** | `:=`  `+` |
| `B := A * 5 - V[2 * 2]` | **5** | `:=`  `*`  `−`  `[ ]`  `*` |
| `B := B + Suma(A, B + 2)` | **4** | `:=`  `+`  `llamada`  `+` |
| `(A <> B) O (C + 1 = X)` | **4** | `<>`  `O`  `+`  `=` |

> [!warning] Ojo
> la llamada a una función cuenta 1 OE; lo que hace la función por dentro se cuenta aparte.

---

## 12 · Analizando un caso

**ANALIZANDO UN CASO**

### La función Buscar

```
Funcion Buscar(c: entero): entero;
Ambiente
    j: entero;
Proceso
    j := 1;                                    {1}
    MIENTRAS (A[j] <> c) Y (j < n) HACER       {2}
        j := j + 1;                            {3}
    FIN_MIENTRAS;
    SI A[j] = c ENTONCES                       {4}
        Buscar := j;                           {5}
    CONTRARIO
        Buscar := 0;                           {6}
    FIN_SI;
Fin;
```

| Línea | OE | Detalle |
|:-:|:-:|---|
| 1 | 1 | `:=` |
| 2 | 4 | `<>`  `[]`  `<`  `Y` |
| 3 | 2 | `:=`  `+` |
| 4 | 2 | `=`  `[ ]` |
| 5 | 1 | `:=` |
| 6 | 1 | `:=` |

*A: ARREGLO[1..n] de entero, declarado en el Ambiente de la Acción.*

> [!bug] Errata de la filmina
> `n` no está declarada ni en la función ni como parámetro; la aclaración sólo dice que `A` está en el Ambiente de la Acción (se entiende que `n` también es global).

---

## 13 · Buscar · Caso mejor

**BUSCAR · CASO MEJOR**

### c está en la primera posición

**Costo por línea** (resaltadas en la filmina las líneas que se ejecutan: 1, 2, 4 y 5)

| | Sentencia | OE | |
|:-:|---|:-:|---|
| **1** | `j := 1` | 1 OE | |
| **2** | `MIENTRAS (A[j] <> c) Y (j < n)` | 4 OE | **½ → 2 OE** |
| 3 | `j := j + 1` | 2 OE | *(no se ejecuta)* |
| **4** | `SI A[j] = c` | 2 OE | |
| **5** | `Buscar := j` | 1 OE | |
| 6 | `Buscar := 0` | 1 OE | *(no se ejecuta)* |

**Buscar c = 7**

| **7** | 12 | 15 | 21 | 30 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | 2 | 3 | 4 | 5 |

> [!info] Cortocircuito
> A[1] <> c es falso, así que el Y ya es falso: no se evalúa j < n.

```
T(n) = 1 + 2 + 2 + 1
T(n) = 6
```

*Constante: no depende de n.*

---

## 14 · Buscar · Caso peor

**BUSCAR · CASO PEOR**

### c no está (o está al final)

**Costo por línea** (resaltadas en la filmina las líneas que se ejecutan: 1, 2, 3, 4 y 6)

| | Sentencia | OE | Veces |
|:-:|---|:-:|---|
| **1** | `j := 1` | 1 OE | |
| **2** | `MIENTRAS (A[j] <> c) Y (j < n)` | 4 OE | **n veces** |
| **3** | `j := j + 1` | 2 OE | **n−1 veces** |
| **4** | `SI A[j] = c` | 2 OE | |
| 5 | `Buscar := j` | 1 OE | *(no se ejecuta)* |
| **6** | `Buscar := 0` | 1 OE | |

**Cada vuelta = línea 2 + línea 3 = 6 OE**

```
 n−1
  Σ  (4 + 2) = 6(n−1)
 i=1

T(n) = 1 + 6(n−1) + 4+2+1
                    ↑ salida del bucle
```

> [!important] Crece linealmente con n
> **`T(n) = 6n + 2`**

> [!bug] Errata de la filmina
> El título junta dos casos que no cuestan lo mismo. El cálculo (última evaluación del MIENTRAS de 4 OE y línea 6) corresponde a **c no está**. Si **c está al final**, con el mismo cortocircuito que se usa en el caso mejor la última evaluación de la condición cuesta 2 OE (A[n] <> c es falso) y se ejecuta la línea 5 en vez de la 6: T(n) = 1 + 6(n−1) + 2 + 2 + 1 = 6n. El orden es el mismo, O(n), pero la cuenta 6n + 2 vale sólo para "c no está".

---

## 15 · Buscar · Caso medio

**BUSCAR · CASO MEDIO**

### En promedio, la mitad del recorrido

El bucle puede iterar 0, 1, …, n−1 veces, cada una con probabilidad 1/n:

```
 n−1                                (n−1)/2
  Σ  i · 1/n = (n−1)/2                 Σ  6 = 3(n−1)
 i=0                                  i=1

 iteraciones en promedio            OE de todas esas vueltas
```

```
T(n) = 1 + 3(n−1) + 2 + 2 + 1
                    ↑ salida al encontrarlo: ½ línea 2
```

> [!important] Casi la mitad del caso peor
> **`T(n) = 3n + 3`**

---

## 16 · Comparando los tres casos

**COMPARANDO LOS TRES CASOS**

### Buscar: mejor, medio y peor

| CASO MEJOR | CASO MEDIO | CASO PEOR |
|:-:|:-:|:-:|
| **6** | **3n + 3** | **6n + 2** |
| constante | = 6 · (n + 1) / 2 | = 6 · (n + 1/3) |

**Promedio de mejor y peor:** `[6 + (6n + 2)] / 2 = 3n + 4  ≈  caso medio.`

> [!tip] Por el principio de invarianza
> los valores son múltiplos de 6 y difieren sólo en constantes. Lo que importa no es la constante sino cómo crece T(n) con n: medio y peor crecen como n.

---

## 17 · Asíntotas

**ASÍNTOTAS**

### ¿Qué pasa cuando n es muy grande?

Para n grande, los términos chicos y las constantes dejan de importar:

| n | 6n + 2 | 6n | peso del +2 |
|:-:|:-:|:-:|:-:|
| 10 | 62 | 60 | 3,2 % |
| 1.000 | 6.002 | 6.000 | 0,03 % |
| 1.000.000 | 6.000.002 | 6.000.000 | ≈ 0 % |

> [!important] Comportamiento asintótico
> Estudiar el algoritmo cuando n tiende a infinito. Las funciones con el mismo comportamiento para n grande forman una familia: un orden de complejidad.

Cada familia se designa con **`O( )`** y se representa con la más sencilla: 6n + 2 → **`O(n)`**

---

## 18 · Notación O

**NOTACIÓN O**

### Una cota superior para T(n)

> [!important] Definición
> T(n) es O(f(n)) si existen c > 0 y n0 tales que, para todo n ≥ n0:
>
> **`T(n) ≤ c · f(n)`**

**Ejemplo: el caso peor de Buscar**

```
6n + 2   ≤   6n + n   =   7n
                  para n ≥ 2

c = 7    n0 = 2    →    O(n)
```

**Regla práctica**

| T(n) | | Orden |
|:-:|:-:|:-:|
| 3n + 3 | → | O(n) |
| 2n² + 5n + 1 | → | O(n²) |
| 6 | → | O(1) |

*Término que más crece, sin su constante.*

---

## 19 · Órdenes de complejidad

**ÓRDENES DE COMPLEJIDAD**

### Las familias más habituales

| Orden | Nombre |
|:-:|---|
| O(1) | Constante |
| O(log n) | Logarítmico |
| O(n) | Lineal |
| O(n log n) | Cuasi-lineal |
| O(n²) | Cuadrático |
| O(n³) | Cúbico |
| O(nᵃ) | Polinómico (a > 3) |
| O(2ⁿ) | Exponencial |
| O(n!) | Factorial |

*(Una flecha al costado de la tabla va de **más eficiente** (arriba) a **menos eficiente** (abajo).)*

> [!info] Jerarquía
> Cada orden es subconjunto de los siguientes: O(n) ⊂ O(n log n) ⊂ O(n²)…

> [!info] Representante
> De cada familia elegimos la función f(n) más sencilla.

---

## 20 · Visualizando el crecimiento

**VISUALIZANDO EL CRECIMIENTO**

### ¿Cómo crece cada orden con n?

![[complej-grafico-crecimiento-ordenes.png]]

*Gráfico de operaciones (eje vertical, 0 a 120) en función de n (eje horizontal, 0 a 16) para O(log n), O(n), O(n log n), O(n²) y O(2ⁿ): 2ⁿ y n² se salen del gráfico antes de n = 8 y n = 12, mientras n log n llega a 64, n a 16 y log n a 4 en n = 16.*

> [!tip] Fijate
> con n = 16, log n vale 4 y n vale 16, pero n² ya vale 256 y 2ⁿ vale 65.536.

---

## 21 · ¿Cuánto es eso en tiempo?

**¿CUÁNTO ES ESO EN TIEMPO?**

### Si cada operación tardara 1 microsegundo

| Orden | n = 10 | n = 100 | n = 1.000 |
|:-:|:-:|:-:|:-:|
| O(log n) | 3 µs | 7 µs | 10 µs |
| O(n) | 10 µs | 100 µs | 1 ms |
| O(n log n) | 33 µs | 664 µs | 10 ms |
| O(n²) | 100 µs | 10 ms | 1 s |
| O(n³) | 1 ms | **1 s** | **17 min** |
| O(2ⁿ) | 1 ms | **4·10¹⁶ años** | **inviable** |

> [!warning] Más rápido no alcanza
> Una máquina 100 veces más rápida no salva a un algoritmo exponencial.

> [!tip] Conclusión
> elegir un algoritmo de mejor orden gana mucho más que optimizar el código.

---

## 22 · Dónde aparece cada orden

**DÓNDE APARECE CADA ORDEN**

### Ejemplos que ya conocemos

| Orden | Cuándo aparece | Ejemplo |
|:-:|---|---|
| O(1) | Instrucciones que se ejecutan una sola vez. | Ej.: Acceder a V[i] |
| O(log n) | Se descarta la mitad del problema en cada paso. | Ej.: Búsqueda binaria |
| O(n) | Un bucle simple con cuerpo constante. | Ej.: Búsqueda secuencial |
| O(n log n) | Divide y vencerás. Si n se duplica, algo más que el doble. | Ej.: Quicksort (caso medio) |
| O(n²) | Bucles doblemente anidados. Si n se duplica, ×4. | Ej.: Burbuja, selección |
| O(2ⁿ) | Recursión con dos o más llamadas internas. | Ej.: Fibonacci recursivo |

---

## 23 · Cómo calcularlo

**CÓMO CALCULARLO**

### Reglas prácticas por estructura de control

| | Estructura | Forma | Costo |
|:-:|---|---|---|
| 1 | Secuencia | `S1;  S2` | T(S1) + T(S2): domina la mayor |
| 2 | Selección | `SI cond ENTONCES S1 CONTRARIO S2` | T(cond) + máx(T(S1), T(S2)) |
| 3 | Repetición | `MIENTRAS / PARA … cuerpo` | vueltas × T(cuerpo) → Σ |
| 4 | Llamada | `Buscar(c)` | T de la subacción invocada |

> [!tip] Para el orden
> las constantes no importan; sí importa cuántas veces se repite cada bucle.

---

## 24 · Herramientas

**HERRAMIENTAS**

### Sumatorias útiles

| | Nombre | Fórmula |
|:-:|---|---|
| 1 | Suma de sumas | `Σ (a + b) = Σ a + Σ b` |
| 2 | Cuerpo constante | `Σ a  (i = k..n) = (n − k + 1) · a` |
| 3 | Constante afuera | `Σ a·i = a · Σ i` |
| **4** | **Suma de i** | **`Σ i  (i = 1..n) = n(n + 1) / 2`** |
| 5 | Índice desde m | `Σ i (i = m..n) = Σ i (1..n) − Σ i (1..m−1)` |
| 6 | Suma de i² | `Σ i² (i = 1..n) = n(n + 1)(2n + 1) / 6` |
| 7 | Suma de i³ | `Σ i³ (i = 1..n) = [n(n + 1) / 2]²` |

*La 4 es la que más vamos a usar: aparece en los bucles anidados "triangulares".*

---

## 25 · Aplicando las reglas: bucles anidados

**APLICANDO LAS REGLAS**

### Bucles anidados

**Recorrer una matriz n × n**

```
PARA i := 1 HASTA n HACER
   PARA j := 1 HASTA n HACER
      M[i, j] := 0;
   FIN_PARA;
FIN_PARA;
```

`n vueltas × n vueltas = n · n` → **O(n²)**

**Triángulo: j llega hasta i**

```
PARA i := 1 HASTA n HACER
   PARA j := 1 HASTA i HACER
      M[i, j] := 0;
   FIN_PARA;
FIN_PARA;
```

`1 + 2 + … + n = n(n + 1)/2` → **O(n²)**

*Aunque haga la mitad de trabajo, el orden es el mismo: la constante ½ no cuenta.*

---

## 26 · Aplicando las reglas: un bucle que divide a la mitad

**APLICANDO LAS REGLAS**

### Un bucle que divide a la mitad

```
k := n;
MIENTRAS k > 1 HACER
   k := k DIV 2;
FIN_MIENTRAS;
```

**Con n = 16:**

```
[16] → [8] → [4] → [2] → [1]
```

**4 vueltas = log₂ 16**

| n | vueltas |
|:-:|:-:|
| 16 | 4 |
| 1.024 | 10 |
| 1.048.576 | 20 |

> [!important]
> Duplicar n agrega **una sola vuelta**. Por eso la búsqueda binaria es **O(log n)**

---

## 27 · Para llevarse: conclusión

**PARA LLEVARSE**

### Conclusión

1. Medimos la eficiencia por los recursos que consume: memoria y tiempo.
2. El tiempo se mide en operaciones elementales, T(n), independiente de la máquina.
3. Se analizan tres casos para un mismo n: mejor, peor y medio.
4. Por la invarianza, importa cómo crece T(n), no sus constantes: notación O.
5. Al programar: una solución correcta, simple y con la estructura de datos adecuada.

---

## 28 · Para practicar: ejercicios

**PARA PRACTICAR**

### Ejercicios

| 1 · Acotar | 2 · Sumar un arreglo | 3 · Bucle anidado |
|---|---|---|
| Demostrar que T(n) = 2n² + 3 es O(n²): encontrar c y n0. | Función que suma los n elementos de A con un PARA. Calcular T(n) en OE y su orden. | PARA i := 1 HASTA n / PARA j := i HASTA n. ¿Cuántas veces se ejecuta el cuerpo? |
| *Pista: compará con 3n²* | *Pista: ¿hay mejor y peor caso?* | *Pista: sumatoria 4* |

*Para cada uno: identificar n, contar o acotar, y quedarse con el término que más crece.*
