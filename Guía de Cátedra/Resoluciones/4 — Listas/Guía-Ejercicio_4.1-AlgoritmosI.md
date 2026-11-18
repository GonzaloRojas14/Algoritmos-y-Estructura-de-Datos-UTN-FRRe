**Fecha de inicio:** 23-10-2024 - Algoritmos I
---
**Tags:** #Completed    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Diseñar un algoritmo para acceder, eliminar o insertar el k-ésimo elemento de una lista (siendo k una posición dada). Si la lista está vacía o si el valor de k esta fuera del rango del índice de la lista, invocar al procedimiento de ERROR. En cualquier otro caso, efectuar el procedimiento solicitado.

### Explicación de Ejercicio
Hasta donde entiendo, el ejercicio debe recibir una posición cualquiera del usuario, almacenar esa posición en una variable `k` y realizar una de las 3 acciones en caso de ser posible o  llamar al procedimiento `ERROR()` en caso de surgir un problema. La acción recibe como dato el elemento tipo nodo llamado `Prim` que es el primer elemento de la Lista.
## Resolución
``` less
Accion Ejercicio_4.1(Prim: Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            dato: Entero
            prox: Puntero a Nodo
        FinRegistro
        
        Ant, Punt, PuntN: Puntero a Nodo
        i, k, accion: Entero
        op: ("S", "N")


        Procedimiento Encontrar_elemento(posicion: Num) Es
            Si posicion = 1 Hacer
                Ant := Null
                Punt := Prim
            Sino
                Para i := 1 hasta posicion - 1 Hacer
                    Si Punt <> Null Hacer
                        Ant := Punt
                        Punt := *Punt.prox
                    Sino
                        Escribir("ERROR: Posición fuera de la lista")
                        ERROR()
                        Romper
                    FinSi
                FinPara
            FinSi
        FinProcedimiento
        

        Procedimiento Procedimiento_Principal() Es
            Mientras op = "S" Hacer
                Punt := Prim
                Ant := Null
                Escribir("¿Qué acción desea realizar?")
                Escribir("Escriba: /// 1 para acceder a un elemento /// 2 para eliminar un elemento /// 3 para insertar un elemento")
                Leer(accion)
                Segun accion Hacer
                    =1: Accion_1()
                    =2: Accion_2()
                    =3: Accion_3()
                FinSegun
            FinMientras
        FinProcedimiento

        Procedimiento Accion_1() Es
            Escribir("Escriba la posición del elemento del que quiere conocer su valor")
            Leer(k)
            Encontrar_elemento(k)
            Si Punt <> Null Hacer
                Escribir("El valor que existe en la posición", k, "es:", *Punt.dato)
            Sino
                Escribir("ERROR")
                ERROR()
            FinSi
        FinProcedimiento

        Procedimiento Accion_2() Es
            Escribir("Escriba la posición del elemento que quiere eliminar")
            Leer(k)
            Encontrar_elemento(k)
            Si Punt <> Null Hacer
                Si Punt = Prim Hacer
                    Prim := *Prim.prox
                    Disponer(Punt)
                Sino
                    *Ant.prox := *Punt.prox
                    Disponer(Punt)
                FinSi
            Sino
                Escribir("ERROR")
                ERROR()
            FinSi
        FinProcedimiento


        Procedimiento Accion_3() Es
            Escribir("Escriba la posición en la que quiere que se encuentre el elemento")
            Leer(k)
            Encontrar_elemento(k)
            Si Punt = Null Entonces
                Escribir("ERROR")
                ERROR()
            Sino
                Escribir("Ingrese el valor que va a tener el elemento")
                Nuevo(PuntN)
                Leer(*PuntN.dato)
                Si Punt = Prim Hacer
                    *PuntN.prox := Prim
                    Prim := PuntN
                Sino
                    *Ant.prox := PuntN
                    *PuntN.prox := Punt
                FinSi
            FinSi
        FinProcedimiento


    finAmbiente
    Proceso
        Escribir("¿Desea realizar una acción? Escriba 'S' para sí y 'N' para no")
        Leer(op)
        Si Prim <> Null Hacer     
            Procedimiento_Principal()
        Sino
            Escribir

```
## Relaciones
- [[Listas-AlgoritmosI]]
- - [[Definición de Registros-AlgoritmosI]]
