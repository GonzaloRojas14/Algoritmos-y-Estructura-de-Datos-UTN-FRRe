**Fecha de inicio:** 13-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de caracteres. Se desea determinar la cantidad de palabras que comienzan con la letra 'I'.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.9-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter
        v: Caracter
        cont: Entero
        primerLetra: Booleano
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            cont:= 0
            primerLetra:= Verdadero
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Mientras v <> " " y NFDS(sec) Hacer
                Si primerLetra y v="I" Entonces
                    cont:= cont +1
                    primerLetra:= Falso
                Sino
                    primerLetra:= Falso
                finSi
                AVZ(sec, v)
            finMientras
            primerLetra:= Verdadero
            Si v = " " y NFDS(sec) Entonces
                AVZ(sec, v)
            finSi
        finMientras
        Si primerLetra y v = "I" Entonces
            cont:= cont + 1
        finSi
        Cerrar(sec)
        Escribir("La cantidad de palabras que empiezan con I son:", cont)
    finProceso
finAccion
```
## Relaciones


