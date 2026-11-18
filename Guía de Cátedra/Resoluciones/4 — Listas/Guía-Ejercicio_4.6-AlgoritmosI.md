

**Fecha de inicio:** 25-10-2024 - Algoritmos I
---
**Tags:** #Completed   #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
En el restaurante ÑOQUIS se está pensando en una solución informática para el soporte de datos del nuevo sistema de atención a clientes. Se han decidido por LISTAS por su dinamismo en cuanto a la cantidad de elementos. Diseñe un algoritmo que realice las siguientes funciones:

- Añadir cliente al ser atendido (lista simple ordenada por Nombre del Cliente).
- Registrar su consumo (Acumular el Total Consumido en valores de montos).
- Realizar el cobro (emitir ticket con Nombre, Fecha, Número de Mesa y Total).
- Eliminar del listado de atención.

La información almacenada debe mantenerse ordenada por Nombre del cliente.
## Resolución
``` less
Accion Guia-Ejercicio4.6 Es
    Ambiente
        FA:arrelo(1...3) de N
        Clientes = Registro
            Nombre:AN(15)
            Consumo:N(10)
            Prox:Puntero a Clientes
        finRegistro
        
        Prim, Punt, Ant, Punt_N:Puntero a Clientes
        Bandera, Encontrado:Booleano
        Opcion:(1...4)
        Resg_monto, Num_Mesa:N
        Resg_Nombre:AN(15)
        Procedimiento Primer_Cliente() Es
            Nuevo(Punt_N)
            Escribir("La lista esta vacia, antes de realizar operaciones necesita haber un cliente")
            Leer("Ingrese nombre del Clinete:",*Punt_N.Nombre)
            Leer("Ingrese el monto gastado:",*Punt_N.Consumo)
            Prim:= Punt_N
        finProcedimiento

        Procedimiento Añadir_Cliente() Es
            Nuevo(Punt_N)
            Leer("Nombre del Cliente:",*Punt_N.Nombre)
            *Punt_N.Consumo:=0
            Punt:=Prim
            Si *Punt.Nombre>*Punt_N.Nombre Hacer
                *Punt_N.Prox:=Punt
                Prim:=Punt_N
            SiNo
                Mientras *Punt.Nombre<=*Punt_N.Nombre Y Punt<>Null Hacer
                    Ant:=Punt
                    Punt:=*Punt.Prox
                finMientras
                Si Punt <> Null Hacer
                    *Punt_N.Prox:=Punt
                finSi
                *Ant.Prox:=Punt_N
            finSi 
        finProcedimiento

        Procedimiento Cobro_Ticket() Es
            Punt := Prim
            Encontrado := Falso
            Leer("Nombre del Cliente:", Resg_Nombre)
            
            Mientras Punt <> Null Y No Encontrado Hacer
                Si *Punt.Nombre = Resg_Nombre Entonces
                    Encontrado := Verdadero
                Sino
                    Punt := *Punt.Prox
                FinSi
            FinMientras

            Si Encontrado Entonces
                Leer("Monto del consumo:", Resg_monto)
                Leer("Número de mesa:", Num_Mesa)
                Leer("Día:", FA[1])
                Leer("Mes:", FA[2])
                Leer("Año:", FA[3])
                *Punt.Consumo := *Punt.Consumo + Resg_monto
                Escribir("Factura: // Nombre:", *Punt.Nombre, " // Fecha: ", FA[1], "/", FA[2], "/", FA[3], " // Número de mesa:", Num_Mesa, " // Total:", *Punt.Consumo)
            Sino
                Escribir("No se encontró al cliente.")
            FinSi
        finProcedimiento

        Procedimiento Eliminar_Cliente() Es
            Accion Guia_Ejercicio4_6 Es
    Ambiente
        FA: arreglo(1...3) de N
        Clientes = Registro
            Nombre: AN(15)
            Consumo: N(10)
            Prox: Puntero a Clientes
        FinRegistro
        
        Prim, Punt, Ant, Punt_N: Puntero a Clientes
        Bandera, Encontrado: Booleano
        Opcion: (1...4)
        Resg_monto, Num_Mesa: N
        Resg_Nombre: AN(15)

        Procedimiento Primer_Cliente() Es
            Nuevo(Punt_N)
            Escribir("La lista está vacía. Ingrese el primer cliente para continuar.")
            Leer("Ingrese nombre del Cliente:", *Punt_N.Nombre)
            Leer("Ingrese el monto gastado:", *Punt_N.Consumo)
            Punt_N.Prox := Null
            Prim := Punt_N
        FinProcedimiento

        Procedimiento Añadir_Cliente() Es
            Nuevo(Punt_N)
            Leer("Nombre del Cliente:", *Punt_N.Nombre)
            *Punt_N.Consumo := 0
            Punt := Prim
            Si *Punt.Nombre > *Punt_N.Nombre Entonces
                *Punt_N.Prox := Punt
                Prim := Punt_N
            Sino
                Mientras Punt <> Null Y *Punt.Nombre <= *Punt_N.Nombre Hacer
                    Ant := Punt
                    Punt := *Punt.Prox
                FinMientras
                Si Punt <> Null Entonces
                    *Punt_N.Prox := Punt
                FinSi
                *Ant.Prox := Punt_N
            FinSi 
        FinProcedimiento

        Procedimiento Cobro_Ticket() Es
            Punt := Prim
            Encontrado := Falso
            Leer("Nombre del Cliente:", Resg_Nombre)
            
            Mientras Punt <> Null Y No Encontrado Hacer
                Si *Punt.Nombre = Resg_Nombre Entonces
                    Encontrado := Verdadero
                Sino
                    Punt := *Punt.Prox
                FinSi
            FinMientras

            Si Encontrado Entonces
                Leer("Monto del consumo:", Resg_monto)
                Leer("Número de mesa:", Num_Mesa)
                Leer("Día:", FA[1])
                Leer("Mes:", FA[2])
                Leer("Año:", FA[3])
                *Punt.Consumo := *Punt.Consumo + Resg_monto
                Escribir("Factura: // Nombre:", *Punt.Nombre, " // Fecha: ", FA[1], "/", FA[2], "/", FA[3], " // Número de mesa:", Num_Mesa, " // Total:", *Punt.Consumo)
            Sino
                Escribir("No se encontró al cliente.")
            FinSi
        FinProcedimiento

        Procedimiento Eliminar_Cliente() Es
            Punt := Prim
            Ant := Null
            Encontrado := Falso
            Leer("Nombre del Cliente a eliminar:", Resg_Nombre)
            
            Mientras Punt <> Null Y No Encontrado Hacer
                Si *Punt.Nombre = Resg_Nombre Entonces
                    Encontrado := Verdadero
                Sino
                    Ant := Punt
                    Punt := *Punt.Prox
                FinSi
            FinMientras

            Si Encontrado Entonces
                Si Punt = Prim Entonces
                    Prim := *Punt.Prox
                Sino
                    *Ant.Prox := *Punt.Prox
                FinSi
                Disponer(Punt)
                Escribir("Cliente eliminado correctamente.")
            Sino
                Escribir("No se encontró el cliente:", Resg_Nombre)
            FinSi
        finProcedimiento

    finAmbiente
    Proceso
        Punt:=Null; Prim:=Null; Ant:=Null; Punt_N:=Null
        Bandera:=Verdadero;Encontrado:=Falso
        Primer_Cliente()
        Mientras Bandera Hacer
            Escribir("Elije que operacion deseas realizar: // 1:AÑADIR CLIENTE // 2:REALIZAR COBRO // 3:ELIMINAR CLIENTE // 4:TERMINAR OPERACION")
            Leer(Opcion)
            Segun Opcion Hacer
                =1:Añadir_Cliente()
                =2:Cobro_Ticket()
                =3:Eliminar_Cliente()
                =4:Bandera:=Falso
            finSegun
        finMientras
    finProceso
finAccion
```
## Relaciones

- [[Listas-AlgoritmosI]]
- [[Arreglos-AlgoritmosI]]
- [[Definición de Registros-AlgoritmosI]]
