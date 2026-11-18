

**Fecha de inicio:** 04-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dados el siguiente fichero con datos de un censo de la ciudad de Resistencia:

**CENSO** Ordenado por Radio, Manzana, Nro_Vivienda

- Radio
- Manzana
- Nro_Vivienda
- Condicion_Vivienda
- Cantidad_Habitantes

Condición puede ser : Muy Buena, Buena o Mala. Obtener los siguientes totales de personas que habitan en viviendas cuya condición es muy buena: total en la ciudad y totales por Radio y Manzana).
## Resolución
``` less
Accion Guía-Ejercicio_2.2.14-AlgoritmosI Es
    Ambiente
        Censo = Registro 
            Clave = Registro
                Radio: N 
                Manzana: N 
                Nro_Vivienda: N 
            finRegistro
            CondicionVivienda: ("Muy Buena", "Buena", "Mala")
            Cantidad_Habitantes: N 
        finRegistro
        arch_Censo: Archivo de Censo Ordenado Por Clave
        reg_Censo: Registro de Censo
        cont_Manzana, cont_Radio, total: N 
        resg_Manzana, resg_Radio: N 

        Procedimiento inicializar() Es
            Abrir E/(arch_Censo)
            Leer(arch_Censo, reg_Censo)
            cont_Manzana:= 0
            cont_Radio:= 0 
            total:= 0
            resg_Manzana:= reg_Censo.Clave.Manzana
            resg_Radio:= reg_Censo.Clave.Radio

        finProcedimiento

        Procedimiento Corte_Manzana() Es
            cont_Radio:= cont_Radio + cont_Manzana
            Escribir("La cantidad de habitantes en la Manzana", resg_Manzana, "es:", cont_Manzana)
            cont_Manzana:= 0
            resg_Manzana:= reg_Censo.Clave.Manzana
        finProcedimiento

        Procedimiento Corte_Radio() Es 
            Corte_Manzana()
            total:= total + cont_Radio
            Escribir("La cantidad de habitantes en el radio", resg_Radio, "es:", cont_Radio)
            cont_Radio:= 0
            resg_Radio:= reg_Censo.Clave.Radio 
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(arch_Censo) Hacer
            Si resg_Radio <> reg_Censo.Clave.Radio Entonces
                Corte_Radio()
            SiNo
                Si resg_Manzana <> reg_Censo.Clave.Manzana Entonces
                    Corte_Manzana()
                finSi
            finSi
            Si reg_Censo.CondicionVivienda = "Muy Buena" Entonces
                cont_Manzana:= cont_Manzana + reg_Censo.Cantidad_Habitantes
            finSi
            Leer(arch_Censo, reg_Censo)
        finMientras
        Corte_Radio()
        Escribir("Total de habitantes con Condicion de Vivienda muy buena es:", total)
        Cerrar(arch_Censo)
    finProceso
finAccion
```
## Relaciones


