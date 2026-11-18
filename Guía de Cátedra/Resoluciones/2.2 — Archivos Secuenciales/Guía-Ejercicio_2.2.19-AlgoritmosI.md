**Fecha de inicio:** 07-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
En una Empresa Farmacéutica se posee un archivo **MAE_REMEDIOS** (ordenado por Clave: Farmacia + Medicamento), el que se actualiza semanalmente, a traves de la información que se encuentra cargada en un archivo de **MOVIMIENTOS** (ordenado por Clavem: Farmacia + Medicamento, y Cod_Mov), de la siguiente forma:

- Si Clave (**MAE_REMEDIOS**) es menor que Clavem (**MOVIMIENTOS**), simplemente se transfieren los datos del Maestro a la salida y se graban.
    
- Si Clave (**MAE_REMEDIOS**) es igual a Clavem (**MOVIMIENTOS**) y el Codmov es 1, se considera error y se lista un mensaje indicando el tipo de error; pero si el Codmov es 2, entonces es un remedio que deja de fabricarse y se transfiere el registro al archivo de Remedios vencidos (**REM_VENC**) ; pero si el Cod_Mov es 3, se modifica la cantidad actual con la cantidad recibida.
    
- Si Clave (**MAE_REMEDIOS**) es mayor que Clavem (**MOVIMIENTOS**) y el Codmov es 1, se incorpora el remedio a nuestro Vademecum, considerando que la cantidad recibida configura la cantidad actual y la Fecha_Vencimiento es 30 días posterior a la fecha actual; pero si el Codmov es 2 o 3 se considera error y se deben producir los correspondientes mensajes de error.
    

Se considera que solo existe un registro de movimiento para cada registro del maestro.

**MAE_REMEDIOS** Ordenado por Farmacia y Medicamento

- Farmacia
- Medicamento
- Cant_Actual
- Fecha_Vencimiento

**MOVIMIENTOS** Ordenado por Farmacia, Medicamento y Cod_Mov

- Farmacia
- Medicamento
- Cod_Mov
- Cant_Recibida

**REM_VENC** Ordenado por Medicamento

- Medicamento
- Cant_Vencida
## Resolución
``` less
Accion Guía-Ejercicio_2.2.19-AlgoritmosI Es
    Ambiente
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        
        Maestro = Registro
            Clave = Registro
                Farmacia: AN 
                Medicamento: AN 
            finRegistro
            Cant_Actual: N 
            Fecha_Vencimiento: Fecha
        finRegistro
        
        Movimientos = Registro
            Clave = Registro
                Farmacia: AN 
                Medicamento: AN 
                Cod_Movimiento: N
            finRegistro
            Cant_Recibida: N 
        finRegistro
        
        Vencidos =  Registro
            Medicamento: AN 
            Cant_Vencida: N
        finRegistro
        
        arch_MaestroActualizado: Archivo de Maestro
        reg_MaestroActualizado: Maestro
        
        arch_Maestro: Archivo de Maestro Ordenado Por Clave
        reg_Maestro: Maestro
        
        arch_Movimientos: Archivo de Movimientos Ordenado Por Clave
        reg_Movimientos: Movimientos
        
        arch_Vencidos: Archivo de Vencidos 
        reg_Vencidos: Vencidos

        Fecha_Actual: Fecha 

        Procedimiento Leer_Maestro() Es
            Leer(arch_Maestro, reg_Maestro)
            Si FDA(arch_Maestro) Entonces
                reg_Maestro.Clave.Farmacia:= HV 
            finSi
        finProcedimiento
        
        Procedimiento Leer_Movimientos() Es
            Leer(arch_Movimientos, reg_Movimientos)
            Si FDA(arch_Movimientos) Entonces
                reg_Movimientos.Clave.Farmacia:= HV
            finSi
        finProcedimiento

        Procedimiento Iguales() Es
            Si reg_Movimientos.Clave.Cod_Movimiento = 1 Entonces
                Escribir("Error tipo de movimiento 1")
            SiNo
                Si reg_Movimientos.Clave.Cod_Movimiento = 2 Entonces
                    reg_Vencidos.Medicamento:= reg_Maestro.Clave.Medicamento
                    reg_Vencidos.Cant_Vencida:= reg_Maestro.Cant_Actual + reg_Movimientos.Cant_Recibida
                    GRABAR(arch_Vencidos, reg_Vencidos)
                SiNo
                    reg_Maestro.Cant_Actual:= reg_Maestro.Cant_Actual + reg_Movimientos.Cant_Recibida
                    GRABAR(arch_MaestroActualizado, reg_Maestro)
                finSi
            finSi
            Leer_Maestro()
            Leer_Movimientos()
        finProcedimiento

        Procedimiento Diferentes() Es
            Si reg_Movimientos.Clave.Cod_Movimiento = 1 Entonces
                reg_MaestroActualizado.Clave.Farmacia:= reg_Movimientos.Clave.Farmacia
                reg_MaestroActualizado.Clave.Medicamento:= reg_Movimientos.Clave.Medicamento
                reg_MaestroActualizado.Cant_Actual:= reg_Movimientos.Cant_Recibida
                
                
                reg_MaestroActualizado.Fecha_Vencimiento.Dia:= Fecha_Actual.Dia
                Si Fecha_Actual.Mes = 12 Entonces
                    reg_MaestroActualizado.Fecha_Vencimiento.Mes:= 1
                    reg_MaestroActualizado.Fecha_Vencimiento.Año:= Fecha_Actual.Año + 1
                SiNo
                    reg_MaestroActualizado.Fecha_Vencimiento.Mes:= Fecha_Actual.Mes + 1
                    reg_MaestroActualizado.Fecha_Vencimiento.Año:= Fecha_Actual.Año
                finSi
                
                GRABAR(arch_MaestroActualizado, reg_MaestroActualizado)
            SiNo
                Si reg_Movimientos.Clave.Cod_Movimiento = 2 Entonces
                    Escribir("Error Movimiento tipo 2")
                SiNo
                    Escribir("Error Movimiento tipo 3")
                finSi
            finSi
            Leer_Movimientos()
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_Maestro); Abrir E/(arch_Movimientos)
            Abrir S/(arch_MaestroActualizado); Abrir S/(arch_Vencidos)
            Leer_Maestro()
            Leer_Movimientos()
            Escribir("Ingrese Fecha Actual:")
            Escribir("Dia:")
            Leer(Fecha_Actual.Dia)
            Escribir("Mes:")
            Leer(Fecha_Actual.Mes)
            Escribir("Año:")
            Leer(Fecha_Actual.Año)
        finProcedimiento
    finAmbiente
    
    Proceso
        inicializar()
        Mientras reg_Maestro.Clave.Farmacia <> HV o reg_Movimientos.Clave.Farmacia <> HV Hacer
            Si reg_Maestro.Clave.Farmacia = reg_Movimientos.Clave.Farmacia Entonces
                Si reg_Maestro.Clave.Medicamento = reg_Movimientos.Clave.Medicamento Entonces
                    Iguales()
                SiNo
                    Si reg_Maestro.Clave.Medicamento < reg_Movimientos.Clave.Medicamento Entonces
                        GRABAR(arch_MaestroActualizado, reg_Maestro)
                        Leer_Maestro()
                    SiNo
                        Diferentes()
                    finSi
                finSi
            SiNo
                Si reg_Maestro.Clave.Farmacia < reg_Movimientos.Clave.Farmacia Entonces
                    GRABAR(arch_MaestroActualizado, reg_Maestro)
                    Leer_Maestro()
                SiNo
                    Diferentes()
                finSi
            finSi
        finMientras
        Cerrar(arch_Maestro); Cerrar(arch_MaestroActualizado)
        Cerrar(arch_Movimientos); Cerrar(arch_Vencidos)
    finProceso
finAccion
```
## Relaciones


