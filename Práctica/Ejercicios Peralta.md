---
tipo: practica
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - ejercicios
---

# Ejercicios Peralta

> [!abstract] Qué hay acá
> Resoluciones de **Peralta**. El set más completo: cada ejercicio suele venir en dos versiones — el `.txt` con el pseudocódigo de cátedra y el `.py` con la misma lógica traducida a Python para poder correrla.
> **30 archivos**, transcriptos íntegros desde `Practica/Ejercicios Peralta/`.
> Los originales siguen intactos en esa carpeta; esto es una copia legible dentro de Obsidian.

---

## Índice

- [[#1.1.5.1.py]]
- [[#1.1.5.1.txt]]
- [[#1.1.5.2.py]]
- [[#1.1.5.2.txt]]
- [[#1.1.5.3.py]]
- [[#1.1.5.3.txt]]
- [[#1.1.6 CORREGIR.txt]]
- [[#1.1.6.py]]
- [[#1.1.12.py]]
- [[#1.1.12.txt]]
- [[#1.1.24.py]]
- [[#1.1.24.txt]]
- [[#1.1.28.py]]
- [[#1.1.28.txt]]
- [[#1.1.35.py]]
- [[#1.1.35.txt]]
- [[#1.2.11.py]]
- [[#1.2.11.txt]]
- [[#1.2.12.txt]]
- [[#1.11.py]]
- [[#1.11.txt]]
- [[#1.12.py]]
- [[#1.12.txt]]
- [[#1.13.py]]
- [[#1.13.txt]]
- [[#1.14.py]]
- [[#1.14.txt]]
- [[#1.15.txt]]
- [[#2.1.19]]
- [[#2.2.18.txt]]

---

## 1.1.5.1.py

```python
C=float(input("Ingrese el precio actual del articulo: "))
N=int(input("Ingrese el año actual: "))
R=float(input("Ingrese la tasa de inflacion: "))
A=int(input("Ingrese el año futuro: "))
P = C*(1+R)**(N-A)
print("El precio final es: ", (C*(1+R)**(N-A)) )
```

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

## 1.1.5.2.py

```python
# Las raíces de una ecuación de segundo grado ax2+bx+c=0 son reales si y sólo si el discriminante dado por (b2−4ac) no es negativo. Se desea leer el valor de los coeficientes a, b, c e imprimir el resultado del discriminante. Realizar prueba de escritorio.


a=float(input("Ingrese el primer coeficiente: "))
b=float(input("Ingrese el segundo coeficiente: "))
c=float(input("Ingrese el tercer coeficiente: "))

print('El resultado del discriminante es: ', ((b**2)-4*a*c))
```

## 1.1.5.2.txt

```
Las raíces de una ecuación de segundo grado ax2+bx+c=0 son reales si y sólo si el discriminante dado por (b2−4ac) no es negativo. Se desea leer el valor de los coeficientes a, b, c e imprimir el resultado del discriminante. Realizar prueba de escritorio.

Accion 1.1.5.2 es
    Ambiente
        a,b,c,result: real

    Algoritmo
        Escribir("Ingrese los valores de los coeficientes a,b,c"); Leer(a,b,c)

        result:= (b**2-4*a*c)
```

## 1.1.5.3.py

```python
# Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado por la suma de los precios de costos, los porcentajes de ganancia del vendedor y un 21% de IVA. Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora. Se leen los costos y se imprimen el precio total de ventas.

iva= 1.21
GanPC= 1.12
GanIMP=1.07

precioPC= float(input("Ingrese el precio del PC: "))
precioIMP=float(input("Ingrese el precio de la impresora: "))

precioPC=(precioPC*GanPC)*iva
precioIMP=(precioIMP*GanIMP)*iva

total=precioPC+precioIMP

print("El precio total es de: ",total)
```

## 1.1.5.3.txt

```
Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado por la suma de los precios de costos, los porcentajes de ganancia del vendedor y un 21% de IVA. Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora. Se leen los costos y se imprimen el precio total de ventas.


Accion 1.1.5.3 es
    Ambiente
        iva= 1.21
        GanPC= 1.12
        GanIMP=1.07

        PC,IMP,total:Real
        precioPC,precioIMP:Real
    Algoritmo

        Escribir("Ingrese el precio de la PC"); Leer(PC)
        Escribir("Ingrese el precio de la Impresora"); Leer(IMP)

        precioPC:= (PC*GanPC)*iva
        precioIMP:= (IMP*GanIMP)*iva
        total:= precioPC+precioIMP
        escribir("El precio total de la venta es de: ", total)
    FinAlgoritmo
FinAccion
```

## 1.1.6 CORREGIR.txt

```
Escriba un algoritmo que permita ingresar 3 valores numéricos y determine cuál es el mayor, el medio y el menor. (era el 3 de los complementarios)

Accion 1.1.6 
    Ambiente
        a,b,c:entero
    Algoritmo
        ESCRIBIR("Ingrese 3 valores numericos para determinar el mayor, el del medio y el menor")
        Leer(a,b,c)

        SI (a>b y b>c) ENTONCES 
            ESCRIBIR("el mayor es",a," el del medio ",b,"y el del menor " ,c) //a b c
        SINO
            SI (a>c y c>b) ENTONCES
                ESCRIBIR("el mayor es ",a,"el del medio ",c," y el menor ",b)//a c b
            SINO
                SI (b>a y a>c) ENTONCES 
                    ESCRIBIR("el mayor es ",b,"el del medio ",a," y el menor ",c)//b a c 
                SINO
                    SI (b>a y c>a) ENTONCES 
                        ESCRIBIR("el mayor es ",b,"el del medio ",c," y el menor ",a)//b c a 
                    SINO
                        SI (c>a y a>b) ENTONCES 
                            ESCRIBIR("el mayor es ",c,"el del medio ",a," y el menor ",b)//c a b
                        SINO
                            SI (c>a y b>a) ENTONCES 
                                ESCRIBIR("el mayor es ",c,"el del medio ",b," y el menor ",a)//c b a 
                            FIN_SI
                        FIN_SI
                    FIN_SI 
                FIN_SI
            FIN_SI
        // FIN_SI

        
        
FinAccion
```

## 1.1.6.py

```python

while True:
    a=int(input("Ingrese el valor de a "))
    b=int(input("Ingrese el valor de b "))
    c=int(input("Ingrese el valor de c "))
    if (a>b and b>c):
        print(" caso 1 el mayor es",a," el del medio ",b,"y el menor " ,c)# a b c
    elif (a>c and c>b):
        print(" caso 2 el mayor es ",a,"el del medio ",c," y el menor ",b)# a c b
    elif (b>a and a>c):
        print("caso 3 el mayor es ",b,"el del medio ",a," y el menor ",c)# b a c
    elif (b>c and c>a):
        print("caso 4 el mayor es ",b,"el del medio ",c," y el menor ",a)#b c a
    elif (c>a and a>b):
        print("caso 5 el mayor es ",c,"el del medio ",a," y el menor ",b)#c a b
    else:#a=1 b=2 c=3
        print("caso 6 el mayor es ",c,"el del medio ",b," y el menor ",a)#c b a
    print()
```

## 1.1.12.py

```python
# Ejercicio 1.1.12
# Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000, y muestre como
# está compuesto (unidades, decenas y centenas) y si es múltiplo de 3 (Recordar: todo número600
# cuya suma de sus dígitos sea múltiplo de 3, 10 es también).

num= int(input("Ingrese un numero entre 100 y 1000: "))
if num>100 and num<1000:
    centena=num//100
    decena=(num%100)//10
    unidad=decena%10
    
    suma=centena+decena+unidad
    
    if (suma%3)==0:
        print(f"el numero {num} es multiplo de 3")
    else:
        print(f"el numero {num} no es multiplo de 3")
    print("El numero Ingresado esta compuesto por")
    print(f"{centena} centenas")
    print(f"{decena} decenas")
    print(f"{unidad} unidades")
else:
    print("Ingreso un numero que no esta entre 100 y 1000")
```

## 1.1.12.txt

```
// Ejercicio 1.1.12
// Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000, y muestre como
// está compuesto (unidades, decenas y centenas) y si es múltiplo de 3 (Recordar: todo número
// cuya suma de sus dígitos sea múltiplo de 3, lo es también).

Accion 1.1.12 es
    Ambiente
        numero,centena,decena,unidad,sumanum:entero
    Proceso
        Escribir("Ingrese el numero mayor a 100 y menor a 1000: "); Leer(numero)
        si (numero>100) y (numero<1000) Entonces

            centera:=numero div 100 
            decena:= numero mod 100 
            decena:= decena div 10
            unidad:= decena mod 10

            Escribir("El numero esta compuesto por")
            Escribir(centena," Centenas")
            Escribir(decena," Decenas")
            Escribir(unidad," Unidades")

            sumanum:=centena+decena+unidad
            sumanum:=sumanum mod 3

            Si (sumanum=0) Entonces
                Escribir("El numero es multiplo de 3")
            Sino
                Escribir("El numero no es multiplo de 3")
            FinSi

        Sino
            Escribir("No ingreso un numero entre 100 y 1000")
        FinSi
    FinProceso
FinAccion
```

## 1.1.24.py

```python
# Ejercicio 1.1.24
# Escribir un algoritmo que, dado un importe dinero, permia calcular e informar cuanto
# corresponde pagar por un impuesto, en cuantas cuotas y el valor de las mismas. Tener en cuenta
# los siguientes datos:
# • IMPUESTO = 10% del importe dado.
# • Los importes mayores que $500 y menor o igual que $1000 se pagan en dos cuotas.
# • Los mayores de $1000 en tres cuotas. EI algoritmo debe permitir tratar varios importes
# finalizando cuando se ingresa 9999 como importe.

importe=int(input("Ingrese el importe para calcular el impuesto (9999 para salir): "))
while importe != 9999:
    impuesto=importe*0.10
    cuotas=1
    if importe>500 and importe<=1000:
        cuotas=2
    elif importe>1000:
        cuotas=3
    pagocuota=impuesto/cuotas
    print(f"El impuesto correspondiente al importe de ${importe} es del 10% ${impuesto} El impuesto se va a pagar en {cuotas} cuotas de ${pagocuota}")
    print()
    importe=int(input("Ingrese el importe para calcular el impuesto (9999 para salir): "))
```

## 1.1.24.txt

```
// Ejercicio 1.1.24
// Escribir un algoritmo que, dado un importe dinero, permia calcular e informar cuanto
// corresponde pagar por un impuesto, en cuantas cuotas y el valor de las mismas. Tener en cuenta
// los siguientes datos:
// • IMPUESTO = 10% del importe dado.
// • Los importes mayores que $500 y menor o igual que $1000 se pagan en dos cuotas.
// • Los mayores de $1000 en tres cuotas. EI algoritmo debe permitir tratar varios importes
// finalizando cuando se ingresa 9999 como importe.

Accion 1.1.24 es
Ambiente
    IMPORTE,IMPUESTO:REAL
    PAGOCUOTA:REAL
    CUOTAS:ENTERO
    NumeroBool: Booleano
    
Proceso
    Escribir("Ingrese el Importe"); Leer(IMPORTE)
    Mientras(IMPORTE<>9999) 
        IMPORTE:=IMPORTE*1.10
        importe imsporte hacer
            <500: cuotas:=1
            >500 y importe<=1000:cuotas:=2
            >1000 : cuotas:=3
        finsegun
        PAGOCUOTA:=IMPORTE/CUOTAS
        Escribir("El impuesto correspondiente al importe de $",IMPORTE,"es de $",IMPUESTO," el impuesto se va a pagar en ", CUOTAS," cuotas de $", PAGOCUOTA)
        Escribir("Ingrese el Importe"); Leer(IMPORTE)
    FinMientras
FinProceso
FinAccion
```

## 1.1.28.py

```python
# Ejercicio 1.1.28
# Construya un algoritmo capaz de encontrar todas las cifras de tres dígitos que cumplan con la
# condición de que la suma de los cubos de sus dígitos sea igual al número que la cifra
# representa.
for num in range(100, 1000):
    centenas=num//100
    decenas=(num % 100)//10
    unidades= num % 10

    suma_cubos=(centenas**3)+(decenas**3)+(unidades**3)

    if suma_cubos == num:
        print(f"El numero: {num} cumple la condicion")
```

## 1.1.28.txt

```
// Ejercicio 1.1.28
// Construya un algoritmo capaz de encontrar todas las cifras de tres dígitos que cumplan con la
// condición de que la suma de los cubos de sus dígitos sea igual al número que la cifra
// representa.

Accion 1.1.28 es
Ambiente
Proceso
    Para i = 100 hasta 999 Hacer
        centena=i div 100
        decena=(i mod 100)div 10
        unidad=decena mod 10

        suma:=centena**3+decena**3+unidad**3
        Si suma=i Entonces
            Escribir("El numero", i,"Cumple la condicion")
        FinSi
    FinPara
FinProceso
FinAccion
```

## 1.1.35.py

```python
# Ejercicio 1.1.35
# Escriba un algoritmo que acepte un número entero que representa una suma de dinero e indique
# cuantos billetes de cada denominación necesita, suponiendo que solo existen billetes de 500, 100, 50, 20, 10, 5y1 peso.

monto = int(input("Ingrese el monto(entero): "))
b500 = monto // 500
monto %= 500
b100 = monto // 100
monto %= 100
b50 = monto // 50
monto %= 50
b20 = monto // 20
monto %= 20
b10 = monto // 10
monto %= 10
b5 = monto // 5
monto %= 5
b1 = monto  
print("Billetes necesarios:")
print(f"500: {b500}")
print(f"100: {b100}")
print(f" 50: {b50}")
print(f" 20: {b20}")
print(f" 10: {b10}")
print(f"  5: {b5}")
print(f"  1: {b1}")
```

## 1.1.35.txt

```
// Ejercicio 1.1.35
// Escriba un algoritmo que acepte un número entero que representa una suma de dinero e indique
// cuantos billetes de cada denominación necesita, suponiendo que solo existen billetes de 500,
// 100, 50, 20, 10, 5 y 1 peso.

Accion 1.1.35 es
Ambiente
    dinero,b500,b100,b50,b20,b10,b5,b1:ENTERO
Proceso
    Escribir("Ingrese el monto()"); Leer(dinero)
    b500:= dinero div 500
    dinero:= dinero mod 500
    
    b100:= dinero div 100
    dinero:= dinero mod 100

    b50:= dinero div 50
    dinero:= dinero mod 50

    b20:= dinero div 20
    dinero:= dinero mod 20

    b10:= dinero div 10
    dinero:= dinero mod 10

    b5:= dinero div 5
    dinero:= dinero mod 5

    b1:= dinero div 1
    dinero:= dinero mod 
    
    Escribir("Billetes que se necesitan:")
    Escribir(b500,"de 500")
    Escribir(b100,"de 100")
    Escribir(b50,"de 50")
    Escribir(b20,"de 20")
    Escribir(b10,"de 10")
    Escribir(b5,"de 5")
    Escribir(b1,"de 1")
FinProceso
FinAccion
```

## 1.2.11.py

```python
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def menu():
    print("Ingrese el numero de la opcion a la que quiere ingresar")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

def leerVar():
    global num1,num2
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    
menu()
x=int(input())
leerVar()
if x == 1:
    print(f"El resultado de la suma es: {sumar(num1,num2)}")
elif x == 2:
    print(f"El resultado de la resta es: {restar(num1,num2)}")
elif x == 3:
    print(f"El resultado de la multiplicacion es: {mul(num1,num2)}")
elif x == 4:
    print(f"El resultado de la division es: {div(num1,num2)}")
```

## 1.2.11.txt

```
Accion 1.2.11 es
Ambiente
    num1,num2:Real
    x:entero

    Procedimiento Menu()
        Escribir("Ingrese el numero correspondiente a la funcion que quiere usar:");
        Escribir("1. Sumar")
        Escribir("2. Restar")
        Escribir("3. Multiplicar")
        Escribir("4. Dividir")
    FinProcedimiento

    Procedimiento RecibirVar()
        Escribir("Ingrese el primer numero"); Leer(num1)
        Escribir("Ingrese el segundo numero"); Leer(num2)
    FinProcedimiento

    Funcion Suma(a,b:Real):Real
        Suma:=a+b
    FinFuncion

    Funcion Resta(a,b:Real):Real
        Resta:=a-b
    FinFuncion

    Funcion Multiplicacion(a,b:Real):Real
        Multiplicacion:=a*b
    FinFuncion

    Funcion Division(a,b:Real):Real
        Division:=a/b
    FinFuncion

Proceso
    Menu()
    Leer(X)
    RecibirVar()
    Segun x Hacer
        =1 : Escribir("El resultado es:", Suma(num1,num2))
        =2 : Escribir("El resultado es:", Resta(num1,num2))
        =3 : Escribir("El resultado es:", Multiplicacion(num1,num2))
        =4 : Escribir("El resultado es:", Division(num1,num2))
    FinSegun

FinProceso
```

## 1.2.12.txt

```
Ejercicio 1.2.12
Escribir una función que lea desde el teclado las unidades y el precio que quiere comprar, y en función de las unidades introducidas le haga un descuento o no (cuando las unidades excedan media docena se aplicará 4% y el 10% cuando excedan la docena).

Accion 1.2.12 
Ambiente
    uni:entero
    costo,Resultado:real
    
    Funcion Descuento(unidades:entero, precio:real):Real
        Ambiente
            Total:Real

        Segun unidades hacer
        >6 y unidades<12 : Descuento:=unidades*precio*0,96
        >12 : Descuento:=unidades*precio*0,9
        FinSegun
        Descuento:=unidades*precio
    FinFuncion

    Escribir("Ingrese las unidades y el precio del producto a comprar")
    Leer(uni);Leer(costo)
    Resultado:=Descuento(uni,costo)
    Escribir("El precion con el descuento es de", Resultado)s

Proceso
FinProceso
FinAccion
```

## 1.11.py

```python

```

## 1.11.txt

```
    Dados dos números enteros A y B generar un algoritmo que permita determinar si A es divisor de B o B es divisor de A.

    Accion 1.11 es
        Ambiente   
            a,b:entero

        Proceso
            Escribir("Ingrese los dos numeros a dividir"); Leer(a,b)

            SI (b mod a = 0) ENTONCES
                Si (a mod b = 0) ENTONCES
                    Escribir("a es divisor de b y b es divisor de a")
                sino
                    Escribir("a es divisor de b")
                FIN_SI
            sino
                Si (a mod b = 0) ENTONCES
                    ESCRIBIR("b es divisor de a")
                sino 
                    Escribir("Ni a ni b son divisores del otro")         
                FIN_SI       
            FIN_SI

        Fin_proceso
    Fin_Accion
```

## 1.12.py

```python

```

## 1.12.txt

```
Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000, y muestre cómo está compuesto (unidades, decenas y centenas) y si es múltiplo de 3 (Recordar: todo número cuya suma de sus dígitos sea múltiplo de 3, lo es también).

Accion 1.12 es 


    Ambiente
        num,unidad,decena,centena,: Entero 
        
    Proceso
        Escribir("Ingrese un numero mayor a 100 y menor a 1000"); Leer(num) 
        
        unidad:= num mod 10 
        
        si num >100 y num <1000 


            unidad:= numero mod 10     
            numero:= numero div 10      

            digito:= numero mod 10 
            Y:= digito *10
            numero:= nuSmero div 10  

            digito:= numero mod 10 
            Z:= digito *100
            numero:= numero div 10 
            
            

            secuencia:(1234,833,203,300)

    Fin_Proceso
    
Fin_Accion

funcion NaC(x:caracter):entero
    Segun x hacer
        ="0" : Can=0
        ...
        ="9": Can=9
    fin_segun
secuencia: ("auto123")
para i=1 hasta 4 hacer
    AVANZAR(secuencia, v)
fin_para

:= NaC(v) 

("LucianoPeralta-44512762%08/11/2002 CarinaBurger-17307090%10/04/1994 CarinaBurger-17307090%10/04/1994")

mientras v <> "" entonces

mientras v <> "-"

para i=1 hasta 8 hacer



avz()
```

## 1.13.py

```python

```

## 1.13.txt

```
Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000 que representa una suma de dinero e indique cuantos billetes de cada denominación necesita, suponiendo que solo existen billetes de 100, 10 y 1 peso.

Accion 1.13 es 
    Ambiente
        num,b100,b10,b1: Entero
    Proceso
        Escribir("Ingrese un numero mayor a 100 y menor a 1000"); Leer(num)

        Si (num > 100 y num < 1000) entonces
        
            b1:= num mod 10 0
            num:= num div 10 30

            b10:= num mod 10 0
            num:= num div 10 3

            b100:= num mod 10 3

            Escribir("Se necesitan ", b1, " billettes de 1 peso, ", b10," billetes de 10 y ", b100," billetes de 100")

        Sino 
            Escribir("Error, su numero no esta entre 100 y 1000")
        Fin_si
    
    Fin_proceso

Fin_accion
```

## 1.14.py

```python

```

## 1.14.txt

```
Escriba un algoritmo que lea el monto total de una compra en un supermercado y determine el total a pagar según los siguientes criterios:
Si el monto de la compra supera los $200.000, se aplica un 15% de descuento
Luego se consulta el tipo de entrega (el usuario ingresa el número de opción):

Opción 1 → retiro en sucursal, no se suma ningún cargo adicional
Opción 2 → envío a domicilio dentro de Resistencia, se suma un 5% sobre el monto final
Opción 3 → envío a domicilio fuera de Resistencia, se suma un 10% sobre el monto final


Accion 1.14 es 

    Ambiente 
        monto: real
        opcion:entero
    proceso
        Escribir("Ingrese el monto de la compra"); Leer(monto)150     
        si (monto > 200000) entonces
            monto:= monto - monto*0.15
        fin_si 
        Escribir("Ingrese el tipo de entrega 1/2/3"); Leer(opcion)
        SEGUN opcion HACER
            2:  monto:= monto + monto*0.05 
            3:  monto:= monto + monto*0.1 
        FIN_SEGUN
        Escribir("El monto total a pagar es de: ", monto)

    fin_proceso
Fin_Accion
```

## 1.15.txt

```
Hacer un algoritmo que calcule la altura aproximada de un edificio en pies, ingresando como dato la cantidad de pisos del mismo y la altura promedio de cada piso, en metros. (1 m = 3.28 pies)
Modifique el algoritmo del punto 1. para que permita calcular la altura de 50 edificios.
Modifique el algoritmo del punto 1. para que permita calcular la altura de una cantidad indeterminada de edificios. Prevea una condición de fin.


Accion 1.15 es
    Ambiente
        pisos,opcion:entero
        metros,pies:real
    proceso

        Repetir 
            Escribir("Ingrese la altura del piso y la cantidad de pisos"); Leer(metros,pisos)
            pies:= metros*pisos*3.28
            Escribir("La altura del edificio es de: ", pies)

            Escribir("Quiere Calcular la altura de otro edificio? Escriba 0 para salir y 1 para volver a calcular"); Leer(opcion)

        Hasta que (opcion = 0)

    fin_proceso
Fin_Accion
```

## 2.1.19

```
En una Empresa Farmacéutica se posee un archivo MAE_REMEDIOS (ordenado por Clave: Farmacia + Medicamento), el que se actualiza semanalmente, a traves de la información que se encuentra cargada en un archivo de MOVIMIENTOS (ordenado por Clavem: Farmacia + Medicamento, y Cod_Mov), de la siguiente forma:

Si Clave (MAE_REMEDIOS) es menor que Clavem (MOVIMIENTOS), simplemente se transfieren los datos del Maestro a la salida y se graban.

Si Clave (MAE_REMEDIOS) es igual a Clavem (MOVIMIENTOS) y el Codmov es 1, se considera error y se lista un mensaje indicando el tipo de error; pero si el Codmov es 2, entonces es un remedio que deja de fabricarse y se transfiere el registro al archivo de Remedios vencidos (REM_VENC) ; pero si el Cod_Mov es 3, se modifica la cantidad actual con la cantidad recibida.

Si Clave (MAE_REMEDIOS) es mayor que Clavem (MOVIMIENTOS) y el Codmov es 1, se incorpora el remedio a nuestro Vademecum, considerando que la cantidad recibida configura la cantidad actual y la Fecha_Vencimiento es 30 días posterior a la fecha actual; pero si el Codmov es 2 o 3 se considera error y se deben producir los correspondientes mensajes de error.

MAE_REMEDIOS Ordenado por Farmacia y Medicamento

FarmaciaMedicamentoCant_ActualFecha_Vencimiento
MOVIMIENTOS Ordenado por Farmacia, Medicamento y Cod_Mov

FarmaciaMedicamentoCod_MovCant_Recibida
REM_VENC Ordenado por Medicamento

MedicamentoCant_Vencida

Accion 2.1.19 
Ambiente 
    rem = registro
        clave: registro
            Farmacia:AN
            Medicamento:AN
        finregistro
        Cant_Actual:N
        Fecha_Vencimiento: fecha
    finregistro

    Fech = registro
            año: N
            mes: N
            dia: N
        finregistro                                     
    
    Mov= registro
        clave: registro
            Farmacia:AN
            Medicamento:AN
        finregistro
        cod_mov:N 
        Cant_Recibida
    finregistro

    ven = registro
        Medicamento: AN
        Cant_Vencida
    finregistro

    reg_rem : rem; 
    reg_fecha: fech; 
    reg_mov: mov;
    reg_rem_ven: ven
    reg_sal: rem

    mae_remedios: archivo de rem ordenado por farmacia, Medicamento
    movimientos: archiivo de mov ordenado por farmacia, Medicamento,cod_mov
    rem_venc: archivo de ven ordenado por medicamento
    mae_sal: archivo de rem ordenado por farmaca, medicamento

    procedimiento Leer_mae()
    


Proceso
    Abrir E/S(mae_remedios); Abrir S(rem_venc) Abrir E/(movimientos)
    Crear(mae_sal)
    

    mientras mae_remedios <> HV o movimientos <> HV

        si  reg_rem.clave < reg_mov.clave hacer
            reg_sal:= reg_rem 
            grabar(mae_sal,reg_sal)
        sino
            si reg_rem.clave = reg_mov.clave hacer
                segun reg_mov.cod_mov hacer
                    =1 : escribir("error")
                    =2 : reg_rem_venc.medicamento:= reg_mov.medicamento;
                        reg_rem_venc.Cant_Vencida:= reg_mov.Cant_Recibida;
                        grabar(rem_venc,reg_rem_venc);
                    =3 : reg_sal.Cant_Actual:= reg_mov.Cant_Recibida;
                        reg_sal:= reg_rem
                        reg_sal.Cant_Actual:=reg_mov.Cant_Recibida
                        grabar(mae_sal,reg_sal)
                finsegun
            sino 
                si si reg_rem.clave >    reg_mov.clave hacer
        reg.clave:="juan"
        leer(arch,reg)
        mientras NFDA(arch)

                
        finsi 

    finmientras


segun variable hacer
```

## 2.2.18.txt

```

```
