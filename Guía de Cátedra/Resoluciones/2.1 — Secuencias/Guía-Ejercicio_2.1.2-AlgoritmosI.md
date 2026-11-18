

**Fecha de inicio:** 12-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada una secuencia de letras del alfabeto que finaliza con la letra "Z", contar cuantas consonantes hay en la secuencia.
## Resolución
```less
Accion Guía-Ejercicio_2.1.2-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter
        v: Caracter
        cont: Entero
        vocales: ("A", "E", "I", "O", "U")
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            cont:= 1
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si No(v existe en vocales) Hacer
                cont:= cont + 1
            finSi
            AVZ(sec, v)
        finMientras
        Escribir("La cantidad de consonantes que hay en la secuencia es:", cont)
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones
- [[General-Secuencias-AlgoritmosI]]

