**Fecha de inicio:** 31-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
A partir de la secuencia del ejercicio 2.01 se desea generar un listado con los alumnos que aprobaron la última materia rendida con nota superior a 7, e ingresaron el año pasado, con el siguiente formato:

| Nro_Legajo | Apellido_Nombre | Carrera |
| ---------- | --------------- | ------- |
|            |                 |         |
## Resolución
``` less
Accion Guía-Ejercicio_2.2.5-AlgoritmosI Es 
    Ambiente
        Fecha = Registro
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        
        Alumnos = Registro
            Apellido_Nombre: AN(100)
            Carrera: ("ISI", "IEM", "IQ")
            Nro_Legajo: N(5)
            Fecha_Nacimiento: Fecha 
            Fecha_Ingreso: Fecha
            DNI: N(8)
            Sexo: ("M", "F")
            Fecha_UltExamenAprobado: Fecha 
            Nota: (1..10)
        finRegistro
        sec_Alumnos: Secuencia de Alumnos
        v_Alumnos: Registro de Alumnos

        Procedimiento inicializar() Es
            ARR(sec_Alumnos)
            AVZ(sec_Alumnos, v_Alumnos)
            Escribir("Nro legajo | Apellido y Nombre | Carrera")

        finProcedimiento
    finAmbiente
    Proceso
	    inicializar()
        Mientras NFDS(sec_Alumnos) Hacer
            Si v_Alumnos.Nota>7 y v_Alumnos.Fecha_Ingreso.año = 2025 Entonces
                Escribir(v_Alumnos.Nro_Legajo, "|", v_Alumnos.Apellido_Nombre, "|", v_Alumnos.Carrera)
            finSi
            AVZ(sec_Alumnos, v_Alumnos)
        finMientras
        Si v_Alumnos.Nota>7 y v_Alumnos.Fecha_Ingreso.año = 2025 Entonces
            Escribir(v_Alumnos.Nro_Legajo, "|", v_Alumnos.Apellido_Nombre, "|", v_Alumnos.Carrera)
        finSi
        Cerrar(sec_Alumnos)
    finProceso
finAccion
```
## Relaciones


