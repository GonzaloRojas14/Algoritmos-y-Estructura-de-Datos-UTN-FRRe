

**Fecha de inicio:** 18-02-2025 - Algoritmos I
---
**Tags:** #Completed  #Algoritmos_I #Ejercicios #Listas #Archivos 
---
---
## Descripción de la tarea

### **Ejercicio 1: Gestión de Socios de Supermercado (Listas)**

Una cadena de supermercados desea gestionar la información de sus clientes y sus compras para ofrecer beneficios. La información de los clientes se encuentra en un **archivo indexado** por DNI, con los siguientes datos:

- `DNI_cliente`
- `ApellidoYNombre`
- `Fecha_adhesion`
- `Categoria` (puede ser "Sin categoría", "Silver", "Gold")

Además, se tiene un **archivo secuencial** con información sobre las compras realizadas por los clientes:

- `Fecha_compra`
- `DNI_cliente`
- `Cantidad_artículos`
- `Importe_total`

**Se solicita:**

1. Crear una **lista doblemente enlazada**, ordenada alfabéticamente por `ApellidoYNombre`, con la información de los clientes que pertenecen al programa de fidelización (es decir, que están en el archivo indexado de clientes). Los nodos de esta lista deben contener:
    
    - `ApellidoYNombre`
    - `Chances_total` (calculado como se indica a continuación)
2. Calcular las Chances_total para cada cliente del programa de fidelización de la siguiente manera:
    
    - Base: 5 chances por ser socio del programa.
    - Compras: 1 chance extra por cada $100 gastados en cada compra.
    - Categoría Black: Si el cliente es de categoría "Black", se le asigna una cantidad aleatoria de chances extra. Esta cantidad se obtiene simulando una ruleta a través de una **lista circular simple**. La función `Tirar()` retorna un número aleatorio entre 1 y 55. Para obtener las chances extras, se deben realizar tantos saltos en la lista circular como el valor retornado por `Tirar()`.
3. Mostrar los 5 clientes con más chances y los 5 clientes con menos chances.
    
## Resolución
``` less
Accion Gestion_de_Socios_de_Supermercado (Prim_R: Puntero a Nodo_R) Es
    Ambiente
        form_fecha = Registro 
            año:N(4)
            mes:(1...12)
            dia:(1...31)
        finRegistro

        Clientes = Registro
            DNI_cliente:N 
            apellidoNombre:AN 
            fechaAdhesion:form_fecha
            categoria:("Sin categotia","Silver", "Gold", "Black")
        finRegistro
        
        arch_cl: Archivo de Clientes Indexado por DNI_cliente
        reg_cl: Registro de Clientes

        Compras = Registro
            fechaCompra:form_fecha
            DNI_cliente:N
            cantArt:N
            importTot:N
        finRegistro
        
        arch_co: Archivo de Compras Ordenado por fechaCompra
        reg_co: Registro de Compras

        Nodo_R = Registro
            puntos:(1...55)
            prox:Puntero a Nodo_R
        finRegistro

        punt_R:Puntero a Nodo_R

        Nodo = Registro
            apellidoNombre:AN 
            chancesTotal:N 
            prox:Puntero a Nodo
            ant: Puntero a Nodo
        finRegistro

        punt, Prim:Puntero a Nodo

        Funcion Ruleta():N Es
            Ambiente
                n:N   
            finAmbiente 
            Proceso
                n:=Tirar() 
                Para i:=1 hasta n Hacer
                    punt_R:=*punt_R.prox
                finPara
                Ruleta:=*punt_R.puntos
            finProceso
        finFuncion

        Funcion Existe(apellidoNombre:AN):Booleano Es
            Ambiente
                p:Puntero a Nodo
            finAmbiente
            Proceso
                p:=Prim
                Mientras *p.apellidoNombre<>apellidoNombre y p<>Null Hacer
                    p:=*p.prox
                finMientras
                Si p = Null Hacer
                    Existe:=FALSO
                SiNo
                    *p.chancesTotal:=*p.chancesTotal+puntos
                    Existe:=VERDADERO
                finSi
            finProceso
        finFuncion
        Procedimiento Insertar(p:Puntero a Nodo) Es
            Ambiente
                ant, prox:Puntero a Nodo
            finAmbiente
            Proceso
                prox:=Prim
                Mientras *p.apellidoNombre>*prox.apellidoNombre y prox<>Null Hacer //compara de forma alfabetica su posicion
                    ant:=prox
                    prox:=*prox.prox
                finMientras
                Si ant = Null //Si ant es Null quiere decir que es el primer elemento
                    Prim:= p 
                    Si prox<>Null Hacer
                        *prox.ant:=p 
                    finSi
                    *p.prox:=prox     //apunta a prox sea un Nodo o Null
                SiNo
                    *ant.prox:=p 
                    *p.ant:=ant
                    Si prox<>Null Hacer
                        *prox.ant:=p 
                    finSi
                    *p.prox:=prox
                finSi
            finProceso

            puntos:N 

            Funcion Calcular_Puntos(cat:AN):N Es
                Si cat = "Black" Hacer
                    Calcular_Puntos:= Ruleta()
                SiNo
                    Si cat <>"Sin categoria" Hacer
                        Calcular_Puntos:= 5 + reg_co.importTot DIV 100
                    SiNo
                        Calcular_Puntos:=0
                    finSi
                finSi
            finFuncion

            Procedimiento inicializar() Es 
                Abrir E/(arch_cl),Abrir E/(arch_co)
                Leer(arch_co,reg_co)
                puntos:=0
                Nuevo(Prim)
                punt_R:=Prim_R
            finProcedimiento
    finAmbiente
    Proceso
        inicializar()

        Mientras NFDS(arch_co) Hacer
            reg_cl.DNI_cliente:=reg_co.DNI_cliente
            Leer(arch_cl,reg_cl)
            puntos:=Calcular_Puntos(reg_cl.categoria)
            Si Existe(reg_cl.apellidoNombre) Hacer
                Escribir("Se agregaron los puntos al cliente")
            SiNo
                Nuevo(punt)
                *punt.apellidoNombre:=reg_cl.apellidoNombre
                *punt.chancesTotal:=puntos
                Insertar(punt)
                Escribir("Se agrego un nuevo cliente")
            finsi
            Leer(arch_co,reg_co)
        finMientras

    finProceso
finAccion
```
## Relaciones
- [[Listas-AlgoritmosI]]
- [[Procesos-Archivos-AlgoritmosI]]

