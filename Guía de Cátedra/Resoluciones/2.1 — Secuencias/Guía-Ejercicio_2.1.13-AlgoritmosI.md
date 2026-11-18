**Fecha de inicio:** 17-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
A partir del ejercicio anterior, determinar el porcentaje que representan las palabras que comienzan con "ALG" sobre todas las palabras de la secuencia.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.13-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter
        v: Caracter
        cont_palabras, cont_palabras_ALG: Entero
        puntuacion: (" ", ".", ",", ";", ":")
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            cont_palabras:= 0
            cont_palabras_ALG:= 0
        finProcedimiento
        Procedimiento saltarPalabra() Es
            Mientras No(v existe en puntuacion) y NFDS(sec) Hacer
                AVZ(sec, v)
            finMientras
        finProcedimiento
        
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si v existe en puntuacion Entonces
                AVZ(sec, v)
            Sino
                cont_palabras := cont_palabras + 1     
                Si v = "A" Entonces
                    AVZ(sec,v) 
                    Si v = "L" Entonces
                        AVZ(sec, v)
                        Si v = "G" Entonces
                            AVZ(sec,v)
                            cont_palabras_ALG := cont_palabras_ALG + 1
                            Escribir("La siguiente palabra empieza por ALG:")
                            Escribir("ALG") 
                            Mientras No(v existe en puntuacion) y NFDS(sec) Hacer
                                Escribir(v)
                                AVZ(sec, v)
                            finMientras
                            Si No(v existe en puntuacion) Entonces
                                Escribir(v)
                            finSi
                        Sino
                            saltarPalabra()
                        finSi
                    Sino
                        saltarPalabra()
                    finSi
                Sino
                    saltarPalabra()
                finSi
            finSi
        finMientras
        Si cont_palabras > 0 Entonces
            Escribir("El porcentaje de palabras que empiezan por ALG es:", (cont_palabras_ALG * 100) / cont_palabras, "%")  
        Sino
            Escribir("La secuencia estaba vacía o no contenía palabras.")
        finSi
        Cerrar(sec)    
    finProceso
finAccion
```
## Relaciones


