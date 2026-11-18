# Sintaxis y teoría — AyED UTN-FRRe

> [!success] Documento corregido y alineado con la cátedra
> Las secciones de **notación** fueron corregidas contra las **plantillas oficiales**
> (repo `UTN-FRRe/isi-aed`, carpeta `Pseudocodigo/`). La **teoría sigue igual**: no se
> quitó ni se resumió nada.
>
> **Orden de autoridad** — cuando dos fuentes se contradicen, gana la de arriba:
>
> | # | Fuente | Autoridad sobre |
> |---|---|---|
> | 1 | Plantillas oficiales `isi-aed/Pseudocodigo/` | **Notación.** Es lo que se pide reproducir en el parcial |
> | 2 | Libro de cátedra — Pinto & Bolatti 2026 | **Teoría**: conceptos, clasificaciones, definiciones |
> | 3 | Resoluciones de alumnos `AED26_Guia_Ejercicios` | Solo como ejemplo — **contienen bugs** |

> [!tip] Dónde está cada cosa
> | Necesitás | Archivo |
> |---|---|
> | Teoría, conceptos, clasificaciones | **este documento** |
> | Sintaxis exacta al escribir código | [[sintaxis-completa]] |
> | Estructura fija de cada tipo de ejercicio | [[plantillas]] |
> | Checklist al corregir | [[errores-y-trampas]] |
> | Árbol de decisión "qué plantilla uso" | [[SKILL — pseudocodigo-utn|SKILL.md]] |

> [!warning]- Qué se corrigió respecto de la versión anterior *(desplegar)*
> La versión anterior dedujo la notación **del libro**, pero el parcial se corrige con las
> **plantillas**. En estos seis puntos el libro y las plantillas difieren, y **las plantillas
> coinciden con lo que ya venías escribiendo**:
>
> | Decía antes (deducido del libro) | Correcto (plantillas oficiales) |
> |---|---|
> | ~~`GRABAR(arch, reg)`~~ | **`ESCRIBIR(arch, reg)`** |
> | ~~`REGRABAR(arch, reg)`~~ | **`RE-ESCRIBIR(arch, reg)`** |
> | ~~`Abrir S/(Arch)`~~ | **`ABRIR /S(arch)`** |
> | ~~`SI EXISTE` no existe~~ | **`SI EXISTE ENTONCES`** es la forma oficial en indexados |
> | ~~no hay verbo `ELIMINAR`~~ | **`ELIMINAR(arch, reg)`** existe, para baja física |
> | ~~`PARA ... ; incremento`~~ | **`PARA i := 1 HASTA 10, 1 HACER`** — con coma |
>
> Las secciones afectadas fueron reescritas: [§5](#5-registros-y-archivos-cap-5),
> [§6](#6-archivos-indexados-cap-6), [§7](#7-corte-de-control-) y [§13](#13-notación-oficial).

---

Referencia de teoría de la materia.

**Fuente**: *Algoritmos y Estructuras de Datos — Apuntes de Cátedra*, Pinto & Bolatti, 2026 (9 capítulos).

| Marca | Significado |
|---|---|
| ✅ | Respaldado por el libro de cátedra (con capítulo indicado) |
| 📐 | **Notación verificada** contra las plantillas oficiales de cátedra |
| 🔶 | Inferido de los ejercicios; el libro no lo cubre |
| ❓ | Vacío conocido |

Índice: [1 Fundamentos](#1-fundamentos-cap-1) · [2 Control](#2-estructuras-de-control-cap-2) · [3 Subacciones](#3-subacciones-cap-3) · [4 Secuencias](#4-secuencias-cap-4) · [5 Registros y archivos](#5-registros-y-archivos-cap-5) · [6 Indexados](#6-archivos-indexados-cap-6) · [7 Corte de control](#7-corte-de-control-) · [8 Apareo](#8-apareo-maestro-movimientos-) · [9 Arreglos](#9-arreglos-) · [10 Dinámicas (listas)](#10-estructuras-dinámicas-cap-7) · [11 Recursividad](#11-recursividad-cap-8) · [Árboles (pendiente)](#árboles--pendiente) · [12 Complejidad](#12-complejidad-algorítmica-cap-9) · **[13 Notación oficial](#13-notación-oficial-)** · [14 Errores](#14-catálogo-de-errores-frecuentes) · [15 Pendientes](#15-pendientes)

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
    Ambiente
        a, doble : entero
    Proceso
        ESCRIBIR("Ingrese el número")
        LEER(a)
        doble := a * 2
        ESCRIBIR("Resultado: ", doble)
FIN_ACCION
```

> [!note] 📐 Notación verificada
> **No lleva `FIN_PROCESO`.** Del cuerpo se pasa directo a `FIN_ACCION`.
> → `sintaxis-completa.md` §1 · `errores-y-trampas.md` §A.22

- El nombre **no lleva puntos ni espacios**: `ACCION ej_2_2_4 ES`, no `ACCION 2.2.4 ES`.
- `Ambiente` va siempre, aunque quede vacío.
- Comentarios: `//` de línea, `/* ... */` de bloque. La consigna va arriba del `ACCION`, en bloque.

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
| Abrir lectura | `ABRIR E/(arch)` | Abre para leer; el puntero queda en el primer registro |
| Abrir escritura | `ABRIR /S(arch)` | Crea (o sobreescribe) el archivo para grabar registros nuevos |
| Abrir lectura/escritura | `ABRIR E/S(arch)` | Permite leer y modificar en el mismo archivo |
| Leer registro | `LEER(arch, reg)` | Lee el registro actual y avanza el puntero |
| **Escribir registro** | `ESCRIBIR(arch, reg)` | Escribe `reg` en `arch` |
| Cerrar | `CERRAR(arch)` | Cierra el archivo y libera el buffer |
| Fin de archivo | `FDA(arch)` · negado `NFDA(arch)` | Función: V cuando no hay más registros |

> [!note] 📐 Notación verificada
> **`ESCRIBIR` sirve para las tres cosas** — pantalla, secuencia y archivo. Lo que las distingue
> es el primer argumento: `ESCRIBIR("texto")` es pantalla, `ESCRIBIR(sec, v)` es secuencia,
> `ESCRIBIR(arch, reg)` es archivo.
>
> El **libro** usa `GRABAR(arch, reg)` para archivos, pero **las plantillas oficiales usan
> `ESCRIBIR`** y son las que se corrigen en el parcial.
> → `sintaxis-completa.md` §4
>
> Variantes equivalentes que vas a ver en plantillas viejas de cátedra: `ABRIRe(arch)`,
> `ABRIRs(arch)`, `ABRIRe/s(arch)`, `NoFDA(arch)`.

> ⚠️ Olvidar `CERRAR` puede provocar **pérdida de datos**: los últimos registros escritos quedan en el buffer y no se vuelcan al disco.

### Esquema de recorrido secuencial

```
ABRIR E/(arch)
LEER(arch, reg)                   // lectura anticipada, pegada al ABRIR
MIENTRAS NFDA(arch) HACER
    // tratar reg
    LEER(arch, reg)               // ← última instrucción del ciclo, obligatorio
FIN_MIENTRAS
CERRAR(arch)
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

1. El programa establece la clave buscada: `reg.clave := valor` — **antes** del `LEER`
2. El sistema busca esa clave en el área de índices (**búsqueda binaria, O(log n)**)
3. El índice devuelve la posición física
4. El sistema lee directamente el registro en esa posición

Con 100.000 registros: la búsqueda secuencial puede requerir hasta 100.000 lecturas; la binaria en el índice, como máximo log₂(100.000) ≈ **17 pasos**.

### Verbos comparados

| Operación | Secuencia | Archivo secuencial | Archivo indexado |
|---|---|---|---|
| Abrir lectura | `ARR(sec)` | `ABRIR E/(arch)` | `ABRIR E/S(arch)` |
| Abrir escritura | `CREAR(sec)` | `ABRIR /S(arch)` | — |
| Leer | `AVZ(sec, v)` | `LEER(arch, reg)` | `reg.clave := x` ; `LEER(arch, reg)` |
| Escribir | `ESCRIBIR(sec, v)` | `ESCRIBIR(arch, reg)` | `ESCRIBIR(arch, reg)` (alta) |
| Modificar | — | — | `RE-ESCRIBIR(arch, reg)` |
| Eliminar | — | — | `ELIMINAR(arch, reg)` |
| ¿Hay más? | `NFDS(sec)` | `NFDA(arch)` | `SI EXISTE ENTONCES` |
| Cerrar | `CERRAR(sec)` | `CERRAR(arch)` | `CERRAR(arch)` |

**La diferencia clave en la lectura indexada**: hay que asignar la clave **ANTES** del `LEER`. Eso le indica al sistema qué registro buscar en el índice.

> [!note] 📐 Notación verificada
> El indexado se abre normalmente con **`ABRIR E/S(arch)`**, porque se lee y se modifica en la
> misma pasada. Y **nunca se recorre con `NFDA`**: el acceso es puntual por clave.
> → `sintaxis-completa.md` §5

### Cómo se pregunta si el registro existe

```
ABRIR E/S(archEmpleados)

regEmp.clave := 1005              // ← la clave se asigna ANTES del LEER
LEER(archEmpleados, regEmp)

SI EXISTE ENTONCES
    ESCRIBIR(regEmp.nombre, regEmp.salario)
SINO
    ESCRIBIR("Empleado no encontrado")
FIN_SI

CERRAR(archEmpleados)
```

> [!note] 📐 Notación verificada
> La existencia se pregunta con **`SI EXISTE ENTONCES`**, que consulta el resultado del último
> `LEER`. Es la forma de las plantillas oficiales, y es la que ya usabas en `2.3.frre`.
>
> El orden es siempre el mismo y no se puede alterar:
> **`clave` → `LEER` → `SI EXISTE`**.
> → `sintaxis-completa.md` §5

### ESCRIBIR vs. RE-ESCRIBIR

Distinción fundamental y fuente frecuente de errores.

| | **ESCRIBIR** — alta | **RE-ESCRIBIR** — modificación |
|---|---|---|
| Para qué | insertar un registro que **NO existía** | actualizar uno que **YA fue leído** |
| Qué hace el sistema | busca espacio en el área de datos, escribe, y **agrega la entrada al índice** en la posición correcta | **sobreescribe la misma posición física** del registro leído |
| Requisito | la clave **NO** debe existir (alta pura) | **el registro debe haber sido leído con `LEER` justo antes** |
| Índice | se modifica | no se modifica (la clave no cambia) |
| Si se viola | error de clave duplicada | error de lógica |

> [!note] 📐 Notación verificada
> Es **`RE-ESCRIBIR`**, con guion. Tu `REESCRIBIR` sin guion estaba casi bien —
> el libro lo llama `REGRABAR`, pero las plantillas oficiales usan `RE-ESCRIBIR`.
> → `sintaxis-completa.md` §5 · `errores-y-trampas.md` §A.23

> [!important] El ciclo obligatorio de una modificación es siempre:
> 1. `ABRIR E/S(arch)`
> 2. `reg.clave := valor_buscado`
> 3. `LEER(arch, reg)` ← **lectura obligatoria**
> 4. `SI EXISTE ENTONCES` — modificar campos del `reg`
> 5. `RE-ESCRIBIR(arch, reg)`
>
> Saltarse el paso 3 produce un error de lógica: se re-escribe un registro que nunca se leyó.

### Comparación secuencial vs. indexado

| Criterio | Secuencial | Indexado |
|---|---|---|
| Espacio en disco | solo los registros | registros + área de índices |
| Orden de los datos | no necesariamente ordenado | el índice siempre ordenado por clave |
| Recorrido total | muy eficiente, lectura continua | algo más lento por la doble área |
| Búsqueda puntual | muy lento, O(n) peor caso | muy rápido, O(log n) |
| Modificación | no admite re-escribir | admite `RE-ESCRIBIR` tras lectura |
| Uso ideal | reportes, batch, grandes volúmenes | consultas interactivas, ABM en tiempo real |

### Actualización indexada — ABM

Proceso por el cual un usuario interactivo mantiene el maestro actualizado en tiempo real: **A**lta, **B**aja, **M**odificación.

**Alta** — verificar que la clave NO exista, y recién ahí `ESCRIBIR`:

```
PROCEDIMIENTO Alta(var arch : ARCHIVO de emp) ES
    Ambiente
        nuevoCodigo : entero
        reg : emp
    Proceso
        LEER(nuevoCodigo)
        reg.codigo := nuevoCodigo
        LEER(arch, reg)                      // verificar si ya existe
        SI EXISTE ENTONCES
            ESCRIBIR("Error: clave ya existe. No se puede dar de alta.")
        SINO
            LEER(reg.nombre, reg.salario)    // ingresar datos
            reg.codigo := nuevoCodigo
            ESCRIBIR(arch, reg)              // ← alta
            ESCRIBIR("Alta realizada correctamente.")
        FIN_SI
FIN_PROCEDIMIENTO
```

**Modificación** — leer, cambiar, `RE-ESCRIBIR`:

```
PROCEDIMIENTO Modificacion(var arch : ARCHIVO de emp) ES
    Ambiente
        codigoBuscado : entero
        reg : emp
    Proceso
        LEER(codigoBuscado)
        reg.codigo := codigoBuscado
        LEER(arch, reg)
        SI EXISTE ENTONCES
            ESCRIBIR("Registro actual: ", reg.nombre, reg.salario)
            LEER(reg.salario)
            RE-ESCRIBIR(arch, reg)           // ← modificación
            ESCRIBIR("Modificación realizada.")
        SINO
            ESCRIBIR("Error: registro no encontrado.")
        FIN_SI
FIN_PROCEDIMIENTO
```

**Baja** — dos estrategias:

- **Baja física**: `ELIMINAR(arch, reg)` borra el registro y actualiza el índice. Costosa: deja "huecos" en el área de datos.
- **Baja lógica (preferida cuando el registro tiene campo marca)**: se agrega un campo indicador (`activo : logico` o `Baja : caracter`); al dar de baja se pone la marca y se `RE-ESCRIBIR`. El registro queda en el archivo pero los procesos lo ignoran.

```
PROCEDIMIENTO Baja(var arch : ARCHIVO de emp) ES
    Ambiente
        codigoBuscado : entero
        reg : emp
    Proceso
        LEER(codigoBuscado)
        reg.codigo := codigoBuscado
        LEER(arch, reg)
        SI EXISTE ENTONCES
            SI reg.activo = falso ENTONCES
                ESCRIBIR("Advertencia: el registro ya estaba dado de baja.")
            SINO
                reg.activo := falso              // baja LÓGICA
                RE-ESCRIBIR(arch, reg)
                // baja FÍSICA sería:  ELIMINAR(arch, reg)
                ESCRIBIR("Baja realizada para: ", reg.nombre)
            FIN_SI
        SINO
            ESCRIBIR("Error: registro no encontrado.")
        FIN_SI
FIN_PROCEDIMIENTO
```

> [!note] 📐 Notación verificada
> **`ELIMINAR(arch, reg)` sí existe** en las plantillas oficiales, para baja física.
> La versión anterior de este documento decía que no tenía respaldo — era incorrecto.
>
> Cuál usar: si el registro **tiene campo marca**, baja lógica con `RE-ESCRIBIR`.
> Si no lo tiene, baja física con `ELIMINAR`.
> → `sintaxis-completa.md` §5 · `plantillas.md` §7

### Características de la actualización indexada

| Característica | Por qué |
|---|---|
| **Rápida** | el acceso directo evita recorrer el archivo; cada operación es O(log n) |
| **In situ** | los cambios se aplican directo sobre el maestro, sin copia intermedia |
| **Interactiva** | el usuario ingresa datos y recibe respuesta inmediata; no es batch |
| **Insegura** | al no haber archivo intermedio, un error del usuario afecta el maestro directamente. Se recomienda auditoría (log de operaciones) |

---

## 7. Corte de control 📐

> [!success] Hueco cerrado
> El **libro** no cubre corte de control — no hay capítulo. Pero **las plantillas oficiales sí**,
> con la variante de procedimientos en cascada (`tratar_corte`, `tratar_registro`), que es la
> que se exige. La versión anterior de este documento marcaba esto como "el hueco más grande";
> ya no lo es.
>
> **Plantilla completa: [[plantillas]] §2**
>
> El orden dentro de cada `corte_N` es fijo y no se puede alterar:
> 1. llamar al corte **inferior**
> 2. emitir
> 3. acumular al **superior**
> 4. poner en cero **lo propio**
> 5. **re-resguardar** la clave
>
> Y dos reglas que se caen siempre en el parcial:
> - `tratar_corte` pregunta **de mayor a menor** jerarquía.
> - Después del `MIENTRAS` se llama al corte de **mayor** jerarquía — la cascada baja sola.
>   Llamar al menor es el bug B.1 de `errores-y-trampas.md`, y está en material que circula
>   como resuelto.

Precondición: **el archivo tiene que estar ordenado por la clave de corte.**

### Un nivel — ciclos anidados

```
ABRIR E/(arch); LEER(arch, r)
tot_general := 0

MIENTRAS NFDA(arch) HACER
    resg := r.clave                  // RESGUARDO
    tot_nivel := 0                   // inicializar acumuladores del nivel

    MIENTRAS NFDA(arch) Y r.clave = resg HACER
        tot_nivel := tot_nivel + r.importe        // TRATAR REGISTRO
        LEER(arch, r)
    FIN_MIENTRAS

    ESCRIBIR("Total de ", resg, ": ", tot_nivel)  // TRATAR CORTE
    tot_general := tot_general + tot_nivel        // acumular al nivel superior
FIN_MIENTRAS

ESCRIBIR("Total general: ", tot_general)
CERRAR(arch)
```

### Dos niveles — el patrón se anida

```
MIENTRAS NFDA(arch) HACER
    resg_suc := r.sucursal
    tot_suc := 0

    MIENTRAS NFDA(arch) Y r.sucursal = resg_suc HACER
        resg_rub := r.rubro
        tot_rub := 0

        MIENTRAS NFDA(arch) Y r.sucursal = resg_suc Y r.rubro = resg_rub HACER
            tot_rub := tot_rub + r.importe
            LEER(arch, r)
        FIN_MIENTRAS

        ESCRIBIR("Rubro ", resg_rub, ": ", tot_rub)
        tot_suc := tot_suc + tot_rub
    FIN_MIENTRAS

    ESCRIBIR("Sucursal ", resg_suc, ": ", tot_suc)
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

## 8. Apareo maestro-movimientos 📐

> [!success] Hueco cerrado
> El **libro** define los *tipos* de archivo maestro/movimiento (Cap. 5) pero no el algoritmo.
> **Las plantillas oficiales cubren las cuatro variantes**, y la elección entre ellas es lo que
> más se equivoca:
>
> | Situación | Plantilla | Ref. |
> |---|---|---|
> | Combinar/listar, **los dos archivos deben agotarse** | Mezcla **inclusiva** con `HV` | `plantillas.md` §3 |
> | Combinar/listar, solo mientras haya en ambos | Mezcla **exclusiva** + 2 ciclos de vaciado | `plantillas.md` §4 |
> | Maestro + movimientos, **1 movimiento por clave** | Actualización **unitaria** | `plantillas.md` §5 |
> | Maestro + movimientos, **varios por clave** | Actualización **por lotes** (registro `aux`) | `plantillas.md` §6 |
>
> Con `HV` el ciclo es `MIENTRAS (c1 <> HV) O (c2 <> HV)`; sin `HV` es
> `MIENTRAS NFDA(a1) Y NFDA(a2)` **más los dos vaciados**. Los `LEER` van encapsulados en
> procedimientos que asignan `HV` al detectar `FDA`.

Dos archivos ordenados por la misma clave, recorridos en paralelo comparando claves:

```
ABRIR E/(mae); LEER(mae, m)
ABRIR E/(mov); LEER(mov, v)
ABRIR /S(sal)

MIENTRAS NFDA(mae) O NFDA(mov) HACER
    SI m.clave < v.clave ENTONCES          // solo en maestro → pasa igual
        sal := m; ESCRIBIR(arch_sal, sal)
        LEER(mae, m)
    SINO
        SI m.clave = v.clave ENTONCES      // en los dos → aplicar el movimiento
            SEGUN v.cod_mov HACER
                = 1 : ESCRIBIR("Error: alta de algo que ya existe")
                = 2 : // baja
                = 3 : // modificación
            FIN_SEGUN
            LEER(mov, v)
        SINO                                // solo en movimientos → alta
            SI v.cod_mov = 1 ENTONCES
                // armar el registro nuevo y grabarlo
            SINO
                ESCRIBIR("Error: baja/modificación de algo inexistente")
            FIN_SI
            LEER(mov, v)
        FIN_SI
    FIN_SI
FIN_MIENTRAS
```

> [!success] Resuelto
> El **fin desparejo** tiene dos tratamientos oficiales, y elegir mal es el error más común:
> - **Inclusiva** — clave alta ficticia `HV`: `MIENTRAS (c1 <> HV) O (c2 <> HV)`. Los dos archivos se agotan.
> - **Exclusiva** — sin `HV`: `MIENTRAS NFDA(a1) Y NFDA(a2)` **más dos ciclos de vaciado** al salir.
>
> → `plantillas.md` §3 (inclusiva) y §4 (exclusiva)

---

## 9. Arreglos 📐

> [!success] Hueco cerrado
> El **libro** solo los menciona al pasar en el Cap. 7 ("los arreglos tienen un número máximo
> de elementos declarado en el ambiente"). **La notación oficial está en las plantillas**:
> `ARREGLO[li..ls] de tipo`, y el paso por referencia se marca con el prefijo **`var`** en el
> parámetro formal.
> → `sintaxis-completa.md` §9 · §8 (paso de parámetros)

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

> [!info] Fuentes de esta sección
> - **Teoría**: libro de cátedra, Cap. 7.
> - **Notación y algoritmos**: la teoría de listas de la guía ([aed-frre.github.io/teoria/listas](https://aed-frre.github.io/teoria/listas/), transcripta en `Guía de Cátedra/Teoría/Listas.md`) y los Complementos Teóricos de la Guía 2026 (p. 63-64: `LISTA_CIRCULAR` y `LISTA_DOBLE`).
> - **Clase**: tus notas en `Práctica/Clase 5 Listas.frre`.
>
> Todo lo de esta sección corre en la extensión desde la 0.12.0.

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

**Verbos**: `NUEVO(q)` reserva memoria para un nodo; `DISPONER(p)` la libera (el libro lo llama `BORRAR(p)`).

#### Las formas que aparecen en el material

Todas son válidas y quieren decir lo mismo. La primera columna es la que usamos.

| Concepto | Forma que usamos | También aparece | Dónde |
|---|---|---|---|
| Tipo puntero | `p : Puntero a NODO` | `punt = Puntero a NODO` y después `p : punt` | teoría de la guía, tus notas |
| Puntero que no apunta a nada | `NIL` | `nil`, `NULO` | `NIL` en la guía, `NULO` en el libro |
| Pedir un nodo | `NUEVO(p)` | — | todos |
| Liberar un nodo | `DISPONER(p)` | `BORRAR(p)` | `DISPONER` en la guía, `BORRAR` en el libro |
| Campo del nodo apuntado | `*p.dato` | `p^.dato` (tus notas), `P↑.DATO` (guía, ej. 4.1), `*P.PROX` / `P*.PROX` (Complementos 2026) | — |
| Anidado | `*(*p.ant).prox` | — | Complementos 2026 |

> `p.dato` **sin** asterisco está mal: `p` es un puntero, no un registro. Primero hay que ir al
> nodo (`*p`) y recién ahí pedir el campo.

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

### Las cargas de la guía

La teoría de la guía les pone nombre a las formas de armar una lista. Son las mismas operaciones
de arriba, leyendo hasta una marca de fin (`'*'`):

| Nombre en la guía | Qué hace | Equivale a |
|---|---|---|
| **Carga apilada** | cada nodo nuevo queda **primero** (`*p.Prox := Prim; Prim := p`) | insertar al inicio; la lista queda al revés de como se leyó |
| **Carga encolada** | cada nodo nuevo queda **último**, con un puntero `a` al anterior | insertar al final; la lista queda en el orden de lectura |
| **Carga ordenada** | busca la posición con `q` (actual) y `a` (anterior) | insertar en orden |
| **Eliminación** | busca con `q` y `a`, engancha `*a.prox := *q.prox` y `DISPONER(q)` | eliminar por valor |

Las plantillas completas están en [[plantillas]] §9.

### Lista que llega por parámetro

La guía da la lista ya cargada: *"el algoritmo recibe como parámetro de entrada la dirección del
primer elemento"* (ej. 4.2). Se escribe en la cabecera de la ACCION:

```
ACCION Ej_4_2 (PRIM: Puntero a NODO) ES
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

### Lista circular

El último nodo **no** apunta a `NIL`: apunta al **primero**. No hay "fin de lista", así que el
recorrido termina cuando se vuelve al principio. Con un solo nodo, ese nodo se apunta a sí mismo.

Búsqueda, de `LISTA_CIRCULAR` (Complementos Teóricos de la Guía 2026, p. 63):

```
SI PRIMERO = NIL ENTONCES
    ESCRIBIR('ERROR, Lista Vacía')
SINO
    T := PRIMERO
    MIENTRAS (*T.SIG <> PRIMERO) Y (*T.VALOR <> DATO) HACER
        T := *T.SIG
    FIN_MIENTRAS
    SI *T.VALOR <> DATO ENTONCES
        ESCRIBIR('ERROR, ', DATO, ' no está en la Lista')
    SINO
        ESCRIBIR('HALLADO VALOR: ', *T.VALOR)
    FIN_SI
FIN_SI
```

- La condición de corte es `*T.SIG <> PRIMERO`, **no** `T <> NIL`. Con `NIL` el ciclo no termina nunca.
- Por eso el último nodo se compara **después** del ciclo: el `MIENTRAS` se detiene parado sobre él.
- En una **circular doble** además el `ant` del primero apunta al último.

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

### Cómo se escribe en clase: el planteo formal

En clase cada ejercicio arranca con el **planteo formal** (los casos escritos como una función
matemática) y recién después se pasa a pseudocódigo. Ejemplo de clase, `EsPar` usando solo la resta:

```
Planteo formal: EsPar(Num)
  Casos base:      = verdadero,  si Num = 0
                   = falso,      si Num = 1
  Caso recursivo:  EsPar(Num - 2), si Num > 1
```

```
FUNCION EsPar(Num: N(3)): logico ES
    Proceso
        SI Num = 0 ENTONCES
            EsPar := verdadero                  // caso base
        SINO
            SI Num = 1 ENTONCES
                EsPar := falso                  // caso base
            SINO
                EsPar := EsPar(Num - 2)         // caso recursivo
            FIN_SI
        FIN_SI
FIN_FUNCION
```

### Recursión sobre un arreglo: las dos direcciones

El índice es el parámetro que "se acerca al caso base". Puede bajar o subir:

| | Baja (de N a 1) | Sube (de 1 a N) |
|---|---|---|
| Llamada inicial | `Suma(V, 10)` | `Promedio_10_Elementos(V, 1)` |
| Caso base | `i = 1` → `A[1]` | `i = 10` → `A[10] / 10` |
| Caso recursivo | `A[i] + Suma(A, i - 1)` | `A[i] / 10 + Promedio_10_Elementos(A, i + 1)` |
| De dónde sale | guía 5.1.8, resuelto en clase | ejercicio extra de clase |

Los dos son correctos. Lo que no puede faltar es que **cada llamada se acerque al caso base**.

### Prueba de escritorio de una recursión

Se hace en dos tiempos:

1. **Bajada**: cada llamada pide la siguiente y queda **esperando**. Se anotan una debajo de la otra, con sangría, hasta llegar al caso base.
2. **Subida**: el caso base devuelve un valor sin llamar a nadie, y cada llamada pendiente **termina su cuenta** con lo que le devolvió la de abajo, de la última a la primera.

```
CantImpares(3527)  -> último 7, impar -> 1 + CantImpares(352)
  CantImpares(352) -> último 2, par   -> CantImpares(35)
    CantImpares(35)  -> último 5, impar -> 1 + CantImpares(3)
      CantImpares(3)   -> caso base: 3 es impar -> 1
    = 1 + 1 = 2
  = 2
= 1 + 2 = 3
```

Para ver una recursión corriendo paso a paso: `Práctica/Recursividad — prueba de escritorio.frre`.

### Ejercicios resueltos

| Ejercicio | Archivo | Idea |
|---|---|---|
| `EsPar` (clase) | `Práctica/Recursividad.frre` | resta 2 hasta llegar a 0 o 1 |
| Suma de un vector, guía 5.1.8 (clase) | ídem | `A[i] + Suma(A, i - 1)` |
| Promedio de 10 elementos (clase) | ídem | cada elemento aporta `A[i] / 10` |
| Promedio de aprobados (clase) | ídem | igual, sumando solo los que aprobaron |
| Promedio, de n hacia abajo | ídem + prueba de escritorio | `(Promedio(A, n-1) * (n-1) + A[n]) / n` |
| Cantidad de dígitos impares de N | `Práctica/Recursividad — dígitos impares.frre` | último dígito `N MOD 10`, resto `N DIV 10` |

El **Práctico 5 de la guía** pide funciones recursivas para factorial, Fibonacci, potencia con
multiplicaciones, dígitos todos pares, división entera con restas, par/impar con restas, MCD de
Euclides y suma de un vector (1.01 a 1.08), y procedimientos recursivos para imprimir un número
al revés, el palíndromo de una palabra, una lista en orden descendente y un decimal en binario
(2.01 a 2.04). Ver `Guía de Cátedra/Práctica/5 — Recursividad.md`.

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

### Trampas de recursividad

| Trampa | Qué pasa |
|---|---|
| Falta el caso base, o la llamada no se acerca a él | las llamadas no terminan nunca. La extensión corta a las 10000 llamadas con un error |
| `N` y `n` como si fueran distintas | el pseudocódigo **no distingue mayúsculas**: un parámetro `n` tapa a la constante `N` dentro de la función |
| Condición distinta en el caso base y en el recursivo | en el promedio de aprobados de clase quedó `> 6` en uno y `>= 6` en el otro: un 6 cuenta en todas las posiciones menos en la última |
| Llamar a la función como instrucción suelta | `Suma(A, i - 1)` solo no hace nada: el resultado se usa en una expresión o se asigna |

---

## Árboles — pendiente

> [!todo] Próximo tema
> Todavía no se vio en clase. Lo que hay hasta ahora:

- **Libro de cátedra**: solo los nombra como estructura dinámica, en la tabla del Cap. 7. No hay desarrollo.
- **Guía 2026, Práctico 5 §5.3** (`Guía de Cátedra/Práctica/5 — Recursividad.md`): es la única fuente con contenido. Pide:
  - **Terminología** sobre un árbol dado: hojas, raíz, padre, hijos, antecesores, descendientes, hermanos, profundidad, altura de un nodo, caminos de longitud 3.
  - **Árboles de expresión**: dibujar el de `[(x-y)*z] / (m+n**p)`, pasar expresiones a prefija y postfija, y evaluar uno (letras en las hojas, operadores en los nodos interiores).
  - **Recorridos**: pre-orden, en-orden y post-orden, con prueba de escritorio, y reconstruir un árbol a partir de su pre-orden y en-orden.
  - **Funciones recursivas sobre árboles binarios**: cantidad de nodos, altura, suma de los elementos, suma de los múltiplos de 3, buscar una clave y operar con ella.
  - **AVL**: decidir cuál de dos árboles lo es.
- **Declaración que da la guía** (ej. 10):

```
arbol = registro
    X: entero;
    Izq, Dcha: puntero a arbol;
Freg;
```

- **Extensión**: un árbol binario ya corre, porque es un registro con dos punteros más recursividad. Se probó insertar en un árbol de búsqueda, recorrerlo en orden y calcular la altura. Falta confirmarlo con los ejercicios de la guía cuando se dé el tema.
- **Falta**: la teoría de clase, la notación que use la cátedra para los recorridos y las plantillas.

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

## 13. Notación oficial 📐

> [!success] Sección reescrita
> La versión anterior comparaba tu código contra **el libro** y marcaba como errores cosas que
> estaban bien. Esta versión compara contra las **plantillas oficiales**
> (`isi-aed/Pseudocodigo/`), que son las que se corrigen en el parcial.

### 13.1 — Tabla de referencia rápida

Esta es la notación que hay que usar. Fuente: `sintaxis-completa.md`.

| Concepto | Forma oficial |
|---|---|
| Esqueleto | `ACCION nombre ES` · `Ambiente` · `Proceso` · `FIN_ACCION` |
| Fin de proceso | **no lleva `FIN_PROCESO`** — del cuerpo se pasa directo a `FIN_ACCION` |
| Nombre de acción | sin puntos ni espacios: `ej_2_2_4`, nunca `2.2.4` |
| Asignación | `:=` |
| Comparación | `=` igual · `<>` distinto |
| Lógicos | `Y` `O` `NO` · pertenencia `EN` |
| Aritméticos | `+` `-` `*` `/` `MOD` `DIV` `**` (potencia) |
| Ciclo con paso | `PARA i := 1 HASTA 10, 1 HACER` — **el incremento va con coma**, puede ser negativo |
| Retorno de función | se asigna **al nombre de la función** |
| Paso por referencia | prefijo **`var`** en el parámetro formal |
| Cerrar estructuras | `FIN_SI` `FIN_MIENTRAS` `FIN_PARA` `FIN_SEGUN` `FIN_REGISTRO` `FIN_FUNCION` `FIN_PROCEDIMIENTO` `FIN_ACCION` |

**Verbos por estructura** — la tabla que más se consulta:

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

---

### 13.2 — Dónde el libro y las plantillas se contradicen

En estos seis puntos las dos fuentes dicen cosas distintas. **Gana la plantilla.**

| Concepto | Libro (Pinto & Bolatti) | ✅ Plantillas oficiales — usar esta |
|---|---|---|
| Grabar en archivo | `GRABAR(arch, reg)` | **`ESCRIBIR(arch, reg)`** |
| Modificar en indexado | `REGRABAR(arch, reg)` | **`RE-ESCRIBIR(arch, reg)`** |
| Abrir escritura | `Abrir S/(Arch)` | **`ABRIR /S(arch)`** |
| ¿Existe el registro? | `SI NO FDA(arch)` | **`SI EXISTE ENTONCES`** |
| Baja física | *(no define verbo)* | **`ELIMINAR(arch, reg)`** |
| Incremento del `PARA` | `PARA i := a HASTA b; incr` | **`PARA i := a HASTA b, incr HACER`** |

---

### 13.3 — Variantes que **sí** son válidas

No son errores. Aparecen en plantillas de cátedra de distintas épocas y se entienden.

**Las dos son válidas y se pueden mezclar.** No es una preferencia nuestra: los propios
materiales de la cátedra las mezclan. El libro y las filminas usan una, las resoluciones de
la guía usan la otra de punta a punta (83 de 83 archivos en notación vieja, cero `FIN_SI`), y
los parciales que el profesor resuelve en clase combinan `finaccion` con estructuras modernas.
La extensión acepta cualquier combinación y no avisa nada.

Dicho eso, la **preferencia de Gonzalo** es la forma moderna en mayúsculas: `FIN_SI`,
`FIN_MIENTRAS`, `FIN_ACCION`. Es la que se usa al escribir código nuevo en este workspace.

| Forma moderna (preferir) | Forma vieja (válida) |
|---|---|
| `Proceso` | `Algoritmo` |
| `SINO` | `Contrario` |
| `FIN_SI` `FIN_MIENTRAS` | `FinSi` `FinMientras` |
| `FIN_ACCION` | `FinAccion.` |
| `FIN_PROCEDIMIENTO` | `Fin_Proc;` / `Fin;` |
| sin `;` al final de línea | con `;` |
| `ABRIR E/(arch)` | `ABRIRe(arch)` |
| `ABRIR /S(arch)` | `ABRIRs(arch)` |
| `ABRIR E/S(arch)` | `ABRIRe/s(arch)` |
| `NFDA(arch)` · `NFDS(sec)` | `NoFDA(arch)` · `NoFDS(sec)` |
| `ESCRIBIR(...)` por pantalla | `ESC(...)` |

---

### 13.4 — Convenciones internas

| Usar | No usar |
|---|---|
| `:=` para asignar | `=` para asignar |
| `<>` para distinto | `!=` |
| Palabras clave en MAYÚSCULA | mezclar en el mismo archivo |
| `FIN_SEGUN` — sin acento en el código | `FIN_SEGÚN` |
| Nombre de acción sin puntos: `ej_2_2_4` | `2.2.4` |
| Un solo registro notacional por archivo | mezclar `Proceso`/`Algoritmo`, `SINO`/`Contrario` |
| Cerrar toda estructura abierta | — |

Los **tipos** van en minúscula (`edad : entero`) y los **nombres de tipos registro** en mayúscula
(`RegPersona = REGISTRO`). No es regla dura, pero conviene ser consistente.

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

### De notación 📐

> [!warning] Corregido
> La lista anterior (errores 19 a 24) marcaba como errores cosas que **estaban bien**:
> `ABRIR /S`, `ESCRIBIR(arch, reg)`, `REESCRIBIR` y `SI EXISTE`. Salían de comparar contra el
> libro en vez de contra las plantillas. Esta es la lista real.
> → `errores-y-trampas.md` §A "Notación"

| # | Error | Correcto |
|---|---|---|
| 19 | `NOFDA` | `NFDA` o `NoFDA` |
| 20 | `PROCESSO` / `FIN_PROCESSO` | `Proceso`, y **no lleva** `FIN_PROCESO` |
| 21 | `REESCRIBIR` sin guion | `RE-ESCRIBIR` |
| 22 | `SI ... ENTONCES:` con dos puntos | sin dos puntos |
| 23 | `SEC DE CARACTER` | `SECUENCIA de caracter` |
| 24 | Nombre de acción con puntos: `ACCION 2.2.4 ES` | `ACCION ej_2_2_4 ES` |
| 25 | `PARA i := 1 HASTA 10 HACER` cuando el paso no es 1 | `PARA i := 20 HASTA -20, -2 HACER` |
| 26 | `p.dato` con `p` puntero | `*p.dato` (el nodo apuntado), ver §10 |

> Mezclar la notación vieja y la moderna en un mismo archivo **no** es error (ver §13.3): los
> propios materiales de la cátedra lo hacen.

### De listas y recursividad

| # | Error | Dónde apareció |
|---|---|---|
| 27 | En el recorrido, avanzar con `p := *p.dato` en vez de `p := *p.prox` | tus notas, `Clase 5 Listas.frre` |
| 28 | Recorrido que nunca avanza (`p := *p.prox` olvidado) → ciclo infinito | patrón general |
| 29 | Usar `*p` cuando `p = NIL`, o un nodo después de `DISPONER` | patrón general |
| 30 | Recorrer una circular con `MIENTRAS p <> NIL` → no termina nunca | §10, lista circular |
| 31 | Cola: al desencolar el último no se pone `ULT := NIL` | §10, colas |
| 32 | Recursión sin caso base, o que no se acerca a él | §11 |
| 33 | Caso base y caso recursivo con condiciones distintas (`>` y `>=`) | promedio de aprobados de clase |
| 34 | Parámetro `n` que tapa a la constante `N` | §11, trampas |

Detalle en [[errores-y-trampas]] §A "Listas" y "Recursividad".

---

### 🪤 Bugs en el material que circula como resuelto

No son errores tuyos: están en archivos de `AED26_Guia_Ejercicios` que se copian a ciegas.
Detalle completo en [[errores-y-trampas]] §B.

| # | Bug | Dónde | Consecuencia |
|---|---|---|---|
| B.1 | Después del `MIENTRAS` se llama al corte **menor** (`corte_carr`) en vez del mayor | `Ejercicio_2.2.11.frre.txt` | Nunca se emiten los totales del último grupo |
| B.2 | Filtro negado: `SI (alu.fecha_ing.anio <> 2009)` | mismo archivo | Cuenta justo los que **no** pedía la consigna |
| B.3 | Barridos invertidos: blancos con `<>` y palabra con `O` | `Parcial 2025 Tema A` *(marcado como corregido por profesores)* | Barre lo que no es, o ciclo infinito |

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
| Notación oficial contradictoria | ✅ Resuelto en [§13.2](#132--dónde-el-libro-y-las-plantillas-se-contradicen) — gana la plantilla |
| Arreglos | ✅ `ARREGLO[li..ls] de tipo`, paso por referencia con `var` |
| Paso de parámetros por referencia | ✅ Prefijo `var` en el parámetro formal |

Siguen abiertos:

- ❓ **Árboles**: es el próximo tema. Ver [Árboles — pendiente](#árboles--pendiente) para lo que pide la guía y lo que falta.

Cerrados desde la versión anterior:

- ✅ **Listas, pilas y colas en la notación de cátedra**: la teoría de listas de la guía y los Complementos Teóricos 2026 dan los algoritmos en pseudocódigo. Ver §10 y [[plantillas]] §9.
- ✅ **Recursividad**: planteo formal de clase, ejercicios resueltos y prueba de escritorio. Ver §11 y [[plantillas]] §10.
- ✅ **Ordenación y búsqueda sobre arreglos**: están en pseudocódigo en `Teoría/Arreglos y Actualización — apunte completo.md` (lineal, con centinela, binaria, selección, inserción e intercambio).
