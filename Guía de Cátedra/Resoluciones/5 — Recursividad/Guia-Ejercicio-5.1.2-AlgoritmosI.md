

**Fecha de inicio:** 14-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Dado un número $n$ como parámetro de entrada, calcular el $n$-ésimo número de la serie de Fibonacci. Tener en cuenta la siguiente definición:
$$
Fib(n)=
\begin{cases}
1, & \text{si } n = 1,n=2 \\ \\
 Fib(n-1)+Fib(n-2),& \text{si }n>2
\end{cases}
$$
## Resolución
``` less
Accion Guia-Ejercicio-5.1.2 Es
    Ambiente
        Num: Numero
        Funcion Fibonacci(N: Numero): Numero Es
            Si N = 1 o N = 2 Entonces
                Fibonacci := 1
            SiNo
                Fibonacci := Fibonacci(N - 1) + Fibonacci(N - 2)
            finSi
        finFuncion
    finAmbiente
    Proceso
        Escribir("Ingresa el número que deseas calcular")
        Leer(Num)
        Si Num > 0 Entonces
            Escribir("Resultado: ", Fibonacci(Num))
        SiNo
            Escribir("El número no es válido")
        finSi
    finProceso
finAccion
```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

