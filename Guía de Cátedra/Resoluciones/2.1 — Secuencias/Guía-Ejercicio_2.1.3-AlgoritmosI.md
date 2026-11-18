

**Fecha de inicio:** 12-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de caracteres y se desea obtener una secuencia de salida que resulte de copiar la secuencia de entrada, descartando el caracter "$".
## Resolución
``` less
Accion Guía-Ejercicio_2.1.3-AlgoritmosI Es 
    Ambiente
        secEntrada, secSalida: secuencia de Caracter
        vEntrada: Caracter
        Procedimiento inicializar()
            ARR(secEntrada)
            AVZ(secEntrada, vEntrada)
            CREAR(secSalida)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(secEntrada) Hacer
            Si vEntrada<>"$" Entonces
                Grabar(secSalida, vEntrada)
            finSi
            AVZ(secEntrada, vEntrada)
        finMientras
        Si vEntrada <> "$" Entonces
            Grabar(secSalida, vEntrada)
        finSi
        Cerrar(secEntrada)
        Cerrar(secSalida)
    finProceso
finAccion

```
## Relaciones
- [[General-Secuencias-AlgoritmosI]]

