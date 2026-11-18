

**Fecha de inicio:** 19-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se desea calcular el costo de un telegrama, que se determina en función del número de palabras (que vale V1 cada una), salvo que el promedio de letras por palabra supere las cinco letras, caso en que cada palabra vale V2.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.17-AlgoritmosI Es
    Ambiente
        sec: Secuencia de Caracter
        v: Caracter
        cont_letras, cont_palabras: Entero
        procesada: Booleano
        puntuacion: (" ", ".", ",", ";", ":")
        V1, V2: Real

        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            cont_letras:= 0
            cont_palabras:= 0
            procesada := Falso
            Escribir("Ingrese la tarifa normal (V1) y la tarifa especial (V2):")
            Leer(V1, V2)
        finProcedimiento
        
        Procedimiento saltarPalabra() Es
            Mientras No(v existe en puntuacion) y NFDS(sec) Hacer
                cont_letras:=cont_letras + 1
                AVZ(sec, v)
            finMientras
            Si No(v existe en puntuacion) Entonces
                cont_letras:= cont_letras + 1
                procesada := Verdadero
            finSi
            cont_palabras:= cont_palabras + 1
        finProcedimiento

    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si No(v existe en puntuacion) Entonces 
                saltarPalabra()
            finSi
            Si v existe en puntuacion y NFDS(sec) Entonces
                AVZ(sec, v)
            finSi
        finMientras
        Si No(v existe en puntuacion) y No(procesada) Entonces
            saltarPalabra()
        finSi
            

        Si cont_palabras > 0 Entonces
            Si (cont_letras / cont_palabras) > 5 Entonces
                Escribir("El telegrama costara: $", cont_palabras * V2)
            Sino
                Escribir("El telegrama costara: $", cont_palabras * V1)
            finSi
        Sino
            Escribir("No se encontraron palabras válidas en la secuencia.")
        finSi
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones


