**Fecha de inicio:** 13-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de caracteres. Se desea contar la cantidad de palabras que comienzan con una letra dada.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.10-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter
        v, letra: Caracter
        cont: Entero
        primerLetra: Booleano
        puntuacion: (" ", ".", ",", ";", ":")
        Procedimiento inicializar() Es:
            ARR(sec)
            AVZ(sec, v)
            cont:= 0
            primerLetra:= Verdadero
            Escribir("Ingrese una letra:")
            Leer(letra)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si v existe en puntuacion Entonces
                AVZ(sec, v)
                primerLetra:= Verdadero
            Sino
                Si v = letra y primerLetra Entonces
                    cont:= cont + 1
                    primerLetra:= Falso
                Sino
                    primerLetra:= Falso
                finSi
                AVZ(sec, v)
            finSi
        finMientras
        Si v = letra y primerLetra Entonces
            cont:= cont + 1
            primerLetra:= Falso
        finSi
        Escribir("La cantidad de palabras que empiezan con", letra, " es:", cont)    
        Cerrar(sec)    
    finProceso
finAccion
```
## Relaciones


