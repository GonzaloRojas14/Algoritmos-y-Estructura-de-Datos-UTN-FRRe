**Fecha de inicio:** 31-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

Se cuenta con una secuencia que contiene el Apellido y Nombre y Promedio General de los Graduados de una Facultad, y se solicita generar un listado con diversas recomendaciones para cubrir vacantes en una importante Empresa. Las mencionadas recomendaciones serán establecidas del siguiente modo: si el promedio es menor que 7, la recomendación será negativa ("NO"); por el contrario, si el promedio es menor que 8, la recomendación será positiva ("SI"); de lo contrario, si el promedio es menor que 9, la recomendación será favorable ("F"); por último, si el promedio supera los 9 puntos, la recomendación será muy favorable("MF"). El listado deber respetar el siguiente formato:

| Apellido_Nombre | Promedio | Recomendación |
| --------------- | -------- | ------------- |
|                 |          |               |


Además, se solicita la impresión del total de graduados que recibieron cada una de las recomendaciones, y el promedio global de los mismos.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.6-AlgoritmosI Es
    Ambiente
        Graduados = Registro
            ApellidoNombre: AN 
            PromGeneral: N(1..10)
        finRegistro

        sec_Graduados: Secuencia de Graduados
        v_Graduados: Registro de Graduados

        cont_1a7, cont_7a8, cont_8a9, cont_9a10, Total: N 
        Procedimiento inicializar() Es
            ARR(sec_Graduados)
            AVZ(sec_Graduados, v_Graduados)
            cont_1a7:=0; cont_7a8:=0; cont_8a9:=0; cont_9a10:=0; Total:= 0
            Escribir("Apellido y Nombre  |  Promedio  |  Recomendacion")
        finProcedimiento

        Procedimiento Analizar() Es
            Si v_Graduados.PromGeneral < 7 Entonces
                cont_1a7:= cont_1a7 + 1
                Escribir(v_Graduados.ApellidoNombre, "|", v_Graduados.PromGeneral, "|  NO" )
            SiNo
                Si  v_Graduados.PromGeneral < 8 Entonces
                    cont_7a8:= cont_7a8+1
                    
                    Escribir(v_Graduados.ApellidoNombre, "|", v_Graduados.PromGeneral, "|  SI" )
                SiNo
                    Si v_Graduados.PromGeneral < 9 Entonces
                        cont_8a9:= cont_8a9+1
                        
                        Escribir(v_Graduados.ApellidoNombre, "|", v_Graduados.PromGeneral, "|  F" )
                    SiNo
                        cont_9a10:= cont_9a10 +1 
                        
                        Escribir(v_Graduados.ApellidoNombre, "|", v_Graduados.PromGeneral, "|  MF" )
                    finSi
                finSi
            finSi
            Total:= Total + v_Graduados.PromGeneral
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras NFDS(sec_Graduados) Hacer
            Analizar()
            AVZ(sec_Graduados, v_Graduados)
        finMientras
        Analizar()
        Escribir("Total de graduados no recomendados:", cont_1a7)
        Escribir("Total de graduados recomendados:", cont_7a8)
        Escribir("Total de graduados con Recomendacion favorable:", cont_8a9)
        Escribir("Total de graduados con Recomendacion muy favorable:", cont_9a10)
        Escribir("La nota promedio global es:", Total/(cont_1a7+cont_7a8+cont_8a9+cont_9a10))
        Cerrar(sec_Graduados)
    finProceso
finAccion
```
## Relaciones


