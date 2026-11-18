**Fecha de inicio:** 23-10-2024 - Algoritmos I
---
**Tags:** #Completed     #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea

Se dispone de una lista simplemente encadenada de números enteros, diseñar un algoritmo que a partir de ella genere otra lista conteniendo los nodos cuyos datos terminan en cero; dichos elementos, deberán ser eliminados de la lista original. Se asume que la lista está cargada, y que el algoritmo recibe como parámetro de entrada la dirección del primer elemento.

### Explicación del Ejercicio
#### A tener en cuenta
- El algoritmo recibe como parámetro de entrada la dirección del primer elemento. Ejemplo:
``` less
Accion Ejercicio_4.2(Prim: Puntero a Nodo) Es
FinAccion
```
- La lista ya esta cargada
#### Cosas que debe hacer el Algoritmo
- debe generar otra **Lista** con los _datos_ que terminen en 0.
- Los **elementos** que se cargue a la segunda **Lista** deben ser eliminados.

## Resolución
``` less
Accion Ejercicio_4.2(Prim: Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            dato : Num
            prox : Puntero a Nodo
        FinRegistro
        Punt_1,Ant,Punt_2,Prim_2,Ant_2:Puntero a Nodo


        Funcion termina_en_0 (numero:Num):Booleano Es
            numero:=numero MOD 10
            Si numero = 0 Hacer
                termina_en_0:=Verdadero
            Sino
                termina_en_0:=Falso
            FinSi
        FinFuncione
    finAmbiente

    Proceso
        Punt_1:=Prim
        Ant:=Null
        Ant_2:=Null
        Punt_2:=Null
        Mientras Punt_1 <> Null Hacer
            Si termina_en_0(*Punt_1.dato) Hacer
                Si Ant= Null Hacer
                    Prim:=*Punt_1.prox
                    Nuevo(Punt_2)
                    *Punt_2.dato:= *Punt_1.dato
                    Disponer(Punt_1)
                    Punt_1:=Prim
                    Prim_2:=Punt_2
                Sino
                    Si Ant_2 = Null
                        Nuevo(Punt_2)
                        *Ant.prox:=*Punt_1.prox
                        *Punt_2.dato:=*Punt_1.dato
                        Disponer(Punt_1)
                        Punt_1:=*Ant.prox
                        Prim_2:=Punt_2
                    Sino
                        Ant_2:=Punt_2
                        Nuevo(Punt_2)
                        *Ant.prox:=*Punt_1.prox
                        *Punt_2.dato:=*Punt_1.dato
                        *Ant_2.prox:=Punt_2
                        Disponer(Punt_1)
                        Punt_1:=*Ant.prox
                    FinSi
                FinSi
            Sino
                Punt_1:=*Punt_1.prox
            FinSi
        FinMientras
    finProceso
FinAccion

```

## Relaciones
- [[Listas-AlgoritmosI]]
- [[Definición de Registros-AlgoritmosI]]
