

**Fecha de inicio:** 25-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Leer una palabra (una cadena de caracteres) y la cantidad de caracteres y generar su palíndromo. El palíndromo de “Venezuela” es “aleuzeneV”.
## Resolución
``` less
Accion Guia-Ejercicio-5.2.2 Es
    Ambiente
        Procedimiento Palindromo() Es
            Ambiente
                resg:Caracter
            finAmbiente
            Proceso
                resg:=v
                AVZ(Sec,v)
                Si FDS(v) Hacer
                    Escribir(v)
                SiNo
                    Palindromo()
                finSi
                Escribir(resg)
            finProceso
        finProcedimiento
        Sec: Secuencia de Caracteres
        v: Caracter
    finAmbiente
    Proceso
        Abrir E/(Sec)
        AVZ(Sec, v)
		Palindromo()
    finProceso
finAccion

```
## Relaciones
- [[Recursividad-Introduccion-AlgoritmosI]]
- [[Secuencia-AlgoritmosI]]

