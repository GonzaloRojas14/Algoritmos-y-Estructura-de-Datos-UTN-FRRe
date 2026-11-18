**Fecha de inicio:** 25-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Para las siguientes expresiones:
- $( 5 + 7 ) / 8 – ( 6 * 7 )^2$
- $3 – 6 + 6 * ( 8 / 3 )$
- $4 / ( 8 – 6 * ( 8 + 3 ) )$

1. Grafique el árbol equivalente
2. Indique las expresiones resultantes de los recorridos EN-ORDEN, PRE-ORDEN y POST-ORDEN
3. Calcule los resultados numéricos que arroja la ejecución de cada uno de los recorridos.
## Resolución
1) 
	1) **Grafico 1:**
	```mehrmaid
	%%{init: {'theme': 'dark'}}%%
	graph TD;
	menos["$-$"]---div["$/$"];menos---pot["^"]
	div---mas["$+$"];div---8
	mas---5;mas---71[7]
	pot---mult["$*$"];pot---2
	mult---6;mult---72[7]
	```


	2) **Grafico 2:**
	```mehrmaid
	%%{init: {'theme': 'dark'}}%%
	graph TD;
	mas["+"]---menos["$-$"];mas---mult["*"]
	menos---31[3];menos---61[6]
	mult---6;mult---div["$/$"]
	div---8;div---3
	```
	
	3) **Grafico 3:**
	```mehrmaid
	%%{init: {'theme': 'dark'}}%%
	graph TD;
	div["$/$"]---4;div---menos["$-$"]
	menos---81[8];menos---mult["$*$"]
	mult---6;mult---suma["$+$"]
	suma---8;suma---3 
	```
2) **Recorridos:**
	1) **In-Order**
		1) Grafo 1: 5, + , 7, /, 8, -, 6, $*$, 7. ^, 2 = -288,125
		2) Grafo 2: 3, -, 6, +, 6, $*$, 8, /, 3 = 13
		3) Grafo 3: 4, /, 8, -, 6, $*$, 8, +, 3 = -44,5
	2) **Pre-Order:**
		1) Grafo 1: -, /, +, 5, 7, 8, ^, $*$, 6, 7, 2 = No calculable
		2) Grafo 2: +, -, 3, 6, $*$, 6, /, 8, 3 = No calculable
		3) Grafo 3: /, 4, -, 8, $*$, 6, +, 8, 3 = No calculable
	3) **Post-Order:**
		1) Grafo 1: 5, 7, +, 8, /, 6,7, $*$, 2, ^, - = No calculable
		2) Grafo 2: 3, 6, -, 6, 8, 3, /, $*$, + = No calculable
		3) Grafo 3: 4, 8, 6, 8, 3, +, $*$, -, / = No calculable
## Relaciones
- [[Grafos-Discreta]]
- [[Arboles-AlgoritmosI#Árboles de Expresión]]

