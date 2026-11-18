

**Fecha de inicio:** 25-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dado un vector de 10 números enteros, calcular la suma de sus elementos
## Resolución
``` less
Accion Guia-Ejercicio-5.1.8 Es
    Ambiente
        vect: Arreglo[1..10] de Enteros
        Funcion Suma(arr:Arreglo de Enteros, Pos:Numero):Numero Es
            Si Pos=10 Hacer
                Suma:=arr[Pos]
            SiNo
                Suma:=arr[Pos]+Suma(arr, Pos+1)
            finSi
        finFuncion
    finAmbiente
    Proceso
        Cargar(vect)
        Escribir("La suma de ss elementos da:",Suma(vect,1))
    finProceso
finAccion
```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

