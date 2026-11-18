

**Fecha de inicio:** 19-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
La empresa Ideas Argentinas S.A. posee datos de sus empleados en dos secuencias de caracteres; la primera secuencia (Sec1) formada por los nombres (uno por persona) de los empleados separados por blancos y la segunda secuencia (Sec2) posee los números de documento de cada uno de los empleados (palabras de 8 dígitos numéricos). Ambas secuencias poseen la misma cantidad de datos, es decir al primer nombre de la primera secuencia le corresponde el primer número de documento de la segunda secuencia y así sucesivamente. La secuencia de números de documentos no posee espacios en blanco ni ningún otro tipo de caracter que separe un número de documento de otro.  
A la empresa le interesa tener en una nueva secuencia (Sec3) los datos de todas aquellas personas que cumplan la condición de que el nombre se encuentre en una posición impar. La nueva secuencia debe generarse de la siguiente manera: el número de documento seguido (sin espacios) por una coma y luego (sin espacios) por el nombre y seguido al nombre un #.
## Resolución
``` less
Accion Guía-Ejercicio_2.1.22-AlgoritmosI Es
    Ambiente
        Sec1, Sec2, Sec3: Secuencia de Caracter
        v1, v2: Caracter
        par: Booleano
        i: Entero
        
        Procedimiento inicializar() Es
            ARR(Sec1); ARR(Sec2)
            AVZ(Sec1, v1); AVZ(Sec2, v2)
            CREAR(Sec3)
            par:= Falso
        finProcedimiento
        Procedimiento grabarNombre() Es
            Para i:= 1 hasta 7 Hacer
                GRABAR(Sec3, v2)
                AVZ(Sec2, v2)
            finPara
            GRABAR(Sec3, v2)
            Si NFDS(Sec2) Entonces
                AVZ(Sec2, v2)
            finSi
            GRABAR(Sec3, ",")
            Mientras v1 <> " " y NFDS(Sec1) Hacer
                GRABAR(Sec3, v1)
                AVZ(Sec1, v1)
            finMientras
            Si v1 <> " " Entonces
                GRABAR(Sec3, v1)
            SiNo
                Si NFDS(Sec1) Entonces
                    AVZ(Sec1, v1)
                finSi
            finSi
            GRABAR(Sec3, "#")
        finProcedimiento
        
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(Sec1) Hacer
            Si par Entonces
                Para i:= 1 hasta 7 Hacer
                    AVZ(Sec2, v2)
                finPara
                Si NFDS(Sec2) Entonces
                    AVZ(Sec2, v2)
                finSi
                Mientras v1 <> " " y NFDS(Sec1) Hacer
                    AVZ(Sec1, v1)
                finMientras
                Si NFDS(Sec1) Entonces
                    AVZ(Sec1, v1)
                finSi
                par:= Falso
            SiNo
                grabarNombre()
                par:= Verdadero
            finSi
        finMientras
        Cerrar(Sec1)
        Cerrar(Sec2)
        Cerrar(Sec3)
    finProceso
finAccion
```
## Relaciones


