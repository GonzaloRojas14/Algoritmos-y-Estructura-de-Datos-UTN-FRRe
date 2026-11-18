---
tipo: practica
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - ejercicios
---

# Ejercicios Brisaa

> [!abstract] Qué hay acá
> Resoluciones de **Brisa**. Pocos archivos, todos de la unidad 1.1 (secuencias).
> **4 archivos**, transcriptos íntegros desde `Practica/Ejercicios Brisaa/`.
> Los originales siguen intactos en esa carpeta; esto es una copia legible dentro de Obsidian.

---

## Índice

- [[#1.1.5]]
- [[#1.1.5.2]]
- [[#1.1.5.3.txt]]
- [[#1.1.5.4.txt]]

---

## 1.1.5

```
Escribir un programa que permita calcular el precio de un artículo para un año dado, considerando que la inflación es del 4 por 100 anual.

La fórmula del precio es: P = C * (1 + R) ^ (N - A)

C - Precio actual.
N - Año futuro.
R - Tasa de Inflación.
A - Año actual.


Accion ej_1.1.5.1 es 
    Ambiente 
    C, P: REAL
    N, A: ENTERO
    R: 0.4

    PROCESO 
    Escribir("Ingrese el precio del articulo, el año actual y el año a calcular")
    Leer(c,a,n)
    P = C * (1 + R) ^ (N - A)
    Escribir("El precio calculado en base a la inflacion es: ", P)

FIN_ACCION
```

## 1.1.5.2

```
//Las raíces de una ecuación de segundo grado ax^2+bx+c=0 son reales si y sólo si el discriminante dado por (b2−4ac) no es negativo. 
//Se desea leer el valor de los coeficientes a,b,c
//Imprimir el resultado del discriminante. Realizar prueba de escritorio.

ACCION Ej_1.1.5.2 es
     AMBIENTE
     A,B,C,disc: REAL

     PROCESO
     escribir("Ingrese los valores de A,B,C")
     leer(A,B,C)

     disc:= (b ** 2)-(4 * a * c)

     SI (disc <= 0) ENTONCES
     escribir("Las raices son reales, el discriminante es: ", disc)
     SINO 
         escribir("Las raices no son reales, el discriminante es negativo: ", disc)  
     FIN_SI
FIN_ACCION
```

## 1.1.5.3.txt

```
//Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado por la suma de los precios de costos, 
//los porcentajes de ganancia del vendedor y un 21% de IVA. 
//Supóngase una ganancia del vendedor del 12% por la PC y 7% por la impresora. 
//Se leen los costos y se imprimen el precio total de ventas.

ACCION EJ_1.1.5.3 es
    AMBIENTE
    PC, IMP, P_TOTAL: REAL
    IVA= 1.21
    por_PC= 1.12
    por_IMP= 1.07

    PROCESO
    escribir("Ingrese el valor de la PC y la impresora")
    leer(pc,imp)
    P_TOTAL:= (pc * por_pc)+(imp * por_IMP)
    P_TOTAL:=(P_TOTAL * IVA)

    escribir("El precio total es: ", P_TOTAL)
FIN_ACCION
```

## 1.1.5.4.txt

```

```
