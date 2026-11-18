

**Fecha de inicio:** 13-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
La secuencia de socios del problema anterior tiene el inconveniente de que los números están ordenados pero no son correlativos. Se desea generar una secuencia que contenga los números de socios que no figuran en la secuencia de socios.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.5-AlgoritmosI Es 
    Ambiente
        sec, secSalida: secuencia de Entero
        v, nro_socio: Entero
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            CREAR(secSalida)
            nro_socio:=1
        finProcedimiento 
    finAmbiente 
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Mientras nro_socio <> v Hacer
                Grabar(secSalida, nro_socio)
                nro_socio:= nro_socio + 1
            finMientras
            nro_socio:= nro_socio + 1
            AVZ(sec, v)
        finMientras
        Mientras nro_socio <> v Hacer
            Grabar(secSalida, nro_socio)
            nro_socio:= nro_socio + 1
        finMientras
        Cerrar(secSalida)
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones
- [[General-Secuencias-AlgoritmosI]]

