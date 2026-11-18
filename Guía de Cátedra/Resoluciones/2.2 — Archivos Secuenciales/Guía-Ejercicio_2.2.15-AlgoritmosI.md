

**Fecha de inicio:** 04-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
El organismo del cual dependen las escuelas de un distrito lleva un archivo con los registros para todos los alumnos de nivel secundario de ese distrito:

**ALUMNOS** Ordenado por Escuela, Año, División

- Escuela
- Año
- División
- Nombre
- Cant_Inasistencias

Se introduce como dato el número de distrito y la cantidad de días de clase dictados en el año. El archivo está ordenado por número de escuela, año y división. Los alumnos que superan el 20% de las inasistencias están en situación de LIBRES, de lo contrario son REGULARES.

Se desea conocer:  
**Para cada división:**  
- Cantidad de alumnos  
**Para cada año:**  
- Cantidad total de alumnos libres  
- Cantidad de alumnos regulares  
- Cantidad total de alumnos  
**Todas las escuelas:**  
- Cantidad total de alumnos  
- Porcentaje de alumnos libres. - Promedio de inasistencias por alumnos.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.15-AlgoritmosI Es
    Ambiente
        Alumnos = Registro
            Clave = Registro
                Escuela: AN 
                Año: N 
                Division: N 
            finRegistro
            Nombre: AN 
            Cant_Inasistencias: N
        finRegistro
        arch_Alumnos: Archivo de Alumnos Ordenado Por Clave
        reg_Alumnos: Registro de Alumnos

        resg_Escuela: AN 
        resg_Año, resg_Division: N 

        cont_Alumnos_Division, cont_Alumnos_Año, cont_regulares, cont_libres, total, total_libres, total_inasistencias: N
        var_DiasClase, Nro_Distrito: N 

        Procedimiento Corte_Division() Es
            cont_Alumnos_Año:= cont_Alumnos_Año + cont_Alumnos_Division
            Escribir("La cantidad de alumnos en la Division", resg_Division, "es:", cont_Alumnos_Division)
            cont_Alumnos_Division:= 0
            resg_Division:= reg_Alumnos.Clave.Division
        finProcedimiento

        Procedimiento Corte_Año() Es
            Corte_Division()
            total:= total+ cont_Alumnos_Año
            total_libres:= total_libres + cont_libres
            Escribir("Analisis del año", resg_Año)
            Escribir("Alumnos Libres:", cont_libres)
            Escribir("Alumnos Regulares:", cont_regulares)
            Escribir("Total de Alumnos:", cont_Alumnos_Año)
            resg_Año:= reg_Alumnos.Clave.Año
            cont_Alumnos_Año:= 0
            cont_libres:= 0
            cont_regulares:= 0
        finProcedimiento

        Procedimiento Corte_Escuela() Es
            Corte_Año()
            Escribir("Analisis Escuela:", resg_Escuela)
            Escribir("Cantidad Total De Alumnos:", total)
            Escribir("Porcentaje de alumnos libres:", (total_libres*100)/total)
            Escribir("Promedio de inasistencia:", total_inasistencias/total)
            total:= 0
            total_inasistencias:= 0
            total_libres:= 0
            resg_Escuela:= reg_Alumnos.Clave.Escuela
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_Alumnos)
            Leer(arch_Alumnos, reg_Alumnos)
            
            // Contadores
            cont_Alumnos_Division:= 0
            cont_Alumnos_Año:= 0
            cont_regulares:= 0
            cont_libres:= 0 
            total:= 0 
            total_libres:= 0
            total_inasistencias:= 0

            // Resguardos
            resg_Año:= reg_Alumnos.Clave.Año
            resg_Division:= reg_Alumnos.Clave.Division
            resg_Escuela:= reg_Alumnos.Clave.Escuela

            // Datos Usuario
            Escribir("Ingrese Distrito:")
            Leer(Nro_Distrito)
            Escribir("Ingrese Total de dias de clase:")
            Leer(var_DiasClase)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(arch_Alumnos) Hacer
            Si resg_Escuela<>reg_Alumnos.Clave.Escuela Entonces
                Corte_Escuela()
            SiNo
                Si resg_Año<>reg_Alumnos.Clave.Año Entonces
                    Corte_Año()
                SiNo
                    Si resg_Division<>reg_Alumnos.Clave.Division Entonces
                        Corte_Division()
                    finSi
                finSi
            finSi

            cont_Alumnos_Division:= cont_Alumnos_Division + 1
            total_inasistencias:= total_inasistencias + reg_Alumnos.Cant_Inasistencias
            Si reg_Alumnos.Cant_Inasistencias>(var_DiasClase*0.2) Entonces
                cont_libres:= cont_libres + 1
            SiNo
                cont_regulares:= cont_regulares + 1
            finSi
            Leer(arch_Alumnos, reg_Alumnos)
        finMientras
        Corte_Escuela()
        Cerrar(arch_Alumnos)
    finProceso
finAccion
```
## Relaciones


