---
fuente: https://aed-frre.github.io/teoria/arreglos/
tipo: guia-catedra
bloque: Teoría
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - guia-catedra
  - teoria
---

> [!info] Guía de Trabajos Prácticos — cátedra AED UTN-FRRe
> Transcripción íntegra de [https://aed-frre.github.io/teoria/arreglos/](https://aed-frre.github.io/teoria/arreglos/), sin resumir ni alterar.
> Bajada el 24/08/2026.

---

> [!tip] Las filminas de la cátedra sobre este mismo tema
> [[4 — Arreglos]] · [[5 — Búsqueda y Ordenamiento]] · [[6 — Procesos Estadísticos]] — 81 diapositivas transcriptas, con las trazas y el pseudocódigo que en el original eran imágenes.

---
# Arreglos


## **Búsqueda**


### **Búsqueda lineal**
```
LEER(x)
PARA i:= 1 a N HACER
  SI A[i] = x ENTONCES
  Escribir ('El elemento', x, 'está en la posición', i)
  FIN SI
FIN PARA
```
### **Búsqueda lineal con centinela**
```
LEER(x)
i:=1

MIENTRAS (i < N) y A[i] <> x HACER
    i:=i+1
FIN MIENTRAS

SI A[i] = x ENTONCES
    ESCRIBIR ('El elemento', x, 'se encontró en la posición', i)
SINO
    ESCRIBIR ('No encontrado')
FIN SI
```
### **Búsqueda binaria o dicotómica**
```
LEER(x)
iz:=1
de:=N

cen:=(iz+de) DIV 2

MIENTRAS (iz < de) y (nom[cen] <> x) HACER
    SI (nom[cen] > x) ENTONCES
        de:=cen-1
    SINO
        iz:=cen+1
    FIN SI
    cen:=(iz+de) div 2;
FIN MIENTRAS

SI (nom[cen] = x) ENTONCES
    ESCRIBIR ('El elemento buscado está en la posición ',cen)
SINO
    ESCRIBIR ('El elemento buscado no está en el arreglo');
FIN SI
```
## **Ordenamiento**


### **Inserción directa**
```
// Ordena de menor a mayor

CARGAR_ARREGLO

PARA i:= 2 a n HACER
    x:=a[i]
    j:=i-1
    MIENTRAS (j > 0) y (x < a[j]) HACER
        a[j+1]:=a[j]
        j:=j-1
    FIN MIENTRAS
    a[j+1]:=x
FIN PARA
```
### **Seleccion directa**
```
// Ordena de mayor a menor

CARGAR_ARREGLO

PARA i:= 1 a n-1 HACER
    x:=a[i]
    max:=i
    PARA j:= i+1 a n HACER
        SI (x < a[j]) ENTONCES
            max:=j
            x:=a[j]
        FIN SI
    FIN PARA
    a[max]:=a[i]
    a[i]:=x
FIN PARA
```
### **Intercambio directo / Burbuja**
```
// Ordena de mayor a menor

CARGAR_ARREGLO

Bandera:= Falso

MIENTRAS No Bandera HACER
    Bandera:= Verdadero
    PARA j:=1 a n-1 HACER
        SI (a[j] < a[j+1]) ENTONCES
            x:=a[j]
            a[j]:=a[j+1]
            a[j+1]:=x
            Bandera:= Falso
        FIN SI
    FIN PARA
FIN MIENTRAS
```
