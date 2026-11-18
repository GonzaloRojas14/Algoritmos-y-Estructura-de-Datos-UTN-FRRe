**Fecha de inicio:** 28-10-2024 - Algoritmos I
---
**Tags:** #Completed   #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Escribir un algoritmo que permita buscar, insertar o borrar un elemento identificado con una clave determinada en una lista circular simplemente encadenada.
## Resolución
``` less
Accion Guía-Ejercicio_4.8 (Prim: Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            dato:N 
            Prox:Puntero a Nodo
        finRegistro
        Punt, PuntN, PuntAnt:Puntero a Nodo
        opcion:(1..4)
        bandera:Booleano
        datoBuscar, datoInsertar:N
        Procedimiento Buscar() Es
            Punt:= Prim
            bandera:=Verdadero
            Si *Punt.dato = datoBuscar Hacer
                Escribir("Se encontro el dato en la lista")
            SiNo
                Punt:=*Punt.Prox
                Mientras *Punt.dato <> datoBuscar y bandera  Hacer
                    Punt:=*Punt.Prox
                    Si Punt = Prim Hacer
                        bandera:=Falso
                    finSi
                finMientras
                Si bandera Hacer
                    Escribir("Se encontro el dato en la lista")
                SiNo
                    Escribir("No existe el elemento en lista")
                finSi
            finSi
        finProcedimiento

        Procedimiento insertar() Es
            Punt:=Prim
            Nuevo(PuntN)
            Si datoInsertar<=*Punt.dato Hacer  
                PuntAnt:=Prim
                Mientras *PuntAnt.Prox <> Prim Hacer
                    PuntAnt=*PuntAnt.Prox
                finMientras
                *PuntN.dato:=datoInsertar
                *PuntAnt.Prox:=PuntN
                *PuntN.Prox:=Punt
                Prim:=PuntN
            SiNo
                PuntAnt:=Punt
                Punt:=*Punt.Prox
                Mientras datoInsertar>=*Punt.dato Y Punt<> Prim Hacer
                    PuntAnt:=Punt
                    Punt:=*Punt.Prox
                finMientras 
                Si Punt= Prim
                    *PuntAnt.Prox:=PuntN
                    *PuntN.dato:=datoInsertar
                    *PuntN.Prox:=Prim
                SiNo  
                    *PuntN.dato:=datoInsertar
                    *PuntAnt.Prox:=PuntN
                    *PuntN.Prox:=Punt
                finSi
        finProcedimiento

        Procedimiento eliminar() Es
            Punt:=Prim;
            bandera:=Verdadero
            Si datoEliminar = *Punt.dato Hacer
                PuntAnt:=Prim
                Mientras *PuntAnt.Prox <> Prim Hacer
                    PuntAnt=*PuntAnt.Prox
                finMientras
                *PuntAnt.Prox:=*Punt.Prox
                Disponer(Punt)
                Prim:=*PuntAnt.Prox
            SiNo
                PuntAnt:=Punt
                Punt:= *Punt.Prox
                Mientras datoEliminar<>*Punt.dato y bandera Hacer
                    Punt:=*Punt.Prox
                    Si Punt=Prim Hacer
                        bandera:=Falso
                    finSi
                finMientras
                Si bandera Hacer
                    *PuntAnt.Prox:=*Punt.Prox
                    Disponer(Punt)
                SiNo
                    Escribir("No existe el elemento a eliminar")
                finSi
                finMientras

            finSi
        finProcedimiento
    finAmbiente
    Proceso
        bandera:=Verdadero
        Mientras bandera Hacer
            Escribir("Escriba que operacion desea realizar: /// Buscar /// Insertar /// borrar /// terminar operaciones ")
            Leer(opcion)
            Si opcion = 1 Hacer
                Leer("Escriba ele elemento a buscar:",datoBuscar)
                buscar()
            SiNo
                Si opcion = 2 Hacer
                    Leer("Escriba el dato a insertar:",datoInsertar)
                    insertar()

                SiNo
                    Si opcion = 3 Hacer
                        Leer("Escriba el dato a eliminar:", datoEliminar)
                        eliminar()
                    SiNo
                        bandera:=Falso
                    finSi
                finSi
        finMientras
    finProceso
finAccion
```
## Relaciones
- [[Listas-AlgoritmosI]]

