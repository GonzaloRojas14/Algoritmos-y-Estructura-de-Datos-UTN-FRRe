**Fecha de inicio:** 15-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Dados dos números enteros, divídalos (división entera) y muestre el resultado, usando sólo la operación resta.
## Resolución
``` less
Accion Guia-Ejercicio-5.1.4 Es
    dividendo, divisor: Numero
    Ambiente
        Funcion Division(Dividendo:Numero, Divisor:Numero):Numero Es
            Si Divisor = 0 Entonces
                Escribir("Error: División por cero")
                Division := 0
            SiNo
                Si Dividendo < Divisor Entonces
                    Division := 0
                SiNo
                    Division := 1 + Division(Dividendo - Divisor, Divisor)
                finSi
            finSi
        finFuncion
    finAmbiente
    Proceso
        dividendo := 18
        divisor := 3
        Escribir("El resultado de la division entera entre ", dividendo, " y ", divisor, " es: ", Division(dividendo, divisor))
    finProceso
finAccion

```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]
