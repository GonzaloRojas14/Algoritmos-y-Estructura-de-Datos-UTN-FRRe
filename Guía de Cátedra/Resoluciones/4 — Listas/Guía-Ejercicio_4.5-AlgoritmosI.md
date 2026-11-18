**Fecha de inicio:** 23-10-2024 - Algoritmos I
---
**Tags:** #Completed     #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Dada una lista simplemente encadenada que contiene datos de todas las provincias de la República Argentina: nombre, capital, cantidad total de habitantes y cantidad de analfabetos, y está ordenada en forma decreciente por número de habitantes analfabetos, generar otras tres listas que contengan el nombre, la capital y el porcentaje de analfabetos de las Provincias que respondan a las siguientes restricciones.

- L1: <= 10 % analfabetos
- L2: 16 a 25 % analfabetos
- L3: => 26 % analfabetos
## Resolución
``` LESS
Accion Guia-Ejercicio4.5(Prim:Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            Nombre:AN(30)
            Capital:AN(15) 
            CTH:N(5)
            CTA:N(5)
            Prox:Puntero a Nodo
        finRegistro
        Nodo_Sal = Registro
            Nombre:AN(30)
            Capital:AN(15) 
            PA:N(3)
            Prox:Puntero a Nodo_Sal
        finRegistro
        Porcentaje:N
        Punt_P:Puntero a Nodo
        Ant_1 ,Punt_1, Ant_2, Punt_2, Ant_3, Punt_3:Puntero a Nodo_Sal
        

        Procedimiento Lista_1(datos:Puntero a Nodo) Es
            Nuevo(Punt_1)
            *Punt_1.Nombre := *datos.Nombre
            *Punt_1.Capital := *datos.Capital
            *Punt_1.PA := (*datos.CTA * 100) / *datos.CTH
            *Punt_1.Prox := Null

            Si Ant_1 = Null Entonces
                Ant_1 := Punt_1
            Sino
                *Ant_1.Prox := Punt_1
                Ant_1:=Punt_1
            finSi
        finProcedimiento

        Procedimiento Lista_2(datos:Puntero a Nodo) Es
            Nuevo(Punt_2)
            *Punt_2.Nombre := *datos.Nombre
            *Punt_2.Capital := *datos.Capital
            *Punt_2.PA := (*datos.CTA * 100) / *datos.CTH
            *Punt_2.Prox := Null

            Si Ant_2 = Null Entonces
                Ant_2 := Punt_2
            Sino
                *Ant_2.Prox := Punt_2
                Ant_2 := Punt_2
            FinSi
        finProcedimiento

        Procedimiento Lista_3(datos:Puntero a Nodo) Es
            Nuevo(Punt_3)
            *Punt_3.Nombre := *datos.Nombre
            *Punt_3.Capital := *datos.Capital
            *Punt_3.PA := (*datos.CTA * 100) / *datos.CTH
            *Punt_3.Prox := Null

            Si Ant_3 = Null Entonces
                Ant_3 := Punt_3
            Sino
                *Ant_3.Prox := Punt_3
                Ant_3 := Punt_3
            FinSi
        finProcedimiento

        Procedimiento SeleccionDeLista(datos:Puntero a Nodo) Es
            Porcentaje := (*datos.CTA * 100) / *datos.CTH
            Si Porcentaje <= 10 Entonces
                Lista_1(datos)
            Sino 
                Si Porcentaje >= 16 Y Porcentaje <= 25 Entonces
                    Lista_2(datos)
                Sino  
                    Si Porcentaje >= 26 Entonces
                        Lista_3(datos)
                    SiNo
                        Escribir("Error")
                    finSi
                finSi
            FinSi
        finProcedimiento


    finAmbiente
    Proceso
        Porcentaje:=0
        Punt_P:=Prim;Ant_1:=Null;Ant_2:=Null;Ant_3:=Null
        Punt_1:=Null;Punt_2:=Null;Punt_3:=Null
        Mientras Punt_P<>Null Hacer
            SeleccionDeLista(Punt_P)
            Punt_P:=*Punt_P.Prox

        finMientras
    finProceso
finAccion

```
## Relaciones
- [[Listas-AlgoritmosI]]
- [[Definición de Registros-AlgoritmosI]]

