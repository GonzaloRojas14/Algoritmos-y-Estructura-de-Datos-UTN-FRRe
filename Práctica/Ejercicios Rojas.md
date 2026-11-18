---
tipo: practica
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - ejercicios
---

# Ejercicios Rojas

> [!abstract] Qué hay acá
> Resoluciones **tuyas**. Incluye los tres enunciados de parcial (`Parcial.1/2/3`) y ejercicios de arreglos, registros, corte de control y archivos indexados.
> **26 archivos**, transcriptos íntegros desde `Practica/Ejercicios Rojas/`.
> Los originales siguen intactos en esa carpeta; esto es una copia legible dentro de Obsidian.

---

## Índice

- [[#1.1.5.1.txt]]
- [[#1.1.5.2.txt]]
- [[#1.1.5.3.txt]]
- [[#1.7.txt]]
- [[#1.8.txt]]
- [[#1.9.txt]]
- [[#1.10.txt]]
- [[#1.11.txt]]
- [[#1.12.txt]]
- [[#2.1.4.txt]]
- [[#2.1.15.txt]]
- [[#2.1.18.txt]]
- [[#2.2.1.txt]]
- [[#2.2.2.txt]]
- [[#2.2.4.txt]]
- [[#2.2.12.txt]]
- [[#2.3.frre]]
- [[###Te dan un array de enteros nums y un v.py]]
- [[#Arreglos:]]
- [[#Corte de control.txt]]
- [[#NyDNI]]
- [[#Parcial.1.txt]]
- [[#Parcial.2.txt]]
- [[#Parcial.3.txt]]
- [[#Resgistros]]
- [[#un archivo indexado es una tabla de indi]]

---

## 1.1.5.1.txt

```
//Escribir un programa que permita calcular el precio de un artículo para un año dado, considerando que la inflación es del 4 por 100 anual.

//La fórmula del precio es: P = C * (1 + R) ^ (N - A)

//C - Precio actual.
//N - Año futuro.
//R - Tasa de Inflación.
//A - Año actual

ACCION ejercicio_1.1.5 ES
    AMBIENTE
        c, p: REAL
        n, a: ENTERO
        r: 0.4
    PROCESO
        ESCRIBIR("Ingrese el año actual y el año futuro: ")
        LEER(a, n)
        ESCRIBIR("Ingrese el precio del producto: ")
        p := c * (1 + r) ^ (n - a)
        ESCRIBIR("El precio calculado a base de la inflacion es: ", p)
FIN_ACCION
```

## 1.1.5.2.txt

```
//Las raíces de una ecuación de segundo grado ax^2+bx+c=0 son reales si y sólo si el discriminante dado por (b2−4ac) no es negativo. 
//Se desea leer el valor de los coeficientes a,b,c
//Imprimir el resultado del discriminante. Realizar prueba de escritorio.
```

## 1.1.5.3.txt

```
//Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado por la suma de los precios de costos, 
//los porcentajes de ganancia del vendedor y un 21% de IVA. 
//Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora. 
//Se leen los costos y se imprimen el precio total de ventas.

ACCION 1.1.5.3 ES
    AMBIENTE 
        iva = 1.21
        por_pc = 1.12
        por_imp = 1.07
        costo_pc, costo_imp, precio_total: REAL
    PROCESO
        ESCRIBIR("Ingrese el costo de la PC y luego el de la impresora: ")
        LEER(costo_pc, costo_imp)
        precio_total := (costo_pc * por_pc) + (costo_imp * por_imp)
        precio_total := precio_total * iva
        ESCRIBIR("El preico total es: ", precio_total)
FIN_ACCION
```

## 1.7.txt

```
//Escriba un algoritmo que permita ingresar 3 valores numéricos y determine cuál es el mayor, el medio y el menor. 
//(era el 3 de los complementarios)

ACCION 1.7 ES
    AMBIENTE
        a,b,c: REAL
    PROCESO
        ESCRIBIR("Ingresar 3 numeros en cualquier orden: ")
        LEER(a,b,c)
        SI a > b Y b > c ENTONCES:  // a b c
            ESCRIBIR("El numero mayor es: ", a, "El segundo numero mayor es: ", b, "Y el tercer numero mayor es: ", c)
        SINO 
            SI b > a Y a > c ENTONCES: // b a c
                ESCRIBIR("El numero mayor es: ", b, "El segundo numero mayor es: ", a, "Y el tercer numero mayor es: ", c)
            SINO
                SI c > a Y a > b ENTONCES: // c a b
                    ESCRIBIR("El numero mayor es: ", c, "El segundo numero mayor es: ", a, "Y el tercer numero mayor es: ", b)
                SINO
                    SI c > b Y b > a ENTONCES: // c b a
                        ESCRIBIR("El numero mayor es: ", c, "El segundo numero mayor es: ", b, "Y el tercer numero mayor es: ", a)
                    SINO
                        SI b > c Y c > a ENTONCES: // b c a
                            ESCRIBIR("El numero mayor es: ", b, "El segundo numero mayor es: ", c, "Y el tercer numero mayor es: ", a)
                        SINO
                            SI a > c Y c > b ENTONCES: // a c b
                                ESCRIBIR("El numero mayor es: ", a, "El segundo numero mayor es: ", c, "Y el tercer numero mayor es: ", b)
                            FIN_SI
                        FIN_SI
                    FIN_SI
                FIN_SI
            FIN_SI
        FIN_SI
    FIN_PROCESO
FIN_ACCION
```

## 1.8.txt

```
//Escriba un algoritmo que acepte dos números, calcule la suma e imprima el mensaje de acuerdo al resultado obtenido.
//
//Suma <= 50
//Suma > 50 y <= 100
//Suma > 100 y <= 200
//Suma > 200

ACCION 1.8 ES
    AMBIENTE
        suma,a,b: ENTERO
    PROCESO 
        ESCRIBIR("Ingrese dos numeros: ")
        LEER(a,b)
        suma := a + b

        SEGUN suma HACER:
            <= 50: ESCRIBIR("El valor es menor o igual a 50")
            <= 100: ESCRIBIR("El valor es menor o igual a 100")
            <= 200: ESCRIBIR("El valor es menor o igual a 200")
            OTROS: ESCRIBIR("El valor es mayor a 200")
        FIN_SEGUN
    FIN_PROCESO
FIN_ACCION
```

## 1.9.txt

```
//Escriba un algoritmo que permita conocer la edad de una persona, 
//con solo ingresar la fecha de nacimiento y la fecha actual, 
//ambas en el formato: DIA, MES, AÑO

ACCION 1.9 ES
    AMBIENTE
        dia_nac, mes_nac, año_nac, dia, mes, año, edad: ENTERO
    PROCESO
        ESCRIBIR("Ingrese el nacimiento en dd/mm/aaaa")
        LEER(dia_nac,mes_nac,año_nac)
        ESCRIBIR("Ingrese la fecha actual en dd/mm/aaaa")
        LEER(dia,mes,año)
        edad := año_nac - año 
        SI mes_nac > mes ENTONCES:
            edad := edad - 1
        SINO
            SI mes_nac = mes Y dia_nac > dia ENTONCES:
                edad := edad - 1
            FIN_SI
        FIN_SI
        ESCRIBIR("La edad del individuo es: ", edad)
FIN_ACCION
```

## 1.10.txt

```
//Una persona decide realizar un viaje a Europa, para lo cual necesita una determinada cantidad de euros. 
//La persona tiene ahorrada una cierta suma en dólares y desea saber si es suficiente y, 
//en caso de haber diferencia (de más o de menos) a cuantos pesos equivale. 
//Realice un algoritmo que solucione el problema, para lo cual deberá prever que se ingresen las equivalencias de monedas 
//que considere necesarias (por ejemplo la cotizacion en pesos de dólar y/o del euro, o a cuantos euros equivale un dólar).

ACCION 1.10 ES
    AMBIENTE
        dol,pesos,diff,cot_dol,cot_eu,cot_pesos,total,viaje: REAL        
    PROCESO
        ESCRIBIR("Ingrese el monto en Dolares: ")
        LEER(dol)
        ESCRIBIR("Ingrese el costo del viaje en Euros: ")
        LEER(viaje)
        ESCRIBIR("Ingrese la cotizacion del Euro en Dolares: ")
        LEER(cot_eu)
        total := dol * cot_eu
        diff := total - viaje
        SI diff <> 0 ENTONCES:
            ESCRIBIR("Ingrese la cotizacion de Euro a Pesos")
            LEER(cot_pesos)
            diff := diff * cot_pesos
            ESCRIBIR("La diferencia en pesos es: ", diff)
        SINO
            ESCRIBIR("No hay diferencias, el viaje en Euros es: ". viaje)
        FIN_SI
    FIN_PROCESO        
FIN_ACCION
```

## 1.11.txt

```
//Dados dos números enteros A y B generar un algoritmo que permita determinar si A es divisor de B o B es divisor de A.

ACCION ejercicio_1_11 ES
    AMBIENTE
        a,b: ENTERO
    PROCESO
        ESCRIBIR("Ingrese dos numeros a verificar: ")
        LEER(a,b)
        SI a MOD b = 0 ENTONCES
            ESCRIBIR("El numero ", b, "es divisor del numero ", a)
        SINO
            SI b MOD a = 0 ENTONCES
                ESCRIBIR("El numero ", a, "es divisor del numero ", b)
            SINO
                ESCRIBIR("Los numeros no son divisores entre si")
            FIN_SI
        FIN_SI
FIN_ACCION
```

## 1.12.txt

```
//Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000, 
//y muestre cómo está compuesto (unidades, decenas y centenas) y si es múltiplo de 3 
//(Recordar: todo número cuya suma de sus dígitos sea múltiplo de 3, lo es también).

ACCION ejercicio_1_12 ES
    AMBIENTE
        num: ENTERO
    PROCESO
        ESCRIBIR("Ingrese un numero desde 100 al 1000:")
        LEER(num)
        SI num > 100 Y num < 1000 ENTONCES
```

## 2.1.4.txt

```
//Se dispone de 2 secuencias de caracteres, una contiene caracteres, incluidos espacios y otra contiene caracteres “numéricos”. 
//Se pide crear una nueva secuencia de salida de caracteres donde se copien los caracteres de ambas secuencias en forma alternada, o sea un carácter, 
//un digito, un carácter, un digito, etc.
//
//Ejemplo:
//
//Sec1: Para habilitar la función de Salas para grupos pequeños para su uso*
//
//Sec2: 13481460918460846161334868461086*
//
//Salida: P1a3r4a8 1h4….
//
//Analice y responda: Que pasaría en el caso de que una secuencia de entrada termine antes que la otra? se podría cumplir con la consigna?
//Como modificaría el algoritmo en el caso de que solicite contar la cantidad de caracteres de cada secuencia y mostrar por pantalla al final del proceso?





ACCION 2_1_4 ES
    AMBIENTE 
        s1, s2, sal: SEC DE CARACTER.  // Se necesita definir las secuencias en el ambiente, NO cuenta como empezarla   
        v1, v2: CARACTER. // Se definen las ventanas de cada secuencia 
    PROCESO
        ARRANCAR(s1); ARRANCAR(s2); CREAR(sal)
        AVANZAR(s1, v1); AVANZAR(s2, v2)

        MIENTRAS NFDS(s1) Y NFDS(s2) HACER
            ESCRIBIR(sal, v1); ESCRIBIR(sal, v2) // Necesitamos SIEMRPE escribir LA VENTANA asignada en la SECUENCIA DE SALIDA 
            AVANZAR(s1,v1); AVANZAR(s2,v2) // Una vez que hayamos manipulado lo que el ejercicio pedia, se tiene que avanzar las ventanas de las secunecias en uso
        FIN_MIENTRAS

        CERRAR(sal); CERRAR(s1); CERRAR(s2) // Siempre se cierran las secuencias para guardarlas o algo asi, si o si se cierran por cada secuencia en separado
FIN_ACCION
```

## 2.1.15.txt

```
//Se desea saber la cantidad promedio de palabras que contienen las oraciones de una secuencia de caracteres. 
//Supóngase que los puntos son siempre contiguos al último caracter de la palabra. La secuencia finaliza con una marca.

ACCION Ej_2_1_15 ES
    AMBIENTE
        sec : SECUENCIA DE CARACTERES
        v : CARACTER
        cont_pal, cont_ora : ENTERO
        prom : REAL
    PROCESO
        cont_pal := 0
        cont_ora := 0
        
        ARRANCAR(sec)
        AVANZAR(sec, v)

        MIENTRAS NFDS(sec) HACER
            
            // Ignorar posibles espacios en blanco antes de una oración
            MIENTRAS v = ' ' HACER
                AVANZAR(sec, v)
            FIN_MIENTRAS

            SI NFDS(sec) Y v <> '.' ENTONCES
                cont_ora := cont_ora + 1  // Detectamos el inicio de una nueva oración
                
                // 2. Ciclo de subsecuencia jerárquica: ORACIÓN
                MIENTRAS v <> '.' Y NFDS(sec) HACER
                    
                    // Ignorar posibles espacios múltiples entre palabras
                    MIENTRAS v = ' ' HACER
                        AVANZAR(sec, v)
                    FIN_MIENTRAS

                    SI v <> '.' Y NFDS(sec) ENTONCES
                        cont_pal := cont_pal + 1  // Detectamos el inicio de una nueva palabra
                        
                        // 3. Ciclo de subsecuencia jerárquica: PALABRA
                        // Avanzamos hasta que la palabra termine por un espacio O por el punto
                        MIENTRAS v <> ' ' Y v <> '.' Y NFDS(sec) HACER
                            AVANZAR(sec, v)
                        FIN_MIENTRAS
                    FIN_SI
                FIN_MIENTRAS
                
                // Estamos parados en el punto que finaliza la oración actual, lo superamos
                SI v = '.' ENTONCES
                    AVANZAR(sec, v)
                FIN_SI
            FIN_SI
            
        FIN_MIENTRAS

        // Salida segura evitando división por cero
        SI cont_ora > 0 ENTONCES
            prom := cont_pal / cont_ora
            ESCRIBIR("El promedio de palabras por oraciones es: ", prom)
        SINO
            ESCRIBIR("La secuencia no contenía oraciones válidas.")
        FIN_SI
FIN_ACCION
```

## 2.1.18.txt

```
//Escribir un algoritmo que produzca una secuencia de salida que contenga una oración formada 
//por las palabras en posición par de cada oración de una secuencia texto de entrada, que además comienzan con la letra 'M'.

ACCION 1_2_18 ES
    AMBIENTE
        sec, sal: SEC DE CARACTERES
        v: CARACTER
        cont: ENTERO
    PROCESO
        ARRANCAR(sec); AVANZAR(sec, v); CREAR(sal)

        MIENTRAS NFDS(sec) HACER
            cont := 0

            MIENTRAS v <> '.' HACER

                MIENTRAS v = ' ' HACER
                    AVANZAR(sec,v)
                FIN_MIENTRAS
                cont := cont + 1

                SI cont MOD 2 = 0 Y v + 'm' ENTONCES // Consulta si la palabra es par, que es lo que pide el ejercicio procesar si solo es palabra par

                    MIENTRAS v <> ' ' y v <> '.' HACER
                        ESCRIBIR(sal,v)
                        AVANZAR(sec, v)
                    FIN_MIENTRAS

                SINO
                    MIENTRAS v <> ' ' y v <> '.' HACER
                        AVANZAR(sec,v)
                    FIN_MIENTRAS
                FIN_SI
            FIN_MIENTRAS  
            AVANZAR(sec,v)
        FIN_MIENTRAS  
FIN_ACCION
```

## 2.2.1.txt

```
ACCION 2_2_1 ES
    AMBIENTE
        FECHA = REGISTRO                                    // Estructura auxiliar para representar una fecha
            aa: ENTERO                                      // año
            mm: ENTERO                                      // mes
            dd: ENTERO                                      // día
        FIN_REGISTRO

        ALUMNO = REGISTRO                                   // Estructura completa con todos los datos del alumno
            apynom: AN(40)
            carrera: ('isi','iem','iq','lar')
            legajo: ENTERO
            fecha_nac: FECHA                                // campos FECHA anidados dentro de ALUMNO
            fecha_ing: FECHA
            dni: N(8)
            sexo: ('M', 'F')
            fecha_ult_exam: FECHA
            nota: ENTERO
        FIN_REGISTRO

        ALUMNOISI = REGISTRO                                // Versión reducida de ALUMNO, solo los campos necesarios para ISI
            apynom: AN(40)
            carrera: ('isi','iem','iq','lar')
            legajo: ENTERO
            fecha_ing: FECHA
            dni: N(8)
        FIN_REGISTRO

        arch_alu, arch_alu_iq: Archivo de ALUMNO           // arch_alu: entrada | arch_alu_iq: salida para alumnos IQ
        arch_alu_isi: Archivo de ALUMNOISI                 // salida para alumnos ISI con formato reducido
        alu, aluiq: ALUMNO                                 // variables de trabajo para leer y copiar registros ALUMNO
        aluisi: ALUMNOISI                                  // variable de trabajo para armar el registro reducido ISI

    PROCESSO
        Abrir E/(arch_alu); Leer(arch_alu, alu)            // abre el archivo de entrada y lee el primer registro
        Abrir /S(arch_alu_iq); Abrir /S(arch_alu_isi)      // abre los dos archivos de salida (vacíos)

        MIENTRAS NFDA(arch_alu) HACER                      // recorre todos los registros hasta el fin de archivo
            ESCRIBIR(alu.legajo, alu.apynom, alu.dni, alu.carrera)  // muestra por pantalla los datos básicos del alumno

            SI alu.carrera = 'iq' ENTONCES
                aluiq := alu                               // como son del mismo tipo, copia todos los campos de una vez
                ESCRIBIR(arch_alu_iq, aluiq)               // graba el registro completo en el archivo de IQ
            SINO
                SI alu.carrera = 'isi' ENTONCES

                    aluisi.apynom := alu.apynom            // los tipos son distintos (ALUMNO vs ALUMNOISI),
                    aluisi.legajo := alu.legajo            // no se puede asignar directo, hay que copiar
                    aluisi.fecha_ing := alu.fecha_ing      // campo por campo solo los que tiene ALUMNOISI
                    aluisi.dni := alu.dni

                    ESCRIBIR(arch_alu_isi, aluisi)         // graba el registro reducido en el archivo de ISI

                FIN_SI
            FIN_SI

            LEER(arch_alu, alu)                            // lee el siguiente registro para continuar el ciclo
        FIN_MIENTRAS

        CERRAR(arch_alu); CERRAR(arch_alu_iq); CERRAR(arch_alu_isi)   // cierra los tres archivos al terminar
    FIN_PROCESO
FIN_ACCION
```

## 2.2.2.txt

```
ACCION 2_2_2 ES
    AMBIENTE
        
        FECHA = REGISTRO
            aa: ENTERO
            mm: ENTERO
            dd: ENTERO
        FIN_REGISTRO

        FACTURA = REGISTRO
            nro: ENTERO
            f_fact: FECHA
            imp: REAL
        FIN_REGISTRO

        facturas: Archivo de FACTURA
        fac: FACTURA

        fecha_us: FECHA

    PROCESO
        ABRIR E/(facturas): LEER(facturas, fac)
        ESCRIBIR("Ingrese la fecha deseada, dia, mes, año")
        LEER(fecha_us.dd, fecha_us.mm, fecha_us.aa)                 // SI la fecha se ingresa de este formato, se reformatea al que tiene la esctrucutra de fecha

        MIENTRAS NOFDA(facturas) HACER
            SI fac.f_fact > fecha_us Y fac.imp < 1000 ENTONCES
                ESCRIBIR(fac.nro, fac.f_fact.dd, fac.f_fact.mm, fac.f_fact.aa, fac.imp)
            FIN_SI
            LEER(facturas, fac)
        FIN_MIENTRAS
        CERRAR(facturas)
    FIN_PROCESO
FIN_ACCION
```

## 2.2.4.txt

```
// A partir de la secuencia del ejercicio 2.01 se desea generar otra secuencia con los alumnos de una carrera dada
// que aprobaron alguna materia este año, con nota mayor a 7 (siete).
//
// - Apellido y Nombre
// - Carrera (ISI - IEM - IQ)
// - Nº de Legajo
// - Fecha de Nacimiento
// - Fecha de Ingreso
// - D.N.I.
// - Sexo (M o F)
// - Fecha de último examen aprobado
// - Nota


ACCION 2_2_4 ES
    AMBIENTE

        carrera_ingresada: AN(30)                           // guarda la carrera que el usuario ingresa por teclado para filtrar
        año_actual: ENTERO                                  // guarda el año ingresado para comparar con el año del último examen del alumno

        FECHA = REGISTRO                                    // estructura auxiliar reutilizable para representar cualquier fecha
            dia: ENTERO                                     // día
            mes: ENTERO                                     // mes
            año: ENTERO                                     // año — este campo se usa luego para comparar si el examen fue este año
        FIN_REGISTRO


        ALUMNO = REGISTRO                                   // estructura que representa a un alumno con todos sus datos académicos y personales
            apynom: AN(40)
            carrera: ('isi','iem','iq','lar')
            legajo: ENTERO
            fecha_nac: FECHA                                // campos de tipo FECHA anidados dentro del registro ALUMNO
            fecha_ing: FECHA
            dni: N(8)
            sexo: ('M', 'F')
            fecha_ult_exam: FECHA                          // fecha del último examen aprobado — se accede al año con alu.fecha_ult_exam.año
            nota: ENTERO
        FIN_REGISTRO

    arch_alu, arch_alu_sal: Archivo de ALUMNO              // arch_alu: archivo de entrada con todos los alumnos | arch_alu_sal: archivo de salida filtrado
    alu, alusal: ALUMNO                                    // alu: variable para leer cada registro del archivo | alusal: variable para armar el registro de salida

    PROCESO
        Abrir E/(arch_alu); LEER(arch_alu, alu)            // abre el archivo de entrada en modo lectura y carga el primer registro en alu
        Abrir /S(arch_alu_sal);                            // abre el archivo de salida en modo escritura (empieza vacío)

        ESCRIBIR("Ingrese el AÑO ACTUAL y la CARRERA a consultar, en ese orden")
        LEER(año_actual, carrera_ingresada)                // el usuario define los dos criterios de filtro: año del examen y carrera buscada

        MIENTRAS NFDA(arch_alu) HACER                      // recorre el archivo de entrada completo hasta llegar al fin de archivo
            ESCRIBIR(alu.legajo, alu.apynom, alu.dni, alu.carrera)  // imprime por pantalla los datos básicos de cada alumno que se va procesando

            SI alu.carrera = carrera_ingresada Y alu.nota > 7 Y alu.fecha_ult_exam.año = año_actual ENTONCES  // triple condición: carrera coincide, nota aprobada con más de 7, y el examen fue en el año ingresado
                alusal := alu                              // como ambas variables son del mismo tipo ALUMNO, se puede copiar el registro completo de una sola vez
                ESCRIBIR(arch_alu_sal, alusal)             // escribe el registro en el archivo de salida — solo llegan acá los que cumplen las tres condiciones
            FIN_SI

            LEER(arch_alu, alu)                            // avanza al siguiente registro del archivo para continuar el ciclo
        FIN_MIENTRAS

        CERRAR(arch_alu); CERRAR(arch_alu_sal)             // cierra ambos archivos al terminar — importante para que el sistema libere los recursos
    FIN_PROCESO
FIN_ACCION
```

## 2.2.12.txt

```
Ejercicio 2.2.12¶
Dada una secuencia con información de población de un PAIS:

POBLACION Ordenado por Provincia, Departamento, Ciudad, Barrio, ID_Casa

ProvinciaDepartamentoCiudadBarrioID_CasaCantidad_Habitantes
Generar una secuencia con información de los departamentos de esa provincia, cuyo registro tenga el siguiente formato:

POBLACION_SALIDA

ProvinciaDepartamentoCantidad_Habitantes



Primero se crea el procedimiento de corte de menor nivel

en el proceso se abren los archivos, se inicializan los contadores, inicicializar los resguardo y mientras NFDA

Tratar corte es siempre igual, aprender d e memoria
y tratar registro depende de lo que tenga que hacer en la activdidad


se pregunta si el resguardo cambia, en caso de que si se aplica el corte

una vez tratado el registro, es importante leer el sigueiente regustro


dependiendo del corte, si se piden totales por ejemplo rubro o sucursal, se calcula por suma por rubro y por sucurslar


tratar corte tratar regisytro leer()
```

## 2.3.frre

```
2.3.10

Una empresa dedicada a la venta de combustibles para automotores anunció una promoción 
mediante la cual los clientes pueden acceder a descuentos importantes. 
En cada carga los clientes suman 10 puntos por cada $100 de combustible, y una vez que el cliente llega a los 100 puntos, 
este los puede canjear por un descuento de $100 en el importe total. La cantidad de puntos que tiene cada cliente está almacenado 
en el archivo indexado PUNTOS el cual tiene el siguiente formato:

PUNTOS Indexado por DNI

DNICant_PuntosUlt_Carga
Los datos de cada cliente se encuentran almacenados en el archivo CLIENTE también indexado con el siguiente formato

CLIENTE Indexado por DNI

DNI Ape_Nom Edad Ciudad
Se pide realizar el algoritmo que permita:

Realizar la carga interactiva de las cargas de combustible 
(ingresando monto), actualizando la cantidad de Puntos y la Fecha de Última Carga en el archivo PUNTOS. 
Si no existe el Cliente, se lo debe inicializar en ambos archivos con los datos correspondientes.
Permitir al cliente aplicar descuentos a las cargas realizadas siempre y cuando tenga puntos suficientes 
(sólo se puede canjear 100 puntos por carga).
Determinar la cantidad de cargas realizadas de usuarios no existentes.


ACCION ej2.3.10 ES
    AMBIENTE
        punto = REGISTRO
            DNI: ENTERO
            cant_punt: ENTERO
            ult_carga: FECHA
        FIN_REGISTRO

        puntos: ARCHIVO DE punto INDEXADO POR DNI

        p: punto

        cliente = REGISTRO
            DNI: ENTERO
            nombre: AN
            edad: ENTERO
            ciudad: AN
        FIN_REGISTRO

        clientes: ARCHIVO DE cliente INDEXADO POR DNI
        c: cliente

        monto: ENTERO
        cont: ENTERO; resp:('s','n')

    Proceso
        Abrir E/S(puntos); Abrir E/S(clientes)
        cont:= 0
        repetir 
            Escribir("Ingrese DNI del cliente")
            Leer(p.dni)
            Escribir("Ingrese el monto de la carga")
            Leer(monto)
            Leer(puntos,p)
            Si existe Entonces
                Si p.cant_puntos > 100 Entonces
                    Escribir("Quiere usar 100 puntos para aplicar el descuento")
                    Leer(respuesta)
                    Si respuesta = "s" Entonces
                        p.cant_puntos:= p.cant_puntos-100
                        monto:= monto-100
                        Escribir("Nuevo monto a pagar: ", monto)

                    Fin_Si
                Fin_Si
                p.cant_puntos:= p.cant_puntos + (monto div 100) * 10
                p.ultima_carga:= fechasistema()
                Reescribir(puntos,p)
            Fin_Si
        hasta que (resp = 'n')
        ESCRIBIR('La cantidad de altas fueron: ', cont)
        CERRAR(puntos); CERRAR(clientes)
Fin_Accion
```

## ##Te dan un array de enteros nums y un v.py

```python
##Te dan un array de enteros nums y un valor val. Tenés que remover in-place todas las apariciones de val, manteniendo el orden r
#elativo de los demás elementos. No importa qué quede después de la posición final — igual que en los ejercicios anteriores, devolvés k 
# (la cantidad de elementos que no son val), y solo las primeras k posiciones del array tienen que ser correctas.
##Ejemplo 1:
##Input: nums = [3,2,2,3], val = 3
##Output: k = 2, nums = [2,2,_,_]
##Ejemplo 2:
##Input: nums = [0,1,2,2,3,0,4,2], val = 2
##Output: k = 5, nums = [0,1,4,0,3,_,_,_]
##(el orden de los elementos que quedan puede variar, mientras sean los correctos)


nums = [3,2,2,3]
val = 3

def remove_val(nums):
    k=0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_val(nums))



# Maximum Sum Subarray of Size K
# Dado un array de enteros nums y un entero k, encontrá la suma máxima de cualquier subarray contiguo de tamaño exactamente k.
# Ejemplo:
# nums = [2, 1, 5, 1, 3, 2], k = 3
# Los subarrays de tamaño 3 son: [2,1,5]→8, [1,5,1]→7, [5,1,3]→9, [1,3,2]→6
# Output: 9 (el de [5,1,3])


nums = [2, 1, 5, 1, 3, 2]
k = 3

def sum_subarray(nums, k):
    # Paso 1: suma de la primera ventana (índices 0 a k-1)
    window_sum = sum(nums[0:k])
    mejor = window_sum

    # Paso 2 y 3: deslizar la ventana de a uno
    for i in range(k, len(nums)):
        # i = índice que entra (extremo derecho nuevo)
        # i - k = índice que sale (quedó k lugares atrás de i)
        window_sum = window_sum - nums[i - k] + nums[i]
        mejor = max(mejor, window_sum)

    return mejor


print(sum_subarray(nums, k))




def reverse_array(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
```

## Arreglos:

```
Arreglos: 

(Los arreglos son estructuras que estan en la memoria interna, no se puede modificar en ejecucion)

Que es un arreglo?: 
    Es una coleccion finita, homogena y ordenada de elementos

    Finita porque tiene un limite de elementos

    Homogenea porque sus compoenntes son del mismo tipo de dato

    Ordenada porque se puede identificar el primero, el segundo, etc


Por que existen los arreglos?
    Se utilizan para manejar variables dentro de los elementos por ejemplo a los contadores, accediendo a cada posicion

Los arreglos podrian ser unidimensionales y bidimensionales, siendo como vectores o matrices.

Esta compuesto por componentes e indices, como elementos. Es cada celda que lo compone. Se define un indice por dimension

Las operaciones que componen los arreglos, al ser un conjunto de variables es un tipo de dato estructurado, 



Se define de la sigueinte manera:

v: arreglo[1..50] de REAL;

Se accede mediante el indice v[i]


El indice puede ser de tipo de dato entero, conjutnos vocales("a","e","i","o","u") y el alfabeto


Declaracion de un vectores

v: arreglo[li..ls] DE TIPO X;

Donde el numero total de componentes esta dado por limite superior - limite inferior + 1


Para que se usan los vectores:

    Notas de alumnos, temperaturas diarias, stock de productos, nombre de meses


Declaracion de matrices

m: arreglo[1..f..1..c] DE TIPO X
m[2,5] <-- fila 2 columna 5

Se elige una matriz por sobre un vector dependiendo de la clase o tipo de la representacion de los elementos

Operaciones con arreglos:

    Carga de un vector


ACCION carga_vector ES:
    AMBIENTE 
        v: arreglo[1..50] DE ENTERO
        i: ENTERO
    PROCESO
        PARA i:=1 HASTA 50 HACER
            LEER(v[i])                  <----- Ingresa el valor directamente en esa posicion
        FIN_PARA
    FIN_PROCESSO
FIN_ACCION


    Recorrido y lectura de un vector:

ACCION leer_vector ES:
    AMBIENTE 
        v: arreglo[1..50] DE ENTERO
        i: ENTERO
    PROCESO
        PARA i:=1 HASTA 50 HACER
            ESCRIBIR(v[i])                  <----- Muestra el valor directamente en esa posicion
        FIN_PARA
    FIN_PROCESSO
FIN_ACCION



Accion CARGAR _MATRIZ ES;
    Ambiente
        m: arreglo [1..10, 1..5] de real;
        i, j: entero;
    Proceso
        PARA i:=1 HASTA 10 HACER
            PARA j:=1 HASTA 5 HACER
               Leer(m [i,j]);
        FIN_PARA;
    FIN_PARA;
FinAccion
```

## Corte de control.txt

```

```

## NyDNI

```
//Subsecuencias para escribir el Nombre y el DNI, sabiendo que el DNI tiene 8 caracteres. 
//Ademas mostrar cuantas personas fueron ya procesadas con un contador


ACCION NyDNI ES
    AMBIENTE
        sec: SEC DE CARACTERES
        v: CARACTER
        cont: ENTERO
    PROCESO
        ARRANCAR(sec); AVANZAR(sec, v)
        cont := 1

        MIENTRAS NFDS(sec) HACER
            ESCRIBIR('Nombre', cont)

            MIENTRAS v <> '-' HACER
                ESCRIBIR(v)
                AVANZAR(sec, v)
            FIN_MIENTRAS

            AVANZAR(sec, v)

            PARA i := 1 HASTA 8 HACER
                ESCRIBIR(v)
                AVANZAR(sec, v)
            FIN_PARA

            cont := cont + 1
        FIN_MIENTRAS
FIN_ACCION
```

## Parcial.1.txt

```
//Ejercicio N° 1 Una cadena de hoteles necesita un informe de ocupación y pagos para el mes de JUNIO. Para
//esto, se cuenta con dos secuencias de datos:
//
//Secuencia de caracteres:
//
//Estructura: Hotel (cantidad indeterminada de caracteres) & cantidad de reservas (3 caracteres)
//hotel & cantidad de reservas....FDS
//Ejemplo: HotelAlas&340HotelBahia&999... FDS
//
//Secuencia de enteros: Estructura: Para cada reserva: Nro de reserva, tipo de habitación (1: single, 2: doble, 3: suite),
//cantidad de noches, importe.
//
//Ejemplo: 1234|1|3|120.000|2345|3|2| 65.000 |...FDS
//
//Nota: La función ConvertiraNumero(caracter) puede ser utilizada si se considera necesario para
//convertir un carácter a un dato entero.
//
//Se pide escribir un algoritmo que permita: 
//
//1) Generar una secuencia de salida de enteros que contenga el número de reserva y el importe,
//cuando el importe sea menor a 90.000.
//
//2) Informe, para cada hotel, cuál fue la reserva (NroReserva) con mayor cantidad de noches (y la
//cantidad de noches).



ACCION parc1 ES
    AMBIENTE 
        sec, secsal: SECUENCIA DE ENTEROS
        sech: SECUENCIA DE CARACTERES
        cont, vs, cantres, reserva, resmay, noches, nocmay, i: ENTERO 
        vh: CARACTER

        PROCEDIMIENTO maroya(res: ENTERO, noc: ENTERO) 
            AMBIENTE
                // Sin variables locales
            PROCESO
                // Corrección: Solo evaluamos si es mayor al máximo actual
                SI noc > nocmay ENTONCES
                    resmay := res
                    nocmay := noc
                FIN_SI 
        FIN_PROCEDIMIENTO

    PROCESO
        // Corrección: el contador de hoteles se inicializa una sola vez al inicio
        cont := 0 
        
        CREAR(secsal)
        ARRANCAR(sec); ARRANCAR(sech)
        AVANZAR(sec, vs); AVANZAR(sech, vh)
    
        // Corrección sintáctica: NFDS
        MIENTRAS NFDS(sech) HACER
            
            // Corrección: Inicializar los máximos CADA VEZ que arranca un hotel
            nocmay := -1
            resmay := 0
            
            // Seguridad: agregamos NFDS al ciclo interno
            MIENTRAS NFDS(sech) Y vh <> "&" HACER
                AVANZAR(sech, vh)
            FIN_MIENTRAS
    
            AVANZAR(sech, vh) // Supera el '&'
    
            cantres := convertiranumero(vh) * 100
            AVANZAR(sech, vh)
            cantres := cantres + convertiranumero(vh) * 10
            AVANZAR(sech, vh)
            cantres := cantres + convertiranumero(vh)
            
            AVANZAR(sech, vh) // Avanza al primer carácter del próximo hotel
    
            PARA i := 1 HASTA cantres HACER
                reserva := vs
                AVANZAR(sec, vs) // Salto el tipo de habitación
                AVANZAR(sec, vs) 
                
                noches := vs
                maroya(reserva, noches)
                
                AVANZAR(sec, vs) 
    
                SI vs < 90000 ENTONCES
                    ESCRIBIR(secsal, reserva)
                    ESCRIBIR(secsal, vs)
                FIN_SI // Corrección: faltaba cerrar el SI
                
                // Corrección: Se saca el AVANZAR fuera del condicional
                AVANZAR(sec, vs) 
                
            FIN_PARA
            
            cont := cont + 1
            ESCRIBIR("Para el hotel numero ", cont, " la reserva con mayor cantidad de noches fue ", resmay, " con ", nocmay)
            
        FIN_MIENTRAS
        
        // Corrección: Clausura obligatoria de estructuras
        CERRAR(sec)
        CERRAR(sech)
        CERRAR(secsal)
        
FIN_ACCION




//Ejercicio N° 2
//La red de estaciones de carga urbana para vehículos eléctricos (VE) dispone de un sistema de monitoreo que
//registra las sesiones de carga realizadas durante el mes de JUNIO. La información se encuentra ordenada por
//Número de Estación, Tipo de Vehículo, y Número de Carga, y para cada sesión de carga se registra:
//Nro. de Estación Tipo de Vehículo

//(SD, SV, UT) Nro. Carga Fecha de carga Duración carga

//(minutos) Costo carga

//Nota: SD: Sedan. SV: Suv y UT: Utilitario
//Se pide escribir un algoritmo para:
//a) Listar todas las cargas de la primera quincena.
//b) Mostrar el total recaudado por estación y por tipo de vehículo.
//c) Crear un archivo de salida que contenga, por cada estación:
//• Número de Estación
//• Total recaudado en vehículos de tipo UTILITARIO
//d) Informar cuáles son las estaciones de carga que tuvieron mayor recaudación en vehículos tipo SEDAN que en
//vehículos tipo UTILITARIO.


ACCION ej_parcial_1_2 ES
    AMBIENTE

        fecha = REGISTRO
            dia: ENTERO
            mes: ENTERO
            año: ENTERO
        FIN_REGISTRO

        reg = REGISTRO
            clave = REGISTRO
                nro_estacion: ENTERO
                tipo_veh: ALFANUMERICO
                nro_carga: ENTERO
            FIN_REGISTRO
            fecha_carg: FECHA
            dura_carg: ENTERO
            costo_carg: REAL
        FIN_REGISTRO

        regsal = REGISTRO
            nro_estacion_sal: ENTERO
            total_ut: ENTERO
        FIN_REGISTRO

        arch: Archivo de reg ordenado por clave
        arch_sal = Archivo de regsal

        total_quinc, may_estac: ENTERO
        total_rec, total_rec_util: REAL
        
        
    PROCESO
```

## Parcial.2.txt

```
//Ejercicio N° 1
//Durante la Feria del Libro se relevó información sobre las editoriales participantes y los libros que presentan. Los
//datos fueron almacenados en dos secuencias de caracteres, las cuales deben ser procesadas para obtener distintos
//informes.
//
//Datos de Entrada
//A. Secuencia de Editoriales:
//Cada editorial está representada de la siguiente manera:
//
//- Nombre de la editorial (cantidad indeterminada de caracteres, finaliza con ‘&’)
//- Provincia (2 caracteres que representan un número del ‘01’ al ‘23’)
//Ejemplo: Planeta&01Sudamericana&03...
//
//B. Secuencia de Libros:
//
//Por cada editorial hay una cantidad indeterminada de libros, separados por el carácter ‘@’. Cada libro contiene los
//siguientes campos:
//
//- Tema (1 carácter): L = Literatura / C = Ciencia / A = Autoayuda y desarrollo personal / I = Infantiles
//- Cantidad de páginas: (3 caracteres, por ejemplo 245)
//- Nombre del libro: (cantidad indeterminada de caracteres, finaliza con ‘&’)
//- Resumen: texto libre (finaliza con el carácter ‘#’).
//Las palabras están separadas por una cantidad variable de espacios en blanco.
//
//Ejemplo:
//
//L245Elprincipito&Una vida a vivir y aprender.#@C120FisicaParaTodos&Conceptos basicos para jovenes.#...
//Se solicita escribir un algoritmo en pseudocódigo que permita:
//
//a) Generar una secuencia de salida con los nombres de los libros de tema ‘Literatura’ (tema = ‘L’) que tengan más
//de 200 y hasta 300 páginas inclusive.
//
//b) Para cada editorial, informar la longitud promedio de los resúmenes, expresada en cantidad de palabras (una
//palabra se define como una secuencia de caracteres alfabéticos, separada por espacios en blanco).
//
//c) Indicar en qué provincia se encuentra la editorial con mayor cantidad de libros presentados.
//En caso de ser necesario, escribir una función auxiliar para convertir secuencias de caracteres a valores numéricos.


ACCION Ejercicio_Feria_Libro ES
    AMBIENTE
        sec_ed, sec_lib, sec_sal : SECUENCIA DE CARACTERES
        ve, vl : CARACTER
        
        // Variables para la Editorial
        prov, prov_max, max_libros : ENTERO
        
        // Variables para los Libros y Cálculos
        tema_lib : CARACTER
        cant_pags, cant_libros_ed, tot_palabras_ed : ENTERO
        es_objetivo : LOGICO

        // Función obligatoria para convertir caracteres a números.
        // Las subacciones deben tener su propio AMBIENTE y PROCESO aislados [4, 5].
        FUNCION car_a_ent(x : CARACTER) : ENTERO
            AMBIENTE
            PROCESO
                SEGUN x HACER
                    '0': car_a_ent := 0 
                    '1': car_a_ent := 1 
                    '2': car_a_ent := 2 
                    '3': car_a_ent := 3 
                    '4': car_a_ent := 4 
                    '5': car_a_ent := 5 
                    '6': car_a_ent := 6 
                    '7': car_a_ent := 7 
                    '8': car_a_ent := 8 
                    '9': car_a_ent := 9 
                FIN_SEGUN
        FIN_FUNCION

    PROCESO
        // 1. Inicialización Global
        // Se inicializa el máximo fuera de todos los ciclos para no perder su valor [6, 7].
        max_libros := -1 

        // 2. Preparación de Motores (Secuencias)
        // El verbo ARRANCAR ubica el motor antes del primer elemento, y CREAR inicializa la cinta vacía [8, 9].
        ARRANCAR(sec_ed); AVANZAR(sec_ed, ve)
        ARRANCAR(sec_lib); AVANZAR(sec_lib, vl)
        CREAR(sec_sal)

        // 3. MOTOR PRINCIPAL: Recorre las editoriales.
        // Usamos MIENTRAS porque la secuencia es Indefinida Impura [10].
        MIENTRAS NFDS(sec_ed) HACER
            
            // --- CINTA A: Procesar Editorial ---
            // 3.1. Saltar el nombre de la editorial (termina en '&')
            MIENTRAS NFDS(sec_ed) Y ve <> '&' HACER
                AVANZAR(sec_ed, ve)
            FIN_MIENTRAS
            
            AVANZAR(sec_ed, ve) // AVANCE VITAL: Superar el '&' para leer el número.

            // 3.2. Leer la Provincia (Sabemos que son 2 caracteres exactos)
            prov := car_a_ent(ve) * 10
            AVANZAR(sec_ed, ve)
            prov := prov + car_a_ent(ve)
            
            AVANZAR(sec_ed, ve) // AVANCE VITAL: Dejar la cinta lista para la próxima editorial.

            // 4. Inicialización Local (Por cada Editorial)
            // Estos contadores se resetean a 0 cada vez que empezamos una editorial nueva.
            cant_libros_ed := 0
            tot_palabras_ed := 0

            // --- CINTA B: Procesar Libros de esta Editorial ---
            // El '@' es el Fin de Secuencia (FDS) local de los libros de esta editorial [11, 12].
            MIENTRAS NFDS(sec_lib) Y vl <> '@' HACER
                
                cant_libros_ed := cant_libros_ed + 1 // Contamos un libro nuevo
                
                // 4.1. Leer Tema
                tema_lib := vl
                AVANZAR(sec_lib, vl)
                
                // 4.2. Leer Páginas (Sabemos que son 3 caracteres)
                cant_pags := car_a_ent(vl) * 100
                AVANZAR(sec_lib, vl)
                cant_pags := cant_pags + car_a_ent(vl) * 10
                AVANZAR(sec_lib, vl)
                cant_pags := cant_pags + car_a_ent(vl)
                AVANZAR(sec_lib, vl) // Superamos el último dígito
                
                // 4.3. Evaluar Condición (Punto A)
                // Usamos operadores lógicos para evaluar múltiples datos y guardar el resultado [13].
                SI tema_lib = 'L' Y (cant_pags > 200 Y cant_pags <= 300) ENTONCES
                    es_objetivo := V
                SINO
                    es_objetivo := F
                FIN_SI

                // 4.4. Procesar Nombre del Libro
                MIENTRAS NFDS(sec_lib) Y vl <> '&' HACER
                    // Si el libro cumple, lo escribimos en la secuencia nueva [14].
                    SI es_objetivo = V ENTONCES
                        ESCRIBIR(sec_sal, vl)
                    FIN_SI
                    AVANZAR(sec_lib, vl)
                FIN_MIENTRAS
                
                AVANZAR(sec_lib, vl) // AVANCE VITAL: Superar el '&'

                // 4.5. Procesar Resumen (Subsecuencia Jerárquica: Palabras) [2, 12]
                MIENTRAS NFDS(sec_lib) Y vl <> '#' HACER
                    
                    // Ignorar espacios en blanco múltiples
                    MIENTRAS NFDS(sec_lib) Y vl = ' ' HACER
                        AVANZAR(sec_lib, vl)
                    FIN_MIENTRAS
                    
                    // Si no chocamos con el fin del resumen, hay una palabra
                    SI vl <> '#' ENTONCES
                        tot_palabras_ed := tot_palabras_ed + 1
                        
                        // Recorrer la palabra hasta el próximo espacio o el '#'
                        MIENTRAS NFDS(sec_lib) Y vl <> ' ' Y vl <> '#' HACER
                            AVANZAR(sec_lib, vl)
                        FIN_MIENTRAS
                    FIN_SI
                    
                FIN_MIENTRAS
                
                AVANZAR(sec_lib, vl) // AVANCE VITAL: Superar el '#' para ir al próximo libro.
                
            FIN_MIENTRAS // Fin de los libros de ESTA editorial

            // AVANCE VITAL: Superar el delimitador '@' en la cinta B, 
            // así queda lista para la próxima editorial en el ciclo general principal.
            SI vl = '@' ENTONCES
                AVANZAR(sec_lib, vl)
            FIN_SI

            // 5. Cálculos Estadísticos de la Editorial (Punto B y C)
            // Seguro contra fallo de división por cero [15].
            SI cant_libros_ed > 0 ENTONCES
                ESCRIBIR("Editorial de Provincia ", prov, " - Promedio de palabras por resumen: ", tot_palabras_ed / cant_libros_ed)
            SINO
                ESCRIBIR("La editorial de la Provincia ", prov, " no presentó libros.")
            FIN_SI
            
            // Evaluar el máximo de libros
            SI cant_libros_ed > max_libros ENTONCES
                max_libros := cant_libros_ed
                prov_max := prov
            FIN_SI

        FIN_MIENTRAS // Fin del recorrido de todas las editoriales

        // 6. Clausura y Resultados Finales
        ESCRIBIR("La provincia con la editorial de mayor cantidad de libros es: ", prov_max)
        
        // Obligatorio cerrar los archivos/secuencias para liberar la memoria buffer [16].
        CERRAR(sec_ed)
        CERRAR(sec_lib)
        CERRAR(sec_sal)

FIN_ACCION
```

## Parcial.3.txt

```
//Ejercicio 1 
//Se lanzó la preventa del Primavera Sound 2023, la modalidad que se elige es lanzar una preventa de entradas, sin anunciar los artistas que
//se presentarán. Los early birds #1 (preventa de entradas), se lanzarán el 1 de mayo de 2023 a las 13:00 hs, pero los fanáticos pueden hacer
//“fila virtual” desde las 00:00 para asegurar su lugar en el famoso festival, una vez que se lance la venta virtual los usuarios pueden ir
//comprando las entradas de a tandas.
//
//Con la finalidad de analizar si se debe optimizar el rendimiento de la plataforma, se disponen dos secuencias de caracteres. La primera
//secuencia contiene a los fanáticos que hacen la “fila virtual”, esta secuencia contiene la hora en la que se registró en la fila (hhmm), el
//número en la fila (6 caracteres), el medio de pago con el que piensa pagar (“T”- tarjeta, “C”-efectivo, “E”-transferencia) y cuántas entradas
//piensa comprar (como máximo puede comprar 5 entradas).
//
//En estos sistemas de fila, al colocarse en ella se obtiene un identificador o número de fila, pero recién el usuario inicia sesión al llegar a su
//lugar en la fila y entrar a la sección de Compras.
//
//En una segunda secuencia se encuentran las compras reales realizadas, esta secuencia contiene el número en la fila (6 caracteres), el
//nombre de usuario (cantidad indefinida, termina en “+”), y luego contiene los datos de para quién es cada entrada en la compra,
//incluyendo su DNI y nombre (separados con ‘.’). Una compra finaliza con un “?”.
//
//Secuencia Fila_Virtual:
//horafilanumerofilamediopagocantentradas#
//Ejemplo:
//0301123456T3#0345234567E4#
//
//Secuencia Compras:
//numerofilanombre_usuario+dninombre.dninombre.dninombre?
//Ejemplo:
//123456unsuario+33254787Juan.27895614Melisa.36257489Pedro?
//
//Si por algún motivo algún fanático deja su lugar en la fila, en la secuencia de Compras en nombre de usuario aparece un carácter “#”, el
//signo “+” y luego la marca “?”. Esto implica una correspondencia 1 a 1 entre las dos secuencias.
//
//Escriba un algoritmo en pseudocódigo que resuelva las siguientes consignas:
//a) Generar una secuencia de salida con los nombres de usuario y cada DNI de las entradas compradas que fueron pagadas con
//Tarjeta. Separar cada campo con un + y finalizar con “#” al completar la compra de un usuario.
//EJ: nombreusuario+dni+dni#nombreusuario+dni+dni#
//
//b) Se desea conocer cuántos usuarios compraron una cantidad de entradas distinta a la que declararon en la fila virtual.
```

## Resgistros

```
Un campo es la entidad lógica más pequeña y la unidad mínima de información que conforma el registro.

Un registro es un conjunto de datos heterogéneos.

Todo campo requiere una declaración basada en tres atributos esenciales: nombre, tipo, tamaño.

    Ejemplo:
    {
        dni:    N(8)
        carrera: ('isi', 'iq', 'iem', 'lar')   -- tipo de dato enumerado
    }


Declaración de ambiente (estructura):

    AMBIENTE
        PERSONA = REGISTRO      -- No se ocupa "PERSONA", es solo la estructura.
                                -- Se accede con persona.dni o reg.campo
            DNI:       ENTERO
            NOMBRE:    AN(50)
            DOMICILIO: AN(70)
        FIN_REGISTRO

    Asignación: reg.dni := 12131231


Los registros anidados son cuando existen estructuras dentro de otra.
Por ejemplo, las fechas que se definen como una estructura aparte.

Un archivo secuencial es un conjunto de registros.

LEER() lee todo el registro entero, ESCRIBIR() también escribe todo el registro completo.

Clave compuesta: dos o más campos que juntos forman una llave única para identificar.

Flujo de archivo esencial:

    Abrir → Leer → Control (no FDA) → ... → Cerrar
```

## un archivo indexado es una tabla de indi

```
un archivo indexado es una tabla de indices que estan ordenados secuencialmentes las claves del arhcivos asociado a 
unon d eellos en la direccion fisica


para acceder al registro necesitamos saber la clave id 

Se define de la siguiente manera:

DATO=registro
    CLAVE:...
    CAMPO2:...



Se abre de la siguiente manera:

ABRIR E/S (variable_archivo).  <---- Se puede abrir de entrada/salida


Para accerder a los registros

reg.clave := valor_buscado

LEER(arch,reg)

Podemos usar un SI EXISTE ENTONCES para preguntar por la existencia del mismo


ESCRIBIR(arch,reg) <--- Para escirbir un registro

REESCRIBIR(arch,reg) <----- Para cambiar algun campo que NO sea la clave

ELIMINAR(arch,reg) <----- Eliminar el registro (baja fisica)
```
