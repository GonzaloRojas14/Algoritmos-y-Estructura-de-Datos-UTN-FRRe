**Fecha de inicio:** 08-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se desea generar una secuencia, a partir de la secuencia del problema [[Guía-Ejercicio_2.2.1-AlgoritmosI#Descripción de la tarea]], donde se actualice la fecha de aprobación del último exámen, para ello se cuenta con información del último turno de exámen, según el siguiente detalle:

**EXAMENES** Ordenado por Nro_Legajo

- Nro_Legajo
- Carrera
- Cod_Materia
- Fecha_Examen
- Nota

Se debe considerar que no necesariamente todos los alumnos se presentan en cada turno de exámen, y que un alumno puede presentarse a rendir más de una materia en un mismo turno. Supónganse ambas secuencias ordenadas por Número de Legajo.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.20-AlgoritmosI Es
    Ambiente
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro

        Alumnos = Registro 
            ApeyNombre: AN 
            Carrera: ("ISI", "IEM", "IQ")
            Nro_Legajo: N
            Fecha_Nacimiento: Fecha
            Fecha_Ingreso: Fecha
            DNI : N
            Sexo : ("M", "F")
            Fecha_UltExamenApob: Fecha
            Nota: N
        finRegistro

        Examenes = Registro
            Nro_Legajo: N
            Carrera: ("ISI", "IEM", "IQ")
            Cod_Materia: N
            Fecha_Examen: Fecha
            Nota:N
        finRegistro

        sec_Examenes: Secuencia de Examenes
        v_Examenes: Examenes
        sec_Alumnos, sec_AlumnosActualizado: Secuencia de Alumnos
        v_Alumnos: Alumnos



        Procedimiento inicializar() Es
            ARR(sec_Alumnos); ARR(sec_Examenes); CREAR(sec_AlumnosActualizado)
            Leer_Alumnos(); Leer_Examenes()
        finProcedimiento

        Procedimiento Iguales() Es
            Mientras v_Alumnos.Nro_Legajo = v_Examenes.Nro_Legajo Hacer
                Si v_Examenes.Nota >= 6 Entonces
                    Si ((v_Alumnos.Fecha_UltExamenApob.Año * 10000) + (v_Alumnos.Fecha_UltExamenApob.Mes * 100) + v_Alumnos.Fecha_UltExamenApob.Dia) < (v_Examenes.Fecha_Examen.Año * 10000) + (v_Examenes.Fecha_Examen.Mes * 100) + v_Examenes.Fecha_Examen.Dia Entonces
                        v_Alumnos.Fecha_UltExamenApob:= v_Examenes.Fecha_Examen
                        v_Alumnos.Nota:= v_Examenes.Nota 
                    finSi
                finSi
                Leer_Examenes()
            finMientras
            GRABAR(sec_AlumnosActualizado, v_Alumnos)
            Leer_Alumnos()
        finProcedimiento

        Procedimiento Leer_Alumnos() Es
            AVZ(sec_Alumnos, v_Alumnos)
            Si FDS(sec_Alumnos) Entonces
                v_Alumnos.Nro_Legajo:= HV
            finSi
        finProcedimiento

        Procedimiento Leer_Examenes() Es
            AVZ(sec_Examenes, v_Examenes)
            Si FDS(sec_Examenes) Entonces
                v_Examenes.Nro_Legajo:= HV
            finSi
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras v_Alumnos.Nro_Legajo <> HV o v_Examenes.Nro_Legajo <> HV Hacer
            Si v_Alumnos.Nro_Legajo = v_Examenes.Nro_Legajo Entonces
                Iguales()
            SiNo
                Si v_Alumnos.Nro_Legajo< v_Examenes.Nro_Legajo Entonces
                    GRABAR(sec_AlumnosActualizado, v_Alumnos)
                    Leer_Alumnos()
                SiNo
                    Escribir("Error, Alumno no encontrado")
                    Leer_Examenes()
                finSi
            finSi
        finMientras
        Cerrar(sec_Alumnos); Cerrar(sec_AlumnosActualizado); Cerrar(sec_Examenes) 
    finProceso
finAccion
```
## Relaciones


