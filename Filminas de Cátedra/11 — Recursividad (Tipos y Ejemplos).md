---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 11
titulo_original: "Recursividad — Clase 2 · Tipos, ejemplos y comparación con iteración"
archivo_original: 05_Recursividad_Clase2_Tipos_y_Ejemplos_Rev_1.pdf
diapositivas: 33
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - recursividad
---

# 11 — Recursividad (Tipos y Ejemplos)

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 33 diapositivas de **Recursividad — Clase 2 · Tipos, ejemplos y comparación con iteración** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[05_Recursividad_Clase2_Tipos_y_Ejemplos_Rev_1.pdf]] (carpeta `PDF originales/`).
> El PDF tiene 33 páginas pero la numeración de la filmina llega a 27: seis páginas son **ampliaciones** del código de la diapositiva anterior (repiten el mismo número al pie). Acá van en su lugar, marcadas como *(ampliación)*.

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

Viene de [[10 — Recursividad (Concepto)]]

---

## 1 · Portada

**ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE**

# Recursividad

**Clase 2 · Tipos, ejemplos y comparación con iteración**

*Directa e indirecta · Cabeza, cola, múltiple · Números y arreglos · Recursión vs iteración*

---

## 2 · Repaso de la clase anterior — Lo que ya sabemos

*REPASO DE LA CLASE ANTERIOR*

| Caso base | Caso recursivo | Pila de llamadas |
|---|---|---|
| Se resuelve sin volver a llamar. Corta la recursión. | Se vuelve a llamar con un problema más chico, acercándose al caso base. | Cada llamada apila su registro de activación; se resuelve al volver (LIFO). |

```
SI <caso base> ENTONCES
    <resolver sin llamar>
CONTRARIO
    <llamarse con un problema más chico>
FIN_SI;
```

**Tres preguntas**
Caso base · Más pequeño · Caso general

---

## 3 · Tipos de recursividad — Según cómo se invoca: directa o indirecta

*TIPOS DE RECURSIVIDAD*

```
   DIRECTA                     INDIRECTA (MUTUA)

   ┌─────┐                     ┌─────┐  ───►  ┌─────┐
   │  A  │◄─┐                  │  A  │        │  B  │
   └─────┘  │                  └─────┘  ◄───  └─────┘
      └─────┘
```

| DIRECTA | INDIRECTA (MUTUA) |
|---|---|
| **`A llama a A`** | **`A llama a B, B llama a A`** |
| *Ej.: Factorial, Potencia* | *Ej.: EsPar / EsImpar* |

> [!warning] En ambos casos
> tiene que existir un caso base que corte la cadena de llamadas.

---

## 4 · Recursividad indirecta — Ejemplo: EsPar y EsImpar

*RECURSIVIDAD INDIRECTA*

```
Funcion EsPar(n: entero): logico;
Proceso
    SI n = 0 ENTONCES
        EsPar := VERDADERO;
    CONTRARIO
        EsPar := EsImpar(n - 1);
    FIN_SI;
Fin;
```

```
Funcion EsImpar(n: entero): logico;
Proceso
    SI n = 0 ENTONCES
        EsImpar := FALSO;
    CONTRARIO
        EsImpar := EsPar(n - 1);
    FIN_SI;
Fin;
```

**Traza de EsPar(3):**

```
EsPar(3) ──► EsImpar(2) ──► EsPar(1) ──► EsImpar(0) ──► FALSO
```

---

## 5 · Tipos de recursividad — Según dónde está la llamada recursiva

*TIPOS DE RECURSIVIDAD*

| De cola | De cabeza | Intermedia |
|---|---|---|
| La llamada es lo último que se ejecuta. Las instrucciones se hacen antes de llamar. | La llamada es lo primero. El resto se ejecuta a la vuelta, en orden inverso. | Hay instrucciones antes y después de la llamada. |

| Múltiple | Anidada | |
|---|---|---|
| Hay más de una llamada recursiva en el mismo subprograma (ej.: Fibonacci). | Un parámetro de la llamada es otra llamada recursiva (ej.: Ackermann). | **Vamos a ver un ejemplo simple de cada una.** |

---

## 6 · De cola y de cabeza — Mismo procedimiento, distinto orden

*DE COLA Y DE CABEZA*

**DE COLA**

```
Procedimiento Cuenta(n: entero);
Proceso
    SI n > 0 ENTONCES
        Escribir(n);
        Cuenta(n - 1);
    FIN_SI;
Fin;
```

Salida de Cuenta(3)

```
3   2   1
```

**DE CABEZA**

```
Procedimiento Cuenta(n: entero);
Proceso
    SI n > 0 ENTONCES
        Cuenta(n - 1);
        Escribir(n);
    FIN_SI;
Fin;
```

Salida de Cuenta(3)

```
1   2   3
```

---

## 7 · De cola y de cabeza *(ampliación de la diapositiva 6)*

**DE COLA**

```
Procedimiento Cuenta(n: entero);
Proceso
    SI n > 0 ENTONCES
        Escribir(n);
        Cuenta(n - 1);
    FIN_SI;
Fin;
```

Salida de Cuenta(3): `3   2   1`

**DE CABEZA**

```
Procedimiento Cuenta(n: entero);
Proceso
    SI n > 0 ENTONCES
        Cuenta(n - 1);
        Escribir(n);
    FIN_SI;
Fin;
```

Salida de Cuenta(3): `1   2   3`

*(En la ampliación, por el tamaño de letra, la cabecera queda cortada en dos renglones: `Procedimiento Cuenta(n:` / `entero);`.)*

---

## 8 · De cabeza — ¿Por qué sale 1 2 3?

*DE CABEZA*

```
IDA: nadie escribe todavía                         VUELTA: se escribe

Cuenta(3)  pendiente: Escribir(3)                  vuelve a Cuenta(1)   →  1
  ↘
    Cuenta(2)  pendiente: Escribir(2)              vuelve a Cuenta(2)   →  2
      ↘
        Cuenta(1)  pendiente: Escribir(1)          vuelve a Cuenta(3)   →  3
          ↘
            Cuenta(0)  no hace nada
```

> [!tip] Regla práctica
> lo que está ANTES de la llamada se ejecuta a la ida; lo que está DESPUÉS, a la vuelta (en orden inverso).

---

## 9 · Intermedia — Instrucciones antes y después de la llamada

*INTERMEDIA*

```
Procedimiento Espejo(n: entero);
Proceso
    SI n > 0 ENTONCES
        Escribir(n);
        Espejo(n - 1);
        Escribir(n);
    FIN_SI;
Fin;
```

Salida de Espejo(3)

```
3 2 1 1 2 3
```

| A la ida | A la vuelta |
|---|---|
| Escribir(n) antes de llamar: 3 2 1 | Escribir(n) después: 1 2 3 |

> [!info] Sale como un espejo
> la mitad de ida y la mitad de vuelta.

---

## 10 · Intermedia *(ampliación de la diapositiva 8)*

```
Procedimiento Espejo(n: entero);
Proceso
    SI n > 0 ENTONCES
        Escribir(n);
        Espejo(n - 1);
        Escribir(n);
    FIN_SI;
Fin;
```

Salida de Espejo(3): `3 2 1 1 2 3`

| A la ida | A la vuelta |
|---|---|
| Escribir(n) antes de llamar: 3 2 1 | Escribir(n) después: 1 2 3 |

---

## 11 · Múltiple — Fibonacci: dos llamadas recursivas

*MÚLTIPLE*

**`0, 1, 1, 2, 3, 5, 8, 13, 21, …`**

```
Funcion Fibo(n: entero): entero;
Proceso
    SI (n = 0) O (n = 1) ENTONCES
        Fibo := n;
    CONTRARIO
        Fibo := Fibo(n - 1) + Fibo(n - 2);
    FIN_SI;
Fin;
```

> [!tip] Dos casos base
> Fibo(0) = 0 y Fibo(1) = 1

**Dos llamadas**
Cada llamada genera otras dos: se forma un árbol.

---

## 12 · Múltiple — Árbol de llamadas de Fibo(4)

*MÚLTIPLE*

```
                          Fibo(4)
                 ┌───────────┴───────────┐
              Fibo(3)                 [Fibo(2)]
           ┌─────┴─────┐            ┌─────┴─────┐
       [Fibo(2)]    (Fibo(1))   (Fibo(1))    (Fibo(0))
       ┌───┴───┐
   (Fibo(1)) (Fibo(0))

   ( ) caso base          [ ] cálculo repetido
```

*(En la filmina los casos base están en naranja y los cálculos repetidos —las dos Fibo(2)— en bordó.)*

> [!warning] 9 llamadas para Fibo(4).
> Fibo(2) se calcula 2 veces. Es elegante, pero repite trabajo.

---

## 13 · Anidada — Una llamada como parámetro de otra

*ANIDADA*

```
Funcion Ack(m, n: entero): entero;
Proceso
    SI m = 0 ENTONCES
        Ack := n + 1;
    CONTRARIO
        SI n = 0 ENTONCES
            Ack := Ack(m - 1, 1);
        CONTRARIO
            Ack := Ack(m - 1, Ack(m, n - 1));
        FIN_SI;
    FIN_SI;
Fin;
```

**La forma**
Ack(m - 1, Ack(m, n - 1)): para poder llamar, primero hay que resolver otra llamada.

> [!info] Sólo para reconocerla
> Es el ejemplo clásico (función de Ackermann). Crece muy rápido.

---

## 14 · Ejemplos con números — Contar los dígitos de un número

*EJEMPLOS CON NÚMEROS*

```
Funcion ContarDig(num: entero): entero;
Proceso
    SI num < 10 ENTONCES
        ContarDig := 1;
    CONTRARIO
        ContarDig := 1 + ContarDig(num DIV 10);
    FIN_SI;
Fin;
```

> [!tip] Recordá
> 352 DIV 10 = 35 · 352 MOD 10 = 2

**Caso base**
Un número de un solo dígito (num < 10) tiene 1 dígito.

**Cambio de estado**
num DIV 10 quita el último dígito.

---

## 15 · Contar los dígitos *(ampliación de la diapositiva 12)*

```
Funcion ContarDig(num: entero): entero;
Proceso
    SI num < 10 ENTONCES
        ContarDig := 1;
    CONTRARIO
        ContarDig := 1 + ContarDig(num DIV 10);
    FIN_SI;
Fin;
```

---

## 16 · Ejecución paso a paso — ContarDig(352)

*EJECUCIÓN PASO A PASO*

```
IDA                                              VUELTA

ContarDig(352) = 1 + ContarDig(35)               ContarDig(3) = 1
  ↘                                                ↘
    ContarDig(35) = 1 + ContarDig(3)                 ContarDig(35) = 1 + 1 = 2
      ↘                                                ↘
        ContarDig(3) = 1                                 ContarDig(352) = 1 + 2 = 3
```

```
┌───┬───┬───┐
│ 3 │ 5 │ 2 │   ← cada llamada quita el último dígito
└───┴───┴───┘
```

---

## 17 · Ejemplos con números — Sumar los dígitos de un número

*EJEMPLOS CON NÚMEROS*

```
Funcion SumarDig(num: entero): entero;
Proceso
    SI num = 0 ENTONCES
        SumarDig := 0;
    CONTRARIO
        SumarDig := (num MOD 10) + SumarDig(num DIV 10);
    FIN_SI;
Fin;
```

**Comparar**
Igual que ContarDig, cambia lo que se suma.

**SumarDig(352)**

```
= 2 + SumarDig(35) = 2 + 5 + SumarDig(3) = 2 + 5 + 3 + 0 = 10
```

---

## 18 · Sumar los dígitos *(ampliación de la diapositiva 14)*

```
Funcion SumarDig(num: entero): entero;
Proceso
    SI num = 0 ENTONCES
        SumarDig := 0;
    CONTRARIO
        SumarDig := (num MOD 10) + SumarDig(num DIV 10);
    FIN_SI;
Fin;
```

---

## 19 · Recursividad con arreglos — Sumar los elementos de un arreglo

*RECURSIVIDAD CON ARREGLOS*

```
Ambiente
    V: ARREGLO[1..5] de entero;

Funcion SumarVec(i: entero): entero;
Proceso
    SI i > 5 ENTONCES
        SumarVec := 0;
    CONTRARIO
        SumarVec := V[i] + SumarVec(i + 1);
    FIN_SI;
Fin;
```

> [!tip] Idea
> la suma del arreglo desde i es V[i] más la suma del resto (desde i + 1).

**Invocación**
total := SumarVec(1);

---

## 20 · Sumar los elementos *(ampliación de la diapositiva 15)*

```
Ambiente
    V: ARREGLO[1..5] de entero;

Funcion SumarVec(i: entero): entero;
Proceso
    SI i > 5 ENTONCES
        SumarVec := 0;
    CONTRARIO
        SumarVec := V[i] + SumarVec(i + 1);
    FIN_SI;
Fin;
```

---

## 21 · Ejecución paso a paso — SumarVec(1) con V = [4, 7, 1, 8, 5]

*EJECUCIÓN PASO A PASO*

```
┌───┬───┬───┬───┬───┐
│ 4 │ 7 │ 1 │ 8 │ 5 │  i →
└───┴───┴───┴───┴───┘
  1   2   3   4   5

SumarVec(1) = 4 + SumarVec(2)
  SumarVec(2) = 7 + SumarVec(3)
    SumarVec(3) = 1 + SumarVec(4)
      SumarVec(4) = 8 + SumarVec(5)
        SumarVec(5) = 5 + SumarVec(6)
          SumarVec(6) = 0   (i > 5)
```

**A la vuelta**

```
5 + 0 = 5
8 + 5 = 13
1 + 13 = 14
7 + 14 = 21
4 + 21 = 25
```

> [!important] Resultado: 25

---

## 22 · Recursividad con arreglos — Mostrar el arreglo: en orden e invertido

*RECURSIVIDAD CON ARREGLOS*

**EN ORDEN (de cola)**

```
Procedimiento Mostrar(i: entero);
Proceso
    SI i <= 5 ENTONCES
        Escribir(V[i]);
        Mostrar(i + 1);
    FIN_SI;
Fin;
```

Mostrar(1) con V = [4, 7, 1, 8, 5]

```
4   7   1   8   5
```

**INVERTIDO (de cabeza)**

```
Procedimiento Invertido(i: entero);
Proceso
    SI i <= 5 ENTONCES
        Invertido(i + 1);
        Escribir(V[i]);
    FIN_SI;
Fin;
```

Invertido(1)

```
5   8   1   7   4
```

---

## 23 · Recursividad con arreglos — Búsqueda binaria recursiva (Parte 1/2)

*RECURSIVIDAD CON ARREGLOS*

```
Funcion BusBin(x, izq, der: entero): entero;
Ambiente
    medio: entero;
Proceso
    SI izq > der ENTONCES
        BusBin := 0;
    CONTRARIO
        medio := (izq + der) DIV 2;
        SI V[medio] = x ENTONCES
            BusBin := medio;
        CONTRARIO   { sigue en Parte 2 }
```

> [!tip] Caso base 1
> izq > der: no quedan elementos → 0

> [!tip] Caso base 2
> V[medio] = x: lo encontré → medio

---

## 24 · Recursividad con arreglos — Búsqueda binaria recursiva (Parte 2/2)

*RECURSIVIDAD CON ARREGLOS*

```
        { viene de Parte 1 }
        CONTRARIO
            SI x < V[medio] ENTONCES
                BusBin := BusBin(x, izq, medio - 1);
            CONTRARIO
                BusBin := BusBin(x, medio + 1, der);
            FIN_SI;
        FIN_SI;
    FIN_SI;
Fin;
```

> [!info] Nota de transcripción
> El `CONTRARIO` del comienzo de la Parte 2 es el mismo con que termina la Parte 1 (la filmina lo repite para dar contexto): en la función completa aparece una sola vez.

**Mitad izquierda**
x < V[medio]: buscar en [izq, medio − 1]

**Mitad derecha**
x > V[medio]: buscar en [medio + 1, der]

**Invocación:** pos := BusBin(x, 1, 7);

---

## 25 · Ejecución paso a paso — BusBin(21, 1, 7) con V ordenado

*EJECUCIÓN PASO A PASO*

| Llamada | V[1] | V[2] | V[3] | V[4] | V[5] | V[6] | V[7] | |
|---|---|---|---|---|---|---|---|---|
| **BusBin(21, 1, 7)** | 3 | 8 | 12 | **[15]** | 21 | 30 | 42 | medio = 4 · V[4] = 15 < 21 → derecha |
| **BusBin(21, 5, 7)** | ~~3~~ | ~~8~~ | ~~12~~ | ~~15~~ | 21 | **[30]** | 42 | medio = 6 · V[6] = 30 > 21 → izquierda |
| **BusBin(21, 5, 5)** | ~~3~~ | ~~8~~ | ~~12~~ | ~~15~~ | **[21]** | ~~30~~ | ~~42~~ | medio = 5 · V[5] = 21 → ¡encontrado! |

*(En la filmina el elemento `medio` está resaltado en naranja —acá entre corchetes— y las posiciones que ya quedaron fuera del intervalo aparecen en gris —acá tachadas—.)*

> [!important] Resultado
> BusBin devuelve 5 (la posición de 21).

---

## 26 · Comparación — Iteración vs recursión

*COMPARACIÓN*

| Aspecto | Iteración | Recursión |
|---|---|---|
| **Repetición** | Ciclo explícito (PARA, MIENTRAS, REPETIR) | Repetidas invocaciones a la subacción |
| **Terminación** | La condición del ciclo deja de cumplirse | Se llega al caso base |
| **Memoria** | Sólo las variables del ciclo | Un registro de activación por llamada (pila) |
| **Velocidad** | Generalmente más rápida | Más lenta: costo de cada llamada |
| **Legibilidad** | Puede ser más larga | Muy cercana a la definición matemática |

---

## 27 · Criterio — ¿Cuándo conviene usar recursividad?

*CRITERIO*

| CONVIENE | NO CONVIENE |
|---|---|
| • El problema se define en forma recursiva (factorial, potencia). | • Si la velocidad es importante: la iteración suele ser más rápida. |
| • La solución queda más corta y legible. | • Si la memoria (pila) es limitada. |
| • Estructuras recursivas: listas, árboles (los vamos a ver). | • Si recalcula lo mismo muchas veces (Fibonacci). |

> [!important] La recursividad se usa cuando realmente es necesaria: cuando no existe una solución iterativa simple.

---

## 28 · A resolver — Problemas propuestos

*A RESOLVER*

| 1 · Longitud de una lista | 2 · Sumatoria de x a y | 3 · Buscar en un arreglo |
|---|---|---|
| Función recursiva que devuelva la cantidad de nodos de una lista simplemente enlazada. | Función recursiva que sume los enteros de x a y, incluidos los extremos. | Función recursiva que indique si un elemento x está en un arreglo de 10 enteros. |

> [!question] Para cada uno
> ¿cuál es el caso base? ¿cómo se achica el problema?

---

## 29 · Solución · Problema 1 — Longitud de una lista

*SOLUCIÓN · PROBLEMA 1*

```
Funcion Longitud(p: puntero a nodo): entero;
Proceso
    SI p = NILL ENTONCES
        Longitud := 0;
    CONTRARIO
        Longitud := 1 + Longitud(*p.sig);
    FIN_SI;
Fin;
```

```
┌───┬───┐     ┌───┬───┐     ┌───┬───┐
│ 5 │ ──┼────►│ 9 │ ──┼────►│ 2 │ ──┼────► NILL
└───┴───┘     └───┴───┘     └───┴───┘
```

**Longitud = 1 + 1 + 1 + 0 = 3**

> [!tip] Caso base
> Lista vacía: p = NILL → 0

**Más pequeño**
*p.sig es la lista sin el primer nodo.

---

## 30 · Longitud de una lista *(ampliación de la diapositiva 24)*

```
Funcion Longitud(p: puntero a nodo): entero;
Proceso
    SI p = NILL ENTONCES
        Longitud := 0;
    CONTRARIO
        Longitud := 1 + Longitud(*p.sig);
    FIN_SI;
Fin;
```

---

## 31 · Solución · Problema 2 — Sumatoria de x a y

*SOLUCIÓN · PROBLEMA 2*

```
Funcion Sumatoria(x, y: entero): entero;
Proceso
    SI x > y ENTONCES
        Sumatoria := 0;
    CONTRARIO
        Sumatoria := x + Sumatoria(x + 1, y);
    FIN_SI;
Fin;
```

**Sumatoria(3, 6)**

```
= 3 + 4 + 5 + 6 + 0 = 18
```

> [!tip] Caso base
> x > y: no quedan números → 0

**Más pequeño**
x + 1: el intervalo se achica de a uno.

---

## 32 · Solución · Problema 3 — Buscar un elemento en un arreglo

*SOLUCIÓN · PROBLEMA 3*

```
Funcion Buscar(x, i: entero): logico;
Proceso
    SI i > 10 ENTONCES
        Buscar := FALSO;
    CONTRARIO
        SI V[i] = x ENTONCES
            Buscar := VERDADERO;
        CONTRARIO
            Buscar := Buscar(x, i + 1);
        FIN_SI;
    FIN_SI;
Fin;
```

> [!tip] Dos casos base
> i > 10: se terminó el arreglo → FALSO.
> V[i] = x: lo encontré → VERDADERO.

**Más pequeño**
i + 1: queda un elemento menos por revisar.

---

## 33 · Cierre de recursividad — Lo que tenemos que llevarnos

*CIERRE DE RECURSIVIDAD*

1. Directa (se llama a sí misma) o indirecta (A llama a B y B a A).
2. Lo que está antes de la llamada se hace a la ida; lo que está después, a la vuelta.
3. Múltiple (Fibonacci) es elegante pero puede repetir muchísimo trabajo.
4. Con arreglos, un índice que avanza es el cambio de estado; el caso base, el fin del arreglo.
5. Usar recursión cuando no existe una solución iterativa simple.

---

Viene de [[10 — Recursividad (Concepto)]]
