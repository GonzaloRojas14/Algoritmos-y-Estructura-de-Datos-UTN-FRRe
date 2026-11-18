**Fecha de inicio:** 03-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de un archivo con datos de los alumnos de la U.T.N. con la siguiente información para cada alumno:

**Alumnos** Ordenado por Sexo, Carrera, Nro_Legajo

- Sexo
- Carrera
- Nro_Legajo
- Fecha_Ingreso
- Total_Materias_Aprobadas

Se desea un listado con el siguiente detalle por sexo, carrera y total general

1. Total de alumnos que ingresaron en el año 2009 con más de 20 materias aprobadas.
    
2. Total de alumnos que ingresaron en el año 2009 con menos de 20 materias aprobadas
## Resolución
``` less
Accion Guía-Ejercicio_2.2.11-AlgoritmosI Es
    Ambiente
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        
        Alumnos = Registro
            Sexo: AN
            Carrera: AN 
            Nro_Legajo: N 
            Fecha_Ingreso: Fecha
            Total_MateriasAprobadas: N 
        finRegistro
        
        arch_Alumnos: Archivo de Alumnos Ordenado Por Sexo, Carrera, Nro_Legajo
        reg_Alumnos: Registro de Alumnos 
        
        cont_carreraMas, cont_carreraMenos: N
        cont_sexoMas, cont_sexoMenos: N
        total_Mas, total_Menos: N 
        resg_sexo, resg_carrera: AN

        Procedimiento Corte_Carrera() Es
            // 1. Acumular al nivel superior (Sexo)
            cont_sexoMas := cont_sexoMas + cont_carreraMas
            cont_sexoMenos := cont_sexoMenos + cont_carreraMenos
            
            // 2. Mostrar subtotales
            Escribir("Carrera: ", resg_carrera, " | Sexo: ", resg_sexo)
            Escribir(" - Ingresantes 2009 con más de 20 materias: ", cont_carreraMas)
            Escribir(" - Ingresantes 2009 con menos de 20 materias: ", cont_carreraMenos)
            
            // 3. Reiniciar contadores del nivel actual
            cont_carreraMas := 0
            cont_carreraMenos := 0
            
            // 4. Actualizar el resguardo
            resg_carrera := reg_Alumnos.Carrera
        finProcedimiento

        Procedimiento Corte_Sexo() Es
            // 1. Llamar al corte menor por cascada
            Corte_Carrera() 
            
            // 2. Acumular al nivel superior (Total General)
            total_Mas := total_Mas + cont_sexoMas
            total_Menos := total_Menos + cont_sexoMenos
            
            // 3. Mostrar subtotales
            Escribir("Total Sexo ", resg_sexo, " con más de 20 materias: ", cont_sexoMas)
            Escribir("Total Sexo ", resg_sexo, " con menos de 20 materias: ", cont_sexoMenos)
            
            // 4. Reiniciar contadores del nivel actual
            cont_sexoMas := 0
            cont_sexoMenos := 0
            
            // 5. Actualizar el resguardo
            resg_sexo := reg_Alumnos.Sexo
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_Alumnos)
            Leer(arch_Alumnos, reg_Alumnos)
            
            // Cargar primeros resguardos
            resg_sexo := reg_Alumnos.Sexo
            resg_carrera := reg_Alumnos.Carrera
            
            // Inicializar contadores en cero
            cont_carreraMas := 0; cont_carreraMenos := 0
            cont_sexoMas := 0; cont_sexoMenos := 0
            total_Mas := 0; total_Menos := 0
        finProcedimiento
    finAmbiente

    Proceso
        inicializar()
        
        Mientras NFDS(arch_Alumnos) Hacer
            // Evaluación de cortes de mayor a menor jerarquía
            Si resg_sexo != reg_Alumnos.Sexo Entonces
                Corte_Sexo()
            SiNo
                Si resg_carrera != reg_Alumnos.Carrera Entonces
                    Corte_Carrera()
                finSi
            finSi

            // Procesamiento del registro actual
            Si reg_Alumnos.Fecha_Ingreso.Año = 2009 Entonces
                Si reg_Alumnos.Total_MateriasAprobadas > 20 Entonces
                    cont_carreraMas := cont_carreraMas + 1
                SiNo
                    Si reg_Alumnos.Total_MateriasAprobadas < 20 Entonces
                        cont_carreraMenos := cont_carreraMenos + 1
                    finSi
                finSi
            finSi

            Leer(arch_Alumnos, reg_Alumnos)
        finMientras
        
        // El último corte mayor dispara también al menor
        Corte_Sexo() 
        
        Escribir("Total general con más de 20 materias: ", total_Mas)
        Escribir("Total general con menos de 20 materias: ", total_Menos)
        
        Cerrar(arch_Alumnos)
    finProceso
finAccion
```
## Relaciones


