---
tipo: filminas
materia: Algoritmos y Estructura de Datos
institucion: UTN FRRe
unidad: 6
titulo_original: Procesos Estadísticos — Clase — Arreglos bidimensionales aplicados a informes estadísticos
archivo_original: Procesos_Estadisticos_2026_2.pdf
diapositivas: 16
fuente: PDF publicado por la cátedra (carpeta Presentaciones, OneDrive del profesor)
tags:
  - AED
  - filminas
  - teoria
  - arreglos
  - matrices
  - archivos
  - procesos-estadisticos
---

# 6 — Procesos Estadísticos

> [!abstract] Qué es esta nota
> Transcripción **íntegra** de las 16 diapositivas de **Procesos Estadísticos — Arreglos bidimensionales aplicados a informes estadísticos** (Algoritmos y Estructuras de Datos 2026, UTN FRRe). El PDF original está en [[Procesos_Estadisticos_2026_2.pdf]] (carpeta `PDF originales/`).
> Las secciones siguen el número de **página del PDF** (1 a 16); el pie de cada diapositiva trae su propia numeración (02 a 13), porque dos diapositivas se repiten como ampliación del código.
> Con la presentación vinieron el programa [[estadistico.c]] y el archivo de datos [[ventas.csv]]: están transcriptos en los anexos del final.

> [!info] Cambios respecto de la versión anterior
> La versión anterior era otro PDF de 13 diapositivas: [[6 — Procesos Estadísticos (versión anterior)]] (PDF: [[6 — Procesos Estadísticos (filminas).pdf]]).
> - **Temas nuevos:** informe estadístico en tres etapas (Recopilación, Tratamiento, Divulgación), cuadro estadístico (filas y columnas, buen diseño, totalizadores), un **problema nuevo** (ventas de una semana, 5 sucursales × 7 rubros, matriz `A[1..6, 1..8]`), el algoritmo **ESTAD** en 5 pasos con su **AMBIENTE completo** (registro `Venta` con sub-registro `Fecha_Venta`), la comparación **pseudocódigo ↔ C**, un ejemplo ejecutado sobre `ventas.csv` y el material de la clase (`estadistico.c` y `ventas.csv`).
> - **Se sacó:** el cuadro de energía de Irlanda, los TIPS de cuándo aplicar procesos estadísticos (y el ejemplo de viajes), la **metodología de 7 pasos**, el escenario de **50 bases de datos × 30 problemas** (matriz 51 × 31) con su algoritmo, el uso de `HV` y los dos **problemas de repaso** (ventas de agosto e inmobiliaria).
> - **Notación:** cambió. Antes `Abrir E/(A)`, `Mientras NFDA(A) Hacer … FinMientras`, `FinPara`, `FinSi`, comentarios con `//` y sin punto y coma. Ahora `Abrir E(Arch);`, `Mientras No FDA(Arch) hacer … Fin_Mientras;`, comentarios entre `{ }`, `;` al final de cada sentencia, `Accion ESTAD ES; … Fin_Accion.` y `ARREGLO [1..6, 1..8] de Real;`.
> - **Erratas de la versión anterior:** ninguna sigue. La mezcla `M[51,J]` / `M[51,j]` desapareció junto con ese algoritmo, y la falta de `AMBIENTE` está resuelta: ahora la filmina declara el registro, el archivo, la matriz y `Lin`. Lo que la filmina sigue sin desarrollar son las subacciones `Poner_Cero_Arreglo`, `Mostrar_Arreglo` y `Mostrar_Salida_Solicitada` (ver página 10).

[[📽️ Filminas de Cátedra — Índice|← Volver a Filminas]] · [[💻 Algoritmos — Índice|← Materia]]

---

## 1 · Portada

ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE

**Procesos Estadísticos**

Clase — Arreglos bidimensionales aplicados a informes estadísticos

*Cuadro estadístico · Matriz · Totalizadores · Pseudocódigo y C*

---

## 2 · ¿Qué vamos a aprender hoy?

*OBJETIVOS DE LA CLASE*

1. **Informe y cuadro estadístico**
   Qué es un informe estadístico y cómo se organiza en un cuadro de filas y columnas.
2. **El problema de negocio**
   Ventas semanales de un comercio con 5 sucursales y 7 rubros, a partir de un archivo ordenado por Id.
3. **La matriz como estructura de datos**
   Representar el cuadro con un arreglo bidimensional, agregando fila y columna de totales.
4. **Del pseudocódigo al código en C**
   Implementar el algoritmo ESTAD y probarlo con un archivo de datos real (ventas.csv).

---

## 3 · ¿Qué es un informe estadístico?

*INFORME ESTADÍSTICO*

> [!important] Definición
> Es el conjunto de resultados cuantitativos que se obtienen de un proceso sistemático de recopilación, tratamiento y divulgación de datos primarios sobre hechos relevantes para el estudio de fenómenos demográficos, sociales y económicos.

| **R** — Recopilación | **T** — Tratamiento | **D** — Divulgación |
|---|---|---|
| Se reúnen los datos primarios: en nuestro ejemplo, cada renglón del archivo de Ventas. | Se procesan y organizan los datos, por ejemplo acumulándolos en una matriz por sucursal y rubro. | Se presentan los resultados en un cuadro claro, con totales que facilitan su lectura. |

---

## 4 · Filas, columnas y totalizadores

*CUADRO ESTADÍSTICO*

> [!important] Definición
> Es un arreglo de filas y columnas dispuesto de modo tal que se puedan presentar y organizar los datos, para clasificarlos, compararlos e interpretar las características de dos o más variables.

| **F** — Filas y columnas | **D** — Buen diseño | **T** — Totalizadores |
|---|---|---|
| Cada fila representa una categoría (sucursal) y cada columna, otra (rubro). | Un cuadro prolijo transmite la calidad del trabajo de recopilación y análisis previo. | Filas y columnas adicionales resumen el total por categoría y el total general. |

---

## 5 · Ventas de la semana por sucursal y rubro

*EL PROBLEMA*

Comercio mayorista con 5 sucursales. El archivo VENTAS contiene las operaciones de una semana, ordenado por Id.

| Campo | Tipo |
|---|---|
| `Id` | `N(9)` |
| `Cod_Prod` | `N(6)` |
| `Fecha_Venta` | `Fecha` |
| `Suc` | `N(2)  [1..5]` |
| `Rubro` | `N(2)  [1..7]` |
| `Cant` | `N(10,2)` |
| `Precio_Unitario` | `N(10,2)` |

> [!example] Se pide
> - ✓ Mostrar las ventas de la semana discriminadas por sucursal y rubro.
> - ✓ Informar la sucursal con mayor cantidad de ventas en la semana.
> - ✓ Informar la sucursal con menor cantidad de ventas en la semana.
> - ✓ Informar el rubro que más vendió en la semana.
> - ✓ Informar el total general de ventas de la semana.

---

## 6 · El cuadro como matriz A[Sucursal, Rubro]

*ARREGLOS BIDIMENSIONALES*

| Suc \ Rubro | Alm. | Beb. | Lác. | Pan. | Lim. | Cong. | Perf. | TOTAL |
|---|---|---|---|---|---|---|---|---|
| **Sucursal 1** | A[1,1] | A[1,2] | A[1,3] | A[1,4] | A[1,5] | A[1,6] | A[1,7] | **A[1,8]** |
| **Sucursal 2** | A[2,1] | A[2,2] | A[2,3] | A[2,4] | A[2,5] | A[2,6] | A[2,7] | **A[2,8]** |
| **Sucursal 3** | A[3,1] | A[3,2] | A[3,3] | A[3,4] | A[3,5] | A[3,6] | A[3,7] | **A[3,8]** |
| **Sucursal 4** | A[4,1] | A[4,2] | A[4,3] | A[4,4] | A[4,5] | A[4,6] | A[4,7] | **A[4,8]** |
| **Sucursal 5** | A[5,1] | A[5,2] | A[5,3] | A[5,4] | A[5,5] | A[5,6] | A[5,7] | **A[5,8]** |
| **TOTAL** | **A[6,1]** | **A[6,2]** | **A[6,3]** | **A[6,4]** | **A[6,5]** | **A[6,6]** | **A[6,7]** | **A[6,8]** |

(La celda `A[6,8]` está resaltada.)

> [!tip] Los totalizadores
> - **Columna 8** — Total general por sucursal (fila)
> - **Fila 6** — Total general por rubro (columna)
> - **A[6,8]** — Total general de ventas de la semana

---

## 7 · ESTAD, paso a paso

*EL ALGORITMO*

1. **Inicializar en cero**
   Poner_Cero_Arreglo: todas las celdas de A quedan en 0, incluidas las de totales.
2. **Leer el primer registro**
   Abrir el archivo VENTAS y leer el primer renglón (Reg).
3. **Acumular en la matriz**
   Sumar Cant × Precio_Unitario en A[Suc,Rubro] y en los totales de fila y columna.
4. **Repetir hasta fin de archivo**
   Leer el siguiente registro y repetir mientras No FDA(Arch).
5. **Mostrar resultados**
   Mostrar la matriz y la información pedida: extremos y total general.

---

## 8 · Acción ESTAD — declaración y estructura

*PSEUDOCÓDIGO*

```
Accion ESTAD ES;
Ambiente
  Venta = Registro
    Id: N(9);  Cod_Prod: N(6);
    Fecha_Venta = Registro
      Dia:1..31; Mes:1..12; Anio:N(4);
    Fin_Reg;
    Suc: 1..5;   Rubro: 1..7;
    Cant: Real;  Precio_Unitario: Real;
  Fin_Reg;

  Arch: archivo de Venta
          ordenado por Id;
  Reg: Venta;
  A: ARREGLO [1..6, 1..8] de Real;
  Lin: Real;
```

**Lectura del algoritmo**

- Venta es un registro con los mismos campos que un renglón del archivo, incluida Fecha_Venta como sub-registro.
- A es la matriz del cuadro estadístico: 6 filas (5 sucursales + TOTAL) por 8 columnas (7 rubros + TOTAL).
- Arch es el archivo de ventas, ya ordenado por Id (no hace falta ordenarlo en el algoritmo).
- Lin guarda el importe de cada renglón (Cant × Precio_Unitario) antes de acumularlo.

---

## 9 · Acción ESTAD — declaración (ampliación del código)

Ampliación a pantalla completa del código de la página 8 (mismo pie, 08):

```
Accion ESTAD ES;
Ambiente
  Venta = Registro
    Id: N(9);  Cod_Prod: N(6);
    Fecha_Venta = Registro
      Dia:1..31; Mes:1..12; Anio:N(4);
    Fin_Reg;
    Suc: 1..5;   Rubro: 1..7;
    Cant: Real;  Precio_Unitario: Real;
  Fin_Reg;

  Arch: archivo de Venta
          ordenado por Id;
  Reg: Venta;
  A: ARREGLO [1..6, 1..8] de Real;
  Lin: Real;
```

---

## 10 · Acción ESTAD — el proceso completo

*PSEUDOCÓDIGO*

```
Proceso
  Abrir E(Arch);
  Leer(Arch, Reg);
  Poner_Cero_Arreglo;

  Mientras No FDA(Arch) hacer
    Lin := Reg.Cant * Reg.Precio_Unitario;
    A[Reg.Suc, Reg.Rubro] := A[Reg.Suc, Reg.Rubro] + Lin;   { celda }
    A[Reg.Suc, 8]         := A[Reg.Suc, 8]         + Lin;   { fila  }
    A[6, Reg.Rubro]       := A[6, Reg.Rubro]       + Lin;   { columna }
    A[6, 8]               := A[6, 8]               + Lin;   { total   }
    Leer(Arch, Reg);
  Fin_Mientras;

  Mostrar_Arreglo;             { cuadro con sus totalizadores }
  Mostrar_Salida_Solicitada;   { máximos, mínimos y total     }
  Cerrar(Arch);
Fin_Accion.
```

> [!info] Lo que la filmina no desarrolla
> `Poner_Cero_Arreglo`, `Mostrar_Arreglo` y `Mostrar_Salida_Solicitada` se invocan pero no se escriben en pseudocódigo (tampoco se declaran sus índices). Su versión en C está en el anexo: `poner_cero`, `mostrar_arreglo` y `mostrar_salida_solicitada`.

---

## 11 · Acción ESTAD — el proceso completo (ampliación del código)

Ampliación a pantalla completa del código de la página 10 (mismo pie, 09):

```
Proceso
  Abrir E(Arch);
  Leer(Arch, Reg);
  Poner_Cero_Arreglo;

  Mientras No FDA(Arch) hacer
    Lin := Reg.Cant * Reg.Precio_Unitario;
    A[Reg.Suc, Reg.Rubro] := A[Reg.Suc, Reg.Rubro] + Lin;   { celda }
    A[Reg.Suc, 8]         := A[Reg.Suc, 8]         + Lin;   { fila  }
    A[6, Reg.Rubro]       := A[6, Reg.Rubro]       + Lin;   { columna }
    A[6, 8]               := A[6, 8]               + Lin;   { total   }
    Leer(Arch, Reg);
  Fin_Mientras;

  Mostrar_Arreglo;             { cuadro con sus totalizadores }
  Mostrar_Salida_Solicitada;   { máximos, mínimos y total     }
  Cerrar(Arch);
Fin_Accion.
```

---

## 12 · Misma lógica, distinta sintaxis

*DEL PSEUDOCÓDIGO AL CÓDIGO EN C*

**PSEUDOCÓDIGO**

```
A: ARREGLO [1..6, 1..8]
     de Real;
...
Lin := Reg.Cant *
       Reg.Precio_Unitario;

A[Reg.Suc, Reg.Rubro] :=
  A[Reg.Suc, Reg.Rubro] + Lin;
A[Reg.Suc, 8] :=
  A[Reg.Suc, 8] + Lin;
```

**C**

```c
static double A[7][9];
/* usamos 1..6 y 1..8;
   la fila y columna 0
   quedan sin usar */
...
double lin = reg.cant *
  reg.precio_unitario;

A[reg.suc][reg.rubro] += lin;
A[reg.suc][8]         += lin;
```

*La idea no cambia: se sigue acumulando en la celda [sucursal, rubro] y en sus dos totales. Sólo cambia la sintaxis de declaración e indexado (en C, arrancamos los índices en 0 y simplemente no usamos la fila/columna 0).*

---

## 13 · De ventas.csv al cuadro estadístico

*EJEMPLO COMPLETO*

**ventas.csv (extracto)**

```
Id,Cod_Prod,Dia,Mes,Anio,Suc,Rubro,Cant,Precio_Unitario
1,1013,17,8,2026,1,1,3.46,882.16
2,1078,17,8,2026,1,7,1.96,2567.52
3,1030,17,8,2026,1,3,2.03,1435.84
4,1018,17,8,2026,2,1,5.61,843.09
5,1054,17,8,2026,2,5,9.90,1013.14
...  (70 registros, una semana)
```

Ejecución: `./estadistico ventas.csv`

| Sucursal | Total ($) |
|---|---:|
| Resistencia | 113.913,40 |
| Barranqueras | 91.558,54 |
| Fontana | 92.641,53 |
| Pto. Vilelas | 122.021,10 |
| M. Belén | 140.872,33 |
| **TOTAL** | **561.006,89** |

| | |
|---|---|
| **Más vendió** | M. Belén — $ 140.872,33 |
| **Menos vendió** | Barranqueras — $ 91.558,54 |
| **Rubro top** | Perfumería — $ 134.123,30 |

> [!info] Comprobado
> Compilando `estadistico.c` y corriéndolo sobre `ventas.csv` salen exactamente estas cifras (totales por sucursal, total general, máximo, mínimo y rubro top).

---

## 14 · Código C y archivo de datos

*MATERIAL DE LA CLASE*

**C — `estadistico.c`**

Implementa el algoritmo ESTAD: lee ventas.csv, arma la matriz A[Sucursal, Rubro] y muestra el cuadro con los totales y la información pedida.

```
gcc -Wall -std=c99 \
  estadistico.c -o estadistico

./estadistico ventas.csv
```

**D — `ventas.csv`**

70 registros de ventas de una semana (17 al 23/08), 5 sucursales × 7 rubros, ordenado por Id, en formato CSV.

```
Id,Cod_Prod,Dia,Mes,Anio,
  Suc,Rubro,Cant,
  Precio_Unitario
```

Ver [[#Anexo — estadistico.c]] y [[#Anexo — ventas.csv]].

---

## 15 · Lo esencial de hoy

*SÍNTESIS*

1. **Un cuadro estadístico es una matriz**
   Filas y columnas representan variables; los totalizadores resumen la información.
2. **El algoritmo recorre el archivo una sola vez**
   Cada registro se acumula directamente en la celda [Suc, Rubro] y en sus totales.
3. **Pseudocódigo y C comparten la lógica**
   Cambia la sintaxis, no la idea: inicializar, acumular y mostrar.
4. **La matriz vive en memoria, el archivo en disco**
   Por eso conviene una sola pasada: leer, acumular y mostrar recién al final.

---

## 16 · Cierre

ALGORITMOS Y ESTRUCTURAS DE DATOS · UTN FRRE

**¡Eso es Procesos Estadísticos!**

Cerramos la aplicación de arreglos bidimensionales a informes estadísticos: cuadro, matriz, algoritmo y su implementación en C.

*Próxima clase: nuevas estructuras de datos*

---

## Anexo — estadistico.c

Archivo [[estadistico.c]], que vino junto con la presentación en la carpeta `PDF originales/`. Código completo, tal cual:

```c
/* ============================================================
   estadistico.c
   Algoritmos y Estructuras de Datos - UTN FRRe
   Procesos Estadisticos: cuadro estadistico con arreglo bidimensional

   Lee el archivo VENTAS (ventas.csv) y arma una matriz
   A[Sucursal, Rubro] con el total vendido ($) de la semana,
   agregando fila y columna de totales (igual que el pseudocodigo
   "Accion ESTAD" visto en clase).

   Compilar:  gcc -Wall -std=c99 estadistico.c -o estadistico
   Ejecutar:  ./estadistico ventas.csv
   ============================================================ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SUC_MAX   5   /* sucursales:      1..5           */
#define RUBRO_MAX 7   /* rubros:          1..7           */
#define FILA_TOT  (SUC_MAX + 1)    /* fila   de totales -> 6 */
#define COL_TOT   (RUBRO_MAX + 1)  /* columna de totales -> 8 */

typedef struct {
    long  id;
    int   cod_prod;
    int   dia, mes, anio;
    int   suc;
    int   rubro;
    double cant;
    double precio_unitario;
} Venta;

const char *nombre_sucursal[SUC_MAX + 1] = {
    "-", "Resistencia", "Barranqueras", "Fontana", "Pto. Vilelas", "M. Belen"
};

const char *nombre_rubro[RUBRO_MAX + 1] = {
    "-", "Almacen", "Bebidas", "Lacteos", "Panificados",
    "Limpieza", "Congelados", "Perfumeria"
};

/* Poner_Cero_Arreglo */
void poner_cero(double A[FILA_TOT + 1][COL_TOT + 1]) {
    for (int i = 1; i <= FILA_TOT; i++)
        for (int j = 1; j <= COL_TOT; j++)
            A[i][j] = 0.0;
}

/* Leer(Arch, Reg) — lee un renglon del CSV. Devuelve 0 al llegar a FDA. */
int leer_registro(FILE *arch, Venta *reg) {
    char linea[256];
    if (!fgets(linea, sizeof(linea), arch)) return 0;   /* FDA(Arch) */

    int leidos = sscanf(linea, "%ld,%d,%d,%d,%d,%d,%d,%lf,%lf",
                         &reg->id, &reg->cod_prod,
                         &reg->dia, &reg->mes, &reg->anio,
                         &reg->suc, &reg->rubro,
                         &reg->cant, &reg->precio_unitario);
    return (leidos == 9) ? 1 : leer_registro(arch, reg); /* salta lineas invalidas */
}

void mostrar_arreglo(double A[FILA_TOT + 1][COL_TOT + 1]) {
    printf("\n%-14s", "Sucursal/Rubro");
    for (int j = 1; j <= RUBRO_MAX; j++) printf("%12s", nombre_rubro[j]);
    printf("%12s\n", "TOTAL");

    for (int i = 1; i <= FILA_TOT; i++) {
        printf("%-14s", (i == FILA_TOT) ? "TOTAL" : nombre_sucursal[i]);
        for (int j = 1; j <= COL_TOT; j++)
            printf("%12.2f", A[i][j]);
        printf("\n");
    }
}

void mostrar_salida_solicitada(double A[FILA_TOT + 1][COL_TOT + 1]) {
    int suc_max = 1, suc_min = 1, rubro_top = 1;

    for (int i = 1; i <= SUC_MAX; i++) {
        if (A[i][COL_TOT] > A[suc_max][COL_TOT]) suc_max = i;
        if (A[i][COL_TOT] < A[suc_min][COL_TOT]) suc_min = i;
    }
    for (int j = 1; j <= RUBRO_MAX; j++)
        if (A[FILA_TOT][j] > A[FILA_TOT][rubro_top]) rubro_top = j;

    printf("\n--- Informe solicitado ---\n");
    printf("Sucursal con MAYOR venta en la semana : %-14s ($ %.2f)\n",
           nombre_sucursal[suc_max], A[suc_max][COL_TOT]);
    printf("Sucursal con MENOR venta en la semana : %-14s ($ %.2f)\n",
           nombre_sucursal[suc_min], A[suc_min][COL_TOT]);
    printf("Rubro con mayor venta en la semana    : %-14s ($ %.2f)\n",
           nombre_rubro[rubro_top], A[FILA_TOT][rubro_top]);
    printf("Total general de ventas de la semana  : $ %.2f\n",
           A[FILA_TOT][COL_TOT]);
}

int main(int argc, char *argv[]) {
    const char *nombre_archivo = (argc > 1) ? argv[1] : "ventas.csv";

    FILE *arch = fopen(nombre_archivo, "r");
    if (!arch) {
        fprintf(stderr, "No se pudo abrir el archivo %s\n", nombre_archivo);
        return 1;
    }

    char cabecera[256];
    fgets(cabecera, sizeof(cabecera), arch);   /* descarta encabezado del CSV */

    static double A[FILA_TOT + 1][COL_TOT + 1];
    poner_cero(A);

    Venta reg;
    while (leer_registro(arch, &reg)) {
        double lin = reg.cant * reg.precio_unitario;

        A[reg.suc][reg.rubro] += lin;   /* celda sucursal-rubro     */
        A[reg.suc][COL_TOT]   += lin;   /* total de la sucursal     */
        A[FILA_TOT][reg.rubro]+= lin;   /* total del rubro          */
        A[FILA_TOT][COL_TOT]  += lin;   /* total general            */
    }
    fclose(arch);

    printf("Cuadro estadistico - Ventas de la semana por Sucursal y Rubro\n");
    mostrar_arreglo(A);
    mostrar_salida_solicitada(A);

    return 0;
}
```

---

## Anexo — ventas.csv

Archivo [[ventas.csv]], que vino junto con la presentación en la carpeta `PDF originales/`.

- **Columnas (9):** `Id`, `Cod_Prod`, `Dia`, `Mes`, `Anio`, `Suc`, `Rubro`, `Cant`, `Precio_Unitario`. La fecha va partida en tres columnas (`Dia`, `Mes`, `Anio`), que corresponden al sub-registro `Fecha_Venta` del pseudocódigo.
- **Filas:** 70 registros más la línea de encabezado. Todos son de agosto de 2026, días 17 a 23; `Suc` va de 1 a 5 y `Rubro` de 1 a 7.
- **Primeras 5 filas:**

| Id | Cod_Prod | Dia | Mes | Anio | Suc | Rubro | Cant | Precio_Unitario |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1013 | 17 | 8 | 2026 | 1 | 1 | 3.46 | 882.16 |
| 2 | 1078 | 17 | 8 | 2026 | 1 | 7 | 1.96 | 2567.52 |
| 3 | 1030 | 17 | 8 | 2026 | 1 | 3 | 2.03 | 1435.84 |
| 4 | 1018 | 17 | 8 | 2026 | 2 | 1 | 5.61 | 843.09 |
| 5 | 1054 | 17 | 8 | 2026 | 2 | 5 | 9.90 | 1013.14 |

---

## 🔗 Notas relacionadas

- [[6 — Procesos Estadísticos (versión anterior)]] — la presentación anterior (13 diapositivas)
- [[4 — Arreglos]] · [[5 — Búsqueda y Ordenamiento]] — las presentaciones de arreglos
- [[Corte de Control]] · [[Actualización]] — teoría del sitio de la cátedra sobre procesamiento de archivos
- [[plantillas]] — las plantillas canónicas de procesamiento secuencial de archivos
- [[2.2 — Archivos Secuenciales]] — ejercicios de archivos de la Guía de Cátedra
