**Fecha de inicio:** 13-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

Teniendo en cuenta el ejercicio anterior, se solicita que la secuencia de salida sea una secuencia de caracteres y los CUIT se separen unos de otros con el caracter "-".
## Resolución
``` less
Accion Guía-Ejercicio_2.1.8-AlgoritmosI Es
    Ambiente
        sec: secuencia de Entero
        secSalida: secuencia de Caracter
        v: Entero
        primero: Booleano
        Procedimiento numeroCaracter(num: Entero, cant: Entero) Es
            Ambiente
                digito: Entero 
                j: Entero      
            finAmbiente
            
            
            Para j:= cant-1 Hasta 0 Paso -1 Hacer 
                digito:= (num DIV 10**j) MOD 10
                Segun digito Hacer
                    = 0: Grabar(secSalida, "0")
                    = 1: Grabar(secSalida, "1")
                    = 2: Grabar(secSalida, "2")
                    = 3: Grabar(secSalida, "3")
                    = 4: Grabar(secSalida, "4")
                    = 5: Grabar(secSalida, "5")
                    = 6: Grabar(secSalida, "6")
                    = 7: Grabar(secSalida, "7")
                    = 8: Grabar(secSalida, "8")
                    = 9: Grabar(secSalida, "9")
                finSegun
            finPara
        finProcedimiento

        Procedimiento inicializar() Es
            ARR(sec)
            AVZ(sec,v)
            CREAR(secSalida)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras v <> 0 Hacer
            Si ((v MOD 100)DIV 10) >=0 y ((v MOD 100)DIV 10)<= 3 Entonces
                Si No primero Entonces
                    Grabar(secSalida, "-")
                Sino
                    primero := Falso
                finSi
                numeroCaracter(v, 11)
            finSi
            AVZ(sec, v)
        finMientras
        Cerrar(secSalida)
        Cerrar(sec)
    finProceso
finAccion

```
## Relaciones
