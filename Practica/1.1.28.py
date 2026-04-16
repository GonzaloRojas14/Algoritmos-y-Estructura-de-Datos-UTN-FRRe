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
