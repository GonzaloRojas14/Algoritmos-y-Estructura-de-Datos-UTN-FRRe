---
name: pseudocodigo-utn
description: Sintaxis exacta, plantillas canónicas y checklist de errores del pseudocódigo de Algoritmos y Estructuras de Datos (UTN-FRRe, AED 2026). Usar SIEMPRE que se escriba, corrija, revise o explique pseudocódigo con ACCION/AMBIENTE/PROCESO, secuencias (ARR/AVZ/NFDS), archivos secuenciales (LEER/ESCRIBIR/NFDA), archivos indexados (SI EXISTE/RE-ESCRIBIR/ELIMINAR), corte de control, mezcla, actualización por lotes o unitaria, arreglos, registros, funciones y procedimientos; o cuando se trabaje sobre archivos de Practica/ o con extensión .frre.
---

# Pseudocódigo AED — UTN-FRRe

Notación de la cátedra AED (ISI, UTN-FRRe). **Los ejercicios se resuelven copiando una plantilla canónica y adaptándola**, no inventando estructura.

## Fuentes y prioridad

Cuando dos fuentes se contradicen, gana la de arriba:

1. **Plantillas oficiales de cátedra** — repo `UTN-FRRe/isi-aed`, carpeta `Pseudocodigo/`. Es lo que se pide reproducir en el parcial.
2. **Libro de cátedra** — Pinto & Bolatti 2026. Autoridad para **teoría** (conceptos, clasificaciones, definiciones), no siempre para notación.
3. **Resoluciones de alumnos** — repo `Anderwsont-Experimental/AED26_Guia_Ejercicios`. Útiles como ejemplo; **contienen bugs** (ver `references/errores-y-trampas.md`).

## Archivos de referencia

Leer el que corresponda **antes** de escribir código:

| Archivo | Cuándo |
|---|---|
| `references/sintaxis-completa.md` | Siempre. Declaraciones, tipos, verbos, operadores, variantes aceptadas |
| `references/plantillas.md` | Al resolver cualquier ejercicio de Unidad 2 (archivos en adelante) |
| `references/errores-y-trampas.md` | Al corregir o revisar código, propio o ajeno |

## Qué plantilla usar — árbol de decisión

```
¿Con qué se trabaja?
│
├─ Nada persistente (solo teclado/pantalla) ─────────► ACCION simple
│
├─ SECUENCIA (cinta, ARR/AVZ) ──────────────────────► esquema de secuencia
│   ├─ pura (cantidad conocida) ──────► PARA
│   ├─ indefinida (marca de fin) ─────► MIENTRAS NFDS / MIENTRAS v <> marca
│   └─ con subsecuencias ─────────────► ciclos anidados, uno por nivel
│
└─ ARCHIVO
    ├─ 1 archivo, se recorre entero ───────────────► esquema secuencial
    │   └─ ¿pide totales por grupos/niveles?
    │        └─ SÍ ──────────────────────────────► CORTE DE CONTROL
    │
    ├─ 2 archivos ordenados por la misma clave
    │   ├─ solo combinar/listar ───────────────────► MEZCLA
    │   │    ├─ ¿los dos deben agotarse? ──► INC (con HV)
    │   │    └─ ¿solo mientras haya en ambos? ──► EXC (+ ciclos de vaciado)
    │   └─ maestro + movimientos (A/B/M) ─────────► ACTUALIZACIÓN
    │        ├─ 1 movimiento por clave ──────────► UNITARIA
    │        └─ varios movimientos por clave ────► LOTE (registro aux)
    │
    └─ INDEXADO (acceso por clave) ────────────────► ACT INDEXADA (ABM interactivo)
         ├─ baja lógica ────► campo marca + RE-ESCRIBIR
         └─ baja física ────► ELIMINAR
```

## Núcleo de sintaxis

Lo mínimo que no se puede equivocar. El detalle completo está en `references/sintaxis-completa.md`.

```
ACCION nombre_sin_puntos ES
    Ambiente
        // constantes, tipos registro, variables, subacciones
    Proceso
        // instrucciones
FIN_ACCION
```

- Asignación `:=` · comparación `=` · distinto `<>` · lógicos `Y` `O` `NO` · `MOD` `DIV` · potencia `**`
- Cerrar siempre: `FIN_SI` `FIN_MIENTRAS` `FIN_PARA` `FIN_SEGUN` `FIN_REGISTRO` `FIN_FUNCION` `FIN_PROCEDIMIENTO` `FIN_ACCION`
- **`PARA i := 1 HASTA 10, 1 HACER`** — el incremento va con **coma**, puede ser negativo
- Retorno de función: se asigna **al nombre de la función**
- Los procedimientos se invocan **por nombre solo**, sin paréntesis si no llevan parámetros
- Todo lo que se abre (`ABRIR`, `ARR`, `CREAR`) se cierra con `CERRAR`, uno por uno

### Verbos por estructura

| | Secuencia | Archivo secuencial | Archivo indexado |
|---|---|---|---|
| Abrir lectura | `ARR(sec)` | `ABRIR E/(arch)` | `ABRIR E/S(arch)` |
| Abrir escritura | `CREAR(sec)` | `ABRIR /S(arch)` | — |
| Leer | `AVZ(sec, v)` | `LEER(arch, reg)` | `reg.clave := x` ; `LEER(arch, reg)` |
| Escribir | `ESCRIBIR(sec, v)` | `ESCRIBIR(arch, reg)` | `ESCRIBIR(arch, reg)` (alta) |
| Modificar | — | — | `RE-ESCRIBIR(arch, reg)` |
| Eliminar | — | — | `ELIMINAR(arch, reg)` |
| ¿Hay más? | `NFDS(sec)` | `NFDA(arch)` | `SI EXISTE ENTONCES` |
| Cerrar | `CERRAR(sec)` | `CERRAR(arch)` | `CERRAR(arch)` |

> `ESCRIBIR` sirve para pantalla, secuencia y archivo: lo distingue el primer argumento.
> En indexado **nunca** se recorre con `NFDA`: se accede por clave y se pregunta `SI EXISTE`.

## Reglas de oro por tema

**Secuencias** — `ARR` + `AVZ` van juntos, siempre. Al salir de un ciclo que buscaba un delimitador la ventana quedó **parada en el delimitador**: hay que avanzar una vez más. Todo ciclo interno lleva guarda `NFDS`. Contadores del nivel se inicializan al abrir el nivel; los globales, una sola vez.

**Archivos secuenciales** — lectura anticipada pegada al `ABRIR`, y `LEER` como **última instrucción del ciclo**.

**Corte de control** — el orden dentro de cada `corte_N` es fijo: llamar al corte inferior → emitir → acumular al superior → poner en cero lo propio → **re-resguardar la clave**. `tratar_corte` pregunta de **mayor a menor** jerarquía. Después del `MIENTRAS` se llama al corte **de mayor jerarquía** (cascada hacia abajo sola).

**Mezcla / actualización** — con `HV` (inclusivo) el ciclo es `MIENTRAS (c1 <> HV) O (c2 <> HV)`; sin `HV` (exclusivo) es `MIENTRAS NFDA(a1) Y NFDA(a2)` **más dos ciclos de vaciado**. Los `LEER` van encapsulados en procedimientos que ponen `HV` al detectar `FDA`.

**Lote vs. unitaria** — lote usa un registro `aux` y un ciclo interno que consume **todos** los movimientos de la misma clave antes de grabar una sola vez.

**Indexado** — `clave` primero, `LEER` después, y recién ahí `SI EXISTE`. Modificar exige haber leído justo antes.

## Checklist al revisar

1. ¿Falta el `AVZ` que **supera el delimitador**?
2. ¿Ciclo interno de cinta sin guarda `NFDS`?
3. ¿El `LEER` está al final del ciclo de archivo?
4. ¿Los barridos de blancos usan `= " "` y los de palabra `<> " " Y <> marca`? (el `O` en vez de `Y` es ciclo infinito)
5. En corte: ¿cada `corte_N` re-resguarda su clave y pone en cero **sus** acumuladores?
6. En corte: ¿el llamado posterior al ciclo es al corte de **mayor** jerarquía?
7. En corte: ¿`tratar_corte` pregunta de mayor a menor?
8. En mezcla/actualización: ¿los `LEER` asignan `HV` al llegar a `FDA`?
9. En lote: ¿se lee el siguiente movimiento **antes** de entrar al ciclo de lote en la rama de alta?
10. ¿Contadores declarados que nunca se incrementan? ¿Variables usadas sin leer?
11. ¿`>` donde iba `>=`? ¿división sin verificar divisor > 0?
12. ¿Se resolvieron **todos** los incisos (a, b, c…)? Contarlos uno por uno.
13. ¿Todo lo abierto se cerró?

## Al corregir

Señalar el error, explicar **por qué** falla con el caso concreto que lo rompe, y recién después mostrar la corrección. No reescribir el archivo entero si el error es puntual. Si el código sigue una plantilla, indicar **qué paso de la plantilla se salteó**.
