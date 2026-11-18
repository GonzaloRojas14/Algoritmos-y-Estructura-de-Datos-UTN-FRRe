# Simulador Artemis — Situación 4 · Documento General del Proyecto

Este es el documento "mapa" del proyecto. Cada integrante tiene además su propio documento paso a paso:

## 1. Qué problema resuelve el programa

Una cápsula **Orion** (m = 10 400 kg) vuelve de la Luna y **reingresa a la atmósfera** a 120 km de altura y 11 000 m/s. El escudo térmico la frena por rozamiento hasta 25 m/s, a 2 500 m de altura, donde se abren los paracaídas. Finalmente **amerizaje** en el Pacífico a 8 m/s, hundiéndose 1,5 m.

El programa es una **simulación por consola** con menú. El usuario puede usar los datos oficiales o **ingresar sus propios 9 parámetros**, y el programa responde las 4 preguntas del enunciado:

| **Pregunta** | **Qué calcula** | **Fórmula** | **Dónde** |
|---|---|---|---|
| **A** | Trabajo de la fuerza de rozamiento | W = E_final − E_inicial, con E = ½·m·v² + m·g·h | `calcular_trabajo_rozamiento` |
| **B** | Desaceleración media durante el frenado (m/s² y en g) | a = (v_inicial − v_paracaídas) / Δt | `calcular_desaceleracion_media` |
| **C** | Fuerza promedio del agua al amerizar (N y múltiplos del peso) | F = ½·m·v² / d + m·g | `calcular_fuerza_amerizaje` |
| **D** | ¿Qué pasa si el ángulo de reingreso γ está fuera de 5,5° ≤ γ ≤ 7,0°? | γ < 5,5° ⇒ rebote; γ > 7,0° ⇒ desintegración | `ejecutar_simulacion_dinamica` |

Además hay una **simulación paso a paso (1 s por paso)** que llena una **"caja negra"** (arreglo de registros) con tiempo, altitud, velocidad y fuerzas G, y muestra el **pico máximo de G**.

### Los 9 parámetros de entrada (struct entradas)

| **Campo** | **Significado** | **Unidad** | **Valor oficial** | **Rango permitido (personalizada)** |
|---|---|---|---|---|
| `masa` | Masa de la cápsula | kg | 10 400 | 1 000 – 50 000 |
| `h_inicial` | Altitud al reingresar | m | 120 000 | 10 000 – 150 000 |
| `v_inicial` | Velocidad al reingresar | m/s | 11 000 | 1 000 – 20 000 |
| `angulo_reingreso` | Ángulo γ de reingreso | grados | 6,2 | 0,1 – 89,9 |
| `tiempo_frenado` | Duración de la fase de mayor desaceleración | s | 400 | 10 – 2 000 |
| `h_paracaidas` | Altitud de apertura de paracaídas | m | 2 500 | 100 – 50 000 |
| `v_paracaidas` | Velocidad al abrir paracaídas | m/s | 25 | 5 – 1 000 |
| `v_impacto` | Velocidad al tocar el agua | m/s | 8 | 0,1 – 500 |
| `hundimiento` | Distancia que se hunde en el agua | m | 1,50 | 0,1 – 20 |

**Coherencia física obligatoria** (validación cruzada): `h_paracaidas < h_inicial`, `v_paracaidas < v_inicial`, `v_impacto < v_paracaidas`.

## 2. Estructura de archivos

```text
Simulador Artemis/
├── main.c              ← Rol 4   (menú y coordinación)
├── simulador.h         ← Rol 4 lo arma, TODOS lo usan (contrato)
├── simulador.c         ← Rol 1 + Rol 2 + Rol 3 (cada uno en SU sección)
├── validaciones.h      ← Rol 1   (firmas)
├── validaciones.c      ← Rol 1   (lógica de entrada segura)
├── Makefile            ← Rol 4
├── README.md           ← Rol 4 (estructura) + todos (sus secciones)
├── .gitignore          ← Rol 4
├── pruebas/            ← cada rol agrega SU programa de prueba (test_rolN.c)
│   ├── test_rol1.c
│   ├── test_rol2.c
│   └── test_rol3.c
└── docs/               ← esta documentación
```

| **Archivo** | **Tipo** | **Responsabilidad** |
|---|---|---|
| `simulador.h` | Cabecera (contrato) | Constantes (`#define`), los 3 structs (`entradas`, `instante_vuelo`, `resultados`) y los **prototipos** de todas las funciones del simulador. |
| `validaciones.h` | Cabecera | Prototipos de `limpiar_buffer`, `pedir_double_seguro`, `pedir_entero_seguro`. |
| `validaciones.c` | Implementación | Lectura segura por teclado: nunca se cuelga ni acepta letras. |
| `simulador.c` | Implementación (motor) | Carga de misión, física analítica (A, B, C), simulación iterativa (D) y reportes. **Tiene 3 secciones, una por integrante.** |
| `main.c` | Punto de entrada | Declara **toda la memoria** (variables y arreglo) y ejecuta el menú. |

**Regla de oro de arquitectura:** ningún módulo de lógica lee del teclado directamente; todo pasa por `validaciones.c`. Y toda la memoria vive en `main`: los demás módulos reciben **punteros** a esa memoria.

## 3. Reparto de tareas

|  | **Integrante 1** | **Integrante 2** | **Integrante 3** | **Integrante 4** |
|---|---|---|---|---|
| **Rol** | Seguridad y carga de datos | Física estática y energía | Simulación dinámica y telemetría | Interfaz, integración y entrega |
| **Archivos** | `validaciones.c/.h` + sección 1 de `simulador.c` | Sección 2 de `simulador.c` | Sección 3 de `simulador.c` | `main.c`, `simulador.h`, `Makefile`, `README.md`, `.gitignore` |
| **Funciones** | `limpiar_buffer`, `pedir_double_seguro`, `pedir_entero_seguro`, `cargar_mision_historica`, `configurar_mision_personalizada` (**5**) | `calcular_trabajo_rozamiento`, `calcular_desaceleracion_media`, `calcular_fuerza_amerizaje`, `procesar_calculos_analiticos`, `mostrar_resultados_analiticos` (**5**) | `ejecutar_simulacion_dinamica`, `mostrar_telemetria`, `mostrar_reporte_completo` (**3**, una es la más difícil del proyecto) | `main`, `mostrar_menu`, `correr_simulacion` (**3**) + esqueleto + integración |
| **Dificultad** | Media (scanf, buffer, bucles) | Baja-media (fórmulas) pero escribe doc. de física | Alta (bucle de simulación, arreglos, punteros) | Media (flujo, Git, Makefile, pruebas finales) |
| **Aporte al README** | "Validaciones y reglas de entrada" | "Escenario Artemis y fórmulas A, B, C" | "Modelo de simulación, estados y limitaciones (D)" | Estructura, integrantes, compilación, registro de IA |
| **Parte del video (≈1 min c/u)** | Demo de validaciones con entradas erróneas | Explicación de A, B, C | Explicación del ciclo + caja negra + demo rebote/desintegración | Presentación, arquitectura, demo del caso exitoso |

**Equidad:** Rol 3 tiene el código más difícil; Rol 2 tiene menos líneas pero además redacta la parte física del README y arma los casos de prueba con cálculos manuales; Rol 4 tiene menos código pero carga con la integración, Git, Makefile y README. Cada rol tiene entre 3 y 5 funciones, tiene su programa de prueba y su sección de README.

## 4. Catálogo completo de funciones

Leyenda de punteros: `const X *p` = "puedo **leer** pero no modificar"; `X *p` = "puedo **modificar** lo que hay en la dirección".

| **#** | **Función** | **Archivo** | **Dueño** | **Entradas (parámetros)** | **Retorna** | **Quién la llama** |
|---|---|---|---|---|---|---|
| 1 | `limpiar_buffer` | `validaciones.c` | R1 | — | nada | #2, #3 |
| 2 | `pedir_double_seguro` | `validaciones.c` | R1 | `const char *mensaje`, `double min`, `double max` | `double` validado | #5 |
| 3 | `pedir_entero_seguro` | `validaciones.c` | R1 | `const char *mensaje`, `int min`, `int max` | `int` validado | `main` |
| 4 | `cargar_mision_historica` | `simulador.c` | R1 | `entradas *mision` | nada (modifica por referencia) | `main` (opción 1) |
| 5 | `configurar_mision_personalizada` | `simulador.c` | R1 | `entradas *mision` | nada (modifica por referencia) | `main` (opción 2) |
| 6 | `calcular_trabajo_rozamiento` | `simulador.c` | R2 | `const entradas *mision` | `double` (J, negativo) | #9 |
| 7 | `calcular_desaceleracion_media` | `simulador.c` | R2 | `const entradas *mision` | `double` (m/s²) | #9 |
| 8 | `calcular_fuerza_amerizaje` | `simulador.c` | R2 | `const entradas *mision` | `double` (N) | #9 |
| 9 | `procesar_calculos_analiticos` | `simulador.c` | R2 | `const entradas *mision`, `resultados *res` | nada (llena 3 campos de `res`) | `correr_simulacion` (main) |
| 10 | `mostrar_resultados_analiticos` | `simulador.c` | R2 | `const entradas *mision`, `const resultados *res` | nada (imprime A, B, C) | #13 |
| 11 | `ejecutar_simulacion_dinamica` | `simulador.c` | R3 | `const entradas *mision`, `instante_vuelo *caja_negra`, `resultados *res` | `int` = cantidad de filas cargadas | `correr_simulacion` (main) |
| 12 | `mostrar_telemetria` | `simulador.c` | R3 | `const resultados *res`, `const instante_vuelo *caja_negra`, `int cantidad_pasos` | nada (imprime D + tabla + pico G) | #13 |
| 13 | `mostrar_reporte_completo` | `simulador.c` | R3 | `const entradas *mision`, `const resultados *res`, `const instante_vuelo *caja_negra`, `int cantidad_pasos` | nada (imprime reporte entero) | `main` (opciones 1, 2, 3) |
| 14 | `mostrar_menu` (`static`) | `main.c` | R4 | — | nada | `main` |
| 15 | `correr_simulacion` (`static`) | `main.c` | R4 | `const entradas *mision`, `resultados *reporte`, `instante_vuelo *caja_negra` | `int` = pasos | `main` |
| 16 | `main` | `main.c` | R4 | — | `int` (0) | el sistema operativo |

`static` delante de una función en `main.c` significa "solo se puede usar dentro de este archivo", por eso no va en ningún `.h`.

## 5. Quién llama a quién

**Diagrama de llamadas (quién llama a quién):**

| **Función que llama** | **Funciones a las que llama** |
|---|---|
| main (R4) | mostrar_menu (R4); pedir_entero_seguro (R1); cargar_mision_historica (R1); configurar_mision_personalizada (R1); correr_simulacion (R4); mostrar_reporte_completo (R3) |
| configurar_mision_personalizada (R1) | pedir_double_seguro (R1) |
| pedir_double_seguro (R1) | limpiar_buffer (R1) |
| pedir_entero_seguro (R1) | limpiar_buffer (R1) |
| correr_simulacion (R4) | procesar_calculos_analiticos (R2); ejecutar_simulacion_dinamica (R3) |
| procesar_calculos_analiticos (R2) | calcular_trabajo_rozamiento (R2); calcular_desaceleracion_media (R2); calcular_fuerza_amerizaje (R2) |
| mostrar_reporte_completo (R3) | mostrar_resultados_analiticos (R2); mostrar_telemetria (R3) |

### Secuencia de una simulación (opciones 1 y 2)

**Secuencia de una simulación (en orden):**

1. Usuario → main (R4): elige opcion 1 o 2

2. main (R4) → validaciones (R1): pedir_entero_seguro

3. main (R4) → carga de mision (R1): cargar_mision_historica / configurar_mision_personalizada

4. carga de mision (R1) → main (R4): llena "mision_actual" (por puntero)

5. main (R4) → fisica A,B,C (R2): procesar_calculos_analiticos(mision, reporte)

6. fisica A,B,C (R2) → main (R4): llena trabajo, desaceleracion, f_impacto

7. main (R4) → simulacion D (R3): ejecutar_simulacion_dinamica(mision, caja_negra, reporte)

8. simulacion D (R3) → main (R4): llena caja_negra, estado_mision, mensaje; devuelve pasos

9. main (R4) → simulacion D (R3): mostrar_reporte_completo(...)

10. simulacion D (R3) → fisica A,B,C (R2): mostrar_resultados_analiticos

11. simulacion D (R3) → Usuario: imprime A, B, C, D, tabla y pico G

## 6. Flujo de datos y memoria

Las 3 estructuras se **declaran una sola vez en** `main` y viajan por **puntero**:

| **Estructura / variable** | **La declara** | **La escribe** | **La lee** |
|---|---|---|---|
| `entradas mision_actual` | `main` | R1 (`cargar_…`, `configurar_…`) | R2 (todas las `calcular_…`), R3 (`ejecutar_…`), `mostrar_*` |
| `resultados reporte_actual` → `trabajo_rozamiento`, `desaceleracion_media`, `f_impacto` | `main` | **R2** (`procesar_calculos_analiticos`) | R2 (`mostrar_resultados_analiticos`) |
| `resultados reporte_actual` → `estado_mision`, `mensaje_falla` | `main` | **R3** (`ejecutar_simulacion_dinamica`) | R3 (`mostrar_telemetria`) |
| `instante_vuelo caja_negra[1000]` | `main` | **R3** (`ejecutar_simulacion_dinamica`) | R3 (`mostrar_telemetria`) |
| `int pasos_registrados` | `main` | `main` (con lo que retorna R3) | `main` (se lo pasa a `mostrar_reporte_completo`) |
| `int mision_simulada` (bandera 0/1) | `main` | `main` | `main` (opción 3) |

**Orden obligatorio:** primero se llenan las `entradas` (R1), después se llama a `procesar_calculos_analiticos` (R2) y `ejecutar_simulacion_dinamica` (R3), y **recién ahí** se muestra el reporte.

## 7. Contrato: los archivos .h definitivos

Estos dos archivos son el **contrato**: todos programan contra ellos. Los crea/completa **el Integrante 4 en el Paso 0** y nadie los modifica sin avisar al grupo.

Tu `simulador.h` actual tiene los structs y 4 constantes, pero **le faltan** `VENTANA_ANGULO_MIN/MAX`, `PI`, `COEF_ARRASTRE_AREA`, los estados, y todos los prototipos. Reemplazalo por esto:

### simulador.h

```c
#ifndef SIMULADOR_H
#define SIMULADOR_H

/* ===== CONSTANTES FISICAS Y DE CONFIGURACION ===== */
#define LIMITE_ARREGLO 1000
#define GRAVEDAD 9.8
#define DENSIDAD_BASE 1.225
#define CONSTANTE_ALTURA 8500.0
#define VENTANA_ANGULO_MIN 5.5
#define VENTANA_ANGULO_MAX 7.0
#define PI 3.14159265358979323846
#define COEF_ARRASTRE_AREA 15.0

/* ===== CODIGOS DE ESTADO DE LA MISION ===== */
#define ESTADO_NOMINAL 1
#define ESTADO_DESINTEGRACION 2
#define ESTADO_REBOTE 3

/* ===== PARAMETROS DE LA SIMULACION Y DEL REPORTE ===== */
#define PASOS_ANTES_REBOTE 30   /* pasos de descenso antes de que la capsula rebote */
#define PASOS_TOTAL_REBOTE 60   /* pasos totales que se registran en un rebote */
#define FILAS_TABLA 20          /* filas aproximadas que se imprimen de la caja negra */

/* ===== ESTRUCTURA DE ENTRADAS ===== */
typedef struct{
    double masa;
    double h_inicial;
    double v_inicial;
    double angulo_reingreso;
    double tiempo_frenado;
    double h_paracaidas;
    double v_paracaidas;
    double v_impacto;
    double hundimiento;
} entradas;

/* ===== REGISTRO DE TELEMETRIA (una fila de la caja negra) ===== */
typedef struct{
    double t_actual;
    double h_actual;
    double v_actual;
    double fuerzas_g;
} instante_vuelo;

/* ===== REGISTRO DE RESULTADOS ===== */
typedef struct{
    double trabajo_rozamiento;
    double desaceleracion_media;
    double f_impacto;
    int estado_mision;
    char mensaje_falla[100];
} resultados;

/* ===== PROTOTIPOS ===== */
/* Rol 1 */
void cargar_mision_historica(entradas *mision);
void configurar_mision_personalizada(entradas *mision);

/* Rol 2 */
double calcular_trabajo_rozamiento(const entradas *mision);
double calcular_desaceleracion_media(const entradas *mision);
double calcular_fuerza_amerizaje(const entradas *mision);
void procesar_calculos_analiticos(const entradas *mision, resultados *res);
void mostrar_resultados_analiticos(const entradas *mision, const resultados *res);

/* Rol 3 */
int ejecutar_simulacion_dinamica(const entradas *mision, instante_vuelo *caja_negra, resultados *res);
void mostrar_telemetria(const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos);
void mostrar_reporte_completo(const entradas *mision, const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos);

#endif
```

### validaciones.h

```c
#ifndef VALIDACIONES_H
#define VALIDACIONES_H

void limpiar_buffer(void);
double pedir_double_seguro(const char *mensaje, double min, double max);
int pedir_entero_seguro(const char *mensaje, int min, int max);

#endif
```

## 8. Esqueleto inicial ("Paso 0")

Para que **los 4 puedan compilar desde el minuto cero** (aunque las funciones todavía estén vacías), el Integrante 4 sube a `main` el siguiente esqueleto con **cuerpos vacíos ("stubs")**. Cada integrante luego **reemplaza únicamente los cuerpos de sus funciones**.

El código de `main.c` y del `Makefile` está completo en el documento del Integrante 4. Acá van `validaciones.c` y `simulador.c` vacíos.

### validaciones.c (esqueleto)

```c
#include <stdio.h>
#include <stdlib.h>
#include "validaciones.h"

/* ============================================================
   ROL 1 - Validaciones  (ESQUELETO: reemplazar el cuerpo)
   ============================================================ */

void limpiar_buffer(void)
{
    /* TODO ROL 1 */
}

double pedir_double_seguro(const char *mensaje, double min, double max)
{
    (void)mensaje; (void)max;
    return min; /* TODO ROL 1 */
}

int pedir_entero_seguro(const char *mensaje, int min, int max)
{
    (void)mensaje; (void)min;
    return max; /* TODO ROL 1 (devuelve max=4 para que el menu de main termine y no se cuelgue) */
}
```

### simulador.c (esqueleto)

```c
#include <stdio.h>
#include <string.h>
#include <math.h>
#include "simulador.h"
#include "validaciones.h"

/* ============================================================
   ROL 1 - Carga de mision   (ESQUELETO: reemplazar los cuerpos)
   ============================================================ */

void cargar_mision_historica(entradas *mision)
{
    (void)mision; /* TODO ROL 1 */
}

void configurar_mision_personalizada(entradas *mision)
{
    (void)mision; /* TODO ROL 1 */
}

/* ============================================================
   ROL 2 - Fisica analitica (Puntos A, B y C)
   ============================================================ */

double calcular_trabajo_rozamiento(const entradas *mision)
{
    (void)mision;
    return 0.0; /* TODO ROL 2 */
}

double calcular_desaceleracion_media(const entradas *mision)
{
    (void)mision;
    return 0.0; /* TODO ROL 2 */
}

double calcular_fuerza_amerizaje(const entradas *mision)
{
    (void)mision;
    return 0.0; /* TODO ROL 2 */
}

void procesar_calculos_analiticos(const entradas *mision, resultados *res)
{
    (void)mision; (void)res; /* TODO ROL 2 */
}

void mostrar_resultados_analiticos(const entradas *mision, const resultados *res)
{
    (void)mision; (void)res; /* TODO ROL 2 */
}

/* ============================================================
   ROL 3 - Simulacion dinamica y telemetria (Punto D)
   ============================================================ */

int ejecutar_simulacion_dinamica(const entradas *mision, instante_vuelo *caja_negra, resultados *res)
{
    (void)mision; (void)caja_negra; (void)res;
    return 0; /* TODO ROL 3 */
}

void mostrar_telemetria(const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos)
{
    (void)res; (void)caja_negra; (void)cantidad_pasos; /* TODO ROL 3 */
}

void mostrar_reporte_completo(const entradas *mision, const resultados *res, const instante_vuelo *caja_negra, int cantidad_pasos)
{
    (void)mision; (void)res; (void)caja_negra; (void)cantidad_pasos; /* TODO ROL 3 */
}
```

`(void)variable;` le dice al compilador "sí, sé que este parámetro no se usa todavía" y evita warnings. **Se borra cuando escribas el cuerpo real.** Estas dos versiones del esqueleto fueron compiladas con `-Wall -Wextra -std=c99 -pedantic` sin errores ni advertencias.

## 9. Plan de trabajo y Git

La cátedra exige **múltiples commits de todos los integrantes** y recomienda ramas + Pull Requests. Plan:

### Fase 0 — Preparación (Integrante 4, ~30 min)

1. Crear el repositorio **público** en GitHub y agregar a los otros 3 como colaboradores.

2. Subir a `main`: `simulador.h`, `validaciones.h`, esqueletos de `validaciones.c` y `simulador.c`, `main.c`, `Makefile`, `.gitignore`, carpeta `docs/`.

3. Avisar al grupo: "Paso 0 listo, hagan `git clone` / `git pull`."

### Fase 1 — Desarrollo en paralelo (los 4 a la vez)

Cada uno trabaja **en su propia rama** y **solo toca lo suyo**:

| **Integrante** | **Rama** | **Archivos que toca** |
|---|---|---|
| 1 | `feature/rol1-validaciones` | `validaciones.c`, **sección ROL 1** de `simulador.c`, `pruebas/test_rol1.c` |
| 2 | `feature/rol2-fisica` | **sección ROL 2** de `simulador.c`, `pruebas/test_rol2.c` |
| 3 | `feature/rol3-simulacion` | **sección ROL 3** de `simulador.c`, `pruebas/test_rol3.c` |
| 4 | `feature/rol4-main` | `main.c`, `Makefile`, `README.md` |

Comandos básicos (ejemplo para el Integrante 1):

```bash
git clone <URL-del-repo>
cd <carpeta-del-repo>
git checkout -b feature/rol1-validaciones   # crea y entra a tu rama
# ... programás ...
git add validaciones.c
git commit -m "Rol1: implementa limpiar_buffer y pedir_double_seguro"
git push -u origin feature/rol1-validaciones
```

Hacer **commits chicos y frecuentes** (uno por función, mínimo). Cada documento de rol sugiere los mensajes de commit.

### Fase 2 — Integración

1. Cada uno abre un **Pull Request** hacia `main` desde GitHub. Otro integrante lo revisa y lo aprueba (esto cuenta como trabajo colaborativo).

2. **Orden de merge sugerido:** R1 → R2 → R3 → R4 (R4 al final, para probar todo junto).

3. Si Git avisa de **conflicto** en `simulador.c`: significa que dos personas tocaron líneas contiguas. Se abre el archivo, se buscan las marcas `<<<<<<<`, `=======`, `>>>>>>>`, se **deja el código de ambos**, se borran las marcas, se compila y se hace commit.

4. Tras cada merge: `git checkout main && git pull`, compilar y correr los casos de la sección 10.

### Fase 3 — Entrega

README completo, video, pruebas finales (ver sección 13).

### Compilación

```bash
make                 # usa el Makefile (recomendado)
./simulador_artemis

# o, sin make:
gcc -Wall -Wextra -std=c99 -pedantic main.c simulador.c validaciones.c -o simulador_artemis -lm
```

- `-lm` **va al final** y enlaza la librería matemática (`exp`, `sin`).

- Probar tu parte aislada (sin `main.c`): `gcc -I. pruebas/test_rolN.c simulador.c validaciones.c -o test_rolN -lm`.

- En Windows (MinGW) funciona el mismo `gcc`; el ejecutable queda como `simulador_artemis.exe`.

## 10. Casos de prueba de integración

Verificados contra una implementación de referencia completa del proyecto.

### Caso 1 — Misión histórica (menú 1)

| **Resultado** | **Valor esperado** |
|---|---|
| Punto A | `W_roz = -6.4117e+11 J  (-641.17 GJ)` |
| Punto B | `a_media = 27.44 m/s2  (2.80 g)` |
| Punto C | `F_prom = 323786.67 N  (3.18 veces el peso)` |
| Punto D | `MISION EXITOSA: ...` (estado 1) |
| Caja negra | 739 filas (t = 0 … 738 s); fila 0: h = 120000.0, v = 11000.00; última fila: h = 20892.6, v ≈ 25.01 |
| Pico G | `29.36 g a 41837.4 m de altitud (t = 70.0 s)` |

### Caso 2 — Ángulo 5,0° (rebote), resto de datos oficiales (menú 2)

Entradas: `10400, 120000, 11000, 5.0, 400, 2500, 25, 8, 1.5`

- A, B, C **idénticos al caso 1** (no dependen del ángulo).

- Estado 3: `REBOTE ATMOSFERICO: ...`; **60 filas**; la altitud baja hasta ≈ 91 252 m (t = 30) y **luego sube** hasta ≈ 118 968 m (t = 59).

- Pico G: `0.24 g a 91252.3 m (t = 30.0 s)`.

### Caso 3 — Ángulo 10° (desintegración)

Entradas: `10400, 120000, 11000, 10, 400, 2500, 25, 8, 1.5`

- Estado 2: `DESINTEGRACION: ...`; **467 filas** (última t = 466 s).

- Pico G: `47.71 g a 38580.7 m (t = 45.0 s)` → **mucho mayor** que el caso 1.

### Caso 4 — Validaciones (menú y modo personalizado)

| **Entrada** | **Dónde** | **Resultado esperado** |
|---|---|---|
| `hola` | menú | `[ERROR] Debe ingresar un numero entero...`, vuelve a pedir, **sin colgarse** |
| `9` | menú | `[ERROR] El valor debe estar entre 1 y 4.` |
| `2.5` o `1abc` | menú | `[ERROR] Ingreso caracteres extra despues del numero.` |
| `3` antes de simular | menú | `[AVISO] Todavia no hay datos. Ejecute primero la opcion 1 o 2.` |
| `-5` o `abc` | masa | error y vuelve a pedir |
| `h_inicial=20000` y `h_paracaidas=30000` | personalizada | `Incoherencia fisica: ... MENOR que la altitud inicial` y vuelve a pedir **solo ese dato** |
| `v_paracaidas=25` y `v_impacto=30` | personalizada | `Incoherencia fisica: ... MENOR que la de paracaidas` |
| Ctrl+D (fin de entrada) | cualquier prompt | Mensaje y el programa termina limpio (no bucle infinito) |

### Caso 5 — Tras una simulación, menú 3 muestra el mismo reporte sin recalcular.

## 11. Limitaciones del modelo (para el coloquio)

Es una **simulación simplificada**; hay que saber explicarlo si el tribunal pregunta:

1. **Sin sustentación ni gravedad en la ecuación de velocidad.** La cápsula real usa sustentación (reingreso "con rebote controlado") y logra picos de ~4 g. Este modelo es una **entrada balística** a ángulo constante: el pico de G sale ≈ 29 g incluso para un ángulo "exitoso". El pico depende casi solo de `v²·sen(γ)/(2·e·H)`, **no** de `COEF_ARRASTRE_AREA`.

2. **La simulación y los Puntos A, B no coinciden entre sí.** A y B usan los datos del enunciado (frenado de 400 s hasta 25 m/s a 2 500 m). El ciclo de integración usa arrastre exponencial: llega a 25 m/s a ≈ 20,9 km, no a 2,5 km. Son dos modelos distintos: analítico (balance de energía) vs numérico (paso a paso). Mejora posible: sumar el término de gravedad `+ GRAVEDAD * sin(rad) * dt` a `v`.

3. **Ángulo constante:** la trayectoria es una recta con ángulo γ fijo.

4. **Integración de Euler con dt = 1 s:** simple, con error numérico; alcanza con fines didácticos.

5. **Densidad exponencial:** `ρ = ρ₀ · e^(−h/H)` con H = 8 500 m.

6. **Rebote simplificado:** tras 30 pasos se invierte el sentido vertical y se registran 30 pasos más; no se modela el escape real.

7. **Límite de 1 000 filas:** con ángulos muy chicos (p. ej. 0,1° con v pequeña) el ciclo termina por `LIMITE_ARREGLO` en vez de por altitud/velocidad.

## 12. Entregables y video

**Repositorio público** (GitHub/GitLab) con: `.c` y `.h`, `Makefile`, historial de commits **de los 4 integrantes**, y **README.md** con: a) integrantes y comisión; b) descripción del escenario y reglas; c) breve detalle de funcionamiento; d) instrucciones de compilación y ejecución; e) **registro detallado del uso de IA** (herramienta, para qué, prompts, cómo se validó el código).

**Video ≤ 5 min**

| **Min** | **Quién** | **Contenido** |
|---|---|---|
| 0:00–0:45 | R4 | Presentación de los 4 integrantes + arquitectura (5 archivos, punteros y memoria en `main`) |
| 0:45–1:45 | R2 | Escenario y Puntos A, B, C con la ejecución oficial |
| 1:45–2:45 | R3 | Ciclo de simulación, caja negra, pico G, demo rebote (5°) y desintegración (10°) |
| 2:45–3:45 | R1 | Demo de validaciones: letras, fuera de rango, `12abc`, incoherencia física |
| 3:45–4:30 | R4 | Caso exitoso completo y cierre |

**Coloquio:** cualquiera puede ser elegido y  pueden pedir explicar **cualquier línea**. Por eso cada documento de rol termina con preguntas de práctica, y se recomienda que **cada uno lea el código de los demás** al menos una vez.

## 14. Reglas de equipo

1. **Solo editás tu sección.** Si necesitás cambiar un `.h` o una función ajena, avisá al grupo primero.

2. **Nombres exactos:** funciones, parámetros y campos tal cual están en este documento (si cambia uno, el programa de otro deja de compilar).

3. **Sin acentos ni** `ñ` en `printf` y comentarios.

4. **Compilá siempre con** `-Wall -Wextra -std=c99 -pedantic` y dejá **cero warnings**.

5. **Nada de** `scanf` **fuera de** `validaciones.c`**.**

6. **Comentá** cada función con 2–3 líneas (qué hace, qué recibe, qué devuelve).

7. **Commits chicos** con mensajes del estilo `RolN: qué hiciste`.

8. **Antes de abrir un PR:** `make clean && make` sin warnings y tu programa de prueba corre bien.

9. **Uso de IA:** anotá cada consulta (herramienta, prompt, qué te devolvió, qué cambiaste) **mientras trabajás**, para el README.

10. **Entender todo lo que subís.**
