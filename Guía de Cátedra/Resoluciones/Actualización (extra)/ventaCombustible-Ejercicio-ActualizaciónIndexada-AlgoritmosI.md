

**Fecha de inicio:** 17-09-2024 - Algoritmos I
---
**Tags:** #InProgress  #Trabajo #Proyecto #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea

Una empresa dedicada a la venta de combustibles para automotores anunció una promoción mediante la cual los clientes pueden acceder a descuentos importantes. En cada carga los clientes suman 10 puntos por cada $100 de combustible, y una vez que el cliente llega a los 100 puntos, este los puede canjear por un descuento de $100 en el importe total. La cantidad de puntos que tiene cada cliente está almacenado en el archivo indexado PUNTOS el cual tiene el siguiente formato:

PUNTOS Indexado por DNI
● DNI
● Cant_Puntos
● Ult_Carga

Los datos de cada cliente se encuentran almacenados en el archivo CLIENTE también indexado con el siguiente formato:

CLIENTE Indexado por DNI
● DNI
● Ape_Nom
● Edad
● Ciudad

Se pide realizar el algoritmo que permita:
1. Realizar la carga interactiva de las cargas de combustible (ingresando monto), actualizando la cantidad de Puntos y la Fecha de Última Carga en el archivo PUNTOS. Si no existe el Cliente, se lo debe inicializar en ambos archivos con los datos correspondientes.
2. Permitir al cliente aplicar descuentos a las cargas realizadas siempre y cuando tenga puntos suficientes (sólo se puede canjear 100 puntos por carga).
3. Determinar la cantidad de cargas realizadas de usuarios no existentes.
## Resolución
``` 
ACCION 2.3.11 ES
	AMBIENTE
		PUNTOS = registro
			DNI: N(8)
			Cant_Puntos: Real(7,2)
			Ult_Carga: AN(10)
		fin_registro
		ArchPuntos:Archivo PUNTOS indexado por DNI
		RPuntos: PUNTOS
			CLIENTES = registro
			DNI:N(8)
			Ape_Nom:AN(50)
			Edad:N(2)
			Ciudad:AN(50)
		fin_registro
		ArchCliente:Archivo CLIENTES indexado por DNI
		RCliente: CLIENTES
		carga, descuento: ("SI","NO")
		monto: Real
		clave: entero
	proceso
		ABRIR E/S (ArchPuntos)
		ABRIR E/S(ArchCliente)
		REPETIR
			ESC("Ingrese monto")
			LEER(monto)
			ESC("Ingrese DNI")
			LEER(RCliente.DNI)
			LEER(ArchCliente, RCliente)
			SI EXISTE ENTONCES
				RPuntos.DNI := clave
				LEER(ArchPuntos, RPuntos)
				SI EXISTE ENTONCES
					SI RPuntos.Cant_Puntos >= 100 entonces
						ESC("DESEA DESCONTAR $100 DEL MONTO TOTAL? INGRESE SI O NO")
						LEER(descuento)
						SI descuento = "SI" entonces
							monto := monto - 100
						finsi
					finsi
					ESC("DEBE PAGAR: ", monto)
					RCliente.Cant_Puntos := RCliente.Cant_Puntos + monto DIV 10
					RPuntos.Ult_Carga:= fecha_sistema()
					REGRABAR(ArchPuntos, RPuntos)
				SI NO EXISTE
					ESC("Error cliente existente no esta en archivo puntos")
				finsi
			SI NO EXISTE ENTONCES
				//Dar de alta en ambos archivos
				RCliente.DNI := clave
				ESC("Ingrese nombre"); LEER(RCliente.Ape_Nom)
				ESC("Ingrese edad"); LEER(RCliente.Edad)
				ESC("Ingrese ciudad"); LEER(RCliente.Ciudad)
				GRABAR(ArchCliente, RCliente)
				RPuntos.DNI:= clave
				RPuntos.Cant_Puntos:= monto div 100
				SI RPuntos.Cant_Puntos >= 100 entonces
					ESC("DESEA DESCONTAR $100 DEL MONTO TOTAL? INGRESE SI O NO")
					LEER(descuento)
					SI descuento = "SI" entonces
						monto := monto - 100
					finsi
				finsi
				RPuntos.Ult_Carga:= fecha_sistema()
				GRABAR(ArchPuntos, RPuntos)
			finsi
			ESC("Desea realizar otra carga? Ingrese SI o NO")
			LEER(carga)
		HASTA QUE carga = "NO"
		
		
		acceso PUNTOS
		si existe
			acceso clientes
```


## Relaciones
- [[Actualización INDEXADA.pptx]]
- [[Actualización-AlgoritmosI#Actualización indexada]]

