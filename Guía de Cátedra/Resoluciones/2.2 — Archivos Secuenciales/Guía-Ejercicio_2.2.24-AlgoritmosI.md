**Fecha de inicio:** 15-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

Una obra social lleva el control de los costos que le insume cada afiliado. Considerando como costos, los pagos que la misma debe realizar (en conceptos de honorarios, pagos a farmacias, etc) por los distintos servicios que el afiliado utiliza. Para esto la empresa cuenta con un archivo **COSTOS_POR_AFILIADO**, en el cual se registran la cantidad de atenciones y/o servicios que solicita el empleado y el costo total (en pesos) que la empresa debe pagar por estos. Este archivo está conformado por registros con el siguiente formato, y está ordenado Cod_Afiliado

**COSTOS_POR_AFILIADO** Ordenado por Cod_Afiliado

- Cod_Afiliado
- Fecha_Alta
- Fecha_Baja
- Cant_Servicios
- Costo

Cada viernes en la organización, se lleva a cabo un proceso de actualización del archivo **COSTOS_POR_AFILIADO**. Para poder realizarlo se cuenta con un archivo **SERVICIOS_SEMANALES**, ordenado por cod_afiliado y fecha_at, en el cual se registran los servicios que solicitaron los afiliados durante cada semana. Cada registro de este archivo presenta el siguiente formato,

**SERVICIOS_SEMANALES** Ordenado por Cod_Afiliado

- Cod_Afiliado
- Fecha_At
- Cod_Servicio
- Costo

En el archivo **SERVICIOS_SEMANALES** puede existir más de un registro por cada afiliado.

Para realizar el proceso de actualización se deben tener en cuenta las siguientes consideraciones.

- Si algún Cod_Afiliado de serviciosSemanales, no se encuentra en ningún registro del archivo COSTOS_POR_AFILIADO, y el primer Cod_Servicio asociado al mismo es igual a 001 entonces se trata de un nuevo afiliado que fue dado de alta.
    
- Si Cod_Afiliado de serviciosSemanales es igual al de COSTOS_POR_AFILIADO y el Cod_Servicio es igual a 000 se trata de un afiliado que fue dado de baja y se considera como fecha de baja el valor que reside en Fecha_At. Si en cambio, el Cod_Servicio tiene algún otro valor este representa un servicio o atención que solicitó el afiliado; por lo tanto deben contabilizarse la cantidad de servicios que solicitó; como así también los costos que estos insumen.
    
- Si algún Cod_Afiliado de COSTOS_POR_AFILIADO no se encuentra en el archivo SERVICIOS_SEMANALES, se trata de un afiliado que no utilizó los servicios en la semana que se realiza la actualización.
    
- Cualquier otro caso distinto a los considerados anteriormente se toma como un error, y deben ser informados por pantalla; indicando claramente el motivo del error.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.24-AlgoritmosI Es
    Ambiente
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        Costo_Por_Afiliado = Registro
            Cod_Afiliado: N 
            Fecha_Alta: Fecha
            Fecha_Baja: Fecha
            Cant_Servicios: N 
            Costo: N 
        finRegistro
        Servicios_Semanales = Registro
            Cod_Afiliado: N 
            Fecha_At: Fecha
            Cod_Servicio: AN
            Costo: N 
        finRegistro

        arch_MAE: Archivo DE Costo_Por_Afiliado Ordenado Por Cod_Afiliado
        arch_Salida: Archivo de Costo_Por_Afiliado
        arch_MOV: Archivo de Servicios_Semanales Ordenado Por Cod_Afiliado
        reg_MAE, reg_Salida: Costo_Por_Afiliado
        reg_MOV: Servicios_Semanales

        Procedimiento Leer_MOV() Es
            Leer(arch_MOV, reg_MOV)
            Si FDA(arch_MOV) Entonces
                reg_MOV.Cod_Afiliado:= HV 
            finSi
        finProcedimiento
        Procedimiento Leer_MAE() Es
            Leer(arch_MAE, reg_MAE)
            Si FDA(arch_MAE) Entonces
                reg_MAE.Cod_Afiliado:= HV 
            finSi
        finProcedimiento

        Procedimiento Iguales() Es
            reg_Salida.Cod_Afiliado:= reg_MAE.Cod_Afiliado
            reg_Salida.Cant_Servicios:= reg_MAE.Cant_Servicios
            reg_Salida.Costo:= reg_MAE.Costo
            reg_Salida.Fecha_Alta:= reg_MAE.Fecha_Alta
            Mientras reg_MAE.Cod_Afiliado = reg_MOV.Cod_Afiliado Hacer
                Si reg_MOV.Cod_Servicio = "000" Entonces
                    reg_Salida.Fecha_Alta:= reg_MAE.Fecha_Alta
                    reg_Salida.Fecha_Baja:= reg_MOV.Fecha_At
                    reg_Salida.Cant_Servicios:= reg_MAE.Cant_Servicios
                    reg_Salida.Costo:= reg_MAE.Costo 
                SiNo
                    reg_Salida.Cant_Servicios:= reg_Salida.Cant_Servicios + 1
                    reg_Salida.Costo:= reg_Salida.Costo + reg_MOV.Costo
                finSi
                Leer_MOV()
            finMientras
            Escribir(arch_Salida, reg_Salida)
            Leer_MAE()
        finProcedimiento

        Procedimiento Diferentes() Es
            Si reg_MOV.Cod_Servicio = "001" Entonces
                reg_Salida.Cod_Afiliado:= reg_MOV.Cod_Afiliado
                reg_Salida.Fecha_Alta:= reg_MOV.Fecha_At
                reg_Salida.Cant_Servicios:= 0
                reg_Salida.Costo:= 0
                reg_Salida.Fecha_Baja:= HV 
                Mientras reg_MOV.Cod_Afiliado= reg_Salida.Cod_Afiliado Hacer
                    reg_Salida.Cant_Servicios:= reg_Salida.Cant_Servicios+1
                    reg_Salida.Costo:= reg_Salida.Costo+ reg_MOV.Costo
                    Leer_MOV()
                finMientras
                Escribir(arch_Salida, reg_Salida)
            SiNo
                Escribir("ERROR: Este Afiliado no fue dado de Alta en el sistema")
                Leer_MOV()
            finSi
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_MAE); Abrir E/(arch_MOV); Abrir S/arch_Salida
            Leer_MAE(); Leer_MOV()
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras reg_MAE.Cod_Afiliado<>HV o reg_MOV.Cod_Afiliado<>HV Hacer
            Si reg_MAE.Cod_Afiliado=reg_MOV.Cod_Afiliado Entonces
                Iguales()
            SiNo
                Si reg_MAE.Cod_Afiliado<reg_MOV.Cod_Afiliado Entonces
                    Escribir(arch_Salida, reg_MAE)
                    Leer_MAE()
                SiNo
                    Diferentes()
                finSi
            finSi
        finMientras
        Cerrar(arch_MAE);Cerrar(arch_MOV); Cerrar(arch_Salida)
    finProceso
finAccion
```

## Relaciones


