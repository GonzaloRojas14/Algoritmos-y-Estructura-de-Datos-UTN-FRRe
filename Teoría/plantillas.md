# Plantillas canónicas — AED UTN-FRRe

Estructuras fijas. Se copian y se adaptan; **no se reinventan**. Provienen de `isi-aed/Pseudocodigo/` (cátedra), normalizadas a la notación moderna.

Índice: [Secuencial](#1-recorrido-de-archivo-secuencial) · [Corte de control](#2-corte-de-control) · [Mezcla INC](#3-mezcla-inclusiva-con-hv) · [Mezcla EXC](#4-mezcla-exclusiva-con-vaciado) · [Actualización unitaria](#5-actualización-unitaria-inclusiva) · [Actualización lote](#6-actualización-por-lotes) · [ABM indexado](#7-actualización-indexada-abm-interactivo) · [Secuencias](#8-secuencias) · [Listas](#9-listas-con-punteros) · [Recursividad](#10-recursividad)

---

## 1. Recorrido de archivo secuencial

```
ACCION recorrido ES
    Ambiente
        reg = REGISTRO
            campo1 : ...
        FIN_REGISTRO
        arch : ARCHIVO de reg
        r : reg
    Proceso
        ABRIR E/(arch)
        LEER(arch, r)
        MIENTRAS NFDA(arch) HACER
            // tratar r
            LEER(arch, r)
        FIN_MIENTRAS
        CERRAR(arch)
FIN_ACCION
```

Con archivo de salida: agregar `ABRIR /S(arch_sal)` y `ESCRIBIR(arch_sal, r_sal)` dentro del ciclo, y su `CERRAR`.

---

## 2. Corte de control

**Precondición: el archivo tiene que estar ordenado por las claves de corte, de mayor a menor jerarquía.**

Un nivel de corte por cada nivel de totalización que pida la consigna. El ejemplo tiene 3 (`clave1` mayor → `clave3` menor).

```
ACCION archivo_corte ES
    Ambiente
        reg = REGISTRO
            clave1 : AN(50)      // corte mayor
            clave2 : entero      // corte intermedio
            clave3 : entero      // corte menor
            campo1 : entero
        FIN_REGISTRO

        arch : ARCHIVO de reg ordenado por clave1, clave2 y clave3
        r : reg

        // un resguardo por cada nivel de corte (NO por la clave más fina)
        resg_clave1 : AN(50)
        resg_clave2 : entero
        resg_clave3 : entero

        // un "set" de acumuladores por cada cosa que pida la consigna:
        // uno por nivel + uno general
        acum3, acum2, acum1, acumT : entero

        PROCEDIMIENTO inicializar ES
            acumT := 0; acum1 := 0; acum2 := 0; acum3 := 0
            resg_clave1 := r.clave1
            resg_clave2 := r.clave2
            resg_clave3 := r.clave3
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO tratar_registro ES
            // lo que se hace con UN registro
            acum3 := acum3 + 1
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO emitir_totales ES
            ESCRIBIR("Total general: ", acumT)
        FIN_PROCEDIMIENTO

        // ── CORTE MENOR: no llama a nadie ──
        PROCEDIMIENTO corte_clave3 ES
            ESCRIBIR("Total de ", resg_clave3, ": ", acum3)   // 1. emitir
            acum2 := acum2 + acum3                            // 2. acumular arriba
            // 3. escribir archivo de salida (ver NOTA)
            acum3 := 0                                        // 4. poner en cero
            resg_clave3 := r.clave3                           // 5. re-resguardar
        FIN_PROCEDIMIENTO

        // ── CORTE INTERMEDIO ──
        PROCEDIMIENTO corte_clave2 ES
            corte_clave3                                      // 0. llamar al inferior
            ESCRIBIR("Total de ", resg_clave2, ": ", acum2)
            acum1 := acum1 + acum2
            acum2 := 0
            resg_clave2 := r.clave2
        FIN_PROCEDIMIENTO

        // ── CORTE MAYOR ──
        PROCEDIMIENTO corte_clave1 ES
            corte_clave2
            ESCRIBIR("Total de ", resg_clave1, ": ", acum1)
            acumT := acumT + acum1
            acum1 := 0
            resg_clave1 := r.clave1
        FIN_PROCEDIMIENTO

        // ── ELECCIÓN DE CORTE: de MAYOR a MENOR jerarquía ──
        PROCEDIMIENTO tratar_corte ES
            SI (r.clave1 <> resg_clave1) ENTONCES
                corte_clave1
            SINO
                SI (r.clave2 <> resg_clave2) ENTONCES
                    corte_clave2
                SINO
                    SI (r.clave3 <> resg_clave3) ENTONCES
                        corte_clave3
                    FIN_SI
                FIN_SI
            FIN_SI
        FIN_PROCEDIMIENTO

    Proceso
        ABRIR E/(arch)
        LEER(arch, r)          // ← el LEER va ANTES de inicializar
        inicializar            //   porque los resguardos toman el 1er registro

        MIENTRAS NFDA(arch) HACER
            tratar_corte
            tratar_registro
            LEER(arch, r)      // MUY IMPORTANTE
        FIN_MIENTRAS

        corte_clave1           // ← corte de MAYOR jerarquía; cascadea hacia abajo
        emitir_totales
        CERRAR(arch)
FIN_ACCION
```

### Reglas que no se negocian

1. **El orden dentro de `corte_N` es fijo**: llamar al inferior → emitir → acumular arriba → poner en cero lo propio → re-resguardar la clave.
2. El **corte menor no llama a nadie**. Todos los demás llaman al inmediato inferior, **como primera línea**.
3. `tratar_corte` pregunta **de mayor a menor**, con `SINO` anidados: si cortó el nivel alto, la cascada ya cubre los bajos.
4. Después del `MIENTRAS` se llama al corte de **mayor** jerarquía, no al menor.
5. `LEER` primero, `inicializar` después. Sin el primer registro no hay resguardo posible.
6. La clave más fina del archivo (`clave0`, el identificador único) **no genera corte**: no hay nada que totalizar dentro de ella.

### NOTA sobre archivo de salida

Si la consigna pide generar un archivo con totales, el `ESCRIBIR(arch_sal, reg_sal)` va **en el corte cuyo nivel coincide con el campo más fino del registro de salida**. Se carga desde las variables de **resguardo**, no desde `r` (que ya avanzó al registro siguiente).

```
// dentro de corte_clave2, si la salida es (clave1, clave2, total)
reg_sal.c1 := resg_clave1
reg_sal.c2 := resg_clave2
reg_sal.total := acum2
ESCRIBIR(arch_sal, reg_sal)
```

---

## 3. Mezcla inclusiva (con HV)

Dos archivos ordenados por la misma clave. **Los dos se agotan.** No hay ciclos de vaciado.

```
ACCION mezcla_inc ES
    Ambiente
        HV = 99999999

        ejemplo = REGISTRO
            clave  : entero
            campo1 : AN(50)
        FIN_REGISTRO

        reg1, reg2 : ejemplo
        arch1, arch2 : ARCHIVO de ejemplo

        PROCEDIMIENTO leer_arch1 ES
            LEER(arch1, reg1)
            SI FDA(arch1) ENTONCES
                reg1.clave := HV
            FIN_SI
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO leer_arch2 ES
            LEER(arch2, reg2)
            SI FDA(arch2) ENTONCES
                reg2.clave := HV
            FIN_SI
        FIN_PROCEDIMIENTO

    Proceso
        ABRIR E/(arch1); ABRIR E/(arch2)
        leer_arch1; leer_arch2

        MIENTRAS (reg1.clave <> HV) O (reg2.clave <> HV) HACER
            SI (reg1.clave < reg2.clave) ENTONCES
                // acciones archivo 1
                leer_arch1
            SINO
                SI (reg1.clave = reg2.clave) ENTONCES
                    // acciones archivo 1
                    leer_arch1
                    // acciones archivo 2
                    leer_arch2
                SINO
                    // acciones archivo 2
                    leer_arch2
                FIN_SI
            FIN_SI
        FIN_MIENTRAS

        CERRAR(arch1); CERRAR(arch2)
FIN_ACCION
```

`HV` (high value) es un valor mayor que cualquier clave real. Al agotarse un archivo su clave pasa a `HV`, así el otro siempre gana la comparación y termina de volcarse solo.

---

## 4. Mezcla exclusiva (con vaciado)

Sin centinela. El ciclo principal corre **mientras haya en los dos**, y después hay que vaciar el que sobró.

```
    Proceso
        ABRIR E/(arch1); ABRIR E/(arch2)
        LEER(arch1, reg1); LEER(arch2, reg2)

        MIENTRAS NFDA(arch1) Y NFDA(arch2) HACER
            SI (reg1.clave < reg2.clave) ENTONCES
                // acciones archivo 1
                LEER(arch1, reg1)
            SINO
                SI (reg1.clave = reg2.clave) ENTONCES
                    // acciones archivo 1
                    LEER(arch1, reg1)
                    // acciones archivo 2
                    LEER(arch2, reg2)
                SINO
                    // acciones archivo 2
                    LEER(arch2, reg2)
                FIN_SI
            FIN_SI
        FIN_MIENTRAS

        // ── CICLOS DE VACIADO: obligatorios, uno por archivo ──
        MIENTRAS NFDA(arch1) HACER
            // acciones archivo 1
            LEER(arch1, reg1)
        FIN_MIENTRAS

        MIENTRAS NFDA(arch2) HACER
            // acciones archivo 2
            LEER(arch2, reg2)
        FIN_MIENTRAS

        CERRAR(arch1); CERRAR(arch2)
FIN_ACCION
```

**Inclusiva vs. exclusiva**: `O` + `HV` + sin vaciado, contra `Y` + sin `HV` + dos vaciados. Elegir una y ser consistente; mezclarlas es el error clásico.

---

## 5. Actualización unitaria (inclusiva)

Maestro + movimientos, **un movimiento como máximo por clave**. Genera un maestro nuevo.

```
ACCION act_unitaria ES
    Ambiente
        HV = 99999999

        mae = REGISTRO
            clave  : entero
            campo1 : AN(50)
            campo4 : real
            Baja   : caracter
        FIN_REGISTRO

        mov = REGISTRO
            clave   : entero
            campo1  : AN(50)
            campo4  : real
            TipoMov : ('A','B','M')
        FIN_REGISTRO

        reg_mae : mae
        reg_mae_act : mae          // para armar las altas, sin pisar reg_mae
        arch_mae, arch_mae_act : ARCHIVO de mae
        reg_mov : mov
        arch_mov : ARCHIVO de mov

        PROCEDIMIENTO leer_mae ES
            LEER(arch_mae, reg_mae)
            SI FDA(arch_mae) ENTONCES
                reg_mae.clave := HV
            FIN_SI
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO leer_mov ES
            LEER(arch_mov, reg_mov)
            SI FDA(arch_mov) ENTONCES
                reg_mov.clave := HV
            FIN_SI
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO paso_directo ES
            ESCRIBIR(arch_mae_act, reg_mae)
        FIN_PROCEDIMIENTO

        // claves IGUALES → el registro existe → baja o modificación
        PROCEDIMIENTO iguales ES
            SI (reg_mov.TipoMov = 'A') ENTONCES
                ESCRIBIR("ERROR - ALTA de registro existente")
            SINO
                SI (reg_mov.TipoMov = 'B') ENTONCES
                    reg_mae.Baja := '*'
                    ESCRIBIR(arch_mae_act, reg_mae)
                SINO
                    // modificación: solo los campos que vienen con dato
                    SI (reg_mov.campo1 <> "") ENTONCES
                        reg_mae.campo1 := reg_mov.campo1
                    FIN_SI
                    SI (reg_mov.campo4 <> 0) ENTONCES
                        reg_mae.campo4 := reg_mov.campo4
                    FIN_SI
                    ESCRIBIR(arch_mae_act, reg_mae)
                FIN_SI
            FIN_SI
        FIN_PROCEDIMIENTO

        // claves DISTINTAS (mov < mae) → el registro no existe → alta
        PROCEDIMIENTO distintos ES
            SI (reg_mov.TipoMov = 'B') ENTONCES
                ESCRIBIR("ERROR - BAJA de registro inexistente")
            SINO
                SI (reg_mov.TipoMov = 'M') ENTONCES
                    ESCRIBIR("ERROR - MODIFICACION de registro inexistente")
                SINO
                    // alta: campo por campo, los formatos son distintos.
                    // OJO: va en reg_mae_act, NO en reg_mae. En esta rama reg_mae
                    // tiene un registro del maestro sin procesar (por eso perdió
                    // la comparación) y pisarlo lo destruye. Ver errores-y-trampas B.6.
                    reg_mae_act.clave  := reg_mov.clave
                    reg_mae_act.campo1 := reg_mov.campo1
                    reg_mae_act.campo4 := reg_mov.campo4
                    reg_mae_act.Baja   := '-'
                    ESCRIBIR(arch_mae_act, reg_mae_act)
                FIN_SI
            FIN_SI
        FIN_PROCEDIMIENTO

    Proceso
        ABRIR E/(arch_mae); ABRIR E/(arch_mov)
        ABRIR /S(arch_mae_act)
        leer_mae; leer_mov

        MIENTRAS (reg_mae.clave <> HV) O (reg_mov.clave <> HV) HACER
            SI (reg_mae.clave < reg_mov.clave) ENTONCES
                paso_directo                 // maestro sin movimiento
                leer_mae
            SINO
                SI (reg_mae.clave = reg_mov.clave) ENTONCES
                    iguales
                    leer_mae
                    leer_mov
                SINO
                    distintos                // movimiento sin maestro
                    leer_mov
                FIN_SI
            FIN_SI
        FIN_MIENTRAS

        CERRAR(arch_mae); CERRAR(arch_mov); CERRAR(arch_mae_act)
FIN_ACCION
```

**Las tres ramas y qué significan:**

| Comparación | Situación | Acción |
|---|---|---|
| `mae < mov` | maestro sin movimiento | paso directo, leer maestro |
| `mae = mov` | el registro existe | baja o modificación; error si es alta. Leer **los dos** |
| `mae > mov` | movimiento sin maestro | alta; error si es baja o modificación. Leer **solo movimiento** |

---

## 6. Actualización por lotes

Igual que la unitaria, pero **puede haber varios movimientos para la misma clave**. Se acumulan sobre un registro auxiliar `aux` y se graba **una sola vez** al final del lote.

```
        aux_mae, reg_mae : mae

        // aplica UN movimiento sobre aux (no graba)
        PROCEDIMIENTO iguales ES
            SI (reg_mov.TipoMov = 'A') ENTONCES
                ESCRIBIR("ERROR - ALTA de registro existente")
            SINO
                SI (reg_mov.TipoMov = 'B') ENTONCES
                    aux_mae.Baja := '*'
                SINO
                    SI (reg_mov.campo1 <> "") ENTONCES
                        aux_mae.campo1 := reg_mov.campo1
                    FIN_SI
                    SI (reg_mov.campo4 <> 0) ENTONCES
                        aux_mae.campo4 := reg_mov.campo4
                    FIN_SI
                FIN_SI
            FIN_SI
        FIN_PROCEDIMIENTO

        // consume TODOS los movimientos de la misma clave y graba una vez
        PROCEDIMIENTO lote ES
            MIENTRAS (aux_mae.clave = reg_mov.clave) HACER
                iguales
                leer_mov
            FIN_MIENTRAS
            ESCRIBIR(arch_mae_act, aux_mae)
        FIN_PROCEDIMIENTO

    Proceso
        ABRIR E/(arch_mae); ABRIR E/(arch_mov)
        ABRIR /S(arch_mae_act)
        leer_mae; leer_mov

        MIENTRAS (reg_mae.clave <> HV) O (reg_mov.clave <> HV) HACER
            SI (reg_mae.clave < reg_mov.clave) ENTONCES
                paso_directo
                leer_mae
            SINO
                SI (reg_mae.clave = reg_mov.clave) ENTONCES
                    aux_mae := reg_mae       // copio el maestro al auxiliar
                    lote
                    leer_mae
                SINO
                    // ALTA: cargo aux desde el movimiento
                    aux_mae.clave  := reg_mov.clave
                    aux_mae.campo1 := reg_mov.campo1
                    aux_mae.campo4 := reg_mov.campo4
                    aux_mae.Baja   := '-'
                    leer_mov                 // ← consumir el 'A' ANTES de entrar al lote
                    lote                     //   si no, el lote lo reprocesa como error
                FIN_SI
            FIN_SI
        FIN_MIENTRAS

        CERRAR(arch_mae); CERRAR(arch_mov); CERRAR(arch_mae_act)
FIN_ACCION
```

> El `leer_mov` antes de `lote` en la rama de alta es imprescindible. La plantilla oficial de cátedra lo omite y eso hace que el propio movimiento de alta se reprocese dentro de `lote`, disparando "ERROR - ALTA".

---

## 7. Actualización indexada (ABM interactivo)

Acceso puntual por clave, en tiempo real, sobre el maestro (**in situ**, sin archivo intermedio).

```
ACCION act_indexada ES
    Ambiente
        mae = REGISTRO
            clave  : entero
            campo1 : AN(50)
            campo4 : real
            Baja   : caracter
        FIN_REGISTRO

        reg_mae : mae
        arch_mae : ARCHIVO de mae INDEXADO por clave

        campo1 : AN(50)              // auxiliares para leer del teclado
        campo4 : real
        op, acc : caracter

        PROCEDIMIENTO alta ES
            ESCRIBIR("Ingrese clave")
            LEER(reg_mae.clave)
            LEER(arch_mae, reg_mae)
            SI EXISTE ENTONCES
                ESCRIBIR("ERROR, EL REGISTRO YA EXISTE")
            SINO
                ESCRIBIR("Ingrese campo1: "); LEER(reg_mae.campo1)
                ESCRIBIR("Ingrese campo4: "); LEER(reg_mae.campo4)
                reg_mae.Baja := '-'
                ESCRIBIR(arch_mae, reg_mae)          // ← alta = ESCRIBIR
            FIN_SI
        FIN_PROCEDIMIENTO

        PROCEDIMIENTO modif_baja(TipoMov : caracter) ES
            ESCRIBIR("Ingrese clave")
            LEER(reg_mae.clave)
            LEER(arch_mae, reg_mae)
            SI EXISTE ENTONCES
                SI (TipoMov = 'B') ENTONCES
                    reg_mae.Baja := '*'              // baja LÓGICA
                SINO
                    ESCRIBIR("Ingrese campo1: "); LEER(campo1)
                    SI (campo1 <> "") ENTONCES       // vacío = no modificar
                        reg_mae.campo1 := campo1
                    FIN_SI
                    ESCRIBIR("Ingrese campo4: "); LEER(campo4)
                    SI (campo4 <> 0) ENTONCES
                        reg_mae.campo4 := campo4
                    FIN_SI
                FIN_SI
                RE-ESCRIBIR(arch_mae, reg_mae)       // ← modificación = RE-ESCRIBIR
            SINO
                ESCRIBIR("ERROR, EL REGISTRO NO EXISTE")
            FIN_SI
        FIN_PROCEDIMIENTO

    Proceso
        ABRIR E/S(arch_mae)

        ESCRIBIR("Desea continuar? S/N"); LEER(op)

        MIENTRAS (op = 'S') HACER
            ESCRIBIR("Ingrese accion A/B/M"); LEER(acc)
            SEGUN acc HACER
                'A'      : alta
                'B', 'M' : modif_baja(acc)
                otros    : ESCRIBIR("Accion INCORRECTA")
            FIN_SEGUN
            ESCRIBIR("Desea continuar? S/N"); LEER(op)
        FIN_MIENTRAS

        CERRAR(arch_mae)
FIN_ACCION
```

**Baja física** — el registro se borra de verdad; el registro no necesita campo marca:

```
        PROCEDIMIENTO baja ES
            ESCRIBIR("Ingrese clave")
            LEER(reg_mae.clave)
            LEER(arch_mae, reg_mae)
            SI EXISTE ENTONCES
                ELIMINAR(arch_mae, reg_mae)
            SINO
                ESCRIBIR("ERROR, EL REGISTRO NO EXISTE")
            FIN_SI
        FIN_PROCEDIMIENTO
```

**Secuencia obligatoria de toda operación indexada**: asignar clave → `LEER` → `SI EXISTE` → operar. `RE-ESCRIBIR` sin `LEER` previo es error de lógica.

---

## 8. Secuencias

**Pura** (cantidad conocida):

```
    Proceso
        ARR(sec); AVZ(sec, v)
        PARA i := 1 HASTA 23 HACER
            // tratar v, avanzando lo que corresponda
            AVZ(sec, v)
        FIN_PARA
        CERRAR(sec)
```

**Indefinida con marca de fin propia**:

```
    Proceso
        ARR(sec); AVZ(sec, v)
        CREAR(sal)
        MIENTRAS (v <> "*") HACER
            ...
            AVZ(sec, v)
        FIN_MIENTRAS
        CERRAR(sec); CERRAR(sal)
```

**Indefinida impura con palabras** (barrido de blancos + barrido de palabra):

```
    Proceso
        ARR(sec); AVZ(sec, v)
        MIENTRAS NFDS(sec) HACER
            MIENTRAS (v = " ") HACER          // barrer blancos
                AVZ(sec, v)
            FIN_MIENTRAS
            cont_pal := cont_pal + 1
            MIENTRAS (v <> " ") Y NFDS(sec) HACER   // barrer la palabra
                AVZ(sec, v)
            FIN_MIENTRAS
        FIN_MIENTRAS
        CERRAR(sec)
```

**Dos secuencias en paralelo** (una de "cabecera" y otra de "detalle"): cada una tiene su propia ventana y avanza por su cuenta. El ciclo externo lo maneja la de cabecera; el interno consume el detalle hasta su delimitador.

```
        ARR(sec_cab); AVZ(sec_cab, c)
        ARR(sec_det); AVZ(sec_det, d)
        MIENTRAS NFDS(sec_cab) HACER
            MIENTRAS (d <> "@") HACER         // detalle de esta cabecera
                ...
                AVZ(sec_det, d)
            FIN_MIENTRAS
            AVZ(sec_det, d)                   // superar el "@"
            // ahora procesar la cabecera
            ...
        FIN_MIENTRAS
```

---

## 9. Listas con punteros

Salen de la teoría de listas de la guía (`Guía de Cátedra/Teoría/Listas.md`) y de los Complementos
Teóricos de la Guía 2026 (`LISTA_CIRCULAR`, p. 63-64), pasadas a la notación moderna. En la guía
original hay tres asignaciones escritas con `=` (`p = *p.prox`, `Prim = p`, `Prim = *q.prox`): acá
van con `:=`. Ver [[errores-y-trampas]] §B.8.

**Declaración**:

```
    Ambiente
        NODO = REGISTRO
            dato: <tipo>
            prox: Puntero a NODO
        FIN_REGISTRO
        PRIM, p, q, a: Puntero a NODO
        valor: <tipo>
```

**Recorrido**:

```
        p := PRIM
        MIENTRAS p <> NIL HACER
            ESCRIBIR(*p.dato)
            p := *p.prox                    // avanzar: sin esto, ciclo infinito
        FIN_MIENTRAS
```

**Búsqueda**:

```
        LEER(valor)
        p := PRIM
        MIENTRAS (p <> NIL) Y (*p.dato <> valor) HACER
            p := *p.prox
        FIN_MIENTRAS
        SI p <> NIL ENTONCES
            ESCRIBIR('Se encontró el elemento')
        SINO
            ESCRIBIR('No se encontró el elemento')
        FIN_SI
```

**Carga apilada** (cada nuevo queda primero; la lista sale al revés de la lectura):

```
        PRIM := NIL
        LEER(valor)
        MIENTRAS valor <> '*' HACER
            NUEVO(p)
            *p.dato := valor
            *p.prox := PRIM
            PRIM := p
            LEER(valor)
        FIN_MIENTRAS
```

**Carga encolada** (cada nuevo queda último; `a` es el último hasta ahora):

```
        PRIM := NIL
        LEER(valor)
        MIENTRAS valor <> '*' HACER
            NUEVO(p)
            *p.dato := valor
            *p.prox := NIL
            SI PRIM = NIL ENTONCES
                PRIM := p
            SINO
                *a.prox := p
            FIN_SI
            a := p
            LEER(valor)
        FIN_MIENTRAS
```

**Carga ordenada** (inserta un valor en su lugar; `q` es el actual y `a` el anterior):

```
        LEER(valor)
        NUEVO(p)
        *p.dato := valor
        a := NIL
        q := PRIM
        MIENTRAS (q <> NIL) Y (*q.dato < valor) HACER
            a := q
            q := *q.prox
        FIN_MIENTRAS
        SI a = NIL ENTONCES                 // va primero (o la lista estaba vacía)
            *p.prox := PRIM
            PRIM := p
        SINO
            *p.prox := q
            *a.prox := p
        FIN_SI
```

**Eliminación**:

```
        LEER(valor)
        a := NIL
        q := PRIM
        MIENTRAS (q <> NIL) Y (*q.dato <> valor) HACER
            a := q
            q := *q.prox
        FIN_MIENTRAS
        SI q = NIL ENTONCES
            ESCRIBIR('Error, el valor no existe')
        SINO
            SI a = NIL ENTONCES             // era el primero
                PRIM := *q.prox
            SINO
                *a.prox := *q.prox
            FIN_SI
            DISPONER(q)
        FIN_SI
```

> En la guía `a := NIL` está una sola vez, arriba de todo. Si la carga ordenada o la eliminación se
> repiten dentro de un ciclo, `a` tiene que volver a `NIL` **cada vez**, o arrastra el anterior de
> la vuelta pasada.

**Lista circular**: el último apunta al primero. De `LISTA_CIRCULAR` (Complementos 2026):

```
        // listar
        SI PRIMERO = NIL ENTONCES
            ESCRIBIR('ERROR, Lista Vacía')
        SINO
            T := PRIMERO
            MIENTRAS *T.SIG <> PRIMERO HACER
                ESCRIBIR(*T.VALOR)
                T := *T.SIG
            FIN_MIENTRAS
            ESCRIBIR(*T.VALOR)              // el último, donde se detuvo el ciclo
        FIN_SI

        // insertar (en el 2º lugar, para no tener que buscar el último)
        NUEVO(P)
        *P.VALOR := DATO
        SI PRIMERO = NIL ENTONCES
            *P.SIG := P                     // único nodo: se apunta a sí mismo
            PRIMERO := P
        SINO
            *P.SIG := *PRIMERO.SIG
            *PRIMERO.SIG := P
        FIN_SI
```

Para eliminar en una circular hay tres casos: único nodo (`PRIMERO := NIL`), el primero (hay que
buscar el último para engancharlo al nuevo primero) y uno del medio (`*ANT.SIG := *T.SIG`). El
algoritmo completo está en los Complementos 2026 y en `aed-vscode/test/fixtures/guia_lista_circular.frre`.

**Pilas y colas**: ver [[SINTAXIS]] §10. Apilar es la carga apilada de un nodo; encolar es la
carga encolada con un puntero `ULT` fijo.

---

## 10. Recursividad

Como se resuelve en clase: **primero el planteo formal, después la función**.

```
/*
Planteo formal: F(x)
  Caso base:       <valor>,          si <x es el caso trivial>
  Caso recursivo:  <cuenta con F(x')>, si <no lo es>       // x' más cerca del caso base
*/

FUNCION F(x: <tipo>): <tipo> ES
    Proceso
        SI <x es el caso trivial> ENTONCES
            F := <valor>                    // caso base: sin llamada recursiva
        SINO
            F := <cuenta con F(x')>         // caso recursivo
        FIN_SI
FIN_FUNCION
```

**Sobre un arreglo**, con el índice como parámetro que se acerca al caso base:

```
// de N hacia 1: se llama Suma(V, N)
FUNCION Suma(A: vector; i: entero): entero ES
    Proceso
        SI i = 1 ENTONCES
            Suma := A[i]
        SINO
            Suma := A[i] + Suma(A, i - 1)
        FIN_SI
FIN_FUNCION

// de 1 hacia N: se llama Promedio_10_Elementos(V, 1)
FUNCION Promedio_10_Elementos(A: vector; i: entero): real ES
    Proceso
        SI i = 10 ENTONCES
            Promedio_10_Elementos := A[i] / 10
        SINO
            Promedio_10_Elementos := A[i] / 10 + Promedio_10_Elementos(A, i + 1)
        FIN_SI
FIN_FUNCION
```

**Sobre los dígitos de un número**: el último dígito es `N MOD 10` y el resto del número es `N DIV 10`.
El caso base es `N < 10` (queda un solo dígito).

**Procedimiento recursivo**: lo que se hace **antes** de la llamada sale en orden de bajada; lo que
se hace **después**, en orden de subida. Por eso para escribir un número en binario se llama
primero y se escribe después:

```
PROCEDIMIENTO Binario(n: entero) ES
    Proceso
        SI n > 1 ENTONCES
            Binario(n DIV 2)
        FIN_SI
        ESCRIBIR(n MOD 2)
FIN_PROCEDIMIENTO
```

Antes de entregar, revisar: ¿hay caso base? ¿cada llamada se acerca a él? ¿el caso base y el
recursivo usan la misma condición? ¿el resultado de la función se asigna a su nombre en **todas**
las ramas?

