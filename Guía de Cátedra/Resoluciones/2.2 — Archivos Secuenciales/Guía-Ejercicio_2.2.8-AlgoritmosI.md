

**Fecha de inicio:** 01-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
De los datos del siguiente ejercicio:

**COMPRAS** Ordenado por Nro_Cliente

- Nro_Cliente
- Fecha_Ultima_Compra
- Monto

**CLIENTES** Ordenado por Nro_Cliente

- Nro_Cliente
- Apellido_Nombre
- Domicilio
- Teléfono
- DNI

Ambos archivos están ordenados por Nro. de Cliente en forma ascendente. Listar los nombres fecha y monto de última compra, de todos aquellos clientes cuya última compra sea posterior a una fecha dada y el monto supere un monto dado.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.8-AlgoritmosI Es
    Ambiente
        Fecha = Registro
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        
        Compras = Registro
            Nro_Cliente: N 
            Fecha_UltimaCompra: Fecha
            Monto: N 
        finRegistro
        Clientes = Registro
            Nro_Cliente: N 
            ApellidoNombre: AN 
            Domicilio: AN 
            Telefono: N 
            DNI: N 
        finRegistro

        arch_Compras: Archivo de Compras Ordenado Por Nro_Cliente
        arch_Clientes: Archivo de Clientes Ordenado Por Nro_Cliente
        reg_Compras: Registro de Compras 
        reg_Clientes: Registro de Clientes

        var_Fecha: Registro de Fecha
        var_Monto: N

        Procedimiento inicializar() Es
            Abrir E/(arch_Clientes); Abrir E/(arch_Compras)
            Leer(arch_Clientes, reg_Clientes); Leer(arch_Compras, reg_Compras)
            Escribir("Ingrese Fecha:")
            Escribir("Dia:")
            Leer(var_Fecha.Dia)
            Escribir("Mes:")
            Leer(var_Fecha.Mes)
            Escribir("Año:")
            Leer(var_Fecha.Año)
            Escribir("Ingrese un Monto:")
            Leer(var_Monto)
            Escribir("Nombre | Fecha | Monto")
        finProcedimiento

        Procedimiento Listar() Es
            Escribir(reg_Clientes.ApellidoNombre , "|", reg_Compras.Fecha_UltimaCompra.Dia, "/", reg_Compras.Fecha_UltimaCompra.Mes, "/", reg_Compras.Fecha_UltimaCompra.Año, "|", reg_Compras.Monto)
        finProcedimiento

        Procedimiento Verificacion() Es
            Si reg_Compras.Monto > var_Monto Entonces
                Si reg_Compras.Fecha_UltimaCompra.Año > var_Fecha.Año Entonces
                    Listar()
                SiNo
                    Si reg_Compras.Fecha_UltimaCompra.Año = var_Fecha.Año y reg_Compras.Fecha_UltimaCompra.Mes > var_Fecha.Mes Entonces
                        Listar
                    SiNo
                        Si reg_Compras.Fecha_UltimaCompra.Año = var_Fecha.Año y reg_Compras.Fecha_UltimaCompra.Mes = var_Fecha.Mes y reg_Compras.Fecha_UltimaCompra.Dia > var_Fecha.Dia Entonces
                            Listar
                        finSi
                    finSi
                finSi

            finSi
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
         Mientras NFDS(arch_Clientes) Hacer
            Verificacion()
            Leer(arch_Clientes, reg_Clientes); Leer(arch_Compras, reg_Compras)
            
         finMientras
         Verificacion()
         Cerrar(arch_Clientes);Cerrar(arch_Compras)
    finProceso
finAccion
```
## Relaciones


