# Errores y trampas — AED UTN-FRRe

Dos secciones: errores del alumno (repo `Practica/`) y bugs encontrados **en las fuentes de referencia**, que se copian sin querer.

---

## A. Errores propios recurrentes

### Secuencias

| # | Error | Cómo se rompe | Visto en |
|---|---|---|---|
| 1 | Falta el `AVZ` que **supera el delimitador** | el ciclo siguiente arranca parado en `&` y no entra nunca, o entra infinitamente | patrón general |
| 2 | Ciclo interno sin guarda `NFDS` | si la cinta se acaba sin el delimitador, ciclo infinito | varios |
| 3 | Barrido de blancos con `<>` en vez de `=` | `MIENTRAS (v <> " ")` barre la palabra, no los blancos | ver §B.3 |
| 4 | Barrido de palabra con `O` en vez de `Y` | `(v <> " ") O (v <> "#")` es siempre verdadero → infinito | ver §B.3 |
| 5 | Máximo/contador inicializado en el nivel equivocado | se pisa en cada vuelta, o arrastra el valor del grupo anterior | `Parcial.1.txt` |
| 6 | Condición que no es booleana: `Y v + 'm'` | debía ser `Y v = "M"` | `2.1.18.txt` |

### Archivos

| # | Error | Cómo se rompe | Visto en |
|---|---|---|---|
| 7 | Falta el `LEER` al final del ciclo | ciclo infinito sobre el mismo registro | patrón general |
| 8 | Falta la rama de "no existe" en indexado | la consigna pedía dar de alta y no se hace | `2.3.frre` |
| 9 | Variable de corte del `REPETIR` nunca leída | `HASTA QUE (resp = 'n')` con `resp` sin asignar | `2.3.frre` |
| 10 | Nombres de campo que no coinciden con la declaración | `cant_punt` declarado, `cant_puntos` usado | `2.3.frre` |
| 11 | Falta `CERRAR` de alguna secuencia o archivo | pérdida de datos del buffer | varios |
| 12 | `FECHA` declarada `dia, mes, anio` y comparada como registro entero | la comparación da mal; va `anio, mes, dia` | `Parcial.1.txt` |

### Lógica general

| # | Error | Visto en |
|---|---|---|
| 13 | Contador declarado, inicializado y nunca incrementado | `2.3.frre` |
| 14 | Variable usada en un cálculo sin haberla leído nunca | `1.1.5.1.txt` (`c`) |
| 15 | Porcentaje mal convertido: `0.4` para 4% (va `0.04`) | `1.1.5.1.txt` |
| 16 | Resta invertida: `anio_nac - anio` | `1.9.txt` |
| 17 | Cascada de `SI` que no cubre empates ni tiene `SINO` final | `1.7.txt` |
| 18 | `>` donde correspondía `>=` en un umbral | `2.3.frre` |
| 19 | Dividir sin verificar divisor > 0 | evitado bien en `2.1.15.txt` |
| 20 | **No resolver todos los incisos de la consigna** | `2.3.frre`, `Parcial.1.txt` |

### Notación

| # | Error | Correcto |
|---|---|---|
| 21 | `NOFDA` | `NFDA` o `NoFDA` |
| 22 | `PROCESSO` / `FIN_PROCESSO` | `Proceso`, y **no lleva** `FIN_PROCESO` |
| 23 | `REESCRIBIR` | `RE-ESCRIBIR` |
| 24 | `SI ... ENTONCES:` con dos puntos | sin dos puntos |
| 25 | `SEC DE CARACTER` | `SECUENCIA de caracter` |
| 26 | Nombre de acción con puntos: `ACCION 2.2.4 ES` | `ACCION ej_2_2_4 ES` |
| 27 | `PARA i := 1 HASTA 10 HACER` cuando el paso no es 1 | `PARA i := 20 HASTA -20, -2 HACER` |

### Listas con punteros

| # | Error | Cómo se rompe | Visto en |
|---|---|---|---|
| 28 | Avanzar con `p := *p.dato` en vez de `p := *p.prox` | `p` recibe un dato, no una dirección: el recorrido se rompe en el primer paso | tus notas, `Clase 5 Listas.frre` |
| 29 | Recorrido sin `p := *p.prox` | ciclo infinito sobre el primer nodo | patrón general |
| 30 | `p.dato` sin asterisco | `p` es un puntero, no un registro: va `*p.dato` | patrón general |
| 31 | Usar `*p` con `p = NIL`, o un nodo después de `DISPONER(p)` | no hay nodo: error | patrón general |
| 32 | Circular recorrida con `MIENTRAS p <> NIL` | en una circular nunca aparece `NIL`: ciclo infinito | patrón general |
| 33 | Circular: el ciclo `MIENTRAS *T.SIG <> PRIMERO` y olvidarse del último | el último nodo no se lista ni se compara | patrón general |
| 34 | Cola: desencolar el último sin poner `ULT := NIL` | `ULT` queda apuntando a un nodo liberado | patrón general |
| 35 | `a` (anterior) que no vuelve a `NIL` en cada inserción o eliminación | arrastra el anterior de la vuelta pasada y engancha mal | carga ordenada de la guía, si se repite |

### Recursividad

| # | Error | Cómo se rompe | Visto en |
|---|---|---|---|
| 36 | Sin caso base, o con una llamada que no se acerca a él | llamadas infinitas (la extensión corta a las 10000) | patrón general |
| 37 | Caso base y caso recursivo con condiciones distintas | `> 6` en uno y `>= 6` en el otro: un 6 cuenta según en qué posición esté | promedio de aprobados de clase |
| 38 | Parámetro `n` y constante `N` en la misma función | no se distinguen mayúsculas: `n` tapa a `N` | `Recursividad — prueba de escritorio.frre` |
| 39 | Función recursiva llamada como instrucción suelta | el resultado se pierde: va en una expresión o asignado | patrón general |
| 40 | Una rama del `SI` que no asigna el resultado al nombre de la función | la función devuelve el valor por defecto en ese caso | patrón general |
| 41 | "Promedio" que divide por el total cuando solo se sumaron algunos | `Promedio_Aprobados` de clase da suma de aprobados / 10, no el promedio de los aprobados | promedio de aprobados de clase |

---

## B. Bugs en las fuentes de referencia

**Importante**: estos archivos circulan como material de estudio y tienen errores. No copiarlos a ciegas.

### B.1 — Corte de control: llamar al corte equivocado al final

En `AED26_Guia_Ejercicios/Resueltos/TP2/3_Corte de Control/Ejercicio_2.2.11.frre.txt`, después del `MIENTRAS` se llama a `corte_carr`, que es el corte **menor**.

```
        FIN_MIENTRAS
        corte_carr            // ✗ es el corte MENOR
        emitir_totales
```

Consecuencia: nunca se emiten los totales del último género ni se acumulan al total general, así que `emitir_totales` imprime de menos. Debe ser `corte_gen` (el mayor), que cascadea hacia abajo llamando a `corte_carr` solo.

### B.2 — Corte de control: condición del filtro negada

En el mismo archivo:

```
        PROCEDIMIENTO tratar_registro ES
            SI (alu.fecha_ing.anio <> 2009) ENTONCES     // ✗ cuenta los que NO son de 2009
```

La consigna pide los que ingresaron **en** 2009. Va `= 2009`.

### B.3 — Secuencias: barridos invertidos

En `AED26_Guia_Ejercicios/Resueltos/Parciales/Parcial 1/Parcial 2025 Tema A - Feria del libro.frre.txt` (archivo marcado como corregido por profesores):

```
                    //barrido de blancos:
                    MIENTRAS (lib <> " ") HACER          // ✗ debe ser (lib = " ")
                        AVZ(sec_lib, lib)
                    FIN_MIENTRAS

                    //barrido de palabra:
                    MIENTRAS ((lib <> " ") O (lib <> "#")) HACER   // ✗ debe ser Y
                        AVZ(sec_lib, lib)
                    FIN_MIENTRAS
```

El segundo es el error más grave: `(x <> " ") O (x <> "#")` es **siempre verdadero** para cualquier carácter, así que el ciclo no termina nunca.

Lo que sí hay que copiar de ese archivo: el idioma de acumulación de dígitos y el patrón de `flag`.

```
        cant_pag := 0
        PARA i := 1 HASTA 3 HACER
            cant_pag := cant_pag * 10 + car_ent(lib)     // ✓ limpio y correcto
            AVZ(sec_lib, lib)
        FIN_PARA
```

### B.4 — Actualización por lotes: falta consumir el movimiento de alta

En `isi-aed/Pseudocodigo/ACTUALIZACION INC LOTE [TEMPLATE].txt`, la rama de alta carga `aux_mae` desde `reg_mov` y llama directo a `LOTE`:

```
            SINO
                aux_mae.clave := reg_mov.clave
                ...
                LOTE;                    // ✗ falta LEER_arch_mov antes
```

Como `LOTE` arranca con `MIENTRAS (aux_mae.clave = reg_mov.clave)`, la primera vuelta reprocesa el **mismo** movimiento de alta a través de `IGUALES`, que imprime "ERROR - ALTA". Hay que leer el siguiente movimiento antes de entrar al lote.

La versión de `AED26_Guia_Ejercicios/Resueltos/TP2/5_Actualizacion/Actualizacion_Lotes.frre.txt` sí lo hace bien.

### B.5 — Plantillas a medio adaptar

`AED26_Guia_Ejercicios/Resueltos/TP2/3_Corte de Control/Parcial_2023_ej_Corte_cad_supermercado.frre.txt` está resuelto hasta la mitad: de `C2_Sucursal` en adelante quedó el texto de la plantilla sin adaptar, con variables que no existen (`cont1`, `Resg1`, `r.clave1`, `corte_1`, `arch`). No sirve como ejemplo completo de nada más que el primer corte.

Lo mismo con `Plantilla_Corte_Control.frre.txt`, que tiene un typo: `conT := contT + cont3` (falta una `t` en el destino).

### B.6 — Actualización unitaria: el alta pisa el registro del maestro

La rama de alta de `plantillas.md` §5 (y la plantilla de cátedra de la que salió) armaba el
registro nuevo **encima de `reg_mae`**:

```
                SINO
                    reg_mae.clave  := reg_mov.clave      // ✗
                    reg_mae.campo1 := reg_mov.campo1
                    ESCRIBIR(arch_mae_act, reg_mae)
```

A la rama de alta se llega cuando `reg_mae.clave > reg_mov.clave`. O sea: `reg_mae` **tiene un
registro del maestro, válido y sin procesar** — perdió la comparación justamente por eso.
Pisarlo lo destruye. Y como en esa rama solo avanza `leer_mov`, el `reg_mae` corrupto sobrevive
a la vuelta siguiente y se compara como si fuera real.

Verificado ejecutando el ejercicio 2.2.19 con 6 registros de maestro y 6 movimientos: un
registro se grabó dos veces, otro quedó con la cantidad del movimiento en lugar de la suya, y
un tercero desapareció del maestro nuevo.

La solución es un registro aparte (`reg_mae_act : mae`) para armar las altas. `reg_mae` se toca
solo para leerlo y para la modificación, donde sí corresponde porque ahí el registro **es** el
que se está tratando.

La plantilla de **lotes** (§6) no tiene el problema: ya usa `aux_mae` para armar todo. El
auxiliar estaba por otro motivo —acumular varios movimientos sobre la misma clave— pero de paso
la protege de esto.

Es el mismo patrón que el `i` global pisado por `busqueda` en el parcial resuelto en clase: una
variable compartida que alguien sobreescribe mientras otro todavía la necesita.

### B.7 — Errores menores dispersos

- `Ejercicio_6.frre` (secuencias): `CERRAR("sec_hab")` con comillas — es un identificador, no un string. Además declara `sec_hab : secuencia de caracter` pero le avanza enteros, y usa `prov` como índice del `PARA` sin declararla.
- `Ejercicio_13.frre`: declara `cont_alg`/`cont_pal` y al imprimir usa `cant_alg`/`cant_pal`.
- `ACT INDEX BAJA FIS [TEMPLATE].txt`: `RE-ESCRIBIR(arch_mae_act, reg_mae)` sobre un archivo que nunca se declaró ni abrió; debe ser `arch_mae`.
- `Ejercicio No Secuencial ILSE`: la función `multi_11_alt` asigna a `multi_11` (otro nombre) y no inicializa `sum`.

### B.8 — Guía 2026: listas

- **Teoría de listas** (`Guía de Cátedra/Teoría/Listas.md`): tres asignaciones escritas con `=` en vez de `:=`: `p = *p.prox` (búsqueda), `Prim = p` (carga encolada) y `Prim = *q.prox` (eliminación). Con `=` es una comparación, no asigna nada.
- **Complementos, `LISTA_CIRCULAR`** (p. 63): usa `ANT` en la eliminación sin declararlo en el Ambiente.
- **Complementos, `LISTA_DOBLE`** (p. 64): declara el campo `ant` con un tipo `punt` que no está definido, y le falta un `Fsi`.

Los tres algoritmos corren corregidos en `aed-vscode/test/fixtures/` (`guia_lista_circular.frre`, `guia_lista_doble.frre`), con la corrección comentada.

---

## C. Trampas conceptuales

| Trampa | Qué hay que saber |
|---|---|
| Confundir la clave más fina con un nivel de corte | El identificador único (`nro_legajo`, `cod_articulo`) **no genera corte**: no hay nada que totalizar dentro de él |
| Mezclar mezcla inclusiva con exclusiva | `O` + `HV` + sin vaciado, **o** `Y` + sin `HV` + dos vaciados. Nunca cruzadas |
| Recorrer un indexado con `NFDA` | El indexado se accede por clave; el recorrido secuencial es de archivos secuenciales |
| `RE-ESCRIBIR` sin `LEER` previo | Error de lógica: no hay posición física sobre la cual sobreescribir |
| Alta con `RE-ESCRIBIR` o modificación con `ESCRIBIR` | Alta = `ESCRIBIR`, modificación = `RE-ESCRIBIR`. Son distintos |
| Cargar el archivo de salida desde `r` en un corte | En el momento del corte `r` ya avanzó al registro del grupo siguiente. Se carga desde los **resguardos** |
| Inicializar antes de leer el primer registro en corte | Los resguardos necesitan el primer registro: `LEER` va antes de `inicializar` |
| Consistencia vs. congruencia | Consistencia = campo válido en sí mismo (aislado). Congruencia = datos coherentes entre sí (relacional). Si no es consistente, no puede ser congruente; si es consistente, todavía puede ser incongruente |
| Lista enlazada vs. arreglo | El arreglo tiene tamaño fijo y acceso directo por índice; la lista crece nodo a nodo y se recorre desde `PRIM`. Insertar en el medio de una lista solo mueve punteros |
| Copiar un puntero no copia el nodo | `q := p` deja **dos punteros al mismo nodo**: cambiar `*q.dato` cambia `*p.dato` |
| Carga apilada vs. encolada | Apilada: cada nuevo queda primero y la lista sale **al revés** de la lectura. Encolada: queda último y sale **en orden** |
| Recursión: bajada y subida | Lo que va antes de la llamada se ejecuta al bajar; lo que va después, al subir. Por eso `Binario` llama primero y escribe después |
| Recursividad vs. iteración | La recursiva usa más memoria (una llamada pendiente por nivel). La cátedra pide usarla cuando el problema es naturalmente recursivo |
