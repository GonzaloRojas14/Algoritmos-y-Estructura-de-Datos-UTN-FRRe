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
    

