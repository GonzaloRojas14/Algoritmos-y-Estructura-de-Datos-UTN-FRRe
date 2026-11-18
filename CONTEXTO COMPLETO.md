# Contexto completo — Algoritmos y Estructuras de Datos (UTN-FRRe)

> Documento de contexto de todo el trabajo hecho sobre la materia: el material de
> cátedra recopilado, la teoría destilada, los ejercicios resueltos, y la extensión
> de VS Code que ejecuta el pseudocódigo.
>
> **Última actualización: 04/11/2026.** Extensión en la versión 0.12.1, publicada
> (listas con punteros, notación de la guía de TP, Anexo y parámetros). La 0.12.2
> (recursividad) está lista en el código pero **sin publicar**. Temas vistos hasta
> ahora: hasta **listas y recursividad**; **árboles** es el próximo.

---

## 0. De un vistazo

| | |
|---|---|
| **Materia** | Algoritmos y Estructuras de Datos — ISI, UTN-FRRe |
| **Alumno** | Rojas Gonzalo ([@gonza._007](https://instagram.com/gonza._007)) |
| **Carpeta raíz** | `~/Desktop/Estudios/Algoritmos/` |
| **Extensión** | `RojasGonzalo007.aed-pseudocodigo` v0.12.1 |
| **Marketplace** | https://marketplace.visualstudio.com/items?itemName=RojasGonzalo007.aed-pseudocodigo |
| **Repositorio** | https://github.com/GonzaloRojas14/pseudocodigo_exe (público, MIT) |
| **Release** | https://github.com/GonzaloRojas14/pseudocodigo_exe/releases/tag/v0.12.1 |
| **Estado del código** | 199 tests unitarios + 17 de integración, todos en verde. Los cambios de la 0.12.2 están sin commitear |

### Qué hay en cada carpeta

| Carpeta | Archivos | Qué es |
|---|--:|---|
| `Campus/` | 10 | Material original bajado del aula virtual (docx, txt) |
| `Clases/` | 8 | Transcripciones de las clases 1 a 7 |
| `Filminas de Cátedra/` | 13 notas + PDF | Las 13 presentaciones 2026 del profesor (1-2 a 14), sus PDF en `PDF originales/`, imágenes en `img/` y las versiones viejas de 4, 5 y 6 en `versión anterior/` |
| `Guía de Cátedra/` | 111 | Los 275 ejercicios del sitio oficial + 78 resoluciones |
| `Práctica/` | 36 | Ejercicios propios, parciales, apuntes de clase |
| `Teoría/` | 9 | La teoría destilada: sintaxis, plantillas, trampas, apuntes en PDF |
| `Trabajo Práctico/` | 5 + carpeta | Actividades formativas N°2 (e-Commerce con IA) y N°3 (Estación de Monitoreo, en `AF3 - Estación de Monitoreo/`) |
| `aed-vscode/` | — | El código fuente de la extensión |

---

## 1. El material de cátedra

### 1.1 Libro de cátedra

`Teoría/Libro de Cátedra — Teoría completa.pdf` — 56 páginas, armado desde
`Libro_Algoritmos_y_Estructuras_de_Datos.docx` del repo `AEDUTNFRRe/Apuntes2026`.

**Verificado**: 10.737 de 10.737 palabras presentes; solo se agregaron 31 palabras
(la portada). No se inventó ni se resumió nada.

> **Hueco importante**: el libro **no tiene ningún capítulo sobre arreglos ni
> matrices**. Todo lo de la unidad 3 sale de las filminas, no del libro.

### 1.2 Guía de cátedra

Transcripción íntegra de https://aed-frre.github.io/ (bajada el 24/08/2026).
21 páginas, **275 ejercicios**, 5 de teoría.

| Sección | Unidad | Ejercicios |
|---|---|--:|
| Práctica | 0 — Algoritmos | 5 |
| Práctica | 1.1 — Datos y Estructuras Elementales | 41 |
| Práctica | 1.2 — Subacciones | 12 |
| Práctica | 2.1 — Secuencias | 32 |
| Práctica | 2.1 EXTRAS | 4 |
| Práctica | 2.2 — Archivos Secuenciales | 25 |
| Práctica | 2.3 — Archivos Indexados | 12 |
| Práctica | 3 — Arreglos | 32 |
| Práctica | 4 — Listas | 17 |
| Práctica | 5 — Recursividad | 28 |
| Práctica | X — Parcial | 1 |
| Complementarios | 1, 2.1, 2.2, 3, 4 | 66 |

Teoría de la guía: `Actualización.md`, `Arreglos.md`, `Corte de Control.md`,
`Listas.md`, `Mezcla.md`.

### 1.3 Resoluciones (de `Ejercicios.rar`)

83 notas de Obsidian con ejercicios resueltos, incorporadas el 23/09/2026 en
`Guía de Cátedra/Resoluciones/`, reorganizadas por unidad.

| Unidad | Resueltos | De un total de |
|---|--:|--:|
| 2.1 — Secuencias | 22 | 32 |
| 2.2 — Archivos Secuenciales | 25 | 25 |
| 2.3 — Archivos Indexados | 1 | 12 |
| 4 — Listas | 11 | 17 |
| 5 — Recursividad | 12 | 28 |
| 5.3 — Árboles | 5 | — |
| Actualización (extra) | 2 | — |
| Generados con IA (**no son de la cátedra**) | 5 | — |
| **1.1 / 1.2 / 3 (arreglos)** | **0** | **90** |

> **Leerlas con desconfianza.** Son apuntes personales de alguien que cursó, no
> material oficial. La mayoría está marcada `#InProgress` por el propio autor.
> Usan notación vieja al 100% (0 de 83 usan `FIN_SI`) y cosas que **no existen en
> ningún material de la cátedra**, como `finAmbiente` (en 72 de 83 archivos),
> `Entonces:` con dos puntos, `;` al final de sentencia, y `Romper`.
>
> **Ninguna corre en la extensión tal cual.** Se probó: de los 71 bloques con
> código completo, 0 pasan el checker. Aplicando 4 conversiones mecánicas
> (nombre de acción con guiones, `Procedimiento X():`, `finAmbiente`, `Entonces:`)
> pasan 8. El resto necesita trabajo a mano.

### 1.3b Campus — TEMA VI: Listas

`Campus/TEMA VI — Listas/` (bajado el 17/11/2026): las 4 presentaciones de Google enlazadas en la
sección (3.01 simples, 3.02 dobles y circulares, 3.03 pilas y colas, 12 "cómo borrar"), el
`.docx` de carga ordenada en circular simple y el código de listas del repo `UTN-FRRe/isi-aed`
(C, Python, pseudocódigo) con su traducción al pseudocódigo probada. Es la **única fuente de
inserción ordenada en circulares** (la del repo es correcta; la del `.docx` tiene dos errores).
Índice con erratas: `TEMA VI — Listas — Índice.md`.

### 1.4 Filminas

Las 13 presentaciones de teoría 2026 (carpeta *Presentaciones* del OneDrive del profesor, bajadas el
17/11/2026), transcriptas íntegras en `Filminas de Cátedra/`, una sección por página:
1-2 Introducción · 3 Secuenciales y Condicionales · 4 Arreglos · 5 Búsqueda y Ordenamiento ·
6 Procesos Estadísticos · 7 Listas · 8 Inserción y Eliminación · 9 Pilas y Colas · 10–11 Recursividad ·
12–13 Árboles · 14 Complejidad. Falta la `03` de listas (probablemente "Recorridos y Listas Circulares").
El índice de la carpeta tiene la tabla de erratas y la lista de notación que la extensión todavía no
acepta (`Accion X ES;`, `NILL`, `SI_NO`, `SINO SI` con un solo cierre, `numérico`/`alfanumérico`,
`Subaccion` sin `Proceso`, parámetro `arreglo [1..n]`).

---

## 2. La teoría destilada

Archivos en `Teoría/`, escritos a partir del material de cátedra.

| Archivo | Qué tiene |
|---|---|
| `SINTAXIS.md` | La referencia larga: tipos, estructuras, archivos, apareo, listas (§10), recursividad (§11) y lo que se sabe de árboles (pendiente) |
| `sintaxis-completa.md` | La referencia corta, en 14 secciones (13: punteros y listas, 14: recursividad) |
| `Listas — búsqueda e inserción.md` | Búsqueda e inserción en lista simple, doble, circular simple y circular doble: algoritmos, casos, trazas, errores típicos. Los 22 bloques se probaron en la extensión (104 corridas) |
| `plantillas.md` | 10 plantillas canónicas, listas para copiar |
| `errores-y-trampas.md` | Errores propios, bugs de las fuentes, trampas conceptuales |
| `Arreglos y Actualización — apunte completo.pdf` | 26 páginas, apunte de estudio |
| `SKILL — pseudocodigo-utn.md` | Instrucciones para escribir pseudocódigo correcto |

### 2.1 Las 10 plantillas

1. Recorrido de archivo secuencial
2. Corte de control
3. Mezcla inclusiva (con HV)
4. Mezcla exclusiva (con vaciado)
5. Actualización unitaria
6. Actualización por lotes
7. Actualización indexada (ABM interactivo)
8. Secuencias
9. Listas con punteros: recorrido, búsqueda, cargas apilada / encolada / ordenada, eliminación, circular
10. Recursividad: planteo formal + caso base + caso recursivo

Las 9 y 10 no vienen de `isi-aed` (no tiene listas ni recursividad): salen de la teoría de
listas de la guía, los Complementos Teóricos 2026 y lo resuelto en clase. Todas corren en
la extensión.

### Listas, recursividad y árboles

- **Listas** (`SINTAXIS.md` §10): notación de la cátedra (`Puntero a NODO`, `NIL`,
  `NUEVO`, `DISPONER`, `*p.dato`) con todas las variantes que aparecen en el material,
  las cargas con el nombre que les da la guía, listas dobles y circulares, pilas y colas.
- **Recursividad** (`SINTAXIS.md` §11): el **planteo formal** como se escribe en clase,
  las dos direcciones del índice sobre un arreglo, la prueba de escritorio en bajada y
  subida, los ejercicios resueltos y las trampas.
- **Árboles** (`SINTAXIS.md`, "Árboles — pendiente"): todavía no se pasó a la documentación.
  Fuentes: el Práctico 5 §5.3 de la guía y, desde el 17/11/2026, las filminas 12 y 13
  (notación completa: `nodo = registro … izq, der: puntero a nodo; fin_reg;`, recorridos, ABB). Un árbol binario
  ya corre en la extensión (registro con dos punteros + recursividad).

### 2.2 Las tres cosas que sostienen todo

**1. `FDA` no significa "el cursor llegó al final".** Significa **"el último LEER no
trajo nada"**. De ahí sale la lectura anticipada arriba y el `LEER` al final del
ciclo. Si el `LEER` va arriba, procesás un registro vacío; si hay uno solo, entrás
en loop infinito.

**2. Los registros se comparan campo por campo, en orden de declaración.** Por eso
una fecha va `anio, mes, dia` y el registro clave se declara en el mismo orden que
dice el "ordenado por" del enunciado.

**3. Los arreglos arrancan en 1.** El tamaño es `ls - li + 1`.

### 2.3 El esqueleto invariante

```
ACCION nombre ES
    Ambiente
        <registros> <archivos> <variables de trabajo> <subacciones>
    Proceso
        inicializar
        ABRIR E/(arch)
        LEER(arch, r)                ← LECTURA ANTICIPADA
        MIENTRAS NFDA(arch) HACER
            ...
            LEER(arch, r)            ← LEER AL FINAL DEL CICLO
        FIN_MIENTRAS
        cierre_final
        CERRAR(arch)
FIN_ACCION
```

Lo que cambia según el tipo de ejercicio:

| Tipo | Qué se agrega |
|---|---|
| Recorrido simple | nada |
| Corte de control | resguardos + comparar al **entrar** al ciclo |
| Proceso estadístico | una matriz; el cierre final es imprimirla |
| Secuencias | `ARR`/`AVZ`/`NFDS` en vez de `ABRIR`/`LEER`/`NFDA` |

### 2.4 Actualización: el armazón y la tabla

**Cinco subacciones, cuatro genéricas**: `leer_mae`, `leer_mov` (encapsulan el `HV`),
`paso_directo`, y las dos que cambian por ejercicio: `iguales` y `distintos`.

**El ciclo, siempre igual:**

```
MIENTRAS (reg_mae.cla.<1er campo> <> HV) O (reg_mov.cla.<1er campo> <> HV) HACER
    SI reg_mae.cla < reg_mov.cla  →  paso_directo ; leer_mae        (avanza UNO)
    SI reg_mae.cla = reg_mov.cla  →  iguales ; leer_mae ; leer_mov  (LOS DOS)
    SINO                          →  distintos ; leer_mov           (avanza UNO)
FIN_MIENTRAS
```

**La regla**: avanza el que se consumió.

**La tabla de seis celdas** — todo el ejercicio se reduce a esto:

| | Alta | Baja | Modificación |
|---|---|---|---|
| **Existe** (`mae = mov`) → `iguales` | ERROR | marcar/mudar y grabar | pisar campos y grabar |
| **No existe** (`mae > mov`) → `distintos` | crear y grabar | ERROR | ERROR |

Tres válidas en diagonal, tres errores. Si tu tabla no tiene tres errores, leíste mal.

**Secuencial vs indexada:**

| | Secuencial | Indexada |
|---|---|---|
| Archivos para el maestro | **dos**: `E/` y `/S` | **uno**: `E/S` |
| Genera maestro nuevo | sí, siempre | no, in situ |
| La baja | no copiar al nuevo | marcar `'*'` o `ELIMINAR`/`BORRAR` |
| `HV` | sí | no |

> **Regla práctica**: en secuencial, el maestro cuenta doble. Si el enunciado nombra
> tres archivos, declarás cuatro variables.

**Unitaria o por lotes** — cómo darse cuenta:

- **Buscá la frase.** Si dice *"solo existe un registro de movimiento para cada
  registro del maestro"* → unitaria. Si no dice nada, no lo asumas.
- El tercer criterio de orden en los movimientos **no alcanza** como señal: el 2.2.19
  ordena por `Farmacia, Medicamento y Cod_Mov` y aun así es unitaria.
- **Ante la duda, escribí por lotes.** Es un superconjunto: con un solo movimiento
  por clave el ciclo interno da una vuelta y sale. Al revés se rompe — el segundo
  movimiento cae en la rama de "registro inexistente".

### 2.5 Procesos estadísticos: la matriz con márgenes

De Filminas 6, lámina 9, textual:

> *"La matriz es de 51 × 31: 50 filas de bases de datos + una fila más de totales, y
> 30 columnas de problemas + una columna más de totales. La intersección final es el
> total general."*

**Los cuatro incrementos por registro** (paso 5 de la metodología):

```
T[fila, col] += valor     // la celda
T[fila, N]   += valor     // total de la fila
T[M, col]    += valor     // total de la columna
T[M, N]      += valor     // total general
```

**Corte de control vs proceso estadístico** — el criterio:

- **Corte**: el archivo está ordenado por lo que hay que totalizar. Acumuladores
  sueltos, se informa sobre la marcha, no importa cuántos grupos hay.
- **Estadístico**: hay que totalizar por criterios que **no están en el orden**, o
  cruzar dos a la vez. No se informa nada hasta terminar. Exige grupos **conocidos y
  finitos**.

---

## 3. Bugs encontrados en las fuentes

Documentados en `Teoría/errores-y-trampas.md`, sección B. Los dos más importantes
están **probados ejecutando**.

| | Dónde | Qué pasa |
|---|---|---|
| B.1 | Corte de control | llama al corte equivocado al final |
| B.2 | Corte de control | condición del filtro negada |
| B.3 | Secuencias | barridos invertidos |
| **B.4** | Actualización por lotes | falta `leer_mov` antes de entrar al lote: el propio movimiento de alta se reprocesa y dispara "ERROR - ALTA" |
| B.5 | — | plantillas a medio adaptar |
| **B.6** | Actualización unitaria | **el alta pisa el registro del maestro** |
| B.7 | — | errores menores dispersos |

### B.6, con el detalle porque es el más grave

La rama de alta armaba el registro nuevo **encima de `reg_mae`**. A esa rama se llega
cuando `reg_mae.clave > reg_mov.clave`, o sea cuando `reg_mae` **tiene un registro
del maestro válido y sin procesar**. Pisarlo lo destruye, y como ahí solo avanza
`leer_mov`, el registro corrupto sobrevive a la vuelta siguiente.

Ejecutado con 6 registros de maestro y 6 movimientos:

```
1  500  120     <- grabado dos veces
1  500  120
2  100   10     <- tenía 80, quedó con la cantidad del movimiento
2  100   10
(2, 400)        <- perdido, nunca se grabó
```

La solución: **un registro por archivo**. `reg_mae_act` para armar las altas,
`reg_mae` solo para leer. La plantilla de **lotes no tiene el problema** porque ya
usa `aux_mae`.

### El bug del parcial resuelto en clase

Documentado en `Práctica/Clase 4 — notas del parcial resuelto en clase.md`. Dos
errores probados por ejecución en la solución que el profesor escribió en el
pizarrón:

1. **El `i` global pisado por `busqueda`**: entra como mes 6 y vuelve valiendo 50.
2. **`pos_max := 1` adentro del ciclo**: informa "mes 1 con 10" en lugar de
   "mes 7 con 95".

Es el mismo patrón que B.6: una variable compartida que alguien sobreescribe
mientras otro todavía la necesita.

---

## 4. La extensión de VS Code

### 4.1 Qué es

Extensión que ejecuta el pseudocódigo de la cátedra tal cual, con botón de play,
errores marcados mientras se escribe, y archivos de datos al lado del algoritmo.

**No es un lenguaje "inspirado en"**: es la sintaxis exacta de la cátedra, con las
dos notaciones (moderna y vieja) y sin distinguir mayúsculas.

### 4.2 Arquitectura

**5428 líneas de TypeScript**, cuatro etapas:

```
texto  →  lexer  →  parser  →  checker  →  interpreter
          tokens    AST       diagnósticos   ejecución
```

| Módulo | Líneas | Qué hace |
|---|--:|---|
| `src/lexer.ts` | 548 | tokeniza; tabla de palabras clave con todas las variantes; normaliza lo que se pega de los PDF |
| `src/parser.ts` | 1121 | recursivo descendente; arma el AST; recuperación de errores que garantiza avanzar |
| `src/checker.ts` | 864 | pasada semántica sin ejecutar: variables no declaradas, campos inexistentes, ciclos que no entran |
| `src/interpreter.ts` | 1362 | recorre el árbol ejecutándolo; async para que `LEER` pueda esperar |
| `src/archivos.ts` | 547 | TSV/CSV ↔ registros; indexados; verificación del `ordenado por` |
| `src/extension.ts` | 501 | diagnósticos, CodeLens, comandos, la terminal |
| `src/ast.ts` | 318 | tipos de los nodos |
| `src/valores.ts` | 111 | `RecordVal`, `ArrayVal`, `Nodo`, `NIL`, `RuntimeError`, `formatValue` |
| `src/texto.ts` | 38 | utilidades de texto |
| `src/diagnostics.ts` | 18 | el tipo `Diagnostic` |

### 4.3 Los tres mecanismos que la hacen funcionar

**El intérprete es asíncrono.** Cuando el programa llega a un `LEER`, hace
`await host.readLine()` y esa promesa no se resuelve hasta que el usuario aprieta
Enter. Sin eso habría que bloquear el hilo y VS Code se congelaría.

**El `Host` es la frontera.** El intérprete no sabe qué es una terminal ni un archivo:

```typescript
interface Host {
  write(text: string): void;
  readLine(): Promise<string>;
  isCancelled?(): boolean;
  archivos?: SistemaDeArchivos;
}
```

En VS Code lo implementa la terminal; en los tests, un array en memoria. Por eso los
199 tests ejecutan pseudocódigo de verdad sin abrir un editor.

**Las celdas explican el `var`.** Cada variable vive en una `Cell`. Si la celda tiene
un `slot`, no guarda el valor: es un **alias** que lee y escribe en otro lado. Eso es
el pasaje por referencia.

**La terminal** es un `Pseudoterminal`: cuando el programa pide datos, guarda el
`resolve` de la promesa en `pendingRead` y dibuja el marcador `▸`. Cada tecla se
acumula en un buffer; con el Enter se llama a `resolve(linea)` y el `await` del
`LEER` se despierta. Maneja backspace, `Ctrl+C` y descarta las secuencias de escape
de las flechas.

**Contra los cuelgues**: un contador de pasos. A los 20 millones corta con un mensaje
que apunta a las causas típicas.

### 4.4 Qué cubre

**Anda todo el lenguaje hasta archivos**: `ACCION/Ambiente/Proceso`, todos los tipos
(`entero`, `real`, `caracter`, `logico`, `AN(n)`, `N(n)`, `N(e,d)`, subrangos,
enumerados), registros anidados, arreglos y matrices **de cualquier dimensión**
(probado hasta 4D), `SI`/`SEGUN`/`MIENTRAS`/`REPETIR`/`PARA`, funciones y
procedimientos con paso por valor y por `var`, **recursividad** (con tope de 10000
llamadas anidadas desde la 0.12.2), `ESCRIBIR`/`LEER`,
**archivos secuenciales**, **secuencias**, **archivos indexados**, **datos externos
por parámetro de la ACCION**, y desde la 0.12.0 **listas con punteros**.

Con eso corren: corte de control, mezcla inclusiva y exclusiva, actualización
unitaria e indexada y por lotes, procesos estadísticos, ABM indexados, y las listas
simples, dobles y circulares de la unidad 4.

**Verbos aceptados**, incluidas las variantes del material:

| Canónico | También acepta |
|---|---|
| `ESCRIBIR` | `ESC`, `GRABAR` |
| `ELIMINAR` | `BORRAR` |
| `ARR` / `AVZ` | `ARRANCAR` / `AVANZAR` |
| `NFDA` | `NOFDA` |
| `FIN_SI` / `Proceso` / `SINO` | `FinSi` / `Algoritmo` / `Contrario` |
| `ABRIR E/` | `ABRIRe`, `ABRIR E/S`, `ABRIRe/s` |
| `ABSO`, `TRUNC`, `REDOND`, `ASCII` | — |
| `PROCEDIMIENTO X(...) ES` | `Subacción X es; ... FSubacción;` · `Acción X (a: T): T es ... Faccion` (subacciones de la guía) |
| `verdadero` / `falso` | `V` / `F` (si no hay una variable con ese nombre) |
| `R = REGISTRO ...` | cualquier tipo con nombre: `vector = ARREGLO[1..N] de entero`, `punt = Puntero a NODO`, `dia = 1..31` |
| `FIN_REGISTRO` / `ABRIR E/(arch)` | `fin_reg` / `ABRIR E(arch)`, `ABRIR(arch)` (el Anexo de las actividades formativas) |
| `PROCEDIMIENTO X(a, b) ES` | `Procedimiento X(a: T; var b: T);` (parámetros con `;` y sin `ES`, como el Anexo) |
| `*p.dato` (nodo apuntado) | `p^.dato`, `p*.dato` (la guía escribe `P★.PROX`; el ★ pegado del PDF se acepta con aviso) |
| `ENTONCES` / `FIN_SI` / `FIN_MIENTRAS` / `FIN_REGISTRO` / `FIN_ACCION` | `Ent.` / `Fsi` / `Fmientras` / `Freg` / `Facción.` (Complementos Teóricos de la Guía de TP 2026) |
| `SEGUN x HACER` · `x EN (1, 2)` | `Según x` sin `HACER` · `x En [1 .. 5]` |
| `NIL` / `DISPONER(p)` | `NULO` / `BORRAR(p)` (la notación de `SINTAXIS.md`) |
| `FIN_SI`, `FIN_REGISTRO`, … | `FIN SI`, `FIN REGISTRO`, … (con espacio, como en las filminas de listas) |
| `// comentario` | `{ comentario }` entre llaves |

**Listas con punteros (0.12.0)**: `Puntero a NODO`, `NIL` (o `NULO`, como en
`SINTAXIS.md`), `NUEVO(p)`, `DISPONER(p)` (o `BORRAR(p)`: con un solo argumento libera el
nodo; con dos, `BORRAR(arch, reg)` sigue siendo la baja en el indexado), y
el nodo apuntado con `*p.dato` o `p^.dato`, anidado con paréntesis como en
`*(*p.ant).prox := q`. Se acepta la notación de las filminas tal cual: `{ CASO 1 }`,
`FIN SI;`, varias sentencias por línea con `;`, parámetros después del `ES`
(`ACCION ELIM ES(PRIM: Puntero a NODO);`) y nombres agrupados (`PRIM, ULT: ...`).

Cómo funciona por dentro: cada `NUEVO` crea un objeto `Nodo` en la memoria del
intérprete con una dirección simulada (`0x1000`, `0x1010`, …); el puntero **es** la
referencia a ese objeto, así que `p := q` hace que los dos apunten al mismo nodo.
`NIL` es un objeto único. `DISPONER` no borra el nodo: lo marca liberado para poder
avisar si alguien lo sigue usando. **Los nodos existen solo durante la ejecución.**

Errores que se explican: `*p` con `p = NIL`, nodo usado después de `DISPONER`, un dato
guardado en el puntero en vez de en el nodo, punteros comparados con `<`. El checker
avisa `p.dato` sin `*`, un `*` sobre algo que no es puntero, y el recorrido que se
olvida de avanzar con `p := *p.prox`.

**Verificado contra la Guía de Trabajos Prácticos 2026** (`Guía de Cátedra/Guía de Trabajos Prácticos 2026.pdf`, idéntica a `Práctica/guia-aed-frre.pdf`): los algoritmos LISTA_CIRCULAR y LISTA_DOBLE de los Complementos Teóricos (p. 63-66) corren transcriptos tal cual y quedan como tests (`test/fixtures/guia_*.frre`). La guía tiene tres errores que la extensión marca: LISTA_CIRCULAR usa `ANT` sin declararlo; LISTA_DOBLE declara `ant: punt;` (el tipo `punt` no existe) y en "Eliminar" le falta un `Fsi`. En los fixtures se corrigió lo mínimo, comentado. El ejercicio complementario 1 (p. 67, órdenes con `P★.PROX`) también corre y da lo que sale a mano.

Un detalle del lexer: un `*` al principio de una línea, pegado a un nombre, es
desreferencia (`*p.prox := nil`), no la continuación de una multiplicación.

### 4.5 Los datos

Carpeta `<ejercicio>.datos/` al lado del `.frre`. **Cada archivo se llama como la
variable declarada**, no como el tipo.

| Qué | Archivo | Formato |
|---|---|---|
| `ARCHIVO de registro` | `<var>.tsv` (o `<var>.csv`) | encabezado + una fila por registro, tabulaciones (o comas en el `.csv`); anidados aplanados con punto (`fecha.anio`) |
| `SECUENCIA` | `<var>.txt` | la cinta cruda, con espacios y marca de fin |
| Parámetro de la `ACCION`, arreglo de registros | `<param>.tsv` | igual que un archivo |
| Parámetro, arreglo de escalares o valor suelto | `<param>.txt` | un valor por línea |
| Parámetro, registro suelto (`N: NODO`) | `<param>.tsv` | encabezado + **una** fila |
| Parámetro `PRIM: Puntero a NODO` (la lista hecha) | `<param>.tsv` | encabezado con los campos del nodo **sin los punteros** + una fila por nodo, en el orden de la lista; se enlazan solos (`ant…` al anterior, el resto al siguiente). Solo el encabezado = lista vacía |
| Parámetro `ULT` en `(PRIM, ULT: Puntero a NODO)` | — | no lleva archivo: apunta al último nodo de la lista de `PRIM` |
| Lista **circular** por parámetro | `<param>.circular.tsv` | mismo contenido que `PRIM.tsv`; el último apunta al primero (en una doble, el `ant` del primero al último). El tipo no distingue una circular de una simple: lo dice la consigna, y se indica con el nombre del archivo. Si el nombre no coincide con cómo se recorre, el error sugiere el correcto |

Comando **"AED: Generar plantilla de datos"** (click derecho): lee el Ambiente y los
parámetros, crea la carpeta y un archivo por cada uno con los encabezados puestos. No
pisa lo que ya existe.

Los archivos de salida se escriben al `CERRAR`. Los **indexados persisten entre
corridas**. Si falta un archivo o una celda no cuadra con el tipo, corta y explica
dónde. Si se declaró `ordenado por`, **se verifica antes de arrancar**.

### 4.6 Historial de versiones

| Versión | Qué trajo |
|---|---|
| 0.1.0 – 0.3.0 | Núcleo del lenguaje, integración con VS Code, botón de play |
| 0.4.0 – 0.5.1 | Errores que explican en vez de señalar; avisos de ciclos que no entran |
| 0.6.0 | Distinguir función de procedimiento; endurecer rangos |
| 0.7.0 | **Archivos indexados** (fase 3) |
| 0.8.0 | Verificación del `ordenado por`; sin ruido binario en reales; CLI `npm run aed` |
| 0.8.1 | `LEER` en registro de otro tipo apunta a la declaración |
| 0.9.0 | **Las dos notaciones sin avisar**; claves de orden que son REGISTRO comparadas campo por campo |
| 0.9.1 | `arr`/`avz` solo son primitivas con paréntesis |
| 0.10.0 | `TRUNC`/`REDOND`; constantes como límite de arreglo; `EN` con conjunto literal |
| 0.11.0 | **La ACCION recibe datos externos por parámetro** |
| 0.11.1 | README con la autoría arriba y los datos explicados |
| 0.12.2 (sin publicar) | **Recursividad**: tope de 10000 llamadas anidadas con error claro (antes una recursión sin caso base se comía la memoria y colgaba VS Code); la notación de los ejercicios resueltos en clase (`: =`, `=>`, `arreglo (1..10)`, parámetro sin tipo) |
| 0.12.1 | La página explica las listas con punteros: cómo se escriben según la cátedra, qué pasa al ejecutar y qué errores explica |
| 0.12.0 (publicada el 22/10/2026) | **Listas con punteros**, incluidas las **circulares por parámetro** (`PRIM.circular.tsv`); `BORRAR` como sinónimo de `ELIMINAR`; registro suelto por parámetro; notación de las filminas de listas (`{ }`, `FIN SI`, parámetros después del `ES`); **dialecto del Anexo** de las actividades formativas (`fin_reg`, parámetros con `;`, `ABRIR(arch)`); datos en `.csv`; `ASCII(c)` |

### 4.7 Bugs de la extensión encontrados usándola

Todos salieron de ejercicios reales, no de tests sintéticos:

| Bug | Cómo apareció |
|---|---|
| Loop infinito del parser en recuperación de errores | crash por OOM |
| `(?i)` en `language-configuration.json` | inválido en regex de JS, VS Code descartaba las reglas de indentación en silencio |
| La terminal podía quedar vacía | escrituras dentro de `open()` se descartan |
| `sec` como palabra clave | rompía las plantillas canónicas — revertido |
| El demo preguntaba lo mismo para siempre | comparaba solo `'S'` mayúscula |
| Límites de arreglo invertidos | daba un error crudo de JS |
| **Claves de orden que son REGISTRO** | se comparaban como texto: el día 17 quedaba antes que el 3 |
| **`arr` como nombre de variable** | era palabra reservada; 8 errores que no mencionaban el problema |
| **Parámetros de la ACCION llegaban en cero** | se convertían en variables del Ambiente, en silencio |
| **`BORRAR` no existía** | la teoría de actualización indexada de la cátedra lo usa |

### 4.8 Reglas que resultaron ser invento nuestro

Documentado por honestidad:

> **"Nunca se recorre un indexado con `NFDA`"** — esa frase aparece **solo** en
> `Teoría/SINTAXIS.md`, que escribimos nosotros. **No hay prohibición explícita en
> ningún material primario de la cátedra.** Lo que sí hay: el libro (Cap. 6) dice que
> la organización indexada **soporta** acceso secuencial y mixto, y la teoría de
> actualización indexada **siempre** muestra acceso por clave con `EXISTE`. La
> extensión bloquea el recorrido, que es más estricto que lo que dice la cátedra.
> **Pendiente**: preguntarle al profesor.

### 4.9 Tests

**199 unitarios** (`npm test`) + **17 de integración** (`npm run test:vscode`, abre
VS Code de verdad en dos suites: con carpeta y archivo suelto). Los de listas están en
`test/listas.test.ts`; el de integración de listas corre el comando de plantillas con
`PRIM, ULT` y un registro suelto, completa los datos y ejecuta.

Lo que cubren:

- Los **cuatro patrones canónicos** end to end con salida exacta: mezcla inclusiva y
  exclusiva, actualización unitaria (con la regresión de B.6, verificando que el
  maestro salga sin duplicados ni pérdidas) y proceso estadístico (verificando que
  los márgenes cierren).
- Los **ejemplos que viajan en el `.vsix`**, ejecutados contra sus datos reales sobre
  una copia temporal. `corte_1000` verifica que los tres niveles sumen el general y
  que se procesen las 1000 ventas.
- Arreglos: binaria, selección, intercambio con la bandera, vectores paralelos, 3 y
  4 dimensiones.
- Recursividad (`test/recursividad.test.ts`): factorial, Fibonacci, MCD, binario,
  locales propias por llamada, el archivo de Práctica, los ejercicios de clase escritos
  como a mano, y el corte a las 10000 llamadas.
- Lenguaje: case-insensitivity, un programa entero en notación vieja, `arr` como
  arreglo conviviendo con `ARR(sec)`, `EN` en sus tres formas, `BORRAR`.
- Parámetros de la ACCION: arreglo de escalares, arreglo de registros, mensaje cuando
  faltan los datos, desajuste de tamaño.

### 4.10 Publicación

**Marketplace de Microsoft** — publicado el 27/09/2026.

El `vsce login` falló con `TF400813` aunque el token estaba bien: se verificó que el
token resolvía al perfil, que el publisher existía y estaba verificado, y que la API
del Marketplace le respondía 200. Es un bug del paso de verificación de `vsce login`,
no de la publicación. Se publicó pasando el token directo con `VSCE_PAT`.

> **Azure DevOps ya no es gratis sin tarjeta**: desde 2026 toda organización nueva
> tiene que estar linkeada a una suscripción de Azure. El plan gratuito sigue
> existiendo (5 usuarios, repos ilimitados), pero piden la suscripción igual para
> crear la organización. Las suscripciones **de estudiante** sirven y no piden
> tarjeta.

**GitHub** — repo público con MIT. Antes de publicarlo se limpió:

- una **ruta absoluta del disco** hardcodeada en `scripts/tm-check.cjs`
- la carpeta de **borradores personales** `ejemplos/pruebas/`, que estaba versionada
- `PUBLICAR.md`, el instructivo de publicación, purgado también del historial
- `scripts/md2pdf.py`, que era del apunte y no de la extensión

Se barrieron los 209 objetos del historial buscando credenciales: sin hallazgos.
También se sacó la línea `Co-Authored-By` de los 23 commits.

**Antigravity, Cursor, Windsurf y VSCodium no leen el Marketplace de Microsoft**:
usan Open VSX. Ahí la extensión **no aparece** buscando. Para esos editores hay que
instalar el `.vsix` del release. **Pendiente**: publicar en open-vsx.org, que se
entra con GitHub y no pide tarjeta.

---

## 5. Los ejercicios de `Práctica/`

| Archivo | Tema | Estado |
|---|---|---|
| `Actualizacion Parcial.frre` | Corte de control de 2 niveles (estaciones de carga VE) | resuelto por Gonzalo, corre |
| `Parcial — Circuitos y equipos.frre` | Proceso estadístico + consulta a indexado | resuelto, verificado contra Python |
| `Actualizacion 2.2.19 — Remedios.frre` | Actualización unitaria, clave compuesta, 3 archivos | resuelto, con la nota de B.6 |
| `Parcial — FIFA participaciones.frre` | Corte de control de 2 niveles + archivo de salida filtrado | resuelto, verificado |
| `Parcial — Santa Claus.frre` | Actualización **por lotes** (NIÑOS + EVENTOS) | en curso, lo resuelve Gonzalo |
| `Clase 4 para entender matrices.frre` | Final 04/03/2022, matriz de errores | solo la consigna — lo resuelve Gonzalo |
| `Eco-Rutas — revision de mi solucion.frre` | Revisión de la solución de Gonzalo al de circuitos | 3 bugs señalados |
| `Proceso Estadistico Parcial.frre` | — | — |
| `ejemplo_array.frre` | Búsqueda en arreglo de registros | de Gonzalo |
| `Clase 5 Listas.frre` | Notas de clase de listas: nodo, punteros, cargas apilada y encolada | apuntes de Gonzalo (el recorrido avanza con `*p.dato`: es el error #28) |
| `Recursividad.frre` | Teoría + ejercicios de clase: EsPar, Suma (guía 5.1.8), promedio de 10, promedio de aprobados, promedio de n hacia abajo | corre, verificado contra Python |
| `Recursividad — prueba de escritorio.frre` | La fórmula del promedio recursivo, mostrando la bajada y la subida | corre |
| `Recursividad — dígitos impares.frre` | Cantidad de dígitos impares de N, recursivo | corre, verificado contra Python |
| `Parcial 3 Tema A — Ej1 HackaTec.frre` | 3er parcial 2025, Tema A: secuencial + indexado → lista doble ascendente con desempate, top 3 desde ULT | corre, verificado a mano |
| `Parcial 3 Tema B — Ej1 Juegos Inter Carrera.frre` | 3er parcial 2025, Tema B: secuencial + indexado → lista simple descendente, conteo por equipo | corre, verificado a mano |
| `Patrón — Ejercicio 1 de listas (3er parcial).md` | Lo común de los tres ejercicios 1 (Empresa, Tema A, Tema B) y la receta para resolverlos | apunte |

### Notas de clase

- `Clase 1 — apuntes de arreglos.md`
- `Clase 2 — apuntes de procesos estadísticos.md`
- `Clase 4 — notas del parcial resuelto en clase.md` — el análisis del parcial que el
  profesor resolvió en el pizarrón, con los dos bugs probados por ejecución.

### Ejercicios de compañeros

`Ejercicios Rojas.md`, `Ejercicios Peralta.md`, `Ejercicios Brisaa.md`.

---

## 6. Decisiones tomadas y preferencias

### Sobre el pseudocódigo

- **Notación**: escribir en **moderna mayúsculas** (`FIN_SI`, `FIN_MIENTRAS`,
  `FIN_ACCION`). Pero las dos son válidas y **mezclarlas no es error** — los propios
  materiales de la cátedra las mezclan. La extensión no avisa nada.
- **Nada de procedimientos triviales**: lo que se puede hacer en el `Proceso`, va en
  el `Proceso`. Un procedimiento se justifica si se llama desde más de un lugar
  (`leer_mae`) o si encapsula una unidad conceptual grande (`iguales`, `distintos`).
  Una línea suelta llamada una vez, nunca.
- **Ambigüedades del enunciado**: elegir una interpretación y **dejar el comentario**
  diciendo qué se asumió. Eso no se descuenta; adivinar en silencio sí.

### Sobre cómo trabajamos

- Gonzalo **resuelve los ejercicios él**, salvo que pida explícitamente lo contrario.
  Cuando pide un ejercicio nuevo, va la consigna transcripta + los datos + las
  respuestas en un archivo aparte para contrastar.
- Todo lo que se afirma **se verifica ejecutando**, no de memoria. Los resultados se
  contrastan contra un cálculo independiente en Python.
- Los bugs de la extensión que aparecen usándola **se arreglan con test de regresión**.
- **No inventar**: en listas y recursividad se hace lo que dicen la teoría, la guía, lo
  resuelto en clase y los apuntes de Gonzalo. Si algo no está en esas fuentes, se pregunta.
- Lo resuelto en clase se pasa en limpio **sin corregirle la lógica**: si tiene algo
  dudoso (como el `>` / `>=` del promedio de aprobados), se deja como está y se señala.

### Sobre la publicación

- Autoría: **Rojas Gonzalo**, con Instagram, arriba de todo en el README.
- **No oficial**: aclarado en el README y en el mensaje de difusión. No está asociada
  ni respaldada por la UTN-FRRe.
- **Open source**: MIT. El archivo `LICENSE` y el campo del `package.json` se
  mantienen — sin eso, legalmente quedaría "todos los derechos reservados".

---

## 7. Lo que queda pendiente

| | Qué |
|---|---|
| **Cátedra** | Preguntar si un indexado se puede recorrer secuencialmente, y con qué notación |
| **Cátedra** | Confirmar la lectura del punto 3 del FIFA ("delanteros ≥ 15" es la suma del equipo) |
| **Extensión** | Publicar en **Open VSX** para Antigravity, Cursor y Windsurf |
| **Material** | Conseguir las líneas 1-36 del parcial que resolvió el profesor (el Ambiente) |
| **Tema** | **Árboles**: pasar a `SINTAXIS.md` la teoría y la notación de las filminas 12 y 13, armar la plantilla y probar los ejercicios del Práctico 5 §5.3 en la extensión |
| **Extensión** | Aceptar la notación de las filminas 2026 que hoy da error: `Accion X ES;`, `NILL`, `SI_NO`, `SINO SI` con un solo `FIN SI`, `numérico`/`alfanumérico`, `Subaccion` sin `Proceso`; decidir qué hacer con `(v: arreglo [1..n] de entero)` (ver índice de Filminas) |
| **Material** | Conseguir la presentación `03` de listas (Recorridos y Listas Circulares), que no está en la carpeta del profesor |
| **Extensión** | Aceptar `^` como "Y" lógico (`MIENTRAS (P <> NIL) ^ (*P.DATO < X)`, presentaciones 3.01 y 12 del campus): hoy lo toma como potencia |
| **Extensión** | Aceptar un **arreglo como campo de un registro de archivo** (`tecnologias: ARREGLO [1..5] de logico` dentro del registro de un secuencial o indexado): hoy corta con "no se puede guardar como columna". Lo piden los dos Ej 1 de los modelos de tercer parcial 2025 |
| **Cátedra** | Promedio de aprobados de clase: ¿aprueba con `> 6` o con `>= 6`? Quedó uno en cada caso |
| **Extensión** | Commitear y publicar la **0.12.2** (recursividad con tope, notación de los ejercicios de clase) |
| **Extensión** | Decidir qué mecanismos de listas por parámetro se quedan: `PRIM.tsv`, `ULT`, `PRIM.circular.tsv`, registro suelto `N.tsv` (los pensamos nosotros, no están en la teoría) |
| **Extensión** | Avisar cuando un parámetro tapa a una constante con el mismo nombre en otra mayúscula (`n` / `N`) |
| **AF3** | Revisar el PDF final de la Estación de Monitoreo antes de entregarlo |

---

## 8. Cómo retomar

**Correr los tests de la extensión:**
```bash
cd ~/Desktop/Estudios/Algoritmos/aed-vscode
npm test              # 199 unitarios
npm run test:vscode   # 17 de integración, abre VS Code
```

**Ejecutar pseudocódigo desde la terminal, sin abrir el editor:**
```bash
npm run aed -- check "../Práctica/mi_ejercicio.frre"
npm run aed -- run   "../Práctica/mi_ejercicio.frre" entrada1 entrada2
```

**Publicar una versión nueva:**
```bash
npx @vscode/vsce login RojasGonzalo007   # pide el token de Azure DevOps
npx @vscode/vsce publish patch           # sube el número y publica
```
Y después subir el `.vsix` como asset de un release nuevo en GitHub.

**Regenerar el apunte en PDF:**
```bash
python3 "Teoría/md2pdf.py" "Teoría/Arreglos y Actualización — apunte completo.md" \
  "Teoría/Arreglos y Actualización — apunte completo.pdf" \
  "Arreglos y Actualización de Archivos" "Apunte de estudio · AED · UTN-FRRe"
```
