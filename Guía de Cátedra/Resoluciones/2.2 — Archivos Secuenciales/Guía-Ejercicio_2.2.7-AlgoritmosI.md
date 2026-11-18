

**Fecha de inicio:** 01-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

Se dispone de un archivo con los datos de un padrón electoral con la siguiente información:

- Nombre y apellido
- Clase
- DNI
- Dirección
- Nº de Mesa
- Observaciones
- Nº de Circuito
- Partido (0= independiente, 1=‘A’, 2=‘B’, 3=‘C’)

Generar:  
a) Una secuencia de salida con nombre y apellido, DNI, y dirección de todas las personas afiliadas al partido “C”.  
b) Una secuencia de salida con nombre y apellido, DNI, y dirección de todas las personas no afiliadas a ningún partido y de clase posterior a 1940.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.7-AlgoritmosI Es
    Ambiente
        Padron = Registro
            NombreApellido: AN 
            Clase: N 
            DNI: N
            Direccion: AN 
            Nro_Mesa: N 
            Observaciones: AN 
            Nro_Circuito: N 
            Partido: (0..3)
        finRegistro

        Persona = Registro 
            NombreApellido: AN 
            DNI: N 
            Direccion: AN
        finRegistro

        arch_Padron: Archivo de Padron
        reg_Padron: Registro de Padron 
        sec_salidaA, sec_salidaB: Secuencia de Persona
        reg_salida: Registro de Persona

        Procedimiento GRABAR_SALIDA(sec: Caracter) Es
            reg_salida.NombreApellido:= reg_Padron.NombreApellido
            reg_salida.DNI:= reg_Padron.DNI
            reg_salida.Direccion:= reg_Padron.Direccion
            Segun sec Hacer
                = "A" : GRABAR(sec_salidaA, reg_salida)
                = "B" : GRABAR(sec_salidaB, reg_salida)
            finSegun
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_Padron); CREAR(sec_salidaA); CREAR(sec_salidaB)
            Leer(arch_Padron, reg_Padron)
        finProcedimiento
    finAmbiente
    Proceso
        inicializar() 
        Mientras NFDS(arch_Padron) Hacer
            Si reg_Padron.Partido = 3 Entonces
                GRABAR_SALIDA("A")
            SiNo
                Si reg_Padron.Partido= 0 y reg_Padron.Clase > 1940 Entonces
                    GRABAR_SALIDA("B")
                finSi
            finSi
            Leer(arch_Padron, reg_Padron)
        finMientras
        Si reg_Padron.Partido = 3 Entonces
            GRABAR_SALIDA("A")
        SiNo
            Si reg_Padron.Partido= 0 y reg_Padron.Clase < 1940 Entonces
                GRABAR("B")
            finSi
        finSi
        Cerrar(arch_Padron); Cerrar(sec_salidaA); Cerrar(sec_salidaB)
    finProceso
finAccion
```
## Relaciones


