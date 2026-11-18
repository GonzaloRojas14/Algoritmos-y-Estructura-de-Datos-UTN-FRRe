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