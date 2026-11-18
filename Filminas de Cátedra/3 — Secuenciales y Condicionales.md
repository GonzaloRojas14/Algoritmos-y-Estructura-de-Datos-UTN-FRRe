---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 3
titulo_original: ESTRUCTURAS DE CONTROL
archivo_original: TEMA 3-Secuenciales_Condicionales.pdf
diapositivas: 35
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - estructuras-de-control
  - secuenciales
  - condicionales
---

# 3 — Estructuras de Control: Secuenciales y Condicionales

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 35 diapositivas de **ESTRUCTURAS DE CONTROL** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[TEMA 3-Secuenciales_Condicionales.pdf]] (carpeta `PDF originales/`).
> Casi todo el pseudocódigo de la presentación está como imagen; se transcribió respetando palabras clave, mayúsculas, comillas y sangría de cada filmina. Los diagramas de flujo están recortados en `img/`.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Apertura

*(dibujo de un robot con un globo de diálogo)*

> Hoy vamos a enseñarle a una computadora a tomar decisiones

```
SI tengo hambre
   ENTONCES como
SINO
   sigo programando
```

---

## 2 · Portada

**ESTRUCTURAS DE CONTROL**

Algoritmos y Estructuras de Datos 2026
UTN FRRe

---

## 3 · Qué vamos a ver

| 01 | 02 | 03 | 04 |
|---|---|---|---|
| Introducción | Estructuras Secuenciales | Estructuras Condicionales | Estructuras Repetitivas |

---

## 4 · Estructuras de Control

*(imagen decorativa: vista aérea de un cruce de autopistas)*

> [!important] Definición
> Las estructuras de control tienen una finalidad bastante definida: ***señalar el orden en que tienen que sucederse los pasos de un algoritmo.***

---

## 5 · Una estructura de control se caracteriza por

> [!info] Inicio y Fin
> Una estructura de control tiene un único punto de entrada y un único punto de salida

> [!info] Acciones
> Una estructura de control se compone de sentencias o de otras estructuras de control

---

## 6 · *(Inicio, acciones y fin en un algoritmo)*

![[control-estructura-inicio-acciones-fin.png]]
Código de ejemplo con anotaciones: una flecha **INICIO** apunta a la línea 1 (`ACCION EJEMPLO1 ES`), una llave **ACCIONES** abarca las líneas 4 a 8 (de `PROCESO` hasta el último `Escribir`) y una flecha **FIN** apunta a la línea 9 (`FIN_ACCION`).

```
ACCION EJEMPLO1 ES
AMBIENTE
    var:entero

PROCESO
    Escribir("Ingrese su nro. favorito")
    Leer(var)
    Escribir ("Su nro favorito es:", var)
FIN_ACCION
```

---

## 7 · Clasificación de Estructuras de Control

```
                          ┌──────────────────┐
                     ┌────┤   SECUENCIALES   │
                     │    └──────────────────┘
 ESTRUCTURAS         │    ┌──────────────────┐
 DE CONTROL  ────────┼────┤  CONDICIONALES   │
                     │    └──────────────────┘
                     │    ┌──────────────────┐
                     └────┤   REPETITIVAS    │
                          └──────────────────┘
```

---

## 8 · A — Estructuras Secuenciales

**A**
**Estructuras Secuenciales**

*(diapositiva separadora de sección)*

---

## 9 · Estructuras Secuenciales

```
ACCION Ejemplo1 ES
AMBIENTE
   a,doble: entero
PROCESO
   ESCRIBIR('Ingrese el número')
   LEER(a)
   doble := a * 2
   ESCRIBIR('Resultado>>',doble)
FIN_ACCION
```

> [!important] Estructuras Secuenciales
> La ejecución comienza con la **primera sentencia** del algoritmo y **prosigue hasta la última sentencia**, cada una de las cuales
> **<u>se ejecuta una sola vez</u>**

---

## 10 · Problema / Solución

> [!question] Problema
> **Dado un importe, obtener su 10%**
>
> **Ingresar importe**
> 452
> **El 10% es**
> $45.2

> [!tip] Solución
> **Una variable tipo numérica**
> **Estructura secuencial**

```
Accion Porcentaje Es
Ambiente
   importe: numérico
Proceso
 Esc(‘Ingrese importe’)
 Leer(importe)
 Esc(‘El 10% es ‘, 10*importe/100)
Fin Accion
```

---

## 11 · B — Estructuras Condicionales

**B**
**Estructuras Condicionales**

*(diapositiva separadora de sección)*

---

## 12 · Vacaciones

**Vacaciones**
A dónde vamos?

*(imagen decorativa: tres fotos en círculos — una playa con palmeras, montañas, un televisor con Netflix)*

Factores que aparecen alrededor: **Dinero disponible** · **Fechas posibles** · **Feriados XXL**

---

## 13 · Estructuras Condicionales

1. Cuando hay que **tomar una decisión** aparecen las **`estructuras condicionales`**.
2. En estas estructuras se realiza una **evaluación de una condición** y de acuerdo al resultado, el algoritmo realiza **una determinada acción**.
3. Las condiciones son especificadas utilizando **expresiones lógicas**.

---

## 14 · Estructuras Condicionales

| | Tipo | |
|---|---|---|
| **01** | **Condicionales Simples** | Una sola opción |
| **02** | **Condicionales Alternativas** | Dos opciones |
| **03** | **Condicionales Múltiples** | Más de dos opciones |

*(las tres tarjetas se conectan a un círculo que dice **Cuáles?**)*

---

## 15 · Condicional Simple

![[control-diagrama-condicional-simple.png]]
Diagrama de flujo: ACCIÓN 1 → rombo «SE CUMPLE CONDICIÓN»; por **SI** se ejecuta ACCIÓN 2; por **NO** se saltea ACCIÓN 2 y ambos caminos se unen a la salida.

1. Si **se verifica una determinada condición**, ejecutar una serie de instrucciones y luego seguir adelante.
2. Si **la condición NO se cumple, NO se ejecutan** dichas instrucciones y se sigue adelante.

---

## 16 · Ejemplo Condicional Simple

```
SI condicion_se_cumple ENTONCES

   ACCIÓN_1
   ACCIÓN_2
   ….
   ACCIÓN_N

FIN SI
```

---

## 17 · Ejemplo Condicional Simple

Cálculo del valor de la función **f(x) = 0 si x ≤ 0, f(x) = x² si x > 0**

```
Accion EjercicioCS Es
Ambiente
  x,f:numérico
Proceso
  Esc(‘Ingrese valor X:’)
  Leer(x)
  f:=0
  Si x > 0 entonces
    f:= x**2
  Fin Si
  Esc(‘El valor de la función f(x) para x =’, x, ‘es:’, f)

Fin Acción
```

---

## 18 · Python

*(logo de Python)*

https://www.online-python.com/

---

## 19 · Ejemplo Condicional Simple

EJEMPLO
Mostrar por pantalla un mensaje si un número es mayor a 100

```
Accion Mayor100 Es
Ambiente
  a:numérico
Proceso
  ESC(“Ingrese el número”)
  LEER(a)
  SI a > 100 ENTONCES
    ESCRIBIR(“El nro. está autorizado”)
  FIN_SI
Fin Acción
```

```python
# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Verificar si el número es mayor a 100
if numero > 100:
    print("El nro. Está autorizado")
```

---

## 20 · Ejemplo Condicional Simple

EJEMPLO
Dada un número, mostrar por pantalla si es par.

```
Accion EsPar Es
Ambiente
  a:numérico
Proceso
  ESC(“Ingrese el número”)
  LEER(a)
  SI a MOD 2 = 0 ENTONCES
    ESCRIBIR(“El nro. es par”)
  FIN_SI
Fin Acción
```

```python
num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("El nro. es par.")
```

---

## 21 · Condicional Alternativo

![[control-diagrama-condicional-alternativo.png]]
Diagrama de flujo: ACCIÓN 1 → rombo «SE CUMPLE CONDICIÓN»; por **SI** se ejecuta ACCIÓN 2, por **NO** se ejecuta ACCIÓN 3.

1. Si **se verifica una determinada condición**, ejecutar una serie de instrucciones y luego seguir adelante.
2. Si **la condición NO se cumple, ejecuta otra serie de acciones.**

---

## 22 · Ejemplo Condicional Alternativo

```
SI condicion_se_cumple ENTONCES

   ACCIÓN_1
   ….
   ACCIÓN_N
CONTRARIO
       OTRAS_ACCIONES
FIN SI
```

---

## 23 · Ejemplo Condicional Alternativo

**Mostrar por pantalla si un número es o no mayor que otro**

```
Accion EjercicioCS Es
Ambiente
  a,b:numérico
Proceso
  ESC(“Ingrese el primer número”), LEER(A)
  ESC(“Ingrese el segundo número”), LEER(B)
  SI A > B ENTONCES
   ESC(A,“es mayor que “,B)
  SINO
   ESC(A,“NO es mayor que “,B)
  FIN_SI

Fin Acción
```

*(en la filmina, la rama del `ENTONCES` está resaltada en amarillo y la del `SINO` en celeste)*

> [!info] Mayúsculas mezcladas
> En `Ambiente` se declaran `a,b` y en el `Proceso` se usan `A` y `B`. No es un error: el pseudocódigo no distingue mayúsculas (ver [[sintaxis-completa]]), aunque conviene escribirlas siempre igual.

---

## 24 · Ejemplo Condicional Alternativo

**Mostrar por pantalla si un número es o no mayor que otro**

```python
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
else:
    print(f"{num2} es mayor o igual que {num1}.")
```

---

## 25 · Ejemplo Condicional Alternativo

**Dada la cantidad de personas que usan Twitter e Instagram, qué red social es más usada?**

```
Accion EjercicioCS Es
Ambiente
  a,b:numérico
Proceso
  ESC(“Ingrese cantidad de personas en Twitter”), LEER(A)
  ESC(“Ingrese cantidad de personas en Instagram”), LEER(B)
  SI A > B ENTONCES
   ESC(“Twitter es más usada que Instagram”)
  SINO
   ESC(“Instagram es más usada que Twitter”)
  FIN_SI

Fin Acción
```

*(en la filmina, la rama del `ENTONCES` está resaltada en amarillo y la del `SINO` en celeste)*

> [!bug] Errata de la filmina
> Si las dos cantidades son iguales (`A = B`), el algoritmo muestra «Instagram es más usada que Twitter». La versión en Python de la diapositiva siguiente sí contempla el empate.

---

## 26 · Ejemplo Condicional Alternativo

**Dada la cantidad de personas que usan Twitter e Instagram, qué red social es más usada?**

```python
tw_usr = int(input("Ingrese la cantidad de usuarios de Twitter: "))
ig_usr = int(input("Ingrese la cantidad de usuarios de Instagram: "))

if tw_usr > ig_usr:
   print("Twitter es la red social más usada.")
elif ig_usr > tw_usr:
   print("Instagram es la red social más usada.")
else:
   print("Ambas redes tienen la misma cantidad de usuarios.")
```

---

## 27 · Y qué pasa si hay más de una alternativa de acción?

*(imagen decorativa: mapa con tres chinches rojas)*

**Y qué pasa si hay más de una alternativa de acción?**

---

## 28 · Condicional Múltiple

![[control-diagrama-condicional-multiple.png]]
Diagrama de flujo: ACCION 0 → rombo «VARIABLE»; según su valor sale por **VALOR 1** a ACCIÓN 1, por **VALOR 2** a ACCIÓN 2 o por **OTROS** a ACCIÓN N.

> [!important] Definición
> Las estructuras de comparación múltiples, es una toma de decisión especializada que permiten **evaluar una variable** con distintos posibles resultados, ejecutando para cada caso una **serie de instrucciones específicas**.

---

## 29 · Ejemplo Condicional Múltiple

```
SEGÚN variable HACER
  VALOR1: ACCIONES_1
  VALOR2: ACCIONES_2
  …
  OTROS: ACCIONES_N
FIN SEGÚN
```

---

## 30 · Ejemplo Condicional Múltiple

EJEMPLO
Indicar si una persona es < de 18 años, < de 50 años o mayor a 50 años

```
Accion Mayor Es
Ambiente
  edad:numérico
Proceso
  ESC(“Ingrese edad”)
  LEER(edad)
  SEGÚN edad HACER
   <18: ESCRIBIR (‘Menor de 18 años’)
   <50: ESCRIBIR (‘Menor de 50 años’)
   >50: ESCRIBIR (‘Mayor de 50 años’)
   OTRO: ESCRIBIR (‘Tiene 50 años’)
  FIN_SEGUN
Fin Acción
```

```python
def clasificar_edad(edad):
    if edad < 18:
        return "Menor de 18 años"
    elif edad < 50:
        return "Menor de 50 años"
    else:
        return "Mayor de 50 años"

# Ejemplo de uso
edad = int(input("Ingrese la edad: "))
print(clasificar_edad(edad))
```

> [!bug] Errata de la filmina
> - Las dos versiones no hacen lo mismo con `edad = 50`: el pseudocódigo cae en `OTRO` y muestra «Tiene 50 años», pero el Python entra al `else` y devuelve «Mayor de 50 años».
> - Los casos `<18` y `<50` se superponen (una edad de 10 cumple los dos); el resultado depende de que el `SEGÚN` tome solo el primer caso que se cumple, cosa que la filmina no aclara.
> - El esquema general de la diapositiva 29 usa `OTROS:` y `FIN SEGÚN`; este ejemplo usa `OTRO:` y `FIN_SEGUN`.

---

## 31 · Otras Herramientas

**OTRAS HERRAMIENTAS**

Anidamiento de condicionales

---

## 32 · Condicionales Anidados

Imagina un programa que informe si un número es positivo, negativo o cero. Y que no puedes utilizar el condicional múltiple

```
ACCION TresOpciones ES
AMBIENTE
  user: alfanumérico
  followers: numérico
PROCESO
  Escribir('Ingrese un número')
  Leer(num)
  Si num > 0 entonces
    Escribir(num, "es un número positivo")
  contrario
    Si num < 0 entonces
      Escribir(num, "es un número negativo")
    contrario
      Escribir(num, "es 0")
    Fin_Si
  Fin_Si
FIN_ACCION
```

```python
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")
```

`num > 0` evalúa a `True` (que es `1`) si el número es positivo y a `False` (que es `0`) si no lo es.

`num < 0` hace lo mismo para los negativos.

`num == 0` lo hace para el caso en que sea exactamente cero.

Como `True` equivale a `1` y `False` equivale a `0`, cada comparación actúa como un interruptor que activa el mensaje correcto.

> [!bug] Errata de la filmina
> - La variable `num` se usa (`Leer(num)`) pero no está declarada en `AMBIENTE`. En cambio se declaran `user: alfanumérico` y `followers: numérico`, que no se usan (parecen de otro ejercicio).
> - El texto explicativo habla de `num == 0` y de comparaciones que actúan «como un interruptor» (`True` = 1, `False` = 0), pero el código Python de la misma filmina es un `if / elif / else` que no evalúa `num == 0` ni usa las comparaciones como números. El texto no describe el código que tiene al lado. Además, al fragmento Python le falta leer `num`.

---

## 33 · Para repasar

Haz un algoritmo que indique qué calificación tiene un alumno dada su nota numérica según el siguiente criterio.

- Suspenso, si la nota es inferior a 5.
- Aprobado, si la nota está en el intervalo [5,7).
- Notable, si la nota está en el intervalo [7,9).
- Sobresaliente, si la nota está en el intervalo [9,10).
- Matrícula de Honor, si la nota es un 10.

---

## 34 · Para repasar

Un año es bisiesto si es divisible por **4**, pero no por **100**, excepto que también sea divisible por **400**. Escribe un pseudocódigo que determine si un año ingresado es bisiesto o no.

---

## 35 · Para repasar

Escribe un algoritmo que determine el signo del zodiaco basado en el día y mes de nacimiento ingresados por el usuario.
