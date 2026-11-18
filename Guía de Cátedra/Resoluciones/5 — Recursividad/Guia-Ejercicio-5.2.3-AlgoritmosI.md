

**Fecha de inicio:** 25-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada una lista de nombres ordenada en forma ascendente, construir un procedimiento recursivo que imprima como salida la misma lista, pero en orden descendente, sin modificar la lista original.
## Resolución
``` less
Accion Guia-Ejercicio-5.2.2(Prim: Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            Nombre:AN(30)
            Prox:Puntero a Nodo
        finRegistro
        Procedimiento Descendente (NodoActual:Puntero a Nodo) Es
            Si *NodoActual.Prox<>Null Hacer
                Descendente(*NodoActual.Prox)
            finSi
            Escribir(*NodoActual.Nombre)
        finProcedimiento
    finAmbiente
    Proceso
        Descendente(Prim)
    finProceso
finAccion
```
## Relaciones

- [[Listas-AlgoritmosI]]
