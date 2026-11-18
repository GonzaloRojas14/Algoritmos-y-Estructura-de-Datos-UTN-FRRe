**Fecha de inicio:** 04-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Un Casino de la región ha notado un incremento en los costos de las reparaciones de tragamonedas en sus sucursales. Por ello solicitó un informe con la cantidad de reparaciones y sus costos, discriminados según tragamonedas, modelo, marca, sucursal y total general.

Se dispone de un archivo REPARACIONES, con el siguiente formato. Cada registro representa la reparación de un tragamonedas, tener en cuenta que puede existir más de una reparación por tragamonedas.

**REPARACIONES** Ordenado por Cod_Sucursal, Marca, Modelo, Cod_Tragamonedas

- Cod_Sucursal
- Marca
- Modelo
- Cod_Tragamonedas
- Fecha_Reparacion
- Costo_Reparacion

Realice el algoritmo para emitir el informe con los totales solicitados
## Resolución
``` less
Accion Guía-Ejercicio_2.2.13-AlgoritmosI Es
    Ambiente
        Fecha = Registro
            Dia: (1..31) 
            Mes: (1..12) 
            Año: N(4)
        finRegistro
        Reparaciones = Registro 
            Clave = Registro
                Cod_Sucursal: N 
                Marca: AN 
                Modelo: AN
                Cod_Tragamonedas: N 
            finRegistro
            Fecha_Reparacion: Fecha 
            Costo_Reparacion: Real
        finRegistro

        arch_Reparaciones: Archivo de Reparaciones Ordenado Por Clave
        reg_Reparaciones: Registro de Reparaciones

        resg_Cod_Sucursal, resg_Cod_Tragamonedas: N 
        resg_Marca, resg_Modelo: AN 

        cont_Cod_Tragamonedas, cont_Cod_Sucursal, cont_Marca, cont_Modelo, total_cont: N 
        acum_Cod_Tragamonedas, acum_Cod_Sucursal, acum_Marca, acum_Modelo, total_acum: N
        
        Procedimiento Corte_Cod_Tragamonedas() Es
            cont_Modelo:= cont_Modelo + cont_Cod_Tragamonedas
            acum_Modelo:= acum_Modelo + acum_Cod_Tragamonedas
            Escribir("Analisis de Tragamonedas:", resg_Cod_Tragamonedas)
            Escribir("La cantidad de reparaciones que tuvo Es:",cont_Cod_Tragamonedas)
            Escribir("Tuvo un costo en reparaciones de:", acum_Cod_Tragamonedas)
            resg_Cod_Tragamonedas:= reg_Reparaciones.Clave.Cod_Tragamonedas
            cont_Cod_Tragamonedas:= 0 
            acum_Cod_Tragamonedas:= 0
        finProcedimiento

        Procedimiento Corte_Modelo() Es
            Corte_Cod_Tragamonedas()
            cont_Marca:= cont_Marca + cont_Modelo
            acum_Marca:= acum_Marca + acum_Modelo
            Escribir("Analisis del Modelo:", resg_Modelo)
            Escribir("Cantidad de reparaciones al Modelo:", cont_Modelo)
            Escribir("Costo en reparaciones:", acum_Modelo)
            cont_Modelo:= 0 
            acum_Modelo:= 0
            resg_Modelo:= reg_Reparaciones.Clave.Modelo
        finProcedimiento

        Procedimiento Corte_Marca() Es
            Corte_Modelo()
            cont_Cod_Sucursal:= cont_Cod_Sucursal + cont_Marca
            acum_Cod_Sucursal:= acum_Cod_Sucursal + acum_Marca
            Escribir("Analisis de la Marca:", resg_Marca)
            Escribir("Cantidad de reparaciones a la Marca:", cont_Marca)
            Escribir("Costo en reparaciones:", acum_Marca)
            cont_Marca:= 0 
            acum_Marca:= 0
            resg_Marca:= reg_Reparaciones.Clave.Marca
        finProcedimiento

        Procedimiento Corte_Sucursal() Es
            Corte_Marca()
            total_cont:= total_cont + cont_Cod_Sucursal
            total_acum:= total_acum + acum_Cod_Sucursal
            Escribir("Analisis de Cod_Sucursal:", resg_Cod_Sucursal)
            Escribir("Cantidad de reparaciones en la sucursal:", cont_Cod_Sucursal)
            Escribir("Costo en reparaciones:", acum_Cod_Sucursal)
            cont_Cod_Sucursal:= 0 
            acum_Cod_Sucursal:= 0
            resg_Cod_Sucursal:= reg_Reparaciones.Clave.Cod_Sucursal
        finProcedimiento


        Procedimiento Inicializar() Es
            Abrir E/(arch_Reparaciones)
            Leer(arch_Reparaciones, reg_Reparaciones)
            cont_Cod_Tragamonedas:= 0
            cont_Cod_Sucursal:= 0
            cont_Marca:= 0
            cont_Modelo := 0
            total_cont:= 0
            acum_Cod_Tragamonedas:= 0
            acum_Cod_Sucursal:= 0
            acum_Marca:= 0
            acum_Modelo := 0
            total_acum:= 0
            
            resg_Cod_Sucursal := reg_Reparaciones.Clave.Cod_Sucursal
            resg_Marca := reg_Reparaciones.Clave.Marca
            resg_Modelo := reg_Reparaciones.Clave.Modelo
            resg_Cod_Tragamonedas := reg_Reparaciones.Clave.Cod_Tragamonedas

        finProcedimiento
    finAmbiente
    Proceso
        Inicializar()
        Mientras NFDS(arch_Reparaciones) Hacer
            Si resg_Cod_Sucursal <> reg_Reparaciones.Clave.Cod_Sucursal Entonces
                Corte_Sucursal()
            SiNo
                Si resg_Marca <> reg_Reparaciones.Clave.Marca Entonces
                    Corte_Marca()
                SiNo
                    Si resg_Modelo<>reg_Reparaciones.Clave.Modelo Entonces
                        Corte_Modelo()
                    SiNo
                        Si resg_Cod_Tragamonedas<>reg_Reparaciones.Clave.Cod_Tragamonedas Entonces
                            Corte_Cod_Tragamonedas()
                        finSi
                    finSi
                finSi
            finSi
            cont_Cod_Tragamonedas:= cont_Cod_Tragamonedas + 1
            acum_Cod_Tragamonedas:= acum_Cod_Tragamonedas + reg_Reparaciones.Costo_Reparacion
            Leer(arch_Reparaciones, reg_Reparaciones)
        finMientras
        Corte_Sucursal()
        Escribir("Las reparaciones totales fueron:", total_cont)
        Escribir("El costo total fue:", total_acum)
        Cerrar(arch_Reparaciones)
    finProceso
finAccion
```
## Relaciones


