

**Fecha de inicio:** 14-11-2024 - Algoritmos I
---
**Tags:** #Completed    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Calcular el factorial de un número positivo $n$. Tener en cuenta la definición matemática de $n!$:
$$
n! = \begin{cases} 1, & \text{si } n = 0 \\ n \times (n - 1)!, & \text{si } n > 0 \end{cases}
$$
## Resolución

``` Less
Accion Guia-Ejercicio-5.1.1 Es
    Ambiente
        N: Entero
        Funcion FACTORIAL(Num: Entero): Entero Es
            Si Num = 0 Entonces
                FACTORIAL := 1
            SiNo
                FACTORIAL := Num * FACTORIAL(Num - 1)
            finSi
        finFuncion
    finAmbiente
    Proceso
        Escribir("Ingrese el número del que quiere saber el factorial:")
        Leer(N)
        Si N < 0 Entonces
            Escribir("El factorial no está definido para números negativos.")
        SiNo
            Escribir("El factorial de ", N, " es: ", FACTORIAL(N))
        finSi
    finProceso
finAccion
```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

