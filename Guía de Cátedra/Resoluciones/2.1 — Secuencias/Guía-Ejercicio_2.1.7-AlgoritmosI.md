

**Fecha de inicio:** 13-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se tiene una secuencia de enteros que contiene todos los CUIT de los empleados de una empresa, la misma termina con el CUIT 0. Para evitar largas esperas en los días de pago, la empresa necesita organizarlos de acuerdo al último dígito de su documento, generar una secuencia con los CUIT de las personas que su número de documento termine con 0, 1, 2 o 3
## Resolución
``` less
Accion Guía-Ejercicio_2.1.7-AlgoritmosI Es
    Ambiente
        sec, secSalida: secuencia de Entero
        v: Entero
        
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec,v)
            CREAR(secSalida)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras v <> 0 Hacer
            Si ((v MOD 100)DIV 10) >=0 y ((v MOD 100)DIV 10)<= 3 Entonces
                Grabar(secSalida, v)
            finSi
            AVZ(sec, v)
        finMientras
        Cerrar(secSalida)
        Cerrar(sec)
    finProceso
finAccion

```
## Relaciones
- [[General-Secuencias-AlgoritmosI]]

