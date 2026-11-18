**Fecha de inicio:** 17-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada una secuencia de caracteres, determinar la cantidad de palabras de 4 caracteres (letras)
## Resolución
``` less
Accion Guía-Ejercicio_2.1.11-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter
        v: Caracter
        cont, cont_palabras: Entero
        puntuacion: (" ", ".", ",", ";", ":")
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            cont:= 0
            cont_palabras:= 0
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si v existe en puntuacion Entonces
                AVZ(sec, v)
            Sino
                cont:= 0
                Mientras No(v existe en puntuacion) y NFDS(sec) Hacer
                    cont:= cont + 1
                    AVZ(sec, v)
                finMientras 
                Si  No(v existe en puntuacion) Entonces
                    cont:= cont + 1
                finSi
                Si cont = 4 Entonces
                    cont_palabras:= cont_palabras + 1
                finSi
            finSi
        finMientras
        Escribir("La cantidad de palabras con 4 letras es de:", cont_palabras)    
        Cerrar(sec)    
    finProceso
finAccion
```
## Relaciones


