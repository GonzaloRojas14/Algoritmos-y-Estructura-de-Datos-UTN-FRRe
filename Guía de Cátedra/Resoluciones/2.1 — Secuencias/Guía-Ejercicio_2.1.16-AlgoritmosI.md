**Fecha de inicio:** 17-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de números de DNI asignados a un circuito electoral, generar otra secuencia de números que contenga los DNI múltiplos de 3.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.16-AlgoritmosI Es
    Ambiente
        sec, sec_salida: Secuencia de Entero
        v: Entero
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            CREAR(sec_salida)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si (v MOD 3) = 0 Entonces
                GRABAR(sec_salida, v)
            finSi
            AVZ(sec, v)
        finMientras
        Si (v MOD 3) = 0 Entonces
            GRABAR(sec_salida, v)
        finSi
        Cerrar(sec)
        Cerrar(sec_salida)
    finProceso
finAccion
```
## Relaciones


