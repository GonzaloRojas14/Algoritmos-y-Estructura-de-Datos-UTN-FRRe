

**Fecha de inicio:** 19-02-2025 - Algoritmos I
---
**Tags:** #InProgress    #Algoritmos_I #Ejercicios
---
---
## Descripción de la tarea

### **Ejercicio 1: Asignación de Alumnos a Aulas (Listas)**

Para el día del tercer parcial de Algoritmos I, se decide agrupar a los alumnos en 6 aulas. Cada aula tendrá un profesor a cargo. Se dispone de una **lista simplemente enlazada** de alumnos con los siguientes datos:

- legajo
- apellido_nombre
- comisión
- notas: Arreglo [1..5] enteros

Además, se cuenta con dos funciones:

1. `EsAlumnoLibre()`, que recibe como parámetro el legajo del alumno, y devuelve `Verdadero` o `Falso` de acuerdo a si el alumno se encuentra libre o no.
2. `AsignarAula()`, devuelve un número aleatorio entre 1 y 6.

**Se solicita**:

- Generar una **lista doblemente enlazada**, de los alumnos en condiciones de rendir (es decir, que no se encuentren libres) con la siguiente información:
    
    - cursoNro
    - cantidad
    - legajo
    
    Donde se deberá cargar un nodo por cada curso, y de forma intermedia, un nodo por cada alumno asignado a dicho curso.
    
- Los nodos de los cursos serán los nodos cabeceras, los nodos intermedios contendrán información del alumno, de tal forma que:
    
    - **Si es un nodo cabecera**:
        
        - El campo `cursoNro` será el número del curso (1..6).
        - El campo `cantidad` indicará la cantidad de alumnos asignados a dicho curso (**SE DEBERÁ ACTUALIZAR CADA VEZ QUE SE ASIGNE UN NUEVO ALUMNO**).
        - El campo `legajo` será 0.
    - **Si es un nodo intermedio**:
        
        - El campo `cursoNro` será el número del curso (1..6).
        - El campo `cantidad` será 1.
        - El campo `legajo` será el legajo del alumno correspondiente.
- En el caso de que el alumno se encuentre en condiciones de rendir, eliminarlo de la lista original.
    
- Informar además:
    
    - Promedio de alumnos por aula.
    - Aula con mayor cantidad de alumnos.


## Resolución

## Relaciones

- [[Recursividad-Introduccion-AlgoritmosI]]
