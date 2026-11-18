

**Fecha de inicio:** 02-09-2024 - Algoritmos I
---
**Tags:** #Completed  #Algoritmos_I #Ejercicios 
---
---
## Descripción de la tarea
En la biblioteca de la UTN-FRRe se posee un archivo MAE_LIBROS (ordenado por Clave: ID_Libro) con cada libro disponible. Esta semana realizaron una gran compra de nuevos libros y decidieron quitar los que ya no están en buen estado para ser utilizados por los estudiantes. En un archivo de MOVIMIENTOS registraron cada compra y aquellos que se quitaron. Considere que las compras pueden ser de títulos existentes o nuevos. Además, en el archivo maestro hay solo un registro por libro, pero en el de MOVIMIENTOS hay un registro por cada ejemplar. Por lo que puede haber más de un movimiento por título del maestro.

MAE_LIBROS Ordenado por ID_Libro

ID_Libro, Tema, Titulo, Cant_Actual

MOVIMIENTOS Ordenado por ID_Libro y Cod_Mov

ID_Libro, Cod_Mov, Tema,  Titulo

Cod_Mov puede ser Alta o Baja (Es “alta” por ser un nuevo ejemplar, pero debe determinar a partir de las claves si es un nuevo título del maestro o no)

Tema puede ser MB(Materias Básicas), ISI, IQ IEM

FILA 1

Se pide que genere 4 nuevos archivos maestro con las cantidades actualizadas según las compras, los nuevos libros y que no contenga los eliminados. Ahora la biblioteca quiere tener en archivos distintos los libros de materias básicas, y los específicos de cada ingeniería (IEM, ISI, IQ)
## Resolución

```
Accion ActualizarLibros es
	Ambiente
	   MAE_LIBROS = registro
		 ID_Libro: N(5)
		 Tema: AN(20)
		 Titulo: AN(30)
		 Cant_Actual: N(5)
	   finregistro
		
	   MOVIMIENTOS = registro
		 ID_Libro: N(5)
		 Cod_Mov: AN(1)
		 Tema: AN(20)
		 Titulo: AN(30)
	   finregistro
	   
	   Maestro: archivo de MAE_LIBROS ordenado por ID_Libro
	   Movimientos: archivo de MOVIMIENTOS ordenado por ID_Libro, Cod_Mov
	   Mat_Basicas,Libros_ISI,Libros_IEM,Libros_IQ: archivo de MAE_LIBROS
		
	   Mae,aux: MAE_LIBROS
	   Mov: MOVIMIENTOS
	   
	   Procedimiento leerMae() es
		   leer(maestro,mae)
		   si FDA (maestro) entones
			   mae.ID_Libros := HV
		   finsi
	   finprocedimiento
		
	   Procedimiento leerMov() es
		   leer(movimiento,mov)
		   si FDA (movimientos) enttones
			   mov.ID_libro := HV
		   finsi
	   finprocedimiento
	
		procedimiento AbrirArchivos() es
		   abrir E/(Maestro)
		   LeerMae()
		   abrir E/(Movimientos)
		   LeerMov()
		   abrir S/(Mat_Basicas)
		   abrir S/(Libros_ISI)
		   abrir S/(Libros_IEM)
		   abrir S/(Libros_IQ)
		finprocedimiento
		
		 procedimiento CerrarArchivos() es
		   cerrar(Maestro)
		   cerrar(Movimientos)
		   cerrar(Mat_Basicas)
		   cerrar(Libros_ISI)
		   cerrar(Libros_IEM)
		   cerrar(Libros_IQ)
		 finprocedimiento
	finAmbiente
	PROCESO
	   AbrirArchivos()
	   MIENTRAS (mae.id_libro <> HV) O (mov.id_libro <> HV) HACER
	       SI mae.id_libro < Mov.id_libro ENTONCES //no hubo modificaciones
	           SEGUN mae.tema HACER
		           = “MB”: Grabar(Mat_Basicas, mae)
		           = “ISI”:   Grabar(Libros_ISI, mae)
		           = “IEM”:   Grabar(Libros_IEM, mae)
		           = “IQ”:    Grabar(Libros_IQ, mae)
	           FINSEGUN
	           LeerMae()
	       SINO
	           si mae.id_Libro = mov.id_Libro ENTONCES
	               SI mov.Cod_Mov = “A”ENTONCES
	                   aux := mae
	                   MIENTRAS aux.id_libro = mov.id_libro HACER
	                       //SE PUEDE AGREGAR CONTROL DE BAJAS
	                       aux.cant_actual := aux.cant_actual + 1
	                       leer_Mov()
	                   FINMIENTRAS
	                   SEGUN mae.tema HACER
	                       = “MB”:     Grabar(Mat_Basicas, mae)
	                       = “ISI”:   Grabar(Libros_ISI, mae)
	                       = “IEM”:   Grabar(Libros_IEM, mae)
	                       = “IQ”:    Grabar(Libros_IQ, mae)
	                   FINSEGUN
	               finsi
	               //en caso de baja no se debe copiar a la salida
	               leer_mae()
	           sino
	               SI mae.id_libro > mov.id_libro ENTONCES//solo puede ser alta
	                   SI mov.Cod_Mov = "A" ENTONCES
	                       aux.id_Libro:= mov.id_Libro
	                       aux.tema := mov.tema
	                       aux.titulo := mov.titulo
	                       aux.cant_actual:= 1
	                       leer_Mov()
	                       MIENTRAS aux.id_Libro = mov.id_Libro HACER
	                           aux.cant_actual := aux.cant_actual + 1
	                           leer_Mov()
	                           //SE PODRIA AGREGAR CONTROL DE BAJAS
	                       FINMIENTRAS
	                       SEGUN mae.tema HACER
	                           = “MB”:     Grabar(Mat_Basicas, mae)
	                           = “ISI”:   Grabar(Libros_ISI, mae)
	                           = “IEM”:   Grabar(Libros_IEM, mae)
	                           = “IQ”:    Grabar(Libros_IQ, mae)
	                       FINSEGUN
	                   SINO
	                       ESC("ERROR")
	                   FINSI
	               FINSI
	           FINSI
	       Finsi
	   FINMIENTRAS
	   LeerMae()
	   CerrarArchivos()
   finProceso
FINACCION
```



## Relaciones
[[Actualización-AlgoritmosI]]

