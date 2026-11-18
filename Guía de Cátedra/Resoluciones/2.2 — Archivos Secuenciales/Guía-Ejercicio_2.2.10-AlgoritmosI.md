**Fecha de inicio:** 03-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

Del archivo general de alumnos de la U.T.N. - Facultad Regional Resistencia, ordenado por carrera, se desea emitir la cantidad de alumnos correspondientes a cada carrera y el total general.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.10-AlgoritmosI Es 
    Ambiente
        Alumnos = Registro 
            Legajo: N 
            NombreApellido: AN 
            Carrera: AN 
            DNI: N
        finRegistro
        
        arch_Alumnos: Archivo de Alumnos Ordenado Por Carrera
        reg_Alumnos: Registro de Alumnos
        resg_Carrera: AN 
        cont_carrera, total: N

        Procedimiento Leer_Archivo() Es
            Leer(arch_Alumnos, reg_Alumnos)
            Si FDS(arch_Alumnos) Entonces
                reg_Alumnos.Carrera := "HV"
            finSi
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_Alumnos)
            Leer_Archivo()
            total := 0
        finProcedimiento

        Procedimiento Corte() Es
            total := total + cont_carrera
            Escribir("La cantidad de alumnos en la carrera ", resg_Carrera, " es: ", cont_carrera)
        finProcedimiento
        
    finAmbiente
    Proceso
        inicializar()
        
        Mientras reg_Alumnos.Carrera <> "HV" Hacer
            // 1. Tomamos el resguardo al inicio del nuevo grupo
            resg_Carrera := reg_Alumnos.Carrera
            cont_carrera := 0
            
            // 2. Procesamos todos los alumnos que pertenezcan a esta carrera
            Mientras reg_Alumnos.Carrera = resg_Carrera Hacer
                cont_carrera := cont_carrera + 1
                Leer_Archivo()
            finMientras
            
            // 3. Al cambiar la carrera (o llegar al HV), ejecutamos el corte
            Corte()
        finMientras
        
        Escribir("El total general de alumnos es:", total)
        Cerrar(arch_Alumnos)
    finProceso
finAccion
```
## Relaciones


