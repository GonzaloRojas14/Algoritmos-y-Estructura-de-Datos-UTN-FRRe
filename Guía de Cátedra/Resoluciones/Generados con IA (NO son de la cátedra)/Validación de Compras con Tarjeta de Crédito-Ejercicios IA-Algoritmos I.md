

**Fecha de inicio:** 18-02-2025 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
### Ejercicio 2: Validación de Compras con Tarjeta de Crédito (Recursividad)

Se tiene una **lista doblemente enlazada** con información de las compras realizadas por los clientes en un comercio electrónico. Cada nodo de la lista contiene los siguientes datos:

- `id_compra`
- `fecha_compra`
- `metodo_pago`
- `nro_tarjeta` (arreglo de 16 posiciones con los dígitos de la tarjeta)
- `monto`

Se necesita validar las compras realizadas con tarjeta de crédito (`metodo_pago` = "TC"). Para validar cada número de tarjeta, se debe aplicar el siguiente algoritmo:

- Procesar los dígitos del número de tarjeta desde el último hacia el primero.
- Duplicar los dígitos en posiciones impares (comenzando desde la derecha, la posición 1 es impar). Si el resultado de la duplicación es mayor que 9, sumar los dígitos del resultado (ej: 14 → 1 + 4 = 5).
- Sumar todos los dígitos obtenidos después de la duplicación (y la suma de sus dígitos, si aplica).
- Si la suma total es divisible por 10, la tarjeta es válida.

**Se solicita:**

1. **Escribir una función recursiva** que valide si un número de tarjeta de crédito es válido según el algoritmo descrito.

## Resolución
``` less
Accion Validación_de_Compras_con_Tarjeta_de_Crédito(Prim:Puntero a Nodo) Es
        Ambiente
        form_fecha = Registro
            dia:(1...31)
            mes:(1...12)
            año:N(4)
        finRegistro
        
        Nodo = Registro
            id_compra:N 
            fecha_compra:form_fecha
            metodo_pago:AN(2)
            nro_tarjeta: Arreglo [16] de enteros
            prox:Puntero a Nodo
            ant:puntero a Nodo
        finRegistro

        punt:Puntero a Nodo

        Funcion suma_tarjeta(arr:Arreglo [16] de enteros, indice:(0...15)):N Es 
            Si indice = 0
                suma_tarjeta:=arr[0]
            SiNo
                Si (indice MOD 2) <> 0 Hacer
                    Si arr[indice]*2 >9 Hacer
                        suma_tarjeta:=(((arr[indice]*2)DIV 10)+ ((arr[indice]*2)MOD 10))+suma_tarjeta(arr,indice-1)
                    SiNo
                        suma_tarjeta:=arr[indice]+suma_tarjeta(arr, indice-1)
                    finSi
                SiNo
                    suma_tarjeta:=arr[indice]+suma_tarjeta(arr,indice-1)
                finSi
            finSi
        finFuncion
    finAmbiente
    Proceso
        punt:=Prim
        Mientras punt <> Null Hacer
            Si (suma_tarjeta(*punt.nro_tarjeta, 15) MOD 10) = 0 Hacer
                Escribir("La tarjeta es valida")
            SiNo
                Escribir("La tarjeta es invalida")
            finSi
            punt:=*punt.prox
        finMientras
    finProceso
finAccion
```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]