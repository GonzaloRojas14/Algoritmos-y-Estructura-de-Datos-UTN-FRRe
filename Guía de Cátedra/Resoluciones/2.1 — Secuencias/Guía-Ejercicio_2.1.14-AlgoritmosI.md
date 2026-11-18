**Fecha de inicio:** 17-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de caracteres y se desea saber la cantidad de caracteres (incluidos los espacios) que existen entre una coma y la siguiente. Se debe considerar que puede haber más de un par de comas, y que las subsecuencias inicial y final deben descartarse por no cumplir la condición enunciada. Supóngase que las comas son siempre contiguas al último caracter de la palabra.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.14-AlgoritmosI Es
    Ambiente
        sec: secuencia de Caracter
        v: Caracter
        cont, cont_final: Entero
        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec, v)
            cont:= 0; cont_final:= 0
            Mientras NFDS(sec) y v <> "," Hacer
                AVZ(sec, v)
            finMientras
            Si NFDS(sec) y v = "," Entonces
                AVZ(sec, v)
            finSi
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si v <> "," Entonces
                cont:= cont+1
            SiNo
                cont_final:= cont_final + cont
                cont:= 0
            finSi
            AVZ(sec, v)
        finMientras
        Si v = "," Entonces
            cont_final:= cont_final + cont
        finSi
        Escribir("La cantidad de Caracteres entre comas es de:", cont_final)
        Cerrar(sec)
    finProceso
finAccion
```
## Relaciones


