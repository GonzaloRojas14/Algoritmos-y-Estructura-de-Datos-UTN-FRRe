

**Fecha de inicio:** 15-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
El algoritmo de Euclides para encontrar el `MCD`(máximo común divisor) de dos números enteros positivos (`m` y `n`) se puede definir recursivamente. Algoritmo de Euclides: el `MCD` de dos enteros es el entero mayor que divide a ambos.

|Dividendo|Divisor|Cociente|Resto|
|---|---|---|---|
|m|n|q1|r1|
|n|r1|q2|r2|
|r1|r2|q3|r3|

Cuando el último resto es cero (por ej. r3 = 0), el `MCD` es el último divisor (en ese caso, r2). El algoritmo recursivo se puede definir con los siguientes pasos:

- `MCD (m,n) = n, si n <= m, n divide a m`
- `MCD (m,n) = MCD (n, m), si m < n`
- `MCD (m,n) = MCD (n, resto de m dividio por n)`

Para simplificar el algoritmo considerar que siempre `m > n`
## Resolución
``` less
Accion Guia-Ejercicio-5.1.7 Es
    Ambiente
        Funcion Euclides(num: Numero, div: Numero): Numero
            Si div = 0 Entonces
                Euclides := num
            SiNo
                Euclides := Euclides(div, num MOD div)
            FinSi
        FinFuncion
        dividendo, divisor: Numero
    finAmbiente
    Proceso
        dividendo := 18
        divisor := 3
        Escribir("Máximo común divisor es: ", Euclides(dividendo, divisor))
    FinProceso
FinAccion

```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

