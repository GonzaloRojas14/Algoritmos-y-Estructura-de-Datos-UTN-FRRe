

**Fecha de inicio:** 31-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
A partir de la secuencia del ejercicio ![[Guía-Ejercicio_2.2.1-AlgoritmosI#Registro de Entrada]] se desea generar otra secuencia con los alumnos de una carrera dada que aprobaron alguna materia este año, con nota mayor a 7 (siete).
## Resolución
``` less
Accion Guía-Ejercicio_2.2.4-AlgoritmosI Es    
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

        sec_Alumnos, sec_salida: Secuencia de Alumnos
        v_alumnos: Registro de Alumnos
        carrera: AN
        bandera: Booleano
        Procedimiento inicializar() Es
            ARR(sec_Alumnos); CREAR(sec_salida)
            AVZ(sec_Alumnos, v_alumnos)
            bandera:= Verdadero
            Escribir("Escribe la carrera que quieres:")
            Mientras bandera Hacer
                Leer(carrera)
                Si carrera Existe En ("ISI", "IEM", "IQ") Entonces
                    bandera:=Falso
                SiNo
                    Escribir("Ingresa una carrera valida")
                finSi
            finMientras
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec_Alumnos) Hacer 
            Si v_alumnos.Carrera = carrera y v_alumnos.Nota>7 Entonces
                GRABAR(sec_salida,v_alumnos)
            finSi
            AVZ(sec_Alumnos,v_alumnos)
        finMientras
        Si v_alumnos.Carrera = carrera y v_alumnos.Nota>7 Entonces
            GRABAR(sec_salida,v_alumnos)
        finSi
        Cerrar(sec_Alumnos); Cerrar(sec_salida)
    finProceso
finAccion
```
## Relaciones


