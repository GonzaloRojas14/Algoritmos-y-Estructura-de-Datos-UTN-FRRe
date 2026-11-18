**Fecha de inicio:** 25-11-2024 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea
Dada la expresión de la siguiente línea, dibujar el árbol equivalente

`[ ( x - y ) * z ] / ( m + n ** p)`
## Resolución

```mehrmaid
%%{init: {'theme': 'dark'}}%% 
graph TD;
    DIVISION["$/$"] --- MULTIPLICACION["$*$"]
    DIVISION --- SUMA["$+$"]
    MULTIPLICACION --- RESTA["$-$"]
    MULTIPLICACION --- Z["z"]
    RESTA --- X["x"]
    RESTA --- Y["y"]
    SUMA --- M["m"]
    SUMA --- POTENCIA["$**$"]
    POTENCIA --- N["n"]
    POTENCIA --- P["p"]

```
## Relaciones

- [[Arboles-AlgoritmosI]]
