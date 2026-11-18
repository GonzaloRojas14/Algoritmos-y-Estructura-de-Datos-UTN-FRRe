**Fecha de inicio:** 23-10-2024 - Algoritmos I
---
**Tags:** #Completed    #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
Se dispone de una lista simplemente encadenada cuyos registros están ordenados en forma ascendente por una clave de tipo entero; diseñar un algoritmo que invierta el orden de la lista.
## Resolución
``` less
Accion InvertirLista(Prim: Puntero a Nodo) Es
    Ambiente
        Nodo = Registro
            dato: Num                   // Dato de tipo numérico
            prox: Puntero a Nodo         // Puntero al siguiente nodo
        FinRegistro
        Punt, Anterior, Siguiente: Puntero a Nodo  // Punteros para invertir la lista
    finAmbiente
    Proceso
        Punt := Prim                      // Inicializamos Punt en el primer nodo
        Anterior := Null                  // No hay nodo anterior al primero

        Mientras Punt <> Null Hacer        // Recorremos la lista
            Siguiente := *Punt.prox        // Guardamos el siguiente nodo
            *Punt.prox := Anterior         // Invertimos el puntero, apunta al nodo anterior
            Anterior := Punt               // Movemos "Anterior" al nodo actual
            Punt := Siguiente              // Avanzamos al siguiente nodo
        FinMientras

        Prim := Anterior                   // Al final, Prim apunta al nuevo primer nodo
    finProceso
FinAccion
```
## Relaciones
- [[Listas-AlgoritmosI]]
- [[Definición de Registros-AlgoritmosI]]
