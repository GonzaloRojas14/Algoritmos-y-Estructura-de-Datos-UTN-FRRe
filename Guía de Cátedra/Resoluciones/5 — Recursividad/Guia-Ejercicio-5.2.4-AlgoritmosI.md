**Fecha de inicio:** 25-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Para convertir un número decimal a binario, simplemente debe dividirse sucesivas veces por dos (2) hasta quedarnos con el cociente cero (0). Todos los restos de las divisiones, tomados en orden inverso, forman el número binario objetivo. Escribir un procedimiento recursivo que, recibiendo como parámetro un número entero positivo, muestre en pantalla el mismo número codificado en binario.
## Resolución
``` less
Accion Guia-Ejercicio-5.2.2 Es
    Ambiente
        Procedimiento Binario (Num: Numero) Es
            Si (Num DIV 2)=1 o (Num DIV 2)=0 Hacer
                Escribir(Num DIV 2)
            SiNo
                Binario(Num DIV 2)
            finSi
            Escribir(Num MOD 2)
        finProcedimiento
    finAmbiente
    Proceso
        Binario(8)
    finProceso
finAccion

```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]

