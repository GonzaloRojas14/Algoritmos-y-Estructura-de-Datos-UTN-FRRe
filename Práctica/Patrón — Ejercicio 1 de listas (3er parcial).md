---
tipo: apunte
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - parcial
  - listas
  - archivos
---

# Patrón — Ejercicio 1 de listas (3er parcial)

Sale de comparar los tres ejercicios 1 de los modelos del 3er parcial 2025:

| Modelo | Resuelto en |
|---|---|
| Empresa Industrial Multinacional (técnicos) | `EJERCICIO Nº 1.frre` |
| Tema A — HackaTec 2025 | `Parcial 3 Tema A — Ej1 HackaTec.frre` |
| Tema B — Juegos Inter Carrera 2025 | `Parcial 3 Tema B — Ej1 Juegos Inter Carrera.frre` |

Los tres corren en la extensión con los datos de su carpeta `.datos/`.

---

## 1. Qué tienen en común

Los tres son **el mismo ejercicio con otro disfraz**. Siempre hay cuatro piezas:

| Pieza | Empresa | Tema A | Tema B |
|---|---|---|---|
| **Lo que se recorre** (una vez, de punta a punta) | lista simple de INTERVENCIONES | archivo secuencial INSCRIPCIONES | archivo secuencial INSCRIPCIONES |
| **Lo que se consulta** por cada elemento | la secuencia ("uno a uno") y la lista circular de técnicos | archivo indexado PUNTAJES (por id_equipo) | archivo indexado RESULTADOS (por cod_equipo) |
| **Lo que se calcula** | qué técnico se asigna (restricciones en orden de prioridad) | puntaje total = criterios + 1 por tecnología | chances = 5 + 3 por disciplina + premio por posición |
| **Lo que se genera** | lista **doble** ordenada por fecha, ascendente | lista **doble** ordenada por puntaje, ascendente | lista **simple** ordenada por chances, descendente |
| **El informe extra** | cuántas por región (del técnico) → `ARREGLO[1..4]` | cuántos con ≥ 3 tecnologías → contador; top 3 → desde `ULT` hacia atrás | por cada equipo, participaciones y campeonatos → se muestra en el ciclo |

Lo que se repite además:

- **Un vector de 5 dentro del registro** (tecnologías, posiciones por disciplina) o una **cadena de condiciones con prioridad** (restricciones). Se resuelve con un `PARA 1..5` o con SI anidados en el orden que da la consigna.
- **El dato que hace falta no está donde se recorre.** El puntaje no está en la inscripción, el técnico no está en la intervención. Siempre hay que ir a buscarlo a la otra estructura.
- **La consigna deja algo sin decir**: qué pasa si no está en el indexado, cómo "aleatoriza" la secuencia, qué pasa con un empate. Se decide y **se deja escrito como supuesto**.

---

## 2. La receta, paso a paso

### Paso 0 — Inventario (antes de escribir código)

Para cada estructura de la consigna, contestá:

- ¿**La recorro** o **la consulto**? Solo una se recorre: la que tiene "un elemento por cada cosa que hay que procesar".
- ¿Cómo se relacionan? "Correspondencia uno a uno" → avanzan juntas. "Indexado por X" → busco por clave. "Lista circular" → doy vueltas.
- ¿Qué lista **genero**? ¿Simple o doble? ¿Ordenada por qué campo? ¿Ascendente o descendente?
- Cada punto del "Se pide": ¿es **por cada elemento** (va dentro del ciclo) o **al final / en total** (contador o arreglo, se muestra después)?

### Paso 1 — El esqueleto: UN ciclo

```
PRIM := NIL                          // (y ULT := NIL si es doble)
ABRIR E/(principal); ABRIR E/(indexado)
LEER(principal, reg)
MIENTRAS NFDA(principal) HACER
    // 2. traer lo que falta
    // 3. calcular
    // 4. acumular / mostrar lo de "por cada"
    // 5. NUEVO + copiar + insertar ordenado
    LEER(principal, reg)
FIN_MIENTRAS
CERRAR(...)
// 6. informes finales
```

Si lo que se recorre es una lista (Empresa), el ciclo es `p := PRIM` … `MIENTRAS p <> NIL` … `p := *p.prox`.

### Paso 2 — Traer el dato que falta

| Si es… | Se hace así |
|---|---|
| **Indexado** | `reg_x.clave := reg.clave` → `LEER(indexado, reg_x)` → `SI EXISTE ENTONCES … SINO … FIN_SI`. El `SINO` no se olvida: decidí qué hacer si no está. |
| **Secuencia uno a uno** | leer hasta la marca (`MIENTRAS NFDS(sec) Y (v <> '$')`), saltar la marca, leer el carácter que sigue. Quedarse parado al principio del próximo tramo. |
| **Lista circular** | guardar `inicio := T`, recorrer con `REPETIR … HASTA QUE encontrado O (T = inicio)`. Nunca `T <> NIL`: en una circular no hay NIL. |

### Paso 3 — Calcular

- **Vector de 5** → `PARA i := 1 HASTA 5` y adentro un SI por valor.
- **Condiciones con prioridad** → SI anidados **en el orden de la consigna**. La primera que no se cumple corta.
- El total arranca con lo fijo (`chances := 5`, `total := cant_tec`) y se va sumando.

### Paso 4 — Acumular lo que piden

| La consigna dice… | Va… |
|---|---|
| "por cada equipo / intervención" | un `ESCRIBIR` **dentro** del ciclo (Tema B, punto 2) |
| "cuántos cumplen X" | un contador, se muestra al final (Tema A, punto 2) |
| "cuántos por región / categoría" | un `ARREGLO[1..k]` indexado por el código, se muestra al final (Empresa, punto b) |

Ojo con **de quién** es el dato: en Empresa se cuenta por la región **del técnico**, no por la de la intervención.

### Paso 5 — NUEVO, copiar, insertar ordenado

```
NUEVO(Q)
*Q.campo1 := ...            // solo los campos que pide la consigna
```

**Lista simple** (recorrido con ANT y P, filmina 8). Los 4 casos se resumen en 2 ramas:

```
P := PRIM; ANT := NIL
MIENTRAS (P <> NIL) Y (*P.clave < *Q.clave) HACER     // < ascendente, > descendente
    ANT := P; P := *P.prox
FIN_MIENTRAS
SI ANT = NIL ENTONCES PRIM := Q SINO *ANT.prox := Q FIN_SI
*Q.prox := P
```

**Lista doble** (con PRIM y ULT, filmina 8): los 4 casos, cada uno con sus 4 enganches.

```
SI PRIM = NIL ENTONCES                    { 1: vacía }
    PRIM := Q; ULT := Q; *Q.prox := NIL; *Q.ant := NIL
SINO
    P := PRIM
    MIENTRAS (P <> NIL) Y (*P.clave < *Q.clave) HACER P := *P.prox FIN_MIENTRAS
    SI P = PRIM ENTONCES                  { 2: primero }
        *Q.prox := P; *P.ant := Q; *Q.ant := NIL; PRIM := Q
    SINO
        SI P = NIL ENTONCES               { 4: último }
            *Q.ant := ULT; *Q.prox := NIL; *ULT.prox := Q; ULT := Q
        SINO                              { 3: medio }
            *Q.ant := *P.ant; *Q.prox := P; *(*P.ant).prox := Q; *P.ant := Q
        FIN_SI
    FIN_SI
FIN_SI
```

**Desempate** (Tema A): se agrega a la condición del MIENTRAS:
`(*P.total < *Q.total) O ((*P.total = *Q.total) Y (*P.lider < *Q.lider))`.

### Paso 6 — Informes finales

- Mostrar la lista: `P := PRIM; MIENTRAS P <> NIL HACER … P := *P.prox`.
- **Los N mejores**: si la lista quedó de mayor a menor, son los N primeros. Si quedó de menor a mayor y es **doble**, son los N últimos: `P := ULT` y avanzar con `P := *P.ant`. Para eso sirve que sea doble.

### Paso 7 — Escribir los supuestos

Un comentario arriba de la `ACCION` con lo que decidiste donde la consigna no es clara. En los tres modelos hubo que decidir algo:

| Modelo | Qué se decidió |
|---|---|
| Empresa | cómo "aleatoriza" la secuencia (avanzar tantos técnicos como letras tiene la descripción); qué pasa si nadie cumple ("SIN ASIGNAR") |
| Tema A | un equipo sin puntaje no entra a la lista; el empate en total va primero el de menor líder, así queda resuelto el top 3 |
| Tema B | un equipo sin resultados suma solo las 5 chances del evento |

---

## 3. Errores típicos

- Olvidarse el **segundo `LEER`** al final del ciclo: el ciclo no termina.
- Usar el registro del indexado **sin `SI EXISTE`**.
- Mostrar al final lo que pedían "por cada equipo", o al revés.
- Contar por el campo equivocado (región de la intervención en vez de la del técnico).
- Olvidarse `PRIM := NIL` (y `ULT := NIL`) antes del ciclo.
- En la doble, hacer solo 2 de los 4 enganches del caso del medio.
- Recorrer la circular con `MIENTRAS T <> NIL`: no termina nunca.
- Invertir el orden: "de mayor a menor" es `>` en el MIENTRAS de la inserción.

---

## 4. Cómo practicarlo

1. Leé la consigna y completá la tabla del §1 (las cinco filas) **antes** de escribir una línea.
2. Escribí el esqueleto del Paso 1 con los pasos en castellano como comentarios.
3. Rellená cada comentario con la plantilla del Paso 2 al 6.
4. Inventá 5 o 6 datos, incluyendo un caso raro (uno que no está en el indexado, un empate), y hacé la prueba de escritorio o corrélo en la extensión.

Ver también: [[plantillas]] §9 (listas) · [[8 — Listas (Inserción y Eliminación)]] (los 4 casos) · [[plantillas]] §7 (indexado: clave → LEER → SI EXISTE).
