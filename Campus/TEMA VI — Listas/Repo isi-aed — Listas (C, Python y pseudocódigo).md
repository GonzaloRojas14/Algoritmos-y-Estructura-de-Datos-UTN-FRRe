---
tipo: campus
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
tema: "TEMA VI: Listas"
fuente: Repositorio de la cátedra UTN-FRRe/isi-aed (GitHub), enlazado en el campus
tags:
  - AED
  - campus
  - listas
  - codigo
---

# Repo isi-aed — Listas

> [!abstract] Qué es esta nota
> El **código oficial de listas de la cátedra**, del repositorio [UTN-FRRe/isi-aed](https://github.com/UTN-FRRe/isi-aed) (rama `master`), que el campus enlaza como "Repo de código de AED". Descargado el **17/11/2026**: carpetas `C/Listas/` (10 programas + `readme.md`), `Python/Listas/` (los mismos 10 + `lista_enlazada.py`) y `Pseudocodigo/LISTA_CIRC`. Los archivos originales están en la carpeta `repo isi-aed/`, al lado de esta nota.
> Todo el código está transcripto **textual**, sin tocar. Lo que agrega esta nota: qué hace cada programa, cómo se corresponde con los casos de las filminas, una **traducción al pseudocódigo** de cada algoritmo (no es material de la cátedra; está probada en la extensión) y los **errores** que tiene el código.

[[TEMA VI — Listas — Índice|← Volver al TEMA VI]] · [[💻 Algoritmos — Índice|← Materia]]

Relacionadas: [[8 — Listas (Inserción y Eliminación)]] (los 4 casos de inserción y eliminación, simples y dobles) · [[3.02 — Listas Doblemente Enlazadas y Circulares]] (circulares, sin código) · [[Ejemplo — Carga ordenada de lista circular simple]] · [[3.03 — Pilas y Colas]]

---

## Resumen

Todos los programas siguen el mismo esquema: **cargan la lista desde el teclado hasta que se ingresa `-1`**, la imprimen, (en los `_DEL`) piden un valor y lo borran, la vuelven a imprimir y al final liberan la memoria. El campo de datos del nodo se llama `val` y es un entero.

| Archivo (`.c` y `.py`) | Lista | Operación | Cómo inserta / cómo elimina | Lenguaje |
|---|---|---|---|---|
| `LISTAS_SIMPLE_INS` | simple, `PRIM` | carga | **Ordenada ascendente.** Busca con `P` y `ANT` hasta `P = NIL` o `DATO >= valor`; un repetido queda antes del igual. | C, Python |
| `LISTAS_SIMPLE_DEL` | simple, `PRIM` | carga + baja | Carga igual a la anterior. Borra la **primera aparición** del valor leído: busca con `P` y `ANT` hasta `P = NIL` o `DATO = valor`. | C, Python (el `.py` **no corre**) |
| `LISTAS_DOBLE_INS` | doble, `PRIM` y `ULT` | carga | **Ordenada ascendente.** Busca sólo con `P` (el anterior es `*P.ant`). | C, Python |
| `LISTAS_DOBLE_DEL` | doble, `PRIM` y `ULT` | carga + baja | Carga igual. Baja con los 4 casos: único, primero, último, medio. | C, Python |
| `LISTAS_SIMPLE_CIRC_INS` | simple **circular**, `PRIM` (+ `ULT` local) | carga | **Ordenada ascendente.** Busca hasta parar en el **último** (`*P.prox = PRIM`) o en `DATO >= valor`; después vuelve a comparar para saber el caso. | C, Python |
| `LISTAS_SIMPLE_CIRC_DEL` | simple circular | carga + baja | Carga igual. Para borrar, primero recorre para encontrar `ULT`; busca hasta el último o `DATO = valor` y mira el último afuera del ciclo. | C, Python |
| `LISTAS_DOBLE_CIRC_INS` | doble **circular**, `PRIM` y `ULT` | carga | **Ordenada ascendente.** Busca hasta `P = ULT` o `DATO >= valor`. | C, Python |
| `LISTAS_DOBLE_CIRC_DEL` | doble circular | carga + baja | Carga igual. La búsqueda corta en `P = NIL`, que en una circular **nunca pasa** (ver errores). | C, Python |
| `LISTAS_PILA` | pila (simple) | carga (apilar) | Siempre **adelante**: `PRIM` es el tope. Queda en orden inverso al de carga. No hay desapilar. | C, Python |
| `LISTAS_COLA` | cola (simple + `ULT`) | carga (encolar) | Siempre **al final**, con `ULT`. Queda en el orden de carga. No hay desencolar. | C, Python |
| `lista_enlazada.py` | simple, con clases | insertar al final / al inicio, eliminar, mostrar | **Sin orden.** Insertar al final recorre hasta el último (no guarda `ULT`). | sólo Python |
| `Pseudocodigo/LISTA_CIRC` | simple circular | recorrido | Escribe todos los nodos. | pseudocódigo |
| `C/Listas/readme.md` | — | — | Una sola línea. | — |

> [!bug] Errores que tiene el código del repo (detalle en cada sección)
> | Archivo | Qué falla |
> |---|---|
> | `LISTAS_SIMPLE_CIRC_INS.c` y `LISTAS_SIMPLE_CIRC_DEL.c` | `libera_lista` no contempla la lista vacía: si se ingresa `-1` de entrada, o si se borra el único nodo, accede a `NULL->prox` y el programa se cae. |
> | `LISTAS_DOBLE_CIRC_DEL.c` y `.py` | La búsqueda corta en `p != NULL`: si el valor **no está**, el ciclo da vueltas para siempre. |
> | `LISTAS_DOBLE_CIRC_DEL.c` | El CASO 4 (borrar el último) **nunca se ejecuta**: el borrado cae en el CASO 3, que enlaza bien pero deja `ult` apuntando al nodo liberado, y la impresión siguiente no termina. Además, adentro del CASO 4 dice `prim->prox` donde va `prim->ant`. (El `.py` lo tiene bien.) |
> | `LISTAS_SIMPLE_DEL.py` | Un `try:` sin `except` (línea 9): Python da `SyntaxError` y el programa no arranca. |
> | `Pseudocodigo/LISTA_CIRC` | No pregunta si `PRIM = NIL`: con la lista vacía accede a `*P.prox` sobre `NIL`. |

### Cómo leer el C en pseudocódigo

| C (o Python) | Pseudocódigo de cátedra |
|---|---|
| `nodo_t *p` | `P: Puntero a NODO` |
| `NULL` (Python: `None`) | `NIL` |
| `q = (nodo_t *) malloc(sizeof(nodo_t));` (Python: `q = Nodo(valor)`) | `NUEVO(Q)` |
| `free(p);` (Python: nada, libera solo) | `DISPONER(P)` |
| `p->val` | `*P.DATO` (en el repo el campo se llama `val`) |
| `p->prox` | `*P.prox` |
| `p->ant->prox = q;` | `*(*P.ant).prox := Q` (el mismo comentario lo dice en `LISTAS_DOBLE_INS.c`) |
| `=` · `==` · `!=` · `&&` | `:=` · `=` · `<>` · `Y` |
| `while (1) { scanf(...); if (valor == -1) break; … }` | `LEER(valor); MIENTRAS valor <> -1 HACER … LEER(valor); FIN_MIENTRAS` |
| `nodo_pu` (registro con `pr` y `ul`) | En C una función devuelve **un solo** valor; para devolver `PRIM` y `ULT` juntos los meten en un registro. En pseudocódigo serían los dos parámetros de la acción. En Python devuelven una tupla `prim, ult`. |

El `&&` de C no evalúa la segunda parte si la primera ya es falsa: por eso `p != NULL && p->val < valor` no se cae cuando `p` llega a `NULL`. Es lo mismo que la filmina escribe como `(P <> NIL) Y (*P.DATO < *Q.DATO)`, y la extensión lo evalúa igual.

> [!note] Sobre las traducciones de esta nota
> Cada traducción reproduce **lo que hace el código**, con sus nombres (`PRIM`, `ULT`, `P`, `Q`, `ANT`, `valor`) y sus casos, aunque tenga errores. Los `SINO SI` de la filmina se escriben acá como `SI` anidados, cada uno con su `FIN_SI`, porque así los pide la extensión. Todas se corrieron en la extensión de pseudocódigo: ver [[#Verificación de las traducciones|§ Verificación]].

---

## 1 · Lista simple — inserción ordenada (`LISTAS_SIMPLE_INS`)

**Qué hace.** Lee enteros hasta `-1` y los va insertando **en orden ascendente** en una lista simple con un solo puntero externo, `prim`. Es exactamente el algoritmo de inserción de la [[8 — Listas (Inserción y Eliminación)|filmina 8]] (diapositivas 13 a 16):

- **Búsqueda del lugar:** `p = prim, ant = NULL` y `while (p != NULL && p->val < valor)` avanza `ant = p; p = p->prox`. Corta cuando `P` llega a `NIL` (el valor es mayor que todos) o cuando encuentra el primer nodo con `DATO >= valor`. Un valor repetido queda **antes** del igual (la misma observación que hace la filmina en la diapositiva 9).
- **CASO 1 (lista vacía),** `prim == NULL`: `prim = q; q->prox = NULL`.
- **CASO 2 (antes del primero),** `p == prim`: `prim = q`.
- **CASOS 3 y 4 (medio y final) juntos:** `ant->prox = q`. En los dos casos se termina con `q->prox = p`; en el CASO 4 `p` vale `NULL`, así que el nuevo queda último. La filmina los escribe en ramas separadas; acá se aprovecha que `*Q.prox := P` con `P = NIL` es lo mismo que `*Q.prox := NIL` (la nota de la filmina 8 ya marca que se podían fusionar).

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> ```
> { Traducción de LISTAS_SIMPLE_INS.c (repo isi-aed): carga ordenada ascendente, corta con -1 }
> ACCION SIMPLE_INS ES
> AMBIENTE
>     NODO = REGISTRO
>         DATO: entero;
>         prox: Puntero a NODO;
>     FIN_REGISTRO;
>     PRIM, P, Q, ANT: Puntero a NODO;
>     valor: entero;
> PROCESO
>     PRIM := NIL;
>     LEER(valor);
>     MIENTRAS valor <> -1 HACER
>         NUEVO(Q);
>         *Q.DATO := valor;
>         SI PRIM = NIL ENTONCES                  { CASO 1: lista vacía }
>             PRIM := Q;
>             *Q.prox := NIL;
>         SINO
>             P := PRIM;  ANT := NIL;
>             MIENTRAS (P <> NIL) Y (*P.DATO < valor) HACER
>                 ANT := P;
>                 P := *P.prox;
>             FIN_MIENTRAS;
>             SI P = PRIM ENTONCES                { CASO 2: antes del primero }
>                 PRIM := Q;
>             SINO                                { CASOS 3 y 4: medio o final }
>                 *ANT.prox := Q;
>             FIN_SI;
>             *Q.prox := P;                       { en el CASO 4, P = NIL }
>         FIN_SI;
>         LEER(valor);
>     FIN_MIENTRAS;
>     { imprime_lista }
>     ESCRIBIR("CONTENIDO DE LA LISTA");
>     P := PRIM;
>     MIENTRAS P <> NIL HACER
>         ESCRIBIR("Valor: ", *P.DATO);
>         P := *P.prox;
>     FIN_MIENTRAS;
> FIN_ACCION
> ```

### Código C — `C/Listas/LISTAS_SIMPLE_INS.c`

```c
//Programa que crea una COLA, utilizando una lista enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox;
} nodo_t;

nodo_t *crea_lista(nodo_t *prim){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL, *ant = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        //Caso 1
        if (prim == NULL){
            
            prim = q;   
            q->prox = NULL;    

                
        }

        else {

            //Busco el lugar para insercion
            p = prim, ant = NULL;            
            while (p != NULL && p->val < valor){

                ant = p;
                p = p->prox;

            }

            //Caso 2
            if (p == prim){
                
                prim = q;
                
            }
            else { //Casos 3 y 4
                
                ant->prox = q;
            }

            q->prox = p;
        
        }
        
    }
    
    return prim;
}

void imprime_lista(nodo_t *prim) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    while (p != NULL) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->prox;
    }
}

void libera_lista(nodo_t *prim) {
    nodo_t  *p = prim, 
            *prox = prim;

    while (p) {
        prox = p->prox;
        free(p);
        p = prox;
    }
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    prim = crea_lista(prim);

    //printf("Valor de PRIM luego de cargar ... %p\n", prim);

    //Muestro la lista creada
    imprime_lista(prim);
    
    //Libero recursos
    libera_lista(prim);

    return 0;
}
```

> [!note] Ojo con el comentario de la línea 1
> Dice "Programa que crea una COLA": está copiado de `LISTAS_COLA.c`. El programa crea una lista **ordenada**, no una cola. Lo mismo pasa en `LISTAS_SIMPLE_DEL.c`.

> [!example]- Versión Python — `Python/Listas/LISTAS_SIMPLE_INS.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>
> def crea_lista():
>     prim = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             q.prox = None
>         else:
>             p = prim
>             ant = None
>             while p is not None and p.val < valor:
>                 ant = p
>                 p = p.prox
>             if p == prim:
>                 prim = q
>             else:
>                 ant.prox = q
>             q.prox = p
>     return prim
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     p = prim
>     while p:
>         print(f"Valor: {p.val}")
>         print(f"Dirección (id) del nodo: {(p)}")
>         print(f"Dirección (id) del prox: {(p.prox)}")
>         p = p.prox
>
> def libera_lista(prim):
>     p = prim
>     while p:
>         prox = p.prox
>         p = prox
>
> def main():
>     prim = crea_lista()
>     imprime_lista(prim)
>     libera_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo. Diferencias: si se escribe algo que no es un número, lo saltea (`except ValueError: continue`); `imprime_lista` muestra además el nodo y su `prox` (como objetos, no con `id()` aunque el texto diga "id"), y `libera_lista` sólo recorre: en Python la memoria la libera el recolector.

---

## 2 · Lista simple — eliminación (`LISTAS_SIMPLE_DEL`)

**Qué hace.** Carga la lista ordenada con el **mismo** `crea_lista` de `LISTAS_SIMPLE_INS` (el código está repetido), la imprime, pide **un** valor, lo borra y la vuelve a imprimir. `borra_lista` es el algoritmo de eliminación de la filmina 8 (diapositivas 39 a 42), casi línea por línea:

- **Lista vacía:** escribe `ERROR - LISTA VACIA!!!!` y no pide el valor.
- **Búsqueda:** `while (p != NULL && p->val != valor)` con `P` y `ANT`. Corta en `NIL` (no está) o en el primer nodo igual al valor: si hay repetidos, borra **sólo el primero**. No aprovecha que la lista está ordenada (la filmina tampoco).
- **No está** (`p == NULL`): escribe `SIN EXITO ..`.
- **CASOS 1 y 2 (único o primero),** `p == prim`: `prim = p->prox` (si era el único, `p->prox` es `NULL` y la lista queda vacía).
- **CASOS 3 y 4 (medio o último):** `ant->prox = p->prox` (si era el último, `p->prox` es `NULL`).
- Siempre termina con `free(p)`, el `DISPONER(P)`.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> La carga es la misma de la sección 1. Esto es `borra_lista`:
> ```
>     { borra_lista }
>     SI PRIM = NIL ENTONCES
>         ESCRIBIR("ERROR - LISTA VACIA!!!!");
>     SINO
>         LEER(valor);
>         P := PRIM;  ANT := NIL;
>         MIENTRAS (P <> NIL) Y (*P.DATO <> valor) HACER
>             ANT := P;
>             P := *P.prox;
>         FIN_MIENTRAS;
>         SI P = NIL ENTONCES
>             ESCRIBIR("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.");
>         SINO
>             SI P = PRIM ENTONCES                { CASOS 1 y 2: único o primero }
>                 PRIM := *P.prox;
>             SINO                                { CASOS 3 y 4: medio o último }
>                 *ANT.prox := *P.prox;
>             FIN_SI;
>             DISPONER(P);
>         FIN_SI;
>     FIN_SI;
> ```

### Código C — `C/Listas/LISTAS_SIMPLE_DEL.c`

```c
//Programa que crea una COLA, utilizando una lista enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox;
} nodo_t;

nodo_t *crea_lista(nodo_t *prim){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL, *ant = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        if (prim == NULL){
            
            prim = q;   
            q->prox = NULL;    

                
        }

        else {

            //Busco el lugar para insercion
            p = prim, ant = NULL;            
            while (p != NULL && p->val < valor){

                ant = p;
                p = p->prox;

            }

            //Casos 1 y 2
            if (p == prim){
                
                prim = q;
                
            }
            else { //Casos 3 y 4
                
                ant->prox = q;
            }

            q->prox = p;
        
        }
        
    }
    
    return prim;
}

void imprime_lista(nodo_t *prim) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    while (p != NULL) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->prox;
    }
}

nodo_t *borra_lista(nodo_t *prim) {
    nodo_t  *ant = prim, 
            *p = prim;

    int valor;

    //Si es el pirmer nodo cargo al inicio, sino al final
    if (prim == NULL){
        printf("ERROR - LISTA VACIA!!!!");    
    }
    else
    {
        printf("Ingrese valor a eliminar:");
        scanf("%d", &valor);  

        //Busco el lugar para insercion
        p = prim, ant = NULL;            
        while (p != NULL && p->val != valor){

            ant = p;
            p = p->prox;

        }

        if (p == NULL){
            printf("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.\n");    
        }
        else
        {
            //Casos 1 y 2
            if (p == prim){
                
                prim = p->prox;
                
            }
            else { //Casos 3 y 4
                
                ant->prox = p->prox;
            }

            free(p);            
        }

    }

    return prim;
}

void libera_lista(nodo_t *prim) {
    nodo_t  *p = prim, 
            *prox = prim;

    while (p) {
        prox = p->prox;
        free(p);
        p = prox;
    }
}

int main(void) {        
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    prim = crea_lista(prim);
    
    //printf("Valor de PRIM luego de cargar ... %p\n", prim);

    //lista recien cargada
    imprime_lista(prim);
    
    //elimino selectivamente
    prim = borra_lista(prim);

    //Veo como queda con el nodo eliminado
    imprime_lista(prim);

    //Libero recursos
    libera_lista(prim);

    return 0;
}
```

> [!example]- Versión Python — `Python/Listas/LISTAS_SIMPLE_DEL.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>
> def crea_lista():
>     prim = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             q.prox = None
>         else:
>             p = prim
>             ant = None
>             while p is not None and p.val < valor:
>                 ant = p
>                 p = p.prox
>             if p == prim:
>                 prim = q
>             else:
>                 ant.prox = q
>             q.prox = p
>     return prim
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     p = prim
>     while p:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>
> def borra_lista(prim):
>     if prim is None:
>         print("ERROR - LISTA VACIA!!!!")
>         return prim
>     valor = int(input("Ingrese valor a eliminar:"))
>     p = prim
>     ant = None
>     while p is not None and p.val != valor:
>         ant = p
>         p = p.prox
>     if p is None:
>         print("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.")
>         return prim
>     if p == prim:
>         prim = p.prox
>     else:
>         ant.prox = p.prox
>     return prim
>
> def libera_lista(prim):
>     p = prim
>     while p:
>         prox = p.prox
>         p = prox
>
> def main():
>     prim = crea_lista()
>     imprime_lista(prim)
>     prim = borra_lista(prim)
>     imprime_lista(prim)
>     libera_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```

> [!bug] Error en el código del repo — `LISTAS_SIMPLE_DEL.py` no arranca
> En `crea_lista` (líneas 9 a 10) hay un `try:` **sin** su `except`: en los otros `.py` sigue `except ValueError: continue`, acá falta. Un `try` sin `except` ni `finally` es un error de sintaxis, así que Python rechaza el archivo entero (`SyntaxError`) antes de ejecutar nada. Por lo demás, el algoritmo es el mismo que el C: `borra_lista` devuelve `prim` y no libera el nodo (lo hace el recolector).

---

## 3 · Lista doble — inserción ordenada (`LISTAS_DOBLE_INS`)

**Qué hace.** Igual que la sección 1 pero con una **lista doble**: cada nodo tiene `prox` y `ant`, y hay dos punteros externos, `prim` y `ult`. Es el algoritmo de las diapositivas 26 a 29 de la filmina 8:

- **Búsqueda:** sólo con `P` (`while (p != NULL && p->val < valor) p = p->prox`). No hace falta `ANT` porque el anterior es `*P.ant`.
- **CASO 1 (vacía):** `prim` y `ult` apuntan al nuevo; `prox` y `ant` en `NULL`.
- **CASO 2 (antes del primero),** `p == prim`: `*Q.prox := P; *P.ant := Q; *Q.ant := NIL; PRIM := Q`.
- **CASO 4 (después del último),** `p == NULL`: `*ULT.prox := Q; *Q.ant := ULT; *Q.prox := NIL; ULT := Q`.
- **CASO 3 (medio):** los cuatro enganches, con `*(*P.ant).prox := Q` (`p->ant->prox = q`, el comentario del código lo escribe en pseudocódigo).
- `crea_lista` devuelve `prim` y `ult` dentro de un registro `nodo_pu`. Imprime la lista hacia adelante (desde `prim` por `prox`) y **hacia atrás** (desde `ult` por `ant`), que es la forma de comprobar que los `ant` quedaron bien.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> ```
> { Traducción de LISTAS_DOBLE_INS.c: lista doble, carga ordenada ascendente, corta con -1 }
> ACCION DOBLE_INS ES
> AMBIENTE
>     NODO = REGISTRO
>         DATO: entero;
>         prox, ant: Puntero a NODO;
>     FIN_REGISTRO;
>     PRIM, ULT, P, Q: Puntero a NODO;
>     valor: entero;
> PROCESO
>     PRIM := NIL;  ULT := NIL;
>     LEER(valor);
>     MIENTRAS valor <> -1 HACER
>         NUEVO(Q);
>         *Q.DATO := valor;
>         SI PRIM = NIL ENTONCES                  { CASO 1: lista vacía }
>             PRIM := Q;  ULT := Q;
>             *Q.prox := NIL;  *Q.ant := NIL;
>         SINO
>             P := PRIM;
>             MIENTRAS (P <> NIL) Y (*P.DATO < valor) HACER
>                 P := *P.prox;
>             FIN_MIENTRAS;
>             SI P = PRIM ENTONCES                { CASO 2: antes del primero }
>                 *Q.prox := P;  *P.ant := Q;
>                 *Q.ant := NIL;  PRIM := Q;
>             SINO
>                 SI P = NIL ENTONCES             { CASO 4: después del último }
>                     *ULT.prox := Q;  *Q.ant := ULT;
>                     *Q.prox := NIL;  ULT := Q;
>                 SINO                            { CASO 3: en el medio }
>                     *Q.ant := *P.ant;
>                     *Q.prox := P;
>                     *(*P.ant).prox := Q;
>                     *P.ant := Q;
>                 FIN_SI;
>             FIN_SI;
>         FIN_SI;
>         LEER(valor);
>     FIN_MIENTRAS;
>     ESCRIBIR("CONTENIDO DE LA LISTA");
>     P := PRIM;
>     MIENTRAS P <> NIL HACER
>         ESCRIBIR("Valor: ", *P.DATO);
>         P := *P.prox;
>     FIN_MIENTRAS;
>     ESCRIBIR("CONTENIDO DE LA LISTA -- REVERSA");
>     P := ULT;
>     MIENTRAS P <> NIL HACER
>         ESCRIBIR("Valor: ", *P.DATO);
>         P := *P.ant;
>     FIN_MIENTRAS;
> FIN_ACCION
> ```

### Código C — `C/Listas/LISTAS_DOBLE_INS.c`

```c
//Programa que crea nodos en una LISTA DOBLE enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox, *ant;
} nodo_t;

typedef struct prim_ult {    
    struct nodo *pr, *ul;
} nodo_pu;

nodo_pu *crea_lista(nodo_t *prim, nodo_t *ult){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL;
    nodo_pu *sal = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        //Caso 1
        if (prim == NULL){
            
            prim = q;   
            ult = q;   
            q->prox = NULL;    
            q->ant = NULL;    
                
        }

        else {

            //Busco el lugar para insercion
            p = prim;            
            while (p != NULL && p->val < valor){
                
                p = p->prox;

            }

            //Caso 2 -- ANTES del PRIMERO
            if (p == prim){
                            
                q->prox = p;
                p->ant = q;
                q->ant = NULL;
                prim = q;
                
            }
            else if (p == NULL) { //Caso 4 -- DESPUES DEL ULTIMO
                
                ult->prox = q;
                q->ant = ult;
                q->prox = NULL;
                ult = q;

            }
                else { //Caso 3 -- MEDIO

                    q->ant = p->ant;
                    q->prox = p;
                    p->ant->prox = q; // *(*p.ant).prox
                    p->ant = q;

                }
        
        }
        
    }

    //printf("Direccion de prim %p \t Direccion de ULT %p \n", prim, ult);

    //Genero el registro de salida con los punteros extremos
    //solicito memoria para el nodo
    sal = (nodo_pu *) malloc(sizeof(nodo_pu));

    sal->pr = prim;
    sal->ul = ult;

    return sal;
}

void imprime_lista(nodo_t *prim) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    //printf("PRIM: %p \n", p);

    while (p != NULL) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Dir del NODO %p \t Dir del PROX %p \t Dir del ANT %p \n", p->val, p, p->prox, p->ant);
        p = p->prox;
    }
}

void imprime_lista_reversa(nodo_t *ult) {
    nodo_t *p = ult;

    printf("CONTENIDO DE LA LISTA -- REVERSA \n");

    //printf("ULT: %p \n", p);

    while (p != NULL) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Dir del NODO %p \t Dir del PROX %p \t Dir del ANT %p \n", p->val, p, p->prox, p->ant);
        p = p->ant;
    }
}

void libera_lista(nodo_t *prim) {
    nodo_t  *p = prim, 
            *prox = prim;

    while (p) {
        prox = p->prox;
        free(p);
        p = prox;
    }
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL, *ult = NULL;
    nodo_pu *rec = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    rec = crea_lista(prim, ult);

    //printf("Valor de PRIM luego de cargar ... %p\n", rec->pr);
    //printf("Valor de ULT luego de cargar ... %p\n", rec->ul);

    //Asigno los valores generados
    prim = rec->pr;
    ult = rec->ul;

    //Muestro la lista creada
    imprime_lista(prim);

    //Muestro la lista creada
    imprime_lista_reversa(ult);
    
    //Libero recursos
    libera_lista(prim);

    return 0;
}
```

> [!example]- Versión Python — `Python/Listas/LISTAS_DOBLE_INS.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>         self.ant = None
>
> def crea_lista():
>     prim = None
>     ult = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             ult = q
>             q.prox = None
>             q.ant = None
>         else:
>             p = prim
>             while p is not None and p.val < valor:
>                 p = p.prox
>             if p == prim:
>                 q.prox = p
>                 p.ant = q
>                 q.ant = None
>                 prim = q
>             elif p is None:
>                 ult.prox = q
>                 q.ant = ult
>                 q.prox = None
>                 ult = q
>             else:
>                 q.ant = p.ant
>                 q.prox = p
>                 p.ant.prox = q
>                 p.ant = q
>     return prim, ult
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     p = prim
>     while p:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>
> def imprime_lista_reversa(ult):
>     print("CONTENIDO DE LA LISTA -- REVERSA")
>     p = ult
>     while p:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.ant
>
> def libera_lista(prim):
>     p = prim
>     while p:
>         prox = p.prox
>         p = prox
>
> def main():
>     prim, ult = crea_lista()
>     imprime_lista(prim)
>     imprime_lista_reversa(ult)
>     libera_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo; `crea_lista` devuelve la tupla `prim, ult` en lugar del registro `nodo_pu`.

---

## 4 · Lista doble — eliminación (`LISTAS_DOBLE_DEL`)

**Qué hace.** Carga como la sección 3 y borra un valor. `borra_lista` es el de las diapositivas 50 y 51 de la filmina 8:

- **Búsqueda:** sólo con `P`, `while (p != NULL && p->val != valor)`.
- **CASO 1 (único nodo),** `prim == ult`: `PRIM := NIL; ULT := NIL`.
- **CASO 2 (el primero),** `p == prim`: `*(*P.prox).ant := NIL; PRIM := *P.prox` (la filmina hace primero `PRIM := *P.prox` y después `*PRIM.ant := NIL`: es lo mismo).
- **CASO 4 (el último),** `p == ult`: `*(*P.ant).prox := NIL; ULT := *P.ant`.
- **CASO 3 (medio):** `*(*P.prox).ant := *P.ant; *(*P.ant).prox := *P.prox`.
- Devuelve `prim` y `ult` en un `nodo_pu`, e imprime hacia adelante y hacia atrás.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> La carga es la misma de la sección 3. Esto es `borra_lista`:
> ```
>     { borra_lista }
>     SI PRIM = NIL ENTONCES
>         ESCRIBIR("ERROR - LISTA VACIA!!!!");
>     SINO
>         LEER(valor);
>         P := PRIM;
>         MIENTRAS (P <> NIL) Y (*P.DATO <> valor) HACER
>             P := *P.prox;
>         FIN_MIENTRAS;
>         SI P = NIL ENTONCES
>             ESCRIBIR("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.");
>         SINO
>             SI PRIM = ULT ENTONCES              { CASO 1: único nodo }
>                 PRIM := NIL;  ULT := NIL;
>             SINO
>                 SI P = PRIM ENTONCES            { CASO 2: el primero }
>                     *(*P.prox).ant := NIL;
>                     PRIM := *P.prox;
>                 SINO
>                     SI P = ULT ENTONCES         { CASO 4: el último }
>                         *(*P.ant).prox := NIL;
>                         ULT := *P.ant;
>                     SINO                        { CASO 3: en el medio }
>                         *(*P.prox).ant := *P.ant;
>                         *(*P.ant).prox := *P.prox;
>                     FIN_SI;
>                 FIN_SI;
>             FIN_SI;
>             DISPONER(P);
>         FIN_SI;
>     FIN_SI;
> ```

### Código C — `C/Listas/LISTAS_DOBLE_DEL.c`

```c
//Programa que crea nodos en una LISTA DOBLE enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox, *ant;
} nodo_t;

typedef struct prim_ult {    
    struct nodo *pr, *ul;
} nodo_pu;

nodo_pu *crea_lista(nodo_t *prim, nodo_t *ult){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL;
    nodo_pu *sal = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        //Caso 1
        if (prim == NULL){
            
            prim = q;   
            ult = q;   
            q->prox = NULL;    
            q->ant = NULL;    
                
        }

        else {

            //Busco el lugar para insercion
            p = prim;            
            while (p != NULL && p->val < valor){
                
                p = p->prox;

            }

            //Caso 2 -- ANTES del PRIMERO
            if (p == prim){
                            
                q->prox = p;
                p->ant = q;
                q->ant = NULL;
                prim = q;
                
            }
            else if (p == NULL) { //Caso 4 -- DESPUES DEL ULTIMO
                
                ult->prox = q;
                q->ant = ult;
                q->prox = NULL;
                ult = q;

            }
            else { //Caso 3 -- MEDIO

                q->ant = p->ant;
                q->prox = p;
                p->ant->prox = q;
                p->ant = q;

            }
        
        }
        
    }

    //printf("Direccion de prim %p \t Direccion de ULT %p \n", prim, ult);

    //Genero el registro de salida con los punteros extremos
    //solicito memoria para el nodo
    sal = (nodo_pu *) malloc(sizeof(nodo_pu));

    sal->pr = prim;
    sal->ul = ult;

    return sal;
}

void imprime_lista(nodo_t *prim) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    while (p != NULL) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->prox;
    }
}

void imprime_lista_reversa(nodo_t *ult) {
    nodo_t *p = ult;

    printf("CONTENIDO DE LA LISTA -- REVERSA \n");

    while (p != NULL) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->ant;
    }
}

nodo_pu *borra_lista(nodo_t *prim, nodo_t *ult) {
    nodo_t  *p = prim;
    nodo_pu *sal = NULL;

    int valor;

    //Si es el pirmer nodo cargo al inicio, sino al final
    if (prim == NULL){
        printf("ERROR - LISTA VACIA!!!!");    
    }
    else
    {
        printf("Ingrese valor a eliminar:");
        scanf("%d", &valor);  

        //Busco el valor a eliminar
        p = prim;            
        while (p != NULL && p->val != valor){
            
            p = p->prox;

        }

        if (p == NULL){
            printf("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.\n");    
        }
        else
        {            
            if (prim == ult) { //Caso 1 -- UNICO NODO

                prim = NULL;
                ult = NULL;

            }            
            else if (p == prim){ //Caso 2
                                                
                p->prox->ant = NULL; //*prim.ant := nil
                prim = p->prox;
                
            }
            else if (p == ult) { //Caso 4
                
                p->ant->prox = NULL; //*ult.prox := nil
                ult = p->ant;

            }
            else { //Caso 3

                p->prox->ant = p->ant;
                p->ant->prox = p->prox;

            }

            free(p);            
        }

    }

    //Genero el registro de salida con los punteros extremos
    //solicito memoria para el nodo
    sal = (nodo_pu *) malloc(sizeof(nodo_pu));

    sal->pr = prim;
    sal->ul = ult;

    return sal;
}

void libera_lista(nodo_t *prim) {
    nodo_t  *p = prim, 
            *prox = prim;

    while (p) {
        prox = p->prox;
        free(p);
        p = prox;
    }
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL, *ult = NULL;
    nodo_pu *rec = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    rec = crea_lista(prim, ult);

    //printf("Valor de PRIM luego de cargar ... %p\n", rec->pr);
    //printf("Valor de ULT luego de cargar ... %p\n", rec->ul);

    //Asigno los valores generados
    prim = rec->pr;
    ult = rec->ul;

    //Muestro la lista creada
    imprime_lista(prim);

    //elimino selectivamente
    rec = borra_lista(prim, ult);

    //Asigno los valores generados
    prim = rec->pr;
    ult = rec->ul;

    //Veo como queda con el nodo eliminado
    imprime_lista(prim);
    
    //Para mostrar como queda en reversa luego de eliminar
    imprime_lista_reversa(ult);

    //Libero recursos
    libera_lista(prim);

    return 0;
}
```

> [!example]- Versión Python — `Python/Listas/LISTAS_DOBLE_DEL.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>         self.ant = None
>
> def crea_lista():
>     prim = None
>     ult = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             ult = q
>             q.prox = None
>             q.ant = None
>         else:
>             p = prim
>             while p is not None and p.val < valor:
>                 p = p.prox
>             if p == prim:
>                 q.prox = p
>                 p.ant = q
>                 q.ant = None
>                 prim = q
>             elif p is None:
>                 ult.prox = q
>                 q.ant = ult
>                 q.prox = None
>                 ult = q
>             else:
>                 q.ant = p.ant
>                 q.prox = p
>                 p.ant.prox = q
>                 p.ant = q
>     return prim, ult
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     p = prim
>     while p:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>
> def imprime_lista_reversa(ult):
>     print("CONTENIDO DE LA LISTA -- REVERSA")
>     p = ult
>     while p:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.ant
>
> def borra_lista(prim, ult):
>     if prim is None:
>         print("ERROR - LISTA VACIA!!!!")
>         return prim, ult
>     try:
>         valor = int(input("Ingrese valor a eliminar:"))
>     except ValueError:
>         return prim, ult
>     p = prim
>     while p is not None and p.val != valor:
>         p = p.prox
>     if p is None:
>         print("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.")
>         return prim, ult
>     if prim == ult:
>         prim = None
>         ult = None
>     elif p == prim:
>         prim = p.prox
>         if prim:
>             prim.ant = None
>     elif p == ult:
>         ult = p.ant
>         if ult:
>             ult.prox = None
>     else:
>         p.ant.prox = p.prox
>         p.prox.ant = p.ant
>     return prim, ult
>
> def libera_lista(prim):
>     p = prim
>     while p:
>         prox = p.prox
>         p = prox
>
> def main():
>     prim, ult = crea_lista()
>     imprime_lista(prim)
>     prim, ult = borra_lista(prim, ult)
>     imprime_lista(prim)
>     imprime_lista_reversa(ult)
>     libera_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo, con el orden de las asignaciones de la filmina (`prim = p.prox` y después `prim.ant = None`) y unos `if prim:` / `if ult:` de más, que nunca son falsos porque el caso de un solo nodo ya se separó antes.

---

## 5 · Lista simple circular — inserción ordenada (`LISTAS_SIMPLE_CIRC_INS`)

**Qué hace.** Carga una lista **simple circular** (el último nodo apunta al primero, no a `NIL`) **ordenada en forma ascendente**. Es el aporte más útil del repo: la cátedra no tiene una presentación de circulares en pseudocódigo con inserción ordenada. La [[3.02 — Listas Doblemente Enlazadas y Circulares|presentación 3.02]] sólo describe las etapas en texto, el `LISTA_CIRCULAR` de los Complementos de la guía inserta siempre en el 2º lugar (sin orden), y el [[Ejemplo — Carga ordenada de lista circular simple|ejemplo del campus]] que sí ordena tiene errores.

Cómo lo resuelve:

- **Punteros:** `prim` (el que devuelve), y adentro de `crea_lista` un `ult` **local** que se va actualizando, porque al insertar antes del primero hay que re-enganchar al último. `crea_lista` no lo devuelve: por eso `LISTAS_SIMPLE_CIRC_DEL` lo vuelve a buscar.
- **CASO 1 (vacía):** `prim = q; ult = q; q->prox = prim`: el único nodo **se apunta a sí mismo**.
- **Búsqueda:** `p = prim, ant = NULL; while (p->prox != prim && p->val < valor)` avanza `ant = p; p = p->prox`. La condición de corte cambia respecto de la lineal: como nunca hay `NIL`, se para **en el último** (`*P.prox = PRIM`), no después. El ciclo puede cortar por dos motivos (llegó al último, o encontró un `DATO >= valor`) y el último nodo nunca se compara dentro del ciclo: por eso, después, **cada caso vuelve a preguntar por el valor**.
- **CASO 2 (antes del primero),** `p == prim && p->val >= valor`: `*Q.prox := PRIM; PRIM := Q; *ULT.prox := Q`. El tercer enganche es el propio de la circular: el último tiene que apuntar al **nuevo** primero.
- **CASO 4 (después del último),** `p->prox == prim && p->val < valor`: `*P.prox := Q; *Q.prox := PRIM; ULT := Q`. El nuevo último cierra el círculo apuntando a `PRIM`.
- **CASO 3 (medio),** todo lo demás: `*ANT.prox := Q; *Q.prox := P` (antes de `P`). Incluye insertar antes del último cuando el último es `>=` al valor. `ANT` nunca es `NIL` acá: si `P` quedó en `PRIM`, es porque el valor es `<=` al primero (CASO 2) o porque hay un solo nodo menor (CASO 4).
- **Recorrido** (`imprime_lista`): `while (p->prox != prim)` escribe y avanza, y el último se escribe **afuera** del ciclo. Es el mismo recorrido de `Pseudocodigo/LISTA_CIRC` (sección 11), con la diferencia de que acá sí se pregunta antes si la lista está vacía.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> El programa completo que se corrió. Las líneas `[verif]` no están en el C: comprueban que el último apunte a `PRIM`. La liberación del final está tal cual el C, para mostrar el error de abajo.
> ```
> { Traducción de LISTAS_SIMPLE_CIRC_INS.c: lista simple circular ordenada ascendente.
>   El último nodo apunta al primero. ULT es local a la carga (el C no lo devuelve). }
> ACCION SIMPLE_CIRC_INS ES
> AMBIENTE
>     NODO = REGISTRO
>         DATO: entero;
>         prox: Puntero a NODO;
>     FIN_REGISTRO;
>     PRIM, ULT, P, Q, ANT: Puntero a NODO;
>     valor: entero;
> PROCESO
>     PRIM := NIL;  ULT := NIL;
>     LEER(valor);
>     MIENTRAS valor <> -1 HACER
>         NUEVO(Q);
>         *Q.DATO := valor;
>         SI PRIM = NIL ENTONCES                  { CASO 1: lista vacía, el nodo se apunta a sí mismo }
>             PRIM := Q;  ULT := Q;
>             *Q.prox := PRIM;
>         SINO
>             P := PRIM;  ANT := NIL;
>             MIENTRAS (*P.prox <> PRIM) Y (*P.DATO < valor) HACER
>                 ANT := P;
>                 P := *P.prox;
>             FIN_MIENTRAS;
>             SI (P = PRIM) Y (*P.DATO >= *Q.DATO) ENTONCES          { CASO 2: antes del primero }
>                 *Q.prox := PRIM;
>                 PRIM := Q;
>                 *ULT.prox := Q;                 { el último se re-engancha al nuevo primero }
>             SINO
>                 SI (*P.prox = PRIM) Y (*P.DATO < *Q.DATO) ENTONCES { CASO 4: después del último }
>                     *P.prox := Q;
>                     *Q.prox := PRIM;            { el nuevo último cierra el círculo }
>                     ULT := Q;
>                 SINO                            { CASO 3: en el medio (antes de P) }
>                     *ANT.prox := Q;
>                     *Q.prox := P;
>                 FIN_SI;
>             FIN_SI;
>         FIN_SI;
>         LEER(valor);
>     FIN_MIENTRAS;
>     { imprime_lista: igual a Pseudocodigo/LISTA_CIRC }
>     ESCRIBIR("CONTENIDO DE LA LISTA");
>     SI PRIM = NIL ENTONCES
>         ESCRIBIR("LISTA VACIA");
>     SINO
>         P := PRIM;
>         MIENTRAS *P.prox <> PRIM HACER
>             ESCRIBIR("Valor: ", *P.DATO);
>             P := *P.prox;
>         FIN_MIENTRAS;
>         ESCRIBIR("Valor: ", *P.DATO);
>         { verificación (no está en el C): P es el último; su prox tiene que ser PRIM y ULT tiene que ser P }
>         ESCRIBIR("[verif] el último apunta a PRIM: ", *P.prox = PRIM, " / ULT es el último: ", ULT = P);
>     FIN_SI;
>     { libera_lista, tal cual el C: no pregunta si PRIM = NIL }
>     P := PRIM;
>     MIENTRAS *P.prox <> PRIM HACER
>         Q := *P.prox;
>         DISPONER(P);
>         P := Q;
>     FIN_MIENTRAS;
>     DISPONER(P);
>     ESCRIBIR("LISTO!!  -- LIBERANDO LA LISTA");
> FIN_ACCION
> ```

### Código C — `C/Listas/LISTAS_SIMPLE_CIRC_INS.c`

```c
//Programa que crea nodos en una LISTA SIMPLE enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox;
} nodo_t;

nodo_t *crea_lista(nodo_t *prim){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL, *ant = NULL, *ult = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        //Caso 1
        if (prim == NULL){
            
            prim = q;   
            ult = q;   
            q->prox = prim;    
                
        }

        else {

            //Busco el lugar para insercion
            p = prim, ant = NULL;            
            while (p->prox != prim && p->val < valor){

                ant = p;
                p = p->prox;

            }
            
            if (p == prim && p->val >= q->val){ //Caso 2
                
                q->prox = prim; 
                prim = q;
                ult->prox = q;                
                
            }
            else if (p->prox == prim && p->val < q->val) { //Caso 4

                p->prox = q;
                q->prox = prim;
                ult = q;

            }
            else { //Caso 3
                
                ant->prox = q;
                q->prox = p;                

            }
        
        }
        
    }
    
    return prim;
}

void imprime_lista(nodo_t *prim) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    if (prim == NULL) {
        printf("LISTA VACIA \n");
        return;
    }

    while (p->prox != prim) {
        //printf("Valor: %d \n", p->val);
        printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->prox;
    }

    //Trato el ultimo nodo fuera del ciclo
    //printf("Valor: %d \n", p->val);
    printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
}

void libera_lista(nodo_t *prim) {
    nodo_t  *p = prim, *prox = prim;

    printf("LIBERANDO LA LISTA \n");

    while (p->prox != prim) {       
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        

        prox = p->prox;            
        free(p);    
        p = prox;        

    }

    //Libero el ultimo afuera
    //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        
    free(p);    

    printf("LISTO!!  -- LIBERANDO LA LISTA \n");
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    prim = crea_lista(prim);

    //printf("Valor de PRIM luego de cargar ... %p\n", prim);

    //Muestro la lista creada
    imprime_lista(prim);
    
    //Libero recursos
    libera_lista(prim);

    return 0;
}
```

> [!bug] Error en el código del repo — `libera_lista` con la lista vacía
> `libera_lista` arranca con `while (p->prox != prim)` sin preguntar antes si `prim` es `NULL`. Si el primer valor que se ingresa es `-1`, la lista queda vacía, `imprime_lista` escribe `LISTA VACIA` (ella sí lo controla) y después `libera_lista(NULL)` accede a `NULL->prox`: el programa se cae (*segmentation fault*). En la traducción, la extensión corta en la misma línea: `"P" vale NIL: no apunta a ningún nodo`. Faltaría un `if (prim == NULL) return;` al principio, como tienen el `imprime_lista` del mismo archivo y el `libera_lista` de la versión Python. El mismo `libera_lista` está en `LISTAS_SIMPLE_CIRC_DEL.c`.

> [!example]- Versión Python — `Python/Listas/LISTAS_SIMPLE_CIRC_INS.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>
> def crea_lista():
>     prim = None
>     ult = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             ult = q
>             q.prox = prim
>         else:
>             p = prim
>             ant = None
>             while p.prox != prim and p.val < valor:
>                 ant = p
>                 p = p.prox
>             if p == prim and p.val >= q.val:
>                 q.prox = prim
>                 prim = q
>                 ult.prox = q
>             elif p.prox == prim and p.val < q.val:
>                 p.prox = q
>                 q.prox = prim
>                 ult = q
>             else:
>                 ant.prox = q
>                 q.prox = p
>     return prim
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     if prim is None:
>         print("LISTA VACIA")
>         return
>     p = prim
>     while p.prox != prim:
>         print(f"Valor: {p.val} \t Direccion del NODO {id(p)} \t Direccion del PROX {id(p.prox)}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>     print(f"Valor: {p.val} \t Direccion del NODO {id(p)} \t Direccion del PROX {id(p.prox)}")
>     # print(f"Dirección (id) del nodo: {id(p)}")
>
> def libera_lista(prim):
>     print("LIBERANDO LA LISTA")
>     if prim is None:
>         return
>     p = prim
>     while p.prox != prim:
>         prox = p.prox
>         p = prox
>     print("LISTO!!  -- LIBERANDO LA LISTA")
>
> def main():
>     prim = crea_lista()
>     imprime_lista(prim)
>     libera_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo. `libera_lista` **sí** pregunta `if prim is None: return`, así que la versión Python no tiene el error de la lista vacía. `imprime_lista` muestra el `id()` de cada nodo y de su `prox`: ahí se ve que el `prox` del último es el `id` del primero.

---

## 6 · Lista simple circular — eliminación (`LISTAS_SIMPLE_CIRC_DEL`)

**Qué hace.** Carga como la sección 5 (código repetido) y borra un valor de la lista circular.

- **Lista vacía:** `ERROR - LISTA VACIA!!!!`.
- **Recupera `ULT`:** como `crea_lista` no lo devolvió, primero recorre `while (p->prox != prim)` hasta el último y lo guarda en `ult`. Hace falta para el CASO 2.
- **Búsqueda:** `while (p->prox != prim && p->val != valor)` con `P` y `ANT`. Como en la inserción, corta **en el último** sin haberlo comparado; por eso la pregunta de "no está" no es `P = NIL` sino **`*P.DATO <> valor`** (el comentario del código lo explica: "estoy parado en el último nodo, y puede ser el valor a borrar"). Si hay repetidos borra el primero.
- **CASO 1 (único nodo),** `prim == ult`: `PRIM := NIL`.
- **CASO 2 (el primero),** `p == prim`: `PRIM := *P.prox; *ULT.prox := *P.prox`: el último pasa a apuntar al nuevo primero.
- **CASO 4 (el último),** `p->prox == prim`: `*ANT.prox := *P.prox` (o sea, `ANT` apunta a `PRIM` y cierra el círculo) y `ULT := ANT`.
- **CASO 3 (medio):** `*ANT.prox := *P.prox`.
- `free(p)` en todos los casos. Es la misma estructura que la eliminación de la filmina 8, con dos cosas propias de la circular: el control del último afuera del ciclo y el re-enganche de `ULT` al borrar el primero.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> La carga es la misma de la sección 5. Esto es `borra_lista`:
> ```
>     { borra_lista }
>     SI PRIM = NIL ENTONCES
>         ESCRIBIR("ERROR - LISTA VACIA!!!!");
>     SINO
>         P := PRIM;                              { recupero el último }
>         MIENTRAS *P.prox <> PRIM HACER
>             P := *P.prox;
>         FIN_MIENTRAS;
>         ULT := P;
>         LEER(valor);
>         P := PRIM;  ANT := NIL;
>         MIENTRAS (*P.prox <> PRIM) Y (*P.DATO <> valor) HACER
>             ANT := P;
>             P := *P.prox;
>         FIN_MIENTRAS;
>         SI *P.DATO <> valor ENTONCES            { P quedó en el último: hay que mirarlo también }
>             ESCRIBIR("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.");
>         SINO
>             SI PRIM = ULT ENTONCES              { CASO 1: único nodo }
>                 PRIM := NIL;  ULT := NIL;
>             SINO
>                 SI P = PRIM ENTONCES            { CASO 2: el primero }
>                     PRIM := *P.prox;
>                     *ULT.prox := *P.prox;       { el último se engancha al nuevo primero }
>                 SINO
>                     SI *P.prox = PRIM ENTONCES  { CASO 4: el último }
>                         *ANT.prox := *P.prox;   { o sea, *ANT.prox := PRIM }
>                         ULT := ANT;
>                     SINO                        { CASO 3: en el medio }
>                         *ANT.prox := *P.prox;
>                     FIN_SI;
>                 FIN_SI;
>             FIN_SI;
>             DISPONER(P);
>         FIN_SI;
>     FIN_SI;
> ```

### Código C — `C/Listas/LISTAS_SIMPLE_CIRC_DEL.c`

```c
//Programa que crea nodos en una LISTA SIMPLE enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox;
} nodo_t;

nodo_t *crea_lista(nodo_t *prim){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL, *ant = NULL, *ult = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        //Caso 1
        if (prim == NULL){
            
            prim = q;   
            ult = q;   
            q->prox = prim;    
                
        }

        else {

            //Busco el lugar para insercion
            p = prim, ant = NULL;            
            while (p->prox != prim && p->val < valor){

                ant = p;
                p = p->prox;

            }
            
            if (p == prim && p->val >= q->val){ //Caso 2
                
                q->prox = prim; 
                prim = q;
                ult->prox = q;                
                
            }
            else if (p->prox == prim && p->val < q->val) { //Caso 4

                p->prox = q;
                q->prox = prim;
                ult = q;

            }
            else { //Caso 3
                
                ant->prox = q;
                q->prox = p;                

            }
        
        }
        
    }
    
    return prim;
}

void imprime_lista(nodo_t *prim) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    if (prim == NULL) {
        printf("LISTA VACIA \n");
        return;
    }

    while (p->prox != prim) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->prox;
    }

    //Trato el ultimo nodo fuera del ciclo
    printf("Valor: %d \n", p->val);
    //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
}

nodo_t *borra_lista(nodo_t *prim) {
    nodo_t *ant = prim, *ult = NULL, *p = prim;

    int valor;

    //Si es el pirmer nodo cargo al inicio, sino al final
    if (prim == NULL){
        printf("ERROR - LISTA VACIA!!!!");    
    }
    else
    {
        
        //Recupero el ultimo para hacer los cambios
        p = prim;            
        while (p->prox != prim){
            
            p = p->prox;

        }
        //Asigno el valor recuperado
        ult = p;
        //printf("ULT - Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);

        printf("Ingrese valor a eliminar:");
        scanf("%d", &valor);  

        //Busco el lugar para insercion
        p = prim, ant = NULL;            
        while (p->prox != prim && p->val != valor){

            ant = p;
            p = p->prox;

        }

        if (p->val != valor){ //Pregunto asi porque estoy parado en el ultimo nodo, y puede ser el valor a borrar
            printf("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.\n");    
        }
        else
        {            
            
            //printf("EXITO - Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);

            if (prim == ult){ //Caso 1 
                //printf("Caso 1 -- Direccion de p %p \n", p);
                prim = NULL;
                ult = NULL;

            }            
            else if (p == prim){ //Caso 2
                
                //printf("Caso 2 -- Direccion de p %p \n", p);
                prim = p->prox;
                ult->prox = p->prox;
                
            }
            else if (p->prox == prim){ //Caso 4
                
                //printf("Caso 4 -- Direccion de p %p \n", p);
                ant->prox = p->prox;
                ult = ant;

            }
            else { //Caso 3
                
                //printf("Caso 3 -- Direccion de p %p \n", p);
                ant->prox = p->prox;
            }

            free(p);            
        }

    }

    //printf("SALGO BORRADO - Direccion de PRIM %p \n", prim);
    return prim;
}

void libera_lista(nodo_t *prim) {
    nodo_t  *p = prim, 
            *prox = prim;

    printf("LIBERANDO LA LISTA \n");

    while (p->prox != prim) {       
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        

        prox = p->prox;            
        free(p);    
        p = prox;        

    }

    //Libero el ultimo afuera
    //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        
    free(p);    

    printf("LISTO!!  -- LIBERANDO LA LISTA \n");
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    prim = crea_lista(prim);

    //printf("Valor de PRIM luego de cargar ... %p\n", prim);

    //Muestro la lista creada
    imprime_lista(prim);

    //elimino selectivamente
    prim = borra_lista(prim);

    //Veo como queda con el nodo eliminado
    imprime_lista(prim);

    //Libero recursos
    libera_lista(prim);

    return 0;
}
```

> [!bug] Error en el código del repo — `libera_lista` cuando la lista queda vacía
> Es el mismo `libera_lista` de la sección 5, y acá se puede llegar a él con la lista vacía de **dos** maneras: ingresando `-1` de entrada, o **borrando el único nodo** (por ejemplo, cargar `5`, `-1` y borrar `5`). `borra_lista` deja `prim` en `NULL` correctamente, `imprime_lista` escribe `LISTA VACIA`, y `libera_lista(NULL)` accede a `NULL->prox` y el programa se cae. En la extensión, las dos entradas terminan con `"P" vale NIL` en el `MIENTRAS *P.prox <> PRIM` de la liberación. `borra_lista` en sí está bien.

> [!example]- Versión Python — `Python/Listas/LISTAS_SIMPLE_CIRC_DEL.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>
> def crea_lista():
>     prim = None
>     ult = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             ult = q
>             q.prox = prim
>         else:
>             p = prim
>             ant = None
>             while p.prox != prim and p.val < valor:
>                 ant = p
>                 p = p.prox
>             if p == prim and p.val >= q.val:
>                 q.prox = prim
>                 prim = q
>                 ult.prox = q
>             elif p.prox == prim and p.val < q.val:
>                 p.prox = q
>                 q.prox = prim
>                 ult = q
>             else:
>                 ant.prox = q
>                 q.prox = p
>     return prim
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     if prim is None:
>         print("LISTA VACIA")
>         return
>     p = prim
>     while p.prox != prim:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>     print(f"Valor: {p.val}")
>     # print(f"Dirección (id) del nodo: {id(p)}")
>
> def borra_lista(prim):
>     if prim is None:
>         print("ERROR - LISTA VACIA!!!!")
>         return prim
>     # find last
>     p = prim
>     while p.prox != prim:
>         p = p.prox
>     ult = p
>     try:
>         valor = int(input("Ingrese valor a eliminar:"))
>     except ValueError:
>         return prim
>     p = prim
>     ant = None
>     while p.prox != prim and p.val != valor:
>         ant = p
>         p = p.prox
>     if p.val != valor:
>         print("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.")
>         return prim
>     if prim == ult:
>         prim = None
>         ult = None
>     elif p == prim:
>         prim = p.prox
>         ult.prox = prim
>     elif p.prox == prim:
>         ant.prox = p.prox
>         ult = ant
>     else:
>         ant.prox = p.prox
>     return prim
>
> def libera_lista(prim):
>     print("LIBERANDO LA LISTA")
>     if prim is None:
>         return
>     p = prim
>     while p.prox != prim:
>         prox = p.prox
>         p = prox
>     # last
>     print("LISTO!!  -- LIBERANDO LA LISTA")
>
> def main():
>     prim = crea_lista()
>     imprime_lista(prim)
>     prim = borra_lista(prim)
>     imprime_lista(prim)
>     libera_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo; en el CASO 2 escribe `ult.prox = prim` después de mover `prim` (es lo mismo que `ult->prox = p->prox`). `libera_lista` controla `None`, así que no tiene el error del C.

---

## 7 · Lista doble circular — inserción ordenada (`LISTAS_DOBLE_CIRC_INS`)

**Qué hace.** Carga una lista **doble circular ordenada ascendente**: el `prox` del último apunta al primero y el `ant` del primero apunta al último. Hay `prim` y `ult`, y los dos se devuelven en un `nodo_pu`.

- **CASO 1 (vacía):** `prim = ult = q`, y `q->prox = q; q->ant = q`: el único nodo se apunta a sí mismo **por los dos lados**.
- **Búsqueda:** sólo con `P`: `while (p != ult && p->val < valor) p = p->prox`. Como hay `ULT`, la condición de corte es **`P = ULT`** (en la simple circular era `*P.prox = PRIM`; es lo mismo, escrito con el puntero externo). Igual que en la simple circular, se para en el último sin compararlo, y los casos vuelven a preguntar por el valor.
- **CASO 2 (antes del primero),** `p == prim && p->val >= valor`: los enganches de la doble (`*Q.prox := P; *P.ant := Q; PRIM := Q`) más los dos del círculo: **`*Q.ant := ULT`** y **`*ULT.prox := Q`**.
- **CASO 4 (después del último),** `p == ult && p->val < valor`: `*ULT.prox := Q; *Q.ant := ULT; ULT := Q` más los dos del círculo: **`*Q.prox := PRIM`** y **`*PRIM.ant := Q`**.
- **CASO 3 (medio):** idéntico a la doble lineal (`*(*P.ant).prox := Q`…), sin enganches extra: el círculo no se toca.
- **Recorridos:** hacia adelante `while (p != ult)` desde `prim` y hacia atrás `while (p != prim)` desde `ult` por `ant`; en los dos, el nodo del extremo se escribe afuera del ciclo.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> El programa completo que se corrió. La línea `[verif]` no está en el C: comprueba los dos cierres del círculo.
> ```
> { Traducción de LISTAS_DOBLE_CIRC_INS.c: lista doble circular ordenada ascendente }
> ACCION DOBLE_CIRC_INS ES
> AMBIENTE
>     NODO = REGISTRO
>         DATO: entero;
>         prox, ant: Puntero a NODO;
>     FIN_REGISTRO;
>     PRIM, ULT, P, Q: Puntero a NODO;
>     valor: entero;
> PROCESO
>     PRIM := NIL;  ULT := NIL;
>     LEER(valor);
>     MIENTRAS valor <> -1 HACER
>         NUEVO(Q);
>         *Q.DATO := valor;
>         SI PRIM = NIL ENTONCES                  { CASO 1: lista vacía, prox y ant apuntan al mismo nodo }
>             PRIM := Q;  ULT := Q;
>             *Q.prox := Q;  *Q.ant := Q;
>         SINO
>             P := PRIM;
>             MIENTRAS (P <> ULT) Y (*P.DATO < valor) HACER
>                 P := *P.prox;
>             FIN_MIENTRAS;
>             SI (P = PRIM) Y (*P.DATO >= *Q.DATO) ENTONCES          { CASO 2: antes del primero }
>                 *Q.prox := P;  *P.ant := Q;
>                 *Q.ant := ULT;
>                 PRIM := Q;
>                 *ULT.prox := Q;                 { cierre: ULT -> nuevo PRIM }
>             SINO
>                 SI (P = ULT) Y (*P.DATO < *Q.DATO) ENTONCES        { CASO 4: después del último }
>                     *ULT.prox := Q;  *Q.ant := ULT;
>                     *Q.prox := PRIM;
>                     ULT := Q;
>                     *PRIM.ant := Q;             { cierre: PRIM <- nuevo ULT }
>                 SINO                            { CASO 3: en el medio (antes de P) }
>                     *Q.ant := *P.ant;
>                     *Q.prox := P;
>                     *(*P.ant).prox := Q;
>                     *P.ant := Q;
>                 FIN_SI;
>             FIN_SI;
>         FIN_SI;
>         LEER(valor);
>     FIN_MIENTRAS;
>     ESCRIBIR("CONTENIDO DE LA LISTA");
>     SI PRIM = NIL ENTONCES
>         ESCRIBIR("LISTA VACIA");
>     SINO
>         P := PRIM;
>         MIENTRAS P <> ULT HACER
>             ESCRIBIR("Valor: ", *P.DATO);
>             P := *P.prox;
>         FIN_MIENTRAS;
>         ESCRIBIR("Valor: ", *P.DATO);
>         ESCRIBIR("CONTENIDO DE LA LISTA -- REVERSA");
>         P := ULT;
>         MIENTRAS P <> PRIM HACER
>             ESCRIBIR("Valor: ", *P.DATO);
>             P := *P.ant;
>         FIN_MIENTRAS;
>         ESCRIBIR("Valor: ", *P.DATO);
>         { verificación (no está en el C): los dos cierres del círculo }
>         ESCRIBIR("[verif] *ULT.prox = PRIM: ", *ULT.prox = PRIM, " / *PRIM.ant = ULT: ", *PRIM.ant = ULT);
>     FIN_SI;
> FIN_ACCION
> ```

### Código C — `C/Listas/LISTAS_DOBLE_CIRC_INS.c`

```c
//Programa que crea nodos en una LISTA DOBLE enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox, *ant;
} nodo_t;

typedef struct prim_ult {    
    struct nodo *pr, *ul;
} nodo_pu;

nodo_pu *crea_lista(nodo_t *prim, nodo_t *ult){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL;
    nodo_pu *sal = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        //Caso 1
        if (prim == NULL){
            
            prim = q;   
            ult = q;   
            q->prox = q;    
            q->ant = q;    
                
        }

        else {

            //Busco el lugar para insercion
            p = prim;            
            while (p != ult && p->val < valor){
                
                p = p->prox;

            }

            //Caso 2 -- ANTES del PRIMERO
            if (p == prim && p->val >= q->val){
                            
                q->prox = p;
                p->ant = q;
                q->ant = ult;
                prim = q;
                ult->prox = q;
                
            }
            else if (p == ult && p->val < q->val) { //Caso 4 -- DESPUES DEL ULTIMO
                
                ult->prox = q;
                q->ant = ult;
                q->prox = prim;
                ult = q;
                prim->ant = q;

            }
            else { //Caso 3 -- MEDIO

                q->ant = p->ant;
                q->prox = p;
                p->ant->prox = q; // *(*p.ant).prox
                p->ant = q;

            }
        
        }
        
    }

    //printf("Direccion de prim %p \t Direccion de ULT %p \n", prim, ult);

    //Genero el registro de salida con los punteros extremos
    //solicito memoria para el nodo
    sal = (nodo_pu *) malloc(sizeof(nodo_pu));

    sal->pr = prim;
    sal->ul = ult;

    return sal;
}

void imprime_lista(nodo_t *prim, nodo_t *ult) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    //Muestro punteros externos
    //printf("prim: %p \n", prim);
    //printf("ult: %p \n", ult);
    

    if (prim == NULL) {
        printf("LISTA VACIA \n");
        return;
    }

    while (p != ult) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Dir del NODO %p \t Dir del PROX %p \t Dir del ANT %p \n", p->val, p, p->prox, p->ant);
        p = p->prox;
    }

    //Trato el ultimo nodo fuera del ciclo
    printf("Valor: %d \n", p->val);
    //printf("Valor: %d \t Dir del NODO %p \t Dir del PROX %p \t Dir del ANT %p \n", p->val, p, p->prox, p->ant);
}

void imprime_lista_reversa(nodo_t *prim, nodo_t *ult) {
    nodo_t *p = ult;

    printf("CONTENIDO DE LA LISTA \n");

    if (prim == NULL) {
        printf("LISTA VACIA \n");
        return;
    }

    while (p != prim) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->ant;
    }

    //Trato el ultimo nodo fuera del ciclo
    printf("Valor: %d \n", p->val);
    //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
}

void libera_lista(nodo_t *prim, nodo_t *ult) {
    nodo_t  *p = prim, *prox = prim;

    printf("LIBERANDO LA LISTA \n");

    while (p != ult) {       
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        

        prox = p->prox;            
        free(p);    
        p = prox;        

    }

    //Libero el ultimo afuera
    //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        
    free(p);    

    printf("LISTO!!  -- LIBERANDO LA LISTA \n");
}


int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL, *ult = NULL;
    nodo_pu *rec = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    rec = crea_lista(prim, ult);

    //printf("Valor de PRIM luego de cargar ... %p\n", rec->pr);
    //printf("Valor de ULT luego de cargar ... %p\n", rec->ul);

    //Asigno los valores generados
    prim = rec->pr;
    ult = rec->ul;

    //Muestro la lista creada
    imprime_lista(prim, ult);

    //Muestro la lista creada
    imprime_lista_reversa(prim, ult);
    
    //Libero recursos
    libera_lista(prim, ult);

    return 0;
}
```

`libera_lista` usa `while (p != ult)`: con la lista vacía `p` y `ult` son los dos `NULL`, no entra al ciclo y hace `free(NULL)`, que no hace nada. Así que acá, a diferencia de la simple circular, la lista vacía no rompe nada.

> [!example]- Versión Python — `Python/Listas/LISTAS_DOBLE_CIRC_INS.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>         self.ant = None
>
> def crea_lista():
>     prim = None
>     ult = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             ult = q
>             q.prox = q
>             q.ant = q
>         else:
>             p = prim
>             while p != ult and p.val < valor:
>                 p = p.prox
>             if p == prim and p.val >= q.val:
>                 q.prox = p
>                 p.ant = q
>                 q.ant = ult
>                 prim = q
>                 ult.prox = q
>             elif p == ult and p.val < q.val:
>                 ult.prox = q
>                 q.ant = ult
>                 q.prox = prim
>                 ult = q
>                 prim.ant = q
>             else:
>                 q.ant = p.ant
>                 q.prox = p
>                 p.ant.prox = q
>                 p.ant = q
>     return prim, ult
>
> def imprime_lista(prim, ult):
>     print("CONTENIDO DE LA LISTA")
>     if prim is None:
>         print("LISTA VACIA")
>         return
>     p = prim
>     while p != ult:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>     print(f"Valor: {p.val}")
>     # print(f"Dirección (id) del nodo: {id(p)}")
>
> def imprime_lista_reversa(prim, ult):
>     print("CONTENIDO DE LA LISTA -- REVERSA")
>     if prim is None:
>         print("LISTA VACIA")
>         return
>     p = ult
>     while p != prim:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.ant
>     print(f"Valor: {p.val}")
>     # print(f"Dirección (id) del nodo: {id(p)}")
>
> def libera_lista(prim, ult):
>     print("LIBERANDO LA LISTA")
>     if prim is None:
>         return
>     p = prim
>     while p != ult:
>         prox = p.prox
>         p = prox
>     print("LISTO!!  -- LIBERANDO LA LISTA")
>
> def main():
>     prim, ult = crea_lista()
>     imprime_lista(prim, ult)
>     imprime_lista_reversa(prim, ult)
>     libera_lista(prim, ult)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo, con la tupla `prim, ult`.

---

## 8 · Lista doble circular — eliminación (`LISTAS_DOBLE_CIRC_DEL`)

**Qué hace.** Carga como la sección 7 (código repetido) y borra un valor. `borra_lista` está armado **copiando el de la doble lineal** (sección 4) y agregándole los enganches del círculo, pero quedaron dos cosas de la lineal que en una circular no funcionan:

- **Búsqueda:** `while (p != NULL && p->val != valor)`, la misma de la doble lineal. En una circular `P` **nunca** llega a `NULL`: si el valor está, corta bien; si no está, da vueltas para siempre.
- **CASO 1 (único),** `prim == ult`: `PRIM := NIL; ULT := NIL`. Bien.
- **CASO 2 (el primero),** `p == prim && p->val >= valor`: `*(*P.prox).ant := ULT; PRIM := *P.prox; *ULT.prox := *P.prox`. Bien: el nuevo primero apunta hacia atrás a `ULT`, y `ULT` hacia adelante al nuevo primero. (El `p->val >= valor` sobra: si se llegó acá, `p->val` es igual a `valor`.)
- **CASO 4 (el último),** `p == ult && p->val < valor`: **nunca es verdadero**, porque `p->val` es igual a `valor`. Ver el error.
- **CASO 3 (medio):** `*(*P.prox).ant := *P.ant; *(*P.ant).prox := *P.prox`.
- Los comentarios `//*prim.ant := nil` y `//*ult.prox := nil` también vienen de la doble lineal.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> La carga es la misma de la sección 7. Esto es `borra_lista` **tal cual el C, con sus errores**:
> ```
>     { borra_lista, tal cual el C }
>     SI PRIM = NIL ENTONCES
>         ESCRIBIR("ERROR - LISTA VACIA!!!!");
>     SINO
>         LEER(valor);
>         P := PRIM;
>         MIENTRAS (P <> NIL) Y (*P.DATO <> valor) HACER   { en una circular P nunca llega a NIL }
>             P := *P.prox;
>         FIN_MIENTRAS;
>         SI P = NIL ENTONCES
>             ESCRIBIR("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.");
>         SINO
>             SI PRIM = ULT ENTONCES                          { CASO 1: único nodo }
>                 PRIM := NIL;  ULT := NIL;
>             SINO
>                 SI (P = PRIM) Y (*P.DATO >= valor) ENTONCES { CASO 2: el primero }
>                     *(*P.prox).ant := ULT;
>                     PRIM := *P.prox;
>                     *ULT.prox := *P.prox;
>                 SINO
>                     SI (P = ULT) Y (*P.DATO < valor) ENTONCES  { CASO 4: nunca es verdadero }
>                         *(*P.ant).prox := PRIM;
>                         ULT := *P.ant;
>                         *PRIM.prox := *P.ant;
>                     SINO                                    { CASO 3 }
>                         *(*P.prox).ant := *P.ant;
>                         *(*P.ant).prox := *P.prox;
>                     FIN_SI;
>                 FIN_SI;
>             FIN_SI;
>             DISPONER(P);
>         FIN_SI;
>     FIN_SI;
> ```

### Código C — `C/Listas/LISTAS_DOBLE_CIRC_DEL.c`

```c
//Programa que crea nodos en una LISTA DOBLE enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox, *ant;
} nodo_t;

typedef struct prim_ult {    
    struct nodo *pr, *ul;
} nodo_pu;

nodo_pu *crea_lista(nodo_t *prim, nodo_t *ult){
    //Defino punteros a NODO para la creación
    nodo_t *q = NULL, *p = NULL;
    nodo_pu *sal = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        //Caso 1
        if (prim == NULL){
            
            prim = q;   
            ult = q;   
            q->prox = q;    
            q->ant = q;    
                
        }

        else {

            //Busco el lugar para insercion
            p = prim;            
            while (p != ult && p->val < valor){
                
                p = p->prox;

            }

            //Caso 2 -- ANTES del PRIMERO
            if (p == prim && p->val >= q->val){
                            
                q->prox = p;
                p->ant = q;
                q->ant = ult;
                prim = q;
                ult->prox = q;
                
            }
            else if (p == ult && p->val < q->val) { //Caso 4 -- DESPUES DEL ULTIMO
                
                ult->prox = q;
                q->ant = ult;
                q->prox = prim;
                ult = q;
                prim->ant = q;

            }
            else { //Caso 3 -- MEDIO

                q->ant = p->ant;
                q->prox = p;
                p->ant->prox = q; // *(*p.ant).prox
                p->ant = q;

            }
        
        }
        
    }

    //printf("Direccion de prim %p \t Direccion de ULT %p \n", prim, ult);

    //Genero el registro de salida con los punteros extremos
    //solicito memoria para el nodo
    sal = (nodo_pu *) malloc(sizeof(nodo_pu));

    sal->pr = prim;
    sal->ul = ult;

    return sal;
}

void imprime_lista(nodo_t *prim, nodo_t *ult) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    //Muestro punteros externos
    //printf("prim: %p \n", prim);
    //printf("ult: %p \n", ult);
    

    if (prim == NULL) {
        printf("LISTA VACIA \n");
        return;
    }

    while (p != ult) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Dir del NODO %p \t Dir del PROX %p \t Dir del ANT %p \n", p->val, p, p->prox, p->ant);
        p = p->prox;
    }

    //Trato el ultimo nodo fuera del ciclo
    printf("Valor: %d \n", p->val);
    //printf("Valor: %d \t Dir del NODO %p \t Dir del PROX %p \t Dir del ANT %p \n", p->val, p, p->prox, p->ant);
}

void imprime_lista_reversa(nodo_t *prim, nodo_t *ult) {
    nodo_t *p = ult;

    printf("CONTENIDO DE LA LISTA -- REVERSA \n");

    if (prim == NULL) {
        printf("LISTA VACIA \n");
        return;
    }

    while (p != prim) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->ant;
    }

    //Trato el ultimo nodo fuera del ciclo
    printf("Valor: %d \n", p->val);
    //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
}

void libera_lista(nodo_t *prim, nodo_t *ult) {
    nodo_t  *p = prim, *prox = prim;

    printf("LIBERANDO LA LISTA \n");

    while (p != ult) {       
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        

        prox = p->prox;            
        free(p);    
        p = prox;        

    }

    //Libero el ultimo afuera
    //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);        
    free(p);    

    printf("LISTO!!  -- LIBERANDO LA LISTA \n");
}

nodo_pu *borra_lista(nodo_t *prim, nodo_t *ult) {
    nodo_t  *p = prim;
    nodo_pu *sal = NULL;

    int valor;

    //Si es el pirmer nodo cargo al inicio, sino al final
    if (prim == NULL){
        printf("ERROR - LISTA VACIA!!!!");    
    }
    else
    {
        printf("Ingrese valor a eliminar:");
        scanf("%d", &valor);  

        //Busco el valor a eliminar
        p = prim;            
        while (p != NULL && p->val != valor){
            
            p = p->prox;

        }

        if (p == NULL){
            printf("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.\n");    
        }
        else
        {            
            if (prim == ult) { //Caso 1 -- UNICO NODO

                prim = NULL;
                ult = NULL;

            }            
            else if (p == prim && p->val >= valor){ //Caso 2
                                                
                p->prox->ant = ult; //*prim.ant := nil
                prim = p->prox;
                ult->prox = p->prox;
                
            }
            else if (p == ult && p->val < valor) { //Caso 4
                
                p->ant->prox = prim; //*ult.prox := nil
                ult = p->ant;
                prim->prox = p->ant;

            }
            else { //Caso 3

                p->prox->ant = p->ant;
                p->ant->prox = p->prox;

            }

            free(p);            
        }

    }

    //Genero el registro de salida con los punteros extremos
    //solicito memoria para el nodo
    sal = (nodo_pu *) malloc(sizeof(nodo_pu));

    sal->pr = prim;
    sal->ul = ult;

    return sal;
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL, *ult = NULL;
    nodo_pu *rec = NULL;

    //printf("Valor inicial de PRIM antes de cargar ... %p\n", prim);

    //Creo la lista con valores enviados desde el teclado    
    //Al terminar de crear retorno el puntero PRIM que se generó en la carga
    rec = crea_lista(prim, ult);

    //printf("Valor de PRIM luego de cargar ... %p\n", rec->pr);
    //printf("Valor de ULT luego de cargar ... %p\n", rec->ul);

    //Asigno los valores generados
    prim = rec->pr;
    ult = rec->ul;

    //Muestro la lista creada
    imprime_lista(prim, ult);

    //elimino selectivamente
    rec = borra_lista(prim, ult);

    //Asigno los valores generados
    prim = rec->pr;
    ult = rec->ul;

    //Veo como queda con el nodo eliminado
    imprime_lista(prim, ult);

    //Muestro la lista creada
    imprime_lista_reversa(prim, ult);
    
    //Libero recursos
    libera_lista(prim, ult);

    return 0;
}
```

> [!bug] Error en el código del repo — si el valor no está, no termina
> La búsqueda es `while (p != NULL && p->val != valor)`. En una lista circular ningún `prox` es `NULL`, así que si el valor **no está** en la lista, `p` da vueltas para siempre y el programa se cuelga (con `3 5 8` y borrar `9`; la extensión corta con "superó 20.000.000 instrucciones: casi seguro hay un ciclo infinito"). El `if (p == NULL)` de "SIN EXITO" nunca se cumple. La forma de cortar en una circular es la que usa el mismo repo en `LISTAS_SIMPLE_CIRC_DEL.c`: parar en el último (`p != ult`) y preguntar afuera `if (p->val != valor)`. **Le pasa también a la versión Python.**

> [!bug] Error en el código del repo — borrar el último deja `ult` colgado
> Con el valor encontrado, `p->val` es igual a `valor`, así que la condición del CASO 4, `p == ult && p->val < valor`, **nunca** es verdadera. Al borrar el último (por ejemplo `3 5 8` y borrar `8`), el programa entra al CASO 3: los enlaces quedan bien (`prim->ant` pasa a ser el 5 y el `prox` del 5 pasa a ser `prim`), pero **`ult` no se actualiza** y queda apuntando al nodo que se acaba de liberar con `free(p)`. Después, `imprime_lista` recorre `while (p != ult)` buscando un nodo que ya no está en el círculo: no termina nunca (en la extensión escribe `3 5 3 5 3 5…` hasta que la corta). `imprime_lista_reversa` y `libera_lista` arrancan desde ese nodo liberado.
> Además, aunque se llegara al CASO 4, su tercera línea está mal: `prim->prox = p->ant` cambia el **`prox`** del primero (lo haría apuntar al nuevo último y saltear el resto de la lista); lo que hay que actualizar es **`prim->ant`**. La versión Python del repo lo tiene bien: `elif p == ult:` sin la comparación de valores, y `prim.ant = ult`.

> [!example]- Corrección probada (no es del repo)
> Las dos correcciones salen del propio repo: la búsqueda de `LISTAS_SIMPLE_CIRC_DEL.c` (cortar en el último y mirarlo afuera) y el CASO 4 de `LISTAS_DOBLE_CIRC_DEL.py`. Se probó en la extensión con los mismos casos que el resto (ver Verificación).
> ```
>     { borra_lista CORREGIDA (no es el código del repo) }
>     SI PRIM = NIL ENTONCES
>         ESCRIBIR("ERROR - LISTA VACIA!!!!");
>     SINO
>         LEER(valor);
>         P := PRIM;
>         MIENTRAS (P <> ULT) Y (*P.DATO <> valor) HACER   { corta en ULT, como la carga }
>             P := *P.prox;
>         FIN_MIENTRAS;
>         SI *P.DATO <> valor ENTONCES                     { P puede ser ULT: se lo mira afuera }
>             ESCRIBIR("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.");
>         SINO
>             SI PRIM = ULT ENTONCES                       { CASO 1: único nodo }
>                 PRIM := NIL;  ULT := NIL;
>             SINO
>                 SI P = PRIM ENTONCES                     { CASO 2: el primero }
>                     *(*P.prox).ant := ULT;
>                     PRIM := *P.prox;
>                     *ULT.prox := PRIM;
>                 SINO
>                     SI P = ULT ENTONCES                  { CASO 4: el último }
>                         *(*P.ant).prox := PRIM;
>                         ULT := *P.ant;
>                         *PRIM.ant := ULT;
>                     SINO                                 { CASO 3: en el medio }
>                         *(*P.prox).ant := *P.ant;
>                         *(*P.ant).prox := *P.prox;
>                     FIN_SI;
>                 FIN_SI;
>             FIN_SI;
>             DISPONER(P);
>         FIN_SI;
>     FIN_SI;
> ```

> [!example]- Versión Python — `Python/Listas/LISTAS_DOBLE_CIRC_DEL.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>         self.ant = None
>
> def crea_lista():
>     prim = None
>     ult = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>             ult = q
>             q.prox = q
>             q.ant = q
>         else:
>             p = prim
>             # find insertion point to keep list sorted ascending
>             while p != ult and p.val < valor:
>                 p = p.prox
>             # Case 2: before first
>             if p == prim and p.val >= q.val:
>                 q.prox = p
>                 p.ant = q
>                 q.ant = ult
>                 prim = q
>                 ult.prox = q
>             # Case 4: after last
>             elif p == ult and p.val < q.val:
>                 ult.prox = q
>                 q.ant = ult
>                 q.prox = prim
>                 ult = q
>                 prim.ant = q
>             # Case 3: middle
>             else:
>                 q.ant = p.ant
>                 q.prox = p
>                 p.ant.prox = q
>                 p.ant = q
>     return prim, ult
>
> def imprime_lista(prim, ult):
>     print("CONTENIDO DE LA LISTA")
>     if prim is None:
>         print("LISTA VACIA")
>         return
>     p = prim
>     while p != ult:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>     print(f"Valor: {p.val}")
>     # print(f"Dirección (id) del nodo: {id(p)}")
>
> def imprime_lista_reversa(prim, ult):
>     print("CONTENIDO DE LA LISTA -- REVERSA")
>     if prim is None:
>         print("LISTA VACIA")
>         return
>     p = ult
>     while p != prim:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.ant
>     print(f"Valor: {p.val}")
>     # print(f"Dirección (id) del nodo: {id(p)}")
>
> def libera_lista(prim, ult):
>     print("LIBERANDO LA LISTA")
>     if prim is None:
>         return
>     p = prim
>     while p != ult:
>         prox = p.prox
>         # In Python, just let reference go
>         p = prox
>     # last node
>     print("LISTO!!  -- LIBERANDO LA LISTA")
>
> def borra_lista(prim, ult):
>     if prim is None:
>         print("ERROR - LISTA VACIA!!!!")
>         return prim, ult
>     try:
>         valor = int(input("Ingrese valor a eliminar:"))
>     except ValueError:
>         return prim, ult
>     p = prim
>     while p is not None and p.val != valor:
>         p = p.prox
>     if p is None:
>         print("SIN EXITO .. NO SE ENCUENTRA VALOR EN LA LISTA.")
>         return prim, ult
>     # Case 1: single node
>     if prim == ult:
>         prim = None
>         ult = None
>     # Case 2: delete first
>     elif p == prim:
>         prim = p.prox
>         prim.ant = ult
>         ult.prox = prim
>     # Case 4: delete last
>     elif p == ult:
>         ult = p.ant
>         ult.prox = prim
>         prim.ant = ult
>     # Case 3: middle
>     else:
>         p.ant.prox = p.prox
>         p.prox.ant = p.ant
>     # In Python, node will be GC'd
>     return prim, ult
>
> def main():
>     prim, ult = crea_lista()
>     imprime_lista(prim, ult)
>     prim, ult = borra_lista(prim, ult)
>     imprime_lista(prim, ult)
>     imprime_lista_reversa(prim, ult)
>     libera_lista(prim, ult)
>
> if __name__ == "__main__":
>     main()
> ```
>
> **Difiere del C en algo importante:** los casos 2 y 4 son `elif p == prim:` y `elif p == ult:` sin comparar valores, y el CASO 4 actualiza `prim.ant = ult`. O sea que en Python **borrar el último funciona**. Pero la búsqueda sigue siendo `while p is not None and p.val != valor`: si el valor no está, tampoco termina.

---

## 9 · Pila (`LISTAS_PILA`)

**Qué hace.** Arma una **pila** con una lista simple: cada valor nuevo se engancha **adelante** (`*Q.prox := PRIM; PRIM := Q`), así que `PRIM` es el tope y la lista queda en orden **inverso** al de carga (cargar `1 2 3` imprime `3 2 1`). No hay búsqueda ni casos: la lista vacía no es un caso aparte, porque si `PRIM = NIL` el nuevo queda con `prox = NIL`, que es lo correcto. Es el CASO 2 de la inserción simple usado siempre. El comentario `//NUEVO(Q)` del código marca la equivalencia con el pseudocódigo. **No hay operación de desapilar**: el programa sólo carga, imprime y libera.

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> ```
> { Traducción de LISTAS_PILA.c: cada nodo nuevo se engancha adelante (PRIM es el tope) }
> ACCION PILA ES
> AMBIENTE
>     NODO = REGISTRO
>         DATO: entero;
>         prox: Puntero a NODO;
>     FIN_REGISTRO;
>     PRIM, P, Q: Puntero a NODO;
>     valor: entero;
> PROCESO
>     PRIM := NIL;
>     LEER(valor);
>     MIENTRAS valor <> -1 HACER
>         NUEVO(Q);
>         *Q.DATO := valor;
>         *Q.prox := PRIM;
>         PRIM := Q;
>         LEER(valor);
>     FIN_MIENTRAS;
>     ESCRIBIR("CONTENIDO DE LA LISTA");
>     P := PRIM;
>     MIENTRAS P <> NIL HACER
>         ESCRIBIR("Valor: ", *P.DATO);
>         P := *P.prox;
>     FIN_MIENTRAS;
> FIN_ACCION
> ```

### Código C — `C/Listas/LISTAS_PILA.c`

```c
//Programa que crea una PILA, utilizando una lista enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox;
} nodo_t;

nodo_t *crea_lista(nodo_t *prim){
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *q = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t)); //NUEVO(Q)

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;
        q->prox = prim;

        //Reasigno prim al nuevo primer nodo
        prim = q;
        
    }

    return prim;    
}

void imprime_lista(nodo_t *prim) {
    nodo_t *p = prim;

    printf("CONTENIDO DE LA LISTA \n");

    while (p != NULL) {
        printf("Valor: %d \n", p->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", p->val, p, p->prox);
        p = p->prox;
    }
}

void libera_lista(nodo_t *prim) {
    nodo_t  *p = prim, 
            *prox = prim;

    while (p) {
        prox = p->prox;
        free(p);
        p = prox;
    }
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL;

    prim = crea_lista(prim);

    imprime_lista(prim);

    libera_lista(prim);

    return 0;
}
```

> [!example]- Versión Python — `Python/Listas/LISTAS_PILA.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>
> def crea_lista():
>     prim = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         q.prox = prim
>         prim = q
>     return prim
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     p = prim
>     while p:
>         print(f"Valor: {p.val}")
>         # print(f"Dirección (id) del nodo: {id(p)}")
>         p = p.prox
>
> def libera_lista(prim):
>     p = prim
>     while p:
>         prox = p.prox
>         p = prox
>
> def main():
>     prim = crea_lista()
>     imprime_lista(prim)
>     libera_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo.

---

## 10 · Cola (`LISTAS_COLA`)

**Qué hace.** Arma una **cola** con una lista simple y un puntero `ult` (local a `crea_lista`): cada valor nuevo se engancha **al final**. Si la lista está vacía, `PRIM := Q`; si no, `*ULT.prox := Q`; en los dos casos `ULT := Q` y `*Q.prox := NIL`. Queda en el orden de carga (`1 2 3` imprime `1 2 3`). Gracias a `ULT` no hace falta recorrer para encontrar el final. Acá la función que libera se llama `borra_lista` (en los otros archivos es `libera_lista`). **No hay operación de desencolar.**

> [!info] Traducción al pseudocódigo (no es material de la cátedra: es la equivalencia del código)
> ```
> { Traducción de LISTAS_COLA.c: cada nodo nuevo se engancha al final, con ULT }
> ACCION COLA ES
> AMBIENTE
>     NODO = REGISTRO
>         DATO: entero;
>         prox: Puntero a NODO;
>     FIN_REGISTRO;
>     PRIM, ULT, P, Q: Puntero a NODO;
>     valor: entero;
> PROCESO
>     PRIM := NIL;  ULT := NIL;
>     LEER(valor);
>     MIENTRAS valor <> -1 HACER
>         NUEVO(Q);
>         *Q.DATO := valor;
>         SI PRIM = NIL ENTONCES
>             PRIM := Q;
>         SINO
>             *ULT.prox := Q;
>         FIN_SI;
>         ULT := Q;
>         *Q.prox := NIL;
>         LEER(valor);
>     FIN_MIENTRAS;
>     ESCRIBIR("CONTENIDO DE LA LISTA");
>     P := PRIM;
>     MIENTRAS P <> NIL HACER
>         ESCRIBIR("Valor: ", *P.DATO);
>         P := *P.prox;
>     FIN_MIENTRAS;
> FIN_ACCION
> ```

### Código C — `C/Listas/LISTAS_COLA.c`

```c
//Programa que crea una COLA, utilizando una lista enlazada...

#include <stdio.h>
#include <stdlib.h> 


typedef struct nodo {
    int val;
    struct nodo *prox;
} nodo_t;

nodo_t *crea_lista(nodo_t *prim){
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *q = NULL, *ult = NULL;

    //Variable para carga
    int valor;

    while (1) {

        printf("Ingrese valor para el nodo (-1 para salir):");
        scanf("%d", &valor);  

        //Salgo dl bucle si ingresa -1
        if (valor == -1){
            break;
        }

        //solicito memoria para el nodo
        q = (nodo_t *) malloc(sizeof(nodo_t));

        //Cargo los datos del nodo (valor y puntero)
        q->val = valor;

        //Si es el pirmer nodo cargo al inicio, sino al final
        if (prim == NULL){
            
            prim = q;   
                
        }
        else {

            ult->prox = q;
        
        }

        ult = q;
        q->prox = NULL;
        
    }
    
    return prim;    
}

void imprime_lista(nodo_t *prim) {
    nodo_t *current = prim;

    printf("CONTENIDO DE LA LISTA \n");

    while (current != NULL) {
        printf("Valor: %d \n", current->val);
        //printf("Valor: %d \t Direccion del NODO %p \t Direccion del PROX %p \n", current->val, current, current->prox);
        current = current->prox;
    }
}

void borra_lista(nodo_t *prim) {
    nodo_t  *current = prim, 
            *prox = prim;

    while (current) {
        prox = current->prox;
        free(current);
        current = prox;
    }
}

int main(void) {    
    //DEFINO mis punteros de soporte y el de inicio
    nodo_t *prim = NULL;

    prim = crea_lista(prim);

    imprime_lista(prim);

    borra_lista(prim);

    return 0;
}
```

> [!example]- Versión Python — `Python/Listas/LISTAS_COLA.py`
> ```python
> class Nodo:
>     def __init__(self, val):
>         self.val = val
>         self.prox = None
>
> def crea_lista():
>     prim = None
>     ult = None
>     while True:
>         try:
>             valor = int(input("Ingrese valor para el nodo (-1 para salir):"))
>         except ValueError:
>             continue
>         if valor == -1:
>             break
>         q = Nodo(valor)
>         if prim is None:
>             prim = q
>         else:
>             ult.prox = q
>         ult = q
>         q.prox = None
>     return prim
>
> def imprime_lista(prim):
>     print("CONTENIDO DE LA LISTA")
>     current = prim
>     while current:
>         print(f"Valor: {current.val}")
>         # print(f"Dirección (id) del nodo: {id(current)}")
>         current = current.prox
>
> def borra_lista(prim):
>     current = prim
>     while current:
>         prox = current.prox
>         # In Python, garbage collection handles free
>         current = prox
>
> def main():
>     prim = crea_lista()
>     imprime_lista(prim)
>     borra_lista(prim)
>
> if __name__ == "__main__":
>     main()
> ```
>
> Mismo algoritmo.

---

## 11 · Pseudocódigo — `Pseudocodigo/LISTA_CIRC`

Es el único archivo de pseudocódigo de listas del repo (no tiene extensión). Transcripción textual:

```
Accion Lista_Circ es (PRIM: puntero a NODO);

Ambiente

	NODO = REGISTRO
			DATO: Entero;
			prox: PUNTERO A NODO;
	FIN REGISTRO;

	P, Q, ANT: PUNTERO A NODO;
	band: logico;

Proceso

	P := PRIM;
	
	MIENTRAS (*P.prox <> PRIM) HACER
			escribir(*P.dato)

			P := *P.prox;
	FIN  MIENTRAS

	//Ultimo nodo
	escribir(*P.dato)

Fin_Accion;
```

**Comentario.** Es un **recorrido** de una lista simple circular que escribe todos los datos; no inserta ni borra.

- Recibe `PRIM` como parámetro. En el `Ambiente` declara el `NODO` (`DATO`, `prox`), los punteros `P, Q, ANT` y `band: logico`, pero sólo usa `P`: los demás sobran (parece la cabecera de un algoritmo más grande, recortado).
- `P := PRIM` y `MIENTRAS (*P.prox <> PRIM)`: escribe `*P.dato` y avanza. La condición corta cuando `P` está **en el último** (su `prox` es `PRIM`), así que el último no se escribe adentro del ciclo: por eso hay un `escribir(*P.dato)` después del `FIN MIENTRAS` (el comentario `//Ultimo nodo`).
- Es exactamente el `imprime_lista` de `LISTAS_SIMPLE_CIRC_INS.c` / `_DEL.c`. Con un solo nodo funciona: `*P.prox` ya es `PRIM`, no entra al ciclo y escribe el único dato afuera.
- Usa `dato` en minúscula al escribir y `DATO` en el registro: en la cátedra es lo mismo. No se ejecutó en la extensión (es material del repo); se analizó leyéndolo, y el mismo recorrido está probado dentro de las traducciones de las secciones 5 y 6.

> [!bug] Error en el código del repo — lista vacía
> No pregunta si la lista está vacía. Si `PRIM = NIL`, `P` vale `NIL` y la condición `*P.prox <> PRIM` accede a un nodo que no existe. El `imprime_lista` del C sí lo controla con `if (prim == NULL)` antes del ciclo; acá faltaría un `SI PRIM = NIL ENTONCES … SINO … FIN_SI` alrededor del recorrido.

---

## 12 · `C/Listas/readme.md`

Transcripción textual (el archivo tiene una sola línea):

```
Definicion y procesos de Listas enlazadas
```

---

## 13 · Extra de Python — `lista_enlazada.py`

No tiene versión en C. Es una lista simple escrita **con clases** (`Nodo` con `dato` y `siguiente`; `ListaEnlazada` con `cabeza`), con otro estilo que el resto:

- `insertar_al_final`: si la lista está vacía, el nuevo es la cabeza; si no, **recorre hasta el último** (`while actual.siguiente`) y lo engancha ahí. No guarda un puntero al último como `LISTAS_COLA`.
- `insertar_al_inicio`: lo engancha adelante, como `LISTAS_PILA`.
- `eliminar`: busca con `actual` y `previo` (son `P` y `ANT`) la primera aparición; si `previo` es `None` mueve la cabeza (casos 1 y 2), si no, `previo.siguiente = actual.siguiente` (casos 3 y 4). Devuelve `True` o `False`.
- `main` ya trae los datos: inserta `10` y `20` al final y `5` al inicio (`5 -> 10 -> 20`), y después borra `20` (el último), `5` (el primero) y `10` (el único), mostrando la lista cada vez hasta que queda `vacía`.
- No inserta en orden.

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.dato == dato:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("Lista:", " -> ".join(elementos) if elementos else "vacía")

def main():
    lista = ListaEnlazada()
    lista.insertar_al_final(10)
    lista.insertar_al_final(20)
    lista.insertar_al_inicio(5)
    lista.mostrar()
    lista.eliminar(20)
    lista.mostrar()
    lista.eliminar(5)
    lista.mostrar()
    lista.eliminar(10)
    lista.mostrar()

if __name__ == "__main__":
    main()
```

---

## Verificación de las traducciones

Cada traducción se armó como programa completo (`.frre`) y se corrió con la extensión de pseudocódigo del estudiante (`aed-vscode`), con `npx tsx scripts/aed.ts check <archivo>` y `npx tsx scripts/aed.ts run <archivo> <entradas…>`. Los programas cargan con `LEER` hasta `-1`, igual que el C, y escriben la lista con el mismo formato (`Valor: n`), hacia adelante y, en las dobles, hacia atrás. En las circulares se agregó una línea `[verif]` que comprueba los cierres del círculo (`*ULT.prox = PRIM`, y en la doble también `*PRIM.ant = ULT`). **El código C y Python del repo no se compiló ni se ejecutó**: se analizó leyéndolo.

Todos los `.frre` pasaron el `check` sin diagnósticos.

| Traducción | Entradas probadas | Resultado |
|---|---|---|
| Simple — inserción | vacía (`-1`); un nodo (`7`); `5 3 8 6 10 1 6`: primero en vacía, antes del primero (3 y 1), medio (6), final (8 y 10), repetido (6) | `1 3 5 6 6 8 10`. Correcto. |
| Simple — eliminación | vacía; único nodo (`5`, borrar 5); `3 5 8` borrando el primero, el del medio, el último y uno que no está (9); repetido (`3 5 5 8`, borrar 5) | Vacía → `ERROR - LISTA VACIA`; único → lista vacía; 3 → `5 8`; 5 → `3 8`; 8 → `3 5`; 9 → `SIN EXITO`; repetido → borra uno solo. Correcto. |
| Doble — inserción | las mismas que la simple | Adelante `1 3 5 6 6 8 10`, atrás `10 8 6 6 5 3 1`. Correcto. |
| Doble — eliminación | las mismas que la simple, más `3 8` borrando el último | Todos los casos dan bien hacia adelante y hacia atrás. Correcto. |
| Simple circular — inserción | vacía; un nodo; `5 3` (antes del primero con un solo nodo); `5 8` (después del último con un solo nodo); `5 5`; `5 8 6` (medio); `5 8 8` (igual al último); `5 3 8 6 10 1 6` | Todas ordenadas y con `[verif]` verdadero. **La vacía se cae en la liberación** (`"P" vale NIL`), que reproduce el error del C. |
| Simple circular — eliminación | vacía; único (borrar 5 y borrar 9); `3 5 8` borrando 3, 5, 8 y 9; `3 8` borrando 3 y 8; `3 5 5 8` borrar 5 | Todas las bajas correctas y el círculo cerrado (`[verif]` verdadero). **Vacía y "borrar el único" se caen en la liberación**, como el C. |
| Doble circular — inserción | las mismas que la simple circular | Todas ordenadas en los dos sentidos y con los dos cierres verdaderos. La vacía funciona. Correcto. |
| Doble circular — eliminación (tal cual el C) | vacía; único; `3 5 8` borrando 3, 5, 8 y 9; `3 8` borrar 8 | Vacía, único, primero y medio: correctos. **Borrar el último** (8): la impresión no termina (`3 5 3 5…`, `3 3 3…`) hasta que la extensión corta por ciclo infinito. **Borrar uno que no está** (9): la búsqueda no termina (corte por ciclo infinito). Reproduce los dos errores. |
| Doble circular — eliminación corregida | las mismas, más único borrando uno que no está, `3 8` borrar 3 y `3 5 5 8` borrar 5 | Todas correctas en los dos sentidos y con los cierres verdaderos. |
| Pila | vacía; `7`; `1 2 3` | Vacía; `7`; `3 2 1`. Correcto. |
| Cola | vacía; `7`; `1 2 3` | Vacía; `7`; `1 2 3`. Correcto. |

Además, se corrieron **100 cargas al azar** (de hasta 8 valores entre 0 y 9, con repetidos) sobre las cuatro inserciones ordenadas, comparando con la lista ordenada esperada (y su inversa en las dobles), y **100 bajas al azar** sobre las tres eliminaciones sin errores y la doble circular corregida, comparando con la lista esperada sin el valor borrado: **0 diferencias**.

`Pseudocodigo/LISTA_CIRC` no se ejecutó, porque es código del repo: se analizó leyéndolo.
