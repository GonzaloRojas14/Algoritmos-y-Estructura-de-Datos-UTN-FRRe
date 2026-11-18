

**Fecha de inicio:** 21-02-2025 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

### 1. Reconstrucción y propiedades de árboles (3 puntos)

Dados los siguientes recorridos de un árbol binario:

- **EN-ORDEN:** B, D, E, A, F, C, G
- **PRE-ORDEN:** A, B, D, E, C, F, G

1. **Reconstruye el árbol binario** a partir de estos recorridos (1 punto).
2. **¿Cuál es el camino de la rama más larga** en el árbol reconstruido? (½ punto)
3. **Si este árbol fuera completo, ¿cuántos nodos tendría en el nivel 5?** (½ punto). Recuerda que la fórmula para calcular el número máximo de nodos en un árbol completo es $N = 2^h - 1$.
4. Si cada nodo ocupa 256 bytes de memoria, y tienes disponibles 4MB, **¿hasta qué nivel podría llegar tu árbol?** (½ punto). Nota: 1 MB = 1024 KB, 1 KB = 1024 Bytes.

### 2. Árboles binarios de búsqueda (ABB) vs. Listas/Arrays (1 punto)

¿Por qué las búsquedas en un ABB son más rápidas que en una lista o array? Elige la respuesta correcta:

1. Los ABB siempre están equilibrados, lo que reduce la altura del árbol y, por lo tanto, el número de comparaciones necesarias.
2. **Los nodos en un ABB se organizan de forma que los nodos del subárbol izquierdo son menores que la raíz, y los del subárbol derecho son mayores**.
3. Los ABB utilizan una implementación dinámica que permite un acceso más rápido a los nodos.

### 3. Operaciones en Árboles ABB y AVL (3 puntos)

Dado el siguiente conjunto de números enteros: 5, 12, 3, 8, 15, 2, 4, 9, 18, 1, 6.

1. **Crea un árbol ABB** insertando los números en el orden dado (1 punto).
2. **¿Cuál es el padre del nodo 8? ¿Cuál es el hijo derecho del nodo 12?** (½ punto)
3. **Indica el camino que conforma la altura del nodo 1** (½ punto).
4. **Indica todas las características del árbol ABB** obtenido (½ punto).
5. Si luego ingresas los enteros 7, 13, 11, ¿**se modifican las características señaladas en el punto 4? ¿Por qué?** (½ punto)
6. **Efectúa el recorrido EN ORDEN del árbol del punto 5 y, basándote en ese recorrido, configura un árbol AVL** (½ punto). Recuerda que un árbol AVL es un árbol ABB cuyo factor de equilibrio en cada nodo es -1, 0 o +1.

### 4. Complejidad Algorítmica (2 puntos)

1. Dado el siguiente fragmento de código, calcula el orden de complejidad en el peor de los casos (1 punto):
    
    ```
    Para i = 1 hasta n hacer
        Para j = 1 hasta i hacer
            Si (i + j) mod 2 == 0 entonces
                Para k = 1 hasta n hacer
                    // Operación de costo constante
                Fin Para
            Fin Si
        Fin Para
    Fin Para
    ```
    
2. Indica si las siguientes afirmaciones son Verdaderas (V) o Falsas (F) (1 punto):
    
    - La eficiencia de un algoritmo se refiere a su capacidad para resolver un problema utilizando los recursos disponibles de manera óptima.
    - La complejidad espacial se refiere a la cantidad de tiempo que tarda un algoritmo en ejecutarse.
    - El análisis a priori de la complejidad temporal implica medir el tiempo real de ejecución en una computadora específica.
    - La notación $O(n^2)$ representa el límite inferior del tiempo de ejecución en el mejor caso.

Este modelo de examen abarca los temas de árboles binarios, ABB, AVL y complejidad algorítmica, siguiendo el estilo de preguntas del parcial de ejemplo.
## Resolución

### 1. Reconstrucción y propiedades de árboles

1. Reconstrucción de Arbol:
   ``` mermaid
	graph TD;
	A---B;A---C
	B---NULLB[NULL];B---D
	D---NULLD[NULL];D---E
	C---F;C---G
	```
2. El camino mas largo seria: A, B, D, E
3. Para calcular la cantidad de nodos del nivel 5 deberíamos usar la siguiente formula: $(2^{5}-1)-(2^{4}-1)$ lo que es igual a 16
4. Primero realizamos una conversion para saber que 4MB de memoria es igual a 4194304 Bytes  de memoria, luego usando la formula $(2^n-1)*256$ deduje que el valor mas aproximado sin ocupar mas memoria de la brindada es con 14 nodos ocupando un total de 4194048 Bytes 
### 2. Árboles binarios de búsqueda (ABB) vs. Listas/Arrays

1. La respuesta correcta es: "Los ABB siempre están equilibrados, lo que reduce la altura del árbol y, por lo tanto, el número de comparaciones necesarias."

### 3. Operaciones en Árboles ABB y AVL

1. Construcción de arbol:
   ```mermaid  
	graph TD
	5---3;5---12
	3---2;3---4
	2---1;2---NULL2[NULL]
	12---8;12---15
	8---6;8---9
	15---null15[NULL];15---18
	```
2. El padre del nodo 8 es el nodo 12 y el hijo derecho del nodo 12 es el nodo 15.
3. Camino al nodo 1: 5, 3, 2, 1
4. Características:
	1. Es un AVL(Ya que es un ABL Balanceado)
	2. Tiene 4 niveles
	3. esta incompleto 
5. No se modifican ya que el arbol sigue balanceado 
6. Recorrido EN-ORDEN: 1,2,3,4,5,6,7,8,9,11,12,13,15,18. Arbol reconstruido: Como se menciono en el punto 5, el arbol sigue balanceado luego de agregar los nodos.

### 4. Complejidad Algorítmica

1. Posee un orden de $O(n)$ 
2. Verdadero o Falso:
    - La eficiencia de un algoritmo se refiere a su capacidad para resolver un problema utilizando los recursos disponibles de manera óptima. V
    - La complejidad espacial se refiere a la cantidad de tiempo que tarda un algoritmo en ejecutarse. F
    - El análisis a priori de la complejidad temporal implica medir el tiempo real de ejecución en una computadora específica. F
    - La notación $O(n^2)$ representa el límite inferior del tiempo de ejecución en el mejor caso. F
## Relaciones
- [[Arboles-AlgoritmosI]]