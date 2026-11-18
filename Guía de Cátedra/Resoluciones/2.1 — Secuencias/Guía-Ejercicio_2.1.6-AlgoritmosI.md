

**Fecha de inicio:** 13-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada una secuencia de enteros que almacena la cantidad de habitantes de las ciudades capitales de las 23 provincias de la República Argentina, discriminados 4 categorías: menores de 18 años (varones y mujeres) y mayores de 18 años (varones y mujeres). Se pide determinar la población total y los siguientes porcentajes: masculinos, femeninos, mayores de 18 y menores de 18.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.6-AlgoritmosI Es 
    Ambiente
        sec: secuencia de Entero
        v: Entero
        Hmenores,Hmayores,Mmenores,Mmayores, total, i, j: Entero
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            Hmenores:= 0
            Hmayores:= 0
            Mmenores:= 0
            Mmayores:= 0
            total:= 0
        finProcedimiento
        Procedimiento Contar() Es
            Para i:=1 Hasta 4 Hacer
                Segun i Hacer
                    = 1: Hmenores:= Hmenores + v
                    = 2: Mmenores:= Mmenores + v
                    = 3: Hmayores:= Hmayores + v
                    = 4: Mmayores:= Mmayores + v
                finSegun
                AVZ(sec, v)
            finPara
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Para j:=1 Hasta 23 Hacer
            Contar()
        finPara
        total:= Hmenores+Hmayores+Mmenores+Mmayores
        Escribir("La poblacion total es igual a:", total)
        Escribir("El porcentaje de poblacion masculina es:",((Hmenores+Hmayores)*100)/total)
        Escribir("El porcentaje de poblacion femenina es:",((Mmenores+Mmayores)*100)/total)
        Escribir("El porcentaje de poblacion mayor es:",((Hmayores+Mmayores)*100)/total)
        Escribir("El porcentaje de poblacion menor es:",((Mmenores+Hmenores)*100)/total)
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones
- [[General-Secuencias-AlgoritmosI]]
