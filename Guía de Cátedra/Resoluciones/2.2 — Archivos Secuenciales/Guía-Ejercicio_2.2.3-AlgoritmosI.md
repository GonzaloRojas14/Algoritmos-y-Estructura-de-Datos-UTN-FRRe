

**Fecha de inicio:** 28-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada la siguiente secuencia de datos con el siguiente formato:

- Nº de socio
- Nº de teléfono
- Apellido y Nombre
- Carrera (ISI - IEM - IQ - LAR)
- Domicilio
- Cantidad de unidades prestadas

Correspondiente a los alumnos socios de la Biblioteca, generar la secuencia de los alumnos de “ISI” que tengan prestadas más de 4 unidades bibliográficas.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.3-AlgoritmosI Es
    Ambiente
        Alumno = Registro
            Nro_Socio: N
            Nro_Telefono: AN 
            ApellidoNombre: AN 
            Carrera: ("ISI","IEM","IQ","LAR")
            Domicilio: AN 
            Cant_UnidadesPrestadas: N 
        finRegistro
        sec_alumnos: Secuencia de Alumno
        v_alumnos: Registro de Alumno
        sec_salida: Secuencia de Alumno

        Procedimiento inicializar() Es
            ARR(sec_alumnos); CREAR(sec_salida)
            AVZ(sec_alumnos, v_alumnos)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec_alumnos) Hacer
            Si v_alumnos.Carrera="ISI" y v_alumnos.Cant_UnidadesPrestadas > 4 Entonces
                GRABAR(sec_salida, v_alumnos)
            finSi
            AVZ(sec_alumnos, v_alumnos)
        finMientras
        Si v_alumnos.Carrera="ISI" y v_alumnos.Cant_UnidadesPrestadas > 4 Entonces
            GRABAR(sec_salida, v_alumnos)
        finSi
        Cerrar(sec_alumnos); Cerrar(sec_salida)
    finProceso
finAccion
```
## Relaciones


