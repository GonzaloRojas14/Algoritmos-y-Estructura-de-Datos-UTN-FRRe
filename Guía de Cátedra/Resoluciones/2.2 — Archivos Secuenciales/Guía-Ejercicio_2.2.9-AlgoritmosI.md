

**Fecha de inicio:** 03-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Una casa deportiva dispone de un archivo de productos, ordenado por código de producto, que contiene los siguientes datos:

**PRODUCTOS** Ordenado por `Cod_Producto`

- `Cod_Producto`
- `Tipo: (1,2,3)`
- `Marca`
- `Modelo`
- `Descripción`
- `Cantidad_Existente`
- `Precio_Unitario`

Se ha registrado en el mercado un aumento de precios, el cual no es uniforme para todos los artículos, sino que varía según el tipo de los mismos de la siguiente manera: tipo 1- Calzados: 10%, tipo 2 – Indumentaria: 25%, tipo 3 - Accesorios (pelotas, raquetas, etc.): 50%. Por este motivo el gerente de la empresa solicitó al Departamento de Informática que modifique los precios de acuerdo a los porcentajes antes mencionados.  
Generar un nuevo fichero de productos para cumplir con la solicitud del gerente.  
Al terminar el proceso informar cantidad total de artículos de cada tipo hay y total general.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.9-AlgoritmosI Es
    Ambiente
        Productos = Registro
            cod_Producto: N 
            Tipo: (1, 2, 3)
            Marca: AN 
            Modelo: AN 
            Descripcion: AN 
            Cantidad_existente: N 
            Precio_Unitario: Real 
        finRegistro
        
        arch_Productos: Archivo de Productos Ordenado Por cod_Producto
        reg_Productos, reg_Salida: Registro de Productos
        arch_Salida: Archivo de Productos
        cont_1, cont_2, cont_3: Entero
        
        Procedimiento inicializar() Es
            Abrir E/(arch_Productos); Abrir S/(arch_Salida)
            Leer(arch_Productos, reg_Productos)
            cont_1:= 0; cont_2:= 0; cont_3:= 0
        finProcedimiento
        
        Procedimiento GrabarArchivo() Es
            reg_Salida:= reg_Productos
            Segun reg_Productos.Tipo Hacer
                = 1: 
                    cont_1:= cont_1 + 1
                    reg_Salida.Precio_Unitario:= reg_Salida.Precio_Unitario * 1.10
                = 2: 
                    cont_2:= cont_2 + 1
                    reg_Salida.Precio_Unitario:= reg_Salida.Precio_Unitario * 1.25
                = 3: 
                    cont_3:= cont_3 + 1
                    reg_Salida.Precio_Unitario:= reg_Salida.Precio_Unitario * 1.50
            finSegun
            GRABAR(arch_Salida, reg_Salida)
        finProcedimiento

    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(arch_Productos) Hacer
            GrabarArchivo()
            Leer(arch_Productos, reg_Productos)
        finMientras
        
        GrabarArchivo() 
        
        Escribir("La cantidad total de artículos tipo 1 es de:", cont_1)
        Escribir("La cantidad total de artículos tipo 2 es de:", cont_2)
        Escribir("La cantidad total de artículos tipo 3 es de:", cont_3)
        Escribir("La cantidad total de artículos es:", cont_1 + cont_2 + cont_3)
        
        Cerrar(arch_Productos); Cerrar(arch_Salida)
    finProceso
finAccion
```
## Relaciones


