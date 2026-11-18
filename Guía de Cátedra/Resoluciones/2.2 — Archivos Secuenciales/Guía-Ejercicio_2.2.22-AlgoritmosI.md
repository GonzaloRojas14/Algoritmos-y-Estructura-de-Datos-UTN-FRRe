**Fecha de inicio:** 08-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
IDEM ejercicio 2.21 pero agregando al enunciado: “Al finalizar el proceso se desea conocer: el usuario que posee más amigos.”
## Resolución
``` less
Accion Guía-Ejercicio_2.2.21-AlgoritmosI Es
    Ambiente
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        
        Amigos = Registro
            Clave = Registro
                Cod_Usuario: N 
                Cod_Amigo: N 
            finRegistro
            Fecha_Amistad: Fecha 
            Mensaje_Muro: AN
        finRegistro

        Notificaciones = Registro
            Clave = Registro
                Cod_Usuario: N 
                Cod_Amigo: N 
                Cod_Movimiento: ("A", "M", "B")
            finRegistro
            Fecha_Amistad: Fecha
            Mensaje_Muro: AN 
        finRegistro

        arch_Amigos: Archivo de Amigos Ordenado Por Clave
        arch_Notificaciones: Archivo de Notificaciones Ordenado Por Clave 
        arch_AmigosActualizado: Archivo de Amigos

        reg_Amigos, reg_AmigosActualizado: Amigos
        reg_Notificaciones: Notificaciones

        cont_Amigos, resg_amigos, resg_Usuario, UsuarioMasAmigos: N

        Procedimiento Leer_Amigos() Es
            Leer(arch_Amigos, reg_Amigos)
            Si FDA(arch_Amigos) Entonces
                reg_Amigos.Clave.Cod_Usuario:= HV
            finSi
        finProcedimiento

        Procedimiento Leer_Notificaciones() Es
            Leer(arch_Notificaciones, reg_Notificaciones)
            Si FDA(arch_Notificaciones) Entonces
                reg_Notificaciones.Clave.Cod_Usuario:= HV
            finSi
        finProcedimiento

        Procedimiento Iguales() Es
            Si reg_Notificaciones.Clave.Cod_Movimiento = "A" Entonces
                Escribir("Error:El Amigo ya existe")
                Escribir(arch_AmigosActualizado, reg_Amigos)
            SiNo
                Si reg_Notificaciones.Clave.Cod_Movimiento = "M" Entonces
                    reg_Amigos.Mensaje_Muro:= reg_Notificaciones.Mensaje_Muro
                    Escribir(arch_AmigosActualizado,reg_Amigos)
                SiNo
                    cont_Amigos:= cont_Amigos - 1
                finSi 
            finSi
            Leer_Amigos()
            Leer_Notificaciones()
        finProcedimiento
        
        Procedimiento Diferentes() Es
            Si reg_Notificaciones.Clave.Cod_Movimiento = "A" Entonces
                reg_AmigosActualizado.Clave.Cod_Usuario:= reg_Notificaciones.Clave.Cod_Usuario
                reg_AmigosActualizado.Clave.Cod_Amigo:= reg_Notificaciones.Clave.Cod_Amigo
                reg_AmigosActualizado.Fecha_Amistad:= reg_Notificaciones.Fecha_Amistad
                reg_AmigosActualizado.Mensaje_Muro:= reg_Notificaciones.Mensaje_Muro
                Escribir(arch_AmigosActualizado, reg_AmigosActualizado)
            SiNo
                Si reg_Notificaciones.Clave.Cod_Movimiento = "B" Entonces
                    Escribir("No existe amigo para dar de baja")
                    cont_Amigos:= cont_Amigos - 1
                SiNo
                    Escribir("No existe amigo para modificar")
                    cont_Amigos:= cont_Amigos - 1
                finSi
            finSi
            Leer_Notificaciones()
        finProcedimiento
        Procedimiento inicializar() Es 
            Abrir E/(arch_Amigos); Abrir E/(arch_Notificaciones); Abrir S/(arch_AmigosActualizado)
            Leer_Amigos(); Leer_Notificaciones()
            cont_Amigos:= 0; resg_amigos:= 0; resg_Usuario:= reg_Amigos.Clave.Cod_Usuario
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras reg_Amigos.Clave.Cod_Usuario <> HV o reg_Notificaciones.Clave.Cod_Usuario <> HV Hacer
            Si resg_Usuario = reg_Amigos.Clave.Cod_Usuario Entonces
                cont_Amigos:= cont_Amigos + 1
            SiNo
                Si cont_Amigos>resg_amigos Entonces
                    resg_amigos:= cont_Amigos
                    UsuarioMasAmigos:= resg_Usuario
                finSi
                cont_Amigos:= 0
                resg_Usuario:= reg_Amigos.Clave.Cod_Usuario
            finSi
            Si reg_Amigos.Clave.Cod_Usuario = reg_Notificaciones.Clave.Cod_Usuario Entonces

                Si reg_Amigos.Clave.Cod_Amigo = reg_Notificaciones.Clave.Cod_Amigo Entonces
                    Iguales()
                SiNo
                    Si reg_Amigos.Clave.Cod_Amigo < reg_Notificaciones.Clave.Cod_Amigo Entonces
                        Escribir(arch_AmigosActualizado, reg_Amigos)
                        Leer_Amigos()
                    SiNo
                        Diferentes()
                    finSi
                finSi
            SiNo
                Si reg_Amigos.Clave.Cod_Usuario < reg_Notificaciones.Clave.Cod_Usuario Entonces
                    Escribir(arch_AmigosActualizado, reg_Amigos)
                    Leer_Amigos()
                SiNo
                    Diferentes()
                finSi
            finSi
        finMientras
        Cerrar(arch_Amigos); Cerrar(arch_AmigosActualizado); Cerrar(arch_Notificaciones)
    finProceso
finAccion
```
## Relaciones


