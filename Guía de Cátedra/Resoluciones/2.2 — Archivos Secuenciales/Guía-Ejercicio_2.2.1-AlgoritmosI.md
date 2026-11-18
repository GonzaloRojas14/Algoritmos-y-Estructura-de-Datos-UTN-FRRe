

**Fecha de inicio:** 28-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia con los datos de los alumnos de la facultad:
### Registro de Entrada
- Apellido y Nombre
- Carrera (ISI - IEM - IQ)
- Nº de Legajo
- Fecha de Nacimiento
- Fecha de Ingreso
- D.N.I.
- Sexo (M o F)
- Fecha de último examen aprobado
- Nota
### Requisitos
Se desea un listado de los mismos, con el siguiente formato:

| <span class="celda-gris">Nro_Legago</span> | Apellido_Nombre | Documento | Carrera |
| ------------------------------------------ | --------------- | --------- | ------- |
|                                            |                 |           |         |

## Resolución
``` less
Accion Guía-Ejercicio_2.2.1-AlgoritmosI Es
    Ambiente
        Alumnos = Registro
            Apellido_Nombre: AN(100)
            Carrera: ("ISI", "IEM", "IQ")
            Nro_Legajo: N(5)
            Fecha_Ingreso: Fecha
            DNI: N(8)
            Sexo: ("M", "F")
            Fecha_UltExamenAprobado: Fecha 
            Nota: (1..10)
        finRegistro

        Fecha = Registro
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro

        arch_alumnos: Archivo de Alumnos
        reg_alumnos: Registro de Alumnos


        Procedimiento Inicializar() Es
            Abrir E/(arch_alumnos);
            Leer(arch_alumnos, reg_alumnos)
            Escribir("Nro_Legajo | Apellido y Nombre | Documento | Carrera")
        finProcedimiento

        Procedimiento Escribir_Reg() Es
            Escribir(reg_alumnos.Nro_Legajo,reg_alumnos.Apellido_Nombre,reg_alumnos.DNI,reg_alumnos.Carrera)
        finProcedimiento
    finAmbiente
    Proceso
        Inicializar()
        Mientras NFDS(arch_alumnos) Hacer
            Escribir_Reg()
            Leer(arch_alumnos, reg_alumnos)
        finMientras
        Escribir_Reg()
        Cerrar(arch_alumnos);Cerrar(arch_salida)
    finProceso
finAccion
```
## Relaciones


