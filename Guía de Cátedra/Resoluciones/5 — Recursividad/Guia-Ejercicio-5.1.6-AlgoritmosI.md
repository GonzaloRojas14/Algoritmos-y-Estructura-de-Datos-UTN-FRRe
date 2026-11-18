**Fecha de inicio:** 15-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Determine recursivamente si un número dado es par o impar, usando sólo la operación resta.
## Resolución
``` less
Accion Guia-Ejercicio-5.1.6 Es
    Ambiente
        Valor: Numero
        Funcion Es_Par(Num:Numero):Booleano Es
            Si Num = 0 Entonces
                Es_Par := verdadero
            SiNo
                Si Num = 1 Entonces
                    Es_Par := falso
                SiNo
                    Es_Par := Es_Par(Num - 2)
                finSi
            finSi
        finFuncion
    finAmbiente
    Proceso
        Valor := 7
        Si Es_Par(Valor) Entonces
            Escribir("El número es par")
        SiNo
            Escribir("El número es impar")
        finSi
    finProceso
finAccion


```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

