**Fecha de inicio:** 08-09-2026 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Una empresa de distribución de energía eléctrica posee un archivo maestro con los siguientes datos de sus clientes (la fecha de última lectura son las mediciones realizadas hasta el mes de mayo del 2014):

**CLIENTE** Ordenado por Id_Casa

- Id_Casa
- Fecha_Ult_Lectura
- Cant_Lecturas
- Prom_Lecturas
- Tipo_Consumidor

El campo tipo de consumidor puede ser:

- A (cuando el promedio de lectura es menor a 20K)
- B (cuando el promedio de lectura es menor a 40K)
- C (cuando el promedio de lectura es igual o supera los 40K)

Cuenta además con el siguiente archivo con datos de las mediciones realizadas en los dos últimos años (desde junio del 2014 hasta junio del 2016)

**Mediciones** Ordenado por Id_Casa

- Id_Casa
- Fecha_Medicion
- Consumo

Se pide actualizar el archivo maestro con la información de las lecturas hasta el mes de enero del año 2015 inclusive. Los campos que se deben actualizar son: la fecha de ultima lectura, cantidad de lecturas, el promedio y modificar (en caso de ser necesario) el tipo de consumidor. En caso en que no exista el ID casa (una conexión nueva) se tiene que crear en el maestro y actualizar los otros campos.
## Resolución
``` less
Accion Guía-Ejercicio_2.2.23-AlgoritmosI Es
    Ambiente
        Fecha = Registro 
            Dia: (1..31)
            Mes: (1..12)
            Año: N(4)
        finRegistro
        Cliente = Registro
            ID_Casa: N 
            Fecha_UltLectura: Fecha
            Cant_Lecturas: N 
            Prom_Lecturas: N 
            Tpo_Consumidor: ("A", "B", "C")
        finRegistro
        Mediciones = Registro
            ID_Casa: N 
            Fecha_Medicion: Fecha
            Consumo: N
        finRegistro

        arch_Cliente: Archivo de Cliente Ordenado Por ID_Casa
        arch_Salida: Archivo de Cliente
        arch_Mediciones: Archivo de Mediciones Ordenado Por ID_Casa
        reg_Cliente, reg_Salida: Cliente
        reg_Mediciones: Mediciones
        resg_Fecha, Fecha_Maxima: Fecha
        cont_Lecturas, acum_Mediciones, resg_ID_Casa: N

        Funcion FechaReciente(Fecha_Guardada: Fecha, Fecha_Nueva: Fecha): Booleano Es
            Ambiente
                FechaNum_Guardada, FechaNum_Nueva: N
            finAmbiente 
            FechaNum_Guardada:= Fecha_Guardada.Año*10000+Fecha_Guardada.Mes*100+Fecha_Guardada.Dia
            FechaNum_Nueva:= Fecha_Nueva.Año*10000+Fecha_Nueva.Mes*100+Fecha_Nueva.Dia
            Si FechaNum_Guardada<FechaNum_Nueva Entonces
                FechaReciente:= Verdadero
            SiNo
                FechaReciente:= Falso
            finSi
        finFuncion

        Procedimiento Leer_Cliente() Es
            Leer(arch_Cliente, reg_Cliente)
            Si FDA(arch_Cliente) Entonces
                reg_Cliente.ID_Casa:= HV
            finSi
        finProcedimiento
        Procedimiento Leer_Movimiento() Es
            Leer(arch_Mediciones, reg_Mediciones)
            Si FDA(arch_Mediciones) Entonces
                reg_Mediciones.ID_Casa:= HV
            finSi
        finProcedimiento

        Procedimiento Iguales() Es
            cont_Lecturas:= 0
            acum_Mediciones:= 0
            resg_Fecha.Año:= reg_Mediciones.Fecha_Medicion.Año
            resg_Fecha.Mes:= reg_Mediciones.Fecha_Medicion.Mes
            resg_Fecha.Dia:= reg_Mediciones.Fecha_Medicion.Dia
            reg_Salida.ID_Casa:= reg_Cliente.ID_Casa
            
            Mientras reg_Cliente.ID_Casa = reg_Mediciones.ID_Casa Hacer
                Si FechaReciente(reg_Mediciones.Fecha_Medicion, Fecha_Maxima) Entonces
                    cont_Lecturas:= cont_Lecturas+1
                    acum_Mediciones:= acum_Mediciones+reg_Mediciones.Consumo
                    Si FechaReciente(resg_Fecha, reg_Cliente.Fecha_UltLectura) Entonces
                        resg_Fecha.Año:= reg_Cliente.Fecha_UltLectura.Año
                        resg_Fecha.Mes:= reg_Cliente.Fecha_UltLectura.Mes
                        resg_Fecha.Dia:= reg_Cliente.Fecha_UltLectura.Dia
                    finSi
                    Si FechaReciente(resg_Fecha, reg_Mediciones.Fecha_Medicion) Entonces
                        resg_Fecha.Año:= reg_Mediciones.Fecha_Medicion.Año
                        resg_Fecha.Mes:= reg_Mediciones.Fecha_Medicion.Mes
                        resg_Fecha.Dia:= reg_Mediciones.Fecha_Medicion.Dia
                    finSi
                    
                finSi
                Leer_Movimiento()
            finMientras
            reg_Salida.Fecha_UltLectura:= resg_Fecha
            Si (reg_Cliente.Prom_Lecturas*reg_Cliente.Cant_Lecturas + acum_Mediciones) / (reg_Cliente.Cant_Lecturas + cont_Lecturas) < 20000 Entonces
                reg_Salida.Tpo_Consumidor:="A"
            SiNo
                Si (reg_Cliente.Prom_Lecturas*reg_Cliente.Cant_Lecturas + acum_Mediciones) / (reg_Cliente.Cant_Lecturas + cont_Lecturas) < 40000 Entonces
                    reg_Salida.Tpo_Consumidor:="B"
                SiNo
                    reg_Salida.Tpo_Consumidor:="C"
                finSi
            finSi
            reg_Salida.Cant_Lecturas:= reg_Cliente.Cant_Lecturas+cont_Lecturas
            reg_Salida.Prom_Lecturas:= (reg_Cliente.Prom_Lecturas*reg_Cliente.Cant_Lecturas + acum_Mediciones) / (reg_Cliente.Cant_Lecturas + cont_Lecturas)
            GRABAR(arch_Salida, reg_Salida)
            Leer_Cliente()
        finProcedimiento

        Procedimiento Diferentes() Es
            resg_ID_Casa:= reg_Mediciones.ID_Casa
            cont_Lecturas:= 0 
            acum_Mediciones:= 0
            resg_Fecha.Año:= reg_Mediciones.Fecha_Medicion.Año
            resg_Fecha.Mes:= reg_Mediciones.Fecha_Medicion.Mes
            resg_Fecha.Dia:= reg_Mediciones.Fecha_Medicion.Dia
            Mientras resg_ID_Casa = ID_Casa Hacer
                Si FechaReciente(reg_Mediciones.Fecha_Medicion, Fecha_Maxima) Entonces
                    cont_Lecturas:= cont_Lecturas + 1
                    acum_Mediciones:= acum_Mediciones + reg_Mediciones.Consumo
                    Si FechaReciente(resg_Fecha, reg_Mediciones.Fecha_Medicion) Entonces
                        resg_Fecha.Año:= reg_Mediciones.Fecha_Medicion.Año
                        resg_Fecha.Mes:= reg_Mediciones.Fecha_Medicion.Mes
                        resg_Fecha.Dia:= reg_Mediciones.Fecha_Medicion.Dia
                    finSi
                finSi
                Leer_Movimiento()
            finMientras
            reg_Salida.ID_Casa:= resg_ID_Casa
            reg_Salida.Fecha_UltLectura:= resg_Fecha
            reg_Salida.Cant_Lecturas:= cont_Lecturas
            reg_Salida.Prom_Lecturas:= acum_Mediciones/cont_Lecturas
            Segun reg_Salida.Prom_Lecturas Hacer
                < 20000: reg_Salida.Tpo_Consumidor:= "A"
                < 40000: reg_Salida.Tpo_Consumidor:= "B"
                De Otro Modo: reg_Salida.Tpo_Consumidor:= "C"
            finSegun
            GRABAR(arch_Salida,reg_Salida)
        finProcedimiento

        Procedimiento inicializar() Es
            Abrir E/(arch_Cliente); Abrir E/(arch_Mediciones); Abrir S/(arch_Salida)
            Leer_Cliente();Leer_Movimiento()
            Fecha_Maxima.Año:= 2015
            Fecha_Maxima.Mes:= 1
            Fecha_Maxima.Dia:= 31
        finProcedimiento
    finAmbiente
    Proceso
        inicializar()
        Mientras reg_Cliente.ID_Casa<>HV o reg_Mediciones.ID_Casa<>HV Hacer
            Si reg_Cliente.ID_Casa = reg_Mediciones.ID_Casa Entonces
                Iguales()
            SiNo
                Si reg_Cliente.ID_Casa< reg_Mediciones.ID_Casa Entonces
                    GRABAR(arch_Salida, reg_Cliente)
                    Leer_Cliente()
                SiNo
                    Diferentes()
                finSi
            finSi
        finMientras
        Cerrar(arch_Cliente); Cerrar(arch_Mediciones);Cerrar(arch_Salida)
    finProceso
finAccion
```
## Relaciones


