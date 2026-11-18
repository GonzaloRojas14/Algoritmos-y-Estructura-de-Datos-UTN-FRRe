

**Fecha de inicio:** 12-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de números de socios, y se desea saber la cantidad de socios que están registrados.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.4-AlgoritmosI Es 
    Ambiente
        sec: secuencia de Entero
        v, cont: Entero 
        Procedimiento inicializar() Es 
            ARR(sec)
            AVZ(sec, v)
            cont:=1
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            cont:= cont + 1
            AVZ(sec, v)
        finMientras
        Escribir("La cantidad de socios es de:", cont)
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones
- [[General-Secuencias-AlgoritmosI]]

