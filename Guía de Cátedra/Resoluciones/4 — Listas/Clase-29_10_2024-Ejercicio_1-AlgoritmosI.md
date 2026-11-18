

**Fecha de inicio:** 30-10-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Usando las operaciones de Lista, escribir un procedimiento AGRUPA (PRIM, ULT: puntero a nodo; A:entero) que, dada una lista doblemente encadenada de enteros L agrupe (sume) elementos de tal manera que en L queden sólo elementos mayores o iguales que A. El algoritmo recorre la lista y cuando encuentra un elemento menor empieza a agrupar (sumar) el elemento con los siguientes hasta llegar al valor A o superarlo; o hasta que se acabe la lista 

Por ejemplo si A= 10 y la lista es:

L = {3,4,2,4,1,4,4,3,2,2,4,1,4,1,4,4,1,4,4,2}, entonces 

AGRUPA(PRIM, ULT,10) da L = {13,12,13,10,10}. 

En la lista final NO deben quedar elementos menores que A, salvo, eventualmente, el último

## Resolución
``` less
Accion Clase-29_10_2024-Ejercicio_1(Prim:Puntero a Nodo, Ult:Puntero a Nodo, A:N) Es
    Ambiente
        Nodo = Registro
            Dato:N
            Prox: Puntero a Nodo
            Ant: Puntero a Nodo
        finRegistro
        Punt, PuntSig, inicio:Puntero a Nodo

        valor:N

        Procedimiento Agrupar() Es
            inicio:=Punt
            valor:=*inicio.Dato
            bandera:=Verdadero   
            
            Mientras valor <= A Y bandera Hacer
                PuntSig:=*inicio.Prox
                valor:=valor+*PuntSig.Dato
                Si PuntSig = Ult Hacer
                    *Prim.Ant:=inicio
                    *inicio.Prox:=Prim
                    bandera:=Falso
                    Ult:=inicio
                SiNo  
                    *inicio.Prox:=*PuntSig.Prox
                    *(*PuntSig.Prox).Ant:=inicio
                
                finSi
                Disponer(PuntSig)
            finMientras
            *inicio.Dato:=valor
            
            
        finProcedimiento

    finAmbiente
    Proceso
        valor:=0
        Punt:=Prim
        Mientras Punt <> Ult Hacer
            Agrupar()
            Si inicio<>Ult
                Punt:=*inicio.Prox
            finSi
        finMientras

    finProceso
finAccion
```
## Relaciones

- [[Listas-AlgoritmosI]]
