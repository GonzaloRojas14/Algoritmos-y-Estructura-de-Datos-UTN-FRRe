# Sintaxis completa — pseudocódigo AED UTN-FRRe

Derivada de las plantillas oficiales (`isi-aed/Pseudocodigo/`), el libro de cátedra y las resoluciones corregidas por profesores.

---

## 1. Esqueleto

```
ACCION nombre_accion ES
    Ambiente
        // constantes
        // tipos registro
        // variables
        // subacciones (funciones y procedimientos)
    Proceso
        // instrucciones
FIN_ACCION
```

- El nombre **no lleva puntos ni espacios**: `ACCION ej_2_2_4 ES`, nunca `ACCION 2.2.4 ES`.
- `Ambiente` va siempre, aunque quede vacío.
- **No lleva `FIN_PROCESO`.** Del cuerpo se pasa directo a `FIN_ACCION`.
- Comentarios: `//` de línea, `/* ... */` de bloque. La consigna va arriba del `ACCION` en bloque.

### Variantes que vas a ver y son válidas

Las plantillas viejas de cátedra usan un registro más "pascalero". Se entienden, pero **para el parcial conviene la forma de arriba**, que es la de los ejercicios recientes.

| Forma moderna (usar) | Forma vieja (aparece en plantillas de cátedra) |
|---|---|
| `Proceso` | `Algoritmo` |
| `SINO` | `Contrario` |
| `FIN_SI` `FIN_MIENTRAS` | `FinSi` `FinMientras` |
| `FIN_ACCION` | `FinAccion.` |
| `FIN_PROCEDIMIENTO` | `Fin_Proc;` / `Fin;` |
| sin `;` al final de línea | con `;` |

No mezclar registros dentro de un mismo archivo.

---

## 2. Tipos y declaración de variables

```
nombre : tipo
a, b, c : entero
```

| Tipo | Uso | Ejemplo |
|---|---|---|
| `entero` | enteros | `i : entero` |
| `real` | con decimales | `precio : real` |
| `caracter` | un carácter | `v : caracter` |
| `logico` | `verdadero` / `falso` | `flag : logico` |
| `alfanumerico` / `AN(n)` | texto de hasta n | `nom : AN(50)` |
| `N(n)` | numérico de n dígitos | `dni : N(8)` |
| `N(e,d)` | n dígitos, d decimales | `importe : N(5,2)` |
| **subrango** | rango cerrado de valores | `dia : 1..31` · `anio : 1900..9999` |
| **enumerado** | lista literal de valores | `tipo : ("IND","DOB","SUITE")` · `mov : ('A','B','M')` |

`AN[50]` con corchetes también aparece en plantillas de cátedra; `AN(50)` es lo más frecuente.

### Constantes

Sin tipo, con valor directo:

```
lim_descuento = 200000
descuento = 0.15
HV = 99999999
```

### Booleanos

Se escriben `verdadero` / `falso` (también `Verdadero`/`Falso`, `V`/`F`). Una variable lógica se usa directo en la condición:

```
flag := Falso
...
SI (flag) ENTONCES
```

---

## 3. Registros

```
fecha = REGISTRO
    dia : 1..31
    mes : 1..12
    anio : 1900..9999
FIN_REGISTRO

persona = REGISTRO
    nombre    : AN(50)
    dir       : AN(50)
    fecha_nac : fecha          // registro anidado
FIN_REGISTRO

reg : persona                  // recién acá se declara la variable
```

- El registro define **un tipo**, no una variable.
- Acceso con `.`, encadenable: `reg.fecha_nac.dia`
- Se opera como **una sola entidad**: `reg_sal := reg_mae` copia todo.
- Entre tipos **distintos** hay que asignar **campo por campo**.

### Clave compuesta

```
formato_clave = REGISTRO
    clave1 : ...
    clave2 : ...
FIN_REGISTRO

formato_maestro = REGISTRO
    clave  : formato_clave     // campo continente
    campo1 : ...
FIN_REGISTRO
```

Así se puede comparar `reg_mae.clave < reg_mov.clave` de una sola vez.

> **FECHA**: declarar `anio, mes, dia` (de mayor a menor) si se van a comparar fechas como registro entero. Al revés la comparación da mal.

---

## 4. Archivos

```
arch : ARCHIVO de persona
arch : ARCHIVO de reg ordenado por clave1, clave2 y clave3
arch : ARCHIVO de mae INDEXADO por clave
```

| Operación | Forma |
|---|---|
| Abrir lectura | `ABRIR E/(arch)` |
| Abrir escritura | `ABRIR /S(arch)` |
| Abrir lectura/escritura | `ABRIR E/S(arch)` |
| Leer | `LEER(arch, reg)` |
| Escribir/grabar | `ESCRIBIR(arch, reg)` |
| Cerrar | `CERRAR(arch)` |
| Fin de archivo | `FDA(arch)` · negado `NFDA(arch)` |

Variantes equivalentes en plantillas de cátedra: `ABRIRe(arch)`, `ABRIRs(arch)`, `ABRIRe/s(arch)`, `NoFDA(arch)`. El libro además usa `GRABAR(arch, reg)` en lugar de `ESCRIBIR`; **las plantillas oficiales usan `ESCRIBIR`**.

### Esquema de recorrido

```
ABRIR E/(arch)
LEER(arch, reg)                 // lectura anticipada
MIENTRAS NFDA(arch) HACER
    // tratar reg
    LEER(arch, reg)             // ← última instrucción del ciclo, obligatorio
FIN_MIENTRAS
CERRAR(arch)
```

---

## 5. Archivos indexados

```
arch_mae : ARCHIVO de mae INDEXADO por clave
```

| Operación | Forma | Nota |
|---|---|---|
| Abrir | `ABRIR E/S(arch)` | lo normal, porque se lee y se modifica |
| Buscar | `reg.clave := valor` ; `LEER(arch, reg)` | **la clave se asigna ANTES del LEER** |
| ¿Existe? | `SI EXISTE ENTONCES ... SINO ... FIN_SI` | pregunta por el resultado del último `LEER` |
| Alta | `ESCRIBIR(arch, reg)` | la clave **no** debe existir |
| Modificación | `RE-ESCRIBIR(arch, reg)` | exige `LEER` inmediatamente antes |
| Baja física | `ELIMINAR(arch, reg)` | |
| Baja lógica | `reg.Baja := '*'` + `RE-ESCRIBIR` | preferida cuando el registro tiene campo marca |

**No se recorre con `NFDA`**: el acceso es puntual por clave.

---

## 6. Secuencias

```
sec : SECUENCIA de caracter
sec : SECUENCIA de entero
v   : caracter
```

| Operación | Forma |
|---|---|
| Arrancar (lectura) | `ARR(sec)` |
| Crear (escritura) | `CREAR(sec)` |
| Avanzar | `AVZ(sec, v)` |
| Escribir | `ESCRIBIR(sec, v)` |
| Fin de secuencia | `NFDS(sec)` · variante `NoFDS(sec)` |
| Cerrar | `CERRAR(sec)` |

```
ARR(sec); AVZ(sec, v)           // siempre juntos
CREAR(sal)

MIENTRAS NFDS(sec) HACER
    ...
FIN_MIENTRAS

CERRAR(sec); CERRAR(sal)
```

### Clasificación (define qué ciclo usar)

| Tipo | Qué significa | Ciclo |
|---|---|---|
| **Pura** | cantidad de elementos conocida | `PARA` |
| **Indefinida** | termina con marca (`*`, `#`, FDS) | `MIENTRAS` |
| **Impura** | los elementos no son todos iguales / hay estructura interna | `MIENTRAS` + subciclos |

### Idiomas obligatorios

**Barrido de blancos** — condición `= " "`:

```
MIENTRAS (v = " ") HACER
    AVZ(sec, v)
FIN_MIENTRAS
```

**Barrido de palabra** — condición con `Y`, nunca `O`:

```
MIENTRAS (v <> " ") Y (v <> ".") Y NFDS(sec) HACER
    AVZ(sec, v)
FIN_MIENTRAS
```

**Superar el delimitador** — el avance vital:

```
MIENTRAS NFDS(sec) Y (v <> "&") HACER
    AVZ(sec, v)
FIN_MIENTRAS
AVZ(sec, v)                     // ← sin esto quedás parado en el '&'
```

**Armar un número de N dígitos** — la forma corta y correcta:

```
num := 0
PARA i := 1 HASTA 3 HACER
    num := num * 10 + car_ent(v)
    AVZ(sec, v)
FIN_PARA
```

**Subsecuencias jerárquicas** — un ciclo por nivel:

```
MIENTRAS NFDS(sec) HACER               // texto
    MIENTRAS (v <> ".") HACER          // oración
        MIENTRAS (v = " ") HACER       // blancos
            AVZ(sec, v)
        FIN_MIENTRAS
        MIENTRAS (v <> " ") Y (v <> ".") HACER   // palabra
            AVZ(sec, v)
        FIN_MIENTRAS
    FIN_MIENTRAS
    AVZ(sec, v)                        // superar el '.'
FIN_MIENTRAS
```

---

## 7. Estructuras de control

```
SI condicion ENTONCES
    ...
SINO
    ...
FIN_SI
```

```
SEGUN expresion HACER
    1 : ...
    2 : ...
    'A' : ...
    'B', 'M' : ...              // varios valores en una rama
    otros : ...                 // variante: CONTRARIO :
FIN_SEGUN
```

```
MIENTRAS condicion HACER        // 0..n vueltas, condición al inicio
FIN_MIENTRAS

REPETIR                          // 1..n vueltas, condición al final
HASTA QUE condicion

PARA i := inicio HASTA fin, incremento HACER
FIN_PARA
```

- El incremento del `PARA` va con **coma** y puede ser negativo: `PARA x := 20 HASTA -20, -2 HACER`
- Si el incremento es 1 se puede omitir: `PARA i := 1 HASTA 23 HACER`
- El contador del `PARA` **no** se inicializa antes.

### Criterio de elección

Cantidad de vueltas conocida → `PARA`. Depende de un dato leído → `MIENTRAS`. Tiene que ejecutarse al menos una vez (menús, cargas interactivas) → `REPETIR`.

---

## 8. Subacciones

### Función — devuelve **un** valor

```
FUNCION car_ent(c : caracter) : entero ES
    Ambiente
        // locales
    Proceso
        SEGUN c HACER
            "0" : car_ent := 0
            "1" : car_ent := 1
            ...
        FIN_SEGUN
FIN_FUNCION
```

El retorno se asigna **al nombre de la función**. La lista de parámetros no puede estar vacía. Se invoca dentro de una expresión: `SI (multi_11(y)) ENTONCES`.

### Procedimiento — no devuelve valor

```
PROCEDIMIENTO tratar_registro ES
    // sin Ambiente si no hay locales
    cont := cont + 1
FIN_PROCEDIMIENTO
```

Se invoca **por su nombre solo**: `tratar_registro`. Con parámetros: `MODIF_BAJA(acc)`.

### Paso de parámetros

- **Por valor** (por defecto): se copia; los cambios no salen.
- **Por referencia**: prefijo `var` en el parámetro formal. Los cambios sí afectan al original.

```
PROCEDIMIENTO carga_vector(var X : ARREGLO[1..10] de entero) ES
```

### Ámbito

Local = declarada en la subacción, visible solo ahí. Global = declarada en el `Ambiente` de la acción, visible desde todas las subacciones. **Las plantillas de corte de control dependen de que contadores y resguardos sean globales.**

---

## 9. Arreglos

```
V : ARREGLO[1..10] de entero
M : ARREGLO[1..3, 1..3] de entero
```

- Colección **finita, homogénea y ordenada**; tamaño fijo, no cambia en ejecución.
- Cantidad de componentes = `ls - li + 1`
- Acceso: `V[i]`, `M[i,j]` (fila, columna)
- Se recorren con `PARA`; matrices con `PARA` anidados.

```
PARA i := 1 HASTA 3 HACER
    PARA j := 1 HASTA 3 HACER
        LEER(M[i,j])
    FIN_PARA
FIN_PARA
```

---

## 10. Operadores

| Categoría | Operadores |
|---|---|
| Aritméticos | `+` `-` `*` `/` `MOD` `DIV` `**` (potencia) |
| Relacionales | `=` `<>` `>` `>=` `<` `<=` |
| Lógicos | `Y` `O` `NO` |
| Pertenencia | `EN` → `SI (v EN consonantes) ENTONCES` |
| Asignación | `:=` |

**Prioridad** (de mayor a menor): `()` → `NO` → `*` `/` `MOD` `DIV` → `+` `-` → relacionales → `Y` `O`.

Funciones auxiliares que aparecen en consignas: `ABSO(n)` valor absoluto, `car_ent(c)` / `ConvertirANumero(c)` carácter a entero (hay que escribirla).

---

## 11. Entrada / salida por pantalla

```
ESCRIBIR("texto: ", variable, " más texto")
LEER(a, b, c)                   // varias variables de una
```

Variante abreviada en plantillas de cátedra: `ESC(...)`. Comillas simples o dobles, indistinto, pero ser consistente.

---

## 12. Convenciones internas

| Usar | No usar |
|---|---|
| `:=` para asignar | `=` para asignar |
| `<>` | `!=` |
| Palabras clave en MAYÚSCULA | mezclar en el mismo archivo |
| `FIN_SEGUN` (mayúsculas, sin acento en el código) | — |
| Cerrar toda estructura abierta | — |
| Un solo registro notacional por archivo | mezclar `Proceso`/`Algoritmo`, `SINO`/`Contrario` |
