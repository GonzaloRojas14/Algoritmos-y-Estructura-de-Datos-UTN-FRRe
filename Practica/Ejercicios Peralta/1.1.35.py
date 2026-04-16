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
