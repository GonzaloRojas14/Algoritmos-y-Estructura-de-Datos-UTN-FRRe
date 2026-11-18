**Fecha de inicio:** 19-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
El siguiente es un ejercicio del primer recuperatorio del primer parcial del año 2017:

La AFIP dispone de dos secuencias de caracteres:

- **PERSONAS** Contiene los siguientes datos de personas físicas o Empresas: nombre completo y fecha (de nacimiento o de creación, respectivamente), agrupadas por provincias. No existe carácter separador entre personas, el fin de cada provincia se indica con el carácter &.  
    Ejemplo: `María Góm-14021977Carlos Alberto Rodriguez-20061990....&Lionel Messi-24061987....&....{fin}` `nombre-ddmmaaaanombre-ddmmaa....&`
    
- **CUIT**: contiene la Clave Unica de Identificación Tributaria de las personas de la secuencia PERSONAS (existiendo una correspondencia una a una, es decir la primer persona con el primer cuit, la segunda con el segundo y asi sucesivamente) Cada número de CUIT se almacena por medio de 11 caracteres: los 2 primeros indican el tipo, los 6 siguientes el número de DNI (en caso de personas físicas) o de sociedad (en caso de Empresas) y el último es un digito verificador.  
    Ejemplo: `**20123456786**23134567823**30712434445**`
    

Los tipos pueden ser:20, 23, 24 y 27 para Personas Físicas y 30, 33 y 34 para Empresas.

Se solicita.

1. Generar una secuencia de salida que contenga DNI, y el nombre completo de todas las personas físicas cuyo nombre comience con vocal.
2. Para cada Provincia calcular el total de personas físicas y el porcentaje sobre el total de la provincia.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.30-AlgoritmosI Es
    Ambiente
        PERSONAS, CUIT, sec_salida: Secuencia de Caracter
        v_persona, v_cuit: Caracter

        total, total_personas, i, nro_provincia: Entero

        cod_personas: (20, 23, 24, 27)
        vocales: ("A", "E", "I", "0", "U")

        Procedimiento inicializar() Es
            ARR(PERSONAS);ARR(CUIT)
            CREAR(sec_salida)
            AVZ(PERSONAS, v_persona); AVZ(CUIT, v_cuit)
            total:= 0;total_personas:= 0; i:= 0; nro_provincia:= 1
        finProcedimiento
        
        Procedimiento avanzar(num: Entero, sec: AlfaNumerico) Es
            Si sec = "P" Entonces
                Para i:= 1 hasta num Hacer
                    AVZ(PERSONAS, v_persona)
                finPara
            SiNo
                Si sec = "C" Entonces
                    Para i:= 1 hasta num Hacer
                        AVZ(CUIT, v_cuit)
                    finPara
                finSi
        finProcedimiento

        Procedimiento grabarPersona() Es
            Para i:=0 hasta 7 Hacer
               GRABAR(sec_salida, v_cuit)
               AVZ(CUIT, v_cuit)
            finPara
            avanzar(2, "C")
            Mientras v_persona <> "-" Hacer
                GRABAR(sec_salida, v_persona)
                AVZ(PERSONAS, v_persona)
            finMientras
            avanzar(9, "P")
        finProcedimiento

        

        Funcion ANaN(): Entero Es
            Ambiente
                num: Entero
            finAmbiente
            num:= 0; ANaN:= 0
            Para i:= 1 hasta 0, i-- Es
                Segun v_cuit Hacer
                    = "0": num:= 0
                    = "2": num:= 2
                    = "3": num:= 3
                    = "4": num:= 4
                    = "7": num:= 7
                finSegun
                ANaN:= ANaN + num*(10**i) 
                AVZ(CUIT, v_cuit)
            finPara
        finFuncion
     
    finAmbiente
    Proceso
        inicializar()
        Mientras v_cuit="*" Hacer
            AVZ(CUIT, v_cuit)
        finMientras
        Mientras NFDS(PERSONAS) Hacer
            total:= total + 1
            Si ANaN Existe En cod_personas Hacer
                total_personas:= total_personas + 1
                Si v_persona Existe En vocales Entonces
                    grabarPersona()
                SiNo
                    avanzar(10, "C");
                    Mientras v_persona <> "-" Entonces
                        AVZ(PERSONAS, v_persona)
                    finMientras
                    avanzar(9, "P")
                finSi
            SiNo
                avanzar(10, "C");
                Mientras v_persona <> "-" Entonces
                    AVZ(PERSONAS, v_persona)
                finMientras
                avanzar(9, "P")
            finSi
            Si v_persona = "&" Entonces
                Escribir("El total de personas fisicas en la provincia ", nro_provincia," es:", total_personas)
                Escribir("El porcentaje de personas fisicas es de:", (total_personas*100)/total,"%")
                total:= 0; total_personas:= 0; nro_provincia:= nro_provincia + 1
                Si NFDS(PERSONAS) Entonces
                    AVZ(PERSONAS, v_persona)
                finSi
            finSi
            Si NFDS(CUIT) Entonces
                AVZ(CUIT, v_cuit)
            finSi

        finMientras

        Cerrar(PERSONAS); Cerrar(CUIT); Cerrar(sec_salida)
    finProceso
finAccion
```
## Relaciones


