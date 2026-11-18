**Fecha de inicio:** 28-08-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Se dispone de una secuencia de facturas con los siguientes datos:

- Nº de Factura
- Fecha
- Total

Se desea un listado de las facturas cuyas fechas sean posteriores a una fecha dada, y cuyos importes totales no alcancen los $1000, con el siguiente formato:

| <span class="celda-gris">Nro_Factura</span> | Fecha | Total |
| ------------------------------------------- | ----- | ----- |
|                                             |       |       |

## Resolución
``` less
Accion Guía-Ejercicio_2.2.2-AlgoritmosI Es
    Ambiente
        Fecha = Registro
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        Facturas = Registro
            Nro_Factura: N 
            Fecha_Factura: Fecha 
            Total: N
        finRegistro

        sec_Facturas: Secuencia de Facturas
        v_Facturas: Registro de Facturas 

        var_Fecha: Registro de Fecha

        Procedimiento inicializar() Es
            ARR(sec_Facturas)
            AVZ(sec_Facturas, v_Facturas)
            Escribir(Ingrese El Año a analizar:)
            Leer(var_Fecha.Año)
            Escribir(Ingrese El Mes a analizar:)
            Leer(var_Fecha.Mes)
            Escribir(Ingrese El Dia a analizar:)
            Leer(var_Fecha.Dia)
            Escribir("Nro Factura | Fecha | Total")
        finProcedimiento
        Funcion Posterior(f: Registro de Fecha): Booleano Es
            Si f.Año=var_Fecha.Año Entonces
                Si f.Mes=var_Fecha.Mes Entonces
                    Si f.Dia>var_Fecha.Dia Entonces
                        Posterior:= Verdadero
                    SiNo
                        Posterior:= Falso   
                    finSi
                SiNo
                    Si f.Mes>var_Fecha.Mes Entonces
                        Posterior:= Verdadero
                    SiNo
                        Posterior:= Falso
                    finSi
                finSi
            SiNo
                Si f.Año>var_Fecha.Año Entonces
                    Posterior:= Verdadero
                SiNo
                    Posterior:= Falso
                finSi
            finSi
        finFuncion
    finAmbiente 
    Proceso
        inicializar()
        Mientras NFDS(sec_Facturas) Hacer
            Si Posterior(v_Facturas.Fecha_Factura) Y 1000>v_Facturas.Total Entonces
                Escribir(v_Facturas.Nro_Factura, "|", v_Facturas.Fecha_Factura.Dia, "/",v_Facturas.Fecha_Factura.Mes, "/",v_Facturas.Fecha_Factura.Año, "|", v_Facturas.Total)
            finSi
            AVZ(sec_Facturas,v_Facturas)
        finMientras
        Si Posterior(v_Facturas.Fecha_Factura) Y 1000>v_Facturas.Total Entonces
            Escribir(v_Facturas.Nro_Factura, "|", v_Facturas.Fecha_Factura.Dia, "/",v_Facturas.Fecha_Factura.Mes, "/",v_Facturas.Fecha_Factura.Año, "|", v_Facturas.Total)
        finSi
        Cerrar(sec_Facturas)
    finProceso
finAccion
```
## Relaciones

   
