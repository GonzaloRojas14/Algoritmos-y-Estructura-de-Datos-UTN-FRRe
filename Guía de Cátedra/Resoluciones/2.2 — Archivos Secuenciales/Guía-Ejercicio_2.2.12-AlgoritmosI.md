**Fecha de inicio:** 03-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada una secuencia con información de población de un PAIS:

**POBLACION** Ordenado por Provincia, Departamento, Ciudad, Barrio, ID_Casa

- Provincia
- Departamento
- Ciudad
- Barrio
- ID_Casa
- Cantidad_Habitantes

Generar una secuencia con información de los departamentos de esa provincia, cuyo registro tenga el siguiente formato:

**POBLACION_SALIDA**

- Provincia
- Departamento
- Cantidad_Habitantes
## Resolución
``` less
Accion Guía-Ejercicio_2.2.12-AlgoritmosI Es
    Ambiente
        Poblacion = Registro
            Clave = Registro
                Provincia: AN
                Departamento: AN
                Ciudad: AN

                Barrio: AN

                ID_Casa: N
            finRegistro

            Cantidad_Habitantes: N    
        finRegistro
        Poblacion_Salida = Registro 
            Provincia: AN
            Departamento: AN
            Cantidad_Habitantes: N
        finRegistro
        sec_Poblacion: Secuencia de Poblacion
        sec_Salida: Secuencia de Poblacion_Salida
        reg_Poblacion: Registro de Poblacion
        reg_Salida: Registro de Poblacion_Salida 
        resg_Provincia, resg_Departamento: AN
        cont_Departamento: N
        Procedimiento Corte_Departamento() Es
            reg_Salida.Provincia := resg_Provincia
            reg_Salida.Departamento := resg_Departamento
            reg_Salida.Cantidad_Habitantes := cont_Departamento

            GRABAR(sec_Salida, reg_Salida)
            cont_Departamento := 0
            resg_Departamento := reg_Poblacion.Clave.Departamento
        finProcedimiento

        Procedimiento Corte_Provincia() Es
            Corte_Departamento()
            resg_Provincia := reg_Poblacion.Clave.Provincia
        finProcedimiento

        Procedimiento inicializar() Es
            ARR(sec_Poblacion)
            CREAR(sec_Salida)
            AVZ(sec_Poblacion, reg_Poblacion)
            cont_Departamento := 0
            resg_Provincia := reg_Poblacion.Clave.Provincia
            resg_Departamento := reg_Poblacion.Clave.Departamento
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec_Poblacion) Hacer
            Si resg_Provincia <> reg_Poblacion.Clave.Provincia Entonces
                Corte_Provincia()
            SiNo
                Si resg_Departamento <> reg_Poblacion.Clave.Departamento Entonces
                    Corte_Departamento()
                finSi
            finSi
            cont_Departamento := cont_Departamento + reg_Poblacion.Cantidad_Habitantes
            AVZ(sec_Poblacion, reg_Poblacion)
        finMientras
        Corte_Provincia()
        Cerrar(sec_Poblacion)
        Cerrar(sec_Salida)
    finProceso
finAccion
```
## Relaciones


