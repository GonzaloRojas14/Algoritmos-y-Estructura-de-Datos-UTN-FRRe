

**Fecha de inicio:** 19-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Escribir un algoritmo que produzca una secuencia de salida que contenga una oración formada por las palabras en posición par de cada oración de una secuencia texto de entrada, que además comienzan con la letra 'M'.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.18-AlgoritmosI Es
    Ambiente
        sec, sec_salida: Secuencia de Caracter
        v: Caracter
        procesada, par, inicio_M: Booleano
        puntuacion: (" ", ".", ",", ";", ":")
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            CREAR(sec_salida)
            procesada := Falso
            par := Falso
            inicio_M := Falso
        finProcedimiento
        Procedimiento saltarPalabra() Es 
            inicio_M:= Falso         
            Si v = "M" Entonces
                inicio_M:= Verdadero
            finSi
            Mientras No(v existe en puntuacion) y NFDS(sec) Hacer
                Si inicio_M y par Entonces
                    GRABAR(sec_salida, v)
                finSi
                AVZ(sec, v)
            finMientras
            Si No(v existe en puntuacion) Entonces
                Si inicio_M y par Entonces
                    GRABAR(sec_salida, v)
                finSi
                procesada:= Verdadero 
            SiNo
                Si inicio_M y par Entonces
                    GRABAR(sec_salida, " ")
                finSi
            finSi
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si No(v existe en puntuacion) Entonces 
                Si par Entonces
                    saltarPalabra()
                    par:= Falso
                SiNo
                    saltarPalabra()
                    par:= Verdadero
                finSi
            finSi
            Si v existe en puntuacion y NFDS(sec) Entonces
                Si v = "." Entonces
                    par := Falso
                finSi 
                AVZ(sec, v)
            finSi
        finMientras
        Si No(v existe en puntuacion) y No(procesada) Entonces
            saltarPalabra()
        finSi
        GRABAR(sec_salida, ".")
        Cerrar(sec_salida)
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones


