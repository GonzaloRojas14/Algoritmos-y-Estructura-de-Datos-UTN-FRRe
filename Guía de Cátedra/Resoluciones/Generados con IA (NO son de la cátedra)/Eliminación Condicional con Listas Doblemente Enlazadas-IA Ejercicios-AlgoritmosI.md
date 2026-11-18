

**Fecha de inicio:** 15-02-2025 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

Dada una **lista doblemente enlazada** con información sobre los productos en stock de un almacén, donde cada producto tiene los siguientes datos:

#### **Tabla de Productos**

`| id_producto | nombre | tipo | precio | stock |`

Se debe eliminar de la lista **todos los productos cuyo precio sea un número primo**.  
Para ello, se debe implementar una **función recursiva** `EsPrimo(n: N) → Bool` que determine si un número es primo.

📌 **Requisitos**:

- Implementar la eliminación de nodos de la lista correctamente.
- Usar **recursividad** para determinar si un número es primo.
## Resolución
``` less
Accion Eliminación_Condicional_con_Listas_Doblemente_Enlazadas(Prim: Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            id_producto:N 
            nombre:AN 
            tipo:AN 
            precio:N 
            stock:N 
            prox: Puntero a Nodo
            ant:Puntero a Nodo
        finRegistro

        punt,a: Puntero a Nodo
        bandera:Booleano
        Procedimiento Eliminar(punt_e:Puntero a Nodo) Es
            Ambiente
                p,aux:Puntero a Nodo
            finAmbiente
            Proceso
                p:=*punt_e.prox
                aux:=*punt_e.ant
                Si aux=Null Hacer
                    Si p<>Null Hacer
                        *p.ant=Null
                    finS
                    Prim:=p
                SiNo
                    Si p<>Null Hacer
                        *p.ant:=aux
                    finSi
                    *aux.prox:= p 
                finSi
                Disponer(punt_e)
            finProceso
        finProcedimiento

        Funcion EsPrimo(num:N, div):Booleano Es
            Si div=1 Hacer
                EsPrimo:=Verdadero
            SiNo
                Si (num mod div)=0
                    EsPrimo:=Falso
                SiNo
                    EsPrimo:=Verdadero y EsPrimo(num, div-1)
                finSi
            finSi
        finFuncion
    finAmbiente
    Proceso
	    punt := Prim
	    Mientras punt <> Null Hacer
	        a := *punt.prox
	        Si No EsPrimo(*punt.precio, *punt.precio - 1) Entonces
	            Eliminar(punt)
	        FinSi
	        punt := a
	    FinMientras
	finProceso
finAccion
```
## Relaciones
- [[Listas-AlgoritmosI]]
- [[Recursividad-Introduccion-AlgoritmosI]]
