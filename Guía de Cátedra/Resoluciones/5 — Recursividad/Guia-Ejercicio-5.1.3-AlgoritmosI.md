

**Fecha de inicio:** 14-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Dados dos números: $a$ y $b$. Calcule la potencia $a^b$, usando sólo multiplicaciones sucesivas.
## Resolución
``` less
Accion Guia-Ejercicio-5.1.2 es
    Ambiente
        NumB, NumE:Numero
        Funcion Potencia(B:Numero, E:Numero):Numero Es
            Si E=1 Hacer
                Potencia:=B
            SiNo
                Potencia:=B*Potencia(B,E-1)
            finSi
        finFuncion
    finAmbiente
    Proceso
        Escribir("Escriba la base")
        Leer(NumB)
        Escribir("Escriba el exponente positivo")
        Leer(NumE)
        Si NumE < 0 Entonces
            Escribir("El exponente debe ser un número positivo.")
        SiNo
            Escribir("El resultado de la potencia es: ", Potencia(NumB, NumE))
        finSi
    finProceso
finAccion
```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

