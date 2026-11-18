**Fecha de inicio:** 19-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
El siguiente es un ejercicio del primer parcial del año 2017: La empresa TICKET-TEC ha generado una secuencia de caracteres con información de sus ventas para los eventos de los últimos 3 meses, cuya estructura se describe a continuación. Inicialmente existe el nombre del local de los eventos, cuya longitud se desconoce, termina con un #; a continuación se tiene la información de todos los tickets vendidos para ese local, separado cada ticket del siguiente con el caracter !, y al final de todas las ventas para ese local, el caracter &. Por último la marca de fin de secuencia. También en el caso de butaca se desconoce la longitud del número, termina con un guión.

**EJEMPLO**  
`Teatro Opera#270520171A45-2030!270520173D120-2230!280520172C233-2030!&Galpon de las Luces#070720171C5-2030!301020172A233-2230!&{fin}`

`local de eventos#Fecha del evento[ddmmaaaa] codigo del evento[1..3] butaca [sector [A,C o D], número] - horario evento [hhmm]!`

Solo hay dos horarios 20:30 y 22:30.

La empresa solicita un algoritmo que cumpla con las siguientes consignas:

1. Generar una nueva secuencia de salida con el mismo formato, que contenga los tickets correspondientes a un mes ingresado por el usuario.
    
2. Informar total general de tickets vendidos, total de tickets por evento y porcentaje de cada uno sobre el total general.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.31-AlgoritmosI Es
    Ambiente
        sec, sec_salida: Secuencia de Caracter
        v: Caracter
        mes_usuario: Entero 
        total, total_2030, total_2230, dia, mes: Entero

        Procedimiento inicializar() Es
            ARR(sec); CREAR(sec_salida)
            AVZ(sec, v)
            total:= 0; total_2030:= 0; total_2230:= 0
            dia:= 0; mes:= 0
            Escribir("Ingresa el mes a analizar del 1 al 12:")
            Leer(mes_usuario)
        finProcedimiento
        
        Funcion ANaN(): Entero Es
            Ambiente
                num, j: Entero 
            finAmbiente
            num:= 0; ANaN:= 0
            Para j:= 1 Hasta 0 Paso -1 Hacer 
                Segun v Hacer
                    = "0": num:= 0
                    = "1": num:= 1
                    = "2": num:= 2
                    = "3": num:= 3
                    = "4": num:= 4
                    = "5": num:= 5
                    = "6": num:= 6
                    = "7": num:= 7
                    = "8": num:= 8
                    = "9": num:= 9 
                finSegun
                ANaN:= ANaN + num*(10**j)
                AVZ(sec, v)
            finPara
        finFuncion

        Procedimiento grabarDiaMes(D: Entero, M: Entero) Es
            Ambiente
                num, j: Entero
            finAmbiente
            Para j:= 1 Hasta 0 Paso -1 Hacer
                num:= (D DIV 10**j) MOD 10
                Segun num Hacer 
                    = 0: GRABAR(sec_salida, "0") 
                    = 1: GRABAR(sec_salida, "1") 
                    = 2: GRABAR(sec_salida, "2") 
                    = 3: GRABAR(sec_salida, "3") 
                    = 4: GRABAR(sec_salida, "4") 
                    = 5: GRABAR(sec_salida, "5") 
                    = 6: GRABAR(sec_salida, "6") 
                    = 7: GRABAR(sec_salida, "7") 
                    = 8: GRABAR(sec_salida, "8") 
                    = 9: GRABAR(sec_salida, "9")
                finSegun
            finPara
            Para j:= 1 Hasta 0 Paso -1 Hacer
                num:= (M DIV 10**j) MOD 10
                Segun num Hacer 
                    = 0: GRABAR(sec_salida, "0") 
                    = 1: GRABAR(sec_salida, "1") 
                    = 2: GRABAR(sec_salida, "2") 
                    = 3: GRABAR(sec_salida, "3") 
                    = 4: GRABAR(sec_salida, "4") 
                    = 5: GRABAR(sec_salida, "5") 
                    = 6: GRABAR(sec_salida, "6") 
                    = 7: GRABAR(sec_salida, "7") 
                    = 8: GRABAR(sec_salida, "8") 
                    = 9: GRABAR(sec_salida, "9")
                finSegun
            finPara
        finProcedimiento

        Procedimiento grabarLocal() Es
            Mientras v <> "#" y NFDS(sec) Hacer
                GRABAR(sec_salida, v)
                AVZ(sec, v)
            finMientras
            Si v = "#" Entonces
                GRABAR(sec_salida, v)
                AVZ(sec, v)
            finSi
        finProcedimiento

    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            grabarLocal()
            
            Mientras v <> "&" Hacer
                total:= total + 1
                dia:= ANaN()
                mes:= ANaN()
                
                Si mes = mes_usuario Entonces
                    grabarDiaMes(dia, mes)
                    Mientras v <> "-" Hacer
                        GRABAR(sec_salida, v)
                        AVZ(sec, v)
                    finMientras
                    
                    GRABAR(sec_salida, v); AVZ(sec, v) 
                    GRABAR(sec_salida, v); AVZ(sec, v) 
                    GRABAR(sec_salida, v) 
                    
                    Si v = "0" Entonces
                        total_2030:= total_2030 + 1
                    SiNo
                        total_2230:= total_2230 + 1
                    finSi
                    
                    AVZ(sec, v)
                    GRABAR(sec_salida, v); AVZ(sec, v) // grabamos 3
                    GRABAR(sec_salida, v); AVZ(sec, v) // grabamos 0
                    GRABAR(sec_salida, v); AVZ(sec, v) // grabamos !
                SiNo
                    Mientras v <> "-" Hacer
                        AVZ(sec, v)
                    finMientras
                    
                    AVZ(sec, v) // saltamos guion
                    AVZ(sec, v) // saltamos 1er 2
                    
                    Si v = "0" Entonces
                        total_2030:= total_2030 + 1
                    SiNo
                        total_2230:= total_2230 + 1
                    finSi
                    
                    AVZ(sec, v) // saltamos digito variable
                    AVZ(sec, v) // saltamos 3
                    AVZ(sec, v) // saltamos 0
                    AVZ(sec, v) // saltamos !
                finSi
            finMientras
            Si v = "&" Entonces
                GRABAR(sec_salida, v)
                Si NFDS(sec) Entonces
                    AVZ(sec, v)
                finSi
            finSi

        finMientras

        Si total > 0 Entonces
            Escribir("El total de tickets vendidos es: ", total)
            Escribir("Tickets para las 20:30: ", total_2030, ", porcentaje del total: ", (total_2030 * 100) / total, "%")       
            Escribir("Tickets para las 22:30: ", total_2230, ", porcentaje del total: ", (total_2230 * 100) / total, "%") 
        SiNo
            Escribir("No se registraron ventas en la secuencia.")
        finSi
        
        Cerrar(sec); Cerrar(sec_salida)
    finProceso
finAccion
```
## Relaciones


