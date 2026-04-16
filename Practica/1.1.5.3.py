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