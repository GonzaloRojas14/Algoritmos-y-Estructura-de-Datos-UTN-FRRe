**Fecha de inicio:** 23-10-2024 - Algoritmos I
---
**Tags:** #Completed   #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Dada una lista simplemente encadenada de números diseñar un algoritmo que calcule en forma independiente: La suma de los números impares, y la suma de los números pares.
## Resolución
``` less
Accion Ejercicio_4.3(Prim: Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            dato:Num
            prox:Puntero a Nodo
        FinRegistro
        pares,impares:Num
        Punt:Puntero a Nodo
    finAmbiente
    Proceso
        pares:=0;impares:=0
        Punt:=Prim
        Mientras Punt<>Null Hacer
            Si (*Punt.dato MOD 2)=0 Hacer
                pares:=pares+*Punt.dato
            Sino
                impares:=impares+*Punt.dato
            FinSi
            Punt:=*Punt.prox 
        FinMientras
    finProceso
FinAccion

```
## Relaciones
- [[Listas-AlgoritmosI]]
- [[Definición de Registros-AlgoritmosI]]

