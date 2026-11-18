---
tipo: notas
materia: Algoritmos y Estructura de Datos
tags:
  - AED
  - matrices
  - parcial
---

# Parcial resuelto en clase — Final 04/03/2022, Problema 1

> [!warning] Estado de estas notas
> Armadas a partir de 5 fotos de la pantalla compartida en clase (IMG_5227 a
> IMG_5231). Cubren **de la línea 37 a la 98**, que es el final. Lo transcripto
> está marcado como tal; lo demás es deducción.
>
> **Falta fotografiar las líneas 1 a 36**: todo el `Ambiente` y el arranque del
> `Proceso`. Ver el mapa de abajo.

## Mapa de lo que tenemos

| Líneas | Qué hay | ¿Lo tenemos? |
|---|---|---|
| 1 – 36 | `Ambiente`: registros, archivos, matriz `T`, variables globales. Arranque del `Proceso`: apertura de archivos, lectura del año, llamada a poner en cero, lectura anticipada, `mientras` | **NO** |
| 37 – 40 | final del procedimiento que pone `T` en cero | sí (parcial) |
| 42 – 52 | `procedimiento busqueda` | sí, completo |
| 61 – 76 | cuerpo del ciclo principal | sí, completo |
| 77 – 88 | doble `PARA` que vuelca la matriz a Totales + b.1 | sí, completo |
| 89 – 98 | b.2, b.3, cierres y `finaccion` | sí, completo |

El archivo del profe se llama **`Accion parcial es (1).txt`**. En las pestañas de
Sublime se ven otros resueltos que pueden servir: `2018.P2.TA.E1.txt`,
`Accion Ej2.3.1a es`, `Accion Ej2.3.10 es`, `Accion estadistica es.txt`,
`2do parcial.txt`, `resolucion.txt`, `...eglos de registros.txt`. Vale la pena
pedírselos.

## El ejercicio

Estadística de errores de programas por año.

- **Listado ya cargado** de 50 códigos de error (código AN(8) + descripción AN(30)). Se recibe **como parámetro**, no se carga.
- **Archivo LogErrores** (fecha AN(10), código AN(8)): validado, **sin orden lógico**, puede tener más de un año.
- **Procedimiento provisto** que recibe una fecha y devuelve día/mes/año. No se desarrolla.
- **a)** Procesar LogErrores → generar `NoProcesados` (los de otro año) y `Totales` (mes, código, cantidad).
- **b)** A partir de Totales y los 50 códigos: b.1 códigos no informados por mes · b.2 mes con más errores · b.3 total de errores.

## Lo que se vio en clase (transcripto de las fotos)

### Fragmento 0 — final del procedimiento que pone la matriz en cero

Termina alrededor de la línea 40. Se ve solo el final:

```
      T[i,j]:= 0
    finpara
  finpara
finprocedimiento
```

Usa `i` y `j` como contadores de los dos `PARA`.

### Fragmento 1 — el procedimiento de búsqueda (líneas 42 a 52)

```
procedimiento busqueda () es
  i:= 1; aux:= reg_log.cod_error
  mientras (i<50) y (listado[i].cod_error <> aux) hacer
    i:= i+1
  finmientras
  si listado[i].cod_error = aux entonces
    j:= i
  sino
    j:= 0
  finsi
finprocedimiento
```

> Dos cosas de la foto:
>
> 1. El `si` y el `sino` están comentados (`//si`, `//sino`). Debe haber sido una
>    edición en vivo: así como está, `j` siempre termina en 0.
> 2. **No hay `Ambiente`**: la línea 42 es el encabezado y la 43 ya es `i:= 1`.
>    Entonces `i`, `j` y `aux` son **variables globales**, no locales.

### Fragmento 2 — el cuerpo del ciclo principal

```
fec := funcfecha(reg_log.fecha)
si fec.año = año_ingresado entonces
    i:= fec.mes
    busqueda ()

    T[i,j]  := T[i,j]  + 1
    T[i,51] := T[i,51] + 1
    T[13,j] := T[13,j] + 1
    T[13,51]:= T[13,51]+ 1
  finsi
sino
  reg_nopro:= reg_log
  escribir (no_procesados, reg_nopro)
finsi
leer (arch_log, reg_log)
finmientras
```

### Fragmento 3 — el volcado de la matriz a Totales

```
para i:= 1 hasta 12 hacer
  para j:= 1 hasta 50 hacer

      reg_tot.mes:= i
      reg_tot.cod_error:= listado[j].cod_error
      reg_tot.cant_error:= T[i,j]
      escribir (arch_tot, reg_tot)

  finpara
finpara
```

### Fragmento 4 — el cierre (líneas 82 a 98)

```
      reg_tot.cant_error:= T[i,j]
      escribir (arch_tot, reg_tot)
      si T[i,j] = 0 entonces
        escribir ("el codigo de error", listado[j].cod_error, "no fue informado")
      finsi
    finpara
  finpara
  para i:= 1 hasta 12 hacer
    pos_max:= 1
    si T[i,51] > T[pos_max,51] entonces
      pos_max:= i
    finsi
  finpara
  escribir ("el mes con mayor cantidad de errores es", pos_max)
  escribir ("la cantidad total de errores registrados es de:", T[13,51])
  cerrar (arch_log); cerrar (arch_tot); cerrar (no_procesados)
finaccion
```

## El diseño que se deduce

**La matriz es `T[1..13, 1..51]`**, con márgenes:

| | col 1..50 (códigos) | col 51 |
|---|---|---|
| **fila 1..12** (meses) | celda: errores de ese código en ese mes | total del mes |
| **fila 13** | total de ese código en el año | **total general** |

Por eso son cuatro incrementos por registro: celda, marginal de fila, marginal de
columna y esquina.

**Convención de índices con variables globales:**

- `i` = fila = mes
- `j` = columna = posición del código en el listado
- `busqueda()` no recibe ni devuelve nada: lee `reg_log.cod_error` y deja el
  resultado en `j`.

**La búsqueda es lineal con centinela para arreglos DESORDENADOS** (filmina 17–18).
El `<>` lo confirma: la variante para ordenados usa `>` o `<`. Correcto, porque la
consigna nunca dice que los 50 códigos estén ordenados.

**Totales se escribe completo: las 600 filas (12 × 50), ceros incluidos.** No hay
ningún `si T[i,j] > 0`.

**No hay un segundo algoritmo: está todo en UNA SOLA ACCION.** El `finaccion` viene
justo después de b.3. El inciso b) **no vuelve a leer el archivo Totales**: se
resuelve con la misma matriz que ya está en memoria.

- **b.1** → adentro del mismo doble `PARA` del volcado: después de escribir cada registro, `si T[i,j] = 0` informa que ese código no fue reportado ese mes. Dos pájaros de un tiro.
- **b.2** → recorre la **columna 51** (los totales por mes) buscando el máximo.
- **b.3** → es **leer `T[13,51]`**, la esquina. Nada que acumular.

Ahí se ve para qué servían los marginales: no se vuelcan al archivo, se usan para
contestar b.2 y b.3 sin recorrer nada de nuevo.

> Esto se aparta de la letra de la consigna, que dice *"A partir del archivo Totales
> y los 50 Códigos de Error, informar"*. El profe lo resuelve desde la matriz, no
> releyendo Totales. Vale la pena preguntarle si acepta las dos formas.

## Diferencias con la primera versión que habíamos escrito

| Tema | Lo que habíamos hecho | Lo de la clase |
|---|---|---|
| Tamaño de la matriz | `[1..12, 1..50]` | **`[1..13, 1..51]`**, con marginales |
| Totales por mes / general | acumuladores aparte en b) | salen de la fila 13 y la columna 51 |
| Qué se vuelca a Totales | solo las celdas > 0 | **las 600 filas**, ceros incluidos |
| Estructura general | dos subacciones, a) y b) | **una sola ACCION**, todo seguido |
| Cómo se resuelve b.1 | grilla de lógicos + búsqueda | **`si T[i,j] = 0` adentro del volcado** |
| De dónde salen b.2 y b.3 | acumuladores propios en b) | **de la matriz**: columna 51 y `T[13,51]` |
| Desglose de la fecha | procedimiento con parámetro `var` | **función que devuelve el registro** |
| Búsqueda | bandera `pos = 0` | **centinela de la filmina**, con `<>` |
| Paso de parámetros | por parámetro a cada subacción | variables **globales** (`i`, `j`, `listado`) |

## Para confirmar / lo que falta ver

- [x] ~~Si el `i` de `busqueda` es local~~ → **CONFIRMADO: es global**, el procedimiento no tiene `Ambiente`. Ver el problema abajo.
- [ ] **El `Ambiente` general de la ACCION**: qué está declarado y con qué tipos.
- [ ] El inicio del `Proceso`: cómo se inicializa la matriz en cero y cómo se abren los archivos.
- [x] ~~Todo el inciso b)~~ → **VISTO**: no relee Totales, sale todo de la matriz, y está dentro de la misma ACCION.
- [x] ~~Para qué sirven los marginales~~ → **para b.2 y b.3**: la columna 51 da el máximo por mes y `T[13,51]` el total.
- [ ] La firma exacta de `funcfecha` y si el año ingresado es parámetro o global.

## El problema del `i` pisado

Confirmado que `busqueda` no declara nada local, esta secuencia del ciclo principal
no funciona:

```
i:= fec.mes        // i = el mes, para usarlo como FILA
busqueda ()        // pero adentro hace i:= 1 ... i:= i+1 hasta 50
T[i,j]:= T[i,j]+1  // acá i ya NO es el mes: es donde quedó el contador
```

Como además `busqueda` termina con `j:= i`, al salir quedan `i` y `j` valiendo lo
mismo, así que `T[i,j]` apunta a la diagonal de la matriz. Y si el código no se
encuentra, `i` queda en 50 — una fila que en una matriz de 13 no existe.

Probado en el intérprete: entrando con `i` = 6 (junio), al volver de `busqueda`
vale 50.

Tres formas de arreglarlo, cualquiera sirve:

1. Declarar el contador **local** dentro de `busqueda` (agregarle su `Ambiente`).
2. Usar otra variable para el ciclo de la búsqueda, por ejemplo `x`.
3. Hacer `i := fec.mes` **después** de llamar a `busqueda`.

> Puede ser que en clase lo hayan corregido más adelante y no lo tengamos en las
> fotos. Confirmar.

## El bug del máximo (líneas 89 a 94)

```
para i:= 1 hasta 12 hacer
  pos_max:= 1                          <-- ESTO VA ANTES DEL PARA
  si T[i,51] > T[pos_max,51] entonces
    pos_max:= i
  finsi
finpara
```

`pos_max := 1` está **adentro** del ciclo, así que se reinicia en cada vuelta. En la
práctica el algoritmo termina comparando solo el **último mes contra el primero**:
al salir, `pos_max` vale 12 si diciembre supera a enero, y 1 en cualquier otro caso.

Probado con totales donde el máximo está en julio (95 errores):

```
como está en la foto  -> mes 1 con 10
corregido             -> mes 7 con 95
```

La inicialización del máximo va **antes** del ciclo, y el recorrido arranca en 2:

```
pos_max:= 1
para i:= 2 hasta 12 hacer
  si T[i,51] > T[pos_max,51] entonces
    pos_max:= i
  finsi
finpara
```

Es exactamente el error clásico de "inicializar mal el máximo". Acá no se nota a
simple vista porque la inicialización existe: está, pero en el lugar equivocado.

## Contraste con la teoría de la cátedra

### Lo que coincide

**La matriz con márgenes es textual de las filminas 6 (Procesos Estadísticos),
diapositiva 9:**

> *"La matriz es de 51 × 31: 50 filas de bases de datos **+ una fila más de
> totales**, y 30 columnas de problemas **+ una columna más de totales**. La
> intersección final es el **total general**."*

Es exactamente `T[1..13, 1..51]`: 12 meses + 1 fila, 50 códigos + 1 columna, y la
esquina como total general. No es una idea del profe: es la plantilla de la unidad.

**Los pasos del método también están en esa filmina:**

> 4. *"De acuerdo al valor actualizar la matriz → `A[Reg.BD, Reg.Prob] := A[Reg.BD, Reg.Prob] + 1`"*
> 5. *"**Verificar si se requiere actualizar filas/columnas totalizadoras**"*
> 6. *"Continuar procesando el archivo hasta el final"*
> 7. *"Mostrar la matriz e informar los datos específicos que se soliciten"*

De ahí salen los cuatro incrementos por registro.

**Cuándo corresponde un proceso estadístico** (misma filmina): cuando los datos
vienen **desordenados** desde un archivo y hacen falta totales por categoría. Es
justo la condición de este parcial.

**La búsqueda** es la de la filmina 18 (lineal con centinela, desordenados), con
`<>`. Coincide letra por letra.

**El listado de 50 códigos como vector paralelo**: la filmina del ejemplo dice
*"los nombres se encuentran almacenados en vectores cuyo código se corresponde con
el código de ciudad"*. Mismo rol que `listado[]` acá.

**Las variables globales** entre subacciones: coincide con lo que dice
`sintaxis-completa.md` §8, que las plantillas de corte dependen de que los
contadores y resguardos sean globales.

### Lo que NO coincide

**La notación.** El profe escribe `finaccion`, `finsi`, `finmientras`, `finpara`,
`finprocedimiento`, todo en minúscula y sin guión bajo: es la **forma vieja**.
Nuestro `sintaxis-completa.md` dice que conviene la moderna (`FIN_SI`,
`FIN_ACCION`) porque "es la de los ejercicios recientes". En la práctica, el profe
usa la vieja. **Seguir al profe.**

**Los paréntesis vacíos.** Escribe `procedimiento busqueda () es` y lo invoca como
`busqueda ()`. Nuestro `sintaxis-completa.md` §8 dice que un procedimiento sin
parámetros se invoca por su nombre solo. El profe usa paréntesis en los dos lados.

**El libro no sirve para este tema.** El PDF de teoría que armamos (`Libro de
Cátedra — Teoría completa.pdf`) tiene 9 capítulos y **ninguno es de arreglos ni
matrices**: va de Secuencias directo a Registros y Archivos, y después a Listas.
Todo lo de arreglos, búsqueda, ordenamiento y procesos estadísticos está **solo en
las filminas 4, 5 y 6**.

## Sobre ejecutarlo

El `funcfecha` no se puede escribir en esta notación: no hay forma de partir un
texto de 10 caracteres en día, mes y año. En el parcial da igual, porque la
consigna dice que viene hecho. Para poder correrlo habría que adaptar el diseño
del registro y traer la fecha ya separada.
