**Fecha de inicio:** 17-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se desea saber la cantidad promedio de palabras que contienen las oraciones de una secuencia de caracteres. Supóngase que los puntos son siempre contiguos al último caracter de la palabra. La secuencia finaliza con una marca.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.15-AlgoritmosI Es
    Ambiente
        sec: Secuencia de Caracter
        v: Caracter
        cont_oraciones, cont_palabras: Entero
        puntuacion: (" ", ".", ",", ";", ":")

        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            cont_oraciones:= 0
            cont_palabras:= 0
        finProcedimiento
        
        Procedimiento saltarPalabra() Es
            Mientras No(v existe en puntuacion) y v <> "*" Hacer
                AVZ(sec, v)
            finMientras
            cont_palabras:= cont_palabras + 1
        finProcedimiento
        
    finAmbiente
    Proceso
        inicializar()
        Mientras v <> "*" Hacer
            Mientras v <> "." y v <> "*" Hacer
                Si No(v existe en puntuacion) Entonces 
                    saltarPalabra()
                finSi
                Si v <> "." y v <> "*" Entonces
                    AVZ(sec, v)
                finSi
            finMientras
            Si v = "." Entonces
                cont_oraciones:= cont_oraciones + 1
                AVZ(sec, v)
            finSi
        finMientras
        Si cont_oraciones > 0 Entonces
            Escribir("El promedio de palabras por oracion es: ", cont_palabras / cont_oraciones)
        Sino
            Escribir("No se encontraron oraciones válidas en la secuencia.")
        finSi
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones


