---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 1
titulo_original: TEMA I — Introducción (+ TEMA II — Acciones)
archivo_original: TEMA 1_2 - INTRODUCCIÓN.pdf
diapositivas: 71
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - introduccion
  - algoritmos
  - datos
  - acciones
  - asignacion
  - operadores
---

# 1-2 — Introducción

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 71 diapositivas de **TEMA I — Introducción** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[TEMA 1_2 - INTRODUCCIÓN.pdf]] (carpeta `PDF originales/`).
> El PDF junta dos presentaciones: **TEMA I — Introducción** (diapositivas 1–37: algoritmos, características, elementos, datos, variables y constantes) y **TEMA II — Acciones** (diapositivas 38–71: tipos de acciones, asignación, entrada/salida y operadores).

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

**TEMA I**
**Introducción**

ALGORITMOS Y ESTRUCTURAS DE DATOS 2026 - ISI UTN FRRe

| Conceptos | Elementos | Características | Algo más! |
|---|---|---|---|

---

## 2 · QUÉ VAMOS A VER HOY?

| | |
|---|---|
| **01 — INTRO** *(resaltado)*<br>Empecemos a ver de qué va esto por fa | **02 — CARACTERÍSTICAS**<br>De los algoritmos que vamos a diseñar |
| **03 — ELEMENTOS**<br>Que componen a todos los algoritmos | **04 — DATOS**<br>Clasificación de datos que vamos a manejar |

---

## 3 · 01 INTRODUCCIÓN

**01**
**INTRODUCCIÓN**
A los ALGORITMOS Y ESTRUCTURAS DE DATOS

---

## 4 · ALAN TURING

**ALAN TURING**

Es considerado uno de los padres de la ciencia de la computación y precursor de la informática moderna.

*(foto de Alan Turing, afiche de la película "El Código Enigma" y captura del tráiler)*

CODIGO ENIGMA TRAILER

"The imitation Game" Una película sobre Alan Turing con Benedict Cumberbatch

---

## 5 · GRACE MURRAY HOPPER

**GRACE MURRAY HOPPER**

Fue la creadora del primer compilador de ordenadores en 1952. Asimismo, en 1959, inventó el COBOL (Common Business Oriented Language) el primer lenguaje de programación dedicado a la administración.

*(foto de Grace Murray Hopper)*

---

## 6 · DE DÓNDE VIENE TODO ESTO

**DE DÓNDE VIENE TODO ESTO**

Veamos cómo surgen los algoritmos y su importancia hoy!

---

## 7 · The Map of Mathematics

![[intro-mapa-matematicas.png]]

Infografía *The Map of Mathematics* (Dominic Walliman, 2017) con dos zonas ampliadas y recuadradas en amarillo: **THEORY OF COMPUTATION** (cinta `00011B0`, *P≠NP?*, *COMPLEXITY THEORY*) y **COMPUTER SCIENCE** (*TURING MACHINE*), unidas por una línea a la zona *Foundations / Theory of Computation* del mapa.

---

## 8 · Map of Computer Science

![[intro-mapa-ciencias-computacion.png]]

Infografía *Map of Computer Science* (Dominic Walliman, 2017) con tres zonas ampliadas y recuadradas en amarillo:
- **ALGORITHMS**: `BUBBLESORT(A)` — *1: GO FROM LEFT TO RIGHT. 2: COMPARE EACH PAIR. 3: IF LEFT ONE HIGHER, SWITCH. 4: DO UNTIL NO MORE SWITCHES.* · BUBBLE SORT O(n²) · MERGE SORT O(n log n) · ANALYSIS OF ALGORITHMS · ALGORITHMIC COMPLEXITY.
- **DATA STRUCTURES**: TREE, LINKED LIST, LIST, GRAPH, STACK, HASHING · FORMAL METHODS.
- **SOFTWARE AND PROGRAMMING LANGUAGES**: Python, PHP, Swift, Java, C++, C, JavaScript, Perl, SQL, C#, Assembly → web apps, browser, applications, operating system, BIOS, silicon, machine code, compilers.

---

## 9 · Relación

```
            ┌─────────────────────────────┐
     ▲      │         APLICACIÓN          │   ▲  S
     │      │         ALGORITMO           │   │  O
     │      │  LENGUAJE DE PROGRAMACIÓN   │   │  F
     │      │   LENGUAJE ENSAMBLADOR      │   │  T W A R E
 +ABSTRACCIÒN│     LENGUAJE DE MÁQUINA     │   ▼
     │      ├─────────────────────────────┤   ▲  H
     │      │         PROCESADOR          │   │  A
     │      │      MICROARQUITECTURA      │   │  R D W A R E
     │      │          REGISTROS          │   │
            │        TRANSISTORES….       │   ▼
            └─────────────────────────────┘
```

Pila de niveles: de abajo hacia arriba aumenta la abstracción (flecha **+ABSTRACCIÒN**). Las cinco capas superiores (APLICACIÓN → LENGUAJE DE MÁQUINA) son **SOFTWARE**; las cuatro inferiores (PROCESADOR → TRANSISTORES….) son **HARDWARE**.

---

## 10 · Relación

```
    PROBLEMA                          COMPUTADORA
       ▲                                   │
       │ resuelve                          │ ejecuta
       │                                   ▼
    ALGORITMO  ◄────── implementa ──────  PROGRAMA
       ▲                                   ▲
       │ expresar                          │ programar
       │                                   │ codificar
       │                                   │ implementar
  PSEUDOCÓDIGO                          LENGUAJE
```

---

## 11 · ¿Vamos entendiendo todo?

**¿Vamos entendiendo todo?**

*(imagen de Homero Simpson con la mano en la cara)*

---

## 12 · QUÉ ES UN ALGORITMO

> [!important] Definición — QUÉ ES UN ALGORITMO
> una **secuencia finita de instrucciones**, **reglas o pasos** que describen de modo preciso las **operaciones** que una computadora debe realizar para ejecutar una **tarea determinada** en un **tiempo finito**.

---

## 13 · QUÉ VAMOS A VER HOY?

| | |
|---|---|
| **01 — INTRO**<br>Empecemos a ver de qué va esto por fa | **02 — CARACTERÍSTICAS** *(resaltado)*<br>De los algoritmos que vamos a diseñar |
| **03 — ELEMENTOS**<br>Que componen a todos los algoritmos | **04 — DATOS**<br>Clasificación de datos que vamos a manejar |

---

## 14 · 02 CARACTERÍSTICAS

**02**
**CARACTERÍSTICAS**
DE TODOS LOS ALGORITMOS

---

## 15 · Pasos para crear un algoritmo

```
PROBLEMA ──► ENTRADAS ──► PROCESOS ──► SALIDAS
```

1. **PROBLEMA** — Entender el problema y la necesidad de solución es imprescindible para avanzar.
2. **ENTRADAS** — Definir los datos de entrada con los que se va a trabajar para lograr el resultado.
3. **PROCESOS** — Plantear los procesos necesarios para pasar de los datos de entrada a los datos de salida
4. **SALIDAS** — Validar el algoritmo

---

## 16 · Características del ALGORITMO

| | |
|---|---|
| **PRECISO**<br>Cada paso debe estar claramente definido y sin ambigüedades | **DEFINIDO**<br>Para una misma entrada, siempre produce la misma salida. |
| **CORRECTO**<br>Debe resolver correctamente el problema para el que fue diseñado. | **FINITO**<br>Debe terminar en algún momento. |

---

## 17 · Ejemplos de lo que no debemos hacer

**Ejemplo 1: Algoritmo para hacer un té (IMPRECISO)**

1. Poner agua en un recipiente.
2. Calentar el agua.
3. Agregar té.
4. Servir en una taza.

> [!warning] ¿Por qué es impreciso?
> - **"Poner agua en un recipiente"** → ¿Cuánta agua? ¿Qué tipo de recipiente?
> - **"Calentar el agua"** → ¿A qué temperatura? ¿Cómo se calienta?
> - **"Agregar té"** → ¿Bolsa de té o en hojas? ¿Cuánto té?

---

## 18 · Ejemplos de lo que no debemos hacer

**Ejemplo 1: Algoritmo para sumar dos números (INDEFINIDO)**

1. Pedir al usuario dos números.
2. Sumar los valores ingresados.
3. Si el resultado es "grande", mostrar un mensaje especial.
4. Mostrar el resultado.

> [!warning] ¿Por qué es indefinido?
> - **"Si el resultado es 'grande'"** → ¿Qué significa "grande"? ¿Mayor que 100, 1000, 10⁶?
> - Dependiendo de cómo se interprete "grande", el algoritmo puede dar diferentes resultados en distintas ejecuciones con la misma entrada.

> [!bug] Errata de la filmina
> El título dice "**Ejemplo 1**" igual que la diapositiva anterior; por el orden sería el Ejemplo 2.

---

## 19 · ¿Y ahora cómo vamos?

**¿Y ahora cómo vamos?**

*(imagen de Homero Simpson leyendo el "Nuclear Reactor Safety Manual")*

---

## 20 · QUÉ VAMOS A VER HOY?

| | |
|---|---|
| **01 — INTRO**<br>Empecemos a ver de qué va esto por fa | **02 — CARACTERÍSTICAS**<br>De los algoritmos que vamos a diseñar |
| **03 — ELEMENTOS** *(resaltado)*<br>Que componen a todos los algoritmos | **04 — DATOS**<br>Clasificación de datos que vamos a manejar |

---

## 21 · 03 ELEMENTOS

**03**
**ELEMENTOS**
QUE COMPONEN A TODOS LOS ALGORITMOS

---

## 22 · Siempre recuerda….LOS SISTEMAS

> [!important] Definición
> Un **sistema** es un conjunto de **elementos interrelacionados** que trabajan en conjunto para cumplir un **objetivo** específico, operando bajo ciertas reglas y principios dentro de un entorno determinado.

```
                         Entorno
             ┌──────────────────────────────┐
┌─────────────┐      ┌──────────────────┐      ┌─────────────┐
│  Entradas   │      │     Sistema      │      │   Salidas   │
│             │      │  Transformación  │      │             │
│  Energía    │ ───► │     Procesos     │ ───► │  Energía    │
│  Materia    │      │ que convierten   │      │  Materia    │
│  Información│      │ las entradas en  │      │  Información│
└─────────────┘      │     salidas      │      └─────────────┘
       ▲             └──────────────────┘             │
       │                   Entorno                    │
       └──────────────── Realimentación ◄─────────────┘
```

---

## 23 · Los elementos son

| DATOS | ACCIONES | OPERADORES |
|---|---|---|
| De entrada y de salida | Para transformar las entradas y obtener salidas | Para manipular los datos |

---

## 24 · Herramienta de diseño: PSEUDOCÓDIGO

> [!important] Definición
> El **pseudocódigo** es una forma de **representar** el algoritmo utilizando una combinación de lenguaje sencillo y natural y elementos del **algoritmo**.

**¿Qué quiero Hacer?** ⇒ **Lo escribo en Pseudocódigo** ⇒ **Escribo el Programa en mi lenguaje de Programación**

Ejemplo (captura de editor):

```
ACCION Enlazada ES
AMBIENTE
  S: Secuencia de caracter
  v: caracter
  cont: entero
  Subaccion Tratar_caracter Es
     cantcar:=cantcar + 1
     Si V = "0" entonces
       cont:=cont+1
     FinSi
  FinSubaccion
PROCESO
  ARR(S)
  AVZ(S,v)
  cont:=0
  Mientras NFDS(S) hacer
    Mientras V = "" hacer
      AVZ(S,v)
    FinMientras
    cantcar:=0
    Mientras V <> "" y cantcar < 4 y NFDS(S) hacer
       Tratar_caracter
       AVZ(S,v)
    FinMientras
  FinMientras
  Esc("La cantidad de caracteres 0 encontrados en
       la secuencia es de=", cont)
FinACCION
```

> [!bug] Errata de la filmina
> - `cantcar` se usa (`cantcar:=cantcar + 1`, `cantcar:=0`, `cantcar < 4`) pero no está declarada en el AMBIENTE.
> - Se compara el carácter con `""` (cadena vacía); por el contexto (saltear separadores entre palabras) probablemente se quiso comparar con el blanco `" "`.
> - El `Mientras V = "" hacer AVZ(S,v)` interno no controla `NFDS(S)`, así que si la secuencia termina en blancos avanza más allá del final.

---

## 25 · Partes del Algoritmo

| Parte | Qué contiene |
|---|---|
| **NOMBRE** | • Describe el nombre de la acción principal |
| **AMBIENTE** | • Se definen datos de entrada y de salida<br>• Se definen subacciones |
| **PROCESO** | • Se ejecutan las acciones para manipular datos |

```
ACCION Ventas ES
AMBIENTE
  cant, precio, total: numérico
  nom: alfanumérico
  dscto = 0.10
PROCESO
  Escribir("Ingrese nombre de producto")
  Leer(nom)
  Escribir("Ingrese cantidad a vender")
  Leer(cant)
  Escribir("Ingrese pcio. unitario en $")
  Leer(precio)
  Si cant > 100 entonces
    total:= (cant * precio) - (cant * precio * dscto)
  contrario
    total:= (cant * precio)
  Fin_Si
  Escribir("TOTAL ACTUALIZADO>$ ", total)
FIN_ACCION
```

---

## 26 · Volvamos a los DATOS

> [!important] Definición
> El **dato** se refiere a la representación simbólica de una entidad, por ejemplo *letras del alfabeto, números, puntos, dibujos*, etc.

*(mapa del mundo con el número* **8.166.959.732** *)*

---

## 27 · Entonces, los DATOS

> [!warning] Entonces, los DATOS
> Por sí solos, **no tienen la capacidad de transmitir ningún mensaje** ni mucho menos afecta a quien recibe.
> Pero si **se procesan apropiadamente**, los datos proveen **información** importante ayudando en la toma de decisiones.

---

## 28 · QUÉ VAMOS A VER HOY?

| | |
|---|---|
| **01 — INTRO**<br>Empecemos a ver de qué va esto por fa | **02 — CARACTERÍSTICAS**<br>De los algoritmos que vamos a diseñar |
| **03 — ELEMENTOS**<br>Que componen a todos los algoritmos | **04 — DATOS** *(resaltado)*<br>Clasificación de datos que vamos a manejar |

---

## 29 · 04 DATOS

**04**
**DATOS**
UNA PRIMERA CLASIFICACIÓN

---

## 30 · Clasificación de los datos

```
                    TIPOS DE DATOS
                          │
           ┌──────────────┴──────────────┐
        SIMPLES                    ESTRUCTURADOS
           │
   ┌───────┼──────────────┐
NUMÉRICOS  ALFANUMÉRICOS  BOOLEANOS
```

---

## 31 · Datos SIMPLES

| Numéricos | Alfanuméricos | Lógicos |
|---|---|---|
| Son aquéllos que representan una **cantidad o valor** determinado.<br>Por ejemplo *edad, antigüedad, salario* | Son los datos que representan **información textual**. No se pueden operar<br>Por ejemplo *nombre, descripción, apellido* | También se le denomina **Booleano**, es aquél dato que **solo puede tomar uno de dos valores**<br>Por ejemplo *un sensor, un semáforo peatonal….* |

---

## 32 · Datos SIMPLES

*(foto del robot Eilik)*

Ejemplo de uso de sensor en el robot Eilik

---

## 33 · ¿Dónde se guardan los datos?

**¿Dónde se guardan los datos?**

*(imagen de Homero Simpson festejando)*

---

## 34 · Los datos se almacenan en…

| | |
|---|---|
| **VARIABLES**<br>Representan una **dirección de memoria** en donde se almacena un dato, y su **contenido puede variar** en el desarrollo del algoritmo. | Por ejemplo *si estoy realizando el control de la cantidad de mensajes de wsp que recibe una persona, ese valor irá variando en el tiempo* |
| **CONSTANTES**<br>Representan una **dirección de memoria** en donde se almacena un dato, **cuyo contenido no puede variar** en el desarrollo del algoritmo. | Por ejemplo *quiero calcular cuánto vendí de un producto especial en una tienda online, que ofrece un descuento del 10% en casos puntuales. Ese descuento no varía, es una constante* |

---

## 35 · Variables VS Constantes

```python
# Variable: su valor puede cambiar
edad = 20
print(edad)  # Muestra: 20
edad = 25
print(edad)  # Muestra: 25

# Constante: se usa convención en mayúsculas (pero Python no impide modificarla)
PI = 3.1416
print(PI)  # Muestra: 3.1416
```

*(logo de Python)*

Las **variables y constantes** son esenciales en la programación.

En Python, las variables almacenan referencias a objetos en memoria y pueden cambiar, mientras que las constantes, aunque no son estrictas, se manejan por convención con nombres en mayúsculas.

---

## 36 · Actividad N° 1

1) Luego de la clase de hoy repasamos el contenido
2) De forma individual, ayudate de la IA que uses diariamente, y debes pensar qué datos podrías usar como variables y como constantes en un escenario definido
3) ¿Te parece correcto lo que te devuelve la IA? ¿Cuántas veces cambiaste el prompt?
4) Publicar tu respuesta en el Foro habilitado a tal fin
5) Las respuestas se compartirán la próxima clase

---

## 37 · Variables y Constantes

Ejemplos de respuestas (capturas):

> Escenario: Quiero tener mi entrada para mirar un partido de fútbol antes de llegar al estadio.
>
> Pasos:
> 1. Revisar si hay entradas disponibles en línea o en boletería.
> 2. Elegir en que parte del estadio quiero estar (popular, platea, etc.).
> 3. Elegir el método de pago.
> 4. Comprar la entrada.
> 5. Guardar la entrada en formato digital o impreso.
>
> Variables:
> - Precio de la entrada.
> - Ubicación en el estadio.
> - Método de pago (efectivo, transferencia, etc.).
>
> Constantes:
> - Fecha y hora del partido.
> - Cantidad de entradas disponibles.

> **Escenario:** inventario de una tienda en línea
>
> **Datos variables:**
> cantidad de productos en stock
> Precio de los productos
> numero de los pedios realizados
>
> **Datos constates:**
> nombre de la tienda
> Dirección de la tienda
> numero de teléfono de la tienda

> Usar una computadora para jugar videojuegos
>
> Manejar un Auto
>
> Jugar Futbol

> [!bug] Errata de la filmina
> - En la segunda captura: "pedios" (pedidos) y "Datos constates" (constantes), tal cual en el original.
> - En la primera, "Cantidad de entradas disponibles" figura como **constante**, pero ese valor cambia a medida que se venden entradas (es el mismo caso que el contador de mensajes de wsp de la diapositiva 34), así que sería una variable.

---

## 38 · Portada TEMA II

**TEMA II**
**Acciones**

ALGORITMOS Y ESTRUCTURAS DE DATOS 2025 - ISI UTN FRRe

| Conceptos | Tipos | Simples | Complejas |
|---|---|---|---|

> [!bug] Errata de la filmina
> La portada del TEMA II dice **2025** (la del TEMA I dice 2026). En la capa de texto del PDF el título figura como "TEMA I1".

---

## 39 · QUÉ VAMOS A VER HOY?

| | |
|---|---|
| **01 — INTRO** *(resaltado)*<br>Qué son las acciones | **02 — CARACTERÍSTICAS**<br>De los algoritmos que vamos a diseñar |
| **03 — ELEMENTOS**<br>Que componen a todos los algoritmos | **04 — DATOS**<br>Clasificación de datos que vamos a manejar |

> [!info] Nota
> Las tarjetas 02, 03 y 04 conservan los títulos del TEMA I (aparecen atenuadas). La versión actualizada del índice del TEMA II está en las diapositivas 43, 46 y 69.

---

## 40 · Seguimos por las ACCIONES…

> [!important] Definición
> Una **acción** es un
> acontecimiento producido por un **disparador**
> durante un **período de tiempo finito**,
> produce un **resultado definido** y **preciso** y
> produce un cambio de **estado**.

*(imagen de un robot)*

---

## 41 · Seguimos por las ACCIONES…

- ✅ **Acontecimiento** → Algo que sucede en el programa, como una operación o una instrucción.
- ✅ **Disparador** → El evento que inicia la acción (puede ser una condición, entrada del usuario, etc.).
- ✅ **Período de tiempo finito** → La acción tiene un inicio y un fin, no es infinita.
- ✅ **Resultado definido y preciso** → La acción tiene un efecto concreto, conocido de antemano.
- ✅ **Cambio de estado** → Modifica una variable, estructura o el comportamiento del programa.

---

## 42 · Seguimos por las ACCIONES…

```python
# Disparador: El usuario ingresa un número
numero = int(input("Ingrese un número: "))

# Acción: Se verifica si el número es par o impar
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "impar"

# Cambio de estado: La variable resultado se actualiza
print(f"El número {numero} es {resultado}.")
```

🔷 **Desglose del ejemplo:**
- ✅ **Acontecimiento:** El usuario ingresa un número.
- ✅ **Disparador:** La entrada del usuario (`input()`).
- ✅ **Período finito:** La acción ocurre en un instante (comparación y asignación).
- ✅ **Resultado preciso:** El número será "par" o "impar".
- ✅ **Cambio de estado:** La variable `resultado` cambia según la condición.

---

## 43 · QUÉ VAMOS A VER HOY?

| | |
|---|---|
| **01 — INTRO**<br>Qué son las acciones | **02 — TIPOS** *(resaltado)*<br>Clasificación de las acciones |
| **03 — ELEMENTOS**<br>Que componen a todos los algoritmos | **04 — DATOS**<br>Clasificación de datos que vamos a manejar |

---

## 44 · Los TIPOS de acciones

Las **acciones** que componen un algoritmo se pueden clasificar en **simples** y **complejas**, dependiendo de su *nivel de complejidad* y la *cantidad de operaciones* involucradas.

| Acciones Simples | Acciones Complejas |
|---|---|
| Son **instrucciones básicas** que se ejecutan en **una única operación** y **no requieren llamadas a otras instrucciones o estructuras de control** complejas.<br><br>*Son la unidad más elemental en un algoritmo.* | Son aquellas que **agrupan o combinan varias acciones simples** y requieren estructuras de control para su ejecución. |

---

## 45 · Seguimos por las ACCIONES…

```
                                         ┌── PURA
                         ┌── ASIGNACIÓN ─┤
             ┌── SIMPLES ┤               └── DE EXPRESIÓN
             │           └── ACCION ELEMENTAL
ACCIONES ────┤
             │             ┌── ACCIÓN CON NOMBRE
             └── COMPLEJAS ┼── CONDICIONALES
                           └── REPETITIVAS
```

*(resaltado con un óvalo: **ASIGNACIÓN** → PURA / DE EXPRESIÓN)*

---

## 46 · QUÉ VAMOS A VER HOY?

| | |
|---|---|
| **01 — INTRO**<br>Qué son las acciones | **02 — TIPOS**<br>Clasificación de las acciones |
| **03 — ACCIONES SIMPLES** *(resaltado)* | **04 — DATOS**<br>Clasificación de datos que vamos a manejar |

---

## 47 · ACCIÓN > SIMPLE > ASIGNACIÓN :=

**Asignarle un dato a una variable** consiste en **reemplazar el valor** anterior o inicial de la variable **con un valor nuevo**.

*Una vez que se asigna un nuevo valor, el valor anterior es eliminado de la memoria y no es posible recuperarlo.*

> [!warning] La asignación es una acción destructiva

---

## 48 · ACCIÓN > SIMPLE > ASIGNACIÓN :=

```
salario := 100000
salario := salario + 3
salario := salario / 2
```

> [!question] La variable salario ahora vale más o menos que al inicio?

---

## 49 · ACCIÓN > SIMPLE > ASIGNACIÓN :=

1. **No se puede asignar** un valor a una variable que no haya sido definida con anterioridad.
2. Con cada asignación **se pierde el valor anteriormente guardado** en la variable.
3. Para **modificar el valor de una variable** se utiliza la asignación
4. Solo puedo asignar **valores del mismo tipo** de dato

---

## 50 · ACCIÓN > SIMPLE > ASIGNACIÓN :=

> [!warning] ERRORES A EVITAR
> 1. Una variable caracter/alfanumérica si se asigna a una variable numérica.
> 2. Una variable numérica si se asigna a una variable caracter/alfanumérica.
> 3. Una asignación de una variable lógica a cualquier otra variable de otro tipo, y al contrario.

---

## 51 · ERRORES MÁS COMUNES

- nombre:alfanumerico
- edad:numerico

```
nombre:=edad
```

*(la asignación aparece tachada con una cruz roja, junto a una bomba)*

---

## 52 · ERRORES MÁS COMUNES

- Dinero:numerico

```
dinero:=$45
```

*(la asignación aparece tachada con una cruz roja)*

> [!info] Mayúsculas mezcladas
> La variable se declara como `Dinero` y se usa como `dinero`. No es un error: el pseudocódigo no distingue mayúsculas (ver [[sintaxis-completa]]), aunque conviene escribirla siempre igual.

---

## 53 · ASIGNACIÓN > Pura

*El semáforo puede tomar los siguientes valores:* *Rojo* - *Verde* - *Amarillo*

```
semaforo:=”Rojo”
semaforo:=”Verde”
semaforo:=”Amarillo”
```

*(imagen de un semáforo en verde)*

> [!info] Se asigna directamente un valor

---

## 54 · ASIGNACIÓN > De expresión algebraica

*El descuento corresponde a la mitad del importe*

```
descuento := importe / 2
```

> [!info] Se asigna el resultado de una operación

---

## 55 · ASIGNACIÓN > De expresión funcional

*Mostrar el puntaje final del examen como un valor entero*

```
examen := REDOND(puntaje)
```

> [!info] Se asigna el resultado de una función

---

## 56 · ASIGNACIÓN > De expresión incremental

| CONTADORES | ACUMULADORES |
|---|---|
| Contar cantidad de billetes | Contar cantidad de dinero |
| *billetes := billetes + 1* | *dinero := dinero + billete* |

> [!question] Se te ocurre algún ejemplo para contar y otro para acumular?

---

## 57 · ASIGNACIÓN > De expresión incremental

![[intro-contador-billetes.png]]

Seis billetes argentinos (20, 50, 100, 200, 500 y 1000 pesos) con la denominación marcada en rojo y un **1** encima de cada uno: al **contar** billetes, cada uno suma 1 sin importar su valor.

---

## 58 · Seguimos por las ACCIONES…

```
                                         ┌── PURA
                         ┌── ASIGNACIÓN ─┤
             ┌── SIMPLES ┤               └── DE EXPRESIÓN
             │           └── ACCION ELEMENTAL
ACCIONES ────┤
             │             ┌── ACCIÓN CON NOMBRE
             └── COMPLEJAS ┼── CONDICIONALES
                           └── REPETITIVAS
```

*(resaltado con un óvalo: **ACCION ELEMENTAL**)*

---

## 59 · ACCIÓN > SIMPLE > ACCIÓN ELEMENTAL

Una **acción de salida** consiste en mostrar los valores (datos) obtenidos de la evaluación de una lista de expresiones. Normalmente, los **datos son enviados a la salida estándar** (la pantalla), pero, también existen otros dispositivos de salida (la impresora, el plotter...).

En pseudocódigo, una instrucción de salida se puede escribir utilizando la siguiente sintaxis:

```
Escribir(“Mensaje textual”, variable1)
```

> [!tip]
> Lo que se incluye entre “ “ se muestra tal cual, si no se encierra entre “ “ se muestra el valor de la variable o constante

---

## 60 · ACCIÓN > SIMPLE > ACCIÓN ELEMENTAL

Una **acción de entrada** consiste en asignar a una o más variables, uno o más valores (datos) recibidos desde el exterior. Normalmente, los **datos son recogidos desde la entrada estándar** (el teclado), pero, también existen otros dispositivos de entrada (el ratón, el escáner...).

En pseudocódigo, una instrucción de entrada se puede escribir utilizando la siguiente sintaxis:

```
Leer(variable1)
```

---

## 61 · Las acciones hacen uso de OPERADORES

**Las acciones hacen uso de**

**OPERADORES**

*(íconos de +, −, ÷, ×)*

---

## 62 · Clasificación de OPERADORES

```
               ┌── Aritméticos
OPERADORES ────┼── Relacionales
               └── Lógicos
```

---

## 63 · OPERADORES Aritméticos

| Símbolo | Operación |
|---|---|
| `+` | SUMA |
| `−` | RESTA |
| `/` | DIVISIÓN REAL |
| `*` | MULTIPLICACIÓN |
| `DIV` | DIVISIÓN ENTERA |
| `MOD` | RESTO DE LA DIVISIÓN |

---

## 64 · OPERADORES Aritméticos

```
ACCION Prueba ES
AMBIENTE
   var1,var2: numérico
PROCESO
   Escribir(“Ingrese valores”)
   Leer(var1,var2)
   Escribir(“Resultados”)
   Escribir(“Suma >>”, var1+var2)
   Escribir(“Resta >>”, var1-var2)
   Escribir(“Resto div >>”, var1 MOD var2)
   Escribir(“Div real >>”, var1 / var2)
   Escribir(“Div entera >>”, var1 DIV var2)
FIN_ACCION
```

**Var1 → 24 | var2 → 5**

Salida (señalada con una flecha):

```
Suma> >> 29
Resta >> 19
Resto div >> 4
Div real >> 4.8
Div entera >> 4
```

> [!bug] Errata de la filmina
> En la salida, la primera línea dice "Suma> >> 29" (sobra un `>`); según el `Escribir(“Suma >>”, …)` debería verse "Suma >> 29".

---

## 65 · OPERADORES Relacionales

| Símbolo | Significado |
|---|---|
| `=` | IGUAL A |
| `<` | MENOR A |
| `>` | MAYOR A |
| `<=` | MENOR O IGUAL A |
| `>=` | MAYOR O IGUAL A |
| `<>` | DISTINTO A |

---

## 66 · OPERADORES Relacionales

> [!important] Al aplicar operadores relacionales, los resultados devuelven **valores de verdad**

| var1 = var2 | var1 < var2 | var1 > var2 | var1 <> var2 |
|:-:|:-:|:-:|:-:|
| F | F | V | V |

*(con los valores de la diapositiva anterior: var1 = 24, var2 = 5)*

---

## 67 · OPERADORES Lógicos

| | |
|---|---|
| **AND - Y** | Se deben cumplir las dos condiciones |
| **OR - O** | Se deben cumplir al menos una de las dos condiciones |

**A Y B**

| A | B | RESULTADO |
|:-:|:-:|:-:|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | F |

**A O B**

| A | B | RESULTADO |
|:-:|:-:|:-:|
| V | V | V |
| V | F | V |
| F | V | V |
| F | F | F |

---

## 68 · Actividad N° 2

1) Nos agrupamos de acuerdo a cómo te indica tu profe
2) Deberemos responder un cuestionario en grupo usando

*(logos de ChatGPT, Copilot y Gemini)*

1) Las 6 preguntas se asignarán al azar
2) Tomate una selfie de tu equipo y arroba a @aed.utn.frre en IG
3) **https://bit.ly/ACT1AED2024**
4) Las respuestas se compartirán la próxima clase

---

## 69 · QUÉ VAMOS A VER LA PRÓXIMA?

| | |
|---|---|
| **01 — INTRO**<br>Qué son las acciones | **02 — TIPOS**<br>Clasificación de las acciones |
| **03 — ACCIONES SIMPLES** | **04 — ACCIONES COMPLEJAS** *(resaltado)* |

---

## 70 · Seguimos por las ACCIONES…

```
                                         ┌── PURA
                         ┌── ASIGNACIÓN ─┤
             ┌── SIMPLES ┤               └── DE EXPRESIÓN
             │           └── ACCION ELEMENTAL
ACCIONES ────┤
             │             ┌── ACCIÓN CON NOMBRE
             └── COMPLEJAS ┼── CONDICIONALES
                           └── REPETITIVAS
```

*(resaltado con un óvalo: **COMPLEJAS** → ACCIÓN CON NOMBRE / CONDICIONALES / REPETITIVAS)*

---

## 71 · Gracias!

**Gracias!**

**Momento de preguntas!!!**

| AED | VARIABLES AAAA |
|---|---|
