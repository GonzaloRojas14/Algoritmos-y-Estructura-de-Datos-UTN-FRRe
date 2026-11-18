

**Fecha de inicio:** 25-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Imprimir las cifras de un número $n$ (siendo $n≥0$) en orden inverso al original. Por ej.: el inverso de 254 es 452.
## Resolución
``` less
Accion Guia-Ejercicio-5.2.1 Es
    Ambiente
        Procedimiento NumeroInverso (num:Numero) Es
            Si (num DIV 10)=0 Hacer
                Escribir(num)
            SiNo
                Escribir(num MOD 10)
                NumeroInverso(num DIV 10)
            finSi
        finProcedimiento
        numero:Numero
    finAmbiente
    Proceso
    numero:=232
    NumeroInverso(numero)
    finProceso
finAccion
```
## Relaciones

- [[Recursividad-Introduccion-AlgoritmosI]]
