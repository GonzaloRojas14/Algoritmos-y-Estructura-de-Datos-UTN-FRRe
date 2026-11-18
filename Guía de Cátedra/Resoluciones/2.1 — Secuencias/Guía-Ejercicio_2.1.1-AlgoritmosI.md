**Fecha de inicio:** 12-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada una secuencia de letras del alfabeto que finaliza con una marca '\*', contar cuantas letras "A" hay en la secuencia.
## Resolución
``` less
Accion Guia-Ejercicio_2.1.1-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter;
        v: Caracter;
        cont: Entero;
        Procedimiento inicializar():
            ARR(sec);
            AVZ(sec,v);
            cont:= 0;
        finprocedimiento
    finAmbiente
    Proceso
        inicializar();
        Mientras NFDS(sec) Hacer:
            Si v = "A" Entonces:
                cont:= cont + 1
            finSi
            AVZ(sec,v);
        finMientras
        Escribir("El numero de A's en la secuenci es:", cont);
        Cerrar(sec);
    finProceso
finAccion
```
## Relaciones
- [[General-Secuencias-AlgoritmosI]]

