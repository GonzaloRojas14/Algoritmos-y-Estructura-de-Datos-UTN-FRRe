

**Fecha de inicio:** 20-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se posee una secuencia con los mensajes internos enviados entre los empleados de una empresa, la secuencia está formada de la siguiente manera: 3 caracteres para el destino, 3 caracteres para el origen, 3 caracteres que indican la cantidad de caracteres que tiene el mensaje y el mensaje. No existe ningún carácter que separe un mensaje de otro. se pide:

1. Escribir una secuencia de salida con todos los mensajes (incluyendo origen y destino) que van hacia el área de Mantenimiento (que destino comience con 1).
2. Contar la cantidad de mensajes que se dirigen hacia el área de sistemas (que destino comience con 23).
## Resolución
``` less
Accion Guía-Ejercicio_2.1.32-AlgoritmosI Es
    Ambiente
        sec, sec_salida: Secuencia de Caracter
        v: Caracter
        resguardo,i , cont: Entero
        
        Procedimiento inicializar() Es
            ARR(sec); CREAR(sec_salida)
            AVZ(sec, v)
            cont:= 0; i:= 0; resguardo:= 0
        finProcedimiento
        Procedimiento grabar_cantidad(num: Entero) Es
            Para i:=1 Hasta num Hacer
                GRABAR(sec_salida, v)
                Si NFDS(sec) Entonces
                    AVZ(sec, v)
                finSi
            finPara
        finProcedimiento
        Procedimiento avanzar_cantidad(num: Entero) Es
            Para i:=1 Hasta num Hacer
                Si NFDS(sec) Entonces
                    AVZ(sec, v)
                finSi
            finPara
        finProcedimiento
        Funcion ANaN(num: Entero): Entero Es
            ANaN:= 0
            Para i:=(num-1) Hasta 0, Paso -1 Hacer
                Segun v Hacer
                    = "0": ANaN:= ANaN + 0*(10**i)
                    = "1": ANaN:= ANaN + 1*(10**i)
                    = "2": ANaN:= ANaN + 2*(10**i)
                    = "3": ANaN:= ANaN + 3*(10**i)
                    = "4": ANaN:= ANaN + 4*(10**i)
                    = "5": ANaN:= ANaN + 5*(10**i)
                    = "6": ANaN:= ANaN + 6*(10**i)
                    = "7": ANaN:= ANaN + 7*(10**i)
                    = "8": ANaN:= ANaN + 8*(10**i)
                    = "9": ANaN:= ANaN + 9*(10**i)                    
                finSegun
                AVZ(sec, v)
            finPara
        finFuncion

        Funcion NaAN(num: Entero): Caracter Es
            Segun num Hacer
                = 0: NaAN:= "0"
                = 1: NaAN:= "1"
                = 2: NaAN:= "2"
                = 3: NaAN:= "3"
                = 4: NaAN:= "4"
                = 5: NaAN:= "5"
                = 6: NaAN:= "6"
                = 7: NaAN:= "7"
                = 8: NaAN:= "8"
                = 9: NaAN:= "9"
            finSegun
        finFuncion


    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec) Hacer
            Si v="1" Entonces
                grabar_cantidad(6)
                resguardo:= ANaN(3)
                GRABAR(sec_salida, NaAN((resguardo DIV 100)MOD 10))
                GRABAR(sec_salida, NaAN((resguardo DIV 10)MOD 10))
                GRABAR(sec_salida, NaAN(resguardo MOD 10))
                grabar_cantidad(resguardo)
            SiNo
                Si ANaN(2) = 23 Entonces
                    cont:= cont + 1
                finSi
                avanzar_cantidad(4)
                avanzar_cantidad(ANaN(3))
            finSi
        finMientras
        Escribir("La cantidad de mensajes dirijidos al area de sistemas es:", cont)
        Cerrar(sec);Cerrar(sec_salida)
    finProceso
finAccion
```
## Relaciones


