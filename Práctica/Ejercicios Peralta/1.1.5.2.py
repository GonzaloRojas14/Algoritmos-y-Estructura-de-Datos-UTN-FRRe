# Las raíces de una ecuación de segundo grado ax2+bx+c=0 son reales si y sólo si el discriminante dado por (b2−4ac) no es negativo. Se desea leer el valor de los coeficientes a, b, c e imprimir el resultado del discriminante. Realizar prueba de escritorio.


a=float(input("Ingrese el primer coeficiente: "))
b=float(input("Ingrese el segundo coeficiente: "))
c=float(input("Ingrese el tercer coeficiente: "))

print('El resultado del discriminante es: ', ((b**2)-4*a*c))