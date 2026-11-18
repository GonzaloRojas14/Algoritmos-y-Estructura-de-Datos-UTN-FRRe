**Fecha de inicio:** 05-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Construir un algoritmo que a partir de un fichero de películas nuevas conteniendo:

**PELICULAS_NUEVAS** Ordenado por Nro_Pelicula

- Nro_Pelicula
- Titulo
- Genero
- Cant_Copias
- Fecha_Estreno

y otro fichero de peliculas existentes, ambos ordenados por Nro_Pelicula,

**PELICULAS** Ordenado por Nro_Pelicula

- Nro_Pelicula
- Titulo
- Genero
- Cant_Copias
- Fecha_Estreno

Genere un único archivo (con el mismo formato de los ficheros de entrada) que contenga todas las peliculas. Considerar que hay un solo registro por película y no se repiten entre ficheros.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.16-AlgoritmosI Es
    Ambiente
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro

        Peliculas = Registro 
            Nro_Pelicula: N 
            Titulo: AN 
            Genero: AN 
            Cant_Copias: N 
            Fecha_Estreno: Fecha
        finRegistro

        arch_Peliculas, arch_PeliculasNuevas: Archivo de Peliculas Ordenado Por Nro_Pelicula
        arch_Salida: Archivo de Peliculas

        reg_Peliculas, reg_PeliculasNuevas: Registro de Peliculas

        Procedimiento inicializar() Es
            Abrir E/(arch_Peliculas); Abrir E/(arch_PeliculasNuevas); Abrir S/(arch_Salida)
            Leer_Peliculas(arch_Peliculas, reg_Peliculas); Leer_PeliculasNuevas(arch_PeliculasNuevas, reg_PeliculasNuevas)
        finProcedimiento

        Procedimiento Leer_Peliculas() Es
            Leer(arch_Peliculas, reg_Peliculas)
            Si FDA(arch_Peliculas) Entonces
                reg_Peliculas.Nro_Pelicula:= HV
            finSi
        finProcedimiento
        Procedimiento Leer_PeliculasNuevas() Es
            Leer(arch_PeliculasNuevas, reg_Peliculas)
            Si FDA(arch_PeliculasNuevas) Entonces
                reg_PeliculasNuevas.Nro_Pelicula:= HV
            finSi
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras reg_Peliculas.Nro_Pelicula <> HV o reg_PeliculasNuevas.Nro_Pelicula <> HV Hacer
            Si reg_Peliculas.Nro_Pelicula<reg_PeliculasNuevas.Nro_Pelicula Entonces
                GRABAR(arch_Salida, reg_Peliculas)
                Leer_Peliculas()
            SiNo
                GRABAR(arch_Salida, reg_PeliculasNuevas)
                Leer_PeliculasNuevas()
            finSi
        finMientras
        Cerrar(arch_Peliculas);Cerrar(arch_PeliculasNuevas);Cerrar(arch_Salida)
    finProceso
finAccion
```
## Relaciones


