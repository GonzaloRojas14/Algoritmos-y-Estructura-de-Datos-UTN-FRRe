**Fecha de inicio:** 25-10-2024 - Algoritmos I
---
**Tags:** #Completed     #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Genere un algoritmo que recorra una secuencia texto y genere una lista simplemente encadenada con la frecuencia de utilización de cada letra. La lista debe mantenerse ordenada alfabéticamente y al final informar cual fue la frecuencia de cada letra y cuáles fueron la de mayor y menor frecuencia.
## Resolución
``` less
Accion Guía-Ejercicio_4.7 Es
    Ambiente
        Letras = Registro
            Letra:(A...Z)
            cant:N(3)
            frec:N(3)
            Prox: Puntero a Letras
        finRegistro
        Punt,Ant,Prim:Puntero a Letras
        Cont_Letras:N
        Abecedario:("A"..."Z")
        i:Abecedario
        SEC:Secuencia de Caracter
        V:Caracter
        Procedimiento Inicio() Es
            Prim:=Null
            
            Para i:= "A" Hasta "Z" Hacer
                Nuevo(Punt)
                *Punt.Letra := i
                *Punt.cant := 0
                *Punt.frec := 0
                *Punt.Prox := Null
                Si Prim = Null Entonces
                    Prim := Punt
                Sino
                    *Ant.Prox := Punt
                FinSi
                Ant := Punt
                finSi
            finPara
        finProcedimiento
        Procedimiento Tratar_Caracer(Car:Caracter) Es
            Punt:=Prim
            Para i:="A" Hasta Car Hacer
                Ant:=Punt
                Punt:=*Punt.Prox
            finPara
            *Ant.cant:=*Ant.cant+1
            Cont_Letras:=Cont_Letras+1
        finProcedimiento


    finAmbiente
    Proceso
        ARR(SEC)
        AVZ(SEC,V);Cont_Letras:=0
        Inicio()
        Mientras NFDS(SEC) Hacer
            Si V Esiste en Abecedario Hacer
                Tratar_Caracer(V)
            finSi
            AVZ(SEC,V)
        finMientras
        Punt:=Prim
        Mientras Punt<>Null Hacer
            *Punt.frec:=(*Punt.cant * 100)/Cont_Letras
            Punt:=*Punt.Prox
        finMientras
    finProceso
finAccion
```
## Relaciones

- [[Listas-AlgoritmosI]]
- [[Definición de Registros-AlgoritmosI]]
