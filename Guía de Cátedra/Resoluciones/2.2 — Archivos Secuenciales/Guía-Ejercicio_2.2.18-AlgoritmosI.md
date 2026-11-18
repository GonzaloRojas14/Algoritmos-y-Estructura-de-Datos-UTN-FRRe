**Fecha de inicio:** 07-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Un supermercado desea conocer la totalidad de unidades existentes de cada artículo a fin de hacer un control de stock y decidir si se deben comprar nuevas unidades o redistribuir la mercadería existente.

El supermercado posee dos sucursales, cada una de las cuales envió su información en un fichero con el siguiente formato:

- **ARTICULOS**
	- Cod_Prod
	- Tipo
	- Marca
	- Descripción
	- Cant_Unidades

Escribir un algoritmo que permita obtener un único fichero de salida, con el mismo formato, que contenga la información solicitada y además, emita un listado con los siguientes datos:

| Cod_Prod | Tipo | Marca | Descripción | Cant_Suc_1 | Cant_Suc_2 | Total_Unidades |
| -------- | ---- | ----- | ----------- | ---------- | ---------- | -------------- |
|          |      |       |             |            |            |                |
## Resolución
``` less
Accion Guía-Ejercicio_2.2.18-AlgoritmosI Es
    Ambiente
        Articulos = Registro 
            Cod_Producto: N 
            Tipo: AN 
            Marca: AN 
            Descripcion: AN 
            Cant_Unidades: N 
        finRegistro
        
        arch_suc1, arch_suc2: Archivo de Articulos Ordenado Por Cod_Producto
        reg_suc1, reg_suc2: Articulos
        arch_Salida: Archivo de Articulos

        Procedimiento Leer_suc1() Es
            Leer(arch_suc1, reg_suc1)
            Si FDA(arch_suc1) Entonces 
                reg_suc1.Cod_Producto:= HV 
            finSi
        finProcedimiento

        Procedimiento Leer_suc2() Es
            Leer(arch_suc2, reg_suc2)
            Si FDA(arch_suc2) Entonces 
                reg_suc2.Cod_Producto:= HV 
            finSi
        finProcedimiento

        Procedimiento Escribir_Valores(Cod_Prod: N, Tipo: AN, Marca:AN, Descripcion: AN, Cant_Unidades1: N, Cant_Unidades2:N) Es
            Escribir(Cod_Prod, "|", Tipo, "|", Marca, "|", Descripcion, "|", Cant_Unidades1, "|", Cant_Unidades2, "|", Cant_Unidades1 + Cant_Unidades2)
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_suc1); Abrir E/(arch_suc2); Abrir S/(arch_Salida)
            Leer_suc1(); Leer_suc2()
            Escribir(" Cod_Prod | Tipo | Marca | Descripción | Cant_Suc_1 | Cant_Suc_2 | Total_Unidades |")
        finProcedimiento

    finAmbiente
    
    Proceso
        inicializar()
        
        Mientras reg_suc1.Cod_Producto <> HV o reg_suc2.Cod_Producto <> HV Hacer
            Si reg_suc1.Cod_Producto = reg_suc2.Cod_Producto Entonces
                Escribir_Valores(reg_suc1.Cod_Producto, reg_suc1.Tipo, reg_suc1.Marca, reg_suc1.Descripcion, reg_suc1.Cant_Unidades, reg_suc2.Cant_Unidades)
                reg_suc1.Cant_Unidades:= reg_suc1.Cant_Unidades + reg_suc2.Cant_Unidades
                GRABAR(arch_Salida, reg_suc1)
                Leer_suc1()
                Leer_suc2()
            SiNo
                Si reg_suc1.Cod_Producto < reg_suc2.Cod_Producto Entonces
                    Escribir_Valores(reg_suc1.Cod_Producto, reg_suc1.Tipo, reg_suc1.Marca, reg_suc1.Descripcion, reg_suc1.Cant_Unidades, 0)
                    GRABAR(arch_Salida, reg_suc1)
                    Leer_suc1()
                SiNo
                    Escribir_Valores(reg_suc2.Cod_Producto, reg_suc2.Tipo, reg_suc2.Marca, reg_suc2.Descripcion, 0, reg_suc2.Cant_Unidades)
                    GRABAR(arch_Salida, reg_suc2)
                    Leer_suc2()
                finSi
            finSi
        finMientras
        
        Cerrar(arch_Salida); Cerrar(arch_suc1); Cerrar(arch_suc2)
    finProceso
finAccion
```
## Relaciones


