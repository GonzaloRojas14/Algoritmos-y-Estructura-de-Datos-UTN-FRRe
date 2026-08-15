# Sintaxis y teoría — AyED UTN-FRRe

> ## ⚠️ Este documento quedó desactualizado
>
> La **sintaxis de pseudocódigo** ahora vive en el skill `pseudocodigo-utn`, alimentado con las
> **plantillas oficiales de cátedra** (repo `UTN-FRRe/isi-aed`, carpeta `Pseudocodigo/`):
>
> - `.claude/skills/pseudocodigo-utn/references/sintaxis-completa.md`
> - `.claude/skills/pseudocodigo-utn/references/plantillas.md`
> - `.claude/skills/pseudocodigo-utn/references/errores-y-trampas.md`
>
> **Varias "correcciones" de la sección 13 de este archivo eran equivocadas.** Estaban deducidas
> del libro, pero las plantillas oficiales usan otra notación, y en esos puntos coincide con la
> que ya venías escribiendo:
>
> | Este doc decía | Lo correcto (plantillas oficiales) |
> |---|---|
> | ~~`GRABAR(arch, reg)`~~ | **`ESCRIBIR(arch, reg)`** — como escribías |
> | ~~no existe `SI EXISTE`~~ | **`SI EXISTE ENTONCES`** es la forma oficial en indexados |
> | ~~no existe `ELIMINAR`~~ | **`ELIMINAR(arch, reg)`** existe, para baja física |
> | ~~`Abrir S/(Arch)`~~ | **`ABRIR /S(arch)`** — como escribías |
> | ~~`REGRABAR`~~ | **`RE-ESCRIBIR`** (tu `REESCRIBIR` era casi correcto) |
> | ~~`PARA ... ; incremento`~~ | **`PARA i := 1 HASTA 10, 1 HACER`** — con coma |
>
> Lo que sigue **sirve para la teoría** (capítulos del libro: conceptos, clasificaciones,
> definiciones). Para escribir código, usar el skill.

---

Referencia de teoría de la materia.

**Fuente**: *Algoritmos y Estructuras de Datos — Apuntes de Cátedra*, Pinto & Bolatti, 2026 (9 capítulos).

| Marca | Significado |
|---|---|
| ✅ | Respaldado por el libro de cátedra (con capítulo indicado) |
| 🔶 | Inferido de los ejercicios; **el libro no lo cubre** |
| ❓ | Vacío conocido |

Índice: [1 Fundamentos](#1-fundamentos-cap-1) · [2 Control](#2-estructuras-de-control-cap-2) · [3 Subacciones](#3-subacciones-cap-3) · [4 Secuencias](#4-secuencias-cap-4) · [5 Registros y archivos](#5-registros-y-archivos-cap-5) · [6 Indexados](#6-archivos-indexados-cap-6) · [7 Corte de control](#7-corte-de-control-) · [8 Apareo](#8-apareo-maestro-movimientos-) · [9 Arreglos](#9-arreglos-) · [10 Dinámicas](#10-estructuras-dinámicas-cap-7) · [11 Recursividad](#11-recursividad-cap-8) · [12 Complejidad](#12-complejidad-algorítmica-cap-9) · [13 Notación](#13-notación-oficial-vs-la-que-venís-usando) · [14 Errores](#14-catálogo-de-errores-frecuentes) · [15 Pendientes](#15-pendientes)

---

## 1. Fundamentos (Cap. 1) ✅

### Qué es un algoritmo

Secuencia **finita, precisa y no ambigua** de instrucciones que, dado un conjunto de datos de entrada, produce un resultado de salida en tiempo finito.

**Características** (van casi seguro en el teórico):

| Característica | Significado |
|---|---|
| Precisión | Cada paso indica con claridad qué debe hacerse |
| Determinismo | Dos ejecuciones con los mismos datos → mismo resultado |
| Finitud | Termina en un número finito de pasos |
| Corrección | El resultado obtenido es el esperado |
| Independencia del lenguaje | Se puede expresar en cualquier notación |

### Proceso, acción y estado

- **Proceso**: unidad mínima de trabajo planificable por el SO; secuencia de instrucciones con estado y recursos.
- **Acción**: paso concreto con actor, duración finita y resultado definido.
  - **Simple**: se realiza directamente, sin descomponer.
  - **Compleja**: requiere descomposición en acciones de menor complejidad.
- **Estado**: condición de los datos en un momento de la ejecución. Cada acción lo transforma: hay un **estado antes (precondición)** y uno **después (postcondición)**.

### Representación

Dos herramientas: **diagrama de flujo** (gráfico, símbolos normalizados) y **pseudocódigo** (textual).

Ventajas del pseudocódigo: representa repeticiones complejas con claridad, se transforma fácil a cualquier lenguaje, y si se respetan las reglas **los niveles de anidamiento quedan visibles**.

La **programación estructurada** sostiene que todo algoritmo se escribe con solo tres estructuras: secuencial, condicional y repetitiva.

### Tipos de datos

| Tipo | Contiene | Ejemplos |
|---|---|---|
| `entero` | números sin decimales | 10, -3, 0, 500 |
| `real` | números con decimales | 3.14, -0.5 |
| `alfanumerico` | texto | "Hola", "AED2024" |
| `logico` | dos valores | V, F |

Declaración: `nombre_variable : tipo_de_dato`

```
edad : entero
precio : real
nombre : alfanumerico
```

**Variable**: posición de memoria cuyo valor **puede cambiar** durante la ejecución.
**Constante**: ocupa memoria igual, pero su valor **no puede modificarse**. Se usa para valores fijos que se repiten.

### Operadores

| Categoría | Operadores | Resultado |
|---|---|---|
| Aritméticos | `+ - * / MOD DIV` | Numérico |
| Relacionales | `= <> > >= < <=` | Lógico (V/F) |
| Lógicos | `Y` (AND), `O` (OR), `NO` (NOT) | Lógico (V/F) |
| Asignación | `:=` | Asigna valor a variable |

### Prioridad de operadores

De mayor a menor. **Esto se pregunta y se olvida.**

1. Paréntesis `()`
2. Negación lógica `NO`
3. `*` `/` `MOD` `DIV`
4. `+` `-`
5. Relacionales `=` `<>` `>` `>=` `<` `<=`
6. Lógicos `Y` `O`

> Consecuencia práctica: `a > b Y c > d` se evalúa bien sin paréntesis, porque los relacionales tienen más prioridad que `Y`.

### Prueba de escritorio

Verificación **manual**: se toman datos concretos, se sigue la secuencia paso a paso y se registra el estado de cada variable en una tabla.

```
1. a := 2
2. b := 3
3. suma := a + b
4. suma := suma + 1
```

| Estado | a | b | suma |
|---|---|---|---|
| E₀ (inicial) | ? | ? | ? |
| E₁ (tras paso 1) | 2 | ? | ? |
| E₂ (tras paso 2) | 2 | 3 | ? |
| E₃ (tras paso 3) | 2 | 3 | 5 |
| E₄ (tras paso 4) | 2 | 3 | 6 |

Las variables arrancan en `?` (indefinidas), no en 0.

---

## 2. Estructuras de control (Cap. 2) ✅

### Esqueleto de una ACCION

```
ACCION Ejemplo1 ES
    AMBIENTE
        a, doble : entero
    PROCESO
        ESCRIBIR('Ingrese el número')
        LEER(a)
        doble := a * 2
        ESCRIBIR('Resultado: ', doble)
FIN_ACCION
```

> ⚠️ **Corrección respecto de lo que veníamos usando**: el libro **no cierra con `FIN_PROCESO`**. Va del cuerpo directo a `FIN_ACCION`. Varios de tus archivos ponen `FIN_PROCESO` y otros no — ahora hay criterio: no lleva.

- El nombre no lleva puntos: `ACCION ej_2_2_4 ES`, no `ACCION 2.2.4 ES`.
- `AMBIENTE` va siempre, aunque quede vacío.

### Condicional

```
SI condicion ENTONCES
    ...
SINO
    ...
FIN_SI
```

Sin dos puntos después de `ENTONCES`.

### Condicional múltiple

```
SEGÚN suma HACER
    = 0 : ESCRIBIR('El resultado es igual a 0')
    < 0 : ESCRIBIR('El resultado es menor a 0')
    > 0 : ESCRIBIR('El resultado es mayor a 0')
FIN_SEGÚN
```

Dos cosas que corregir de lo anterior:

- Lleva **acento**: `SEGÚN` / `FIN_SEGÚN`.
- Las ramas **pueden ser condiciones relacionales**, no solo valores literales. Tu `1.8.txt` con `<= 50:` estaba bien.

Se usa para evitar la cascada de `SI` anidados cuando hay más de dos alternativas.

### Ciclos

| Estructura | Cuándo evalúa | Vueltas | Clasificación |
|---|---|---|---|
| `MIENTRAS cond HACER ... FIN_MIENTRAS` | **antes** del cuerpo | 0 o más | Pre-test, **indefinida** |
| `REPETIR ... HASTA QUE cond` | **después** del cuerpo | 1 o más | Post-test, **indefinida** |
| `PARA i := inicio HASTA fin; incremento HACER ... FIN_PARA` | — | conocidas de antemano | Ciclo **definido** |

```
PARA contador := inicio HASTA fin; incremento HACER
    <acciones>
FIN_PARA
```

- La cláusula `; incremento` es parte de la sintaxis (se omite cuando el paso es 1).
- En el `PARA`, **el contador se incrementa automáticamente y no hace falta inicializarlo antes** del bucle.

> ⚠️ **Bucles infinitos**: ocurren cuando la condición de salida nunca se cumple. Verificar siempre que dentro del ciclo haya alguna instrucción que modifique las variables de la condición de corte.

---

## 3. Subacciones (Cap. 3) ✅

Dividir un problema en subproblemas es **diseño top-down**. Cada subproblema se implementa como una subacción.

**Control de ejecución**: el algoritmo principal se detiene cuando delega en una subacción, y retoma cuando esta termina.

### Parámetros

| Tipo | También llamados | Dónde aparecen |
|---|---|---|
| **Formales** | ficticios | en la **DEFINICIÓN** de la subacción |
| **Actuales** | argumentos | en la **LLAMADA** a la subacción |

### Función

Realiza un cómputo y devuelve **UN ÚNICO valor**. Su lista de parámetros **NO puede estar vacía**.

```
FUNCION ES_PRIMO(A : entero) : logico
    AMBIENTE
        i : entero
    PROCESO
        ES_PRIMO := V
        PARA i := 2 HASTA (A - 1) HACER
            SI A MOD i = 0 ENTONCES
                ES_PRIMO := F
            FIN_SI
        FIN_PARA
FIN_FUNCION
```

El valor de retorno se asigna **al nombre de la función**.

### Procedimiento

Ejecuta acciones pero **NO devuelve un valor**. Se invoca como instrucción independiente.

```
PROCEDIMIENTO Login(usu, pass, valid : alfanumerico)
    SI pass = valid ENTONCES
        ESCRIBIR('Acceso autorizado a ', usu)
    SINO
        ESCRIBIR('Login inválido para ', usu)
    FIN_SI
FIN_PROCEDIMIENTO
```

En el libro, el procedimiento sin variables locales **omite el bloque `AMBIENTE`/`PROCESO`** y va directo al cuerpo. La función sí los lleva.

### Ámbito de variables

| Tipo | Definidas en | Accesibles desde | Duración |
|---|---|---|---|
| **Local** | la subacción | solo esa subacción | mientras dura la subacción |
| **Global** | el algoritmo principal | principal + todas las subacciones | toda la ejecución |

### Paso de parámetros

- **Por valor**: se copia el valor de la variable original. La subacción trabaja con la copia; los cambios **no afectan** al original.
- ❓ **Por referencia**: el libro lo anuncia en 3.6 pero la sección quedó incompleta. Falta.

---

## 4. Secuencias (Cap. 4) ✅

Conjunto de datos relacionados que se procesan en **orden estricto**: primero el inicial, después sus sucesores, hasta el final.

### Las cuatro propiedades

1. **Existencia del primer elemento** — acceder al primero habilita el acceso a los demás.
2. **Relación de sucesión** — cada elemento (salvo el último) tiene un sucesor único.
3. **Finitud** — siempre termina, acotada por una condición de fin o una marca (**FDS**, Fin De Secuencia).
4. **Existencia del último elemento** — hay un indicador de fin que permite detener el procesamiento.

> Una secuencia **NO tiene tamaño fijo predefinido**. Su longitud puede variar durante la ejecución del algoritmo que la crea o la procesa.

### Verbos

| Verbo (libro) | Propósito |
|---|---|
| `ARR(sec)` | **Arrancar** — inicializar el recorrido de una secuencia existente |
| `AVZ(sec, v)` | **Avanzar** — leer el elemento actual y pasar al siguiente |
| `CREAR(secNueva)` | Crear una secuencia nueva vacía |
| `ESC(sec, v)` | Escribir un elemento en la secuencia |

El libro usa las formas abreviadas. Tus archivos usan `ARRANCAR` / `AVANZAR` / `ESCRIBIR` — ver [§13](#13-notación-oficial-vs-la-que-venís-usando).

### Esquema básico

```
ARR(sec)
AVZ(sec, elem)                    // leer el primer elemento
MIENTRAS elem <> FDS HACER
    <procesar elem>
    AVZ(sec, elem)                // avanzar al siguiente
FIN_MIENTRAS
```

`ARR` + `AVZ` van **siempre juntos**: arrancar sin avanzar deja la ventana vacía.

### Subsecuencias

Conjunto de elementos **consecutivos** dentro de la secuencia principal, que forman un subgrupo con significado propio.

Ejemplos: **palabra** (empieza con carácter distinto de espacio, termina en espacio), **oración** (termina en punto), **DNI** (8 caracteres numéricos consecutivos).

| Relación | Descripción |
|---|---|
| **Enlazadas** | Las subsecuencias van una a continuación de la otra |
| **Jerárquicas (inclusión)** | Una subsecuencia contiene a otra (oración contiene palabras) |

### Las tres reglas que se caen en el parcial 🔶

No están en el libro como reglas explícitas, pero salen de aplicar el esquema y son lo que más te falló:

1. **AVANCE VITAL**: al salir de un ciclo que buscaba un delimitador, la ventana **está parada en el delimitador**. Hay que avanzar una vez más para superarlo.

   ```
   MIENTRAS elem <> FDS Y elem <> '&' HACER
       AVZ(sec, elem)
   FIN_MIENTRAS
   AVZ(sec, elem)            // ← superar el '&'
   ```

2. **Guarda de fin en todo ciclo interno**: `MIENTRAS elem <> FDS Y elem <> '&'`, nunca solo `elem <> '&'`. Si la cinta se termina sin el delimitador, el ciclo sin guarda no corta nunca.

3. **Dónde inicializar**: contadores y máximos de un nivel se inicializan **al empezar cada elemento de ese nivel**. Los máximos globales, una sola vez al principio (`max := -1`).

### Subsecuencias jerárquicas de tres niveles

```
MIENTRAS elem <> FDS HACER                              // texto
    MIENTRAS elem <> FDS Y elem <> '.' HACER            // oración
        MIENTRAS elem <> FDS Y elem = ' ' HACER         // saltar espacios
            AVZ(sec, elem)
        FIN_MIENTRAS
        SI elem <> '.' ENTONCES
            cont_pal := cont_pal + 1
            MIENTRAS elem <> FDS Y elem <> ' ' Y elem <> '.' HACER   // palabra
                AVZ(sec, elem)
            FIN_MIENTRAS
        FIN_SI
    FIN_MIENTRAS
    SI elem = '.' ENTONCES AVZ(sec, elem) FIN_SI        // superar el '.'
FIN_MIENTRAS
```

### Leer un número de N dígitos de una cinta de caracteres

```
num := car_a_ent(elem) * 100
AVZ(sec, elem)
num := num + car_a_ent(elem) * 10
AVZ(sec, elem)
num := num + car_a_ent(elem)
AVZ(sec, elem)                    // ← el avance de cierre también va
```

---

## 5. Registros y archivos (Cap. 5) ✅

### Campo

**Entidad lógica mínima** de información: conjunto de bytes que conforman un dato con significado propio. Se define con **tres atributos obligatorios**:

| Atributo | Descripción | Ejemplo |
|---|---|---|
| **Nombre** | identifica el campo dentro del registro; único y representativo | `apellido`, `dni` |
| **Tipo** | clase del dato: entero, real, alfanumérico, lógico, fecha | `entero`, `ALFA` |
| **Tamaño** | cantidad máxima de bytes o caracteres | `N(8)`, `ALFA(30)`, `R(6,2)` |

En archivos de **longitud fija**, si se reservan 30 caracteres y el dato ocupa 12, los 18 restantes se rellenan con blancos. Eso garantiza que todos los registros midan igual y permite acceso directo por posición.

### Por qué hacen falta los campos

Guardar datos como una cadena continua no permite distinguir dónde termina un dato y empieza el otro. Dos soluciones:

| Solución | Ventaja | Desventaja |
|---|---|---|
| **Marcas separadoras** (`*`, `%`, `#` entre campos) | Ocupa el mínimo espacio posible | Hay que recorrer la secuencia para separar campos; dificulta el acceso directo |
| **Campos de longitud fija** | Acceso directo por posición; aritmética directa sobre campos numéricos | Si un campo necesita más espacio, hay que redefinir todos los registros |

Los archivos de datos estructurados usan **longitud fija**.

### Registro

Tipo de dato **estructurado** formado por un conjunto de campos que forman una unidad lógica. Representa una entidad del mundo real.

```
AMBIENTE
    RegPersona = REGISTRO
        nombre    : ALFA(30)
        domicilio : ALFA(20)
        localidad : ALFA(15)
        edad      : entero
        salario   : real
    FIN_REGISTRO

    persona : RegPersona        // variable del tipo registro
```

- Se define en el `AMBIENTE` **como un tipo nuevo**; después hay que declarar la variable.
- Acceso con selector `.` → `persona.salario := persona.salario * 1.10`
- **Aunque tiene varios campos, se lo trata como UNA SOLA entidad**: al leer o escribir en un archivo se opera con el registro completo, nunca con campos sueltos.
- **Clave compuesta**: campo continente que agrupa varios campos.

> ⚠️ **Orden de los campos en FECHA** 🔶: declarar `aa, mm, dd` (mayor a menor). Solo así funciona comparar registros enteros (`SI f1 > f2`). Lo hiciste bien en `2.2.2.txt` y al revés en `Parcial.1.txt`. El libro no lo dice; sale de cómo funciona la comparación.

### Archivo

Conjunto de registros almacenados de forma **permanente en memoria externa**.

**Características generales:**

- **Persistencia** — la información sobrevive a la finalización del programa.
- **Independencia de datos** — los datos son independientes de los algoritmos que los procesan; distintos programas pueden acceder al mismo archivo.
- **Capacidad** — permiten volúmenes que no entrarían en RAM.
- **Unidad de E/S** — la unidad básica de lectura/escritura es **el registro completo**. No se puede leer medio registro.
- **Intercambio con memoria interna** — el procesamiento siempre ocurre en RAM; el archivo es fuente y/o destino.

### Operaciones

| Operación | Sintaxis | Descripción |
|---|---|---|
| Abrir lectura | `Abrir E/(Arch)` | Abre para leer; el puntero queda en el primer registro |
| Abrir escritura | `Abrir S/(Arch)` | Crea (o sobreescribe) el archivo para grabar registros nuevos |
| Abrir lectura/escritura | `Abrir E/S(Arch)` | Permite leer y modificar en el mismo archivo |
| Leer registro | `LEER(Arch, Reg)` | Lee el registro actual y avanza el puntero |
| **Grabar registro** | `GRABAR(Arch, Reg)` | Escribe `Reg` en `Arch` |
| Cerrar | `CERRAR(Arch)` | Cierra el archivo y libera el buffer |
| Fin de archivo | `FDA(Arch)` | Función: V cuando no hay más registros |

> ⚠️ **Dos correcciones importantes respecto de tus archivos:**
> 1. Es **`Abrir S/(Arch)`**, con la barra **después** de la S — igual que `E/`. La barra es un separador, no indica posición. Tus archivos escriben `Abrir /S(...)`.
> 2. Para grabar en un archivo el verbo es **`GRABAR`**, no `ESCRIBIR`. `ESCRIBIR` es para pantalla y para secuencias.

> ⚠️ Olvidar `CERRAR` puede provocar **pérdida de datos**: los últimos registros escritos quedan en el buffer y no se vuelcan al disco.

### Esquema de recorrido secuencial

```
Abrir E/(Arch)
LEER(Arch, Reg)                   // leer el primer registro
MIENTRAS NO FDA(Arch) HACER
    <procesar Reg>
    LEER(Arch, Reg)               // leer el siguiente ← última instrucción del ciclo
FIN_MIENTRAS
CERRAR(Arch)
```

El patrón es **abrir → leer → controlar → procesar → leer → cerrar**. Sin el `LEER` final del ciclo es ciclo infinito.

### Consistencia y congruencia

Tema teórico puro, muy examinable, y no estaba en ningún archivo tuyo.

**Consistencia** — cada valor almacenado en un campo es **válido según la definición de ese campo**. Se verifica **campo por campo, de forma aislada**.

- *Automática*: el sistema impone restricciones por tipo. Un campo `entero` no puede contener texto.
- *Por rango o conjunto*: el programador agrega validaciones. Edad entre 0 y 120; mes entre 1 y 12.

**Congruencia** — los datos son **coherentes entre sí**. Es una propiedad **relacional**: requiere comparar dos o más datos.

| Tipo | Alcance | Ejemplo |
|---|---|---|
| **Gruesa** | entre datos del **mismo registro** | fecha 31/02/1990: febrero no tiene 31 días |
| **Fina** | entre datos de **distintos archivos** | DNI en ALUMNOS que no existe en PADRÓN ELECTORAL |

**Las dos reglas:**

> **REGLA 1** — Si un dato NO es consistente, **tampoco puede ser congruente**. Un valor fuera de tipo es inválido antes incluso de compararlo.
>
> **REGLA 2** — Si un dato ES consistente, eso **NO garantiza** que sea congruente. La fecha 31/02/2024 pasa la validación de rango (1–31) pero es incongruente.

### Clasificación de archivos

**Por utilidad / función:**

| Tipo | Contiene | Ejemplo |
|---|---|---|
| **Maestro** | información permanente y actualizada; es la **fuente de verdad** | clientes, empleados, productos |
| **Movimiento / Transacción** | los cambios o novedades a aplicar sobre el maestro | ventas del día, altas y bajas |
| **Histórico** | versiones anteriores del maestro o registros de auditoría | ventas del año anterior |
| **Auxiliar / Temporal** | intermedio, se crea durante el proceso y se elimina al terminar | resultado de un ordenamiento parcial |

**Por datos almacenados:** **texto** (caracteres legibles, `.txt`, `.csv`) y **binario** (bytes en formato propio del sistema, no legible directamente).

### Organización de archivos

Manera en que los registros están estructurados y almacenados en el soporte. Determina qué accesos son posibles.

**Soportes:** *secuenciales* (solo leen/escriben en orden, ej. cintas magnéticas) y *direccionables* (acceden a cualquier posición por dirección física, ej. disco, SSD).

| Organización | Cómo funciona | Ventaja | Desventaja |
|---|---|---|---|
| **Secuencial** | registros uno tras otro en el orden en que se grabaron; para llegar al registro *n* hay que pasar por los *n−1* anteriores | recorrido total muy eficiente | acceso puntual muy lento; no sirve para consultas interactivas |
| **Directa (o relativa)** | la posición se calcula desde la clave con una **función de dispersión (hash)**; el orden físico no coincide con el lógico | acceso puntual O(1) sin colisiones | **colisiones** (dos claves a la misma posición); el recorrido no preserva orden lógico |
| **Secuencial indexada** | área de datos + área de índices | combina ambas; la más versátil | ocupa más espacio |

Requisitos de la organización directa: soporte direccionable, campo clave único, y una función que relacione clave con dirección.

### Tipos de acceso

Concepto **independiente** de la organización, aunque no todas las combinaciones son posibles.

| Acceso | Descripción | Organizaciones compatibles |
|---|---|---|
| **Secuencial** | uno tras otro, en orden de almacenamiento; no se puede saltear | Secuencial, Indexada, Directa |
| **Directo (aleatorio)** | a un registro específico por clave o posición, sin recorrer los anteriores | Directa, Indexada |
| **Mixto** | acceso directo a un punto y desde ahí recorrido secuencial | Indexada |

---

## 6. Archivos indexados (Cap. 6) ✅

Archivo que incluye uno o más **índices** para facilitar la búsqueda. Un campo (o grupo) llamado **CLAVE** se designa como campo de índice.

### Estructura física: dos áreas

**Área de índices** — tabla de dos columnas: valor de la clave y posición física del registro en el área de datos. **SIEMPRE ordenada de menor a mayor por clave**, sin importar el orden en que se grabaron los registros.

```
CLAVE (legajo)  |  POSICIÓN en área de datos
────────────────┼───────────────────────────
1001            |  posición 3
1005            |  posición 1
1009            |  posición 5
2003            |  posición 2
```

**Área de datos** — los registros completos. **NO están necesariamente en orden de clave**: se almacenan según disponibilidad de espacio. Por eso el área de índices es indispensable.

### Proceso de acceso puntual

1. El programa establece la clave buscada: `CLAVE := valor`
2. El sistema busca esa clave en el área de índices (**búsqueda binaria, O(log n)**)
3. El índice devuelve la posición física
4. El sistema lee directamente el registro en esa posición

Con 100.000 registros: la búsqueda secuencial puede requerir hasta 100.000 lecturas; la binaria en el índice, como máximo log₂(100.000) ≈ **17 pasos**.

### Verbos comparados

| Operación | Secuencia | Archivo Secuencial | Archivo Indexado |
|---|---|---|---|
| Iniciar lectura | `ARR(sec)` | `Abrir E/(Arch)` | `Abrir E/(Arch)` o `Abrir E/S(Arch)` |
| Leer | `AVZ(sec, v)` | `LEER(Arch, Reg)` | `CLAVE := valor` ; `LEER(Arch, Reg)` |
| Iniciar escritura | `CREAR(secNueva)` | `Abrir S/(Arch)` | `Abrir S/(Arch)` |
| Escribir | `ESC(sec, v)` | `GRABAR(Arch, Reg)` | `GRABAR` o `REGRABAR(Arch, Reg)` |
| Fin de datos | `FDS` | `FDA(Arch)` | según operación |

**La diferencia clave en la lectura indexada**: hay que asignar la clave **ANTES** del `LEER`. Eso le indica al sistema qué registro buscar en el índice.

### Cómo se pregunta si el registro existe

```
Abrir E/S(archEmpleados)

CLAVE := 1005
LEER(archEmpleados, regEmp)

SI FDA(archEmpleados) ENTONCES
    ESCRIBIR('Empleado no encontrado')
SINO
    ESCRIBIR(regEmp.nombre, regEmp.salario)
FIN_SI

CERRAR(archEmpleados)
```

> ⚠️ **Corrección grande**: la existencia se pregunta con **`FDA(arch)`**, no con `SI EXISTE`.
> `SI FDA(arch)` → **no** existe. `SI NO FDA(arch)` → existe.
> Tanto tu `2.3.frre` como tu apunte de indexados usan `SI EXISTE`, que no aparece en el libro.

### GRABAR vs. REGRABAR

Distinción fundamental y fuente frecuente de errores.

| | **GRABAR** — alta | **REGRABAR** — modificación |
|---|---|---|
| Para qué | insertar un registro que **NO existía** | actualizar uno que **YA fue leído** |
| Qué hace el sistema | busca espacio en el área de datos, escribe, y **agrega la entrada al índice** en la posición correcta | **sobreescribe la misma posición física** del registro leído |
| Requisito | la clave **NO** debe existir (alta pura) | **el registro debe haber sido leído con `LEER` justo antes** |
| Índice | se modifica | no se modifica (la clave no cambia) |
| Si se viola | error de clave duplicada | error de lógica |

> ⚠️ Es **`REGRABAR`**, no `REESCRIBIR`. Tus archivos usan `REESCRIBIR`.

> **El ciclo obligatorio de una modificación es siempre:**
> 1. `Abrir E/S(Arch)`
> 2. `CLAVE := valor_buscado`
> 3. `LEER(Arch, Reg)` ← **lectura obligatoria**
> 4. Modificar campos del `Reg`
> 5. `REGRABAR(Arch, Reg)`
>
> Saltarse el paso 3 produce un error de lógica.

### Comparación secuencial vs. indexado

| Criterio | Secuencial | Indexado |
|---|---|---|
| Espacio en disco | solo los registros | registros + área de índices |
| Orden de los datos | no necesariamente ordenado | el índice siempre ordenado por clave |
| Recorrido total | muy eficiente, lectura continua | algo más lento por la doble área |
| Búsqueda puntual | muy lento, O(n) peor caso | muy rápido, O(log n) |
| Modificación | no admite regrabar | admite `REGRABAR` tras lectura |
| Uso ideal | reportes, batch, grandes volúmenes | consultas interactivas, ABM en tiempo real |

### Actualización indexada — ABM

Proceso por el cual un usuario interactivo mantiene el maestro actualizado en tiempo real: **A**lta, **B**aja, **M**odificación.

**Alta** — verificar que la clave NO exista, y recién ahí `GRABAR`:

```
PROCEDIMIENTO Alta(arch : archivo)
    LEER(nuevoCodigo)
    CLAVE := nuevoCodigo
    LEER(arch, reg)                          // verificar si ya existe
    SI NO FDA(arch) ENTONCES
        ESCRIBIR('Error: clave ya existe. No se puede dar de alta.')
    SINO
        LEER(reg.nombre, reg.salario)        // ingresar datos
        reg.codigo := nuevoCodigo
        GRABAR(arch, reg)
        ESCRIBIR('Alta realizada correctamente.')
    FIN_SI
FIN_PROCEDIMIENTO
```

**Modificación** — leer, cambiar, `REGRABAR`:

```
PROCEDIMIENTO Modificacion(arch : archivo)
    LEER(codigoBuscado)
    CLAVE := codigoBuscado
    LEER(arch, reg)
    SI FDA(arch) ENTONCES
        ESCRIBIR('Error: registro no encontrado.')
    SINO
        ESCRIBIR('Registro actual:', reg.nombre, reg.salario)
        LEER(reg.salario)
        REGRABAR(arch, reg)
        ESCRIBIR('Modificación realizada.')
    FIN_SI
FIN_PROCEDIMIENTO
```

**Baja** — dos estrategias:

- **Baja física**: se elimina el registro y se actualiza el índice. Costosa: deja "huecos" en el área de datos.
- **Baja lógica (recomendada)**: se agrega un campo indicador (`activo : logico`); al dar de baja se pone `activo := F` y se `REGRABAR`. El registro queda en el archivo pero los procesos lo ignoran.

```
PROCEDIMIENTO Baja(arch : archivo)
    LEER(codigoBuscado)
    CLAVE := codigoBuscado
    LEER(arch, reg)
    SI FDA(arch) ENTONCES
        ESCRIBIR('Error: registro no encontrado.')
    SINO SI reg.activo = F ENTONCES
        ESCRIBIR('Advertencia: el registro ya estaba dado de baja.')
    SINO
        reg.activo := F
        REGRABAR(arch, reg)
        ESCRIBIR('Baja lógica realizada para:', reg.nombre)
    FIN_SI
FIN_PROCEDIMIENTO
```

> ⚠️ **El libro no define ningún verbo `ELIMINAR`.** Tu apunte de indexados lo menciona para baja física; no tiene respaldo. Usar baja lógica.

### Características de la actualización indexada

| Característica | Por qué |
|---|---|
| **Rápida** | el acceso directo evita recorrer el archivo; cada operación es O(log n) |
| **In situ** | los cambios se aplican directo sobre el maestro, sin copia intermedia |
| **Interactiva** | el usuario ingresa datos y recibe respuesta inmediata; no es batch |
| **Insegura** | al no haber archivo intermedio, un error del usuario afecta el maestro directamente. Se recomienda auditoría (log de operaciones) |

---

## 7. Corte de control 🔶

> **El libro de cátedra NO cubre corte de control.** No hay capítulo ni sección. Lo que sigue es reconstrucción a partir de las consignas de `2.2.12.txt` y `Parcial.1.txt`, y sigue siendo el hueco más grande.
>
> Tus notas mencionan una variante con procedimientos (`tratar_corte`, `tratar_registro`) y resguardos comparados en un solo ciclo. **Sigue faltando la teoría que fije cuál se exige.**

Precondición: **el archivo tiene que estar ordenado por la clave de corte.**

### Un nivel — ciclos anidados

```
Abrir E/(arch); LEER(arch, r)
tot_general := 0

MIENTRAS NO FDA(arch) HACER
    resg := r.clave                  // RESGUARDO
    tot_nivel := 0                   // inicializar acumuladores del nivel

    MIENTRAS NO FDA(arch) Y r.clave = resg HACER
        tot_nivel := tot_nivel + r.importe        // TRATAR REGISTRO
        LEER(arch, r)
    FIN_MIENTRAS

    ESCRIBIR('Total de ', resg, ': ', tot_nivel)  // TRATAR CORTE
    tot_general := tot_general + tot_nivel        // acumular al nivel superior
FIN_MIENTRAS

ESCRIBIR('Total general: ', tot_general)
CERRAR(arch)
```

### Dos niveles — el patrón se anida

```
MIENTRAS NO FDA(arch) HACER
    resg_suc := r.sucursal
    tot_suc := 0

    MIENTRAS NO FDA(arch) Y r.sucursal = resg_suc HACER
        resg_rub := r.rubro
        tot_rub := 0

        MIENTRAS NO FDA(arch) Y r.sucursal = resg_suc Y r.rubro = resg_rub HACER
            tot_rub := tot_rub + r.importe
            LEER(arch, r)
        FIN_MIENTRAS

        ESCRIBIR('Rubro ', resg_rub, ': ', tot_rub)
        tot_suc := tot_suc + tot_rub
    FIN_MIENTRAS

    ESCRIBIR('Sucursal ', resg_suc, ': ', tot_suc)
    tot_gral := tot_gral + tot_suc
FIN_MIENTRAS
```

**Las cuatro cosas que hay que ubicar bien**, siempre las mismas:

| | Dónde va |
|---|---|
| Resguardo | primera línea **dentro** del ciclo de ese nivel |
| Inicializar acumulador | junto al resguardo |
| Condición del ciclo interno | compara **todos los niveles desde el más externo** hasta el actual |
| Acumular hacia arriba | después de tratar el corte, antes de cerrar el ciclo |

---

## 8. Apareo maestro-movimientos 🔶

> **El libro tampoco cubre el algoritmo de apareo.** El Cap. 5 define los *tipos* de archivo maestro/movimiento, pero no el proceso de actualización batch. Reconstruido desde la consigna de `Ejercicios Peralta/2.1.19`.

Dos archivos ordenados por la misma clave, recorridos en paralelo comparando claves:

```
Abrir E/(mae); LEER(mae, m)
Abrir E/(mov); LEER(mov, v)
Abrir S/(sal)

MIENTRAS NO FDA(mae) O NO FDA(mov) HACER
    SI m.clave < v.clave ENTONCES          // solo en maestro → pasa igual
        sal := m; GRABAR(arch_sal, sal)
        LEER(mae, m)
    SINO
        SI m.clave = v.clave ENTONCES      // en los dos → aplicar el movimiento
            SEGÚN v.cod_mov HACER
                = 1 : ESCRIBIR('Error: alta de algo que ya existe')
                = 2 : // baja
                = 3 : // modificación
            FIN_SEGÚN
            LEER(mov, v)
        SINO                                // solo en movimientos → alta
            SI v.cod_mov = 1 ENTONCES
                // armar el registro nuevo y grabarlo
            SINO
                ESCRIBIR('Error: baja/modificación de algo inexistente')
            FIN_SI
            LEER(mov, v)
        FIN_SI
    FIN_SI
FIN_MIENTRAS
```

❓ Falta definir cómo trata la cátedra el **fin desparejo** de los dos archivos (clave alta ficticia vs. ciclos de vaciado).

---

## 9. Arreglos 🔶

> **El libro no tiene capítulo de arreglos.** Solo los menciona al pasar en el Cap. 7 ("los arreglos tienen un número máximo de elementos declarado en el ambiente"). Lo que sigue viene de tu apunte `Arreglos:`.

```
v : ARREGLO[1..50] DE entero            // vector
m : ARREGLO[1..10, 1..5] DE real        // matriz
```

- Colección **finita, homogénea y ordenada**. Vive en memoria interna; el tamaño **no cambia en ejecución**.
- Cantidad de componentes = `límite_superior − límite_inferior + 1`.
- Acceso por índice: `v[i]`, `m[i,j]` (fila, columna).
- Se recorren con `PARA`, porque la cantidad de vueltas se conoce.

```
PARA i := 1 HASTA 10 HACER
    PARA j := 1 HASTA 5 HACER
        LEER(m[i,j])
    FIN_PARA
FIN_PARA
```

---

## 10. Estructuras dinámicas (Cap. 7) ✅

Tema **completamente ausente** de tus archivos y del documento anterior.

### Estáticas vs. dinámicas

| Criterio | Estáticas | Dinámicas |
|---|---|---|
| Tamaño | fijo en tiempo de diseño | variable en tiempo de ejecución |
| Memoria | se reserva de una sola vez al inicio | se reserva y libera **nodo a nodo**, a demanda |
| Ejemplos | variables, arreglos, registros | listas enlazadas, pilas, colas, árboles |
| Acceso | directo por índice o nombre | **secuencial**: hay que recorrer desde el inicio |
| Inserción / eliminación | costosa: hay que desplazar elementos | eficiente: solo se modifican punteros |

### El nodo

Unidad básica. Tiene **área de datos** (la información útil) y **puntero(s)** (referencias a otros nodos).

```
AMBIENTE
    NODO = REGISTRO
        dato : N(5)                  // área de datos
        prox : PUNTERO a NODO        // enlace al siguiente
    FIN_REGISTRO

    PRIM : PUNTERO a NODO            // puntero externo: apunta al primer nodo
```

- **Punteros internos**: forman parte del nodo (`prox`, `ant`). Establecen los enlaces.
- **Punteros externos**: se declaran fuera (`PRIM`, `ULT`, `aux`). Manipulan la lista desde afuera.
- **`NULO`**: indica que no hay nodo siguiente. Es el marcador de fin de lista.

**Sintaxis de desreferencia**: el asterisco antepuesto accede al contenido del nodo apuntado.

```
*aux.dato        // el dato del nodo al que apunta aux
*q.prox := PRIM  // asignar al campo prox del nodo apuntado por q
```

**Verbos**: `NUEVO(q)` reserva memoria para un nodo; `BORRAR(p)` la libera.

> La conexión entre nodos se establece **por punteros, no por proximidad física** en memoria. Dos nodos consecutivos en la lista pueden estar en posiciones alejadísimas.

### Lista simplemente enlazada

**Recorrer:**

```
aux := PRIM
MIENTRAS aux <> NULO HACER
    ESCRIBIR(*aux.dato)
    aux := *aux.prox
FIN_MIENTRAS
```

**Insertar al inicio** — O(1), la más eficiente:

```
NUEVO(q)
LEER(*q.dato)
*q.prox := PRIM        // el nuevo apunta al antiguo primero
PRIM := q              // PRIM apunta al nuevo
```

**Insertar al final** — O(n) sin puntero `ULT`; O(1) si se mantiene uno:

```
NUEVO(q)
LEER(*q.dato)
*q.prox := NULO
SI PRIM = NULO ENTONCES              // lista vacía
    PRIM := q
SINO
    aux := PRIM
    MIENTRAS *aux.prox <> NULO HACER
        aux := *aux.prox
    FIN_MIENTRAS
    *aux.prox := q
FIN_SI
```

**Insertar en orden ascendente** — con dos punteros, `p` (actual) y `ant` (anterior):

```
NUEVO(q)
LEER(valor)
*q.dato := valor

p := PRIM; ant := NULO
MIENTRAS (p <> NULO) Y (valor > *p.dato) HACER
    ant := p
    p := *p.prox
FIN_MIENTRAS

SI p = PRIM ENTONCES                 // insertar al inicio
    *q.prox := PRIM
    PRIM := q
SINO
    *ant.prox := q
    *q.prox := p
FIN_SI
```

**Eliminar por valor:**

```
p := PRIM; ant := NULO
MIENTRAS (p <> NULO) Y (*p.dato <> valorBuscado) HACER
    ant := p
    p := *p.prox
FIN_MIENTRAS

SI p <> NULO ENTONCES                // se encontró
    SI ant = NULO ENTONCES
        PRIM := *p.prox              // era el primero
    SINO
        *ant.prox := *p.prox         // saltear el nodo
    FIN_SI
    BORRAR(p)
SINO
    ESCRIBIR('Elemento no encontrado')
FIN_SI
```

### Pilas (LIFO)

Lista lineal con **restricción de acceso**: solo se accede al **último elemento insertado**. Política **LIFO** (Last In, First Out). El punto de acceso único es el **tope** (o cima).

Ejemplos: pila de platos, historial de navegación (botón Atrás), pila de llamadas a funciones.

| Operación | Descripción | Complejidad |
|---|---|---|
| **APILAR** (push) | insertar en el tope; equivale a insertar al inicio | O(1) |
| **DESAPILAR** (pop) | extraer y devolver el del tope; la pila no puede estar vacía | O(1) |
| **VER TOPE** (peek) | consultar el tope sin extraerlo | O(1) |
| **ESTÁ VACÍA** | verificar si no tiene elementos | O(1) |

```
// El TOPE es el primer nodo de la lista (PRIM)

PROCEDIMIENTO APILAR(valor)
    NUEVO(q)
    *q.dato := valor
    *q.prox := PRIM        // el nuevo apunta al anterior tope
    PRIM := q              // el nuevo tope es el nuevo nodo
FIN_PROCEDIMIENTO

FUNCION DESAPILAR() : tipo_dato
    SI PRIM = NULO ENTONCES
        ESCRIBIR('Error: pila vacía')
    SINO
        aux := PRIM
        valor := *aux.dato
        PRIM := *PRIM.prox // el tope pasa al siguiente
        BORRAR(aux)
        DESAPILAR := valor
    FIN_SI
FIN_FUNCION
```

**Aplicaciones clásicas**: verificación de paréntesis balanceados, evaluación de expresiones postfijas (notación polaca inversa), recursividad, deshacer/rehacer.

### Colas (FIFO)

Lista lineal con **restricción en ambos extremos**: se inserta por el **fondo** y se extrae por el **frente**. Política **FIFO** (First In, First Out).

Ejemplos: fila en un banco, cola de impresión, cola de procesos del SO.

| Operación | Descripción | Complejidad |
|---|---|---|
| **ENCOLAR** (enqueue) | insertar en el fondo | O(1) **con puntero al último** |
| **DESENCOLAR** (dequeue) | extraer del frente | O(1) |
| **VER FRENTE** (peek) | consultar el frente sin extraerlo | O(1) |
| **ESTÁ VACÍA** | verificar si no tiene elementos | O(1) |

Para que `ENCOLAR` sea O(1) hacen falta **dos punteros externos**: `PRIM` (frente) y `ULT` (fondo). Sin `ULT` habría que recorrer toda la lista: O(n).

```
PROCEDIMIENTO ENCOLAR(valor)
    NUEVO(q)
    *q.dato := valor
    *q.prox := NULO
    SI PRIM = NULO ENTONCES        // cola vacía
        PRIM := q
        ULT  := q
    SINO
        *ULT.prox := q             // conectar al último actual
        ULT := q                   // actualizar el puntero al último
    FIN_SI
FIN_PROCEDIMIENTO

FUNCION DESENCOLAR() : tipo_dato
    SI PRIM = NULO ENTONCES
        ESCRIBIR('Error: cola vacía')
    SINO
        aux := PRIM
        valor := *aux.dato
        PRIM := *PRIM.prox
        SI PRIM = NULO ENTONCES    // la cola quedó vacía
            ULT := NULO
        FIN_SI
        BORRAR(aux)
        DESENCOLAR := valor
    FIN_SI
FIN_FUNCION
```

> El `SI PRIM = NULO ENTONCES ULT := NULO` al desencolar es el detalle que más se olvida: si no se hace, `ULT` queda apuntando a un nodo borrado.

### Lista doblemente enlazada

Cada nodo tiene **dos** punteros: al siguiente y al anterior. Permite recorrer en ambos sentidos y eliminar sin necesitar un puntero al anterior.

```
NODO = REGISTRO
    dato : tipo
    ant  : PUNTERO a NODO        // enlace al ANTERIOR
    prox : PUNTERO a NODO        // enlace al SIGUIENTE
FIN_REGISTRO

PRIM : PUNTERO a NODO
ULT  : PUNTERO a NODO

// El puntero ant del PRIM siempre vale NULO
// El puntero prox del ULT siempre vale NULO
```

Al insertar hay que actualizar **CUATRO** punteros (en lugar de dos): el `prox` y el `ant` del nuevo nodo, más el `ant` del sucesor y el `prox` del predecesor.

### Comparación

| Estructura | Inserción | Extracción | Búsqueda | Uso típico |
|---|---|---|---|---|
| Lista simple (inicio) | O(1) | O(1) si es la cabeza | O(n) | colecciones ordenables con acceso secuencial |
| Lista simple (final) | O(n) sin ULT; O(1) con ULT | O(n) | O(n) | colas, buffers |
| Lista doble | O(1) al inicio/final | O(1) al inicio/final | O(n) | historial, editores de texto, eliminación frecuente |
| **Pila** (LIFO) | O(1) | O(1) solo del tope | no aplica | recursividad, deshacer/rehacer, compiladores |
| **Cola** (FIFO) | O(1) por el fondo | O(1) por el frente | no aplica | sistemas de atención, colas de impresión, procesos |

---

## 11. Recursividad (Cap. 8) ✅

Técnica en la que un algoritmo **se invoca a sí mismo**, reduciendo el problema a un caso más simple del mismo problema.

### Las dos partes

| Parte | Descripción |
|---|---|
| **Caso base** | el caso trivial que se resuelve **directamente, sin llamada recursiva**. Toda recursión debe tener al menos uno |
| **Caso recursivo** | la solución en función de un subproblema más simple, más cercano al caso base |

### Tipos

- **Directa**: el algoritmo se llama a sí mismo. A → A → A
- **Indirecta**: varios algoritmos se llaman mutuamente formando un ciclo. A → B → C → A

### Cómo diseñar uno

1. Obtener una definición exacta del problema.
2. Determinar el tamaño del problema completo (parámetros de la llamada inicial).
3. Resolver el/los casos base, sin recursión.
4. Resolver el caso general en términos de un caso más pequeño.

### Ejemplos

```
FUNCION FACTORIAL(n : entero) : entero
    SI n <= 1 ENTONCES
        FACTORIAL := 1                       // caso base
    SINO
        FACTORIAL := n * FACTORIAL(n - 1)    // caso recursivo
    FIN_SI
FIN_FUNCION
```

```
FUNCION Fib(n : entero) : entero
    AMBIENTE
        fb : entero
    PROCESO
        SI n <= 2 ENTONCES
            fb := 1
        SINO
            fb := Fib(n-1) + Fib(n-2)
        FIN_SI
        Fib := fb
FIN_FUNCION
```

> El libro escribe el retorno de `Fib` como `RETORNAR fb` y cierra con `FIN`, inconsistente con `FACTORIAL := ...` / `FIN_FUNCION` del ejemplo anterior. **Usar siempre `nombre := valor` y `FIN_FUNCION`**, que es la forma declarada en el Cap. 3.

### Propiedades

1. No debe generar una secuencia infinita de llamadas; **debe existir al menos un caso base**.
2. Debe existir una salida de la secuencia de llamadas recursivas.
3. Cada llamada recursiva debe definirse sobre un problema **de menor complejidad**.

### Recursividad vs. iteración

| Criterio | Recursividad | Iteración |
|---|---|---|
| ¿Cuándo termina? | cuando se ejecuta el caso base | cuando la condición del ciclo es falsa |
| Uso de memoria | **mayor** (pila de llamadas) | menor |
| Legibilidad | mayor en problemas con estructura recursiva natural | mayor en problemas lineales simples |
| Velocidad | menor (overhead de llamadas) | mayor |

> **La recursividad se debe usar cuando sea realmente necesaria**, es decir, cuando no exista una solución iterativa simple. En condiciones críticas de tiempo y memoria, preferir la iterativa.

---

## 12. Complejidad algorítmica (Cap. 9) ✅

### Por qué medir

Para comparar soluciones hay que cuantificarlas. Dos dimensiones: **tiempo de ejecución** (cuántas operaciones) y **uso de memoria** (cuánto espacio).

### Principio de invarianza

Dadas dos implementaciones I₁ e I₂ del **mismo** algoritmo, con tiempos T₁(n) y T₂(n), existe una constante c > 0 tal que para todo n suficientemente grande:

```
T1(n) ≤ c · T2(n)
```

Dos implementaciones del mismo algoritmo difieren **como mucho en una constante multiplicativa**. Por eso se descartan las constantes al analizar complejidad.

### Casos de análisis

| Caso | Descripción |
|---|---|
| **Mejor** | menor número posible de operaciones (entrada más favorable) |
| **Peor** | mayor número posible (entrada más desfavorable) |
| **Medio** | promedio ponderado por la probabilidad de cada entrada |

En la práctica el más útil es el **caso peor**, porque garantiza un límite superior.

### Operaciones elementales (OE)

Se cuentan: operaciones aritméticas (`+ - * /`), asignaciones, llamadas a funciones y retornos, comparaciones y operaciones lógicas, y accesos a arreglos (indexación).

```
a := a + 1                → 2 OE  (asignación + suma)
b := a * 5 - v[2*2]       → 5 OE  (asignación, *, -, [], *)
b := b + suma(a, b+2)     → 4 OE  (asignación, +, llamada, +)
(a <> b) O (c + 1 = x)    → 4 OE  (<>, O, +, =)
```

### Órdenes de complejidad

De más a menos eficiente:

| Orden | Nombre | Ejemplo típico |
|---|---|---|
| O(1) | Constante | acceso directo a un elemento por índice |
| O(log n) | Logarítmica | búsqueda binaria (divide y vencerás) |
| O(n) | Lineal | bucle simple; buscar en lista no ordenada |
| O(n log n) | Cuasi-lineal | Mergesort, Quicksort |
| O(n²) | Cuadrática | doble bucle anidado; burbuja, selección |
| O(n³) | Cúbica | triple bucle; multiplicación de matrices naive |
| O(2ⁿ) | Exponencial | dos llamadas recursivas por nivel; Fibonacci sin memoización |
| O(n!) | Factorial | todas las permutaciones; inviable para n > 15 |

### Fórmulas de sumatorias

Para bucles anidados:

```
Σ(i=1..n) 1   = n
Σ(i=1..n) i   = n(n+1)/2
Σ(i=1..n) i²  = n(n+1)(2n+1)/6
Σ(i=1..n) i³  = (n(n+1)/2)²
```

---

## 13. Notación oficial vs. la que venís usando

Estas diferencias son reales y sistemáticas en tus archivos. La columna izquierda es la del libro.

| Libro (oficial) | Lo que escribís | Comentario |
|---|---|---|
| `Abrir S/(Arch)` | `Abrir /S(arch)` | **La barra va después.** `E/`, `S/`, `E/S` |
| `GRABAR(Arch, Reg)` | `ESCRIBIR(arch, reg)` | `ESCRIBIR` es pantalla y secuencias; archivos usan `GRABAR` |
| `REGRABAR(Arch, Reg)` | `REESCRIBIR(arch, reg)` | — |
| `SI FDA(arch)` / `SI NO FDA(arch)` | `SI EXISTE ENTONCES` | `SI EXISTE` **no existe en el libro** |
| (no hay verbo de baja física) | `ELIMINAR(arch, reg)` | El libro enseña **baja lógica** con campo `activo` |
| `MIENTRAS NO FDA(Arch) HACER` | `MIENTRAS NFDA(arch) HACER` | `NFDA` es contracción de clase; ambas se entienden |
| `MIENTRAS elem <> FDS HACER` | `MIENTRAS NFDS(sec) HACER` | ídem. El libro compara la ventana contra `FDS` |
| `ARR` / `AVZ` / `ESC` | `ARRANCAR` / `AVANZAR` / `ESCRIBIR` | El libro abrevia; las formas largas se entienden |
| `SEGÚN` / `FIN_SEGÚN` | `SEGUN` / `FIN_SEGUN` | Lleva acento |
| sin `FIN_PROCESO` | a veces sí, a veces no | **No lleva** |
| `ALFA(30)` | `AN(40)` | El libro usa `ALFA`; `N(8)` y `R(6,2)` coinciden |
| `PARA i := a HASTA b; incr HACER` | `PARA i := a HASTA b HACER` | La cláusula de incremento existe |

**Criterio para el parcial**: usar la columna izquierda. Las contracciones `NFDA`/`NFDS` y los verbos largos son las únicas que probablemente te acepten sin discusión, porque son de uso corriente en clase — pero `S/`, `GRABAR`, `REGRABAR` y `FDA` en lugar de `SI EXISTE` son correcciones reales.

### Convenciones internas

| Usar | No usar |
|---|---|
| `:=` para asignar | `=` para asignar |
| `<>` para distinto | `!=` |
| Palabras clave en MAYÚSCULA | mezclar en el mismo archivo |
| Nombre de acción sin puntos: `ej_2_2_4` | `2.2.4` |
| Cerrar todo: `FIN_SI`, `FIN_MIENTRAS`, `FIN_PARA`, `FIN_SEGÚN`, `FIN_REGISTRO`, `FIN_FUNCION`, `FIN_PROCEDIMIENTO`, `FIN_ACCION` | — |

Los **tipos** se escriben en minúscula en el libro (`edad : entero`), y los **nombres de tipos registro** en mayúscula (`RegPersona = REGISTRO`). No es una regla dura, pero conviene ser consistente.

---

## 14. Catálogo de errores frecuentes

Sacados de tus propios archivos. Son los que ya cometiste, así que son los que vas a repetir.

### De lógica

| # | Error | Dónde apareció |
|---|---|---|
| 1 | Falta el `AVZ` que **supera el delimitador** | patrón general de cintas |
| 2 | Ciclo interno sin guarda de fin de secuencia | varios |
| 3 | Inicializar el máximo/contador en el nivel equivocado | `Parcial.1.txt` |
| 4 | Condición que no es booleana: `Y v + 'm'` en vez de `Y v = 'M'` | `2.1.18.txt` |
| 5 | Falta el `LEER` al final del ciclo de archivo → ciclo infinito | patrón general |
| 6 | Variable de corte del `REPETIR` nunca leída | `2.3.frre` |
| 7 | Falta la rama de "no existe" (alta) al consultar un indexado | `2.3.frre` |
| 8 | Nombres de campo que no coinciden con la declaración | `2.3.frre` (`cant_punt` vs `cant_puntos`) |
| 9 | `>` donde va `>=` en un umbral de canje | `2.3.frre` |
| 10 | Contador declarado, inicializado y nunca incrementado | `2.3.frre` |
| 11 | Variable usada en un cálculo sin haberla leído nunca | `1.1.5.1.txt` (`c`) |
| 12 | Porcentaje mal convertido: `0.4` para 4% (va `0.04`) | `1.1.5.1.txt` |
| 13 | Resta invertida: `año_nac - año` | `1.9.txt` |
| 14 | Cascada de `SI` que no cubre empates ni tiene `SINO` final | `1.7.txt` |
| 15 | `FECHA` declarada `dia, mes, año` y comparada como registro | `Parcial.1.txt` |
| 16 | Falta `CERRAR` de alguna secuencia o archivo | varios |
| 17 | Dividir sin verificar que el divisor sea > 0 | evitado bien en `2.1.15.txt` |
| 18 | No resolver todos los incisos de la consigna (a, b, c…) | `2.3.frre`, `Parcial.1.txt` |

### De notación (nuevos, tras leer el libro)

| # | Error | Dónde |
|---|---|---|
| 19 | `Abrir /S(...)` en lugar de `Abrir S/(...)` | `2.2.1.txt`, `2.2.4.txt` |
| 20 | `ESCRIBIR(arch, reg)` para grabar en archivo, en vez de `GRABAR` | `2.2.1.txt`, `2.2.4.txt` |
| 21 | `REESCRIBIR` en vez de `REGRABAR` | `2.3.frre`, apunte de indexados |
| 22 | `SI EXISTE` en vez de `SI NO FDA(arch)` | `2.3.frre`, apunte de indexados |
| 23 | `FIN_PROCESO` / `FIN_PROCESSO` | `2.2.1.txt`, `2.2.4.txt`, `1.7.txt` |
| 24 | `NOFDA` en vez de `NFDA` | `2.2.2.txt` |

---

## 15. Pendientes

Los huecos que tenía este documento **quedaron cerrados** por las plantillas oficiales de cátedra
(`isi-aed/Pseudocodigo/`), integradas en el skill `pseudocodigo-utn`:

| Antes ❓ | Ahora |
|---|---|
| Corte de control | ✅ Procedimientos en cascada. Ver `references/plantillas.md` §2 |
| Apareo / fin desparejo | ✅ Dos variantes: inclusiva con `HV`, exclusiva con ciclos de vaciado. §3 y §4 |
| Actualización maestro-movimientos | ✅ Unitaria y por lotes. §5 y §6 |
| ABM sobre indexado | ✅ `SI EXISTE` + `ESCRIBIR`/`RE-ESCRIBIR`/`ELIMINAR`. §7 |
| Arreglos | ✅ `ARREGLO[li..ls] de tipo`, paso por referencia con `var` |
| Paso de parámetros por referencia | ✅ Prefijo `var` en el parámetro formal |

Siguen abiertos:

- ❓ **Árboles** — mencionados como estructura dinámica en la tabla del Cap. 7, sin desarrollo ni plantilla.
- ❓ **Listas, pilas y colas en la notación de cátedra** — el libro las cubre (Cap. 7), pero no hay plantilla de pseudocódigo oficial; solo implementaciones en C.
- ❓ **Ordenación y búsqueda sobre arreglos** — hay implementaciones en C (`ARR_ORD_*`, `ARR_BUSC_*`) pero no pseudocódigo.
