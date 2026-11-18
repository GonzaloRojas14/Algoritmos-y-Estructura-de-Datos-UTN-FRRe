---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 10
titulo_original: "Recursividad — Clase 1 · Concepto, diseño y funcionamiento"
archivo_original: 05_Recursividad_Clase1_Concepto_Rev1.pdf
diapositivas: 27
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - recursividad
---

# 10 — Recursividad (Concepto)

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 27 diapositivas de **Recursividad — Clase 1 · Concepto, diseño y funcionamiento** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[05_Recursividad_Clase1_Concepto_Rev1.pdf]] (carpeta `PDF originales/`).
> El PDF tiene 27 páginas pero la numeración de la filmina llega a 22: cinco páginas son **ampliaciones** del código de la diapositiva anterior (repiten el mismo número al pie). Acá van en su lugar, marcadas como *(ampliación)*.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

Sigue en [[11 — Recursividad (Tipos y Ejemplos)]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

# Recursividad

**Clase 1 · Concepto, diseño y funcionamiento**

*Caso base · Caso recursivo · Pila de llamadas · Verificación*

---

## 2 · Objetivos de la clase — ¿Qué vamos a aprender hoy?

*OBJETIVOS DE LA CLASE*

1. **Qué es la recursividad**
   Una subacción que se llama a sí misma para resolver una versión más chica del mismo problema.
2. **Sus dos partes**
   Caso base (corta la recursión) y caso recursivo (se acerca al caso base).
3. **Cómo se ejecuta**
   Traza de llamadas, retornos y la pila de llamadas (registros de activación).
4. **Cómo verificarla**
   El método de las tres preguntas y los errores típicos (recursión infinita).

---

## 3 · Punto de partida — Repaso: una función que llama a otra

*PUNTO DE PARTIDA*

```
Accion SUMAR ES;
Ambiente
    a, b: entero;

Funcion Suma(x, y: entero): entero;
Proceso
    Suma := x + y;
Fin;

Proceso
    Escribir('Ingrese dos valores:');
    Leer(a, b);
    Escribir('Suma: ', Suma(a, b));
FinAccion.
```

*(En la filmina están resaltadas la cabecera `Funcion Suma(x, y: entero): entero;` y la invocación `Suma(a, b)`.)*

**Ya sabemos que…**

El Proceso principal **invoca** a la función Suma y recibe su resultado.

Una subacción también puede invocar a **otra** subacción.

> [!question] ¿Y si una función se llama **a sí misma**?

---

## 4 · Repaso *(ampliación de la diapositiva 3)*

```
Accion SUMAR ES;
Ambiente
    a, b: entero;

Funcion Suma(x, y: entero): entero;
Proceso
    Suma := x + y;
Fin;

Proceso
    Escribir('Ingrese dos valores:');
    Leer(a, b);
    Escribir('Suma: ', Suma(a, b));
FinAccion.
```

> [!question] ¿Y si una función se llama **a sí misma**?

---

## 5 · Una imagen para empezar — La matrushka: una dentro de otra

*UNA IMAGEN PARA EMPEZAR*

*(Ilustración: cinco muñecas matrushka en fila, de la más grande a la más chica.)*

Cada muñeca contiene otra igual, pero más pequeña. Y así, una dentro de otra… hasta llegar a la más chica, que ya no se abre.

> [!info] Abrir una muñeca
> → encontramos el mismo problema, más chico

> [!tip] La muñeca más chica
> → no se abre: ahí termina

> [!important] Esa es la idea
> resolver un problema usando el mismo problema, pero más chico.

---

## 6 · Concepto central — ¿Qué es la recursividad?

*CONCEPTO CENTRAL*

> [!important] Definición
> La recursividad es una técnica en la que **una subacción se invoca a sí misma** dentro de su propio proceso, para resolver una versión **más pequeña** del mismo problema.

| Problema grande | → | Mismo problema, más chico | → | Caso trivial |
|---|---|---|---|---|
| Ej.: calcular 4! | → | 4! = 4 · 3! → 3! = 3 · 2! … | → | 0! = 1 (se resuelve sin recursión) |

*Se aplica tanto a funciones como a procedimientos.*

---

## 7 · Anatomía de un algoritmo recursivo — Caso base y caso recursivo

*ANATOMÍA DE UN ALGORITMO RECURSIVO*

| CASO BASE | CASO RECURSIVO |
|---|---|
| • Es el caso trivial: se resuelve directamente, sin volver a llamar. | • La subacción se vuelve a llamar a sí misma. |
| • Es la condición de corte de la recursión. | • Con parámetros que se acercan al caso base. |
| • Puede haber más de uno. | • Cada llamada resuelve un problema más chico. |

> [!warning] Importante
> si falta el caso base, o la llamada no se acerca a él, la recursión nunca termina.

---

## 8 · Diseño — ¿Cómo resolvemos un problema en forma recursiva?

*DISEÑO*

1. **¿Cómo se resuelve el caso más pequeño?**
   Esa respuesta NO es recursiva y define el caso base. Puede haber más de uno.
2. **Organizar un cambio de estado hacia el caso base**
   En cada llamada se modifican los datos (los parámetros) acercándolos a los del caso base.
3. **Establecer la llamada recursiva**
   ¿En qué punto la subacción se llama a sí misma, y con qué parámetros?

---

## 9 · Un ejemplo clásico — El factorial de un número

*UN EJEMPLO CLÁSICO*

| n! | valor | usando el anterior |
|---|---|---|
| `0!` | 1 | (por definición) |
| `1!` | 1 | `= 1 · 0!` |
| `2!` | 2 | `= 2 · 1!` |
| `3!` | 6 | `= 3 · 2!` |
| `4!` | 24 | `= 4 · 3!` |
| `5!` | 120 | `= 5 · 4!` |

> [!important] En general
> **`n! = n · (n−1)!`**
> para n > 0

Para calcular un factorial necesitamos **el factorial anterior**: el problema se define en términos de sí mismo.

---

## 10 · Solución que ya conocemos — Factorial iterativo

*SOLUCIÓN QUE YA CONOCEMOS*

```
Funcion Factorial(n: entero): entero;
Ambiente
    i, fact: entero;
Proceso
    fact := 1;
    PARA i := 1 HASTA n HACER
        fact := fact * i;
    FIN_PARA;
    Factorial := fact;
Fin;
```

*(Resaltado en la filmina: el ciclo `PARA … FIN_PARA;`.)*

**Ciclo explícito**
Repite con PARA desde 1 hasta n.

**Acumulador**
fact va guardando el producto parcial: 1 · 2 · 3 · … · n

---

## 11 · Factorial iterativo *(ampliación de la diapositiva 9)*

```
Funcion Factorial(n: entero): entero;
Ambiente
    i, fact: entero;
Proceso
    fact := 1;
    PARA i := 1 HASTA n HACER
        fact := fact * i;
    FIN_PARA;
    Factorial := fact;
Fin;
```

---

## 12 · ¿Y la solución recursiva? — Definición formal del factorial

*Y LA SOLUCIÓN RECURSIVA?*

```
        ┌  1             si n = 0      caso base
n!  =  ─┤
        └  n · (n−1)!    si n > 0      caso recursivo
```

> [!info] Observá
> en el caso recursivo el factorial vuelve a aparecer, pero con n − 1 (más cerca del 0).

---

## 13 · Algoritmo recursivo — Factorial recursivo

*ALGORITMO RECURSIVO*

```
Funcion Factorial(n: entero): entero;
Proceso
    SI n = 0 ENTONCES
        Factorial := 1;                        ◀ CASO BASE
    CONTRARIO
        Factorial := n * Factorial(n - 1);     ◀ CASO RECURSIVO
    FIN_SI;
Fin;
```

*(Las etiquetas ◀ CASO BASE y ◀ CASO RECURSIVO son carteles al costado del código en la filmina, no parte del pseudocódigo.)*

> [!info] La llamada
> Factorial(n - 1) invoca a la misma función con un problema más chico. El SI decide cuál de los dos casos se ejecuta.

---

## 14 · Factorial recursivo *(ampliación de la diapositiva 11)*

```
Funcion Factorial(n: entero): entero;
Proceso
    SI n = 0 ENTONCES
        Factorial := 1;                        ◀ CASO BASE
    CONTRARIO
        Factorial := n * Factorial(n - 1);     ◀ CASO RECURSIVO
    FIN_SI;
Fin;
```

---

## 15 · Programa completo — Factorial recursivo dentro de una Accion

*PROGRAMA COMPLETO*

```
Accion FACTORIAL ES;
Ambiente
    num: entero;

Funcion Factorial(n: entero): entero;
Proceso
    SI n = 0 ENTONCES
        Factorial := 1;
    CONTRARIO
        Factorial := n * Factorial(n - 1);
    FIN_SI;
Fin;
```

**Proceso principal**

```
Proceso
    Leer(num);
    Escribir(Factorial(num));
FinAccion.
```

> [!warning] Precondición
> num ≥ 0. Con un negativo nunca se llega a n = 0.

---

## 16 · Programa completo *(ampliación de la diapositiva 12)*

```
Accion FACTORIAL ES;
Ambiente
    num: entero;

Funcion Factorial(n: entero): entero;
Proceso
    SI n = 0 ENTONCES
        Factorial := 1;
    CONTRARIO
        Factorial := n * Factorial(n - 1);
    FIN_SI;
Fin;
```

**Proceso principal**

```
Proceso
    Leer(num);
    Escribir(Factorial(num));
FinAccion.
```

*(En la ampliación están resaltados en amarillo `Factorial(n: entero)` de la cabecera y la llamada recursiva `Factorial(n - 1)`.)*

---

## 17 · Ejecución paso a paso — Factorial(4): la ida (llamadas)

*EJECUCIÓN PASO A PASO*

```
Factorial(4) = 4 * Factorial(3)
  ↘
    Factorial(3) = 3 * Factorial(2)
      ↘
        Factorial(2) = 2 * Factorial(1)
          ↘
            Factorial(1) = 1 * Factorial(0)
              ↘
                Factorial(0) = 1
```

**Cada llamada espera**
No puede calcular su resultado hasta que vuelva la llamada que hizo.

> [!tip] Hasta el caso base
> Factorial(0) ya no llama a nadie: devuelve 1.

---

## 18 · Ejecución paso a paso — Factorial(4): la vuelta (retornos)

*EJECUCIÓN PASO A PASO*

```
Factorial(0) = 1
  ↘
    Factorial(1) = 1 * 1 = 1
      ↘
        Factorial(2) = 2 * 1 = 2
          ↘
            Factorial(3) = 3 * 2 = 6
              ↘
                Factorial(4) = 4 * 6 = 24
```

**Se resuelve al volver**
Cada retorno completa la multiplicación que había quedado pendiente.

> [!important] Resultado
> **`4! = 24`**

---

## 19 · ¿Qué pasa en memoria? — La pila de llamadas

*¿QUÉ PASA EN MEMORIA?*

```
          TOPE
  ┌───────────────────────┐
  │  Factorial    n = 0   │      ▲
  ├───────────────────────┤      │
  │  Factorial    n = 1   │      │
  ├───────────────────────┤      │
  │  Factorial    n = 2   │      │  se apila
  ├───────────────────────┤      │
  │  Factorial    n = 3   │      │
  ├───────────────────────┤      │
  │  Factorial    n = 4   │      │
  └───────────────────────┘
```

> [!info] LIFO
> el último que entra es el primero que sale.

**Registro de activación**
Cada llamada guarda en la pila sus parámetros, variables locales y el punto de retorno.

**Apilar (ida)**
Factorial(4), (3), (2), (1), (0)… cada una queda arriba de la anterior.

**Desapilar (vuelta)**
Al llegar al caso base se desapila y se devuelve el valor: 1, 1, 2, 6, 24.

---

## 20 · Verificación — El método de las tres preguntas

*VERIFICACIÓN*

| Pregunta | |
|---|---|
| **Caso base** | ¿Existe una salida no recursiva? ¿Funciona correctamente para ese caso? |
| **Más pequeño** | ¿Cada llamada recursiva se refiere a un caso más pequeño del problema original? |
| **Caso general** | Suponiendo que la llamada recursiva funciona, ¿la solución es correcta para los casos no base? |

---

## 21 · Verificación — Las tres preguntas aplicadas a Factorial

*VERIFICACIÓN*

```
SI n = 0 ENTONCES
    Factorial := 1;
CONTRARIO
    Factorial := n * Factorial(n - 1);
FIN_SI;
```

| | | |
|---|---|---|
| **Caso base** | n = 0 devuelve 1, y 0! = 1. | ✓ |
| **Más pequeño** | Cada llamada usa n − 1: se acerca a 0. | ✓ |
| **Caso general** | Si Factorial(n−1) = (n−1)!, entonces n · (n−1)! = n! | ✓ |

> [!tip] Las tres en ✓
> El algoritmo es correcto (para n ≥ 0).

---

## 22 · Error típico — ¿Qué pasa si no hay caso base?

*ERROR TÍPICO*

```
Funcion Factorial(n: entero): entero;
Proceso
    Factorial := n * Factorial(n - 1);
Fin;
```

| Sin caso base | No se acerca | Dato inválido |
|---|---|---|
| Nunca hay una salida que no llame de nuevo. | Ej.: Factorial(n + 1): se aleja del caso base. | Factorial(-3) con caso base n = 0: nunca llega. |

```
Factorial(2)
  ↘
    Factorial(1)
      ↘
        Factorial(0)
          ↘
            Factorial(-1)
              ↘
                Factorial(-2) …

        ══ Desbordamiento de pila ══
```

*(En la filmina, Factorial(-1) y Factorial(-2) … están en rojo, igual que el cartel "Desbordamiento de pila".)*

---

## 23 · Segundo ejemplo — Potencia: b elevado a la p

*SEGUNDO EJEMPLO*

**Definición**

| | |
|---|---|
| **`b⁰ = 1`** | caso base (p = 0) |
| **`bᵖ = b · bᵖ⁻¹`** | caso recursivo (p > 0) |

```
Funcion Potencia(b, p: entero): entero;
Proceso
    SI p = 0 ENTONCES
        Potencia := 1;
    CONTRARIO
        Potencia := b * Potencia(b, p - 1);
    FIN_SI;
Fin;
```

> [!info] El cambio de estado
> b no cambia; p baja de a 1 en cada llamada hasta llegar a 0.

---

## 24 · Potencia *(ampliación de la diapositiva 19)*

```
Funcion Potencia(b, p: entero): entero;
Proceso
    SI p = 0 ENTONCES
        Potencia := 1;
    CONTRARIO
        Potencia := b * Potencia(b, p - 1);
    FIN_SI;
Fin;
```

---

## 25 · Ejecución paso a paso — Potencia(2, 3): ida y vuelta

*EJECUCIÓN PASO A PASO*

```
IDA (llamadas)                              VUELTA (retornos)

Potencia(2,3) = 2 * Potencia(2,2)           Potencia(2,0) = 1
  ↘                                           ↘
    Potencia(2,2) = 2 * Potencia(2,1)           Potencia(2,1) = 2 * 1 = 2
      ↘                                           ↘
        Potencia(2,1) = 2 * Potencia(2,0)           Potencia(2,2) = 2 * 2 = 4
          ↘                                           ↘
            Potencia(2,0) = 1                           Potencia(2,3) = 2 * 4 = 8
```

> [!info] Pila
> 4 registros de activación (p = 3, 2, 1, 0). Resultado: 2³ = 8.

---

## 26 · Resumen de la clase — Lo que tenemos que llevarnos

*RESUMEN DE LA CLASE*

1. Recursividad: una subacción que se invoca a sí misma con un problema más chico.
2. Siempre hay un caso base (corta) y un caso recursivo (se acerca al caso base).
3. Cada llamada apila un registro de activación; se resuelve al volver (LIFO).
4. Verificamos con las tres preguntas: caso base, más pequeño, caso general.

---

## 27 · Para practicar — Ejercicios para la próxima clase

*PARA PRACTICAR*

| 1 · Sumatoria | 2 · Producto | 3 · Contar hacia atrás |
|---|---|---|
| Sumar(n) = 1 + 2 + … + n | Multiplicar a · b usando sólo sumas | Procedimiento que escriba n, n−1, …, 1 |
| *Pista: Sumar(0) = 0* | *Pista: a · 0 = 0;  a · b = a + a · (b − 1)* | *Pista: si n = 0 no hace nada* |

*Para cada uno: identificar el caso base, el caso recursivo y responder las tres preguntas.*

---

Sigue en [[11 — Recursividad (Tipos y Ejemplos)]]
