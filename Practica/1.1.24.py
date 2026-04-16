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