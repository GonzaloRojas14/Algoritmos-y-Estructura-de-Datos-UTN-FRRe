**Fecha de inicio:** 05-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
La Secretaria Académica de la Facultad lanza un proyecto para incentivar a aquellos alumnos que realizaron el Cursillo de Ingreso a la Universidad y no lograron aprobarlo en los turnos de Agosto y Febrero, de manera de brindarles apoyo Académico con el fin de que, en el Cursillo del año siguiente puedan aprobar los exámenes necesarios e ingresar a la Universidad.

Para esto, dicha Secretaria ­necesita crear un archivo donde se encuentren todos los aspirantes que realizaron el Cursillo de Ingreso en ambos turnos, y no lograron aprobarlo.

Los datos correspondientes a cada uno de los turnos del Cursillo dictado están almacenados en dos archivos (uno para cada turno), los cuales presentan el siguiente formato:

**ASPIRANTES** Ordenado por DNI

- `DNI`
- `ApeyNom`
- `Carrera`
- `F_Nac`
- `Email`
- `ColegioSec`
- `FechaInscripcion`
- `Aprobado: (Si/No)`

UD debe realizar un algoritmo que permita mezclar los archivos Aspirantes (de Agosto y Febrero) y generar un archivo SEGUIMIENTO con el siguiente formato:

**SEGUIMIENTO** Ordenado por DNI

- `DNI`
- `ApeyNom`
- `Email`
- `ColegioSec`

Al finalizar el proceso informar la cantidad de aspirantes que se grabaron en el archivo SEGUIMIENTO.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.17-AlgoritmosI Es
    Ambiente
        
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro

        Aspirantes = Registro
            DNI: N 
            ApeyNom: AN 
            Carrera: AN 
            Fecha_Nac: Fecha
            Email: AN 
            ColegioSec: AN 
            Fecha_Inscripcion: Fecha 
            Aprobado: ("Si", "No")
        finRegistro

        Seguimiento = Registro
            DNI: N 
            ApeyNom: AN 
            Email: AN 
            ColegioSec: AN
        finRegistro

        arch_AspirantesAgosto, arch_AspirantesFebrero: Archivo de Aspirantes Ordenado Por DNI
        reg_AspirantesAgosto, reg_AspirantesFebrero: Aspirantes

        arch_Salida: Archivo de Seguimiento
        reg_Salida: Seguimiento

        cont: N

        Procedimiento Leer_Agosto() Es
            Leer(arch_AspirantesAgosto, reg_AspirantesAgosto)
            Si FDA(arch_AspirantesAgosto) Entonces
                reg_AspirantesAgosto.DNI:= HV 
            finSi
        finProcedimiento

        Procedimiento Leer_Febrero() Es
            Leer(arch_AspirantesFebrero, reg_AspirantesFebrero)
            Si FDA(arch_AspirantesFebrero) Entonces
                reg_AspirantesFebrero.DNI:= HV 
            finSi
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_AspirantesAgosto); Abrir E/(arch_AspirantesFebrero); Abrir S/(arch_Salida)
            Leer_Agosto();Leer_Febrero()
            cont:= 0
        finProcedimiento


    finAmbiente
    Proceso
        inicializar()
        Mientras reg_AspirantesAgosto.DNI <> HV o reg_AspirantesFebrero.DNI <> HV Hacer
            Si reg_AspirantesAgosto.DNI = reg_AspirantesFebrero.DNI   Entonces
                Si reg_AspirantesAgosto.Aprobado="No" y reg_AspirantesFebrero.Aprobado="No" Entonces
                    reg_Salida.DNI:= reg_AspirantesAgosto.DNI
                    reg_Salida.ApeyNom:= reg_AspirantesAgosto.ApeyNom
                    reg_Salida.Email:= reg_AspirantesAgosto.Email
                    reg_Salida.ColegioSec:= reg_AspirantesAgosto.ColegioSec
                    GRABAR(arch_Salida, reg_Salida)
                    cont:= cont + 1
                finSi
                Leer_Agosto();Leer_Febrero()
            SiNo
                Si reg_AspirantesAgosto.DNI < reg_AspirantesFebrero.DNI Entonces
                    Leer_Agosto()
                SiNo
                    Leer_Febrero()
                finSi
            finSi
        finMientras
        Escribir("Cantidad de Aspirantes Grabados:", cont)
        Cerrar(arch_AspirantesAgosto); Cerrar(arch_AspirantesFebrero); Cerrar(arch_Salida)
    finProceso
finAccion
```
## Relaciones


