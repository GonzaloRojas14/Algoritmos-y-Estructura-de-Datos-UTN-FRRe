**Fecha de inicio:** 15-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Construir un algoritmo recursivo que permita determinar si los dígitos de un número nn dado son todos pares.
## Resolución
``` less
Accion Guia-Ejercicio-5.1.4 Es
    Ambiente
        Funcion Son_Digitos_Pares(n:Numero):Booleano Es
            Si n = 0 Entonces
                Son_Digitos_Pares := verdadero  // Caso base: si no hay más dígitos, todos fueron pares
            SiNo
                Si (n MOD 10) MOD 2 <> 0 Entonces
                    Son_Digitos_Pares := falso  // Si el último dígito es impar, retornamos falso
                SiNo
                    Son_Digitos_Pares := Son_Digitos_Pares(n DIV 10)  // Llamada recursiva con el número sin el último dígito
                finSi
            finSi
        finFuncion
    finAmbiente
    Proceso
        Si Son_Digitos_Pares(120) Entonces
            Escribir("Todos los elementos son pares")
        SiNo
            Escribir("Hay un elemento impar")
        finSi
    finProceso    
finAccion

```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

