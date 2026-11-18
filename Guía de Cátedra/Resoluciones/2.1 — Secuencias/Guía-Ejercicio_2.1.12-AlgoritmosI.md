**Fecha de inicio:** 17-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de caracteres. Se desea listar las palabras que comiencen con "ALG".
## Resolución
``` less
Accion Guía-Ejercicio_2.1.12-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter
        v: Caracter
        puntuacion: (" ", ".", ",", ";", ":")
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
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
                Si v = "A" Entonces
                    AVZ(sec,v) 
                    Si v = "L" Entonces
                        AVZ(sec, v)
                        Si v = "G" Entonces
                            AVZ(sec,v)
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
        Cerrar(sec)    
    finProceso
finAccion
```
## Relaciones


